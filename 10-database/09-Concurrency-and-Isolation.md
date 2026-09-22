# Concurrency & Isolation

Roadmap topic 9 · Stage 3: Correctness

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** the moment two requests can touch the same row at the same time, correctness gets genuinely hard — this topic is about the specific, named ways that goes wrong, and the two main tools (locking, versioning) for stopping it.

---

#### 1. Race Conditions — 🟢 Must Know

A **race condition** produces a wrong result because two operations interleave in an unlucky order.

```text
Double booking:
  Request A: check seat 5 is free → yes
  Request B: check seat 5 is free → yes   (before A has booked it)
  Request A: book seat 5
  Request B: book seat 5   ← both succeed, seat is double-booked
```

Also common: **lost update** (topic `8`, item 5) and **double spend** (the payment version of double booking).

---

#### 2. Isolation Levels — 🟢 Must Know

| Level | Guarantees |
|---|---|
| Read committed | Never see uncommitted data from another transaction |
| Repeatable read | The same query, run twice in one transaction, sees the same rows |
| Serializable | Transactions behave as if run one at a time, in some order |

Stronger isolation = fewer possible anomalies, but generally more locking/conflict overhead — a real trade-off (item 8).

---

#### 3. Anomalies — 🟢 Must Know

1. **Dirty read** — seeing another transaction's uncommitted change.
2. **Non-repeatable read** — re-reading the same row within a transaction gives a different value, because another transaction committed a change in between.
3. **Phantom read** — re-running the same query within a transaction returns a different *set* of rows (a new one appeared).
4. **Lost update** — two writers both read the same value, then both write, and one overwrite silently erases the other's change.
5. **Write skew** — two transactions each check a rule independently (both pass), then both write, and the **combination** breaks the rule neither one violated alone.

---

#### 4. Optimistic vs Pessimistic Locking — 🟢 Must Know

```sql
-- Optimistic: check a version column at write time, don't lock while reading
UPDATE notes SET title = $1, version = version + 1
WHERE id = $2 AND version = $3;   -- fails (0 rows updated) if version has moved on

-- Pessimistic: lock the row up front, for the rest of the transaction
BEGIN;
SELECT * FROM notes WHERE id = $1 FOR UPDATE;   -- other transactions wait here
UPDATE notes SET title = $2 WHERE id = $1;
COMMIT;
```

1. **Optimistic** — assume conflicts are rare; check at write time, retry on conflict. Good for low-contention data.
2. **Pessimistic** — lock the row before reading, so nobody else can touch it until you're done. Good for high-contention data where retries would be common and wasteful.

---

#### 5. Row Locks, Table Locks — 🟢 Must Know

A **row lock** blocks other transactions from modifying (sometimes also reading) that one specific row. A **table lock** blocks operations on the entire table — much more disruptive, and reached for only when genuinely needed (a schema change, for example).

---

#### 6. Deadlocks — 🟢 Must Know

```text
Transaction A: locks row 1, then wants row 2
Transaction B: locks row 2, then wants row 1
→ each waits for the other forever → deadlock
```

The database detects this and forcibly **rolls back one transaction** to break the cycle — the correct application response is to **catch that error and retry** the rolled-back transaction, not treat it as a hard failure.

---

#### 7. MVCC: Readers Don't Block Writers — 🟡 Good to Know

By keeping multiple versions of a row (`7`, item 8), a reader can see a consistent snapshot without blocking a concurrent writer, and vice versa — this is *why* modern relational databases handle high concurrency well without every read needing a lock.

---

#### 8. Choosing an Isolation Level — 🟡 Good to Know

Higher isolation levels catch more anomalies automatically, at the cost of more conflicts, retries, or blocking under contention. **Read committed** is often the practical default; reach for **serializable** specifically for the cases (like write skew, item 3) that lower levels don't protect against.

---

#### 9. Advisory Locks and `SKIP LOCKED` — 🟡 Good to Know

**Advisory locks** — application-defined locks not tied to a specific row, useful for coordinating work outside the normal row-locking model. **`SKIP LOCKED`** — when reading rows to process (a job queue table), skip any row another worker already has locked, rather than waiting — a common, efficient pattern for building a simple queue directly on a relational table.

---

#### 10. Ticket Booking and Inventory Patterns — 🟡 Good to Know

The canonical concurrency interview problem (`SD 32`): prevent double booking with either a unique constraint (a seat can only be booked once — enforced at the database level) or `SELECT ... FOR UPDATE` to lock the seat row while checking and booking it.

---

#### 11. Long-Running Transactions and Side Effects — 🟡 Good to Know

A transaction held open for a long time doesn't just risk its own timeout — it holds locks that block **other** transactions, and (in MVCC systems) can prevent old row versions from being cleaned up, contributing to bloat (`7`, item 8). Keep transactions short (`8`, item 4) partly for this reason too.

---

#### 12. Common Interview Questions

1. **How would you prevent double booking a seat?**
   Either a unique constraint on the seat/event combination (the database rejects a second booking outright), or `SELECT ... FOR UPDATE` to lock the seat row while checking availability and booking it — pick based on expected contention.
2. **What's the difference between optimistic and pessimistic locking?**
   Optimistic checks a version at write time and retries on conflict, assuming conflicts are rare. Pessimistic locks the row up front, assuming conflicts are common enough that waiting is cheaper than retrying.
3. **Explain dirty read, non-repeatable read, and phantom read.**
   Dirty read sees uncommitted data. Non-repeatable read sees a changed value on re-read within the same transaction. Phantom read sees a changed *set* of rows on re-query within the same transaction.
4. **What causes a deadlock, and how should the application handle one?**
   Two transactions each hold a lock the other needs, waiting on each other forever. The database detects and rolls back one automatically; the application should catch that error and retry.
5. **What is write skew, and why don't lower isolation levels catch it?**
   Two transactions each independently check a rule (both pass) and then both write, and the combination breaks the rule — lower isolation levels don't see the other transaction's read, only conflicting writes, so this passes undetected without serializable isolation.

---

#### 13. Common Mistakes

1. Read-modify-write in application code where an atomic update or explicit locking was needed.
2. Not handling a deadlock error by retrying, treating it as a fatal failure instead.
3. Choosing pessimistic locking for low-contention data, adding unnecessary blocking.
4. Assuming "read committed" (a common default) protects against every anomaly, including write skew.

---

#### 14. Related Topics

1. `8` Transactions & ACID — the isolation guarantee this topic expands on
2. `7` Storage Engines & Internals — MVCC, introduced there
3. `BE 11` Transactions & Concurrency — the same core content, first pass
4. `SD 32` Practice: Projects & Designs — the ticket-booking practice problem

---

#### 15. Interview Must Remember

1. **Know the anomalies by name**: dirty read, non-repeatable read, phantom read, lost update, write skew.
2. **Optimistic (version check, retry) vs pessimistic (`FOR UPDATE`, lock first)** — pick based on contention.
3. **Deadlocks are detected and one side is rolled back — catch it and retry.**
4. **MVCC lets readers and writers avoid blocking each other**, most of the time.
