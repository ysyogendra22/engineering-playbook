# Databases: Learning & Interview Roadmap

Schema design, SQL, how databases work inside, and interview answers. `BE 8–11` and `SD 17–19` already teach the essentials — this is the **deeper, dedicated pass**: internals, MVCC, migrations, Redis, analytics, on-device.

- **Numbering:** own, 1–23.
- **References:** `7` = this folder · `BE 8`/`SD 17`/`ARCH 9`/`AI 6` = topic N in that roadmap
- **Marks:** 🟢 must have · 🟡 good to have · (New) for a mobile engineer, or still changing

---

## Index

| #   | Topic                                     | Stage                     |
| --- | ----------------------------------------- | ------------------------- |
| 1   | Database Basics & Landscape               | 1. Foundations            |
| 2   | Relational Model & Data Modeling          | 1. Foundations            |
| 3   | SQL Fundamentals                          | 1. Foundations            |
| 4   | Advanced SQL                              | 1. Foundations            |
| 5   | Indexes                                   | 2. Performance            |
| 6   | Query Performance & Execution Plans       | 2. Performance            |
| 7   | Storage Engines & Internals               | 2. Performance            |
| 8   | Transactions & ACID                       | 3. Correctness            |
| 9   | Concurrency & Isolation                   | 3. Correctness            |
| 10  | Schema Migrations & Evolution             | 3. Correctness            |
| 11  | Choosing a Database                       | 4. Choosing & Scaling     |
| 12  | NoSQL Families                            | 4. Choosing & Scaling     |
| 13  | Caching & Redis                           | 4. Choosing & Scaling     |
| 14  | Replication & High Availability           | 4. Choosing & Scaling     |
| 15  | Partitioning & Sharding                   | 4. Choosing & Scaling     |
| 16  | Consistency, CAP & Distributed Data       | 4. Choosing & Scaling     |
| 17  | Backup, Recovery & Data Migration         | 5. Operating              |
| 18  | Database Security & Privacy               | 5. Operating              |
| 19  | Operations & Monitoring                   | 5. Operating              |
| 20  | Analytics, Warehouses & Data Pipelines    | 6. Beyond the App Database |
| 21  | Mobile Databases (New)                    | 7. Mobile                 |
| 22  | Database Interview Answer Points (New)    | 8. Interview & Practice   |
| 23  | Practice: Projects & Exercises            | 8. Interview & Practice   |

**Short on time:** 1, 2, 3, 5, 6, 8, 9, 11, 14, 15, 21, 22. 🟢 items only.

**Engines to learn first:**

| Level | Engine | Why |
|---|---|---|
| Learn well | **PostgreSQL** (MySQL is similar) | The usual default for app backends. Most concepts here use it |
| Learn well | **SQLite** | The database inside your phone apps (topic 21) |
| Know the basics | **Redis** | Caching, counters, rate limits, queues (topic 13) |
| Know the ideas | One document database (MongoDB or Firestore), one key-value store (DynamoDB), one wide-column store (Cassandra), one search engine (Elasticsearch or OpenSearch) | Enough to explain when and why (topic 12) |

**Glossary:** the terms to learn first are listed at the end, each with a priority mark and the topic that explains it.

---

# What to Follow on Any Project

*The same ten steps work for a new app, a new feature, or a redesign. Keep each output short and write it down.*

