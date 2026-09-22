# Modularity, Coupling & Boundaries

Roadmap topic 8 · Stage 2: Design Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** a module boundary is a promise — "depend on this small, stable surface, and I can change everything behind it freely." Most large-codebase pain comes from boundaries that were never really drawn, or were drawn and then quietly ignored.

---

#### 1. Module Boundaries: Small Public API, Hidden Inside — 🟢 Must Know

Expose only what other modules genuinely need, and keep everything else internal. A module with a large, leaky public surface gives callers too many ways to depend on details that should be free to change — the same principle as `4`'s abstraction, applied at the module level.

---

#### 2. Dependency Direction — 🟢 Must Know

```text
Stable, general abstractions
        ↑
Depend on THIS direction, not the reverse
        ↑
Concrete, volatile details
```

Depend on **stable abstractions**, not on volatile details — this is SOLID's Dependency Inversion (`4`) applied at the architecture scale, and it's what keeps a change in one detail (a specific database driver) from rippling through everything that used it.

---

#### 3. Package by Feature vs by Layer — 🟢 Must Know

1. **By layer** — `controllers/`, `services/`, `repositories/` — everything for one feature is scattered across several top-level folders.
2. **By feature** — `notes/`, `users/`, `billing/` — everything for one feature lives together, each containing its own layers internally.

Packaging by feature generally gives **higher cohesion** (item from `4`) and makes a codebase easier to split into modules or services later, since the boundaries already exist.

---

#### 4. Conway's Law — 🟢 Must Know

*A system's design mirrors the communication structure of the team that built it.*

If three teams build one service together with constant cross-team coordination needed, expect the service's internal structure to reflect that same tangled communication pattern. Worth deliberately accounting for when designing both the system **and** the team structure together (`18`).

---

#### 5. Contracts Between Modules and Services — 🟢 Must Know

The agreed shape of what one module or service expects from, and promises to, another — and critically, **how that contract changes over time** without breaking existing callers (the same discipline as `10`'s API versioning, applied to internal boundaries too, not just external APIs).

---

#### 6. Monorepo vs Polyrepo — 🟡 Good to Know

| | Monorepo | Polyrepo |
|---|---|---|
| Cross-cutting changes | Easier — one atomic commit | Harder — coordinate across repos |
| Tooling | Needs investment at scale | Simpler per-repo, but more repos to manage |
| Team autonomy | Lower by default | Higher by default |

Neither is universally correct — the choice interacts with team structure (item 4) and how independently different parts need to evolve.

---

#### 7. Shared Code and Shared Libraries — 🟡 Good to Know

Sharing code reduces duplication, but it also creates **coupling**: every consumer of a shared library is now tied to its release cadence and its breaking changes. Share deliberately, and version shared libraries carefully — not everything that looks similar needs to be shared (the same DRY caution from `4`).

---

#### 8. Measuring Coupling — 🟡 Good to Know

**Dependency graphs** visualise which modules depend on which; **cyclic dependencies** (A depends on B depends on A) are a strong warning sign — they mean two "separate" modules can't actually be understood, built, or changed independently, defeating the purpose of the boundary.

---

#### 9. Boundaries Inside a Monolith — 🟡 Good to Know

A **modular monolith** enforces the same clean boundaries (small public API, controlled dependency direction) that microservices would enforce, but within one deployable — giving many of the organisational benefits without the operational cost of distribution (`5`, item 2).

---

#### 10. Common Interview Questions

1. **How do you decide where to draw a module boundary?**
   Group by feature/cohesion rather than by technical layer, keep the public API small, and control dependency direction so stable abstractions don't depend on volatile details.
2. **What is Conway's law, and why does it matter for architecture?**
   A system's structure mirrors its team's communication structure — worth designing team structure and system structure together, rather than assuming architecture is independent of organisational reality.
3. **What's a cyclic dependency, and why is it a problem?**
   Two modules depending on each other, directly or indirectly — it means neither can really be built, tested, or changed independently, which defeats the purpose of having drawn a boundary between them at all.
4. **What's a modular monolith, and why might you choose one over microservices?**
   A single deployable with strict internal module boundaries — gets much of the organisational clarity of microservices without their operational cost; a strong "monolith first" default (`5`).

---

#### 11. Common Mistakes

1. Packaging by technical layer, scattering one feature's code across many top-level folders.
2. A module's public API growing large and leaky over time, with no one enforcing it.
3. Cyclic dependencies between modules, quietly defeating the point of the boundary.
4. Sharing code between modules that don't actually share a real concept, just superficially similar logic.

---

#### 12. Related Topics

1. `4` Design Principles — cohesion and coupling as the foundational lens
2. `7` Domain-Driven Design Essentials — bounded contexts as a domain-level boundary concept
3. `18` Teams & Delivery — Conway's law and the inverse Conway manoeuvre, applied to team design

---

#### 13. Interview Must Remember

1. **Small public API, dependency direction toward stable abstractions.**
2. **Package by feature**, generally, over packaging by layer.
3. **Conway's law**: system structure mirrors team structure — design both together.
4. **Cyclic dependencies are a strong warning sign** — they defeat the purpose of a boundary.
