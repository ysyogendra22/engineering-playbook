# Architecture Interview Answers

Roadmap topic 21 · Stage 7: Interview & Practice · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** an architecture interview is really testing whether you can apply everything in Stages 1–6 of this roadmap live, under time pressure, while explaining your reasoning out loud. This topic packages that whole roadmap into a small set of ready answers.

---

#### 1. The Answer Structure — 🟢 Must Know

*The backbone to hang every architecture-interview answer on.*

```text
Clarify → Quality attributes → Options → Decision → Risks → Evolution
```

1. **Clarify** — the actual requirements and constraints (topic `2`), never assumed.
2. **Quality attributes** — name and rank the ones that matter most here.
3. **Options** — the real alternatives, not just the one you'll pick.
4. **Decision** — your recommendation, with the reasoning (topic `3`).
5. **Risks** — what could go wrong, and how you'd mitigate it.
6. **Evolution** — how the design would need to change as scale or requirements grow.

---

#### 2. Name the Trade-Off in Every Choice — 🟢 Must Know

**"I choose X because ...; the cost is ..."** — say both halves, every time. An answer that only states the benefit of a choice, with no acknowledged cost, signals you haven't actually thought through the trade-off (topic `3`).

---

#### 3. Ready Answer: Monolith vs Microservices — 🟢 Must Know

"Monolith first" (`5`, item 2) — start with a modular monolith, clean internal boundaries, and only split into microservices for a specific, real reason (independent team scaling, independent deployment needs) that clearly outweighs the added operational cost.

---

#### 4. Ready Answer: How You Choose a Stack — 🟢 Must Know

Fit for the actual problem, team skills, maturity, community, cost, and exit path (`3`, item 6) — never "because it's popular" or "because I know it well" alone, though team familiarity is a legitimate factor among several, not the only one.

---

#### 5. Ready Answer: How You Handle Change — 🟢 Must Know

Design for cheap change from the start (`16`): clean boundaries, stable contracts, fitness functions. For a specific migration, describe the strangler fig approach (`16`, item 4) over a risky big-bang rewrite.

---

#### 6. Ready Answer: How You Document Decisions — 🟢 Must Know

ADRs (`3`, item 2) kept next to the code (`14`, item 4) — short, with context, options, decision, and consequences, never edited after the fact.

---

#### 7. Ready Answer: How You Keep a Design from Drifting — 🟢 Must Know

Guardrails over gates (`17`, item 1), automated architecture tests as fitness functions (`16`, item 5; `17`, item 3), and clear ownership (`17`, item 9) — enforcement built into the system, not relying on manual policing.

---

#### 8. Tell One or Two Real Decision Stories — 🟢 Must Know

*The connection point to `07-behavioral-leadership`.*

Have one or two real architecture decisions ready in full: context, options, result, and what you'd change (`07-behavioral-leadership/6`) — an interviewer will very often ask you to go deep on a real example, not just explain the theory in the abstract.

---

#### 9. Handling Disagreement and Pushback — 🟡 Good to Know

Disagree and commit, handle pushback with data (`15`, item 5) — the same pattern from `07-behavioral-leadership/9`, directly relevant if an interviewer pushes back on your recommendation mid-interview, which is common and expected.

---

#### 10. Questions to Ask About the Company's Architecture — 🟡 Good to Know

```text
"What's the biggest source of architectural debt right now, and why
 hasn't it been addressed?"
"How are architecture decisions made and recorded here?"
"What's the split between monolith and services, and how did that evolve?"
```

Good questions here double as real signal about the company's engineering maturity (`07-behavioral-leadership/19`, item 7).

---

#### 11. Common Traps — 🟡 Good to Know

1. **Naming tools first** — "we'll use Kafka" before establishing *why* an event-driven approach is even needed here.
2. **Ignoring constraints** — designing an ideal system that ignores the stated budget, deadline, or team skills.
3. **Only the happy path** — never discussing failure modes, security, or what happens at 10x scale.

---

#### 12. Common Interview Questions

1. **Design [a system].** — the direct prompt; use the full structure from item 1, and narrate your reasoning at every step.
2. **Walk me through an architecture decision you made and why.** — item 8; use a real, prepared story.
3. **How would you convince a team to adopt an architectural change they're skeptical of?** — combine item 15's communication skills with the "disagree and commit" pattern from item 9.
4. **What would you do differently on a past project's architecture?** — a genuine, specific answer, the same honesty expected in `07-behavioral-leadership/6`, item 9.

---

#### 13. Common Mistakes

1. Jumping straight to a solution without clarifying requirements and constraints first.
2. Naming a specific technology before establishing the actual need it addresses.
3. Presenting only benefits, never the trade-off cost, for a chosen option.
4. Only ever having theoretical answers ready, with no real decision story to go deep on.

---

#### 14. Related Topics

1. `1`–`20` — this entire folder feeds into this one packaged interview structure
2. `07-behavioral-leadership` (the whole folder, especially topics `2`, `6`, `9`) — the storytelling and disagreement-handling skills this topic draws on directly
3. `22` Practice: Case Studies & Exercises — where this structure actually gets rehearsed

---

#### 15. Interview Must Remember

1. **Clarify → quality attributes → options → decision → risks → evolution** — the structure for every answer.
2. **Always name both halves of a trade-off** — the benefit and the cost.
3. **Have real decision stories ready**, not just theory.
4. **Avoid the three traps**: naming tools first, ignoring constraints, only the happy path.
