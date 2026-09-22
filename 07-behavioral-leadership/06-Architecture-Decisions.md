# Architecture Decisions

Roadmap topic 6 · Stage 2: Core Stories

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond your original ten topics

**In simple words:** this is a technical-decision story (topic `5`) at a bigger scale — one with lasting structural impact, introduced carefully, and explained in plain language even though the underlying choice was complex.

---

#### 1. Pick a Decision with Lasting Impact — 🟢 Must Know

Good candidates: a **modularization** effort, a **state-architecture change** (e.g. adopting a clearer MVVM/MVI pattern), going **offline-first**, a **large migration**, or a **platform choice**. The common thread: something that shaped how the codebase or team worked for a long time afterward, not a one-off fix.

---

#### 2. Explain the Context and Quality Goals — 🟢 Must Know

What problem was the architecture actually solving — slow builds, hard-to-test code, poor offline behaviour, team scaling issues? Naming the **quality attribute** that was suffering (`ARCH 2`) — maintainability, testability, performance — makes the "why" concrete instead of abstract.

---

#### 3. Explain the Options and Trade-Offs in Plain Language — 🟢 Must Know

Translate the technical comparison into terms a non-architect interviewer (or a broader panel) can follow — cost, risk, time, and what you gave up, not framework jargon. If you can't explain it simply, it's a sign to practise the explanation, not a sign the interviewer isn't technical enough.

---

#### 4. Explain How You Introduced It Safely — 🟢 Must Know

Big architecture changes rarely land as one giant rewrite — describe the **incremental steps** and the **checks** along the way (a strangler-fig-style migration, `ARCH 16`): one module first, a proof it worked, then expanding. This shows engineering maturity, not just a good idea.

---

#### 5. Explain the Result and How You Knew It Worked — 🟢 Must Know

Concrete signal that the change actually helped: build time dropped, crash rate fell, a feature that used to take weeks now takes days, fewer bugs in a specific category. Vague "it's cleaner now" claims are weak without a measurable signal behind them.

---

#### 6. How You Handled Technical Debt — 🟡 Good to Know

If the story involves choosing to refactor vs rewrite (`ARCH 16`), explain that reasoning specifically — a rewrite is rarely the safe default, and saying so (with why refactoring won here) shows judgment.

---

#### 7. How You Documented and Taught It — 🟡 Good to Know

A design doc, an ADR, a team walkthrough (`ARCH 14`) — architecture decisions that aren't communicated tend to erode as new people join and don't know the reasoning behind existing patterns.

---

#### 8. How You Kept the Design from Drifting — 🟡 Good to Know

Code review norms, lint rules, module boundary enforcement (`ARCH 17`) — a good architecture decision that nobody protects afterward slowly decays; mention what you put in place to keep it intact.

---

#### 9. A Decision That Turned Out Wrong — 🟡 Good to Know

An honest example where an architecture choice didn't pan out as hoped, and what you changed in response — pairs well with topic `7`'s failure-story guidance, and shows the same honesty as a reversed technical decision (topic `5`, item 6).

---

#### 10. Common Interview Questions

1. **"Tell me about an architecture decision you led."** — use the full shape from items 1–5.
2. **"How do you introduce a big architectural change without breaking things?"** — item 4's incremental-rollout answer.
3. **"How do you explain a technical trade-off to a non-technical stakeholder?"** — item 3's plain-language skill, which also connects to topic `11`.
4. **"Tell me about an architecture decision that didn't work out."** — item 9; have a genuine example, not a deflection.

---

#### 11. Common Mistakes

1. Describing the final architecture without explaining the context or quality goals that drove it.
2. Presenting a big-bang rewrite as if it were the safe, obvious choice.
3. No measurable signal that the change actually helped.
4. Never mentioning how the design was protected from drifting afterward.

---

#### 12. Related Topics

1. `5` Technical Decisions — the smaller-scale version of this story shape
2. `ARCH 2`, `ARCH 3`, `ARCH 16`, `ARCH 17` — the architect-level frameworks this story draws on
3. `11` Communication & Stakeholder Management — explaining trade-offs in plain language

---

#### 13. Interview Must Remember

1. **Pick a decision with real, lasting impact** — modularization, offline-first, a migration, a platform choice.
2. **Name the quality goal it addressed**, and explain trade-offs in plain language.
3. **Show an incremental rollout with checks**, not a risky big-bang change.
4. **A measurable signal it worked**, and how the design was protected afterward.
