# NoSQL Families

> "NoSQL" is a set of different databases built for particular access patterns. Know the families, what each is good at, and what you give up: joins, general queries and often strong consistency. Model by access pattern, not by entities.

Roadmap topic 12 · Stage 4: Choosing & Scaling

**Go deeper:** `11` Choosing a Database · `13` Caching & Redis · `15` Partitioning & Sharding · `16` Consistency & CAP · `20` Analytics · `05-system-design/17-Choosing-a-Database` · `08-artificial-intelligence/06-Embeddings-and-Vector-Search` · `04-backend-engineering/01-Client-Server-and-Request-Flow` (backend-as-a-service).

**Marks:** 🟢 must know · 🟡 good to know · (New) still changing

**How the examples are checked:** the inverted-index and size examples are checked with Python; engine-specific syntax (CQL, MongoDB, DynamoDB, Redis, Firestore) is shown for the idea and not run.

---

#### 1. What Is It?

*The non-relational families and how to use them well.*

| 🟢 Must know | 🟡 Good to know |
|---|---|
| key-value stores (DynamoDB, Redis) | wide-column stores (Cassandra, Bigtable) |
| document databases (MongoDB, Firestore) | graph databases (Neo4j) |
| model by access pattern, not by entities | time-series databases |
| embed vs reference; the cost of duplicated data | search engines: inverted index, relevance |
| what you give up: joins, general queries, often strong consistency | (New) vector databases and vector search |
| | backends as a service (Firebase, Supabase) and their security rules |

1. **Key-value:** `key → value`, lookup by key only.
2. **Document:** `id → JSON-like document`, queries inside documents.
3. **Wide-column:** rows grouped by a partition key, sorted by a clustering key; tables designed per query.
4. **Graph:** nodes and relationships as first-class data.
5. **Time-series:** values over time, optimised for appends and range/aggregate queries.
6. **Search engine:** an inverted index for full-text and relevance.

**Signals in an interview:** "why DynamoDB?", "when would you use MongoDB?", "how do you model data in Cassandra?", "what do you lose with NoSQL?".

---

#### 2. How It Works

**The families at a glance.**

| Family | Examples | Great at | Weak at |
|---|---|---|---|
| Key-value | Redis, DynamoDB, Memcached | O(1) lookup by key, huge scale, caches, sessions | queries other than by key |
| Document | MongoDB, Firestore, CouchDB | flexible, nested data read as one unit | joins, multi-document transactions (improving), consistent duplicates |
| Wide-column | Cassandra, ScyllaDB, Bigtable, HBase | massive write throughput, predictable low latency at scale | ad-hoc queries, joins, changing access patterns |
| Graph | Neo4j, Neptune | deep relationship traversals (friends of friends, fraud rings) | bulk analytics, simple tabular data |
| Time-series | InfluxDB, TimescaleDB, Prometheus | metrics/events over time, downsampling, retention | general relational work |
| Search | Elasticsearch, OpenSearch, Solr | full-text, relevance, facets, fuzzy match | being the source of truth; transactions |
| Vector | pgvector, Pinecone, Weaviate, Qdrant | nearest-neighbour search on embeddings | exact queries, transactions (use alongside) |

**Model by access pattern, not by entities.** In a relational database you model *what things exist* (3NF) and write queries later. In most NoSQL stores you start from **the queries**, then shape the data so each query reads one partition or one document. The same data may be stored several times in different shapes, one per access pattern. Changing a query later may mean a new table and a backfill.

**Embed vs reference (documents).**

| | Embed (nested inside the document) | Reference (store an id) |
|---|---|---|
| Read | one read gets everything | extra lookups or application joins |
| Write | rewrite a growing document; duplicates to update | update one place |
| Consistency | atomic per document | across documents is harder |
| Use when | data is read together, bounded in size, owned by the parent (order lines in an order) | data is shared, large or unbounded, changes often (a user referenced by many comments) |

