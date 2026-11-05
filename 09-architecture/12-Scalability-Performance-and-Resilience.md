# Scalability, Performance & Resilience

> Plan capacity with numbers, find the bottleneck before optimising, remove single points of failure, and design for partial failure with timeouts, retries, breakers and graceful degradation. Measure reliability with SLIs, SLOs and error budgets.

Roadmap topic 12 · Stage 3: Cross-Cutting Concerns

**Go deeper:** `05-system-design/13-Requirements-and-Estimation`, `14-Scaling-and-Load-Balancing`, `15-Caching`, `18-Replication`, `19-Partitioning-and-Sharding`, `25-Overload-and-Failure-Handling`, `27-Observability`, `29-Backup-Recovery-Security-and-Cost` · `2` Quality Attributes · `6` Patterns.

**Marks:** 🟢 must know · 🟡 good to know

---

#### 1. What Is It?

*Handling growth and failure without surprises.*

| 🟢 Must know | 🟡 Good to know |
|---|---|
| capacity planning: numbers first | multi-AZ and multi-region |
| stateless services, horizontal scaling | load testing and chaos testing |
| find the bottleneck first | performance budgets |
| single points of failure and redundancy | back-pressure and load shedding |
| timeouts, retries, breakers, graceful degradation | |
| SLI, SLO, SLA, error budgets | |
| RTO and RPO | |

1. **Scalability:** handling more load by adding resources.
2. **Performance:** how fast (latency) and how much (throughput).
3. **Resilience:** continuing to work when parts fail.
4. **SLI/SLO/SLA:** what you measure / the target / the promise to customers.

**Signals in an interview:** "how would this scale to 10×?", "what is the bottleneck?", "what happens if the database is down?", "what SLO would you set?", "how do you test resilience?".

---

#### 2. How It Works

**Numbers first (`SD 13`).**

