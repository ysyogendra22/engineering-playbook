# Overload & Failure Handling

Roadmap topic 25 · Stage 5: Async & Reliability

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** when traffic is too high or a dependency is failing, the system must protect itself. Limit requests, slow producers, stop calling broken services, drop low-priority work, and keep the core features running.

---

#### 1. Rate Limiting — 🟢 Must Know

*Limit how many requests a client can make in a time period.*

Why: protect against abuse, bugs (an app retrying in a loop), and overload.

| Algorithm | Idea | Note |
|---|---|---|
| **Token bucket** | A bucket refills with tokens at a fixed rate. Each request uses one. Empty = reject | Allows short **bursts** |
| **Sliding window** | Count requests in the last N seconds | Smooth and accurate |
| **Fixed window** | Count per calendar minute | Simple, but bursts at window edges |

1. Limit **per user, IP, or API key**, and per endpoint.
2. Reject with `429 Too Many Requests` and a `Retry-After` header.
3. The client should obey `429` and back off.

---

#### 2. Rate Limiter: Placement and Shared State — 🟢 Must Know

*The classic interview design.*

1. Place it at the **API gateway / load balancer**, before the app servers.
2. With many servers, counters must be **shared**: keep them in **Redis**.
3. Use **atomic operations** (`INCR` with expiry, or a Lua script) so two servers don't race.
4. Decide what happens if Redis is down: **fail open** (allow) or **fail closed** (block). Usually fail open for general APIs.

```text
Request → Gateway → Redis: count for user 42 → under limit? → App
                                              → over limit?  → 429
```

---

#### 3. Backpressure — 🟢 Must Know

*If consumers can't keep up, slow the producers.*

1. Without it, queues grow forever and memory or latency explodes.
2. Options: **bounded queues** (reject or block when full), tell producers to slow down (`429`/`503`), or scale up consumers.
3. Monitor queue length and age of the oldest message.

---

#### 4. Circuit Breaker — 🟢 Must Know

*Stop calling a service that is failing, so you don't make things worse.*

```text
CLOSED     → normal, calls go through
   ↓ too many failures
OPEN       → calls fail immediately (fast), no load on the broken service
   ↓ after a wait time
HALF-OPEN  → allow a few test calls
   ↓ success → CLOSED     ↓ failure → OPEN
```

1. Saves threads and time (no waiting for timeouts).
2. Gives the failing service time to recover.
3. Combine with a **fallback** (cached data, default value).

---

#### 5. Load Shedding — 🟢 Must Know

*When you can't serve everything, choose what to drop.*

1. Reject excess or **low-priority** requests early (`503`), so important ones succeed.
2. Example: drop analytics and recommendations before payments and login.
3. Better to serve most users well than everyone badly.

---

#### 6. Graceful Degradation — 🟢 Must Know

*Keep the core working when parts fail.*

| If this fails | Degrade like this |
|---|---|
| Recommendations service | Hide the section or show popular items |
| Image service | Show placeholders |
| Fresh feed | Show a cached feed |
| Search | Show a "search unavailable" message, rest of the app works |

---

#### 7. Bulkheads — 🟡 Good to Know

*Keep one failing part from using up everything.*

1. Separate resources (thread pools, connection pools) per dependency or feature.
2. One slow dependency can't use up all resources and take down everything.
3. Like watertight compartments in a ship.

---

#### 8. Common Interview Questions

1. **Design a rate limiter. Where does it run and where is the state?**
   At the API gateway, using token bucket or sliding window, with counters in Redis using atomic operations. Return `429`.
2. **Token bucket vs sliding window?**
   Token bucket allows bursts at a steady average rate. Sliding window enforces a strict count in the last N seconds.
3. **What is a circuit breaker?**
   It stops calls to a failing service after repeated errors, then tests it again after a wait. States: closed, open, half-open.
4. **What is backpressure?**
   Slowing or rejecting producers when consumers can't keep up.
5. **What is load shedding?**
   Dropping low-priority work under overload to protect critical work.
6. **A downstream service is down. What does your service do?**
   Timeout, circuit breaker, fallback or degraded response, and alert.

---

#### 9. Common Mistakes

1. Per-server rate limits with no shared state.
2. Non-atomic counters (race conditions).
3. Unbounded queues.
4. Retrying into an overloaded service without backoff.
5. Treating all traffic equally under overload.
6. No fallback when a dependency fails.

---

#### 10. Related Topics

1. `14` Scaling & Load Balancing
2. `21` Queues, Events & Background Jobs
3. `22` Reliable Requests & External Services
4. `32` Practice Designs (rate limiter)

---

#### 11. Interview Must Remember

1. **Rate limit:** token bucket or sliding window, per user, `429` + `Retry-After`.
2. Distributed limiter = **Redis + atomic operations.**
3. **Circuit breaker:** closed → open → half-open.
4. **Backpressure, load shedding, graceful degradation** protect the core.
5. **Bulkheads** isolate failures.
