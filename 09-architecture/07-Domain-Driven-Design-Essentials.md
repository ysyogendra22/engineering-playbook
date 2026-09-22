# Domain-Driven Design Essentials

Roadmap topic 7 · Stage 2: Design Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** DDD's core insight is simple even though the vocabulary sounds heavy — model the software around the real business language and real business boundaries, instead of around whatever the database schema happens to look like.

---

#### 1. Ubiquitous Language — 🟢 Must Know

*The single most valuable DDD idea, usable even without adopting anything else from it.*

Use the **same words** in code, documentation, and conversation with the business — if the business calls something a "reservation", the code should have a `Reservation` class, not a `Booking` or `Order` that means the same thing. This eliminates a whole category of miscommunication and translation bugs.

---

#### 2. Bounded Context — 🟢 Must Know

```text
"Order" in the Sales context:      "Order" in the Fulfillment context:
- customer, items, price           - items, shipping address, status
- discount applied                 - warehouse, carrier
```

A **bounded context** is an area where one model and one set of words have exactly one meaning. The same word ("Order") can mean different things in different contexts — the mistake is trying to force one giant, shared model across the whole business instead of drawing clear boundaries.

---

#### 3. Entities, Value Objects, Aggregates — 🟢 Must Know

1. **Entity** — has a distinct identity that persists over time, even as its attributes change (a specific user, tracked by ID).
2. **Value object** — defined entirely by its attributes, no identity of its own (an amount of money, an address — two identical ones are interchangeable).
3. **Aggregate** — a cluster of entities and value objects treated as one unit for changes, with a single **aggregate root** as the only entry point for modifications — this is what keeps the group's internal rules consistent.

---

#### 4. Core, Supporting, and Generic Subdomains — 🟢 Must Know

1. **Core subdomain** — what makes the business actually competitive; deserves the most design effort and your best engineers.
2. **Supporting subdomain** — necessary, but not a differentiator; solid, straightforward implementation is enough.
3. **Generic subdomain** — a solved problem elsewhere (authentication, payments) — buy or use an existing solution rather than building it (`3`, item 5).

Spend design effort in proportion to which category something falls into — treating every subdomain as equally important wastes effort on parts that don't need it.

---

#### 5. Domain Events — 🟡 Good to Know

A record of something meaningful that happened in the business ("order placed", "payment failed") — used to communicate between bounded contexts or trigger downstream processes (`SD 21`), instead of tight, direct coupling between them.

---

#### 6. Context Map — 🟡 Good to Know

A diagram of how bounded contexts relate to each other: **shared kernel** (contexts deliberately share a small common model), **customer–supplier** (one context's team depends on another's output), **anti-corruption layer** (`6`, item 10 — protects one context's model from another's).

---

#### 7. When DDD Is Overkill — 🟡 Good to Know

For simple CRUD systems with little real business logic, full DDD ceremony (aggregates, bounded contexts, domain events) adds more structure than the problem needs. **Ubiquitous language alone** (item 1) is almost always worth adopting regardless of scale — the rest of DDD is a tool to reach for once real domain complexity justifies it.

---

#### 8. Common Interview Questions

1. **What is ubiquitous language, and why does it matter?**
   Using the same terms in code, docs, and business conversation — it removes a whole class of miscommunication that happens when engineers and the business quietly use different words for the same concept.
2. **What's a bounded context?**
   A boundary within which one model and one meaning for each term hold — the same word can mean different things in different bounded contexts, and that's fine as long as the boundaries are clear.
3. **What's the difference between an entity and a value object?**
   An entity has identity that persists as its attributes change. A value object is defined entirely by its attributes, with no identity — two identical value objects are interchangeable.
4. **When would you decide DDD is overkill for a project?**
   For simple CRUD systems with little real domain complexity — the full ceremony (aggregates, bounded contexts, domain events) costs more than it returns; ubiquitous language is worth keeping regardless.

---

#### 9. Common Mistakes

1. Trying to build one giant shared model across the whole business instead of drawing bounded contexts.
2. Confusing entities and value objects, giving identity to something that should just be a value.
3. Applying full DDD ceremony to a simple CRUD system that doesn't need it.
4. Treating every subdomain as equally deserving of design effort, instead of focusing on the core.

---

#### 10. Related Topics

1. `4` Design Principles — abstraction and information hiding, which bounded contexts apply at a larger scale
2. `6` Architecture & Design Patterns — anti-corruption layer, referenced in item 6
3. `9` Data Architecture — data ownership, closely related to bounded contexts

---

#### 11. Interview Must Remember

1. **Ubiquitous language** — same words in code, docs, and conversation. Worth adopting almost always.
2. **Bounded context** — one model, one meaning, clear edges. The same word can mean different things elsewhere.
3. **Entity = identity. Value object = defined by attributes, no identity.**
4. **Spend design effort proportional to subdomain type** — most on core, least on generic.