| Step | Question to answer | Output |
|---|---|---|
| 1. List the data and the questions | What things do we store? Which reads and writes happen most? How much data, how many requests? | Entity list, top 10 queries, read/write ratio, size estimate |
| 2. Pick the store | Is a relational database enough? Is there a clear reason for something else? | A default choice and a written reason for any exception (topics 11, 12) |
| 3. Model the data | What are the tables, keys, and relationships? | Schema in about third normal form, and an ER diagram (topic 2) |
| 4. Put rules in the database | Which rules must never break, whatever the app does? | Types, `NOT NULL`, unique, foreign key, and check constraints (topics 2, 8) |
| 5. Plan the queries and indexes | Which queries must be fast? | Index for each key query, checked with `EXPLAIN` (topics 5, 6) |
| 6. Handle concurrency | What if two users act at once, or a request repeats? | Transaction boundaries, unique constraints, locks or version columns (topics 8, 9) |
| 7. Plan schema change | How will the schema change while the app is live and old app versions still run? | Versioned migrations, expand-and-contract steps (topic 10) |
| 8. Plan for growth | What happens at 10× data or traffic? | Order of fixes: index, cache, read replica, partition, shard (topics 13–15) |
| 9. Protect and recover | Who can access what? Can we restore? | Least-privilege users, encryption, a tested backup and restore (topics 17, 18) |
| 10. Watch it | How will we know it is slow or failing? | Slow-query log, connection and lag dashboards, alerts (topic 19) |

**Priority order when time is short:** steps 1, 3, 5, and 6. Most database trouble comes from a schema that does not match the queries, a missing index, and two requests changing the same row.

**Default rule:** start with one relational database such as PostgreSQL. Add a cache, replicas, or another store only when a measured problem asks for it.

---

# Stage 1: Foundations

## 1. Database Basics & Landscape

- 🟢 What a database does: store data safely, find it fast, and keep it correct
- 🟢 DBMS, database, table, row, column, schema, query
- 🟢 Relational vs non-relational, at a glance (topic 11)
- 🟢 Client–server database vs embedded database (PostgreSQL vs SQLite)
- 🟢 OLTP vs OLAP: everyday transactions vs large-scale analysis
- 🟢 Why the app talks to a database only through a backend (`BE 1`)
- 🟡 A short history: why so many kinds of databases exist
- 🟡 SQL dialect differences (PostgreSQL, MySQL, SQLite)
- 🟡 Managed database services vs running your own

## 2. Relational Model & Data Modeling

- 🟢 Primary key, foreign key, unique key, composite key
- 🟢 Surrogate keys (IDs) vs natural keys (email) (`SD 20`)
- 🟢 Relationships: one-to-one, one-to-many, many-to-many (join table)
- 🟢 Design the schema from the queries you need (`BE 8`)
- 🟢 Normalization: first, second, third normal form, in plain words
- 🟢 Denormalization: copy data on purpose, and what it costs
- 🟢 Constraints: `NOT NULL`, `UNIQUE`, foreign key, `CHECK`
- 🟢 Data types: money as integers or decimals, time in UTC, text vs enum
- 🟢 `NULL`: what it means, and why `= NULL` does not work
- 🟡 ER diagrams
- 🟡 Soft delete vs hard delete
- 🟡 Audit columns: `created_at`, `updated_at`, `created_by`
- 🟡 Modeling trees, hierarchies, tags, and history

## 3. SQL Fundamentals

- 🟢 `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`
- 🟢 `INSERT`, `UPDATE`, `DELETE`, and why `UPDATE` without `WHERE` is dangerous
- 🟢 Aggregates: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- 🟢 `GROUP BY` and `HAVING`
- 🟢 Joins: inner, left, right, full, and cross
- 🟢 Subqueries and `EXISTS`
- 🟢 Pagination: `OFFSET` vs keyset (cursor) pagination (`BE 3`)
- 🟢 Parameterized queries (never build SQL from strings)
- 🟡 Upsert (`INSERT ... ON CONFLICT`)
- 🟡 Set operations: `UNION`, `INTERSECT`, `EXCEPT`
- 🟡 Bulk insert and batching
- 🟡 Reading and writing SQL that others can read

## 4. Advanced SQL

- 🟢 CTEs (`WITH`) for readable queries
- 🟢 Window functions: `ROW_NUMBER`, `RANK`, running totals, `LAG` and `LEAD`
- 🟢 `CASE` expressions
- 🟢 Common patterns: top N per group, latest row per user, deduplication, gaps and islands
- 🟡 Recursive CTEs (trees and graphs)
- 🟡 Views and materialized views
- 🟡 Stored procedures, functions, and triggers: when they help, when they hurt
- 🟡 JSON columns and JSON queries in a relational database
- 🟡 Full-text search inside the database
- 🟡 Generated columns and computed values

