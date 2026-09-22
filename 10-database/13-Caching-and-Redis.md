# Caching & Redis

Roadmap topic 13 · Stage 4: Choosing & Scaling

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** caching is the single highest-leverage way to make a slow database feel fast — and Redis is the tool most systems reach for to do it. The core skill is knowing what to cache, for how long, and how to keep it from becoming a second, disagreeing source of truth.

---

#### 1. Cache-Aside, TTL, Eviction, Invalidation — 🟢 Must Know

```text
Read:  check cache → hit? return it
                    → miss? read database → store in cache (with a TTL) → return

Write: update database → delete (invalidate) the cache entry
                          (the next read reloads fresh data)
```

**TTL** (time to live) — an entry expires automatically after N seconds, a safety net against staleness. **Eviction** (usually LRU — least recently used) — when the cache is full, remove the least recently accessed entry. Full depth in `SD 15`.

---

#### 2. Redis Data Types — 🟢 Must Know

Beyond simple key-value: **strings** (the basic case), **hashes** (a mini object with fields), **lists** (ordered, good for a queue or recent-items feed), **sets** (unique unordered values), **sorted sets** (unique values with a score, naturally ordered — perfect for leaderboards).

```text
SET session:42 "token123" EX 3600          -- string, with TTL
HSET user:42 name "Asha" plan "pro"         -- hash
ZADD leaderboard 1500 "player1" 2100 "player2"   -- sorted set
```

---

#### 3. Common Redis Uses — 🟢 Must Know

1. **Cache** — the most common use, per item 1.
2. **Session store** — fast lookup of a user's session data.
3. **Counters** — atomic increment (`INCR`), useful for view counts, rate limiting.
4. **Rate limiter** — a counter with a TTL window (`SD 25`).
5. **Leaderboard** — a sorted set naturally maintains ranked order.

---

#### 4. Stampede, Hot Keys, Stale Data — 🟢 Must Know

1. **Stampede** — a popular key expires, and thousands of requests miss simultaneously, all hitting the database at once. Fix: a lock so only one request reloads it, or jitter the TTL so keys don't all expire at the same moment.
2. **Hot key** — one key gets extreme traffic, overloading a single cache node. Fix: replicate that key, or add an in-process cache layer in front of it.
3. **Stale data** — the cache shows old data until the TTL expires or it's explicitly invalidated; decide how stale is acceptable per feature (`SD 15`).

---

#### 5. Never Treat the Cache as the Only Copy — 🟢 Must Know

*The single most important discipline in this topic.*

A cache should always be **rebuildable** from the real source of truth (`11`, item 4). If Redis loses data (a restart, an eviction under memory pressure), the system should degrade to reading from the database directly — never let the cache silently become the only place important data lives.

---

#### 6. Persistence Options — 🟡 Good to Know

Redis can be purely in-memory (fastest, no durability) or use **snapshots** (periodic full saves) or an **append-only log** (every write logged, replayed on restart) for durability — a real trade-off between speed and how much data survives a crash.

---

#### 7. Pub/Sub and Streams — 🟡 Good to Know

Redis can also act as a lightweight messaging system: **pub/sub** (broadcast messages to subscribers, not persisted) or **streams** (an ordered, persisted log, closer to a simple Kafka) — names and purpose, useful to recognise when Redis is being used beyond simple caching.

---

#### 8. Distributed Locks and Their Limits — 🟡 Good to Know

Redis can implement a distributed lock (only one process does something at a time, across multiple servers), but naive implementations have real edge cases around clock drift and network partitions (`SD 33`) — know it's possible, and know it's easy to get subtly wrong.

---

#### 9. Cache Sizing and Hit-Rate Monitoring — 🟡 Good to Know

Monitor the **hit rate** (what fraction of reads are served from cache vs falling through to the database) — a low hit rate means the cache isn't earning its keep, either because it's too small, TTLs are too short, or the access pattern doesn't actually repeat enough to benefit from caching.

---

#### 10. Cluster Mode and Replication — 🟡 Good to Know

Redis can run in a clustered, replicated configuration for higher availability and more capacity than a single instance — names worth recognising; the operational details are beyond what's usually needed for an interview.

---

#### 11. Common Interview Questions

1. **Explain cache-aside.**
   Read: check the cache first; on a miss, read the database and populate the cache with a TTL. Write: update the database, then delete (invalidate) the cache entry so the next read reloads fresh data.
2. **What is a cache stampede, and how do you prevent it?**
   Many requests reload the same expired key simultaneously, hammering the database. Prevent it with a lock (only one request reloads) or jittered TTLs so keys don't all expire at once.
3. **What Redis data type would you use for a leaderboard, and why?**
   A sorted set — it keeps values ordered by score automatically, making "top N" and "rank of this player" queries efficient without extra sorting logic.
4. **Why should you never treat a cache as the only copy of important data?**
   Caches can lose data (restarts, eviction under memory pressure) — if that's the only copy, the data is genuinely gone; a cache should always be rebuildable from the real source of truth.

---

#### 12. Common Mistakes

1. Caching data with no TTL, letting it grow stale indefinitely.
2. No stampede protection on a genuinely hot, expiring key.
3. Using a shared cache key for user-specific data, leaking one user's data to another.
4. Treating Redis as the sole store for data that has no other durable copy.

---

#### 13. Related Topics

1. `SD 15` Caching — the same core content, first pass
2. `11` Choosing a Database — source of truth vs derived/cacheable data
3. `SD 25` Overload & Failure Handling — rate limiting with Redis

---

#### 14. Interview Must Remember

1. **Cache-aside**: read cache → miss → database → fill cache. Write → update database → invalidate cache.
2. **TTL and LRU eviction** are the basic safety nets.
3. **Stampede** (lock or jitter) and **hot keys** (replicate) need explicit handling.
4. **Never let the cache become the only copy** of important data.
