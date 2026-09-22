# Documentation & Diagrams

Roadmap topic 14 · Stage 4: Documenting & Communicating

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** an architecture that lives only in your head might as well not exist for anyone else on the team. Good documentation isn't about writing more — it's about drawing and writing the small set of things that actually help someone else understand and build the system correctly.

---

#### 1. The C4 Model — 🟢 Must Know

*The single most useful diagramming framework for this whole topic — four zoom levels, each for a different audience.*

```text
Level 1 — System Context:  your system, its users, and other systems it talks to
Level 2 — Containers:      the major deployable pieces inside your system
                            (mobile app, backend API, database, queue)
Level 3 — Components:      the major internal pieces of one container
Level 4 — Code:            class-level detail (rarely drawn; the code itself is
                            usually clearer than a diagram at this level)
```

Most architecture conversations only need **Levels 1 and 2** — draw those first, and only go deeper where genuinely useful.

---

#### 2. Draw for Your Audience — 🟢 Must Know

A diagram for business stakeholders should look different from one for the engineering team building it — the former emphasises user value and major systems; the latter can show technical detail (protocols, specific technologies). One diagram rarely serves every audience well.

---

#### 3. Key Flow Diagrams — 🟢 Must Know

**Sequence diagrams** for the main use cases — showing the actual order of calls between components for one real scenario ("user creates a note while offline") — often clearer than a static structure diagram for explaining *how* something actually works end to end.

---

#### 4. ADRs Kept Next to the Code — 🟢 Must Know

ADRs (topic `3`) should live in the repository itself, not in a separate wiki that goes stale — keeping them next to the code they describe makes them far more likely to actually be found and read by the next engineer working in that area.

---

#### 5. Design Docs / RFCs — 🟢 Must Know

A written proposal — **problem, options, decision, risks** — reviewed by others **before** building, not written up afterward as an afterthought. The review process itself is often as valuable as the document, surfacing objections and blind spots while they're still cheap to address.

---

#### 6. Views: Logical, Process, Deployment, Data — 🟡 Good to Know

Different "views" of the same system, each answering a different question: **logical** (how is functionality organised?), **process** (how do things run and communicate at runtime?), **deployment** (what runs where, physically?), **data** (how does data flow and where does it live?). Not every system needs all four documented explicitly, but knowing they're distinct questions helps you notice which one a stakeholder is actually asking about.

---

#### 7. UML Basics — 🟡 Good to Know

Sequence, component, and class diagrams are the most commonly useful UML types in practice — full UML has far more notation than is usually worth learning; C4 (item 1) and sequence diagrams cover most real needs.

---

#### 8. Docs as Code — 🟡 Good to Know

Text-based diagram formats (that render into images from plain text kept in the repo) let diagrams be version-controlled, reviewed in pull requests, and kept in sync with the code they describe — far more durable than a diagram trapped in a slide deck or a separate design tool.

---

#### 9. arc42 and Similar Templates — 🟡 Good to Know

Structured documentation templates (name only) that prompt you to cover the standard set of architecture concerns systematically — useful as a checklist for a full architecture document, when one is genuinely needed.

---

#### 10. Keep Docs Short and Current — 🟡 Good to Know

**Delete what's stale.** A wrong, outdated diagram is worse than no diagram — it actively misleads. Treat documentation like code: review it, update it when the system changes, and remove it when it no longer reflects reality.

---

#### 11. Common Interview Questions

1. **What's the C4 model, and how do you use it?**
   Four zoom levels — context, containers, components, code. Most real conversations only need the top two levels; draw those first and go deeper only where it genuinely helps.
2. **How do you decide what to document?**
   By audience and purpose — key decisions as ADRs kept next to the code, proposals as reviewed design docs before building, and diagrams at the zoom level that actually matches the question being asked.
3. **Why is stale documentation worse than no documentation?**
   It actively misleads someone into believing something that's no longer true — documentation needs the same ongoing maintenance discipline as code, or it should be deleted.
4. **What's the value of a design doc review, beyond the document itself?**
   The review process surfaces objections and blind spots while the decision is still cheap to change, rather than after implementation has already started.

---

#### 12. Common Mistakes

1. Drawing every diagram at maximum detail, regardless of audience.
2. ADRs and design docs scattered across tools disconnected from the code.
3. Writing a design doc only after the implementation is already done, skipping the review's real value.
4. Letting diagrams and docs go stale instead of updating or deleting them.

---

#### 13. Related Topics

1. `3` Trade-Offs & Decision Making — the ADRs this topic explains how to store and present
2. `15` Communicating & Influencing — how these documents actually get used in real conversations
3. `21` Architecture Interview Answers — drawing a C4-style diagram live in an interview

---

#### 14. Interview Must Remember

1. **C4 model**: context and containers cover most real conversations.
2. **ADRs live next to the code**, not in a separate, easily-forgotten wiki.
3. **Design docs are reviewed before building**, not written up afterward.
4. **Stale documentation is worse than none** — keep it current, or delete it.
