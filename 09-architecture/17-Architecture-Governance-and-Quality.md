# Architecture Governance & Quality

Roadmap topic 17 · Stage 5: Evolving & Governing

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** governance done badly is a bottleneck everyone routes around. Governance done well is invisible — the right way to build something is simply the easiest, most natural path, so people follow it without being forced to.

---

#### 1. Guardrails Over Gates — 🟢 Must Know

*The single most important governance mindset.*

A **gate** blocks progress until a manual approval happens — slow, and people learn to route around it. A **guardrail** makes the right way the **easy** way by default (good templates, sensible defaults, automated checks) — people follow it because it's genuinely the path of least resistance, not because they're forced to.

---

#### 2. Architecture Reviews — 🟢 Must Know

Know **when** a review is warranted (a genuinely significant, hard-to-reverse decision — topic `3`), **who** should be in the room (people who'll actually be affected, not everyone), and **what** to look for (alignment with ranked quality attributes, topic `2`; real trade-offs considered, not just one option presented).

---

#### 3. Automated Architecture Tests — 🟢 Must Know

The concrete implementation of fitness functions (`16`, item 5): **dependency rules** (module A must never depend on module B), **layer rules** (the UI layer can't call the database directly), **cycle checks** (`8`, item 8) — run in CI, so violations are caught automatically and immediately, not discovered months later during a manual review.

---

#### 4. Coding Standards and Definition of Done — 🟢 Must Know

A shared, written baseline for what "done" actually means (tests written, reviewed, documented where needed) keeps quality consistent across a team or organisation without needing constant, manual, case-by-case policing.

---

#### 5. Paved Road — 🟡 Good to Know

An approved, well-supported default stack and set of templates for common needs — using it is easy and fast; deviating is allowed, but the deviator takes on more responsibility for figuring things out themselves. A strong practical example of the guardrail philosophy (item 1) in action.

---

#### 6. Tech Radar — 🟡 Good to Know

A structured way to track technology choices across an organisation: **adopt** (use freely), **trial** (try on a real but limited project), **assess** (worth evaluating, not yet proven), **hold** (avoid for new work) — keeps technology choices visible and deliberate rather than ad hoc and inconsistent across teams.

---

#### 7. Balance Standards with Team Autonomy — 🟡 Good to Know

Too little governance and the system fragments into inconsistent, hard-to-maintain approaches (item 1's ungoverned failure mode). Too much and teams lose the ability to make reasonable local decisions and start routing around the process entirely — the right balance is a genuine, ongoing judgment call, not a fixed formula.

---

#### 8. ATAM-Style Reviews — 🟡 Good to Know

A structured method (name and purpose only) for reviewing whether a proposed architecture actually meets its stated quality goals (topic `2`) — useful as a more rigorous reference for especially high-stakes architecture reviews.

---

#### 9. Ownership — 🟡 Good to Know

Knowing exactly **who owns** each service, module, and data set — without clear ownership, quality quietly erodes, since no single person or team feels accountable for maintaining it well over time.

---

#### 10. Common Interview Questions

1. **What's the difference between a guardrail and a gate, and why does it matter?**
   A gate blocks progress until manual approval, and people learn to route around it. A guardrail makes the right path the easiest one by default — better compliance, because it's genuinely the path of least resistance rather than a forced detour.
2. **How do you enforce an architectural rule at scale, without manual policing?**
   Automated architecture tests in CI — dependency rules, layer rules, cycle checks — turning intent into something enforced continuously, rather than something hoped for and occasionally manually reviewed.
3. **How do you decide when a design needs a formal architecture review?**
   For genuinely significant, hard-to-reverse decisions (topic `3`) — not every decision needs one, and over-applying review slows the team without proportionate benefit.
4. **How do you balance standards with team autonomy?**
   An ongoing judgment call — too little governance and the system fragments; too much and teams lose the ability to make reasonable local decisions and start routing around the process. Aim for guardrails, not gates, as the default lever.

---

#### 11. Common Mistakes

1. Relying on manual gates and approvals instead of automated guardrails.
2. Reviewing every decision, significant or not, slowing the team without proportionate benefit.
3. No automated checks for architectural rules, so violations are only caught much later, if at all.
4. Unclear ownership, leading quality to erode with no one clearly accountable.

---

#### 12. Related Topics

1. `16` Evolutionary Architecture & Technical Debt — drift, which governance is meant to catch
2. `3` Trade-Offs & Decision Making — the decisions this topic's reviews are about
3. `18` Teams & Delivery — how governance interacts with team structure and delivery speed

---

#### 13. Interview Must Remember

1. **Guardrails over gates** — make the right way the easy way.
2. **Automated architecture tests in CI**, not manual policing.
3. **Review only genuinely significant, hard-to-reverse decisions.**
4. **Clear ownership** for every service, module, and data set.
