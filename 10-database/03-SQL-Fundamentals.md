# SQL Fundamentals

Roadmap topic 3 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** SQL is the one language every backend and database topic in this vault assumes you can read and write comfortably. This topic is the baseline: the handful of clauses and join types that cover the large majority of real queries.

---

#### 1. `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT` — 🟢 Must Know

```sql
SELECT DISTINCT user_id
FROM notes
WHERE created_at > '2025-01-01'
ORDER BY created_at DESC
LIMIT 20;
```

The basic shape of almost every read query: filter with `WHERE`, sort with `ORDER BY`, cap the result with `LIMIT`, and remove duplicates with `DISTINCT` where needed.

---

#### 2. `INSERT`, `UPDATE`, `DELETE` — 🟢 Must Know

```sql
INSERT INTO notes (id, user_id, title) VALUES (gen_random_uuid(), $1, $2);
UPDATE notes SET title = $1 WHERE id = $2;
DELETE FROM notes WHERE id = $1;
```

**`UPDATE` or `DELETE` without a `WHERE` clause changes or removes every row in the table** — one of the most common and most damaging mistakes possible in SQL. Always double-check the `WHERE` clause before running either, especially by hand in production.

---

#### 3. Aggregates — 🟢 Must Know

`COUNT`, `SUM`, `AVG`, `MIN`, `MAX` — collapse many rows into one summary value.

```sql
SELECT COUNT(*) FROM notes WHERE user_id = $1;
SELECT AVG(balance_cents) FROM accounts;
```

---

#### 4. `GROUP BY` and `HAVING` — 🟢 Must Know

```sql
SELECT user_id, COUNT(*) AS note_count
FROM notes
GROUP BY user_id
HAVING COUNT(*) > 100;    -- filters on the AGGREGATE, after grouping
```

`WHERE` filters rows **before** grouping; `HAVING` filters groups **after** aggregation — a common source of confusion, and a common interview question in its own right.

---

#### 5. Joins — 🟢 Must Know

```text
INNER JOIN:  only rows that match in both tables
LEFT JOIN:   all rows from the left table, matched rows from the right (NULL if no match)
RIGHT JOIN:  the mirror of LEFT JOIN
FULL JOIN:   all rows from both tables, matched where possible
CROSS JOIN:  every row of one table paired with every row of the other (no condition)
```

```sql
SELECT u.name, n.title
FROM users u
LEFT JOIN notes n ON n.user_id = u.id;   -- includes users with zero notes (n.title = NULL)
```

---

#### 6. Subqueries and `EXISTS` — 🟢 Must Know

```sql
SELECT * FROM users
WHERE EXISTS (
    SELECT 1 FROM notes WHERE notes.user_id = users.id
);   -- users who have at least one note
```

`EXISTS` is often faster than an equivalent `IN (SELECT ...)` subquery for this kind of "does a related row exist?" check, since the database can stop as soon as it finds one match.

---

#### 7. Pagination: `OFFSET` vs Keyset — 🟢 Must Know

```sql
-- OFFSET pagination: simple, but slow for deep pages — the database still
-- reads and discards every skipped row
SELECT * FROM notes ORDER BY created_at DESC OFFSET 10000 LIMIT 20;

-- Keyset (cursor) pagination: fast at any depth — jumps straight to the
-- right place using an index
SELECT * FROM notes
WHERE created_at < $lastSeenCreatedAt
ORDER BY created_at DESC
LIMIT 20;
```

Prefer keyset pagination for any API that might page deeply (`BE 3`).

---

#### 8. Parameterized Queries — 🟢 Must Know

*Never build SQL by concatenating strings with user input — the single most important security rule in this topic (`BE 6`).*

```sql
-- Dangerous: string concatenation
"SELECT * FROM users WHERE email = '" + userInput + "'"   -- SQL injection risk

-- Safe: parameterized query
SELECT * FROM users WHERE email = $1;   -- value sent separately from the SQL text
```

---

#### 9. Upsert — 🟡 Good to Know

```sql
INSERT INTO settings (user_id, key, value)
VALUES ($1, $2, $3)
ON CONFLICT (user_id, key) DO UPDATE SET value = EXCLUDED.value;
```

Insert a row, or update it if a conflicting one already exists — one round trip instead of a separate check-then-insert-or-update, and avoids a race condition between the check and the write.

---

#### 10. Set Operations — 🟡 Good to Know

`UNION` (combine results, removing duplicates), `UNION ALL` (combine, keeping duplicates, faster), `INTERSECT` (rows in both), `EXCEPT` (rows in the first but not the second) — useful for combining or comparing result sets from separate queries.

---

#### 11. Bulk Insert and Batching — 🟡 Good to Know

Inserting many rows in one statement (or in reasonably sized batches) is far faster than one `INSERT` per row — each individual round trip to the database has real overhead that adds up quickly at scale.

---

#### 12. Writing Readable SQL — 🟡 Good to Know

Consistent capitalization of keywords, clear indentation for joins and conditions, and meaningful table aliases — SQL is read far more often than it's written, and a query someone else can follow at a glance saves real debugging time later.

---

#### 13. Common Interview Questions

1. **What's the difference between `WHERE` and `HAVING`?**
   `WHERE` filters individual rows before grouping. `HAVING` filters groups after aggregation — you can't use an aggregate function in `WHERE`, which is exactly why `HAVING` exists.
2. **Explain the different join types.**
   Inner joins only matching rows; left/right joins keep all rows from one side, filling unmatched columns with `NULL`; full join keeps all rows from both sides; cross join pairs every row with every other row, with no condition.
3. **Why is keyset pagination usually better than `OFFSET` for deep pages?**
   `OFFSET` still makes the database read and discard every skipped row; keyset pagination uses an index to jump straight to the right position, staying fast regardless of how deep the page is.
4. **Why are parameterized queries important?**
   They send the SQL structure and the data values separately, so user input can never be interpreted as SQL — the standard defense against SQL injection.
5. **What does `ON CONFLICT DO UPDATE` do?**
   Implements an upsert in one atomic statement — insert if the row doesn't exist, update it if it does — avoiding both a separate round trip and a race condition between checking and writing.

---

#### 14. Common Mistakes

1. Running `UPDATE`/`DELETE` without a `WHERE` clause and affecting every row.
2. Building SQL from string concatenation with user input.
3. Using `OFFSET` for deep pagination on a large, frequently-changing table.
4. Confusing `WHERE` and `HAVING`, or trying to use an aggregate in `WHERE`.
5. Inserting rows one at a time in a loop instead of batching.

---

#### 15. Related Topics

1. `2` Relational Model & Data Modeling — the schema these queries run against
2. `4` Advanced SQL — window functions, CTEs, and more complex query patterns
3. `5` Indexes, `6` Query Performance & Execution Plans — making these queries actually fast
4. `BE 3` API Design — cursor pagination applied at the API layer
5. `BE 6` Backend Security Essentials — SQL injection in full depth

---

#### 16. Interview Must Remember

1. **`UPDATE`/`DELETE` with no `WHERE` = every row.** Always double-check.
2. **`WHERE` filters rows before grouping; `HAVING` filters groups after.**
3. **Keyset pagination for deep pages**, not `OFFSET`.
4. **Always parameterize queries** — never concatenate user input into SQL.