1. Requests per second = users × requests per user ÷ 86,400. Peak = 3 to 10× average.
2. Concurrency = throughput × latency (**Little's law**): 2,000 requests per second at 100 ms → 200 requests in flight.
3. Servers = peak throughput ÷ per-server capacity, plus one or two for redundancy (N+1).
4. Data: rows × size × replication × retention.

**Find the bottleneck.** The slowest/most saturated resource limits the system (CPU, memory, database connections, a lock, a downstream service, network, a hot key). Measure (p95 latency, utilisation, queue depth, error rate), fix the biggest limit, measure again. Optimising anything else is wasted.

**Stateless services and horizontal scaling.** Keep servers stateless (state in a database, cache or token), put a load balancer in front, scale by adding instances, auto-scale on a metric (CPU, queue length, requests per instance). Stateful parts (databases) scale differently: read replicas, caching, partitioning (`SD 18`, `SD 19`).

**Single points of failure and redundancy.** For every component ask "if this dies, what stops?". Add redundancy: multiple instances behind a load balancer, replicated databases with failover, multiple zones, redundant networking. Redundancy only counts if failover is tested.

**Availability maths.**

| Arrangement | Formula | Example |
|---|---|---|
| In series (all needed) | multiply | 3 components at 99.9% → 99.7% |
| In parallel (any one works) | 1 − (1 − a)ⁿ | 2 replicas at 99% → 99.99% |

More hops in a request path lowers availability; redundancy raises it.

**Failure handling.**

| Mechanism | Purpose |
|---|---|
| Timeouts | never wait forever; shorter than the caller's |
| Retries with backoff and jitter | recover from transient errors (idempotent only) |
| Circuit breaker | stop hammering a failing dependency |
| Bulkhead | isolate resources per dependency or tenant |
| Graceful degradation | keep the core working (cached or reduced answers) |
| Back-pressure, load shedding | refuse excess work early, protect the system |

**SLI, SLO, SLA and error budgets.**

| Term | Meaning | Example |
|---|---|---|
| SLI | measured indicator | fraction of requests that succeed under 300 ms |
| SLO | internal target for the SLI | 99.9% over 30 days |
| SLA | contractual promise with consequences | 99.5% or service credits |
| Error budget | 100% − SLO: allowed failure | 0.1% ≈ 43 minutes per 30 days |

The error budget balances reliability and feature speed: budget left → ship faster; budget spent → freeze risky changes and fix reliability. Alert on **burn rate** (how fast the budget is being used), not on every blip.

**RTO and RPO (`SD 29`).** Recovery time objective (how long you can be down) and recovery point objective (how much data you can lose) drive the design: backups, replicas, standby regions.

🟡 **Multi-AZ and multi-region.** Multi-AZ is the baseline for production. Multi-region (active-passive, then active-active) only when availability or latency requirements justify the data-consistency complexity and cost.

🟡 **Load testing and chaos testing.** *Load testing* (expected, peak, spike, soak) proves capacity and finds bottlenecks. *Chaos testing* injects failures (kill an instance, add latency, cut a dependency) to prove resilience, starting small and in a safe environment.

🟡 **Performance budgets.** A latency budget across the path (client, network, API, database), payload size limits, startup time targets; fail the build on regressions.

🟡 **Back-pressure and load shedding.** When overloaded, reject quickly with `429/503` and `Retry-After` rather than slow down everyone; prioritise critical traffic.

---

#### 3. Naive vs Better Design

| Naive | Better |
|---|---|
| "make it scalable" with no numbers | estimated load, peak factor, 10× headroom |
| optimise code without profiling | measure, find the bottleneck, fix, re-measure |
| state on the server (sessions in memory) | stateless servers, shared state elsewhere |
| one database instance, no failover | replicas and tested failover |
| call dependencies with no timeout | timeouts, retries, breakers, fallbacks |
| 100% availability promised | an SLO with an error budget |
| failover never tested | game days and chaos experiments |
| reject nothing under overload | shed load, protect the core |

---

#### 4. Templates & Examples

**Capacity calculator.**

```kotlin
fun avgRps(dailyUsers: Long, requestsPerUser: Int) = dailyUsers * requestsPerUser / 86_400.0
fun serversNeeded(peakRps: Double, perServerRps: Double, spares: Int = 1) = Math.ceil(peakRps / perServerRps).toInt() + spares
fun inFlight(rps: Double, latencySeconds: Double) = rps * latencySeconds          // Little's law
```

Checks: `avgRps(500_000, 20)` → `115.7`; peak at 5× → `~579`; with `perServerRps = 150` → `serversNeeded(579, 150)` → `4 + 1 = 5`. `inFlight(2000.0, 0.1)` → `200.0` concurrent requests: size thread pools and connection pools for that.

**Availability maths.**

```kotlin
fun series(vararg a: Double) = a.fold(1.0) { acc, x -> acc * x }
fun parallel(vararg a: Double) = 1 - a.fold(1.0) { acc, x -> acc * (1 - x) }
```

Checks: `series(0.999, 0.999, 0.999)` → `0.997003` (99.70%); `parallel(0.99, 0.99)` → `0.9999` (99.99%). Redundancy turns two mediocre components into a very reliable pair, if failures are independent and failover works.

**Error budget and burn rate.**

```kotlin
fun errorBudgetMinutes(sloPercent: Double, days: Int = 30) = (100 - sloPercent) / 100 * days * 24 * 60
fun burnRate(budgetFractionUsed: Double, windowHours: Double, periodHours: Double = 720.0) = budgetFractionUsed / (windowHours / periodHours)
```

Checks: `errorBudgetMinutes(99.9)` → `43.2` minutes; if `2%` of the monthly budget is used in `1` hour, `burnRate(0.02, 1.0)` → `14.4` (at that rate the budget lasts 50 hours): page someone. A burn rate of `1.0` means you will exactly use the budget by month end.

**Resilience wrapper (timeout + breaker + fallback).**

```kotlin
suspend fun <T> resilient(timeoutMs: Long, breaker: Breaker, fallback: suspend () -> T, call: suspend () -> T): T {
    if (!breaker.allow()) return fallback()
    return try { withTimeout(timeoutMs) { call() }.also { breaker.success() } }
    catch (e: CancellationException) { throw e }
    catch (e: Exception) { breaker.failure(); fallback() }
}
```

Checks: the dependency fails 5 times → the breaker opens and later calls return the fallback immediately (no waiting) until the wait time passes.

**Example SLO table.**

| Service | SLI | SLO (30 days) | Error budget |
|---|---|---|---|
| Notes API | requests succeeding under 300 ms | 99.9% | 43 min |
| Sync | edits visible on another device within 5 s | 99% | 7.2 h |
| Search | queries answered under 1 s | 99.5% | 3.6 h |

**Degradation ladder.**

```text
Healthy → search slow: serve cached suggestions → search down: hide search, keep notes → sync down: queue edits locally → database read-only: allow reads, queue writes
```

**Load test plan.**

```text
Expected: 600 rps for 30 min — p95 < 300 ms.   Peak: 3,000 rps for 10 min — error rate < 0.1%.
Spike: 0 → 3,000 rps in 30 s — no cascading failure.   Soak: 600 rps for 6 h — no memory growth.   Find the first thing that saturates.
```

---

#### 5. Numbers & Rules of Thumb

| Item | Guide |
|---|---|
| Headroom | provision for 2× the expected peak; plan to redesign at 10× |
| Peak factor | 3 to 10× the daily average |
| Utilisation | keep CPU under ~60–70% at peak so spikes don't tip over |
| Availability | 99.9% ≈ 8.8 h/year; 99.99% ≈ 53 min/year |
| Timeouts | shorter down the call chain (client 10 s → API 5 s → DB 1 s) |
| Retries | 3 with backoff and jitter; total time under the caller's timeout |
| Failover time | measured, not assumed; test it regularly |
| Percentiles | track p50, p95, p99 |
| Error-budget policy | freeze risky releases when the budget is spent |

---

#### 6. Common Mistakes & Edge Cases

1. Designing for imaginary scale.
2. Optimising without measuring.
3. Hidden single points of failure (DNS, a certificate, a shared queue).
4. Retry storms that amplify an outage.
5. No timeouts, or timeouts longer than the caller's.
6. An untested failover or restore.
7. Alerting on every error instead of burn rate.
8. Treating the SLA as the target (SLO should be tighter).

Edge cases: a thundering herd after recovery (jitter, warm-up, rate-limit reconnects); a hot partition or hot key; gradual degradation (slow, not down); correlated failures (same zone, same bad deploy); cache stampede; dependency of dependencies; time (certificates, leap seconds, DST).

---

#### 7. Say This in the Interview

1. "I start with numbers: requests per second, the peak factor, data size, and latency targets. I design for about 10× the next milestone."
2. "I find the bottleneck by measuring, fix the biggest one, and re-measure; stateless services scale horizontally, and the database scales through caching, replicas and later partitioning."
3. "I look for single points of failure and add redundancy that I test. Series dependencies multiply availability, parallel ones raise it."
4. "Every outbound call has a timeout, bounded retries with jitter, a breaker, and a fallback so the core keeps working."
5. "I set SLOs with an error budget and alert on burn rate; RTO and RPO drive backup and failover design."
6. "I prove it with load tests and small chaos experiments."

---

#### 8. Quick Check

1. How do you compute servers needed?
2. What is an error budget?
3. How does redundancy change availability?
4. What is graceful degradation?

<details>
<summary>Answers</summary>

1. Peak throughput ÷ per-server capacity, plus spare instances.
2. 100% minus the SLO: the amount of failure allowed in the period; used to balance reliability and feature speed.
3. In parallel, 1 − (1 − a)ⁿ rises sharply (two 99% replicas give 99.99%), provided failover works.
4. Keeping the core function working with reduced features when a dependency fails.

</details>

---

#### 9. Practice

**Interview questions**

1. How would you scale this system 10×?
2. How do you find the bottleneck?
3. What are SLI, SLO and SLA? What is an error budget?
4. How do you design for a dependency being down?
5. How do you handle a traffic spike?
6. How do you test resilience?

**Exercises**

1. Estimate the load for your product (average and peak) and the servers needed.
2. Write SLOs for three user journeys and the error budget for each.
3. List the single points of failure in your system and the mitigation for each.
4. Design a small chaos experiment (kill one instance) with a hypothesis and an abort condition.

**Remember:** numbers first · measure, then fix the bottleneck · stateless + horizontal · remove and test SPOFs · timeouts, retries with jitter, breakers, fallbacks · SLO + error budget + burn rate · RTO/RPO · load and chaos tests.
