# Storage Engines & Internals

Roadmap topic 7 · Stage 2: Performance

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** understanding roughly how a database actually stores and retrieves data on disk explains *why* indexes, transactions, and crash recovery all work the way they do — it turns memorised rules into things you can reason about from first principles.

---

#### 1. How Data Lives on Disk — 🟢 Must Know

Data is stored in fixed-size **pages** (often 4-16 KB), containing multiple rows. **Disk is slow, memory is fast** — this single fact drives most of the design decisions in this topic: minimise disk reads, keep hot data in memory, and write efficiently.

---

#### 2. Write-Ahead Log (WAL) — 🟢 Must Know

*The mechanism that makes crash recovery possible.*

Before a change is applied to the actual data files, it's first written to a sequential **log**. If the database crashes mid-write, it can replay the log on restart to recover exactly what was in progress — this is also the mechanism behind point-in-time recovery (`17`, item 3) and often behind replication (`14`).

```text
1. Change arrives (e.g., UPDATE)
2. Write the change to the WAL first (fast, sequential write)
3. Acknowledge the transaction as committed
4. Apply the change to the actual data pages (can happen slightly later)
5. On crash: replay the WAL from the last checkpoint to recover
```

---

#### 3. Buffer Pool / Page Cache — 🟢 Must Know

Frequently accessed ("hot") pages are kept in memory, in the **buffer pool**, so repeated reads don't hit disk every time. This is a large part of why a database "warms up" after restart — the cache starts empty and gradually fills with the working set of hot data.

---

#### 4. B-Tree Engines vs LSM-Tree Engines — 🟢 Must Know

| | B-tree engine | LSM-tree engine |
|---|---|---|
| Optimised for | Reads (and balanced read/write) | Writes |
| Write pattern | Updates data in place | Appends to memory, flushes to sorted files, merges later |
| Used by | PostgreSQL, MySQL (default) | Cassandra, RocksDB, many time-series databases |

**Read-optimised vs write-optimised** — B-tree engines are the sensible default for most application databases; LSM-tree engines shine for very write-heavy workloads (logging, metrics, event streams).

---

#### 5. Crash Recovery, in Plain Words — 🟢 Must Know

On restart after a crash, the database replays the WAL (item 2) from the last known-good checkpoint, reapplying any committed changes that hadn't yet made it into the main data files, and discarding anything that was never fully committed — this is exactly what guarantees the "durability" in ACID (topic `8`).

---

#### 6. LSM Basics — 🟡 Good to Know

1. **Memtable** — recent writes held in memory, in sorted order.
2. **SSTable** (sorted string table) — the memtable is periodically flushed to disk as an immutable, sorted file.
3. **Compaction** — background process merging multiple SSTables together, removing stale/overwritten data, keeping the number of files (and therefore read cost) manageable.

---

#### 7. Row Store vs Column Store — 🟡 Good to Know

**Row store** (most application databases) — all of one row's columns stored together, efficient for reading/writing whole records. **Column store** (analytics-focused) — all values of one column stored together, efficient for scanning one column across millions of rows (exactly what analytical queries do). Full context in topic `20`.

---

#### 8. MVCC and Vacuum/Bloat — 🟡 Good to Know

**MVCC** (multi-version concurrency control) keeps multiple versions of a row so readers never block writers (`9`) — but old versions eventually need cleaning up. **Vacuum** (PostgreSQL's term) reclaims space from dead row versions; without it, **bloat** accumulates, wasting storage and slowing queries over time.

---

#### 9. Checkpoints, fsync, Durability Settings — 🟡 Good to Know

A **checkpoint** flushes in-memory changes to disk at a known point, shortening how much WAL needs replaying after a crash. **`fsync`** forces data actually onto physical storage (not just an OS buffer) — durability settings trade some performance for a stronger "this write really survived a crash" guarantee.

---

#### 10. In-Memory Databases — 🟡 Good to Know

Databases (or database modes) that keep all data in memory, trading some durability guarantees for very high speed — Redis (`13`) is the most common example encountered in practice; useful for caching and ephemeral data, riskier as a sole source of truth without careful persistence configuration.

---

#### 11. Common Interview Questions

1. **What is a write-ahead log, and why does it exist?**
   Changes are written to a sequential log before being applied to the actual data files — this is what lets the database recover exactly what was in progress after a crash, by replaying the log.
2. **Why is disk I/O the thing databases work hardest to minimise?**
   Disk is orders of magnitude slower than memory — the buffer pool, indexes, and write-ahead logging are all designed around minimising and optimising disk access.
3. **B-tree vs LSM-tree storage engines — when would you choose each?**
   B-tree for balanced or read-heavy workloads (the default for most application databases). LSM-tree for very write-heavy workloads (logs, metrics, event streams), since it's optimised for fast writes at the cost of some read complexity.
4. **What is MVCC, and why does it matter?**
   Multi-version concurrency control keeps multiple versions of a row so readers never block writers — a key part of how modern databases achieve good concurrency (topic `9`) without heavy locking.

---

#### 12. Common Mistakes

1. Assuming all databases use the same storage engine internally.
2. Not knowing why crash recovery works, only that it does.
3. Ignoring vacuum/bloat until storage or query performance visibly degrades.
4. Choosing an LSM-tree-based database for a read-heavy workload without understanding the trade-off.

---

#### 13. Related Topics

1. `8` Transactions & ACID — durability, guaranteed by the WAL and crash recovery described here
2. `9` Concurrency & Isolation — MVCC, introduced briefly here, in full depth
3. `20` Analytics, Warehouses & Data Pipelines — row store vs column store, in full context

---

#### 14. Interview Must Remember

1. **Write-ahead log (WAL)**: log the change first, apply it after — this is how crash recovery works.
2. **Buffer pool** keeps hot data in memory, since disk is slow.
3. **B-tree = read-optimised default. LSM-tree = write-optimised.**
4. **MVCC** keeps multiple row versions so readers don't block writers.
