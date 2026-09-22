# Scalability, Performance & Resilience

Roadmap topic 12 · Stage 3: Cross-Cutting Concerns

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** this topic is about two related but distinct questions — how do you go fast, and what happens when a part of the system breaks anyway. Both need numbers, not adjectives, to actually be designed for.

---

#### 1. Capacity Planning: Numbers First — 🟢 Must Know

Before designing for scale, know the actual numbers: expected users, requests per second, data volume, growth rate (`SD 13`). Designing for "a lot of traffic" is not actionable; designing for "10,000 requests/second at peak, growing 20% per quarter" is.

---

#### 2. Stateless Services and Horizontal Scaling — 🟢 Must Know

A **stateless** service (no per-user memory between requests) can be scaled horizontally — just add more identical instances behind a load balancer (`SD 14`). State that must persist belongs in a database or cache, not in server memory, or horizontal scaling breaks.

---

#### 3. Find the Bottleneck Before Optimising — 🟢 Must Know

*The same discipline as `DB 6`'s "measure before optimizing", applied at the system level.*

Profile and measure to find the **actual** constraint (often the database, sometimes a specific slow dependency) before making architectural changes — optimising a part that isn't the bottleneck wastes effort and doesn't move the real number.

---

#### 4. Single Points of Failure and Redundancy — 🟢 Must Know

Identify every **SPOF** — a component whose failure takes down the whole system — and add redundancy where the cost is justified by the requirement (topic `2`'s ranked availability). Not every SPOF needs eliminating; some are an acceptable, explicit trade-off.

---

#### 5. Timeouts, Retries, Circuit Breakers, Graceful Degradation — 🟢 Must Know

The resilience toolkit (`6`, item 6; `SD 25`), applied architecture-wide: every cross-boundary call needs a timeout, transient failures get retried with backoff, a circuit breaker stops hammering a failing dependency, and the system degrades gracefully (keeps the core working) rather than failing completely when a non-critical part is down.

---

#### 6. SLI, SLO, SLA, and Error Budgets — 🟢 Must Know

1. **SLI** (indicator) — what you actually measure (e.g., successful request percentage).
2. **SLO** (objective) — the internal target (e.g., 99.9% success).
3. **SLA** (agreement) — the external promise to customers, often with consequences if missed.
4. **Error budget** — the gap between 100% and the SLO, spent deliberately on risk (releases, experiments) rather than treated as pure waste.

---

#### 7. RTO and RPO — 🟢 Must Know

**RTO** (recovery time objective) — how long the system can be down. **RPO** (recovery point objective) — how much data loss is acceptable, measured in time (`SD 29`). Both must be explicit numbers, agreed with the business, not assumed.

---

#### 8. Multi-AZ and Multi-Region — 🟡 Good to Know

**Multi-AZ** (availability zone) — redundancy within one region, protecting against a data center failure; usually the standard default. **Multi-region** — redundancy across geographic regions, protecting against a whole-region outage, at significantly higher cost and complexity — only justified by a genuinely strong requirement.

---

#### 9. Load Testing and Chaos Testing — 🟡 Good to Know

**Load testing** — deliberately push traffic beyond normal levels to find where the system actually breaks. **Chaos testing** — deliberately inject failures (kill an instance, add latency) into a running system to verify resilience assumptions hold in practice, not just in theory.

---

#### 10. Performance Budgets — 🟡 Good to Know

Explicit limits for latency and payload size, agreed and enforced (often automatically in CI) — turns "keep it fast" into a measurable, defendable target, the same discipline as topic `2`'s measurable quality attributes applied specifically to performance.

---

#### 11. Back-Pressure and Load Shedding — 🟡 Good to Know

**Back-pressure** — a system signals upstream that it can't keep up, so the sender slows down. **Load shedding** — deliberately dropping or rejecting some requests under extreme load, to protect the system's ability to serve the rest, rather than degrading everything uniformly into failure.

---

#### 12. Common Interview Questions

1. **How do you design a system to scale horizontally?**
   Keep services stateless, so any request can be handled by any instance; put state in a database or cache; scale by adding more instances behind a load balancer.
2. **How do you approach a performance problem?**
   Measure first to find the actual bottleneck, rather than guessing — optimise the real constraint, then re-measure.
3. **What's the difference between SLI, SLO, and SLA?**
   SLI is what you measure. SLO is your internal target. SLA is the external promise to customers, often with consequences attached if it's missed.
4. **How do you design for resilience against a dependency failing?**
   Timeouts on every call, retries with backoff for transient failures, a circuit breaker to stop hammering a failing dependency, and graceful degradation so the core system keeps working even when a non-critical part is down.

---

#### 13. Common Mistakes

1. Designing for scale with no real numbers behind the plan.
2. Optimising a part of the system that isn't the actual bottleneck.
3. State stored in server memory, breaking horizontal scaling.
4. No timeout on a cross-boundary call, letting one slow dependency cascade into a full outage.

---

#### 14. Related Topics

1. `SD 13`, `SD 14`, `SD 25` — estimation, scaling, and overload handling in full depth
2. `SD 29` — backup, recovery, RTO/RPO in full depth
3. `6` Architecture & Design Patterns — the named resilience patterns referenced here

---

#### 15. Interview Must Remember

1. **Numbers first** — capacity planning needs real figures, not adjectives.
2. **Stateless services scale horizontally.** State belongs in a database or cache.
3. **Measure before optimising** — find the real bottleneck.
4. **SLI/SLO/SLA, RTO/RPO** — know all five terms and how they differ.