---

# Stage 2: Performance

## 5. Indexes

- 🟢 What an index is, and full table scan vs index lookup
- 🟢 B-tree index: the default, and why it fits equality and range queries
- 🟢 The cost: slower writes and more storage
- 🟢 Composite index: column order and the leftmost rule
- 🟢 What to index: `WHERE`, `JOIN`, `ORDER BY` columns and foreign keys
- 🟢 Why an index is not used: functions on the column, leading wildcard, type mismatch, low selectivity
- 🟡 Covering index and index-only scan
- 🟡 Partial (filtered) index and expression index
- 🟡 Unique indexes as a correctness tool
- 🟡 Selectivity and cardinality
- 🟡 Clustered vs non-clustered index (how engines differ)
- 🟡 Other index types by name: hash, GIN, GiST, full-text, spatial

## 6. Query Performance & Execution Plans

- 🟢 Read an execution plan: `EXPLAIN` and `EXPLAIN ANALYZE`
- 🟢 Sequential scan vs index scan, and estimated vs actual rows
- 🟢 The usual causes of slow queries: missing index, N+1, `SELECT *`, big `OFFSET`, no limits
- 🟢 The N+1 problem and how to fix it (`BE 9`)
- 🟢 Connection pooling and connection limits
- 🟢 Measure first: slow-query log, p95 latency, then fix one thing at a time
- 🟡 Join algorithms by name: nested loop, hash join, merge join
- 🟡 Statistics and the query planner, and when plans go wrong
- 🟡 Batching, and reducing round trips
- 🟡 Caching results, and read replicas for heavy reads (topics 13, 14)
- 🟡 Locks and long transactions as a cause of slowness (topic 9)

## 7. Storage Engines & Internals

- 🟢 How data lives on disk: pages, rows, and why disk and memory speeds matter
- 🟢 Write-ahead log (WAL): write the change to a log first, so a crash cannot lose it
- 🟢 Buffer pool / page cache: hot data stays in memory
- 🟢 B-tree engines vs LSM-tree engines: read-optimised vs write-optimised
- 🟢 Crash recovery in plain words
- 🟡 LSM basics: memtable, SSTable, compaction
- 🟡 Row store vs column store (topic 20)
- 🟡 MVCC storage and vacuum / bloat (topic 9)
- 🟡 Checkpoints, fsync, and durability settings
- 🟡 In-memory databases and their trade-offs

---

# Stage 3: Correctness

## 8. Transactions & ACID

- 🟢 Transaction: `BEGIN`, `COMMIT`, `ROLLBACK`
- 🟢 ACID: atomicity, consistency, isolation, durability
- 🟢 Where to put the transaction boundary in application code (`BE 9`)
- 🟢 Keep transactions short, and never call slow external services inside one
- 🟢 Atomic updates (`SET balance = balance - 100`) instead of read-modify-write
- 🟢 Unique constraints and idempotency keys to stop duplicates (`BE 11`)
- 🟡 Savepoints
- 🟡 Autocommit, and what happens to a connection that dies mid-transaction
- 🟡 Durability settings and their cost
- 🟡 Transactions in an ORM, and hidden transaction problems

## 9. Concurrency & Isolation

- 🟢 Race conditions: lost update, double booking, double spend
- 🟢 Isolation levels: read committed, repeatable read, serializable
- 🟢 Anomalies by name: dirty read, non-repeatable read, phantom read, lost update, write skew
- 🟢 Optimistic locking (version column) vs pessimistic locking (`SELECT ... FOR UPDATE`)
- 🟢 Row locks, table locks, and what blocks what
- 🟢 Deadlocks: how they happen, and retry as the answer
- 🟡 MVCC: readers do not block writers
- 🟡 Choosing an isolation level, and its cost
- 🟡 Advisory locks and queue tables (`SKIP LOCKED`)
- 🟡 Ticket booking and inventory patterns (`SD 32`)
- 🟡 Long-running transactions and their side effects

