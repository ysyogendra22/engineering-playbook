# NoSQL Families

Roadmap topic 12 · Stage 4: Choosing & Scaling

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** "NoSQL" isn't one thing — it's several genuinely different families of database, each built around a specific access pattern. Knowing the families, and what you give up by choosing one, matters more than memorising specific product names.

---

#### 1. Key-Value Stores — 🟢 Must Know

The simplest model: look up a value by its key, nothing more structured. Extremely fast, extremely simple. Examples: **DynamoDB**, **Redis** (also covered as a cache in topic `13`).

```text
GET user:42:session   →  { token: "...", expiresAt: ... }
```

---

#### 2. Document Databases — 🟢 Must Know

Store flexible, JSON-like documents — each document can have a different shape, and nested structures are natural. Examples: **MongoDB**, **Firestore**.

```json
{ "_id": "note1", "title": "Groceries", "tags": ["home", "urgent"], "items": [...] }
```

---

#### 3. Model by Access Pattern, Not by Entities — 🟢 Must Know

*The single biggest mental shift moving from relational to NoSQL modeling.*

In a relational database, you model entities and their relationships, then write whatever query you need. In most NoSQL databases, you design the **document or key shape around the specific queries you'll actually run** — modeling "the entities" without first knowing the access pattern often produces a shape that's expensive or impossible to query efficiently later.

---

#### 4. Embed vs Reference — 🟢 Must Know

```json
// Embed: the whole comment lives inside the post document
{ "post": "...", "comments": [{"author": "A", "text": "..."}] }

// Reference: the comment is a separate document, linked by ID
{ "post": "...", "commentIds": ["c1", "c2"] }
```

**Embedding** is fast to read (one lookup gets everything) but duplicates data and can bloat a document. **Referencing** avoids duplication but needs multiple lookups (or application-side joining, since most NoSQL databases don't join well) — choose based on the actual read/write pattern.

---

#### 5. What You Give Up — 🟢 Must Know

Compared to a relational database: **joins** (usually absent or limited), **general-purpose querying** (often limited to the access patterns you explicitly designed for), and often **strong consistency** (many NoSQL databases default to eventual consistency, `16`). Know this trade-off explicitly before choosing NoSQL for its scalability alone.

---

#### 6. Wide-Column Stores — 🟡 Good to Know

Designed for **huge write volume**, with a schema built around the specific queries that will run against it (similar spirit to item 3, taken further). Examples: **Cassandra**, **Bigtable**.

---

#### 7. Graph Databases — 🟡 Good to Know

Relationships **are** the main data, stored as first-class edges between nodes, optimised for traversing connections (friend-of-a-friend, recommendation graphs). Example: **Neo4j**.

---

#### 8. Time-Series Databases — 🟡 Good to Know

Optimised specifically for data points ordered by time — metrics, sensor readings, event logs — with efficient storage and querying for time-range queries and aggregation over time.

---

#### 9. Search Engines — 🟡 Good to Know

Built around the **inverted index** (a map from each word to the documents containing it — `03-leetcode-patterns`), relevance ranking, and faceting (filtering by multiple attributes at once). Examples: **Elasticsearch**, **OpenSearch**.

---

#### 10. Vector Databases (New) — 🟡 Good to Know

Store and search **embeddings** — numerical representations of meaning — for similarity search (`AI 6`). A newer category, increasingly used for AI features (semantic search, RAG); also increasingly available as an extension inside relational databases (`pgvector`) rather than always needing a dedicated product.

---

#### 11. Mobile Backend as a Service — 🟡 Good to Know

Firebase and Supabase look like the app talks to the database directly, but a managed API with security rules (Firebase) or row-level security (Supabase) actually sits in front — the app never gets raw database credentials (`BE 1`). Worth knowing these security rules **are** the authorization layer, and getting them wrong leaks data the same way a missing backend check would.

---

#### 12. Common Interview Questions

1. **What are the main NoSQL database families, and what's each good for?**
   Key-value (fast simple lookups), document (flexible, nested data), wide-column (huge write volume), graph (relationship traversal), time-series (data over time), search engines (full-text and faceted search).
2. **How is modeling data for NoSQL different from relational modeling?**
   You design the document/key shape around your specific queries up front, rather than modeling entities generically and writing whatever query you need later — access pattern comes first.
3. **Embed or reference — how do you decide?**
   Embed when the nested data is almost always read together with its parent and doesn't grow unbounded. Reference when the data is large, shared across parents, or needs independent querying.
4. **What do you give up by choosing a NoSQL database over relational?**
   Usually joins, general-purpose ad hoc querying, and often strong consistency — a real trade-off, not a strictly "better" choice, made for a specific reason.

---

#### 13. Common Mistakes

1. Treating "NoSQL" as one interchangeable category instead of several distinct families.
2. Modeling a document database the same way you'd model relational entities, without considering access patterns.
3. Choosing NoSQL purely for "scale" without a real, measured requirement that relational couldn't meet.
4. Misconfigured Firebase/Supabase security rules, effectively exposing the database despite looking like it's "protected" by the SDK.

---

#### 14. Related Topics

1. `11` Choosing a Database — the decision process this topic feeds into
2. `2` Relational Model & Data Modeling — the contrast point for "model by access pattern"
3. `AI 6` Embeddings & Vector Search — vector databases in full depth
4. `BE 1` Client-Server Request Flow — Firebase/Supabase's real security model

---

#### 15. Interview Must Remember

1. **NoSQL is several distinct families**, not one thing — key-value, document, wide-column, graph, time-series, search.
2. **Model by access pattern**, not by entities alone.
3. **Embed for speed and simplicity; reference to avoid duplication and support independent queries.**
4. **You give up joins, general querying, and often strong consistency** — know the trade-off.
