# Service Boundaries & Architecture

Roadmap topic 26 · Stage 6: Architecture & Production

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** should the backend be one application or many small services? How do services talk to each other, and how do you keep data correct across them?

---

#### 1. Monolith vs Microservices — 🟢 Must Know

| | Monolith | Microservices |
|---|---|---|
| Shape | One deployable application | Many small services, each owns a feature and its data |
| Good | Simple, easy to develop, test, and deploy | Independent deploys and scaling, team autonomy |
| Bad | Grows large, one deploy for everything | Network calls, partial failures, hard data consistency, complex operations |

**Advice:** start with a **modular monolith** (clear internal modules). Split into services only when team size, scale, or deploy independence really needs it.

---

#### 2. Sync vs Async Communication — 🟢 Must Know

| | Synchronous (REST / gRPC) | Asynchronous (events / queue) |
|---|---|---|
| How | Call and wait for the answer | Publish an event and continue |
| Good | Simple, immediate answer | Decoupled, resilient, absorbs spikes |
| Bad | Caller is blocked; failures chain | Harder to trace, eventual consistency |

Rule: use **sync** when the caller needs the answer now (get price). Use **async** for work that can happen later (send email, update analytics).

---

#### 3. API Gateway and BFF — 🟢 Must Know

1. **API gateway** — the single entry point for clients: authentication, rate limiting, routing to services, logging.
2. **BFF (Backend for Frontend)** — a backend shaped for one client type (for example, the mobile app). It combines calls to several services into one response, so the app makes **fewer requests** and gets exactly the data it needs.

```text
Mobile App → API Gateway / BFF → User Service
                                → Order Service
                                → Payment Service
```

---

#### 4. Transactional Outbox and CDC — 🟡 Good to Know

*Problem: save data to the database and send an event. If one succeeds and the other fails, the system becomes inconsistent.*

**Outbox pattern:**

```text
1. In ONE database transaction: save the order + save an "OrderCreated" row in an outbox table
2. A separate publisher reads the outbox and sends the events to the queue
3. Marks them as sent (retries if it fails)
```

No event is lost, because the event is saved together with the data. Consumers must handle duplicates (idempotency).

**CDC (change data capture)** — read the database's change log and publish changes as events. An alternative way to feed the outbox.

---

#### 5. Sagas — 🟡 Good to Know

*A multi-service workflow with no single database transaction.*

Example: place an order.

```text
1. Order service     → create order (pending)
2. Payment service   → charge the card
3. Inventory service → reserve the items
   If step 3 fails → COMPENSATE: refund the payment, cancel the order
```

1. Each step has a **compensating action** that undoes it.
2. Coordinated by events (choreography) or a central coordinator (orchestration).
3. Results are eventually consistent.

---

#### 6. Business States and Valid Transitions — 🟡 Good to Know

1. Model important entities as **state machines**.
2. Allow only valid transitions, and enforce them in code and the database.

```text
Order:  CREATED → PAID → SHIPPED → DELIVERED
                 ↘ CANCELLED
(SHIPPED → CREATED is not allowed)
```

3. Makes retries, duplicates, and bugs easier to reason about.

---

#### 7. Service Discovery and Data Ownership — 🟡 Good to Know

1. **Service discovery** — how services find each other's addresses (DNS, or a service registry).
2. **Each service owns its data.** Other services use its API, not its database. Sharing a database couples services together.

---

#### 8. Code Structure and Low-Level Design Basics — 🟡 Good to Know

1. Small modules with clear responsibilities, explicit dependencies, and interfaces.
2. Composition over inheritance. Design patterns only when they solve a real problem.
3. Low-level design (class design) is a **separate preparation** from system design.

---

#### 9. Common Interview Questions

1. **When would you split a monolith? What gets harder?**
   When teams or scale need independent deploys and scaling. Harder: network failures, data consistency, debugging, and operations.
2. **REST vs gRPC vs events between services?**
   REST is simple and common. gRPC is fast and typed for internal calls. Events are for decoupled, async work.
3. **What is an API gateway?**
   A single entry point that handles authentication, rate limiting, and routing.
4. **How do you avoid losing an event after a database write?**
   Transactional outbox: write the event in the same transaction, and publish it separately.
5. **How do you handle a transaction across services?**
   A saga with compensating actions, and idempotent steps.
6. **Why should each service own its data?**
   Shared databases couple services and make independent changes impossible.

---

#### 10. Common Mistakes

1. Microservices too early.
2. Services sharing one database.
3. Long chains of synchronous calls.
4. Ignoring failures between services (no timeouts, retries, or fallbacks).
5. Publishing events outside the database transaction.
6. No plan for distributed workflows that fail halfway.

---

#### 11. Related Topics

1. `14` Scaling & Load Balancing (API gateway)
2. `21` Queues, Events & Background Jobs
3. `22` Reliable Requests & External Services
4. `25` Overload & Failure Handling
5. `32` Practice Designs (payment system)

---

#### 12. Interview Must Remember

1. **Start monolith (modular)**, split when there is a clear reason.
2. **Sync** when you need the answer now. **Async** for the rest.
3. **API gateway / BFF** for clients, especially mobile.
4. **Outbox** = no lost events. **Saga** = compensating steps.
5. **Each service owns its data.**
