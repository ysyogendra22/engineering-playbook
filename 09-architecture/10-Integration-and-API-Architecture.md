# Integration & API Architecture

Roadmap topic 10 · Stage 3: Cross-Cutting Concerns

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** every boundary between systems is a promise that has to be kept even as both sides change independently, and often at different speeds. Integration architecture is about designing that promise deliberately, instead of letting it emerge by accident.

---

#### 1. Synchronous vs Asynchronous Integration — 🟢 Must Know

1. **Synchronous** — the caller waits for a direct response (REST, gRPC) — simpler to reason about, but couples the caller's availability to the callee's.
2. **Asynchronous** — communication via events or messages (`SD 21`), decoupling the two sides in time — more resilient to a dependency being temporarily down, at the cost of more complex flows and eventual consistency (full depth in `SD 26`).

---

#### 2. API-First Design — 🟢 Must Know

Design the **contract** before writing the implementation (`BE 3`) — this forces early agreement between teams, lets client and server work in parallel against a stable interface, and surfaces awkward design issues before they're baked into code.

---

#### 3. API Versioning and Backward Compatibility — 🟢 Must Know

*The constraint that never goes away, especially for mobile clients.*

**Old app versions never fully disappear** (`06-mobile-engineering/1`) — an API change must keep working for clients that haven't updated, sometimes for years. Prefer additive, backward-compatible changes; version explicitly and deliberately when a breaking change is truly unavoidable.

---

#### 4. Idempotency and Retries Across Boundaries — 🟢 Must Know

Any call across a service boundary can fail after partially succeeding — the caller doesn't always know whether it worked. Making operations **idempotent** (the same request repeated has the same effect as once) is what makes retrying safe (`BE 3`, `SD 22`).

---

#### 5. Third-Party Integration — 🟢 Must Know

External services bring their own failure modes: **rate limits**, their own downtime, **webhooks** that may arrive late or duplicated, and the need for **reconciliation** — periodically comparing your records against theirs to catch anything that slipped through (`SD 22`).

---

#### 6. REST, GraphQL, gRPC — 🟡 Good to Know

| | REST | GraphQL | gRPC |
|---|---|---|---|
| Shape | Resource-oriented endpoints | Client-specified query shape | Strongly-typed RPC, binary protocol |
| Best for | General-purpose APIs | Flexible client data needs | High-performance internal service-to-service calls |

No universal winner — choose based on the actual client needs and performance requirements (`BE 3`).

---

#### 7. Events and Messaging Contracts — 🟡 Good to Know

Just like a synchronous API needs a contract, an **event's shape** needs one too — and it needs to evolve compatibly for the same reason. A **schema registry** (name only) centrally tracks and enforces event schema versions across producers and consumers.

---

#### 8. API Gateway Responsibilities — 🟡 Good to Know

Beyond simple routing: authentication, rate limiting, request/response transformation, and observability — centralising these cross-cutting concerns so individual services don't each reimplement them (`6`, item 7; `SD 26`).

---

#### 9. Anti-Corruption Layer Around External Systems — 🟡 Good to Know

A translation layer that converts an external system's model into your own, so a third party's design decisions and quirks don't leak into and pollute your internal domain model (`7`, item 6).

---

#### 10. Common Interview Questions

1. **How do you design an API to stay compatible with old mobile app versions?**
   API-first design with a stable contract, additive (not breaking) changes wherever possible, and explicit versioning when a break is truly unavoidable — old app versions must keep working, often for years.
2. **Synchronous vs asynchronous integration — how do you choose?**
   Synchronous is simpler when the caller genuinely needs an immediate response and can tolerate coupling its availability to the dependency's. Asynchronous decouples the two in time, trading simplicity for resilience — better when the caller doesn't need to block.
3. **Why does idempotency matter across service boundaries?**
   A call can fail after partially succeeding, and the caller often can't tell — a safe retry requires the operation to be idempotent, so retrying doesn't duplicate the effect.
4. **How do you handle a flaky third-party integration?**
   Respect its rate limits, handle its downtime gracefully, handle webhook duplicates/delays, and run periodic reconciliation to catch anything that fell through the gaps.

---

#### 11. Common Mistakes

1. Making a breaking API change without considering clients still on old app versions.
2. Assuming a call across a service boundary either fully succeeded or fully failed, with no in-between state.
3. Trusting a third-party webhook to always arrive exactly once, on time.
4. Letting an external system's model leak directly into your own domain model with no anti-corruption layer.

---

#### 12. Related Topics

1. `BE 3` API Design — the concrete backend-level guidance this topic sits above
2. `SD 22` Reliable Requests & External Services — retries, idempotency, and third-party integration in full depth
3. `SD 26` Service Boundaries & Architecture — sync/async communication and API gateways in full depth

---

#### 13. Interview Must Remember

1. **API-first**: design the contract before the code.
2. **Old app versions never fully disappear** — additive changes, explicit versioning for breaks.
3. **Idempotency is what makes retries across boundaries safe.**
4. **Third-party integrations need rate-limit handling, webhook tolerance, and reconciliation.**
