# Choosing a Database

Roadmap topic 17 · Stage 4: Scale

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** there is no best database. Pick one based on how your app reads and writes data, what it needs to guarantee, and how big it will get. Always explain why.

---

#### 1. Relational (SQL) — 🟢 Must Know

*The default choice. Start here unless you have a reason not to.*

1. Tables, relationships, joins, and **transactions (ACID)**.
2. Strong consistency and a flexible query language.
3. Examples: PostgreSQL, MySQL.
4. Best for: users, orders, payments, most business data.
5. Scales well with indexes, caching, and read replicas. Sharding is harder (topic `19`).

---

#### 2. Non-Relational (NoSQL) Types — 🟢 Must Know

| Type | Idea | Examples | Good for |
|---|---|---|---|
| **Key-value** | Look up a value by key | Redis, DynamoDB | Sessions, cache, simple lookups |
| **Document** | Store JSON-like documents | MongoDB | Flexible or nested data, quick changes |
| **Wide-column** | Huge tables spread across many machines | Cassandra | Very high write volume: messages, activity logs, time-series |

Trade-off: NoSQL often gives easier scaling and flexible data, but with **weaker joins and transactions** and query limits.

---

#### 3. How to Choose — 🟢 Must Know

Ask:

1. **Access pattern** — what queries do I run, and how often? By key? With joins? Ranges?
2. **Consistency and transactions** — do I need ACID (payments) or is eventual consistency fine (likes)?
3. **Scale** — data size, read and write QPS, growth.
4. **Data shape** — structured and related, or flexible?

```text
Payments / orders      → SQL
Session / cache        → Key-value (Redis)
Chat messages at scale → Wide-column or sharded SQL
Product catalog        → SQL or document
```

**Rule:** don't choose a database because it is popular. Say the requirement first, then the database.

---

#### 4. Real Systems Use Several Stores — 🟢 Must Know

*Polyglot persistence: each store for what it does best.*

```text
SQL database      → core data (users, orders)
Redis             → cache, sessions, rate limits
Object storage    → images, videos
Search engine     → full-text search
```

---

#### 5. Graph, Search, Time-Series — 🟡 Good to Know

1. **Graph database** — relationships are the main data (social graph, recommendations).
2. **Search engine** (Elasticsearch, OpenSearch) — full-text search and ranking.
3. **Time-series database** — metrics and sensor data over time.
4. Use them **in addition to** your main database, when a clear need appears.

---

#### 6. Common Interview Questions

1. **Which database for chat messages, and why?**
   Huge write volume, access by conversation and time → wide-column store (or sharded SQL). Say the access pattern first.
2. **SQL vs NoSQL?**
   SQL for related data and transactions. NoSQL for flexible data or massive scale with simple access patterns.
3. **Why not use one database for everything?**
   Different workloads fit different stores (cache, search, files). Use each where it is strong.
4. **When do you move away from SQL?**
   When measured scale or an access pattern can't be met with indexes, cache, replicas, or sharding.
5. **What is a key-value store good for?**
   Fast lookups by key: sessions, caches, counters.

---

#### 7. Common Mistakes

1. Picking a database because it is trendy.
2. Choosing NoSQL "for scale" with no scale problem.
3. Needing transactions on a database that doesn't support them.
4. Not saying **why** in the interview.
5. Using one store for everything.

---

#### 8. Related Topics

1. `08` Databases, SQL & Data Modeling (in `04-backend-engineering`)
2. `18` Replication
3. `19` Partitioning & Sharding
4. `23` Consistency & CAP

---

#### 9. Interview Must Remember

1. **Default to SQL.**
2. **Choose by access pattern, consistency needs, and scale.**
3. Know **key-value, document, wide-column** and their use cases.
4. Real systems use **SQL + Redis + object storage + search**.
5. **Always justify** the choice.
