# Technical Decisions

Roadmap topic 5 · Stage 2: Core Stories

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond your original ten topics

**In simple words:** interviewers don't want to hear "we chose Kotlin coroutines" — they want to hear how you got there: what you compared it against, what evidence you gathered, and what you gave up by choosing it. The decision itself matters less than the reasoning behind it.

---

#### 1. Tell the Full Story of the Decision — 🟢 Must Know

The complete shape: the **problem** that forced a decision, the **options** you genuinely considered, **how you compared them**, the **choice**, and the **outcome**. Skipping straight from "problem" to "choice" leaves out the part that actually demonstrates judgment.

---

#### 2. Show the Criteria — 🟢 Must Know

Name what you actually weighed: **cost, risk, time, team skills, maintainability, user impact**. Different decisions weigh these differently — say which mattered most here, and why, rather than listing all six generically.

---

#### 3. Show How You Got Evidence — 🟢 Must Know

A prototype, a benchmark, a small spike, or real usage data — something beyond "it felt right". Concrete evidence is what separates an engineering decision from a guess, and it's exactly what an interviewer is listening for.

---

#### 4. Show How You Brought Others Along — 🟢 Must Know

Most real decisions aren't made alone — describe how you got buy-in, handled disagreement (topic `9`), and communicated the trade-off to people who'd be affected by it (topic `11`).

---

#### 5. Be Ready for "What If You Had Chosen the Other Option?" — 🟢 Must Know

This near-universal follow-up tests whether you actually understood the alternative, or just picked the option you already liked. Have a genuine, fair answer: what would have gone better, what would have gone worse, with the road not taken.

---

#### 6. A Decision You Reversed — 🟡 Good to Know

A story where you later realised the original choice was wrong, and had the judgment (and courage) to change course — this is a strong, underused story type, since it shows both honesty and adaptability rather than stubbornness.

---

#### 7. A Decision Made with Little Information — 🟡 Good to Know

Describe how you **reduced the risk** of deciding under uncertainty: a small reversible first step, a time-boxed experiment, or explicitly flagging the decision as provisional and revisiting it later.

---

#### 8. Recording the Decision — 🟡 Good to Know

Mention if you wrote it down — an ADR or a short design doc (`ARCH 3`, `ARCH 14`) — this shows a habit of leaving a trail others can follow and revisit, not just deciding in your head.

---

#### 9. Build vs Buy, Library, and Framework Choices — 🟡 Good to Know

A common, concrete flavour of this story: choosing (or rejecting) a third-party library, framework, or service — good territory because the trade-offs (control vs speed, cost vs effort) are usually very explicit and easy to narrate clearly.

---

#### 10. Common Interview Questions

1. **"Tell me about a technical decision you're proud of."** — the direct prompt; use the full structure from item 1.
2. **"How do you decide between two reasonable options?"** — focus on item 2 (criteria) and item 3 (evidence).
3. **"What would you have done if you'd chosen the other approach?"** — have this ready in advance (item 5); don't improvise it for the first time in the room.
4. **"Tell me about a time you changed your mind about a technical decision."** — the reversal story (item 6); a strong, distinct answer if you have one.
5. **"How do you decide when you don't have much information?"** — the item 7 answer: reduce risk with a small, reversible step.

---

#### 11. Common Mistakes

1. Naming the chosen technology without explaining the comparison that led there.
2. No real evidence — the decision sounds like a preference, not an analysis.
3. Being unable to fairly describe the road not taken when asked.
4. Only ever telling "and it worked out great" stories, with no reversal or lesson-learned example ready.

---

#### 12. Related Topics

1. `6` Architecture Decisions — the larger-scale version of this same story type
2. `9` Conflict Resolution & Disagreement — handling pushback on a decision
3. `ARCH 3` Trade-Offs & Decision Making — the technical framework this story-telling maps onto

---

#### 13. Interview Must Remember

1. **Problem → real options compared → evidence → choice → outcome** — the full shape, not just the ending.
2. **Name the criteria** you actually weighed, not a generic list.
3. **Always be ready for "what if the other option?"** — prepare it in advance.
4. A **reversed decision** is a strong, distinct story worth having ready.
