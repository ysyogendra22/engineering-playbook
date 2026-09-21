# Connecting API to Database

Roadmap topic 9 · Stage 3: Data

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** the API code talks to the database through a driver and a limited pool of connections. Know how to do it efficiently (no N+1) and how to turn database errors into clean API errors.

---

#### 1. The Path of a Request to the Database — 🟢 Must Know

```text
Controller → Service → Repository → Connection Pool → Database
```

1. Only the **repository** layer talks to the database (topic `04`).
2. A **driver** (or ORM) sends the SQL and returns the rows.
3. The connection comes from a **pool**.

---

#### 2. Connection Pool — 🟢 Must Know

*Opening a connection is slow. Keep a few open and reuse them, like a set of shared taxis.*

1. Opening a database connection (network + login) is expensive.
2. A **pool** keeps N connections open. A request **borrows** one and **returns** it.
3. Pool size is **small and limited** (for example 10–20 per server), because the database can only handle so many.
4. If all connections are busy, new requests **wait**, and can time out.
5. Always release connections (frameworks do this for you). A leak = slowly frozen server.

```text
Request A → borrow conn 1 → query → return
Request B → borrow conn 2 → query → return
Pool full → Request C waits
```

---

#### 3. ORM Basics — 🟢 Must Know

*An ORM maps table rows to objects. Room (Android) and Core Data (iOS) are the same idea on the app side.*

1. **ORM** = Object-Relational Mapper (Hibernate/JPA, Exposed, Prisma, SQLAlchemy).
2. Benefits: less boilerplate, type safety, easy simple queries.
3. Risks: hidden slow queries (N+1), and people forget SQL.
4. **Learn SQL first.** Turn on SQL logging and read what your ORM sends.
5. For complex or performance-critical queries, write SQL directly (still parameterized).

---

#### 4. N+1 Query Problem — 🟢 Must Know

*One query for the list, then one more query for every item.*

```text
1 query : SELECT * FROM posts LIMIT 20
20 queries: SELECT * FROM users WHERE id = ?   (once per post, for the author)
→ 21 queries for one screen
```

Fix: get the data together.

```sql
-- One query with a JOIN
SELECT p.id, p.title, u.name
FROM posts p JOIN users u ON u.id = p.user_id
LIMIT 20;

-- Or two queries: posts, then authors with IN (...)
SELECT * FROM users WHERE id IN (1, 2, 3, ...);
```

1. It is invisible in small tests and painful with real data.
2. Spot it by logging the number of queries per request.
3. ORM fix: eager loading, fetch join, or batch loading.

---

#### 5. Missing Records & Constraint Errors — 🟢 Must Know

*Turn database errors into clear API errors.*

| Database situation | API response |
|---|---|
| No row found | `404 Not Found` |
| Unique violation (email exists) | `409 Conflict` |
| Foreign key violation (parent doesn't exist) | `400` or `409` |
| Not-null violation | `400` (validate earlier) |
| Connection or timeout error | `503` / `500` |

1. Catch database exceptions in the repository or the central error handler.
2. Never send raw SQL errors to the client.
3. Prefer catching the **unique violation** over "check first, then insert" (the check can race).

---

#### 6. Connection Limits with Many Servers — 🟡 Good to Know

1. The database has a **maximum number of connections** (for example, PostgreSQL defaults to 100).
2. `servers × pool size` must stay below that limit.
3. When you add servers, you can suddenly run out of connections.
4. Fix: smaller pools, or a **connection pooler** (like PgBouncer).

---

#### 7. Common Interview Questions

1. **Why use a connection pool?**
   Opening connections is expensive. A pool reuses a few connections and protects the database from too many.
2. **What is the N+1 problem? How do you fix it?**
   One query for the list plus one per item. Fix with a join, batch fetch (`IN`), or eager loading.
3. **ORM vs raw SQL?**
   ORM saves boilerplate but can hide slow queries. Know the SQL it generates and use raw SQL for complex queries.
4. **How do you handle a duplicate email?**
   Unique constraint → catch the violation → return `409 Conflict`.
5. **What if the database is slow or down?**
   Timeouts, error responses (`503`), pool limits so requests don't pile up, and monitoring.
6. **The endpoint is slow. What do you check first?**
   Number of queries (N+1), missing indexes, and the amount of data returned.

---

#### 8. Common Mistakes

1. N+1 queries.
2. No pool limits, or a pool that is too big.
3. Not releasing connections.
4. Exposing raw database errors.
5. Checking for duplicates in code only, with no unique constraint.
6. Fetching whole tables and filtering in the app.

---

#### 9. Related Topics

1. `04` Backend Building Blocks (layers)
2. `08` Databases, SQL & Data Modeling
3. `10` Indexes & Query Performance
4. `11` Transactions & Concurrency
5. Replication, caching (system design roadmap)

---

#### 10. Interview Must Remember

1. **Connection pool** = reuse a limited set of connections.
2. **N+1** = the classic hidden slowness. Use joins or batch queries.
3. **Learn SQL first**, and know what your ORM generates.
4. Map DB errors: **not found → 404, duplicate → 409**.
5. `servers × pool size` must fit within the database's limit.