## 10. Schema Migrations & Evolution

- 🟢 Versioned migration scripts, kept in source control
- 🟢 Forward-only changes, and testing them on a copy of production
- 🟢 Backward-compatible changes: old app versions and old server versions run at the same time (`SD 28`)
- 🟢 Expand and contract: add new, move data, switch, then remove old
- 🟢 Risky changes: renaming, dropping, changing a type, adding `NOT NULL`
- 🟡 Changing big tables without downtime: batching, online schema change tools
- 🟡 Backfilling data safely
- 🟡 Migration tools (Flyway, Liquibase, and framework-built-in ones)
- 🟡 Rollback plans, and why "forward fix" is often better
- 🟡 Schema and API versioning together (`ARCH 10`)

---

# Stage 4: Choosing & Scaling

## 11. Choosing a Database

- 🟢 Ask first: data shape, query patterns, consistency needs, scale, team skills
- 🟢 Relational as the default, and clear reasons to choose otherwise
- 🟢 Real systems use several stores (polyglot persistence): database, cache, search, object storage (`SD 17`)
- 🟢 Source of truth vs derived data (caches, search indexes, read models)
- 🟢 Managed service vs self-hosted: cost, control, effort, lock-in
- 🟡 A decision table: which store for which job
- 🟡 Cost and licensing
- 🟡 Migration cost of switching later
- 🟡 Hype-driven choices and how to avoid them (`ARCH 3`)

## 12. NoSQL Families

- 🟢 Key-value stores: fast lookup by key (DynamoDB, Redis)
- 🟢 Document databases: flexible JSON-like documents (MongoDB, Firestore)
- 🟢 Model NoSQL by access pattern, not by entities
- 🟢 Embed vs reference, and the cost of duplicated data
- 🟢 What you give up: joins, general queries, and often strong consistency
- 🟡 Wide-column stores (Cassandra, Bigtable): huge write volume, designed around queries
- 🟡 Graph databases (Neo4j): relationships as the main data
- 🟡 Time-series databases: metrics and events over time
- 🟡 Search engines: inverted index, relevance, faceting (Elasticsearch, OpenSearch)
- 🟡 (New) Vector databases and vector search in existing databases (`AI 6`)
- 🟡 Mobile backends as a service (Firebase, Supabase) and their security rules (`BE 1`)

## 13. Caching & Redis

- 🟢 Cache-aside, TTL, eviction (LRU), invalidation (`SD 15`)
- 🟢 Redis data types: strings, hashes, lists, sets, sorted sets
- 🟢 Common Redis uses: cache, session store, counters, rate limiter, leaderboard
- 🟢 Stampede, hot keys, and stale data
- 🟢 Never treat the cache as the only copy of important data
- 🟡 Persistence options: snapshots and append-only log
- 🟡 Pub/sub and streams (names and purpose)
- 🟡 Distributed locks and their limits (`SD 33`)
- 🟡 Cache sizing and hit-rate monitoring
- 🟡 Cluster mode and replication (names)

## 14. Replication & High Availability

- 🟢 Leader–follower replication and read replicas (`SD 18`)
- 🟢 Synchronous vs asynchronous replication, and the trade-off
- 🟢 Replication lag and stale reads, and read-your-writes
- 🟢 Failover: how a follower becomes the leader, and the risk of losing writes
- 🟢 Replication is not a backup
- 🟡 Multi-leader and leaderless replication (names)
- 🟡 Split brain and how it is prevented
- 🟡 Logical vs physical replication
- 🟡 Connection routing: writes to the leader, reads to replicas
- 🟡 High-availability setups and managed failover

## 15. Partitioning & Sharding

