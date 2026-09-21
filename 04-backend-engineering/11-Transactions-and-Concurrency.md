# Transactions & Concurrency

Roadmap topic 11 · Stage 3: Data

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** many users change the same data at the same time. Transactions keep the data correct, and locks or atomic updates stop two users from breaking each other's work.

---

#### 1. Transaction, Commit, Rollback — 🟢 Must Know

*A group of steps that succeed together or fail together.*

Example: transfer money.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;      -- both changes are saved
-- If anything fails: ROLLBACK;  → nothing is saved
```

Without a transaction, a crash between the two updates loses money.

---

#### 2. ACID — 🟢 Must Know

*Four promises a database transaction makes.*

| Letter | Meaning | Simple example |
|---|---|---|
| **A**tomicity | All or nothing | Both transfer steps happen, or neither |
| **C**onsistency | Rules stay true | Balance can't go below zero if that is a rule |
| **I**solation | Concurrent transactions don't disturb each other | Two transfers don't mix half-done states |
| **D**urability | Committed data survives a crash | After `COMMIT`, a power cut loses nothing |

---

#### 3. Race Condition — 🟢 Must Know

*Two requests read the same value, both decide it is fine, and both write.*

Example: one seat left, two users book at the same time.

```text
User A: read seat → free
User B: read seat → free
User A: book seat  ✓
User B: book seat  ✓      ← double booking!
```

Same bug: stock goes negative, a coupon is used twice, a balance is overwritten.

---

#### 4. Atomic Updates & Unique Constraints — 🟢 Must Know

*Let the database do the check and the change in one step.*

```sql
-- Book the seat only if it is still free
UPDATE seats SET booked_by = 7
WHERE id = 12 AND booked_by IS NULL;
-- 1 row updated → success | 0 rows → already taken → return 409

-- Reduce stock, never below zero
UPDATE products SET stock = stock - 1
WHERE id = 5 AND stock > 0;
```

**Unique constraint** as protection:

```sql
UNIQUE (show_id, seat_id)     -- the database rejects a second booking
```

Catch the violation and return `409 Conflict`. This is simple and very reliable.

---

#### 5. Optimistic Locking — 🟢 Must Know

*Assume there is no conflict. Check when saving.*

1. Add a `version` column to the row.
2. Read the row (with its version).
3. Save only if the version is unchanged, and increase it.

```sql
UPDATE notes
SET title = 'New', version = version + 1
WHERE id = 5 AND version = 3;
-- 0 rows updated → someone else changed it → conflict: retry or return 409
```

Good when conflicts are **rare** (editing your own note). No waiting.

---

#### 6. Pessimistic Locking — 🟢 Must Know

*Lock the row first, so others must wait.*

```sql
BEGIN;
SELECT * FROM seats WHERE id = 12 FOR UPDATE;   -- locks the row
-- check and update safely
COMMIT;                                         -- releases the lock
```

Good when conflicts are **common** (a popular ticket). Cost: waiting, and risk of deadlocks. Keep the transaction short.

| | Optimistic | Pessimistic |
|---|---|---|
| Idea | Detect conflict at save | Prevent conflict with a lock |
| Waiting | No | Yes |
| Best when | Conflicts are rare | Conflicts are common |

---

#### 7. Isolation Levels — 🟡 Good to Know

*How much can concurrent transactions see of each other? Higher = safer but slower.*

| Level | Idea |
|---|---|
| Read committed | See only committed data (the common default) |
| Repeatable read | The same row reads the same within a transaction |
| Serializable | As if transactions ran one by one |

Problems the levels prevent:

1. **Dirty read** — reading data that was not yet committed.
2. **Non-repeatable read** — the same row changes between two reads.
3. **Phantom read** — new rows appear between two reads.

For most cases: atomic updates and constraints are simpler than raising the isolation level.

---

#### 8. Deadlocks & Retries — 🟡 Good to Know

*Two transactions wait for each other. The database stops one, and you retry.*

1. **Deadlock** — A waits for B and B waits for A. The database stops one of them with an error.
2. **Retry** the failed transaction a **limited** number of times.
3. Reduce deadlocks: lock rows in the same order, keep transactions short.
4. Don't call slow external services (payment API, email) **inside** a transaction. It holds locks for too long.

---

#### 9. Common Interview Questions

1. **What is a transaction? What is ACID?**
   A group of steps that all succeed or all fail. ACID = atomicity, consistency, isolation, durability.
2. **Two users book the last seat at the same time. How do you prevent a double booking?**
   Atomic update (`WHERE booked_by IS NULL`) and a unique constraint, or a row lock (`FOR UPDATE`).
3. **Optimistic vs pessimistic locking?**
   Optimistic checks a version at save (no waiting, good when conflicts are rare). Pessimistic locks first (waiting, good when conflicts are common).
4. **How do you stop stock going negative?**
   `UPDATE ... SET stock = stock - 1 WHERE stock > 0` and check the row count.
5. **What is a deadlock?**
   Two transactions wait for each other. The database aborts one. Retry, keep transactions short, lock in a consistent order.
6. **Why not call an external API inside a transaction?**
   It is slow, holds locks, and can't be rolled back.

---

#### 10. Common Mistakes

1. Read → check in code → write (a race condition).
2. Relying only on app-level checks and no database constraint.
3. Long transactions.
4. External calls inside transactions.
5. Retrying forever.
6. Forgetting to handle the "0 rows updated" case.

---

#### 11. Related Topics

1. `08` Databases, SQL & Data Modeling (constraints)
2. `09` Connecting API to Database
3. `03` API Design (idempotency, `409`)
4. Idempotency, queues, distributed consistency (system design roadmap)

---

#### 12. Interview Must Remember

1. **ACID**, and **commit/rollback**.
2. Race condition = **read-check-write** with two users.
3. Fixes: **atomic update, unique constraint, optimistic lock, pessimistic lock**.
4. **Optimistic** = version column. **Pessimistic** = `FOR UPDATE`.
5. Keep transactions **short**; no external calls inside.
6. Retry deadlocks a **limited** number of times.
