# Consistency, CAP & Distributed Data

Roadmap topic 16 · Stage 4: Choosing & Scaling

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** once data lives on more than one machine, you can't have everything at once — a network can split, and you have to decide what the system does then. This topic is about naming that trade-off precisely, instead of hand-waving "it's eventually consistent" without knowing what that actually costs.

---

#### 1. Strong vs Eventual Consistency — 🟢 Must Know

1. **Strong consistency** — every read sees the latest write, immediately, everywhere.
2. **Eventual consistency** — reads may return a stale value for a short time, but all copies converge eventually if writes stop.

Full depth in `SD 23`. The choice is per-feature, not a single system-wide setting (item 3).

---

#### 2. CAP Theorem — 🟢 Must Know

*During a network partition, you must choose consistency or availability — you cannot have both.*

```text
C - Consistency:  every node sees the same data at the same time
A - Availability:  every request gets a response (even if not the latest data)
P - Partition tolerance:  the system keeps working despite network failures between nodes

Real distributed systems MUST tolerate partitions (P is not optional) —
so the real choice, during a partition, is between C and A.
```

1. **Choose C** — refuse to answer (or answer with an error) rather than risk returning stale/conflicting data.
2. **Choose A** — keep answering, accepting that different nodes might briefly disagree.

---

#### 3. Which Features Need Which — 🟢 Must Know

*The practical, everyday application of this theory.*

| Feature | Needs |
|---|---|
| Account balance, inventory count | Strong consistency |
| Social media like count, a public feed | Eventual consistency is fine |

Decide this **per feature** — forcing every feature onto the same consistency model wastes either correctness (where it mattered) or performance (where it didn't).

---

#### 4. Idempotency and Retries Across Services — 🟢 Must Know

In a distributed system, a call can fail after partially succeeding, and the caller can't always tell — the fix is the same as `ARCH 10`: make operations **idempotent**, so retrying is always safe.

---

#### 5. Quorum Reads and Writes — 🟡 Good to Know

```text
N = total replicas, W = replicas that must acknowledge a write,
R = replicas that must respond to a read

If R + W > N, a read is guaranteed to see the most recent write
(because any read set and any write set must overlap by at least one node)
```

A tunable way to balance consistency against latency/availability, common in leaderless replication systems (`14`, item 6).

---

#### 6. Causal Consistency and Read-Your-Writes — 🟡 Good to Know

**Read-your-writes** — a user always sees their own writes immediately, even if the system is eventually consistent overall (the specific fix from `14`, item 3). **Causal consistency** — a broader guarantee that causally related events (a reply to a comment) are seen in the correct order, even if unrelated events aren't strictly ordered.

---

#### 7. Distributed Transactions — 🟡 Good to Know

1. **Two-phase commit** (name only) — a protocol to atomically commit a transaction across multiple nodes; rarely used directly in modern systems due to its blocking behaviour and complexity.
2. **Saga** (`ARCH 6`, item 9) — a chain of local transactions with explicit compensating actions if a later step fails; the more commonly used modern alternative.

---

#### 8. PACELC — 🟡 Good to Know

An extension of CAP (name only): **P**artition — choose **A**vailability or **C**onsistency; **E**lse (no partition) — choose **L**atency or **C**onsistency. Captures that the trade-off exists even *without* a partition happening — worth knowing the name if it comes up.

---

#### 9. Conflict Resolution — 🟡 Good to Know

When two nodes accept conflicting writes (common in multi-leader or leaderless systems), something must resolve the conflict: **last-write-wins** (simple, can silently lose a change — `MOB 9`'s conflict resolution discussion), **version vectors** (track causality to detect true conflicts), **CRDTs** (data types specifically designed to merge concurrent edits without conflict, `AI` and mobile sync contexts both use this idea).

---

#### 10. BASE — 🟡 Good to Know

A looser model contrasted with ACID (topic `8`): **B**asically **A**vailable, **S**oft state, **E**ventually consistent — the name for the trade-off many distributed NoSQL systems make deliberately, favouring availability over strict consistency.

---

#### 11. Common Interview Questions

1. **Explain the CAP theorem in your own words.**
   During a network partition, a distributed system must choose between consistency (every node agrees, but might refuse to answer) and availability (every request gets an answer, but nodes might briefly disagree) — partition tolerance itself isn't optional for a real distributed system.
2. **Does every feature in a system need the same consistency guarantee?**
   No — decide per feature. Money and inventory usually need strong consistency; a like count or a social feed can tolerate eventual consistency, and it's a real design choice to keep the system efficient where strict consistency isn't actually required.
3. **What's read-your-writes, and why does it matter?**
   A guarantee that a user always sees their own writes immediately, even in an otherwise eventually consistent system — fixes the confusing "I just posted this and it disappeared" experience.
4. **What's the difference between a two-phase commit and a saga?**
   Two-phase commit atomically commits across nodes but blocks and doesn't scale well. A saga is a chain of local transactions with compensating actions on failure — more resilient, the more commonly used modern pattern.

---

#### 12. Common Mistakes

1. Treating CAP as "pick two of three" rather than "P is mandatory; the real choice is C or A during a partition".
2. Forcing every feature onto the same consistency model, system-wide.
3. Not implementing read-your-writes for a feature where it's clearly expected (a user's own posts).
4. Reaching for two-phase commit instead of a saga for a distributed, multi-step business process.

---

#### 13. Related Topics

1. `SD 23` Consistency & CAP — the same core content, first pass
2. `14` Replication & High Availability — replication lag as a concrete instance of this trade-off
3. `ARCH 6` Architecture & Design Patterns — sagas, in more depth

---

#### 14. Interview Must Remember

1. **CAP: partition tolerance is mandatory; the real choice is consistency or availability.**
2. **Strong vs eventual consistency is a per-feature decision.**
3. **Read-your-writes** fixes the "my own write disappeared" experience.
4. **Sagas**, not two-phase commit, are the usual modern answer for distributed multi-step transactions.
