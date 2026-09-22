# The STAR Method

Roadmap topic 2 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond your original ten topics

**In simple words:** STAR is a shape for a story, not a script to recite. Get the shape right — short setup, long action, a real result — and any story you tell will land clearly, under pressure, without rambling.

---

#### 1. Situation — 🟢 Must Know

*The context, in one or two sentences. Resist the urge to over-explain here.*

State only what's needed to understand the stakes: the team, the product, the constraint. "I was the lead mobile engineer on a checkout flow with a 40% drop-off rate" is enough — no need for company history or unrelated background.

---

#### 2. Task — 🟢 Must Know

Your specific goal or responsibility in that situation — what were *you* meant to achieve or solve, distinct from what the team as a whole was doing.

---

#### 3. Action — 🟢 Must Know

*The longest part of the answer, by far. This is where the actual signal lives.*

1. What **you** specifically did, step by step — not "we decided", but "I proposed", "I built", "I convinced".
2. Include the reasoning behind key choices, not just the actions themselves — this is what shows judgment (`01`).
3. If others were involved, be clear about your role versus theirs.

---

#### 4. Result — 🟢 Must Know

*The outcome, with numbers wherever you can get them.*

"It went well" says nothing. "Checkout completion rose from 60% to 78% over the next month" is evidence. If the number isn't perfectly precise, a reasonable estimate stated as such is still far stronger than no number at all.

---

#### 5. Add a Lesson — 🟢 Must Know

*STAR plus learning — the extra step that turns a report into a reflection.*

One line: what you learned, or what you'd do differently next time. This shows self-awareness (item `16`) and gives you a natural, honest answer to the near-universal follow-up: "what would you change?"

---

#### 6. "I" for Actions, "We" for Team Context — 🟢 Must Know

Use "we" to set the scene (the team's situation), but switch to "I" the moment you describe what *you* did. An answer that's all "we" leaves the interviewer unable to tell what your actual contribution was — this is the single most common fixable weakness in a first-draft story.

---

#### 7. Timing — 🟢 Must Know

Aim for **about two minutes**. Keep the Situation and Task short (a few sentences each); let the Action section carry most of the time. A five-minute answer usually means the setup ran too long.

---

#### 8. Quantify the Result — 🟢 Must Know

*Numbers make a claim checkable, and checkable claims are more convincing.*

Time saved, crash-free rate, users affected, revenue, cost, quality metrics, team size, timeline — any concrete number strengthens the Result section. If you genuinely don't have one, say what you'd estimate and why, rather than skipping it.

---

#### 9. Worked Example (Template) — 🟢 Must Know

```text
Situation: Our app's cold start time had grown to 3.5 seconds, and support
           tickets about "the app feels slow" were increasing.

Task:      As the engineer who owned app performance, I needed to bring
           startup time down without a major architecture rewrite.

Action:    I profiled cold start with the Android Studio Profiler and found
           the dependency-injection graph was initializing eagerly in the
           Application class. I proposed lazy-initializing non-critical
           dependencies, built a proof of concept, measured the improvement,
           and presented it to the team with before/after numbers before
           rolling it out behind a feature flag.

Result:    Cold start dropped from 3.5s to 1.8s. Slow-start-related support
           tickets fell by about 60% over the next release cycle.

Lesson:    I learned to profile before optimising — my first instinct was to
           guess at a different bottleneck, and the data pointed somewhere
           I hadn't expected.
```

---

#### 10. Variations: CAR and SOAR — 🟡 Good to Know

1. **CAR** (Context, Action, Result) — a shorter version, useful for the 30-second answer (topic `3`).
2. **SOAR** (Situation, Obstacle, Action, Result) — adds an explicit obstacle, useful when the challenge itself is the interesting part of the story.

Both are the same underlying shape as STAR — use whichever framing fits the specific story best.

---

#### 11. Adapt One Story to Different Questions — 🟡 Good to Know

The same real event can answer several different competency questions (`00-Content.md`'s Question Bank), just by changing which part you emphasise — the same checkout redesign story can highlight technical judgment, or cross-team collaboration, or handling ambiguity, depending on which part of the Action section you expand.

---

#### 12. Common Mistakes to Avoid — 🟡 Good to Know

1. Too much background, not enough action.
2. Vague action ("I worked on it", "I helped") instead of specific steps.
3. No result, or a result with no number.
4. Rambling past the two-minute mark.

---

#### 13. Recovering When You Lose the Thread — 🟡 Good to Know

If you lose track mid-answer, **pause and restate**: "Let me back up — the key decision was X" is a clean recovery. Silence and stumbling is far less costly than it feels in the moment; a brief pause reads as thoughtful, not weak.

---

#### 14. Common Interview Questions

1. **"Can you walk me through that using a clear structure?"** — a direct invitation to use STAR; take it.
2. **"What was your specific role in that?"** — the standard probe for "we"-heavy answers; have the "I" version ready.
3. **"What was the outcome?"** — always have a number ready, even an estimated one.

---

#### 15. Common Mistakes

1. Reciting STAR mechanically instead of telling a natural story that happens to follow its shape.
2. An Action section that's shorter than the Situation section.
3. No quantified result.
4. Forgetting the lesson, and getting caught flat-footed by "what would you do differently?"

---

#### 16. Related Topics

1. `1` How Behavioral Interviews Work — why this structure works with how interviews are scored
2. `3` Building Your Story Bank — turning real events into STAR-shaped stories, in advance
3. `21` Mock Interviews & Practice Plan — where you practise timing this out loud

---

#### 17. Interview Must Remember

1. **Situation and Task: short. Action: long. Result: with a number.**
2. **Switch to "I" for your own actions** — this is the most common fix a first-draft story needs.
3. **Add a one-line lesson** — it answers "what would you change?" before it's even asked.
4. **About two minutes** — practise the timing, not just the content.