- 🟢 Try first: indexes, cache, replicas, a bigger machine, archiving (`SD 19`)
- 🟢 Table partitioning inside one database vs sharding across many
- 🟢 Hash vs range partitioning
- 🟢 Choosing a shard key: high cardinality, even spread, matches the main query
- 🟢 Hotspots and rebalancing
- 🟢 Costs: cross-shard queries, cross-shard transactions, operations
- 🟡 Consistent hashing
- 🟡 Directory-based sharding
- 🟡 Resharding with double writes
- 🟡 Partition pruning and archiving old partitions
- 🟡 Distributed SQL databases that shard for you (names)

## 16. Consistency, CAP & Distributed Data

- 🟢 Strong vs eventual consistency (`SD 23`)
- 🟢 CAP theorem: during a network split, choose consistency or availability
- 🟢 Which features need strong consistency (money, inventory) and which do not (likes, feeds)
- 🟢 Idempotency and retries across services
- 🟡 Quorum reads and writes (R + W > N)
- 🟡 Causal consistency and read-your-writes
- 🟡 Distributed transactions: two-phase commit (name), and sagas (`SD 26`)
- 🟡 PACELC (name)
- 🟡 Conflict resolution: last-write-wins, version vectors, CRDTs (names)
- 🟡 BASE as a contrast to ACID

---

# Stage 5: Operating

## 17. Backup, Recovery & Data Migration

- 🟢 Backups stored away from the database, and restores that are tested (`SD 29`)
- 🟢 RPO and RTO: how much data and how much time you can afford to lose
- 🟢 Point-in-time recovery using the write-ahead log
- 🟢 Replication is not a backup
- 🟡 Logical backups vs physical backups
- 🟡 Backup encryption and retention rules
- 🟡 Disaster recovery: multi-AZ and multi-region (`ARCH 12`)
- 🟡 Moving data between databases without downtime: dual writes, change data capture, validation (`SD 33`)
- 🟡 Deleting data on request (privacy) and what it means for backups

## 18. Database Security & Privacy

- 🟢 SQL injection and parameterized queries (`BE 6`)
- 🟢 Least privilege: separate database users for the app, migrations, and reporting
- 🟢 Never expose the database to the internet
- 🟢 Encryption in transit and at rest
- 🟢 Secrets for database credentials: a secrets manager, rotation
- 🟢 Personal data (PII): store the minimum, protect it, delete on request
- 🟡 Row-level security (Postgres, Supabase) and how it enforces per-user access
- 🟡 Multi-tenancy: shared tables with a tenant column vs separate schemas or databases
- 🟡 Column encryption, masking, and tokenization
- 🟡 Audit logs and access reviews
- 🟡 Compliance basics (GDPR-style rules)

## 19. Operations & Monitoring

- 🟢 Connection pooling and connection limits with many servers (`BE 9`)
- 🟢 What to monitor: query latency, slow queries, connections, locks, replication lag, disk, CPU, cache hit ratio
- 🟢 Slow-query log and query statistics
- 🟢 Capacity planning: growth of data, storage, and traffic
- 🟡 Routine maintenance: vacuum, analyze, reindex, archive old data
- 🟡 Version upgrades and maintenance windows
- 🟡 Runbooks for common incidents: locks, full disk, replica lag, connection exhaustion
- 🟡 Managed database features and their limits
- 🟡 Cost control: right-sizing and storage tiers (`ARCH 13`)

---

# Stage 6: Beyond the App Database

## 20. Analytics, Warehouses & Data Pipelines

- 🟢 OLTP vs OLAP, and why analytics should not slow the app database
- 🟢 Row store vs column store, and why columns suit analytics
- 🟢 Data warehouse vs data lake, in plain words
- 🟢 ETL vs ELT
- 🟢 Change data capture (CDC): stream changes out of the database (`SD 26`)
- 🟡 Star schema: fact and dimension tables
- 🟡 Batch vs stream processing (`SD 33`)
- 🟡 Lakehouse and open table formats (names)
- 🟡 Reporting from a read replica vs a warehouse
- 🟡 Data quality checks and data lineage

---

# Stage 7: Mobile

## 21. Mobile Databases (New)

