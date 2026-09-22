# Production Incidents

Roadmap topic 8 · Stage 2: Core Stories

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond your original ten topics

**In simple words:** an incident story is a failure story (topic `7`) at system scale, told in a very specific order: what happened, how you responded in real time, and — the part people forget — what changed afterward so it can't happen the same way again.

---

#### 1. Tell It in Order — 🟢 Must Know

*The expected shape, and deviating from it makes an incident story harder to follow.*

**Detect → assess → stop the harm → find the cause → fix → prevent.** Walking through these six steps in order shows a structured, calm response, rather than a chaotic one.

---

#### 2. Show Calm, Clear Communication — 🟢 Must Know

Who did you keep informed, and how, while the incident was live? A good incident response includes clear, honest status updates to stakeholders — panic or silence during an incident is its own kind of failure.

---

#### 3. Show Your Specific Role — 🟢 Must Know

What did **you** personally decide and do — not the team's response in general. If you led the response, say so plainly; if you played a supporting role, describe that role specifically and honestly.

---

#### 4. Separate the Quick Fix from the Real Root Cause — 🟢 Must Know

*A strong, specific signal of engineering maturity.*

The thing that stopped the immediate harm (a rollback, a feature flag disabled, a hotfix) is usually not the same as the underlying reason it happened in the first place. Naming both, distinctly, shows you understand the difference between mitigation and resolution.

---

#### 5. Show the Follow-Up — 🟢 Must Know

A **blameless postmortem** — a review that looks for causes in the systems and processes, not in a person to blame — with concrete **actions and owners** coming out of it. An incident with no real follow-up is a wasted lesson.

---

#### 6. Show the Impact — 🟢 Must Know

Users affected, duration, and cost (in time, money, or trust) — the scale of the incident is part of what makes the story worth telling, and it calibrates how impressive the response actually was.

---

#### 7. Mobile-Specific Incident Examples — 🟡 Good to Know

1. A **crash spike** after a release.
2. A **backend change that broke old app versions** (`MOB 1`, `SD 30`).
3. A **push notification failure** affecting delivery.
4. A **bad remote config** pushed to production.

---

#### 8. Mobile-Specific Constraints — 🟡 Good to Know

*Worth stating explicitly — it shows you understand what makes mobile incidents different from backend ones.*

**You cannot instantly roll back an app** the way you can a backend deploy. The real toolkit is: halting a staged rollout, disabling a feature via a remote flag, a server-side fix that compensates without a new release, or (as a last resort) an emergency hotfix release (`SD 28`, `MOB 15`).

---

#### 9. How You Improved Monitoring Afterward — 🟡 Good to Know

New alerts, dashboards, or tests added because of this incident (`SD 27`) — a concrete example of the "prevent" step from item 1, made specific.

---

#### 10. On-Call Experience — 🟡 Good to Know

If relevant, describe how you handled the stress and responsibility of being on-call — staying calm under a page at 3am, escalating appropriately when the problem was beyond your own expertise, and handing off cleanly.

---

#### 11. Common Interview Questions

1. **"Tell me about a production incident you handled."** — the direct prompt; use the six-step order from item 1.
2. **"How did you find the root cause?"** — item 4's distinction between the quick fix and the real cause.
3. **"What did you do to make sure it didn't happen again?"** — item 5 and item 9; have a concrete, specific answer, not a vague "we were more careful".
4. **"How would you handle an incident when you can't just roll back?"** — the mobile-specific answer from item 8; a strong, differentiating answer for a mobile role.

---

#### 12. Common Mistakes

1. Telling the story out of order, making it hard to follow.
2. Conflating the quick fix with the actual root cause.
3. No real follow-up — the postmortem step skipped entirely.
4. For a mobile incident, describing the response as if an instant rollback were possible.
5. No impact numbers (users affected, duration) to calibrate the story's scale.

---

#### 13. Related Topics

1. `7` Failure Stories & Learning — the personal-scale version of this story shape
2. `SD 27` Observability, `SD 28` Deployment & Release — the technical practices this story demonstrates
3. `MOB 15` Build, Release & Monitoring — the mobile-specific release-safety toolkit referenced in item 8

---

#### 14. Interview Must Remember

1. **Detect → assess → stop the harm → find the cause → fix → prevent** — tell it in this order.
2. **Separate the quick fix from the real root cause** — a strong, specific signal.
3. **Blameless postmortem with real actions and owners**, not just a fix and move on.
4. **Mobile constraint**: no instant rollback — know the real toolkit (flag, staged rollout halt, server-side fix, hotfix).
