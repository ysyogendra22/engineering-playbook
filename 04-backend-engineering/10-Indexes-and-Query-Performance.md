# Indexes & Query Performance

Roadmap topic 10 · Stage 3: Data

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** an index helps the database find rows quickly without reading the whole table. Use the right ones, check with EXPLAIN, and don't add indexes blindly.

---

#### 1. What Is an Index — 🟢 Must Know

*Like the index at the back of a book: jump to the page instead of reading every page.*

1. Without an index the database does a **full table scan**: it reads every row.
2. An index is a sorted structure (usually a **B-tree**) that finds rows fast.
3. Primary keys and unique constraints are indexed automatically.

```text
No index:  1,000,000 rows → check all
Index:     ~ a few steps  → find the row
```

---

#### 2. The Trade-Off — 🟢 Must Know

| Benefit | Cost |
|---|---|
| Faster reads (`WHERE`, `JOIN`, `ORDER BY`) | Slower writes (index must be updated) |
| | Extra storage |

1. Don't index everything. Index what your queries use.
2. Tables with heavy writes feel every extra index.

---

#### 3. What to Index — 🟢 Must Know

1. Columns in `WHERE` filters.
2. Columns used in `JOIN` (foreign keys). Some databases (for example, PostgreSQL) do **not** index FK columns automatically.
3. Columns in `ORDER BY`.
4. Columns with many different values (email, user_id). A column with two values (a boolean) is a poor index on its own.

---

#### 4. Composite Index — 🟢 Must Know

*One index on several columns. The column order matters.*

```sql
CREATE INDEX idx_notes_user_created ON notes (user_id, created_at DESC);
```

Works well for:

```sql
SELECT * FROM notes
WHERE user_id = 42
ORDER BY created_at DESC
LIMIT 20;
```

Rules:

1. The index is used **from the left**: `(user_id, created_at)` helps queries on `user_id`, or on `user_id` + `created_at`.
2. It does **not** help a query using only `created_at`.
3. Put equality columns first (`user_id = ?`), then the range or sort column.

---

#### 5. EXPLAIN — 🟢 Must Know

*Ask the database how it will run your query.*

```sql
EXPLAIN ANALYZE
SELECT * FROM notes WHERE user_id = 42 ORDER BY created_at DESC LIMIT 20;
```

Look for:

1. **Seq Scan** (full table scan) → probably needs an index.
2. **Index Scan** → the index is used.
3. Estimated vs actual rows, and the time.

---

#### 6. Common Causes of Slow Queries — 🟢 Must Know

1. **Missing index** on the filter or join column.
2. **N+1 queries** (topic `09`).
3. **`SELECT *`** and returning too much data.
4. **Large `OFFSET`** (`OFFSET 100000` reads and throws away 100,000 rows). Use cursor pagination.
5. **Function on an indexed column**: `WHERE lower(email) = ...` can't use the plain index on `email`.
6. **Leading wildcard**: `LIKE '%text'` can't use a normal index.
7. Joining or sorting huge results.

---

#### 7. Covering Index — 🟡 Good to Know

1. An index that contains **all** columns the query needs, so the database doesn't read the table at all (an "index-only scan").
2. Faster reads, bigger index.

---

#### 8. Measure Before Optimizing — 🟡 Good to Know

1. Find slow queries first (slow query log, monitoring, p95 latency).
2. Use `EXPLAIN`. Change one thing. Measure again.
3. Don't guess, and don't add indexes "just in case".

---

#### 9. Common Interview Questions

1. **What is an index and why use it?**
   A sorted structure that lets the database find rows without scanning the whole table. Faster reads, slower writes, more storage.
2. **What is a composite index? Does column order matter?**
   An index on several columns. Yes, it works from the left. Equality columns first, then sort or range.
3. **A query is slow. What do you do?**
   Run `EXPLAIN`, look for a full scan, check for N+1, add or fix an index, return fewer columns/rows, then measure again.
4. **Why doesn't the database use my index?**
   Function on the column, leading wildcard, wrong column order, or low selectivity.
5. **Why is a big `OFFSET` slow?**
   The database still reads and skips all previous rows. Use cursor pagination.
6. **Is more indexes always better?**
   No. Every index slows writes and uses storage.

---

#### 10. Common Mistakes

1. Indexing every column.
2. Wrong column order in a composite index.
3. Not indexing foreign keys or filter columns.
4. Wrapping the indexed column in a function.
5. Optimizing without measuring.
6. Using `OFFSET` for deep pages.

---

#### 11. Related Topics

1. `03` API Design (cursor pagination)
2. `08` Databases, SQL & Data Modeling
3. `09` Connecting API to Database (N+1)
4. Caching, replication, sharding (system design roadmap)

---

#### 12. Interview Must Remember

1. **Index = faster reads, slower writes, more storage.**
2. Index columns used in **WHERE, JOIN, ORDER BY**.
3. **Composite index order matters** (left to right).
4. Use **EXPLAIN** to see scans vs index use.
5. Slow endpoint checklist: **N+1, missing index, too much data, big OFFSET.**
6. **Measure before optimizing.**