- 🟢 SQLite: the embedded database in every phone
- 🟢 Room on Android, and Core Data or SwiftData on iOS
- 🟢 Never access the database on the main thread
- 🟢 Schema versions and on-device migrations: every old app version upgrades on its own
- 🟢 Offline-first: the local database is the source of truth, and it syncs with the server (`SD 30`)
- 🟢 Indexes and query design apply on the device too
- 🟢 Key-value settings storage vs a real database
- 🟡 Sync design: changes since a timestamp, conflict resolution, deletes (tombstones)
- 🟡 Encryption on device (SQLCipher and platform options)
- 🟡 Storing large data: files vs blobs
- 🟡 Testing database code and migrations
- 🟡 Other options and their status (Realm, Firebase local persistence): check each library's current support before choosing
- 🟡 How local IDs map to server IDs (`SD 20`)

---

# Stage 8: Interview & Practice

## 22. Database Interview Answer Points (New)

- 🟢 Design a schema from requirements: entities, keys, relationships, top queries
- 🟢 Explain each choice: why this key, this index, this isolation level
- 🟢 Ready answers: SQL vs NoSQL, indexes, transactions, isolation levels, replication, sharding
- 🟢 Ready answers: how to prevent double booking, how to make writes idempotent, how to fix a slow query
- 🟢 Always mention the trade-off and what could go wrong
- 🟡 Reading a query and predicting its plan
- 🟡 Estimating data size and query load
- 🟡 Questions to ask the interviewer about the data
- 🟡 Common traps: adding NoSQL "for scale" without numbers, sharding too early

## 23. Practice: Projects & Exercises

**Build (in order)**

- 🟢 Notes app schema: tables, keys, constraints, and a migration file (`BE 12`)
- 🟢 Load 100,000 rows, then find and fix three slow queries with `EXPLAIN` and indexes
- 🟢 Reservation table: prevent double booking with a unique constraint, then with locking
- 🟢 Money transfer: two accounts, a transaction, and a test with concurrent requests
- 🟡 Add a read replica locally and see replication lag
- 🟡 Cache a query in Redis with cache-aside and TTL
- 🟡 A backup and a full restore, timed
- 🟡 Room or SQLite in an app: entities, migrations, and an offline sync stub

**SQL exercises**

- 🟢 Joins, group by, and having on a small shop dataset
- 🟢 Window functions: top N per group, running total, latest row per user
- 🟡 Recursive query for a comment tree
- 🟡 Rewrite a slow query three ways and compare plans

**Schema designs to practise**

- 🟢 Notes app
- 🟢 E-commerce: users, products, orders, payments
- 🟢 Ticket or seat booking
- 🟢 Chat: users, conversations, messages
- 🟡 Social feed and followers
- 🟡 URL shortener
- 🟡 Multi-tenant app

---

# Glossary: Terms to Learn First

Plain meanings, with a priority. The last column is the topic that explains the term.

**Basics and modeling**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | DBMS | Software that stores, manages, and queries data | 1 |
| 🟢 | Schema | The structure of a database: tables, columns, types, constraints | 2 |
| 🟢 | Primary key | A column or set of columns that uniquely identifies a row | 2 |
| 🟢 | Foreign key | A column that refers to a row in another table | 2 |
| 🟢 | Constraint | A rule the database enforces: `NOT NULL`, unique, foreign key, check | 2 |
| 🟢 | Normalization | Storing each fact once, to avoid conflicting copies | 2 |
| 🟢 | Denormalization | Copying data on purpose to make reads faster | 2 |
| 🟢 | `NULL` | "No value" or "unknown". Compare it with `IS NULL`, not `=` | 2, 3 |
| 🟢 | OLTP / OLAP | Everyday small transactions / large analysis queries | 1, 20 |
| 🟡 | Surrogate key | An ID the system creates (1, 2, 3 or a UUID), not real-world data | 2 |
| 🟡 | ER diagram | A picture of tables and how they relate | 2 |
| 🟡 | Soft delete | Marking a row as deleted instead of removing it | 2 |

