# Caching

Roadmap topic 15 · Stage 4: Scale

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** keep a copy of frequently used data in a fast place, so you don't repeat slow work. The hard part is keeping the copy correct.

---

#### 1. Hit, Miss, and Where Caches Live — 🟢 Must Know

*Same idea as caching images or API responses in your app.*

1. **Cache hit** — data found in the cache (fast).
2. **Cache miss** — not found, so you go to the source (slow) and usually store the result.
3. **Why:** faster responses and less load on the database.

```text
App cache → CDN → Server memory → Redis → Database
 (nearest, fastest)                      (farthest, slowest)
```

---

#### 2. Cache-Aside — 🟢 Must Know

*The most common pattern. The application manages the cache.*

Read:

```text
1. Look in the cache
2. Hit  → return
3. Miss → read the database → put in the cache (with TTL) → return
```

Write:

```text
1. Update the database
2. Delete (invalidate) the cache entry
   → the next read reloads fresh data
```

---

#### 3. TTL, Eviction, Invalidation — 🟢 Must Know

1. **TTL (time to live)** — the entry expires after N seconds. A simple safety net.
2. **Eviction** — when the cache is full, remove something. **LRU** (least recently used) is the common policy.
3. **Invalidation** — remove or update entries when the data changes. This is the hard part, so keep it simple.

---

#### 4. Stale Data — 🟢 Must Know

1. The cache may show old data until the TTL expires or it is invalidated.
2. Decide per feature how stale is acceptable: profile photo (minutes, fine), account balance (never stale).
3. The shorter the TTL, the fresher the data but the lower the hit rate.

---

#### 5. Cache Stampede and Hot Keys — 🟢 Must Know

**Stampede:** a popular key expires and thousands of requests miss at the same time, all hitting the database.

Fixes:

1. **Lock / single-flight** — only one request reloads the value; the others wait.
2. **Jitter the TTL** — add a random amount so many keys don't expire together.
3. **Refresh early** or serve slightly stale data while reloading.

**Hot key:** one key gets extreme traffic (a celebrity profile) and overloads one cache node. Fix: keep a copy in server memory, or replicate the key across nodes.

---

#### 6. Write-Through / Write-Back — 🟡 Good to Know

1. **Write-through** — write to the cache and database together. The cache is always fresh; writes are slower.
2. **Write-back** — write to the cache first and to the database later. Very fast, but data can be lost if the cache dies.

---

#### 7. Cache Penetration — 🟡 Good to Know

1. Requests for keys that **don't exist** always miss and always hit the database (often an attack).
2. Fix: cache the "not found" result briefly, or use a Bloom filter (topic `33`).

---

#### 8. In-Process vs Shared Cache — 🟡 Good to Know

| | In-process (server memory) | Shared (Redis, Memcached) |
|---|---|---|
| Speed | Fastest | Fast (network hop) |
| Consistency | Each server has its own copy, so copies differ | One copy for all servers |
| Survives restart | No | Yes (Redis can persist) |

---

#### 9. HTTP Cache Headers — 🟡 Good to Know

1. `Cache-Control: max-age=60` — the client or CDN may reuse the response for 60 seconds.
2. `ETag` + `If-None-Match` — validate with the server; `304 Not Modified` if unchanged.
3. Good for mobile: fewer requests, less data.

---

#### 10. Watch Out: User-Specific Data — 🟢 Must Know

1. Never serve one user's cached data to another user.
2. Include the user ID in the cache key for personal data (`feed:user:42`).
3. Keep authorization checks correct even when data comes from the cache.

---

#### 11. Common Interview Questions

1. **What do you cache, where, and what happens when data changes?**
   Cache read-heavy, rarely changing data (profiles, feeds) in Redis/CDN. On writes, update the DB and invalidate the cache key. Use a TTL as a safety net.
2. **Explain cache-aside.**
   Read cache; on a miss read the DB and fill the cache. On write, update the DB and delete the cache entry.
3. **What is a cache stampede? How do you prevent it?**
   Many requests reload the same expired key at once. Use a lock, jittered TTL, or early refresh.
4. **How do you handle stale data?**
   Choose TTLs per feature and invalidate on write. For critical data, don't cache or read from the source.
5. **What is LRU?**
   Evict the least recently used entry when the cache is full.
6. **In-process cache vs Redis?**
   In-process is fastest but differs per server. Redis is shared and consistent across servers.

---

#### 12. Common Mistakes

1. Caching without an invalidation plan.
2. No TTL.
3. Caching user-specific data with a shared key.
4. Everything expires at the same time (stampede).
5. Treating the cache as the only copy of the data.
6. Caching data that changes constantly.

---

#### 13. Related Topics

1. `10` Indexes & Query Performance (first fix the query)
2. `16` File Storage & CDN
3. `23` Consistency & CAP
4. `33` Follow-Up Topics (Bloom filter)

---

#### 14. Interview Must Remember

1. **Cache-aside:** read cache → miss → DB → fill cache. **Write:** update DB → invalidate cache.
2. Always set a **TTL**; know **LRU**.
3. **Stale data** is the trade-off, so decide per feature.
4. **Stampede:** lock, jitter, refresh early. **Hot keys:** replicate.
5. **Never mix users' data** in a shared cache key.
