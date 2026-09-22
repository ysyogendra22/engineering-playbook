# Practice: Case Studies & Exercises

Roadmap topic 22 · Stage 7: Interview & Practice

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** every topic in this folder is a tool. This topic is where you actually pick them up and use them — on real exercises, in a fixed order, until applying them feels natural instead of theoretical.

---

#### 1. Write Three ADRs — 🟢 Must Know

Pick **three real decisions** you made or could make (at work, or on a personal project — even the notes app from `BE 12`), and write a full ADR (`3`, item 2) for each: context, options, decision, consequences. This is the fastest way to turn topic `3` from theory into a habit.

---

#### 2. Draw C4 Diagrams for the Notes App — 🟢 Must Know

Using the Notes API from `BE 12`: draw a **System Context** diagram (the app, its users, the backend it talks to) and a **Containers** diagram (mobile app, API, database) — the two levels covered in `14`, item 1, applied to a system you already know well.

---

#### 3. List Top 5 Quality Attributes for Three Apps — 🟢 Must Know

Pick three different kinds of apps (for example: a banking app, a social feed, a note-taking app) and, for each, list the **top 5 quality attributes with numbers** (topic `2`) — this exercise makes clear how differently the same list of ten quality attributes gets ranked depending on the actual system.

---

#### 4. Compare Monolith, Modular Monolith, Microservices — 🟢 Must Know

For **one specific case** (pick a real or imagined product), compare all three (`5`, item 2) against its actual quality attributes and constraints, and give a **recommendation** with reasoning — not just a neutral comparison table.

---

#### 5. Threat-Model One Feature with STRIDE — 🟢 Must Know

Pick a real feature — login, or sharing a note with another user — and walk it through **STRIDE** (`11`, item 4): spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. Write down at least one real concern per category, even if some turn out to be low-risk on reflection.

---

#### 6. Review an App You Know — 🟡 Good to Know

Pick an app you actually work on or use deeply, and honestly assess: strengths, risks, and technical debt (`16`) — a real architecture review, not a hypothetical one, and often more revealing than a textbook exercise.

---

#### 7. Plan a Strangler-Fig Migration — 🟡 Good to Know

For a legacy screen or service you know (real or imagined), sketch a strangler-fig migration plan (`16`, item 4): what gets built first, how traffic shifts gradually, and what the final cutover and removal looks like.

---

#### 8. Design an AI Feature's Architecture — 🟡 Good to Know

Design both the mobile and backend architecture for one AI feature (`AI 22`, `20`) — a genuinely useful exercise for connecting this folder's Stage 6 topics (`19`, `20`) to the deeper `08-artificial-intelligence` and `06-mobile-engineering` material.

---

#### 9. Run a Mock Design Review — 🟡 Good to Know

Present one of your case-study designs to a friend or colleague as a real design review (`15`, item 4) — practising both giving and receiving review feedback, and handling pushback with data (`15`, item 5; `21`, item 9).

---

#### 10. Case Studies to Think Through — 🟢 Must Know

*Work through these fully, using the answer structure from `21`, item 1.*

1. 🟢 **Notes app with sync and offline support** — connects directly to `19` and `06-mobile-engineering`.
2. 🟢 **Chat app** — real-time delivery, message ordering, offline queuing.
3. 🟢 **Payments or checkout flow** — strong consistency requirements, idempotency, security.
4. 🟡 **A startup outgrowing its monolith** — a "when do we actually split" case study.
5. 🟡 **A migration from a legacy backend** — applies the strangler-fig planning from item 7.

---

#### 11. How to Practise Each Case Study — 🟢 Must Know

```text
1. Set a timer (30-45 minutes).
2. Clarify requirements and constraints first — don't skip this (topic 2).
3. Follow the structure from topic 21: quality attributes → options →
   decision → risks → evolution.
4. Draw the C4 diagrams as you go (topic 14).
5. Say your reasoning OUT LOUD, even alone — this is what interview
   practice actually needs.
6. Afterward, write one ADR for the key decision you made.
```

---

#### 12. Common Interview Questions

*This topic is the practice ground, not a new question category — but a few meta-questions do come up:*

1. **"Walk me through a system you designed recently."** — use one of your worked case studies (item 10), told with the structure from `21`.
2. **"What's a design you're not fully happy with, looking back?"** — a genuine answer from item 6's honest app review.

---

#### 13. Common Mistakes

1. Reading this whole folder without ever doing a single hands-on exercise.
2. Skipping the "say it out loud" step — silent practice doesn't build the same interview muscle.
3. Jumping to the hardest case studies before the easier ones (Notes app, item 1's simplest case) feel comfortable.
4. Never writing an actual ADR, treating topic `3` as theory only.

---

#### 14. Related Topics

1. `21` Architecture Interview Answers — the structure every exercise here should follow
2. `BE 12` Checkpoint Project: Notes API — the shared example system used across several exercises
3. `19`, `20` — the mobile and AI case studies this topic extends into

---

#### 15. Interview Must Remember

1. **Every topic in this folder is a tool — this topic is where you actually use them.**
2. **Write real ADRs and draw real C4 diagrams**, don't just read about them.
3. **Practise out loud, timed**, the same discipline as `07-behavioral-leadership/21`.
4. **Start with the Notes app and simpler case studies**, then build up to harder ones.
