# Databases, SQL & Data Modeling

Roadmap topic 8 · Stage 3: Data

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** a relational database stores data in linked tables. SQL is how you ask questions. Good modeling means designing tables around the questions your app will ask.

---

#### 1. Tables, Rows, Columns, Keys — 🟢 Must Know

*Think of a spreadsheet: a table is a sheet, a row is one record, a column is one field.*

1. **Table** — one kind of thing (`users`, `posts`).
2. **Row** — one record. **Column** — one field with a data type.
3. **Primary key (PK)** — unique ID of a row.
4. **Foreign key (FK)** — a column that points to a row in another table.

```sql
CREATE TABLE users (
  id         BIGSERIAL PRIMARY KEY,
  email      TEXT NOT NULL UNIQUE,
  name       TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE posts (
  id         BIGSERIAL PRIMARY KEY,
  user_id    BIGINT NOT NULL REFERENCES users(id),   -- foreign key
  title      TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

---

#### 2. Constraints — 🟢 Must Know

*Rules the database enforces, even if the app has a bug.*

| Constraint | Meaning |
|---|---|
| `PRIMARY KEY` | Unique and not null |
| `FOREIGN KEY` | Must point to an existing row |
| `UNIQUE` | No duplicates (for example, email) |
| `NOT NULL` | Value is required |
| `CHECK` | Custom rule (`price >= 0`) |
| `DEFAULT` | Value used when none is given |

**Remember:** the app validates for a good user experience. The database constraints are the last safety net.

---

#### 3. CRUD in SQL — 🟢 Must Know

```sql
INSERT INTO posts (user_id, title) VALUES (1, 'Hello');      -- Create

SELECT id, title FROM posts
WHERE user_id = 1 ORDER BY created_at DESC LIMIT 20;        -- Read

UPDATE posts SET title = 'Hi' WHERE id = 5;                  -- Update

DELETE FROM posts WHERE id = 5;                              -- Delete
```

1. **Always** use `WHERE` with `UPDATE` and `DELETE`. Without it you change every row.
2. Select only the columns you need. Avoid `SELECT *`.
3. Pass values as parameters (see topic `06`).

---

#### 4. Joins & Group By — 🟢 Must Know

*A join combines rows from two tables using a matching column.*

```sql
-- INNER JOIN: only rows that match in both
SELECT p.id, p.title, u.name
FROM posts p
JOIN users u ON u.id = p.user_id
ORDER BY p.created_at DESC
LIMIT 20;

