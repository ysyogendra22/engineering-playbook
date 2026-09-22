# Design Principles

Roadmap topic 4 · Stage 2: Design Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** these are the small, timeless rules that every larger architectural style and pattern (topics `5`, `6`) is ultimately built from. If a design feels wrong but you can't say why, it's usually breaking one of these.

---

#### 1. Separation of Concerns — 🟢 Must Know

Each part of the system should have **one clear job**. A component that handles UI rendering, business logic, and database access all at once is hard to change without breaking something else — split it so each concern can change independently.

---

#### 2. High Cohesion, Low Coupling — 🟢 Must Know

*The single most useful lens for evaluating any module boundary.*

1. **Cohesion** — how focused a module is. High cohesion means everything inside it genuinely belongs together.
2. **Coupling** — how tied modules are to each other. Low coupling means a change in one rarely forces a change in another.
3. **Aim for both**: high cohesion within modules, low coupling between them.

```text
High cohesion, low coupling:        Low cohesion, high coupling:
[ Auth module ]  [ Billing module ]  [ "Utils" module: auth helpers,
      ↓ small API        ↓                billing math, date formatting,
[ shared contract only ]              image resizing — used everywhere,
                                       everything depends on everything ]
```

---

#### 3. SOLID — 🟢 Must Know

Five object-oriented design principles, each addressing a different way code can become brittle:

| Letter | Principle | Plain meaning |
|---|---|---|
| S | Single Responsibility | A class should have one reason to change |
| O | Open–Closed | Open to extension, closed to modification — add behaviour without editing existing code |
| L | Liskov Substitution | A subtype must be usable anywhere its base type is expected, without surprises |
| I | Interface Segregation | Many small, specific interfaces beat one large, general one |
| D | Dependency Inversion | Depend on abstractions, not on concrete implementations |

---

#### 4. Abstraction and Information Hiding — 🟢 Must Know

Expose a simple interface, and hide the implementation details behind it. This is what lets an implementation change (swap a database, rewrite an algorithm) without forcing every caller to change too.

---

#### 5. KISS, YAGNI, DRY — 🟢 Must Know

1. **KISS** (Keep It Simple, Stupid) — prefer the simpler design that meets the actual requirement.
2. **YAGNI** (You Aren't Gonna Need It) — don't build flexibility for a future requirement that may never arrive.
3. **DRY** (Don't Repeat Yourself) — avoid duplicating knowledge... but **DRY can hurt**: forcing two genuinely different concepts to share code just because they look similar today creates a fragile, wrong abstraction that's harder to untangle later than the original duplication would have been.

---

#### 6. Design for Failure — 🟢 Must Know

Assume any part of the system **will** fail — a network call, a dependency, a whole service. Design explicitly for that (timeouts, retries, fallbacks — full detail in topic `12`) rather than treating failure as an edge case to handle later.

---

#### 7. Composition Over Inheritance — 🟡 Good to Know

Prefer building behaviour by **combining small, focused pieces** (composition) rather than deep inheritance hierarchies — inheritance chains tend to become rigid and hard to change safely as they grow.

---

#### 8. Law of Demeter — 🟡 Good to Know

"Only talk to your immediate friends" — a method should only call methods on objects it directly knows about, not reach through a chain (`a.getB().getC().doSomething()`) into objects several levels removed. Reduces coupling to internal structure you don't own.

---

#### 9. Single Source of Truth — 🟡 Good to Know

Each piece of data should have exactly **one** place that's authoritative for it — everywhere else holds a copy or a reference, not a competing "truth". The same principle underlying `SD 23`'s consistency discussion and `19`'s mobile offline-first pattern.

---

#### 10. Principle of Least Astonishment — 🟡 Good to Know

A component should behave the way someone familiar with the system would expect it to — a function named `getUser` that also deletes a session as a side effect violates this, and tends to cause real bugs when someone reasonably assumes it's safe.

---

#### 11. Common Interview Questions

1. **What's the difference between coupling and cohesion, and why do both matter?**
   Cohesion is how focused a module is internally; coupling is how dependent modules are on each other. Good design aims for high cohesion and low coupling — each part is coherent on its own, and changes don't ripple unpredictably.
2. **Can you explain SOLID in plain terms?**
   Walk through the table in item 3 — one reason to change, extend without modifying, safe substitution, small focused interfaces, depend on abstractions.
3. **When does DRY actually hurt a design?**
   When two things that look similar today are conceptually different and will evolve independently — forcing them to share code creates a fragile shared abstraction that's harder to separate later than the original duplication would have been.
4. **What does "design for failure" mean in practice?**
   Assume any dependency can fail, and design explicit handling (timeouts, retries, fallbacks, graceful degradation) from the start, rather than treating failure as an afterthought.

---

#### 12. Common Mistakes

1. Applying DRY to concepts that only look similar coincidentally, creating a fragile shared abstraction.
2. High coupling disguised as "shared utilities" that everything depends on.
3. Building speculative flexibility for requirements that never materialise (violating YAGNI).
4. Treating failure handling as something to add later instead of designing for it from the start.

---

#### 13. Related Topics

1. `5` Architectural Styles — larger-scale structures built from these principles
2. `6` Architecture & Design Patterns — named, reusable applications of these principles
3. `8` Modularity, Coupling & Boundaries — coupling and cohesion applied at the module/service level

---

#### 14. Interview Must Remember

1. **High cohesion, low coupling** — the single most useful lens for any module boundary.
2. **SOLID**, in plain terms, ready to explain without jargon.
3. **DRY can hurt** — don't force unrelated concepts to share code.
4. **Design for failure** from the start, not as an afterthought.