**SQL**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Join | Combine rows from two tables by a matching condition | 3 |
| 🟢 | `GROUP BY` / aggregate | Combine many rows into summary values such as a count or sum | 3 |
| 🟢 | Subquery | A query inside another query | 3 |
| 🟢 | Parameterized query | SQL and values sent separately, which stops SQL injection | 3, 18 |
| 🟢 | Keyset (cursor) pagination | Page by "after this key" instead of "skip N rows" | 3, 6 |
| 🟢 | CTE | A named temporary query written with `WITH` | 4 |
| 🟢 | Window function | A calculation across related rows without collapsing them | 4 |
| 🟡 | Upsert | Insert a row, or update it if it already exists | 3 |
| 🟡 | View / materialized view | A saved query / a saved query whose result is stored | 4 |
| 🟡 | Stored procedure / trigger | Code that runs inside the database / code that runs automatically on a change | 4 |

**Performance and internals**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Index | A sorted structure that finds rows without reading the whole table | 5 |
| 🟢 | B-tree | The default index structure: sorted, balanced, good for equality and ranges | 5, 7 |
| 🟢 | Composite index | An index on several columns. Column order matters | 5 |
| 🟢 | Full table scan | Reading every row to find a match | 5, 6 |
| 🟢 | Execution plan / `EXPLAIN` | The database's chosen steps for a query, and the command that shows them | 6 |
| 🟢 | N+1 query | One query for a list, then one more query for each item | 6 |
| 🟢 | Connection pool | A set of reusable database connections | 6, 19 |
| 🟢 | WAL (write-ahead log) | A log of changes written before the data files, so a crash cannot lose them | 7 |
| 🟢 | Buffer pool | Memory where the database keeps hot pages | 7 |
| 🟡 | Covering index | An index that holds every column the query needs | 5 |
| 🟡 | Selectivity | How well a condition narrows down rows. Few matches means high selectivity | 5 |
| 🟡 | LSM tree | A write-friendly storage design that merges sorted files over time | 7 |
| 🟡 | Compaction | Merging and cleaning stored files in the background | 7 |
| 🟡 | Row store / column store | Data stored by row (apps) / by column (analytics) | 7, 20 |
| 🟡 | Vacuum / bloat | Cleaning up dead row versions / wasted space from them | 7, 19 |

**Transactions and concurrency**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Transaction | A group of changes that all succeed or all fail | 8 |
| 🟢 | ACID | Atomicity, consistency, isolation, durability | 8 |
| 🟢 | Rollback | Undo everything in the transaction | 8 |
| 🟢 | Race condition | Wrong result because two requests interleave | 9 |
| 🟢 | Isolation level | How much concurrent transactions can see of each other | 9 |
| 🟢 | Lost update | Two writers read the same value, and one overwrites the other | 9 |
| 🟢 | Optimistic / pessimistic locking | Check for change at write time / lock the row first | 9 |
| 🟢 | Deadlock | Two transactions each wait for the other | 9 |
| 🟢 | Idempotency key | A unique ID that makes a repeated request safe | 8, 9 |
| 🟡 | Dirty / non-repeatable / phantom read | Three kinds of unexpected reads between transactions | 9 |
| 🟡 | Write skew | Two transactions each check a rule, then both write, breaking the rule | 9 |
| 🟡 | MVCC | Keep several versions of a row so readers do not block writers | 9 |
| 🟡 | `SELECT ... FOR UPDATE` | Read a row and lock it for the rest of the transaction | 9 |

**Schema change**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Migration | A versioned script that changes the schema | 10 |
| 🟢 | Backward-compatible change | A change that old code still works with | 10 |
| 🟢 | Expand and contract | Add the new shape, move to it, then remove the old shape | 10 |
| 🟡 | Backfill | Filling a new column for existing rows | 10 |
| 🟡 | Online schema change | Changing a big table without blocking traffic | 10 |

