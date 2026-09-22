# Architectural Styles

Roadmap topic 5 · Stage 2: Design Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** an architectural style is a large-scale shape for a system — how its major pieces are organised and how they talk to each other. Knowing several styles well, and knowing which quality attributes each one favours, is what lets you pick the right shape instead of the familiar one.

---

#### 1. Layered Architecture — 🟢 Must Know

```text
Presentation → Business Logic → Data Access → Database
```

Each layer only talks to the layer directly below it. Simple, well-understood, and a reasonable default — the main risk is layers becoming too tightly coupled to each other's internals over time (`8`).

---

#### 2. Monolith, Modular Monolith, Microservices — 🟢 Must Know

| | Monolith | Modular monolith | Microservices |
|---|---|---|---|
| Deployables | One | One, but internally partitioned | Many, independent |
| Team independence | Low | Medium | High |
| Operational complexity | Low | Low–medium | High |
| Cross-cutting changes | Easy (one codebase) | Easy | Hard (coordinate across services) |

**"Monolith first" is often right** — start with a modular monolith with clean internal boundaries, and split into microservices only once you have a real, specific reason (team scaling, independent deployment needs) that outweighs the added operational cost.

---

#### 3. Client–Server and API-First Design — 🟢 Must Know

The foundational style behind almost everything in this vault's `BE`/`SD` folders — a client (mobile app, `06-mobile-engineering`) talks to a server over a defined API. **API-first** means designing that contract deliberately, before implementation (`10`, `BE 3`), rather than letting it emerge accidentally from whatever the server happens to return.

---

#### 4. Event-Driven Architecture — 🟢 Must Know

Components communicate by publishing and reacting to **events**, rather than calling each other directly (`SD 21`). Favours loose coupling and scalability, at the cost of harder-to-trace flows and eventual consistency (`SD 23`) — a real trade-off, not a free upgrade.

---

#### 5. Hexagonal and Clean Architecture — 🟢 Must Know

```text
            ┌─────────────────────────┐
            │   Adapters (details)     │
            │  UI · DB · external APIs │
            │   ┌─────────────────┐   │
            │   │  Business rules  │   │
            │   │    (the core)    │   │
            │   └─────────────────┘   │
            └─────────────────────────┘
```

Business rules sit at the centre, with no dependency on frameworks, databases, or UI. Details (a specific database, a specific UI framework) plug in at the edges through interfaces, and can be swapped without touching the core. The same idea shows up in `19`'s mobile architecture and `06-mobile-engineering/6`.

---

#### 6. Serverless and Functions — 🟡 Good to Know

Code runs as small, independently deployed functions, with the platform handling scaling and infrastructure — favours low operational overhead and pay-per-use cost, at the cost of less control and potential cold-start latency.

---

#### 7. Service-Based Architecture — 🟡 Good to Know

A middle ground between a monolith and full microservices: fewer, larger services than a microservices architecture, each still independently deployable — often a pragmatic step when full microservices' operational cost isn't justified yet.

---

#### 8. Microkernel and Pipe-and-Filter — 🟡 Good to Know

1. **Microkernel (plugin architecture)** — a small, stable core with pluggable extensions (an IDE with plugins).
2. **Pipe-and-filter** — data flows through a series of independent processing stages, each transforming it (a classic Unix-pipeline shape).

---

#### 9. Space-Based and Other Styles — 🟡 Good to Know

Names worth recognising for specific, less common needs (extreme scalability via a shared, distributed in-memory data grid, for space-based architecture) — not needed in depth for most systems.

---

#### 10. Choosing a Style from Ranked Quality Attributes — 🟡 Good to Know

Go back to topic `2`'s ranked list: if independent team scaling and deployment matter most, lean toward microservices or service-based; if simplicity and low operational cost matter most, lean toward a modular monolith. The style should follow from the ranking, not be chosen first and justified after.

---

#### 11. Common Interview Questions

1. **Monolith vs microservices — how do you choose?**
   Start with "monolith first" (a modular monolith with clean boundaries). Move to microservices only for a specific, real reason — independent team scaling, independent deployment needs — that outweighs the real operational cost of running many services.
2. **What's the idea behind hexagonal/clean architecture?**
   Business rules at the centre, with no dependency on frameworks or infrastructure; details (database, UI, external APIs) plug in through interfaces at the edges, and can be swapped without touching the core logic.
3. **What does event-driven architecture trade off?**
   Loose coupling and scalability, against harder-to-trace flows and eventual (not immediate) consistency between components.
4. **How do you pick an architectural style for a new system?**
   From the ranked quality attributes (topic `2`) — the style should follow from what the system actually needs most, not be chosen out of familiarity or trend.

---

#### 12. Common Mistakes

1. Starting with microservices "by default" without a specific reason that justifies the operational cost.
2. Choosing a style based on familiarity or trend rather than the ranked quality attributes.
3. Calling something "hexagonal" while still letting business logic depend directly on a specific database or framework.
4. Treating event-driven architecture as free scalability with no downside.

---

#### 13. Related Topics

1. `2` Requirements, Constraints & Quality Attributes — what a style choice should be grounded in
2. `6` Architecture & Design Patterns — smaller, reusable structures within any of these styles
3. `SD 21`, `SD 23` — event-driven architecture and consistency in more depth
4. `19` Mobile App Architecture — hexagonal/clean architecture applied to a mobile app

---

#### 14. Interview Must Remember

1. **Monolith first** is usually right — modularize before you distribute.
2. **Hexagonal/clean**: business rules at the centre, details plug in at the edges.
3. **Event-driven** trades tracing simplicity and immediate consistency for loose coupling.
4. **Choose a style from ranked quality attributes**, not from trend or familiarity.
