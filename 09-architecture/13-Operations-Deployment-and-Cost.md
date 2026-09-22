# Operations, Deployment & Cost

Roadmap topic 13 · Stage 3: Cross-Cutting Concerns

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** a design that's elegant on paper but painful or expensive to actually run in production isn't a good design — operability and cost are architectural concerns, not something to figure out after the system is built.

---

#### 1. CI/CD and Safe Release Strategies — 🟢 Must Know

Automated build, test, and deployment, plus a deliberate release strategy (canary, blue-green, staged rollout — `SD 28`) — reduces the risk of every single change, and is itself an architectural decision about how the system is designed to evolve safely over time.

---

#### 2. Observability — 🟢 Must Know

**Logs, metrics, traces** (`SD 27`) — designed in from the start, not bolted on after the first production incident. A system you can't observe is a system you can't safely operate or improve.

---

#### 3. Environments and Configuration — 🟢 Must Know

Clear separation between environments (dev, staging, production), and configuration managed explicitly (not hardcoded, not scattered) — a foundational operational hygiene practice that a surprising number of production incidents trace back to getting wrong.

---

#### 4. Infrastructure as Code — 🟢 Must Know

Servers and cloud resources defined in versioned files, not clicked together manually in a console — makes infrastructure changes reviewable, repeatable, and recoverable, the same discipline as version-controlling application code.

---

#### 5. Cost as a Design Constraint — 🟢 Must Know

Cloud bills, the build-vs-buy trade-off (`3`, item 5), and right-sizing resources are real architectural inputs, not just a finance-team afterthought. A technically elegant design that's unaffordable at the required scale is not actually a good design — mention cost explicitly when comparing options.

---

#### 6. Containers and Orchestration — 🟡 Good to Know

Names and concepts (not deep Kubernetes internals): containers package an application with its dependencies for consistent deployment; an orchestrator manages running many containers across machines, handling scheduling, scaling, and recovery.

---

#### 7. Cloud Service Models — 🟡 Good to Know

**IaaS** (infrastructure as a service — raw compute/storage, you manage the OS up), **PaaS** (platform as a service — you manage code, the platform manages the runtime), **SaaS** (software as a service — fully managed application) — a spectrum of how much operational responsibility you take on versus hand to a provider.

---

#### 8. Twelve-Factor App Principles — 🟡 Good to Know

A well-known set of practices for building cloud-friendly services (config in the environment, stateless processes, logs as event streams, and others) — worth knowing as a name and a reference checklist, even without memorising all twelve.

---

#### 9. Runbooks, On-Call, Incident Review — 🟡 Good to Know

A **runbook** documents how to respond to a known failure mode, so on-call response doesn't depend on one specific person's memory. Ties directly into `07-behavioral-leadership/8`'s incident-story guidance — the blameless review and follow-up actions are part of the operational architecture, not just a process nicety.

---

#### 10. Cloud Well-Architected Frameworks — 🟡 Good to Know

Major cloud providers publish their own structured review frameworks (names only) covering pillars like reliability, security, cost, and performance — useful as a checklist reference, provider-specific detail not required for most interviews.

---

#### 11. FinOps Basics — 🟡 Good to Know

Practices for managing and controlling cloud cost: **tagging** resources by team/feature for attribution, setting **budgets**, and tracking **cost per feature** — turning cost from an opaque monthly bill into something you can actually reason about and optimise.

---

#### 12. Common Interview Questions

1. **How do you design a system to be operable, not just functionally correct?**
   Build in observability (logs, metrics, traces) from the start, use infrastructure as code, keep environments cleanly separated, and design safe, automated release strategies — operability is an architectural decision, not an afterthought.
2. **How does cost factor into architecture decisions?**
   As a real constraint alongside other quality attributes — compare options explicitly on cost, right-size resources to actual need, and recognise that build-vs-buy and service choices all have direct cost implications.
3. **What's infrastructure as code, and why does it matter?**
   Defining servers and cloud resources in versioned files rather than manual console clicks — makes infrastructure changes reviewable, repeatable, and recoverable, the same benefits as version-controlling application code.
4. **What's a runbook, and why is it part of architecture?**
   Documented response steps for a known failure mode — it's part of the operational design of the system, ensuring incident response doesn't depend on one person's memory (`07-behavioral-leadership/8`).

---

#### 13. Common Mistakes

1. Treating observability as something to add after the first production incident.
2. Manually configured infrastructure with no version-controlled record of its actual state.
3. Ignoring cost until the bill is already a problem.
4. No runbooks, so incident response depends entirely on whoever happens to be on call knowing the system by memory.

---

#### 14. Related Topics

1. `SD 27`, `SD 28` — observability and deployment/release in full depth
2. `3` Trade-Offs & Decision Making — cost as one input into build-vs-buy decisions
3. `07-behavioral-leadership/8` — the incident-response and blameless-review side of operations

---

#### 15. Interview Must Remember

1. **Observability designed in from the start**, not bolted on after an incident.
2. **Infrastructure as code** — reviewable, repeatable, recoverable.
3. **Cost is a real architectural constraint**, not just a finance concern.
4. **Runbooks** make incident response independent of any one person's memory.
