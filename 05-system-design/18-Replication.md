# Replication

Roadmap topic 18 · Stage 4: Scale

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** keep copies of your database on several servers. Copies let you serve more reads and survive a server failure. The price is that copies can be slightly behind.

---

#### 1. Leader–Follower Replication — 🟢 Must Know

*One database takes all writes (leader). Others copy from it and serve reads (followers, read replicas).*

```text
Writes → Leader ──copies changes──→ Follower 1 ──→ Reads
                               └──→ Follower 2 ──→ Reads
```

Benefits:

1. **Read scaling** — spread reads across followers.
2. **Availability** — if the leader dies, a follower can take over.
3. Reads on followers protect the leader from heavy queries.

Limit: **writes still go to one leader.** Replication does not scale writes (that needs sharding, topic `19`).

---

#### 2. Synchronous vs Asynchronous — 🟢 Must Know

| | Synchronous | Asynchronous |
|---|---|---|
| Leader waits for follower? | Yes | No |
| Write speed | Slower | Faster |
| Data loss if leader dies | Very little | Recent writes may be lost |
| Follower freshness | Up to date | Can lag |

Most systems use asynchronous replication (or one synchronous follower plus the rest asynchronous).

---

#### 3. Replication Lag and Stale Reads — 🟢 Must Know

*A follower can be a few milliseconds or seconds behind.*

Example bug:

```text
1. User posts a comment  → written to the leader
2. User refreshes        → read from a follower that hasn't received it yet
3. The comment is missing!
```

Fixes:

1. **Read-your-writes** — after a user writes, read their own data from the leader for a short time.
2. Use followers only for reads where slight staleness is fine (feeds, counts).
3. Read critical data (balance, payment status) from the leader.

---

#### 4. Failover — 🟢 Must Know

*When the leader dies, promote a follower.*

1. Detect the failure (health checks).
2. Choose a follower (usually the most up to date) and **promote** it to leader.
3. Point the application and other followers to the new leader.

Risks:

1. **Lost writes** — with async replication, the newest writes may not have reached the follower.
2. **Split brain** — the old leader comes back and two servers think they're the leader. Prevent with proper leader election and fencing.

---

#### 5. Replication Is Not a Backup — 🟢 Must Know

1. A mistake (a bad `DELETE`, corrupted data) is **copied to all replicas** within seconds.
2. You still need **separate backups** and tested restores (topic `29`).

---

#### 6. Multi-Leader and Leaderless — 🟡 Good to Know (names only)

1. **Multi-leader** — several nodes accept writes (for example, one per region). Needs conflict resolution.
2. **Leaderless** — any node accepts writes, and reads and writes use quorums (Cassandra, DynamoDB style). See topic `23`.

---

#### 7. Common Interview Questions

1. **The primary database dies. What happens to users?**
   Failover: detect the failure, promote a follower, redirect traffic. Users may see a short outage, and some recent writes may be lost with async replication.
2. **How does replication help scale?**
   Reads are spread across replicas. It does not scale writes.
3. **Sync vs async replication?**
   Sync waits for the follower (safer, slower). Async doesn't (faster, may lose recent data or lag).
4. **A user posts and doesn't see their post after refreshing. Why?**
   Replication lag. Fix with read-your-writes: read from the leader after a write.
5. **Is a replica a backup?**
   No. Bad deletes and corruption replicate too.

---

#### 8. Common Mistakes

1. Thinking replicas scale writes.
2. Reading critical data from lagging followers.
3. Counting replication as a backup.
4. No plan or testing for failover.
5. Ignoring lag when designing user-facing flows.

---

#### 9. Related Topics

1. `14` Scaling & Load Balancing (SPOF)
2. `19` Partitioning & Sharding
3. `23` Consistency & CAP
4. `29` Backup, Recovery, Security & Cost (RPO, RTO)

---

#### 10. Interview Must Remember

1. **Leader takes writes; followers serve reads.**
2. **Async replication → lag → stale reads.** Fix with read-your-writes.
3. **Failover** = promote a follower. Risks: lost writes, split brain.
4. **Replication is not a backup.**
5. Replication scales **reads**, not writes.
