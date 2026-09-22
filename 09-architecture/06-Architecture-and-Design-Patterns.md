# Architecture & Design Patterns

Roadmap topic 6 · Stage 2: Design Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** patterns are named, reusable solutions to problems that keep showing up. Knowing them gives you a shared vocabulary with other engineers — "let's put a circuit breaker here" says in three words what would otherwise take a paragraph to explain.

---

#### 1. Creational and Structural Basics — 🟢 Must Know

1. **Factory** — a method or class dedicated to creating objects, hiding the construction details from callers.
2. **Builder** — constructs a complex object step by step, useful when there are many optional parameters.
3. **Adapter** — converts one interface into another a client expects, letting incompatible pieces work together.
4. **Facade** — a simple interface in front of a more complex subsystem.
5. **Decorator** — adds behaviour to an object dynamically, by wrapping it, without changing its class.

---

#### 2. Behavioural Basics — 🟢 Must Know

1. **Strategy** — encapsulate an algorithm behind a common interface, so it can be swapped at runtime (different sorting or pricing strategies, for example).
2. **Observer** — one object notifies a list of subscribers when its state changes — the foundation of reactive/event-driven code (and, conceptually, `Flow`/`StateFlow` in `06-mobile-engineering/3`).

---

#### 3. Dependency Injection and Inversion of Control — 🟢 Must Know

A class **receives** its dependencies instead of creating them itself — the same principle covered concretely in `06-mobile-engineering/7`, here at the architecture level: it's what makes SOLID's Dependency Inversion (`4`) practical to actually apply.

---

#### 4. Repository Pattern — 🟢 Must Know

A layer that hides where data actually comes from (a database, a cache, a network call) behind a clean interface — the same pattern used concretely in `06-mobile-engineering/6` and `04-backend-engineering`.

---

#### 5. UI Patterns — 🟢 Must Know

**MVC, MVP, MVVM, MVI** — patterns that separate a screen's presentation from its state and logic, each differing in exactly how that separation is drawn. Full mobile-specific detail lives in `19` and `06-mobile-engineering/6`.

---

#### 6. Resilience Patterns — 🟢 Must Know

1. **Timeout** — never wait forever for a dependency.
2. **Retry** — try again on a transient failure, usually with backoff.
3. **Circuit breaker** — stop calling a dependency that's clearly failing, to avoid piling up load on it and to fail fast for callers.
4. **Bulkhead** — isolate resources (thread pools, connection pools) per dependency, so one failing dependency can't exhaust resources needed by others.

Full detail in `SD 22` and `SD 25`.

---

#### 7. API Gateway and BFF — 🟢 Must Know

1. **API gateway** — a single entry point in front of multiple services, handling auth, rate limiting, and routing centrally.
2. **BFF (Backend for Frontend)** — a gateway tailored to one specific client (mobile vs web), shaping responses exactly to that client's needs. Full detail in `SD 26`.

---

#### 8. CQRS and Event Sourcing — 🟡 Good to Know

1. **CQRS** (Command Query Responsibility Segregation) — separate models for writing data and for reading it, optimising each independently.
2. **Event sourcing** — store every change as an event, and derive current state by replaying them, rather than storing only the current state.

Know the name and purpose; both add real complexity and are only worth it for specific, strong reasons.

---

#### 9. Saga and Transactional Outbox — 🟡 Good to Know

1. **Saga** — a multi-step distributed process with explicit compensating actions if a later step fails (used instead of a distributed transaction).
2. **Transactional outbox** — reliably publish an event as part of the same database transaction that made the change, avoiding a gap where the change is saved but the event is lost. Full detail in `SD 26`.

---

#### 10. Strangler Fig, Anti-Corruption Layer, Sidecar — 🟡 Good to Know

1. **Strangler fig** — migrate a legacy system piece by piece behind a stable front, retiring the old pieces gradually (topic `16`).
2. **Anti-corruption layer** — a translation layer that protects your own model from being polluted by an external system's model (`7`, `10`).
3. **Sidecar** — a helper process deployed alongside a service to handle a cross-cutting concern (logging, networking) without embedding it in the service's own code.

---

#### 11. Anti-Patterns — 🟡 Good to Know

1. **God class** — one class that does far too much, violating single responsibility (`4`).
2. **Big ball of mud** — a system with no discernible structure, everything tangled together.
3. **Distributed monolith** — microservices that still have to be deployed and changed together, getting all the operational cost of microservices with none of the independence benefit.
4. **Golden hammer** — applying one favourite tool or pattern to every problem, regardless of fit.

---

#### 12. Common Interview Questions

1. **What resilience patterns would you use for a service calling an unreliable dependency?**
   Timeouts always, retries with backoff for transient failures, a circuit breaker to stop hammering a clearly-failing dependency, and bulkheads to keep one failing dependency from exhausting shared resources.
2. **What's the difference between an API gateway and a BFF?**
   A gateway is a general entry point for multiple clients; a BFF is tailored specifically to one client's needs (mobile vs web), shaping responses exactly for it.
3. **What is a distributed monolith, and why is it a problem?**
   Microservices that still must be deployed and changed together — you pay the full operational complexity of microservices without gaining independent deployability, the main benefit that was supposed to justify the split.
4. **When would you use the strangler fig pattern?**
   Migrating away from a legacy system safely, replacing it piece by piece behind a stable interface, rather than a risky big-bang rewrite (topic `16`).

---

#### 13. Common Mistakes

1. Naming a pattern without understanding the specific problem it solves — pattern-dropping instead of pattern-applying.
2. Adding CQRS or event sourcing without a strong, specific reason — both add real complexity.
3. Ending up with a distributed monolith after a microservices migration, without noticing.
4. The "golden hammer" — reaching for one favourite pattern regardless of fit.

---

#### 14. Related Topics

1. `4` Design Principles — the smaller rules these patterns are built from
2. `5` Architectural Styles — the larger structures these patterns fit inside
3. `SD 22`, `SD 25`, `SD 26` — resilience patterns, overload handling, and service boundaries in full depth

---

#### 15. Interview Must Remember

1. **Resilience patterns**: timeout, retry, circuit breaker, bulkhead — know all four together.
2. **API gateway = general entry point. BFF = tailored to one client.**
3. **Distributed monolith** = the failure mode of a microservices split done wrong.
4. **Strangler fig** for safe legacy migration, not a big-bang rewrite.
