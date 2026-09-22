# What an Architect Does

Roadmap topic 1 · Stage 1: Role & Mindset

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** an architect's job is not to draw diagrams — it's to make the handful of decisions in a system that are expensive to change later, make them well, and help the team actually follow through on them.

---

#### 1. Architecture = The Costly-to-Change Decisions — 🟢 Must Know

*The single best working definition to carry into every conversation.*

1. Architecture is the set of decisions about a system's structure that are **expensive or slow to reverse** — choosing a database, a service boundary, a communication style, a core data model.
2. Decisions that are cheap to change later (a variable name, which library formats dates) are not architecture, however technical they look.
3. This definition is what tells you where to spend your limited attention as an architect: on the decisions that would hurt to get wrong.

---

#### 2. The Architect's Job — 🟢 Must Know

Three parts, in practice:

1. **Make the key decisions** — using the process in topic `3`.
2. **Keep them consistent** — across teams, services, and time, so the system doesn't quietly fragment into contradictory approaches.
3. **Help the team follow them** — through documentation (topic `14`), communication (topic `15`), and governance that makes the right way the easy way (topic `17`).

---

#### 3. Architect vs Tech Lead vs Senior Engineer — 🟢 Must Know

| Role | Typical scope | Distance from the code |
|---|---|---|
| Senior engineer | Deep on their own area | Very close, hands in the code daily |
| Tech lead | One team's technical direction | Close, still writes code regularly |
| Architect | Across teams or the whole system | Further, but never fully detached (item 4) |

The boundaries are fuzzy and differ by company — the useful distinction is **scope** (how many teams/systems your decisions touch), not seniority alone.

---

#### 4. Stay Hands-On — 🟢 Must Know

*The antidote to the most common architecture failure mode (item 7).*

Read real code, build spikes and prototypes yourself (topic `3`), and join code reviews. An architect who only draws diagrams loses the ability to make decisions grounded in reality, and loses the team's trust along with it.

---

#### 5. Breadth Over Depth — 🟢 Must Know

Know a little about many areas (data, security, mobile, infrastructure, the business domain), and go deep specifically where the **risk** is highest for the current project. Trying to be equally deep everywhere is neither possible nor useful — targeted depth beats even, shallow breadth.

---

#### 6. Types of Architect — 🟡 Good to Know

Titles and scopes vary by company, but common flavours: **solution architect** (one project or product), **software architect** (one system's internal design), **enterprise architect** (across many systems and the business), **cloud architect** (infrastructure-focused), **mobile architect** (client-side systems, `19`). Know the names; don't over-index on exact title boundaries, which differ everywhere.

---

#### 7. The "Ivory Tower" Failure — 🟡 Good to Know

*Worth naming explicitly, because it's the most common way architects lose credibility.*

An architect who draws diagrams and dictates decisions, but doesn't build anything real or listen to the engineers actually doing the work — decisions made this way tend to be disconnected from reality, and the team stops trusting or following them.

---

#### 8. Common Interview Questions

1. **What does an architect actually do, day to day?**
   Make the costly-to-reverse decisions well, keep them consistent across the system, and help the team follow through — while staying hands-on enough to keep decisions grounded in reality.
2. **How is an architect different from a senior engineer or tech lead?**
   Mainly scope — how many teams or systems the decisions touch — not a strict seniority ladder; boundaries vary by company.
3. **How do you decide where to focus your attention as an architect?**
   Where the decision is both important and hard to reverse, and go deep specifically where the risk is highest, rather than trying to be equally deep everywhere.
4. **What's the "ivory tower" failure mode, and how do you avoid it?**
   An architect disconnected from real code and the team's actual constraints. Avoided by staying hands-on — writing spikes, reading code, joining reviews.

---

#### 9. Common Mistakes

1. Treating every technical decision as "architecture", spreading attention too thin.
2. Drawing diagrams and making pronouncements without staying hands-on.
3. Going equally deep everywhere instead of targeting the highest-risk areas.
4. Confusing title/seniority with actual decision scope.

---

#### 10. Related Topics

1. `2` Requirements, Constraints & Quality Attributes — what shapes the decisions this topic is about
2. `3` Trade-Offs & Decision Making — the actual decision-making process
3. `15` Communicating & Influencing — how decisions actually get followed, not just made

---

#### 11. Interview Must Remember

1. **Architecture = the decisions that are expensive to change later.**
2. **The job: decide, keep consistent, help the team follow.**
3. **Stay hands-on** — spikes, code review, real code — to avoid the "ivory tower" failure.
4. **Breadth generally, depth where the risk is.**