-- LEFT JOIN: all users, even those with no posts
SELECT u.name, COUNT(p.id) AS post_count
FROM users u
LEFT JOIN posts p ON p.user_id = u.id
GROUP BY u.id, u.name;
```

1. **INNER JOIN** — only matches. **LEFT JOIN** — everything from the left table, plus matches (or NULL).
2. **GROUP BY** + aggregates: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
3. `WHERE` filters rows **before** grouping. `HAVING` filters **after** grouping.

---

#### 5. NULL — 🟢 Must Know

*NULL means "unknown / no value", not zero and not an empty string.*

1. Use `IS NULL` / `IS NOT NULL`. `= NULL` never works.
2. `NULL = NULL` is not true.
3. `COUNT(*)` counts rows. `COUNT(column)` skips NULLs.
4. Use `NOT NULL` on columns that must always have a value.

---

#### 6. Relationships — 🟢 Must Know

| Type | Example | How |
|---|---|---|
| One-to-one | user ↔ profile | FK with `UNIQUE` |
| One-to-many | user → posts | FK on the "many" side |
| Many-to-many | users ↔ liked posts | A **join table** with two FKs |

```sql
CREATE TABLE likes (
  user_id BIGINT NOT NULL REFERENCES users(id),
  post_id BIGINT NOT NULL REFERENCES posts(id),
  PRIMARY KEY (user_id, post_id)          -- one like per user per post
);
```

---

#### 7. Design the Schema from the Queries — 🟢 Must Know

*Start from what the screens need, not only from the nouns.*

1. List the screens and the questions: "recent posts of people I follow", "likes count per post", "notes of this user".
2. Design tables so those queries are simple and fast.
3. Then add constraints and indexes for them (topic `10`).

---

#### 8. Normalization vs Denormalization — 🟢 Must Know

1. **Normalization** — store each fact once (the author's name lives only in `users`). Less duplication, easy updates, more joins.
2. **Denormalization** — deliberately copy data for faster reads (for example, store `like_count` on `posts`). Faster reads, but you must keep the copies in sync.
3. Start normalized. Denormalize only for a measured, real need.

---

#### 9. Money and Time Zones — 🟢 Must Know

1. **Money:** store integer **cents** (`1999`) or `DECIMAL`. **Never** `FLOAT` (rounding errors). Store the currency too.
2. **Time:** store timestamps in **UTC**. The app converts to local time.
3. Use a timestamp type with time zone (`TIMESTAMPTZ`).

---

#### 10. Subqueries, CTEs, Window Functions — 🟡 Good to Know

*Common in SQL interviews.*

```sql
-- Latest post per user, using a CTE and ROW_NUMBER
WITH ranked AS (
  SELECT user_id, title,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
  FROM posts
)
SELECT user_id, title FROM ranked WHERE rn = 1;
```

1. **Subquery** — a query inside another query.
2. **CTE** (`WITH`) — a named subquery that makes long queries readable.
3. **Window function** — calculates across related rows without collapsing them (`ROW_NUMBER`, `RANK`).

---

#### 11. Schema Migrations — 🟡 Good to Know

1. A **migration** is a versioned script that changes the schema (`001_create_users.sql`).
2. Keep them in Git and run them automatically on deploy.
3. Never edit the database by hand in production.
4. Make changes **backward compatible** (add a column first, remove the old one later).

---

#### 12. Soft Delete — 🟡 Good to Know

1. Instead of deleting the row, set `deleted_at`.
2. Good for undo and audit.
3. Cost: every query must filter deleted rows, and unique rules get harder.

---

#### 13. Common Interview Questions

1. **Design a schema for users, posts, and likes.**
   Tables `users`, `posts` (FK `user_id`), and `likes` (join table with a composite primary key).
2. **INNER vs LEFT JOIN?**
   INNER returns only matches. LEFT returns all left rows, with NULL where there is no match.
3. **One-to-many vs many-to-many?**
   One-to-many uses a FK on the many side. Many-to-many needs a join table.
4. **Normalization vs denormalization?**
   Normalization avoids duplication. Denormalization copies data for faster reads but must be kept in sync.
5. **How do you store money and time?**
   Integer cents or DECIMAL, never float. Timestamps in UTC.
6. **What does NULL do in comparisons?**
   `NULL = NULL` is not true. Use `IS NULL`.
7. **Write a query to count posts per user, including users with none.**
   `LEFT JOIN` + `GROUP BY` + `COUNT(p.id)`.

---

#### 14. Common Mistakes

1. `UPDATE` or `DELETE` without `WHERE`.
2. Using `FLOAT` for money.
3. Storing local time instead of UTC.
4. No constraints (duplicates and orphan rows appear).
5. Designing tables without thinking about the queries.
6. Comparing with `= NULL`.
7. Using `SELECT *` everywhere.

---

#### 15. Related Topics

1. `06` Backend Security Essentials (parameterized queries)
2. `09` Connecting API to Database
3. `10` Indexes & Query Performance
4. `11` Transactions & Concurrency
5. Choosing a database, sharding (system design roadmap)

---

#### 16. Interview Must Remember

1. **PK, FK, constraints** keep data correct.
2. **JOIN** types and **GROUP BY** are asked in almost every backend interview.
3. **One-to-many** = FK. **Many-to-many** = join table.
4. **Design from the queries.**
5. Normalize first, **denormalize only when measured**.
6. **Money = cents/DECIMAL. Time = UTC.**
