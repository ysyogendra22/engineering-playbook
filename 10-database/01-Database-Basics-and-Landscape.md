# Database Basics & Landscape

Roadmap topic 1 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** a database's whole job is three things — store data so it isn't lost, find it fast, and never let it become wrong. Everything else in this folder is really just detail on how those three promises are kept.

---

#### 1. What a Database Does — 🟢 Must Know

*The three-part definition worth having ready.*

1. **Store data safely** — survives crashes, restarts, and hardware failure.
2. **Find it fast** — indexes and query engines exist so you don't scan everything every time.
3. **Keep it correct** — constraints and transactions (topics `2`, `8`) stop the data from silently becoming wrong.

---

#### 2. Core Vocabulary — 🟢 Must Know

**DBMS** (database management system) — the software itself. **Database** — a named collection of data. **Table** — rows of the same shape. **Row** — one record. **Column** — one field of that record. **Schema** — the structure: tables, columns, types, constraints (topic `2`). **Query** — a request for data or a change to it.

---

#### 3. Relational vs Non-Relational, at a Glance — 🟢 Must Know

| | Relational (SQL) | Non-relational (NoSQL) |
|---|---|---|
| Structure | Fixed schema, tables, rows | Flexible — documents, key-value, graph, and more |
| Relationships | Joins across tables | Usually embedded or handled in application code |
| Consistency | Strong, by default | Often eventual, by default |
| Best for | Most application data | Specific access patterns at extreme scale, or flexible schemas |

Full depth on when to actually choose each in topic `11`.

---

#### 4. Client-Server vs Embedded — 🟢 Must Know

1. **Client-server** (PostgreSQL, MySQL) — the database runs as its own server process; apps connect to it over the network.
2. **Embedded** (SQLite) — the database runs *inside* the application's own process, reading and writing a local file directly — no separate server. This is exactly why SQLite is the database on your phone (topic `21`), not a network service.

---

#### 5. OLTP vs OLAP — 🟢 Must Know

**OLTP** (online transaction processing) — many small, fast reads and writes; the shape of almost every application database. **OLAP** (online analytical processing) — large, complex queries over historical data, usually run against a separate system (topic `20`) so analytics never competes with production traffic.

---

#### 6. Why the App Talks to a Database Only Through a Backend — 🟢 Must Know

The same rule from `BE 1`: the app never gets direct database credentials. A backend sits in between, checking permissions and validating input before anything touches the database — this is the foundation everything in this folder assumes.

---

#### 7. A Short History — 🟡 Good to Know

Relational databases dominated for decades because they solved the general case well. NoSQL databases emerged to solve specific, extreme-scale or flexible-schema problems that relational databases handled poorly — not as a universal "better" replacement, but as specialised tools for specific jobs (topic `12`).

---

#### 8. SQL Dialect Differences — 🟡 Good to Know

PostgreSQL, MySQL, and SQLite each have their own small syntax differences (data types, some functions, some clauses) on top of standard SQL — worth knowing they exist so you're not surprised when moving between them, without needing to memorise every difference.

---

#### 9. Managed Services vs Running Your Own — 🟡 Good to Know

A managed database service (a cloud provider running and patching it for you) trades cost and some control for far less operational burden — the same build-vs-buy trade-off from `ARCH 3`, applied to databases specifically.

---

#### 10. Common Interview Questions

1. **What does a database actually do, at a high level?**
   Stores data safely (survives failures), finds it fast (indexes and query engines), and keeps it correct (constraints and transactions).
2. **What's the difference between a client-server and an embedded database?**
   Client-server runs as its own process and apps connect over the network (PostgreSQL). Embedded runs inside the application's own process, reading and writing a local file directly (SQLite) — no separate server needed.
3. **OLTP vs OLAP?**
   OLTP is many small, fast transactions — typical app usage. OLAP is large analytical queries over historical data, usually run on a separate system so it doesn't compete with production traffic.
4. **Why doesn't a mobile app connect directly to a production database?**
   The backend is the trust boundary — it checks permissions and validates input before anything touches the database; direct access would expose credentials and bypass every safety check.

---

#### 11. Common Mistakes

1. Treating "NoSQL" as a single thing, rather than several very different families solving different problems (topic `12`).
2. Running analytical queries directly against the production OLTP database.
3. An app or client with direct database credentials.
4. Assuming SQL is identical across PostgreSQL, MySQL, and SQLite.

---

#### 12. Related Topics

1. `2` Relational Model & Data Modeling — the structure inside a relational database
2. `11` Choosing a Database — the fuller relational-vs-NoSQL decision process
3. `21` Mobile Databases — SQLite as the embedded database on every phone
4. `BE 1` Client-Server Request Flow — why the app never gets direct database access

---

#### 13. Interview Must Remember

1. **Store safely, find fast, keep correct** — the three-part job of any database.
2. **Client-server vs embedded** — SQLite is embedded, which is why it's the phone database.
3. **OLTP vs OLAP** — everyday transactions vs large-scale analysis, usually on separate systems.
4. **The app never gets direct database access** — the backend is the trust boundary.
