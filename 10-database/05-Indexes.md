# Indexes

Roadmap topic 5 · Stage 2: Performance

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** an index is a sorted shortcut that lets the database find rows without reading the whole table, the same way a book's index lets you find a topic without reading every page. Almost every "why is this query slow?" question in an interview traces back to a missing or wrong index.

---

#### 1. What an Index Is — 🟢 Must Know

Without one, the database does a **full table scan** — reads every row to find matches. An index is a separate, sorted structure that lets it jump straight to matching rows instead.

```text
No index:  1,000,000 rows → check all
B-tree:    ~ a few steps  → find the row directly
```

---

#### 2. B-Tree: the Default — 🟢 Must Know

A B-tree is a sorted, balanced tree structure — the default index type in almost every relational database, and a good fit for **equality** (`WHERE id = ?`) and **range** (`WHERE created_at > ?`) queries alike, since it keeps values in sorted order.

---

#### 3. The Cost — 🟢 Must Know

| Benefit | Cost |
|---|---|
| Faster reads (`WHERE`, `JOIN`, `ORDER BY`) | Slower writes — every index must be updated too |
| | Extra storage |

Don't index everything — index what your **actual queries** use (item 5). A heavily-written table feels every extra index on every insert and update.

---

#### 4. Composite Index — 🟢 Must Know

*One index on several columns. Column order matters — the "leftmost rule".*

```sql
CREATE INDEX idx_notes_user_created ON notes (user_id, created_at DESC);

-- Uses the index fully:
SELECT * FROM notes WHERE user_id = 42 ORDER BY created_at DESC LIMIT 20;

-- Uses the index PARTIALLY (only the user_id part):
SELECT * FROM notes WHERE user_id = 42;

-- Does NOT use this index at all:
SELECT * FROM notes WHERE created_at > '2025-01-01';   -- created_at alone, not leftmost
```

The index is used **from the left** — put equality columns first, then the sort/range column.

---

#### 5. What to Index — 🟢 Must Know

Columns used in `WHERE` filters, `JOIN` conditions (including foreign keys — not always indexed automatically), and `ORDER BY`. Start from the actual queries the application runs (`2`, item 4), not a guess at what "seems important".

---

#### 6. Why an Index Isn't Used — 🟢 Must Know

1. **A function wraps the column**: `WHERE lower(email) = 'x'` can't use a plain index on `email` — needs a matching expression index (item 8).
2. **A leading wildcard**: `LIKE '%text'` can't use a normal B-tree index (a trailing wildcard, `LIKE 'text%'`, usually still can).
3. **Type mismatch**: comparing a column to a value of a different type can silently prevent index use.
4. **Low selectivity**: an index on a boolean column (few distinct values) rarely helps — the planner may reasonably choose a full scan instead.

---

#### 7. Covering Index — 🟡 Good to Know

An index that contains **every column** a query needs, so the database can answer entirely from the index without touching the table at all (an "index-only scan") — faster reads, at the cost of a larger index.

---

#### 8. Partial and Expression Indexes — 🟡 Good to Know

1. **Partial index** — indexes only rows matching a condition (`WHERE deleted_at IS NULL`), smaller and faster for queries that always include that same filter.
2. **Expression index** — indexes the *result* of an expression (`lower(email)`), fixing exactly the "function on the column" problem from item 6.

---

#### 9. Unique Indexes as a Correctness Tool — 🟡 Good to Know

A unique index is both a performance tool **and** a correctness guarantee — it's what a `UNIQUE` constraint (`2`, item 7) is actually implemented with, enforcing no-duplicates at the database level.

---

#### 10. Selectivity and Cardinality — 🟡 Good to Know

**Cardinality** — the number of distinct values in a column. **Selectivity** — how well a condition narrows down rows (high selectivity = few matches). An index on a low-cardinality column (like a boolean) is usually a poor investment; an index on a high-cardinality column (like an email) is usually a good one.

---

#### 11. Clustered vs Non-Clustered — 🟡 Good to Know

A **clustered** index determines the actual physical order rows are stored on disk (a table has at most one). A **non-clustered** index is a separate structure pointing back to the row's location. How engines handle this differs (PostgreSQL doesn't have true clustered indexes the way some other databases do) — know the concept, check the specifics per engine.

---

#### 12. Other Index Types — 🟡 Good to Know

**Hash** (equality only, no ranges), **GIN/GiST** (PostgreSQL, for full-text search and complex types like JSON or geometric data), **full-text**, **spatial** — specialised structures for specialised query patterns, beyond the default B-tree.

---

#### 13. Common Interview Questions

1. **What is an index, and why does it speed up reads?**
   A sorted structure (usually a B-tree) that lets the database find matching rows directly instead of scanning the whole table — the same way a book's index avoids reading every page.
2. **What's the trade-off of adding an index?**
   Faster reads, at the cost of slower writes (the index must be updated on every insert/update/delete) and extra storage.
3. **Does column order matter in a composite index? Why?**
   Yes — the index is used from the left. Put equality columns first, then the range/sort column, or a query that only filters on the second column won't use the index at all.
4. **Why might the database ignore an index that exists on the exact column being filtered?**
   A function wrapping the column, a leading wildcard, a type mismatch, or low selectivity on that column can each prevent index use — check with `EXPLAIN` (topic `6`) to confirm.
5. **What's a covering index?**
   An index containing every column a query needs, so the database can answer from the index alone without reading the table — an "index-only scan".

---

#### 14. Common Mistakes

1. Adding an index to every column "just in case", slowing down writes for no real benefit.
2. Wrong column order in a composite index.
3. Wrapping an indexed column in a function and being surprised the index isn't used.
4. Not indexing foreign key columns (not automatic in every database).
5. Indexing a low-cardinality column expecting a big performance win.

---

#### 15. Related Topics

1. `6` Query Performance & Execution Plans — how to confirm whether an index is actually being used
2. `2` Relational Model & Data Modeling — designing the schema and queries an index should match
3. `BE 10` Indexes & Query Performance — the same core content, backend-focused first pass

---

#### 16. Interview Must Remember

1. **Index = faster reads, slower writes, more storage.**
2. **B-tree is the default** — good for equality and range queries.
3. **Composite index order matters** — leftmost columns are what get used.
4. **A function, leading wildcard, type mismatch, or low selectivity** can each stop an index from being used.
