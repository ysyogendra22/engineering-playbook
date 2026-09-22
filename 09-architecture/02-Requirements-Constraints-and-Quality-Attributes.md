# Requirements, Constraints & Quality Attributes

Roadmap topic 2 · Stage 1: Role & Mindset

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** before you can design anything well, you need to know what "good" actually means for this specific system — and "good" is almost never just "it works". This topic is about making that explicit, measurable, and ranked, instead of assumed.

---

#### 1. Functional Requirements vs Quality Attributes — 🟢 Must Know

1. **Functional requirements** — what the system does: "users can create a note", "the app supports offline editing".
2. **Quality attributes** — how well it does it: how fast, how available, how secure, how maintainable.
3. Most architecture decisions are actually driven by quality attributes, not functional requirements — two systems doing the exact same thing can need completely different architectures if their quality needs differ.

---

#### 2. Key Quality Attributes — 🟢 Must Know

The standard list to know and be able to name unprompted: **performance, scalability, availability, reliability, security, maintainability, testability, observability, usability, cost.**

```text
"The system must let users create notes" → functional
"Note creation must complete in under 300ms at p95, for 100k
 concurrent users, with 99.9% availability" → the same requirement,
 with quality attributes attached
```

---

#### 3. Architecturally Significant Requirements (ASRs) — 🟢 Must Know

Not every requirement shapes the architecture — an **ASR** is one of the few that genuinely does: a scale target, a strict latency bound, a compliance requirement, an offline requirement. Identifying the 5–8 real ASRs (rather than treating every requirement as equally architecturally important) is what makes the design process tractable.

---

#### 4. Make Them Measurable — 🟢 Must Know

*The single highest-leverage discipline in this whole topic.*

"Fast" is not a requirement you can design against. **"p95 latency under 300ms"** is. Push every vague quality claim toward a number, even a rough, agreed-upon estimate — an unmeasurable requirement can't be verified, and can't drive a real design decision.

---

#### 5. Constraints — 🟢 Must Know

Fixed limits you must accept, not choose: **budget, deadline, team skills, existing systems, regulation, vendor rules.** Unlike quality attributes (which you're free to weigh and trade off), constraints are boundaries the design must simply fit inside.

---

#### 6. Rank the Quality Attributes — 🟢 Must Know

*You cannot maximise all ten from item 2 at once — every design is a set of trade-offs (topic `3`).*

Force an explicit ranking for this specific system: is availability more important than strict consistency here? Is cost more important than raw performance? Writing the ranking down (even roughly) turns implicit, contested trade-offs into an explicit, agreed decision.

```text
Example ranking for a payments feature:
1. Security       (non-negotiable)
2. Reliability     (money must not be lost or duplicated)
3. Availability
4. Performance
5. Cost            (lowest priority here — correctness matters more)
```

---

#### 7. Quality Attribute Scenarios — 🟡 Good to Know

A structured way to make a quality attribute concrete: **stimulus** (what happens — a traffic spike, a node failure), **response** (what the system should do), **measure** (how you'd know it worked). Turns "the system should be available" into something testable.

---

#### 8. Business Drivers and Stakeholder Needs — 🟡 Good to Know

Quality attributes ultimately trace back to real business or user needs — a startup's "move fast" driver and a bank's "never lose a transaction" driver lead to very different rankings in item 6, even for superficially similar systems.

---

#### 9. Standards for Quality Models — 🟡 Good to Know

Formal quality-model standards exist (names only, not needed in depth) — useful to know they exist as a more rigorous reference, without needing to memorise them for most architecture work.

---

#### 10. Common Interview Questions

1. **What's the difference between a functional requirement and a quality attribute?**
   Functional = what the system does. Quality attribute = how well it does it (speed, availability, security, and so on) — and quality attributes are usually what actually drive the architecture.
2. **How do you turn a vague requirement like "the system should be fast" into something you can design against?**
   Push for a measurable number — "p95 latency under 300ms" — even if it starts as a rough, agreed estimate; an unmeasurable requirement can't drive or verify a design decision.
3. **How do you decide which requirements matter most for the architecture?**
   Identify the architecturally significant requirements (ASRs) — the small set that genuinely shapes structural decisions — and explicitly rank the quality attributes against each other for this specific system.
4. **What's the difference between a requirement and a constraint?**
   A requirement is something you design to satisfy and can trade off against others. A constraint (budget, deadline, existing systems) is a fixed limit the design must simply fit inside.

---

#### 11. Common Mistakes

1. Designing against vague, unmeasurable requirements ("it should be fast", "it should scale").
2. Treating every stated requirement as equally architecturally significant.
3. Never explicitly ranking quality attributes, leaving trade-offs implicit and later contested.
4. Confusing a constraint (fixed, must accept) with a quality attribute (can be weighed and traded off).

---

#### 12. Related Topics

1. `1` What an Architect Does — why this is the first real step in the process
2. `3` Trade-Offs & Decision Making — what the ranking in item 6 feeds directly into
3. `12` Scalability, Performance & Resilience — where several of these quality attributes get designed for in depth

---

#### 13. Interview Must Remember

1. **Functional = what. Quality attribute = how well.** Quality attributes usually drive the architecture.
2. **Make every quality requirement measurable** — a number, not an adjective.
3. **Identify the ASRs** — the few requirements that actually shape the design.
4. **Explicitly rank quality attributes** — you can't maximise all of them.
