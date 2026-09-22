# Evolutionary Architecture & Technical Debt

Roadmap topic 16 · Stage 5: Evolving & Governing

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** no architecture is finished — requirements change, teams change, scale changes. The real skill isn't designing something that never needs to change; it's designing so that change stays cheap, and managing the debt that accumulates along the way honestly.

---

#### 1. Architecture Changes Over Time — 🟢 Must Know

*The foundational mindset for this whole topic.*

Design explicitly **so that change is cheap** — clean boundaries (topic `8`), stable contracts (topic `10`), and clear ownership all pay off specifically when the system needs to evolve, which it always eventually does.

---

#### 2. Technical Debt — 🟢 Must Know

1. **Deliberate debt** — a conscious shortcut taken to ship faster, with the trade-off understood and ideally recorded (an ADR, topic `3`).
2. **Accidental debt** — arises from not knowing better at the time, or from a design that made sense once but no longer fits as the system grew.
3. **Track it** — a visible backlog or register, not just something everyone silently knows about and complains over privately.

---

#### 3. Refactoring in Small, Safe Steps — 🟢 Must Know

Large, risky refactors invite large, risky bugs — prefer many small, individually safe, individually testable steps over one sweeping change with an uncertain blast radius.

---

#### 4. Strangler Fig Migration — 🟢 Must Know

```text
Old system  ──────────►  Old system  ────►  Old system (shrinking)
                          ↑ new feature       ↑ old features migrated
Traffic ──► Facade        built new           one by one, old system
                                               eventually removed
```

Replace a legacy system **piece by piece** behind a stable facade, routing traffic to the new implementation gradually as pieces are migrated, until the old system can finally be retired — far safer than a big-bang rewrite (item 9).

---

#### 5. Fitness Functions — 🟢 Must Know

Automated checks that verify an architectural quality **still holds**, run continuously (often in CI): a dependency-direction check, a module-boundary check, a performance budget check (`12`, item 10). Turns architectural intent into something enforced, not just documented and hoped for.

---

#### 6. Deprecation and Removal Plans — 🟢 Must Know

Removing an old API, feature, or system needs a **plan**, not just a decision — a timeline, a communication plan to affected consumers, and a clear cutoff, respecting the reality that old clients (`10`, item 3) can't be forced to move instantly.

---

#### 7. Architecture Drift and Erosion — 🟡 Good to Know

Over time, the **real** system slowly diverges from the **intended** design — small compromises, shortcuts under deadline pressure, and undocumented exceptions accumulate. This is exactly what fitness functions (item 5) and governance (`17`) are meant to catch early, before drift becomes severe.

---

#### 8. Large Migrations Without Downtime — 🟡 Good to Know

Moving to a new database, schema, or platform live, with users still using the system throughout — full pattern detail in `SD 33`; the strangler fig approach (item 4) is the general architectural shape this specific kind of migration usually takes.

---

#### 9. Rewrite vs Refactor — 🟡 Good to Know

A full rewrite is tempting but **often fails** — it takes longer than expected, the old system must be kept running and maintained in parallel the whole time, and the rewrite often reintroduces bugs the old system had long since fixed. Refactoring incrementally (item 3) is usually the safer default; reserve a rewrite for cases where the existing system is genuinely unsalvageable.

---

#### 10. Versioning Strategy — 🟡 Good to Know

A consistent, deliberate approach to versioning across APIs, data schemas, and even app releases (`MOB 15`) — decided once at the architecture level, rather than each team inventing its own inconsistent convention independently.

---

#### 11. Common Interview Questions

1. **How do you keep an architecture from becoming rigid over time?**
   Design explicitly for cheap change — clean boundaries, stable contracts, clear ownership — and use fitness functions to keep enforcing those properties automatically as the system grows.
2. **What's the difference between deliberate and accidental technical debt?**
   Deliberate debt is a conscious, ideally-recorded trade-off made to ship faster. Accidental debt arises from not knowing better at the time, or a design outgrowing its original fit — both need to be tracked visibly either way.
3. **How would you migrate off a legacy system safely?**
   Strangler fig — replace it piece by piece behind a stable facade, routing traffic to the new implementation gradually, rather than a risky big-bang rewrite.
4. **When would you choose a rewrite over a refactor?**
   Rarely, and only when the existing system is genuinely unsalvageable — rewrites usually take longer than expected, require running two systems in parallel, and tend to reintroduce already-solved bugs.

---

#### 12. Common Mistakes

1. Letting technical debt accumulate invisibly, with no tracked backlog or register.
2. A risky, large-scale refactor attempted in one big step.
3. Choosing a rewrite by default, underestimating its real cost and risk.
4. Deprecating something with no communication plan for affected consumers.

---

#### 13. Related Topics

1. `8` Modularity, Coupling & Boundaries — what makes change cheap in the first place
2. `17` Architecture Governance & Quality — how drift gets caught and corrected
3. `6` Architecture & Design Patterns — the strangler fig pattern referenced in item 4

---

#### 14. Interview Must Remember

1. **Design so that change is cheap** — this is the core evolutionary-architecture mindset.
2. **Track technical debt visibly**, deliberate or accidental.
3. **Strangler fig** for safe legacy migration, not a big-bang rewrite.
4. **Fitness functions** enforce architectural intent automatically, catching drift early.
