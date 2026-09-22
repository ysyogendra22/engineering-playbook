# Practice: Projects & Exercises

Roadmap topic 23 · Stage 8: Interview & Practice

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** every topic in this folder becomes real once you've actually broken something and fixed it — a real slow query, a real race condition you watched happen in two terminals. This is where that happens.

---

#### 1. Notes App Schema — 🟢 Must Know

Using the Notes API from `BE 12`: design the full schema — tables, keys, constraints — and write it as a **real migration file** (topic `10`), not just a `CREATE TABLE` script run by hand.

```sql
-- 001_create_notes_schema.sql
CREATE TABLE users (id UUID PRIMARY KEY, email TEXT UNIQUE NOT NULL);
CREATE TABLE notes (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id),
    title TEXT NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_notes_user_created ON notes (user_id, created_at DESC);
```

---

#### 2. Load 100,000 Rows, Find and Fix Three Slow Queries — 🟢 Must Know

Generate a realistic amount of test data, write a few queries you'd expect to be common (a user's recent notes, a search by title), run `EXPLAIN ANALYZE` on each, and fix at least three that come back slow — with indexes (topic `5`), following the "measure, one change, measure again" discipline from topic `6`.

---

#### 3. Reservation Table: Prevent Double Booking — 🟢 Must Know

Build a small reservation system, then implement double-booking prevention **two ways** (topic `9`): first with a unique constraint (simplest), then with `SELECT ... FOR UPDATE` pessimistic locking — and actually test it with two concurrent requests (item 4 in the exercises below) to confirm both approaches genuinely work.

---

#### 4. Money Transfer: Two Accounts, a Transaction, Concurrent Test — 🟢 Must Know

```sql
BEGIN;
UPDATE accounts SET balance_cents = balance_cents - 500 WHERE id = 1 AND balance_cents >= 500;
UPDATE accounts SET balance_cents = balance_cents + 500 WHERE id = 2;
COMMIT;
```

Wrap this in a transaction (topic `8`), then genuinely test it with **concurrent requests** hitting the same account — open two terminals (or write a small concurrent test script) and confirm the balance never goes negative and no money is created or destroyed.

---

#### 5. Add a Read Replica Locally — 🟡 Good to Know

Set up a local read replica (`14`) and deliberately watch **replication lag** happen — write to the leader, immediately read from the replica, and observe the brief window where the write isn't there yet.

---

#### 6. Cache a Query in Redis — 🟡 Good to Know

Implement cache-aside (`13`) for one of your notes queries: check Redis first, fall back to PostgreSQL on a miss, set a TTL, and invalidate on write — then measure the actual speed difference.

---

#### 7. A Backup and a Full Restore, Timed — 🟡 Good to Know

Take a real backup, then actually restore it to a fresh database and **time the whole process** (`17`) — the single best way to internalise why "untested backups are only a guess".

---

#### 8. Room or SQLite in an App — 🟡 Good to Know

Entities, a migration, and an offline sync stub (topic `21`) — connects this folder's theory directly to `06-mobile-engineering`'s concrete implementation.

---

#### 9. SQL Exercises — 🟢 Must Know

1. 🟢 **Joins, group by, having** on a small shop dataset (users, orders, products) — practise the fundamentals from topic `3` until they're fluent, not just understood.
2. 🟢 **Window functions**: top N per group, running total, latest row per user (topic `4`).
3. 🟡 A **recursive query** for a comment tree (topic `4`, item 5).
4. 🟡 **Rewrite a slow query three different ways** and compare their execution plans side by side (topic `6`).

---

#### 10. Schema Designs to Practise — 🟢 Must Know

*Work through each fully: entities, keys, relationships, top queries, indexes — say it out loud, timed.*

1. 🟢 **Notes app** — the running example throughout this folder.
2. 🟢 **E-commerce**: users, products, orders, payments — a good exercise in relationships and money-handling (topic `2`, item 8).
3. 🟢 **Ticket or seat booking** — the concurrency exercise from item 3, as a full schema design.
4. 🟢 **Chat**: users, conversations, messages — ordering, pagination (topic `3`, item 7), and real-time considerations (`SD 24`).
5. 🟡 **Social feed and followers** — a good exercise in denormalization trade-offs (topic `2`, item 6).
6. 🟡 **URL shortener** — a classic, ID-generation-focused design (`SD 20`).
7. 🟡 **Multi-tenant app** — apply topic `18`'s multi-tenancy isolation options.

---

#### 11. How to Practise Each Exercise — 🟢 Must Know

```text
1. Set a timer.
2. Actually run it against a real PostgreSQL instance — don't just write
   the SQL and assume it's correct.
3. For concurrency exercises, genuinely open two terminals/connections —
   watching a race condition happen for real teaches more than reading
   about it ever will.
4. Say your reasoning out loud as you go (topic 22).
5. Afterward, write down one thing that surprised you.
```

---

#### 12. Common Interview Questions

*This topic is the practice ground — a couple of meta-questions do come up:*

1. **"Walk me through a database problem you actually debugged."** — use the slow-query exercise (item 2) or a real one from your own work, following the `EXPLAIN`-first structure from topic `6`.
2. **"Have you seen a race condition happen firsthand?"** — the double-booking or money-transfer concurrency exercises (items 3, 4) give you a genuine, specific answer instead of only theory.

---

#### 13. Common Mistakes

1. Reading about indexes and transactions without ever running `EXPLAIN` or watching a real race condition happen.
2. Skipping the concurrency exercises because they take more setup — they're exactly where the real understanding comes from.
3. Practising schema designs silently instead of out loud, timed.
4. Never actually timing a backup-and-restore, so "test your backups" stays abstract advice.

---

#### 14. Related Topics

1. `BE 12` Checkpoint Project: Notes API — the shared example system this folder's projects extend
2. `22` Database Interview Answer Points — the structure every exercise here should be narrated with
3. `06-mobile-engineering/9`, `06-mobile-engineering/12` — the mobile-side extension of item 8

---

#### 15. Interview Must Remember

1. **Run everything against a real database** — don't just write SQL and assume it's correct.
2. **Actually watch a race condition happen** with two real concurrent connections.
3. **Time a real backup and restore** — this is what makes "test your backups" a real habit, not just advice.
4. **Practise schema designs out loud, timed**, the same discipline as every other folder's interview prep.
