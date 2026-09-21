# Consistency & CAP

Roadmap topic 23 · Stage 5: Async & Reliability

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** when data lives on many servers, they may not agree at every moment. Decide, for each feature, whether users must always see the latest data or can see slightly old data.

---

#### 1. Strong vs Eventual Consistency — 🟢 Must Know

| | Strong | Eventual |
|---|---|---|
| Meaning | Every read sees the latest write | Reads may be stale for a short time, then all copies agree |
| Cost | Slower, less available | Faster, more available |
| Example | Bank balance, seat booking | Like count, feed, follower count |

```text
Strong:    write → everyone reads the new value
Eventual:  write → some read old value → soon all read the new value
```

---

#### 2. Read-Your-Writes — 🟢 Must Know

*A user must at least see their own changes.*

1. Example: you change your profile name and refresh. You must see the new name, even if other users see the old one for a few seconds.
2. How: read your own data from the leader, or from a cache updated on write, for a short time after writing.
3. Related: **monotonic reads** — you never see data go back in time.

---

#### 3. CAP in Simple Words — 🟢 Must Know

*When the network splits, you must choose between correctness and availability.*

1. **C**onsistency — all nodes give the latest data.
2. **A**vailability — every request gets an answer.
3. **P**artition tolerance — the system works when the network between nodes breaks.

Networks do fail, so partitions will happen. **During a partition**, you choose:

- **CP** — refuse or delay some requests to stay correct (payments, bookings).
- **AP** — keep answering, maybe with stale data, and fix it later (feeds, likes).

**Remember:** CAP applies only *during a partition*. When there is no failure, you can have both good consistency and availability (the trade-off is then latency vs consistency).

---

#### 4. Decide Per Feature — 🟢 Must Know

*Don't pick one consistency level for the whole system.*

| Feature | Consistency | Why |
|---|---|---|
| Payment, wallet balance | Strong | Money must be exact |
| Seat / inventory reservation | Strong | Prevent double booking |
| Post a comment (author sees it) | Read-your-writes | Author expects it immediately |
| Feed, likes count, views | Eventual | Slight delay is harmless |

---

#### 5. Quorums — 🟡 Good to Know

*With N copies of the data, read and write to enough of them so they overlap.*

1. **N** replicas, write to **W**, read from **R**.
2. If **R + W > N**, every read overlaps with the latest write and sees it.
3. Example: N=3, W=2, R=2.
4. Trade-off: higher W or R = stronger consistency but slower and less available.
5. Limits: not a full guarantee (timing and failure cases exist).

---

#### 6. Conflict Handling — 🟡 Good to Know

*When two devices edit the same thing offline.*

1. **Last-write-wins** — the newest timestamp wins. Simple, but can lose edits.
2. **Merge** — combine changes (for example, editing different fields), or use CRDTs for collaborative editing.
3. **Ask the user** in rare, important cases.

---

#### 7. Common Interview Questions

1. **Strong vs eventual consistency?**
   Strong: reads always see the latest write. Eventual: reads may be stale briefly, then converge.
2. **Explain CAP.**
   During a network partition you choose consistency (reject or delay requests) or availability (answer with possibly stale data).
3. **Where would you accept stale data in a social app, and where not?**
   Stale is fine for feeds and like counts. Not for payments, balances, or seat bookings.
4. **What is read-your-writes and how do you provide it?**
   A user always sees their own changes. Read from the leader (or updated cache) after their own write.
5. **What is a quorum?**
   Read and write to enough replicas (R + W > N) so reads overlap with the latest write.

---

#### 8. Common Mistakes

1. Choosing one consistency level for everything.
2. Thinking CAP means "pick any 2" at all times.
3. Ignoring that a user must see their own writes.
4. Using eventual consistency for money.
5. Ignoring conflict handling for offline edits.

---

#### 9. Related Topics

1. `11` Transactions & Concurrency (in `04-backend-engineering`)
2. `15` Caching (stale data)
3. `18` Replication (lag)
4. `30` Mobile-Specific Topics (offline sync conflicts)

---

#### 10. Interview Must Remember

1. **Strong** = always latest. **Eventual** = catches up.
2. **Read-your-writes** for the person who made the change.
3. **CAP:** during a partition choose **consistency or availability.**
4. **Decide per feature.** Money and bookings strong; feeds and counts eventual.
5. **Quorum:** R + W > N.
