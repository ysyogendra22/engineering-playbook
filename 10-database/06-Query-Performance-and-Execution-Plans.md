# Query Performance & Execution Plans

Roadmap topic 6 · Stage 2: Performance

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** `EXPLAIN` shows you exactly what the database is planning to do with your query — not a guess, the actual truth. Reading it well turns "this query is slow, I don't know why" into a specific, fixable diagnosis.

---

#### 1. Reading an Execution Plan — 🟢 Must Know

```sql
EXPLAIN ANALYZE
SELECT * FROM notes WHERE user_id = 42 ORDER BY created_at DESC LIMIT 20;
```

`EXPLAIN` shows the **planned** steps and estimated cost. `EXPLAIN ANALYZE` actually **runs** the query and shows real timing and row counts alongside the estimates — always prefer `ANALYZE` when you can safely run the query (careful with write queries, which it also executes for real).

---

#### 2. Sequential Scan vs Index Scan — 🟢 Must Know

```text
Seq Scan on notes           ← reads every row — usually a red flag on a large table
  Filter: (user_id = 42)

Index Scan using idx_notes_user_created on notes    ← uses the index directly
  Index Cond: (user_id = 42)
```

Look for **`Seq Scan`** on a large table where an index should apply — that's the plan telling you an index is missing or not being used (`5`, item 6). Also compare **estimated vs actual rows** — a huge gap between them means the query planner's statistics are stale or wrong.

---

#### 3. Usual Causes of Slow Queries — 🟢 Must Know

1. **Missing index** on a filter, join, or sort column.
2. **N+1 queries** — one query for a list, then one more per item (item 4).
3. **`SELECT *`** — pulling columns the application doesn't actually need, wasting I/O and network.
4. **Big `OFFSET`** — the database still reads and discards every skipped row (`3`, item 7).
5. **No limits** — an unbounded query that could return millions of rows.

---

#### 4. The N+1 Problem — 🟢 Must Know

```text
1 query:  SELECT * FROM users WHERE ...           (get 50 users)
50 queries:  SELECT * FROM notes WHERE user_id = ?  (once PER user, in a loop)
= 51 queries total, when 2 would do
```

**Fix**: a single query with a `JOIN`, or one `WHERE user_id IN (...)` query for all the related rows at once, instead of looping and querying per item (`BE 9`).

---

#### 5. Connection Pooling and Limits — 🟢 Must Know

Every database has a **maximum number of connections** it can handle. A **connection pool** reuses a small set of connections across many requests instead of opening a new one per request — opening too many connections (especially with many server instances, each with their own pool) can exhaust the database's limit and cause failures unrelated to any single query's actual performance.

---

#### 6. Measure First — 🟢 Must Know

*The same discipline that appears throughout this vault: slow-query log → `EXPLAIN` → change one thing → measure again.*

Find slow queries first (a slow-query log, monitoring, p95 latency — topic `19`), not by guessing which query "feels" slow. Change **one thing at a time** and re-measure — changing several things at once makes it impossible to know which change actually helped.

---

#### 7. Join Algorithms — 🟡 Good to Know

1. **Nested loop** — for each row in one table, scan the other — fine for small tables or highly selective joins.
2. **Hash join** — build a hash table from one side, probe it with the other — good for larger, less selective joins.
3. **Merge join** — both inputs already sorted on the join key, merged in one pass — efficient when the data is already ordered (often via an index).

The query planner picks automatically based on table sizes and available indexes — worth recognising the names in an execution plan, not necessarily choosing them manually.

---

#### 8. Statistics and the Query Planner — 🟡 Good to Know

The planner's choices depend on **statistics** about the data (row counts, value distributions) that it keeps and periodically refreshes. Stale statistics (after a large bulk load, for example) can lead to a bad plan — running `ANALYZE` (the maintenance command, distinct from `EXPLAIN ANALYZE`) refreshes them.

---

#### 9. Batching and Reducing Round Trips — 🟡 Good to Know

Each query has real network round-trip overhead — batching several operations into fewer round trips (a bulk insert instead of many single inserts, `3` item 11) often matters as much as the query's own execution time, especially for many small operations.

---

#### 10. Caching and Read Replicas — 🟡 Good to Know

Two ways to reduce load on the primary database for heavy reads: caching results (`13`, `SD 15`) avoids hitting the database at all for repeated queries; read replicas (`14`) spread read traffic across additional copies of the data.

---

#### 11. Locks and Long Transactions — 🟡 Good to Know

A slow query can sometimes be slow not because of its own execution plan, but because it's **waiting on a lock** held by another, unrelated long-running transaction (`9`) — always check for lock contention as a possible cause, not just the query's own plan.

---

#### 12. Common Interview Questions

1. **How do you diagnose a slow query?**
   Find it first via a slow-query log or monitoring, then run `EXPLAIN ANALYZE`, look for a sequential scan where an index should apply, check for a large gap between estimated and actual rows, and change one thing at a time.
2. **What's the difference between `EXPLAIN` and `EXPLAIN ANALYZE`?**
   `EXPLAIN` shows the planned steps and cost estimates without running the query. `EXPLAIN ANALYZE` actually executes it and shows real timing and row counts alongside the estimates.
3. **What's the N+1 problem, and how do you fix it?**
   One query for a list, then one more query per item in a loop — n+1 total queries instead of a small constant number. Fix with a `JOIN` or a single `WHERE ... IN (...)` query for all related rows at once.
4. **Why can a big `OFFSET` be slow even with an index?**
   The database still has to read and discard every row up to the offset — the index doesn't eliminate that scan, it just makes finding the *starting point* fast, not skipping to a deep offset.
5. **A query with the right index is still slow — what else would you check?**
   Whether it's actually being used (via `EXPLAIN`), stale planner statistics, lock contention from another long-running transaction, and whether the query is returning far more data than actually needed.

---

#### 13. Common Mistakes

1. Optimising based on a guess instead of `EXPLAIN`/monitoring data.
2. Not noticing an N+1 pattern until it's already causing production problems.
3. `SELECT *` in a hot path, pulling unnecessary columns.
4. Changing several things at once and being unable to tell what actually helped.
5. Assuming a slow query is always the query's own fault, ignoring lock contention.

---

#### 14. Related Topics

1. `5` Indexes — what `EXPLAIN` is checking whether the query actually uses
2. `9` Concurrency & Isolation — locks as a cause of apparent query slowness
3. `BE 9` Connecting API to Database — the N+1 problem, application-side
4. `DB 13`, `DB 14` — caching and read replicas as scaling responses to read load

---

#### 15. Interview Must Remember

1. **`EXPLAIN ANALYZE`** shows the real plan and real timing — use it, don't guess.
2. **Seq Scan on a large table = usually a missing or unused index.**
3. **N+1 fix**: one query with a join or `IN (...)`, not a query per item in a loop.
4. **Measure, change one thing, measure again.**
