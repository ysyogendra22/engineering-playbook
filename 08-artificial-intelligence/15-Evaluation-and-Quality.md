# Evaluation & Quality

Roadmap topic 15 · Stage 4: AI in Production

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** AI output changes from run to run, so "it looked fine when I tried it" is not a test. An evaluation (eval) is a set of real examples with a way to score the results. Run it every time you change the prompt, the model, or the tools, so you know if things got better or worse.

---

#### 1. Why Normal Tests Are Not Enough — 🟢 Must Know

*The output is not exactly the same each time, and "correct" is often a judgment.*

1. A unit test checks one exact output. An LLM can give many valid wordings.
2. A change that fixes one case can quietly break others.
3. You still write normal tests for your code (parsing, validation, tools). Evals cover the **AI behaviour**.
4. Without evals, you are changing prompts blind.

**Mobile view:** like UI tests and screenshot tests. Unit tests check the logic. Evals check the experience.

---

#### 2. Build an Eval Set — 🟢 Must Know

*Real examples with the expected result.*

1. Start with **20 to 50** real or realistic inputs. It does not need to be big to be useful.
2. For each, write what a **good result** looks like (an exact answer, key facts that must appear, a required format, or a rule that must hold).
3. Include **easy**, **typical**, and **hard** cases, plus **failures** you have already seen.
4. Include cases that must **refuse** or say "not found".
5. Keep it in the repo, and grow it: every bug becomes a new test case (topic `18`).

```text
Input:    "What did we decide about the release date?"
Expected: mentions "14th", cites note 31, does not invent other dates
```

---

#### 3. Regression Evals — 🟢 Must Know

*Re-run the same set after every change.*

1. Run the eval on every change to the **prompt**, the **model**, the **tools**, the **retrieval**, or the **settings**.
2. Compare with the previous score. Look at **which cases changed**, not only the average.
3. Do not ship a change that makes important cases worse.
4. Run a light version in CI, and the full version before release.

---

#### 4. What to Measure — 🟢 Must Know

*Pick a few things to score. Not everything needs a number.*

| Measure | Question |
|---|---|
| **Correctness** | Is the answer right? |
| **Groundedness** | Does it stick to the provided sources, with no invented facts? |
| **Format** | Is the output valid (JSON schema, length, language)? |
| **Task success** | Did the user's goal get done? |
| **Safety** | Did it refuse what it should refuse, and avoid leaking data? |
| **Cost and latency** | Tokens, time to first token, total time |

Score what you can with **code** (valid JSON, contains the key fact). Use judgment scoring (below) for the rest.

---

#### 5. Evaluating Agents — 🟢 Must Know

*Judge the whole run, not only the final answer.*

1. **Task success** — was the goal achieved?
2. **Trajectory** — the steps it took: right tools, sensible order, no repeated calls.
3. **Efficiency** — number of steps, tokens, time, cost.
4. **Safety** — no unapproved write, no data outside the user's permission.
5. Check the **end state** where you can (was the note actually created, with the right text?), not only what the agent said.
6. Run each case several times. Agents vary from run to run.

---

#### 6. LLM-as-Judge — 🟡 Good to Know

*Use a model to grade another model's output.*

1. Give the judge model the question, the answer, and clear **grading criteria** (a rubric), and ask for a score with a reason.
2. Good for things code cannot check: helpfulness, tone, whether an answer is grounded.
3. Limits: the judge can be biased (for example, favouring longer answers), inconsistent, or wrong.
4. **Check the judge against human ratings** on a sample before trusting it.
5. Prefer simple, specific criteria (yes or no) over a vague 1 to 10 score.

---

#### 7. User Feedback — 🟡 Good to Know

*Real users show what your eval set missed.*

1. **Thumbs up or down**, edits the user makes to the output, retries, and abandonment are all signals.
2. Log them with the prompt version and model (topic `18`).
3. Turn bad cases into new eval cases.
4. Feedback is noisy and biased to extremes. It complements evals; it does not replace them.

---

#### 8. A/B Testing Prompts and Models — 🟡 Good to Know

*Test a change on a share of real traffic.*

1. Send a share of real traffic to a new version and compare real outcomes (task success, retries, feedback, cost).
2. Use it **after** offline evals pass, not instead of them.
3. Roll out gradually with a feature flag (`SD 28`).

---

#### 9. Retrieval vs Answer Quality (RAG) — 🟡 Good to Know

*Test finding the text and using the text separately.*

1. Test **retrieval**: did the right chunk reach the model?
2. Test **generation**: given the right chunks, was the answer correct and grounded?
3. If retrieval fails, improving the prompt will not help (topic `07`).

---

#### 10. Public Benchmarks vs Your Own Evals — 🟡 Good to Know

*Use public scores to shortlist, and your own tests to decide.*

1. Benchmarks help shortlist models.
2. Your **own evals** decide, because they match your task, data, and users.
3. Public benchmarks can be outdated or over-fitted by model makers.

---

#### 11. Common Interview Questions

1. **How do you test an LLM feature?**
   Build an eval set of real examples with expected outcomes, score with code and, where needed, an LLM judge, and re-run on every change.
2. **What is a regression eval?**
   Re-running the same set after each change to check nothing got worse.
3. **How do you evaluate an agent?**
   Judge task success, the steps it took, efficiency, and safety, and check the end state. Run several times.
4. **What is LLM-as-judge and what are its limits?**
   A model grades outputs by a rubric. It can be biased or inconsistent, so validate it against human ratings.
5. **How do you measure hallucination?**
   Check groundedness: does each claim appear in the provided sources? Add "not found" cases.
6. **How do you know if a new model is better?**
   Run your eval set on both, compare per-case results, cost and latency, and roll out gradually.
7. **How do you collect real-world quality signals?**
   Thumbs, edits, retries, and abandonment, logged with the version, and turned into new eval cases.

---

#### 12. Common Mistakes

1. "It worked when I tried it" as the only testing.
2. An eval set of only easy cases.
3. Judging only the average, not which cases changed.
4. Trusting an LLM judge without checking it.
5. Judging an agent only by its final message.
6. Changing the prompt or the model without re-running evals.

---

#### 13. Related Topics

1. `01` AI Landscape & ML Basics (test data)
2. `04` Prompting & Context Engineering
3. `07` RAG
4. `10` Agents
5. `12` Building an Agent
6. `18` Observability & LLMOps
7. `BE 7` Testing & Debugging
8. `SD 28` Deployment & Release

---

#### 14. Interview Must Remember

1. **Evals** = real examples + a way to score them.
2. **Run them on every change.** Look at per-case differences.
3. **Measure:** correctness, groundedness, format, task success, safety, cost.
4. **Agents:** score the whole run and the end state.
5. **LLM judge:** useful, but verify it.
6. **Every production failure becomes a new eval case.**
