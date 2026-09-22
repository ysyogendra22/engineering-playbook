# Advanced SQL

Roadmap topic 4 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** window functions and CTEs are what let you answer questions like "the top 3 notes per user" or "the running total by day" in one clean query, instead of pulling everything into application code and looping over it by hand.

---

#### 1. CTEs — 🟢 Must Know

*A `WITH` clause names a subquery, making a complex query readable in steps.*

```sql
WITH active_users AS (
    SELECT id FROM users WHERE last_login > now() - interval '30 days'
)
SELECT notes.* FROM notes
JOIN active_users ON active_users.id = notes.user_id;
```

Equivalent to a subquery, but named and often placed before the main query — makes multi-step logic much easier to read and reason about than deeply nested subqueries.

---

#### 2. Window Functions — 🟢 Must Know

*A calculation across a set of related rows, without collapsing them into one row (unlike `GROUP BY`).*

```sql
SELECT
    user_id,
    title,
    created_at,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn,
    RANK() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rnk,
    SUM(1) OVER (PARTITION BY user_id ORDER BY created_at) AS running_count,
    LAG(title) OVER (PARTITION BY user_id ORDER BY created_at) AS previous_title
FROM notes;
```

1. **`ROW_NUMBER()`** — a unique, sequential number per row within its partition.
2. **`RANK()`** — like `ROW_NUMBER`, but ties share the same rank (and the next rank skips accordingly).
3. **Running totals** — a `SUM(...) OVER (ORDER BY ...)` accumulates as it goes.
4. **`LAG`/`LEAD`** — look at the previous/next row's value, in the same query, without a self-join.

---

#### 3. `CASE` Expressions — 🟢 Must Know

```sql
SELECT
    id,
    CASE
        WHEN balance_cents < 0 THEN 'overdrawn'
        WHEN balance_cents = 0 THEN 'empty'
        ELSE 'positive'
    END AS status
FROM accounts;
```

Inline conditional logic inside a query — useful for categorising or reshaping data without pulling it into application code first.

---

#### 4. Common Patterns — 🟢 Must Know

**Top N per group:**

```sql
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
    FROM notes
) ranked
WHERE rn <= 3;   -- the 3 most recent notes per user
```

**Latest row per user:** same pattern with `rn = 1`. **Deduplication:** partition by the duplicate key, keep `rn = 1`, delete the rest. **Gaps and islands:** finding consecutive runs or missing values in a sequence, usually solved by comparing a row number to a grouping key derived from the ordered column.

---

#### 5. Recursive CTEs — 🟡 Good to Know

*For trees and graphs stored with a self-referencing key (`2`, item 13).*

```sql
WITH RECURSIVE comment_tree AS (
    SELECT id, parent_id, body FROM comments WHERE parent_id IS NULL  -- base case
    UNION ALL
    SELECT c.id, c.parent_id, c.body
    FROM comments c
    JOIN comment_tree ct ON c.parent_id = ct.id                       -- recursive case
)
SELECT * FROM comment_tree;
```

The same base-case/recursive-case shape from `02-algorithm`'s recursion topic, expressed in SQL — walks the whole tree in one query.

---

#### 6. Views and Materialized Views — 🟡 Good to Know

1. **View** — a saved query, re-run every time it's referenced; no storage cost, always fresh.
2. **Materialized view** — a saved query whose **result is stored**, refreshed on a schedule or on demand; faster to read, but can be stale between refreshes.

---

#### 7. Stored Procedures, Functions, Triggers — 🟡 Good to Know

Code that runs **inside** the database. **When they help**: enforcing a rule that must never be bypassed, regardless of which application calls the database. **When they hurt**: business logic split between application code and the database makes the system harder to test, version, and reason about as a whole — use sparingly and deliberately.

---

#### 8. JSON Columns — 🟡 Good to Know

Most relational databases (PostgreSQL's `JSONB`, for example) support storing and querying semi-structured JSON directly in a column — useful for genuinely flexible or sparse data, but overusing it defeats the point of a relational schema (topic `2`) and loses the database's ability to enforce structure.

---

#### 9. Full-Text Search Inside the Database — 🟡 Good to Know

Most relational databases have built-in text search capabilities, good enough for many applications without needing a separate search engine (`12`) — reach for a dedicated search engine only once the database's built-in search genuinely isn't enough.

---

#### 10. Generated Columns — 🟡 Good to Know

A column whose value is computed automatically from other columns in the same row — keeps a derived value always correct and in sync, without needing application code to maintain it manually.

---

#### 11. Common Interview Questions

1. **What's a window function, and how is it different from `GROUP BY`?**
   A window function computes a value across a set of related rows without collapsing them into one output row — `GROUP BY` reduces many rows to one per group; a window function keeps every row while still seeing its group's context.
2. **How would you get the 3 most recent notes per user?**
   `ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC)`, wrapped in an outer query filtering `rn <= 3`.
3. **What's a CTE, and why use one?**
   A named subquery via `WITH`, making multi-step query logic far more readable than deeply nested subqueries.
4. **View vs materialized view?**
   A view re-runs its query every time, always fresh, no storage cost. A materialized view stores the result, faster to read but can go stale until refreshed.
5. **When would you use a recursive CTE?**
   For querying a tree or graph stored with a self-referencing key (a comment thread, a category hierarchy) — walking the whole structure in one query.

---

#### 12. Common Mistakes

1. Solving a "top N per group" problem by pulling all rows into application code instead of using a window function.
2. Confusing a materialized view's staleness with a plain view's always-fresh behaviour.
3. Overusing stored procedures/triggers, spreading business logic across the database and application layers.
4. Storing genuinely structured data as JSON just because it's convenient, defeating the schema's guarantees.

---

#### 13. Related Topics

1. `3` SQL Fundamentals — the base queries these advanced features build on
2. `2` Relational Model & Data Modeling — trees/hierarchies, which recursive CTEs query
3. `03-leetcode-patterns` (topic on SQL patterns, if applicable) — related query patterns for interviews

---

#### 14. Interview Must Remember

1. **CTE = named subquery**, readable multi-step logic.
2. **Window functions keep every row**, unlike `GROUP BY` which collapses them.
3. **`ROW_NUMBER()` + partition + filter** is the standard "top N per group" template.
4. **Recursive CTE** for trees and graphs stored with a self-referencing key.