**Choosing, scaling, and distributed data**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Polyglot persistence | Using several kinds of stores, each for what it does best | 11 |
| 🟢 | Source of truth | The one store that owns the real data. Others are copies | 11 |
| 🟢 | Key-value / document store | Lookup by key / flexible JSON-like records | 12 |
| 🟢 | Cache-aside | Read the cache first, load from the database on a miss | 13 |
| 🟢 | TTL / eviction | Time before an entry expires / removal when the cache is full | 13 |
| 🟢 | Leader / follower | The node that takes writes / nodes that copy it | 14 |
| 🟢 | Replication lag | How far a follower is behind the leader | 14 |
| 🟢 | Failover | Promoting a follower when the leader fails | 14 |
| 🟢 | Sharding / shard key | Splitting data across databases / the field that decides where a row goes | 15 |
| 🟢 | Hotspot | One shard or key receiving far more traffic than others | 15 |
| 🟢 | CAP theorem | During a network split, choose consistency or availability | 16 |
| 🟢 | Strong / eventual consistency | Everyone sees the latest write / everyone sees it after a short delay | 16 |
| 🟡 | Wide-column / graph / time-series store | Kinds of NoSQL built for huge writes / relationships / data over time | 12 |
| 🟡 | Inverted index | A map from each word to the documents that contain it | 12 |
| 🟡 | Consistent hashing | A way to spread keys so adding a node moves little data | 15 |
| 🟡 | Quorum | A majority of replicas that must agree on a read or write | 16 |
| 🟡 | Two-phase commit / saga | A distributed transaction protocol / a chain of steps with undo actions | 16 |
| 🟡 | BASE | A looser model than ACID: basically available, soft state, eventually consistent | 16 |
| 🟡 | CRDT | A data type that merges concurrent edits without conflicts | 16 |

**Operating and analytics**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | PITR | Point-in-time recovery: restore to a chosen moment | 17 |
| 🟢 | RPO / RTO | Data you can lose / time you can be down | 17 |
| 🟢 | SQL injection | An attacker's input changes your SQL because it was mixed into the query text | 18 |
| 🟢 | Least privilege | Each user gets only the database access it needs | 18 |
| 🟢 | Encryption at rest / in transit | Data protected on disk / on the network | 18 |
| 🟢 | PII | Personally identifiable information | 18 |
| 🟢 | Data warehouse / data lake | Structured analytics store / raw data store of many formats | 20 |
| 🟢 | ETL / ELT | Transform then load / load then transform | 20 |
| 🟢 | CDC | Change data capture: stream row changes out of a database | 20 |
| 🟡 | Row-level security | Database rules that decide which rows a user may see | 18 |
| 🟡 | Multi-tenancy | Many customers sharing one system, kept apart | 18 |
| 🟡 | Star schema | A central fact table joined to dimension tables | 20 |

**Mobile**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | SQLite | A small database that lives inside the app | 21 |
| 🟢 | Room / Core Data / SwiftData | The Android and iOS libraries built on or around local storage | 21 |
| 🟢 | Offline-first | The local database is the source of truth, and it syncs with the server | 21 |
| 🟢 | On-device migration | Upgrading the local schema when the app updates | 21 |
| 🟡 | Tombstone | A marker for a deleted record, so the delete can sync | 21 |
| 🟡 | SQLCipher | Encryption for SQLite databases | 21 |

---

## Skip for Now

- Writing your own database or storage engine
- Deep query optimizer theory and cost formulas
- Vendor-specific administration and certifications
- Advanced distributed-systems proofs (consensus algorithms in detail)
- Every NoSQL product. Know the families and one example each

## How to Proceed

1. Do topics 1 to 4 first. Set up PostgreSQL locally and write real queries as you read.
2. Do topics 5 and 6 with a table of 100,000 or more rows, so `EXPLAIN` shows real differences.
3. Do topics 8 and 9 with two terminals, so you can see locks and races happen.
4. Then read topics 11 to 16 as the "what changes at scale" story, in that order.
5. Do topic 21 next to your daily mobile work: look at your own app's local database, its migrations, and its sync.
6. Do topics 22 and 23 last. Practise schema designs out loud and time yourself.
7. For each topic: what it is, what problem it solves, how it works, one downside.
