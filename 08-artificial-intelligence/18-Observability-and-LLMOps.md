# Observability & LLMOps

Roadmap topic 18 · Stage 4: AI in Production

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** when an AI feature gives a bad answer, you must be able to see exactly what went in, what the model did, and what each tool returned. LLMOps means running AI features safely in production: logging, tracing, versioning prompts and models, and re-testing before every upgrade.

---

#### 1. Log Every Model Call — 🟢 Must Know

*If you did not log it, you cannot debug it.*

For each call, record:

1. **Prompt version** and **model name/version**.
2. **Input and output tokens**, and cost.
3. **Latency** (time to first token and total).
4. **Stop reason** and **errors**.
5. **User or session ID**, and a **request ID** (`SD 27`) so a report from the app can be found in the logs.
6. The prompt and the response text, **if you may store them**.

**Careful:** prompts and responses often contain personal data. Redact, limit access, and set retention (topic `16`).

---

#### 2. Tracing Agent Runs — 🟢 Must Know

*See every step of a run, in order.*

1. A **trace** is the full record of one run: each model call, each tool call with arguments and results, timings, and costs.
2. Without it, "the agent gave a weird answer" is a mystery. With it, you see: it called the wrong tool at step 3.
3. Use one **trace ID** across model calls, tool calls, and your backend logs.
4. Tracing is what makes agents debuggable, and it feeds your evals (topic `15`).

```text
Run 8f2c  (4 steps, 3.1 s, $0.012)
 1  model   420 in / 40 out   0.8 s   → tool: search_notes
 2  tool    search_notes("release date")   0.1 s   → 2 results
 3  model   900 in / 60 out   0.9 s   → tool: get_note(31)
 4  model   1,300 in / 90 out 1.2 s   → final answer
```

---

#### 3. Version Prompts, Models, and Tools — 🟢 Must Know

*A behaviour change needs a name and a date.*

1. Keep prompts, tool definitions, and settings **in source control** (topic `04`).
2. Give each a **version**, and record it in the logs.
3. When quality changes, you can tell what changed: prompt v12, model update, or a new tool.
4. Pin a **specific model version** where the provider allows it, instead of a moving "latest".

---

#### 4. Model Upgrades — 🟢 Must Know

*Models get updated and retired. Every switch is a change to your product.*

1. Providers **retire old models** on a schedule. Plan for it.
2. A new model can behave differently: tone, format, refusals, tool use.
3. Before switching: **re-run your evals** (topic `15`) and compare cost and latency.
4. Roll out **gradually** with a feature flag and watch the metrics (`SD 28`).
5. Keep the ability to **roll back**.

---

#### 5. Dashboards and Alerts — 🟡 Good to Know

*Same as normal services (`SD 27`), plus AI-specific numbers.*

1. **Standard:** request rate, error rate, latency (p50, p95, p99).
2. **AI-specific:** tokens per request, **cost per user and per feature**, time to first token, agent steps per run, tool error rate, refusal rate.
3. **Quality signals:** thumbs down rate, retry rate, escalations to a human.
4. **Alert on symptoms:** error spike, latency spike, cost spike, sudden quality drop.

---

#### 6. The Feedback Loop — 🟡 Good to Know

*Production failures make the next version better.*

```text
Production → traces + user feedback → find failures
          → add them to the eval set → fix prompt/tools → run evals → release
```

1. Sample real traces regularly and read them. You will find problems no dashboard shows.
2. Every failure becomes a new eval case (topic `15`).
3. Review before you store: apply privacy rules to anything you save for evals.

---

#### 7. Gradual Rollout and Feature Flags — 🟡 Good to Know

*Release AI changes to a few users first, and keep an off switch.*

1. Release AI changes to a **small percentage** first (`SD 28`).
2. Use a **feature flag** to turn an AI feature off quickly, without an app release.
3. On mobile, a server-side flag is especially useful, because you cannot force users to update.
4. Compare the new version with the old one on real metrics, then increase the percentage.

---

#### 8. Common Interview Questions

1. **The AI gave a wrong answer. How do you investigate?**
   Find the trace: the prompt version, the input, the retrieved context, each tool call, and the output. Then reproduce it, and add it to the eval set.
2. **What do you log for LLM calls?**
   Prompt and model versions, token counts, latency, stop reason, errors, and user and request IDs, with personal data protected.
3. **What is tracing and why do agents need it?**
   A step-by-step record of a run. Without it you cannot see which step went wrong.
4. **How do you handle a model upgrade?**
   Re-run evals, compare quality, cost and latency, roll out gradually, and keep a rollback.
5. **What do you monitor in production?**
   Errors, latency, tokens and cost per feature, agent steps, tool errors, and quality signals.
6. **How do you manage prompt changes?**
   Store in source control, version, test with evals, and release with a flag.
7. **What is LLMOps?**
   The practices for running LLM features in production: logging, tracing, versioning, evaluation, rollout, and cost control.

---

#### 9. Common Mistakes

1. Not logging prompts and versions, so bugs cannot be reproduced.
2. Logging personal data with no protection or retention limit.
3. No tracing for agents.
4. Using a moving "latest" model and being surprised by changes.
5. Switching models without re-running evals.
6. Watching only error rate, not cost and quality.

---

#### 10. Related Topics

1. `04` Prompting & Context Engineering
2. `10` Agents
3. `15` Evaluation & Quality
4. `16` Safety, Security & Privacy
5. `17` Cost, Latency & Reliability
6. `SD 27` Observability
7. `SD 28` Deployment & Release

---

#### 11. Interview Must Remember

1. **Log:** prompt version, model, tokens, latency, errors. Protect personal data.
2. **Trace** every agent step: model calls and tool calls.
3. **Version** prompts, tools, and models. Pin model versions.
4. **Upgrade:** re-run evals, roll out gradually, keep rollback.
5. **Monitor** cost per feature and quality, not only errors.
6. **Failures feed the eval set.**
