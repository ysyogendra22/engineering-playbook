# AI Interview Answer Points

Roadmap topic 21 · Stage 6: Interview

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** AI questions in interviews are still system design questions. Use the same steps, then show that you know the AI-specific problems: wrong answers, cost, speed, privacy, safety, and how you would test it. Do not start with the model. Start with the user problem.

---

#### 1. Start With the Problem, Not the Model — 🟢 Must Know (New)

*Ask whether AI is even needed.*

1. Clarify the **user problem** and what a good result looks like.
2. Ask: could a **rule, a search, or a database query** do it? Simple is faster, cheaper, and more predictable.
3. If AI helps, ask what happens when it is **wrong**. Low-stakes (a suggestion) or high-stakes (money, health)?
4. State the **constraints**: scale, latency, privacy, cost, platforms, offline needs.

---

#### 2. The Standard Concerns — 🟢 Must Know (New)

*Cover these for any AI feature. Say them without being asked.*

| Concern | What to say |
|---|---|
| **Hallucination** | Ground answers with RAG, cite sources, allow "not found", validate output |
| **Cost** | Estimate tokens, cache, smaller models, limits per user |
| **Latency** | Stream, cache, shorter prompts, model routing |
| **Privacy** | Send the minimum, per-user data, provider policy, delete on request |
| **Safety** | Prompt injection, least privilege, human approval for risky actions |
| **Quality** | An eval set, regression tests, feedback, monitoring |
| **Reliability** | Timeouts, retries, fallbacks, graceful degradation |

---

#### 3. Ready Answers to Common Questions — 🟢 Must Know (New)

*Short answers you can extend.*

1. **How do you reduce hallucination?**
   Give the model the facts (RAG), tell it to answer only from them and to say "not found", cite sources, use tools for facts and math, validate the output, and keep temperature low.
2. **How do you control cost?**
   Count tokens, cache, shorten context, route easy tasks to a small model, batch offline work, and set per-user and per-run limits.
3. **How do you test an AI feature?**
   Build an eval set of real cases, score with code and a checked LLM judge, re-run on every change, and turn production failures into new cases.
4. **How do you stop prompt injection?**
   You cannot fully prevent it. Limit damage: least privilege, read-only where possible, human approval for risky actions, and validate output.
5. **RAG or fine-tuning?**
   RAG for facts and changing or private data. Fine-tuning for style, format, or a narrow skill.
6. **Workflow or agent?**
   Workflow when the steps are known. Agent only when the steps cannot be known ahead. Start with the simplest.
7. **One agent or many?**
   One, unless the context is too large, subtasks are independent, or parts need different permissions.
8. **On-device or cloud?**
   On-device for privacy, offline, and simple tasks. Cloud for strong reasoning. Often hybrid.

---

#### 4. Fit AI Into the Normal Design Steps — 🟢 Must Know

*Use the system design structure (`SD 31`).*

```text
1. Clarify        → user problem, is AI needed, stakes, scale, constraints
2. Estimate       → requests/day, tokens per request, cost, latency target
3. API + data     → endpoints, conversation and document storage, vector index
4. High-level     → app → backend → (retrieval, tools, model) → answer
5. Flows          → one chat request; one indexing job; one agent run
6. Deep dive      → hallucination, injection, cost, or agent reliability
7. Trade-offs     → quality vs cost, autonomy vs control, on-device vs cloud
```

Typical AI building blocks to draw: **API gateway/backend, model call, retrieval (vector index), tools, cache, queue and workers, storage, monitoring.**

---

#### 5. Explain Each Term in 30 Seconds — 🟡 Good to Know

*Practise saying these out loud.*

1. **LLM** — a model trained on lots of text that predicts the next token.
2. **RAG** — search your documents at question time and give the results to the model.
3. **Tool use** — the model asks your code to run a function, and gets the result.
4. **MCP** — an open standard for connecting AI apps to tools and data.
5. **Agent** — a model with tools and a loop that works toward a goal.
6. **Harness** — the code around the model that runs the loop, tools, context, and permissions.

---

#### 6. Say What You Would Build First — 🟡 Good to Know

*Show that you can start small and measure.*

1. Propose a **small first version**: one use case, read-only, a handful of tools or a simple RAG.
2. Say how you would **measure success**: task success rate, thumbs up rate, cost per request, latency, escalations.
3. Say how it **grows**: more sources, more tools, more autonomy, only as evals justify.

---

#### 7. Common Trade-Offs — 🟡 Good to Know

*Every AI design choice gives up something.*

| Trade-off | Think about |
|---|---|
| Quality vs cost | Bigger model or more context helps, but costs more |
| Quality vs latency | Reasoning and reflection improve answers but take time |
| Autonomy vs control | More autonomy is faster and riskier |
| On-device vs cloud | Privacy and offline vs strength and easy updates |
| RAG vs fine-tuning | Fresh facts and citations vs style and speed |
| One agent vs many | Simplicity vs parallelism and separation |

---

#### 8. Common Interview Questions

1. **Design a customer-support chatbot.**
   RAG over help articles, cited answers, escalation to a human when confidence is low, per-user context, evals, and cost limits. (topic `22`)
2. **Design "chat with your documents".**
   Ingestion pipeline (chunk, embed, index), per-user filters, retrieval with hybrid search and reranking, grounded answers with citations.
3. **Design an AI writing assistant in a mobile app.**
   App to backend to model, streaming UI, cancel and retry, quotas, privacy, and a fallback when offline.
4. **Design a coding or task-running agent.**
   Harness with tools, permissions, sandbox, context management, limits, human approval, tracing, and evals.
5. **What are the risks of putting an LLM in a product?**
   Hallucination, injection, data leakage, cost, latency, and provider outages. Then the mitigations.
6. **How do you decide if a feature should use AI?**
   Check if a simpler solution works, what a wrong answer costs, and whether the value justifies the cost and risk.
7. **How would you improve a feature that gives poor answers?**
   Look at traces, find whether retrieval, prompt, tools, or model is at fault, fix in that order, and re-run evals.

---

#### 9. Common Mistakes

1. Starting with "I will use GPT/Claude" before understanding the problem.
2. Never asking whether AI is needed.
3. Ignoring hallucination, cost, and safety until asked.
4. Jumping to agents or multi-agent designs for simple tasks.
5. No plan to measure quality.
6. Forgetting the mobile side: streaming, offline, states, key security.

---

#### 10. Related Topics

1. `07` RAG
2. `10` Agents
3. `15` Evaluation & Quality
4. `16` Safety, Security & Privacy
5. `17` Cost, Latency & Reliability
6. `20` AI Features in the App
7. `22` Practice: Projects & Designs
8. `SD 31` Interview Answer Structure

---

#### 11. Interview Must Remember

1. **Problem first.** Ask if AI is needed.
2. **Always cover:** hallucination, cost, latency, privacy, safety, quality, reliability.
3. **Use the normal design steps,** with AI building blocks.
4. **Simplest first:** prompt → RAG → workflow → agent.
5. **Say how you would test and measure it.**
6. **Include the mobile side** of the design.
