# Partitioning & Sharding

Roadmap topic 15 · Stage 4: Choosing & Scaling

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** when one database genuinely can't hold all your data or handle all your writes, you split it across several machines. It's a powerful tool and a genuinely painful one — this topic is as much about knowing when *not* to reach for it as how to do it.

---

#### 1. Try First — 🟢 Must Know

*The most important line in this whole topic.*

**Indexes, cache, read replicas, a bigger machine, archiving old data** — try all of these before sharding (`SD 19`). Sharding solves a real problem (data or write volume genuinely too big for one machine), but it introduces real, lasting complexity — never reach for it before the simpler options are exhausted.

---

#### 2. Table Partitioning vs Sharding — 🟢 Must Know

1. **Table partitioning** — splitting one large table into smaller physical pieces, **within one database** — the database still presents it as one logical table. Much simpler, and often enough on its own.
2. **Sharding** — splitting data **across multiple separate databases**, usually on different machines. A bigger, more complex step, with real operational cost.

---

#### 3. Hash vs Range Partitioning — 🟢 Must Know

| | Hash | Range |
|---|---|---|
| How | `shard = hash(key) % N` | Key ranges (A-H, dates, ID ranges) |
| Data spread | Even | Can be uneven — hotspots |
| Range queries | Hard (data scattered) | Easy (data stays together) |
| Good for | Even load, point lookups | Time-series, ordered scans |

---

#### 4. Choosing a Shard Key — 🟢 Must Know

A good shard key has **high cardinality** (many distinct values), **spreads load evenly**, and **matches the main query** (so most requests hit only one shard).

```text
Chat messages:  conversation_id  → all messages of a chat land on one shard
User data:      user_id          → a user's data stays together
Bad choice:     country          → a few huge, uneven shards
Bad choice:     created_date     → all new writes hit the same shard (hotspot)
```

---

#### 5. Hotspots and Rebalancing — 🟢 Must Know

A **hotspot** is one shard receiving far more traffic than the others (a celebrity account, all of today's writes landing on one date-keyed shard). **Rebalancing** — moving data as shards are added or removed — is slow and operationally risky; plan for it from the start (item 6).

---

#### 6. The Costs — 🟢 Must Know

1. **Cross-shard queries** are slow and complex — no simple join across shards.
2. **Cross-shard transactions** are hard — avoid needing them by keeping related data on the same shard.
3. **More operations** — backups, schema changes, and monitoring now happen per shard, multiplying operational work.

---

#### 7. Consistent Hashing — 🟡 Good to Know

A technique (`02-algorithm/07`) that spreads keys across nodes so that adding or removing a node moves only a **small fraction** of the data, instead of nearly everything — solves the rebalancing pain of a naive `hash(key) % N` scheme, where changing N reshuffles almost every key.

---

#### 8. Directory-Based Sharding — 🟡 Good to Know

A lookup table explicitly records which shard holds which key — flexible (rebalancing is just updating the directory), but the directory itself becomes a critical, must-protect component.

---

#### 9. Resharding with Double Writes — 🟡 Good to Know

Moving data to a new shard layout gradually: write to both the old and new layout during the transition, backfill historical data, validate, then cut over reads — the same expand-and-contract discipline as topic `10`, applied to sharding.

---

#### 10. Partition Pruning and Archiving — 🟡 Good to Know

The query planner can skip partitions that clearly can't contain matching rows (**pruning**) if the partition key is used in the query — and old partitions (last year's data) can be archived or dropped as a whole unit, much cheaper than deleting individual old rows.

---

#### 11. Distributed SQL Databases — 🟡 Good to Know

Some databases (names worth recognising, not needing deep implementation knowledge) handle sharding **for you** internally, presenting a single logical SQL interface while transparently distributing data — trading some of sharding's manual complexity for less mature tooling and a real product dependency.

---

#### 12. Common Interview Questions

1. **How would you shard a `messages` table for a chat app?**
   By `conversation_id` — all messages of one conversation land on the same shard, so reads (per-conversation) hit only one shard, and load spreads evenly across many conversations. Watch for a very large, hot group chat.
2. **What should you try before sharding?**
   Indexes, caching, read replicas, a bigger machine, and archiving old data — sharding is a last resort given its lasting operational cost.
3. **Hash vs range partitioning — trade-offs?**
   Hash spreads data evenly but makes range queries hard, since matching data is scattered. Range keeps data together for efficient scans but risks hotspots if writes cluster around one part of the range (like recent dates).
4. **What are the real costs of sharding, once you've done it?**
   Cross-shard queries and transactions become slow or impossible to do simply, and every operational task (backups, schema changes, monitoring) multiplies across shards.

---

#### 13. Common Mistakes

1. Sharding before trying indexes, caching, replicas, or a bigger machine.
2. A shard key that creates hotspots (a date, a low-cardinality field).
3. Needing cross-shard joins or transactions constantly, fighting the architecture.
4. Using naive `hash % N` sharding with no plan for adding shards later (no consistent hashing, no rebalancing plan).

---

#### 14. Related Topics

1. `SD 19` Partitioning & Sharding — the same core content, first pass
2. `02-algorithm/07` Graph Algorithms (consistent hashing) — the technique referenced in item 7
3. `SD 20` Unique ID Generation — shard-aware ID generation strategies

---

#### 15. Interview Must Remember

1. **Shard last** — indexes, cache, replicas, and a bigger machine come first.
2. **Shard key**: high cardinality, even spread, matches the main query.
3. **Hash = even spread. Range = good for scans, risk of hotspots.**
4. **Costs**: cross-shard queries and transactions, hotspots, multiplied operations.
