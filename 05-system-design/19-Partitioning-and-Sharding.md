# Partitioning & Sharding

Roadmap topic 19 · Stage 4: Scale

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** when one database can't hold all the data or handle all the writes, split the data across several databases. Each one (a shard) holds a part. The hard part is choosing how to split.

---

#### 1. Why and When to Shard — 🟢 Must Know

1. One database has limits: storage, write throughput, memory.
2. Replication scales reads, not writes and not total data size.
3. **Sharding is complex. Try these first:** indexes, caching, read replicas, a bigger machine, archiving old data.
4. Shard when data or write volume truly doesn't fit on one machine.

```text
Users A–H → Shard 1
Users I–P → Shard 2
Users Q–Z → Shard 3
```

---

#### 2. Hash vs Range Partitioning — 🟢 Must Know

| | Hash | Range |
|---|---|---|
| How | `shard = hash(key) % N` | Key ranges (A–H, 1–1000, dates) |
| Data spread | Even | Can be uneven (hotspots) |
| Range queries | Hard (data is scattered) | Easy (data is together) |
| Good for | User IDs, even load | Time series, ordered scans |

Simple hash-mod has a problem: when N changes, almost all keys move. Consistent hashing fixes this (section 5).

---

#### 3. Choosing a Shard Key — 🟢 Must Know

*The shard key decides everything: balance, speed, and problems.*

A good shard key:

1. Has **many distinct values** (high cardinality).
2. **Spreads load evenly.**
3. **Matches the main query** so most requests hit one shard.

Examples:

```text
Chat messages:  conversation_id  → all messages of a chat on one shard
User data:      user_id          → a user's data together
Bad choice:     country          → a few huge shards
Bad choice:     created_date     → all new writes hit one shard (hotspot)
```

---

#### 4. Hotspots and Rebalancing — 🟢 Must Know

1. **Hotspot** — one shard gets far more traffic (a celebrity account, all today's writes).
2. **Uneven data** — some shards are much bigger.
3. **Rebalancing** — moving data when adding shards. Slow and risky, so plan for it (many small partitions, consistent hashing).

---

#### 5. Consistent Hashing — 🟢 Must Know

*Adding or removing a server moves only a small part of the data.*

1. Place servers and keys on a **ring** (a circle of hash values).
2. A key belongs to the **next server clockwise** on the ring.
3. Adding a server takes over only a slice from its neighbor. About `1/N` of keys move, not all.
4. **Virtual nodes** (many points per server on the ring) spread load more evenly.

Used in caches, distributed databases, and load balancing.

---

#### 6. The Costs — 🟢 Must Know

1. **Cross-shard queries** are slow and complex (joins across shards).
2. **Cross-shard transactions** are hard. Avoid them by keeping related data on one shard.
3. More operations: backups, schema changes, monitoring per shard.
4. Changing the shard key later is very painful.

---

#### 7. Resharding, Directory-Based Sharding — 🟡 Good to Know

1. **Resharding** — splitting or merging shards as data grows. Do it gradually, with double-writing and validation.
2. **Directory-based** — a lookup table says which shard holds which key. Flexible, but the directory is a critical component to protect.

---

#### 8. Common Interview Questions

1. **How would you shard the `messages` table? Which shard key?**
   By `conversation_id`. Chat reads are per conversation, so they hit one shard, and load spreads across many conversations. Watch for very hot group chats.
2. **Hash vs range partitioning?**
   Hash gives even spread but poor range queries. Range is good for scans but can create hotspots.
3. **What is consistent hashing?**
   A ring where adding or removing a server moves only a small share of keys.
4. **What problems does sharding cause?**
   Cross-shard queries and transactions, hotspots, rebalancing, and more operations.
5. **When would you not shard?**
   When indexes, caching, replicas, or a bigger machine solve the problem.

---

#### 9. Common Mistakes

1. Sharding too early.
2. A shard key that creates hotspots (date, country).
3. Needing cross-shard joins all the time.
4. Using `hash % N` with no plan for adding servers.
5. No rebalancing plan.

---

#### 10. Related Topics

1. `15` Caching (consistent hashing in caches)
2. `17` Choosing a Database
3. `18` Replication
4. `20` Unique ID Generation

---

#### 11. Interview Must Remember

1. **Shard last.** Index, cache, and replicate first.
2. **Shard key** = high cardinality, even spread, matches the main query.
3. **Hash** = even. **Range** = good for scans, risk of hotspots.
4. **Consistent hashing** = minimal data movement.
5. **Costs:** cross-shard queries and transactions, hotspots, rebalancing.
