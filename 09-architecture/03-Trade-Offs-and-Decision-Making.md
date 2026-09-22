# Trade-Offs & Decision Making

Roadmap topic 3 · Stage 1: Role & Mindset

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** "it depends" is the correct answer to almost every architecture question — the actual skill is saying *what* it depends on, writing the decision down, and being honest about what you're giving up. This topic is the method for doing that well.

---

#### 1. There Is No Best Architecture — 🟢 Must Know

*The mindset shift that everything else in this topic builds on.*

Every architectural choice trades one quality attribute against another (topic `2`) — there's no universally "best" database, style, or pattern, only the one that fits this system's ranked priorities and constraints. Say **"it depends on..."** and then name the specific thing it depends on — never leave it as a vague hedge.

---

#### 2. ADR: Architecture Decision Record — 🟢 Must Know

*The standard artifact for recording a decision, short and durable.*

```text
# ADR-014: Use PostgreSQL for the primary data store

Context:    We need a relational store for the Notes API, with strong
            consistency for user data and support for full-text search.

Options:    1. PostgreSQL   2. MySQL   3. DynamoDB

Decision:   PostgreSQL — strong consistency, mature full-text search,
            team already has operational experience with it.

Consequences:
  + Strong consistency and rich querying out of the box
  + Team familiarity reduces operational risk
  - Vertical scaling limits will need addressing beyond ~X req/s
  - Revisit if we need true multi-region active-active writes
```

Keep ADRs **short**, kept next to the code (topic `14`), and never edited after the fact — if a decision changes, write a new ADR that supersedes the old one, so the history stays honest.

---

#### 3. One-Way vs Two-Way Decisions — 🟢 Must Know

1. **Two-way (reversible)** — easy to undo; a library choice, an internal API shape you can still refactor freely.
2. **One-way (hard to reverse)** — a core data model, a service boundary, a primary database — expensive or risky to change later.
3. Spend your limited deliberation effort on **one-way** decisions. A two-way decision made slightly wrong costs little; a one-way decision made wrong can cost months.

---

#### 4. Risk-Driven Design — 🟢 Must Know

Attack the **biggest unknowns first**, not the easiest parts first. A spike, a proof of concept, or a small prototype that tests the riskiest assumption early is worth far more than polishing a part of the design you already understand well.

---

#### 5. Build vs Buy vs Open Source — 🟢 Must Know

| | Build | Buy (managed service) | Open source, self-hosted |
|---|---|---|---|
| Cost | Engineering time | Ongoing subscription | Infrastructure + operational time |
| Control | Full | Limited to what the vendor exposes | Full, but you own the operations |
| Speed to start | Slowest | Fastest | Medium |
| Lock-in | None | Vendor-specific | Lower, but still real |

No universal answer — weigh against the ranked quality attributes and constraints from topic `2`.

---

#### 6. Technology Selection Criteria — 🟢 Must Know

Beyond "which one is technically best": **fit** for the actual problem, **team skills** (can the team actually run this well?), **maturity** (is it production-proven?), **community** (support and hiring pool), **cost**, and a clear **exit path** if it doesn't work out.

---

#### 7. Last Responsible Moment — 🟡 Good to Know

Delay a decision until **waiting starts costing more than deciding would** — not as long as possible, and not as early as possible. Deciding too early locks in a choice before you have enough information; deciding too late blocks the team and wastes the extra time you didn't actually use to learn more.

---

#### 8. Avoid Resume-Driven and Hype-Driven Choices — 🟡 Good to Know

A technology chosen because it's exciting to learn, or trending, rather than because it genuinely fits this system's requirements and the team's skills — a real, common failure mode worth naming and actively guarding against in yourself and in reviews.

---

#### 9. Cost of Delay and Cost of Change — 🟡 Good to Know

Two numbers worth estimating, even roughly, when deciding how much deliberation a decision deserves: what does it cost to wait longer for more information, versus what does it cost to change the decision later if it turns out wrong?

---

#### 10. Common Interview Questions

1. **How do you approach a technical decision with no clearly "best" option?**
   Rank the relevant quality attributes for this system, weigh the real options against them and the constraints, and write the reasoning down as an ADR rather than deciding silently.
2. **What's an ADR, and why write one?**
   A short record of a decision's context, options considered, the choice, and its consequences — kept next to the code, so the reasoning survives even after the people who made it move on.
3. **How do you decide how much time a decision deserves?**
   By whether it's one-way (hard to reverse — deserves real deliberation) or two-way (easy to reverse — decide quickly and move on), and by weighing the cost of delay against the cost of being wrong.
4. **How do you avoid choosing a technology just because it's popular or interesting?**
   Explicitly evaluate against fit, team skills, maturity, community, cost, and exit path — not personal excitement — and name resume-driven or hype-driven reasoning when you notice it, including in your own thinking.

---

#### 11. Common Mistakes

1. Treating a decision as if it has one objectively correct answer, instead of naming the trade-off.
2. Making one-way decisions as quickly and casually as two-way ones.
3. Never writing decisions down, so the reasoning is lost once the people involved move on.
4. Choosing a technology for excitement or hype rather than fit, team skills, and maturity.

---

#### 12. Related Topics

1. `2` Requirements, Constraints & Quality Attributes — what the trade-offs in this topic are weighed against
2. `14` Documentation & Diagrams — where ADRs live long-term
3. `21` Architecture Interview Answers — how to tell a decision story like this out loud

---

#### 13. Interview Must Remember

1. **"It depends" is correct — always say what it depends on.**
2. **ADR = context, options, decision, consequences.** Short, kept next to the code, never edited after the fact.
3. **Spend deliberation effort on one-way decisions**, not two-way ones.
4. **Attack the biggest unknowns first** — risk-driven, not comfort-driven.