Duplicating data (the author's name in every comment) makes reads fast but each rename needs an update everywhere, with brief inconsistency. Duplicate only what rarely changes or can tolerate staleness.

**What you give up.** Joins (do them in the application or denormalise), general ad-hoc queries (only the patterns you designed), often strong consistency and multi-row transactions (many offer eventual consistency by default and limited transactions), and the maturity of SQL tooling. In return: scale-out, flexible schema, simple operations for a narrow workload.

🟡 **Wide-column stores.** Data is partitioned by the **partition key** (spread across nodes) and sorted within a partition by **clustering keys**. A table is designed per query; writes are cheap (LSM-based, topic 7); there are no joins. Good for time series, messaging, activity feeds at huge scale.

🟡 **Graph databases.** Store nodes and edges with properties and traverse relationships efficiently ("friends of friends of Ann who like jazz"). Use when the relationships *are* the question and depth is large; otherwise a relational join table is enough.

🟡 **Time-series databases.** Optimised for appending timestamped values, compressing, downsampling and expiring old data, and range aggregates ("average CPU per minute over a day").

🟡 **Search engines.** An **inverted index** maps each term to the documents that contain it. Query = look up terms, intersect/union lists, rank by relevance (BM25), plus facets and fuzzy matching. They are *derived* stores, fed from the source of truth, eventually consistent (seconds of lag).

🟡 **(New) Vector databases and vector search.** Store embeddings and find nearest neighbours (HNSW) for semantic search and RAG; often available inside existing databases (pgvector). Use alongside the source of truth, with metadata filters (`AI 6`).

🟡 **Backends as a service (Firebase, Supabase) and their security rules.** The app talks to the database directly (`BE 1` is the exception to "always through a backend"), so **security rules are the backend**: Firestore rules or PostgreSQL row-level security decide who may read/write each document or row. Write them as carefully as server code, test them, and never leave them open (`allow read, write: if true`).

---

#### 3. Naive vs Better Design

| Naive | Better |
|---|---|
| model NoSQL like a relational schema | start from the queries; one partition or document per read |
| a growing array inside one document | reference or bucket (split) unbounded data |
| duplicate frequently changing data everywhere | duplicate only stable data, or reference it |
| MongoDB/DynamoDB as the default for everything | PostgreSQL unless the access pattern says otherwise |
| the search index as the only copy | search is derived from the source of truth |
| open Firestore rules "for now" | per-user rules, tested |
| a hot partition key (`status='active'`) | a high-cardinality key that spreads load |

```javascript
// Naive: an unbounded array inside one document (a chat room) — the document grows without limit
{ "_id": "room1", "messages": [ /* millions of entries */ ] }
```

---

#### 4. SQL & Code

Document model: embed vs reference for an order (sizes: post 2,000 B, 50 comments × 300 B):

```json
{ "_id": "order-42", "userId": "u1", "status": "paid",
  "lines": [ { "sku": "A", "qty": 2, "priceCents": 500 }, { "sku": "B", "qty": 1, "priceCents": 1200 } ],
  "shipTo": { "city": "Berlin", "zip": "10115" } }
```

Order lines are embedded (read together, owned by the order, bounded). The user is referenced by `userId` (shared, changes independently). For a blog post with 50 comments of 300 B, embedding gives a `2,000 + 50 × 300 = 17,000` byte document read in one request; for a post that can collect 100,000 comments, reference the comments (bucket them) instead of embedding.

Key-value / DynamoDB-style single-table design (access patterns drive keys):

```text
Access patterns: (1) get a user  (2) list a user's notes, newest first  (3) get one note
PK            SK                         attributes
USER#u1       PROFILE                    name, email
USER#u1       NOTE#2025-03-04T10:00#n9   title, bodyRef          ← query PK = USER#u1 and SK begins_with "NOTE#" descending → pattern (2)
NOTE#n9       META                       userId, title           ← pattern (3) by id
```

Checks: pattern (2) is one query on one partition, sorted by the sort key; pattern (3) is a key lookup; there is no ad-hoc "all notes containing X": that needs a search index.

Wide-column (Cassandra CQL, a table per query):

```sql
CREATE TABLE messages_by_conversation (
  conversation_id uuid, sent_at timeuuid, sender_id uuid, body text,
  PRIMARY KEY ((conversation_id), sent_at)                -- partition = conversation; sorted by time inside it
) WITH CLUSTERING ORDER BY (sent_at DESC);
SELECT * FROM messages_by_conversation WHERE conversation_id = ? LIMIT 50;       -- the latest 50 messages: one partition read
```

Search: an inverted index in a few lines (Kotlin), checked on three documents `1: red running shoes`, `2: blue running jacket`, `3: red jacket`:

```kotlin
fun buildIndex(docs: Map<Int, String>): Map<String, Set<Int>> {
    val index = HashMap<String, MutableSet<Int>>()
    for ((id, text) in docs) for (word in text.lowercase().split(" ").filter { it.isNotBlank() }) index.getOrPut(word) { sortedSetOf() }.add(id)
    return index
}
fun search(index: Map<String, Set<Int>>, query: String): Set<Int> =
    query.lowercase().split(" ").map { index[it] ?: emptySet() }.reduce { a, b -> a intersect b }
```

Checks: `search(index, "running")` → `{1, 2}`; `search(index, "red jacket")` → `{3}`; `search(index, "green")` → `{}`. Real engines add tokenising, stemming, scoring (BM25) and sharding, but the core idea is this map from term to documents.

Keep search in sync (derived data):

```kotlin
// after a note is saved in PostgreSQL (source of truth), publish an event; a worker updates the index (eventually consistent, idempotent)
fun onNoteSaved(e: NoteSaved) = searchIndex.upsert(id = e.noteId, doc = mapOf("userId" to e.userId, "text" to e.text))
```

Firestore security rules (per-user access; not run):

```text
rules_version = '2';
service cloud.firestore {
  match /databases/{db}/documents {
    match /users/{uid}/notes/{noteId} {
      allow read, write: if request.auth != null && request.auth.uid == uid;      // only the owner
    }
  }
}
```

PostgreSQL row-level security for Supabase-style access (not run):

```sql
ALTER TABLE notes ENABLE ROW LEVEL SECURITY;
CREATE POLICY own_notes ON notes USING (user_id = auth.uid()) WITH CHECK (user_id = auth.uid());
```

Redis is a key-value store with data structures (topic 13). A document store inside PostgreSQL:

```sql
CREATE TABLE docs (id uuid PRIMARY KEY, data jsonb NOT NULL);
CREATE INDEX docs_type ON docs ((data->>'type'));            -- flexible documents with SQL, transactions and joins when needed
```

---

#### 5. Numbers & Limits

| Item | Rule of thumb |
|---|---|
| Document size | MongoDB max 16 MB; keep documents well under 1 MB; avoid unbounded arrays |
| DynamoDB item | max 400 KB; partition throughput limits (hot keys throttle) |
| Cassandra partition | keep under ~100 MB / 100,000 rows; choose keys that spread load |
| Key-value latency | single-digit milliseconds at scale; Redis sub-millisecond |
| Search lag | seconds between the database write and searchable |
| Duplication | each extra copy is another write and another place to be wrong |
| Joins | none (or limited): budget application-side joins |
| Consistency | many stores default to eventual; check per operation (`SD 23`) |

---

#### 6. Common Mistakes & Edge Cases

1. Choosing NoSQL "for scale" with no numbers.
2. Designing from entities instead of access patterns.
3. Unbounded arrays and hot keys.
4. Treating the search index or cache as the only copy.
5. Ignoring consistency defaults.
6. Open security rules in backends-as-a-service.
7. Adding a graph or vector database when SQL would do.
8. Changing access patterns after the data model is fixed, with no backfill plan.

Edge cases: a hot partition (one celebrity user); document growth after launch; transactions across documents; eventual consistency surprising users (read-your-writes); migration between families; backups and restores of distributed stores; limits that differ between managed offerings.

---

#### 7. Say This in the Interview

1. "NoSQL means several different families: key-value, document, wide-column, graph, time-series, search and vector. Each is built for specific access patterns."
2. "I model from the queries: in DynamoDB or Cassandra I design keys so each read hits one partition, and I may store the same data in more than one shape."
3. "Embed data that is read together and bounded; reference data that is shared, large or changes often."
4. "You give up joins, ad-hoc queries and often strong consistency, so I use NoSQL when the workload justifies it, and keep PostgreSQL as the default."
5. "Search engines and vector indexes are derived stores fed from the source of truth; backends as a service need carefully tested security rules."

---

#### 8. Quick Check

1. Name three NoSQL families and one use for each.
2. How does NoSQL modelling differ from relational modelling?
3. When do you embed vs reference?
4. Why not use a search engine as the primary store?

<details>
<summary>Answers</summary>

1. For example: key-value (sessions, caches), document (flexible records), wide-column (huge write volume), search (full-text), graph (relationships), time-series (metrics).
2. You start from the access patterns and shape the data per query, often duplicating it; relational starts from entities and normalises.
3. Embed what is read together, bounded and owned by the parent; reference what is shared, large or changing.
4. It is eventually consistent, lacks transactions and constraints, and can be rebuilt from the source of truth.

</details>

---

#### 9. Practice

**Interview questions**

1. When would you choose DynamoDB or MongoDB over PostgreSQL?
2. How do you model a chat in Cassandra? In DynamoDB?
3. What is an inverted index?
4. How do you keep a search index in sync with the database?
5. What do you give up with NoSQL?
6. How do you secure a Firebase/Supabase backend?

**Hands-on**

1. Model the notes app's three access patterns as a DynamoDB single table and as Postgres tables; compare.
2. Build the inverted index and add stemming (running → run).
3. Write Firestore rules or Postgres RLS policies for per-user notes and test that user B can't read user A's notes.

**Remember:** NoSQL = several families for specific patterns · model from the queries · embed what is read together, reference the rest · you lose joins, ad-hoc queries and often strong consistency · search and vector stores are derived · test the security rules · PostgreSQL stays the default.
