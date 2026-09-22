# Transactions & ACID

Roadmap topic 8 · Stage 3: Correctness

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** a transaction is a promise — either every change inside it happens, or none of them do, even if the power goes out halfway through. ACID is the formal name for that promise's four parts.

---

#### 1. `BEGIN`, `COMMIT`, `ROLLBACK` — 🟢 Must Know

```sql
BEGIN;
UPDATE accounts SET balance_cents = balance_cents - 500 WHERE id = 1;
UPDATE accounts SET balance_cents = balance_cents + 500 WHERE id = 2;
COMMIT;   -- both changes become permanent together, or...
-- ROLLBACK;  -- ...neither does, if something went wrong
```

---

#### 2. ACID — 🟢 Must Know

| Letter | Meaning | Plain example |
|---|---|---|
| **A**tomicity | All-or-nothing | Both sides of a money transfer happen, or neither does |
| **C**onsistency | Rules always hold | A `CHECK (balance >= 0)` constraint is never violated, even mid-transaction |
| **I**solation | Concurrent transactions don't corrupt each other | Two transfers happening at once don't see each other's half-finished state (topic `9`) |
| **D**urability | Once committed, it survives a crash | Guaranteed by the write-ahead log (`7`, item 2) |

---

#### 3. Where to Put the Transaction Boundary — 🟢 Must Know

*The application-code question this topic ultimately serves (`BE 9`).*

Keep the transaction boundary as **tight as possible** around the actual database changes that must be atomic together — not around unrelated work that happens to be nearby in the code.

---

#### 4. Keep Transactions Short — 🟢 Must Know

*The single most important operational rule in this topic.*

**Never call a slow external service (an HTTP request, an email send) inside an open transaction.** A long-held transaction holds locks (topic `9`) the whole time, blocking other work and risking a pile-up of waiting connections if the external call is slow or hangs.

```text
Bad:   BEGIN → update row → call external API (slow!) → COMMIT
                                        ↑ locks held this whole time

Good:  BEGIN → update row → COMMIT → call external API afterward
```

---

#### 5. Atomic Updates Instead of Read-Modify-Write — 🟢 Must Know

```sql
-- Race-prone: read, compute in application code, write back
-- (another transaction could change the value in between)
SELECT balance_cents FROM accounts WHERE id = 1;   -- read: 1000
-- application computes: 1000 - 500 = 500
UPDATE accounts SET balance_cents = 500 WHERE id = 1;   -- write — may overwrite a concurrent change

-- Safe: let the database do the read-and-update atomically, in one statement
UPDATE accounts SET balance_cents = balance_cents - 500 WHERE id = 1;
```

The second form is a single atomic operation — no window where a concurrent transaction could interleave and cause a lost update (topic `9`).

---

#### 6. Unique Constraints and Idempotency Keys — 🟢 Must Know

A unique constraint (`2`, item 7) is a simple, strong tool for stopping duplicates — attempting to insert a payment with an already-used **idempotency key** fails cleanly at the database level, rather than needing fragile application-side duplicate-checking logic (`BE 11`).

```sql
CREATE TABLE payments (
    idempotency_key TEXT UNIQUE NOT NULL,
    amount_cents INTEGER NOT NULL
    -- ...
);
-- A retried request with the same key gets a clean constraint violation,
-- not a duplicate payment.
```

---

#### 7. Savepoints — 🟡 Good to Know

A named point inside a transaction you can roll back **to**, without rolling back the entire transaction — useful for handling a partial failure within a larger, multi-step transaction while keeping the earlier steps intact.

---

#### 8. Autocommit and Dying Connections — 🟡 Good to Know

Without an explicit `BEGIN`, many database clients run in **autocommit** mode — each statement is its own implicit transaction. If a connection dies mid-transaction (before `COMMIT`), the whole transaction is automatically rolled back — worth knowing so an unexpected disconnect doesn't leave data in a confusing, half-applied state.

---

#### 9. Durability Settings and Their Cost — 🟡 Good to Know

Some databases let you trade a small amount of durability guarantee for higher write throughput (a less strict `fsync` setting, `7` item 9) — a real, explicit trade-off between speed and "how certain are we this survives a crash", not a free performance win.

---

#### 10. Transactions in an ORM — 🟡 Good to Know

ORMs often manage transaction boundaries implicitly, which can hide problems: a transaction left open longer than intended, or several unrelated operations accidentally sharing one transaction — worth understanding what your specific ORM actually does under the hood, not just trusting it blindly.

---

#### 11. Common Interview Questions

1. **What does ACID stand for, and can you give an example of each?**
   Atomicity (all-or-nothing, like a money transfer), Consistency (constraints always hold), Isolation (concurrent transactions don't corrupt each other's view), Durability (a commit survives a crash, via the WAL).
2. **Why should you never call an external service inside a transaction?**
   The transaction holds locks the whole time it's open; a slow or hanging external call extends that lock hold indefinitely, blocking other work and risking connection pool exhaustion.
3. **Why is `UPDATE balance = balance - 100` safer than reading, computing, then writing back?**
   The database performs the read-and-update as one atomic operation — no window exists for a concurrent transaction to interleave and cause a lost update.
4. **How would you make a payment endpoint safe to retry?**
   A unique constraint on an idempotency key — a retried request with the same key fails cleanly at the database level instead of creating a duplicate payment.

---

#### 12. Common Mistakes

1. Calling a slow external service inside an open transaction.
2. Read-modify-write in application code for a value that could change concurrently, instead of an atomic `UPDATE`.
3. No idempotency mechanism for a retriable, side-effecting operation.
4. Transactions left open far longer than the actual related work requires, especially via ORM defaults not fully understood.

---

#### 13. Related Topics

1. `7` Storage Engines & Internals — the WAL that makes durability possible
2. `9` Concurrency & Isolation — isolation, in full depth
3. `BE 9` Connecting API to Database — where the transaction boundary lives in application code
4. `BE 11` Transactions & Concurrency — the same core content, first pass

---

#### 14. Interview Must Remember

1. **ACID**: atomicity, consistency, isolation, durability — know an example of each.
2. **Never call a slow external service inside an open transaction.**
3. **Atomic `UPDATE`**, not read-modify-write, for concurrent-safe changes.
4. **Unique constraint + idempotency key** to make a write safely retriable.
