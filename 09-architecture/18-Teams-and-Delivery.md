# Teams & Delivery

Roadmap topic 18 · Stage 5: Evolving & Governing

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** architecture and team structure aren't separate concerns — Conway's law means they shape each other constantly. A good architect designs both together, and thinks about how work actually gets delivered, not just how the system is drawn on a diagram.

---

#### 1. Conway's Law and the Inverse Conway Manoeuvre — 🟢 Must Know

*Introduced in topic `8` — this is where it becomes an active design tool, not just an observation.*

Since a system's structure mirrors its team's communication structure, you can work the relationship **deliberately**: structure the **teams** first, in the shape you want the **architecture** to eventually take — the "inverse Conway manoeuvre". A powerful, underused lever for architects who have influence over team structure.

---

#### 2. Walking Skeleton — 🟢 Must Know

The **thinnest possible end-to-end slice** that runs through every layer of the system — not fully featured, but genuinely connected start to finish (client, through the API, to the database, and back). Build this first, before fleshing out features — it validates the whole architecture actually works together, far earlier than building one layer fully before starting the next.

---

#### 3. Vertical Slices vs Horizontal Layers — 🟢 Must Know

1. **Horizontal** — build the entire database layer, then the entire API layer, then the entire UI — nothing is genuinely usable until all layers are done.
2. **Vertical slice** — build one complete feature through every layer (a thin walking skeleton, item 2, extended one feature at a time) — something real and demonstrable after every slice.

Vertical slices generally reduce risk and produce earlier, more honest feedback about whether the design actually works.

---

#### 4. DevOps Mindset — 🟢 Must Know

**"You build it, you run it."** The team that builds a service also operates it in production — creates a direct, tight feedback loop between design decisions and their real operational consequences, rather than throwing a system "over the wall" to a separate operations team that has no say in the original design.

---

#### 5. Delivery Metrics (DORA) — 🟢 Must Know

Four well-known measures of software delivery performance:

1. **Deployment frequency** — how often changes ship to production.
2. **Lead time for changes** — how long from code committed to running in production.
3. **Change failure rate** — what fraction of deployments cause a problem.
4. **Time to restore service** — how quickly the team recovers from an incident.

Use these as a **team-level** signal for delivery health (`07-behavioral-leadership/14`, item 7) — never to rank or blame individuals.

---

#### 6. Team Topologies — 🟡 Good to Know

A model of four common team types and how they interact: **stream-aligned** (owns delivery of one value stream end to end), **platform** (provides self-service capabilities to stream-aligned teams), **enabling** (helps other teams adopt new skills/practices), **complicated-subsystem** (owns one especially complex, specialised part). Useful vocabulary for reasoning about team structure alongside architecture.

---

#### 7. Architecture in Agile Teams — 🟡 Good to Know

**Just enough design up front** — some upfront architectural thinking (topic `2`, `3`) genuinely reduces risk and rework, but excessive upfront design in an agile context wastes effort on a design that will change anyway as real learning happens. The balance depends on how well-understood and how one-way (topic `3`) the key decisions actually are.

---

#### 8. MVP Thinking — 🟡 Good to Know

What to build now versus deliberately defer — closely related to the walking skeleton (item 2) and vertical slices (item 3): build the smallest real thing that answers the most important open question first.

---

#### 9. Onboarding — 🟡 Good to Know

Docs, diagrams, and code that a genuinely new person can actually read and follow (`14`) — a real, practical test of whether documentation and architecture clarity are actually working, not just an HR checkbox.

---

#### 10. Common Interview Questions

1. **What's Conway's law, and how can you use it deliberately?**
   A system's structure mirrors its team's communication structure. You can use this deliberately — the inverse Conway manoeuvre — by structuring teams first, in the shape you want the resulting architecture to take.
2. **What's a walking skeleton, and why build it first?**
   The thinnest possible end-to-end slice through every layer of the system — validates the whole architecture actually connects and works together far earlier than building one layer fully before starting the next.
3. **Vertical slices vs horizontal layers — which do you prefer, and why?**
   Vertical slices, generally — each one produces something real and demonstrable, reducing risk and surfacing honest feedback earlier than building complete horizontal layers with nothing usable until everything is done.
4. **How do DORA metrics get used well vs badly?**
   Well: as a team-level signal for improving delivery process. Badly: as a way to rank or blame individual engineers — a framing to explicitly avoid.

---

#### 11. Common Mistakes

1. Designing the architecture and the team structure separately, ignoring how they shape each other.
2. Building complete horizontal layers before anything is genuinely usable end to end.
3. Throwing a system "over the wall" to a separate operations team with no ownership of production outcomes.
4. Using delivery metrics to rank or blame individuals instead of improving team process.

---

#### 12. Related Topics

1. `8` Modularity, Coupling & Boundaries — where Conway's law is first introduced
2. `07-behavioral-leadership/14` — the team-health framing of delivery metrics
3. `22` Practice: Case Studies & Exercises — where a walking skeleton gets built in practice

---

#### 13. Interview Must Remember

1. **Conway's law works both ways** — use the inverse Conway manoeuvre deliberately.
2. **Walking skeleton first** — the thinnest genuine end-to-end slice.
3. **Vertical slices over horizontal layers**, generally.
4. **DORA metrics are for team process, never for ranking individuals.**
