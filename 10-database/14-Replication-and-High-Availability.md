# Replication & High Availability

Roadmap topic 14 · Stage 4: Choosing & Scaling

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** replication keeps copies of your data on multiple machines — for reading faster, and for surviving a machine failure. The catch is those copies can briefly disagree, and understanding exactly how and why is most of what this topic is really about.

---

#### 1. Leader-Follower Replication and Read Replicas — 🟢 Must Know

```text
        writes
Client ────────► Leader ──── replicates ────► Follower 1
                    ▲                          Follower 2
                    └──────── reads (optional) ─┘
```

All writes go to the **leader**. **Followers** copy the leader's changes, and can serve **read** traffic — spreading read load across more machines without needing to shard the data (`SD 18`).

---

#### 2. Synchronous vs Asynchronous Replication — 🟢 Must Know

1. **Synchronous** — the leader waits for a follower to confirm the write before acknowledging it as committed. Safer (no data loss if the leader fails immediately after), but slower (every write waits on a network round trip to the follower).
2. **Asynchronous** — the leader acknowledges immediately, replicates in the background. Faster, but a leader failure right after a write can lose that write before it ever reached a follower.

The trade-off is directly between write latency and durability guarantee — a real, explicit choice, not a free win either way.

---

#### 3. Replication Lag and Stale Reads — 🟢 Must Know

*A real bug shape, worth being able to trace through.*

```text
1. User posts a comment  → written to the leader
2. User immediately refreshes → read routed to a follower that
   hasn't received the write yet
3. The comment appears to be missing!
```

**Read-your-writes** — after a user writes, route their own subsequent reads to the leader for a short time, so they never see their own change appear to vanish. Use followers for reads where slight staleness is acceptable (a public feed); read critical, just-written data from the leader.

---

#### 4. Failover — 🟢 Must Know

When the leader fails, a follower is **promoted** to become the new leader. The real risk: any writes that hadn't yet replicated to that follower (especially under asynchronous replication, item 2) are **lost** in the failover — a real cost worth naming explicitly when discussing availability trade-offs.

---

#### 5. Replication Is Not a Backup — 🟢 Must Know

*One of the most important, most commonly missed distinctions in this whole folder.*

A bad `DELETE` or data corruption on the leader **replicates to every follower too**, usually within seconds — replication protects against a machine failing, not against a mistake. A real backup (`17`) is a separate, point-in-time copy, kept apart from live replication.

---

#### 6. Multi-Leader and Leaderless Replication — 🟡 Good to Know

**Multi-leader** — more than one node accepts writes (often one per region), needing conflict resolution when the same data is written differently in two places at once. **Leaderless** — any node can accept a write, and reads/writes use quorums (`16`, item 5) to stay consistent. Names and the general idea; full depth is beyond most interview needs.

---

#### 7. Split Brain — 🟡 Good to Know

A dangerous failure mode where a network partition causes **two nodes to both believe they're the leader**, both accepting writes independently — leads to conflicting, hard-to-reconcile data. Prevented by mechanisms like consensus protocols or a majority-vote requirement for promotion.

---

#### 8. Logical vs Physical Replication — 🟡 Good to Know

**Physical** — replicates the exact low-level storage changes (fast, simple, but requires the same database version/format on both sides). **Logical** — replicates at the level of actual data changes (rows inserted/updated), more flexible (can replicate to a different version or even a different kind of consumer), at some added complexity.

---

#### 9. Connection Routing — 🟡 Good to Know

Application code (or a proxy in front of the database) needs to route **writes to the leader** and (optionally) **reads to replicas** — a real piece of infrastructure/configuration, not something that happens automatically just because replicas exist.

---

#### 10. High-Availability Setups and Managed Failover — 🟡 Good to Know

Managed database services often provide automated failover (detecting a leader failure and promoting a replica automatically) as a built-in feature — worth knowing this exists and is a real reason managed services (`11`, item 5) are attractive, without needing to implement it yourself.

---

#### 11. Common Interview Questions

1. **What's the difference between synchronous and asynchronous replication?**
   Synchronous waits for a follower to confirm before acknowledging the write — safer, slower. Asynchronous acknowledges immediately and replicates in the background — faster, with a small window of possible data loss on leader failure.
2. **A user posts a comment and it briefly disappears on refresh — what's happening?**
   Replication lag — the read was routed to a follower that hadn't yet received the write. Fix with read-your-writes: route a user's own reads to the leader for a short time after they write.
3. **Is replication a backup? Why or why not?**
   No — a bad delete or corruption on the leader replicates to every follower too, usually within seconds. Replication protects against machine failure, not against mistakes; a backup is a separate, point-in-time copy.
4. **What happens during failover, and what can go wrong?**
   A follower is promoted to leader. Any writes that hadn't yet replicated to that follower (especially under async replication) are lost — a real, explicit availability-vs-durability trade-off.

---

#### 12. Common Mistakes

1. Treating replication as a substitute for real backups.
2. Reading a user's own just-written data from a replica and being surprised it's missing.
3. Ignoring the data-loss risk of asynchronous replication during failover.
4. Assuming reads are automatically routed to replicas with no explicit configuration.

---

#### 13. Related Topics

1. `SD 18` Replication — the same core content, first pass
2. `17` Backup, Recovery & Data Migration — the real backup this topic contrasts with
3. `16` Consistency, CAP & Distributed Data — the broader consistency trade-offs this connects to

---

#### 14. Interview Must Remember

1. **Leader takes writes; followers replicate and can serve reads.**
2. **Synchronous = safer, slower. Asynchronous = faster, riskier on failover.**
3. **Replication lag causes stale reads — use read-your-writes for a user's own data.**
4. **Replication is NOT a backup** — a bad delete replicates too.
