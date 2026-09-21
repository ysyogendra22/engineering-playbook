# Cost, Latency & Reliability

Roadmap topic 17 · Stage 4: AI in Production

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** LLM calls are slower and more expensive than normal API calls, and they can fail. Tokens drive both cost and speed. Keep prompts small, stream the answer, cache what repeats, use the smallest model that works, and always have a plan for when the provider is slow or down.

---

#### 1. Tokens Drive Cost and Latency — 🟢 Must Know

*More tokens means more money and more waiting.*

1. You pay for **input tokens** (everything you send) and **output tokens** (what the model writes). Output tokens usually cost more.
2. Latency grows with output length: the model writes one token at a time (topic `02`).
3. Common causes of high cost: long system prompts, huge histories, big retrieved chunks, long tool outputs, and agent loops with many steps.
4. **Estimate before building:** requests per day × tokens per request × price per token.

```text
Example: 10,000 chats/day × (2,000 input + 400 output tokens) = 24M tokens/day.
Change the average by 500 tokens and the bill moves noticeably.
```

---

#### 2. Time to First Token vs Total Time — 🟢 Must Know

*The user feels the wait for the first word.*

1. **TTFT (time to first token)** — how long until the answer starts appearing.
2. **Total time** — until the answer is finished.
3. **Streaming** improves perceived speed: the user reads while it writes (topic `05`).
4. For agents, total time also includes every tool call and every extra model call.
5. Show progress for long tasks: "Searching notes…", "Reading note 31…".

---

#### 3. Caching — 🟢 Must Know

*Do not pay twice for the same work.*

1. **Response cache** — same (or very similar) question, same data, same answer. Store it (`SD 15`). Careful with personal data: include the user in the key.
2. **Prompt caching** — the provider reuses the unchanged start of your prompt (topic `05`). Put stable content first.
3. **Tool and retrieval caches** — cache search results or fetched pages that do not change often.
4. Set a **TTL** and think about stale answers, as with any cache.

---

#### 4. Timeouts, Retries, Fallbacks — 🟢 Must Know

*Assume the provider will be slow or fail sometimes (`SD 22`, `SD 25`).*

1. **Timeouts** on every call. Streaming helps with long answers.
2. **Retry** transient errors (`429`, `5xx`, timeouts) with **backoff and jitter**. Not `400`-style errors.
3. **Fallbacks:**
   - a second model (or provider),
   - a cached or simpler answer,
   - a clear error message with a retry option.
4. **Circuit breaker** — after repeated failures, stop calling for a moment (`SD 25`).
5. **Degrade gracefully:** if AI is unavailable, the rest of the app should still work.

---

#### 5. Queue Non-Urgent Work — 🟢 Must Know

*If the user is not waiting, it does not belong in the request.*

1. Anything the user is **not waiting on** goes to a queue (`SD 21`): tagging notes, summarizing yesterday's meetings, re-embedding documents.
2. Workers process at a controlled rate, so you do not hit rate limits.
3. Use **batch APIs** for large offline jobs (topic `05`).
4. Long agent runs: return "started", then notify when done (`SD 24`).

---

#### 6. Reduce Tokens and Use Smaller Models — 🟡 Good to Know

*Send fewer tokens and use a model that fits the task.*

1. **Shorter prompts:** cut repeated or unused instructions.
2. **Send less context:** retrieve fewer, better chunks. Summarize history (topic `13`).
3. **Cap output length** with `max_tokens`. Ask for concise answers.
4. **Model routing:** small model for easy tasks, large model for hard ones (topic `05`).
5. Always check quality after cutting (topic `15`).

---

#### 7. Budgets — 🟡 Good to Know

*Limits that stop a bug or an attacker from running up the bill.*

1. **Per-user limits** and quotas (daily or monthly) enforced on the server.
2. **Per-run limits** for agents: max steps, max tokens, max cost.
3. **Cost alerts** and a global spending cap, so a bug or an attack cannot produce a surprise bill.
4. Track **cost per user and per feature** (topic `18`).

---

#### 8. Batch Processing — 🟡 Good to Know

*Cheaper processing for work that can wait.*

1. For offline work, batch many requests together and accept results later, usually at a lower price.
2. Good for: overnight labelling, backfilling summaries, evaluations.
3. Not for interactive features.

---

#### 9. Provider Outages — 🟡 Good to Know

*Plan for the provider being slow, limited, or down.*

1. Providers have limits and outages. Do not tie the whole product to one call.
2. Options: a second provider or model behind the same interface, queued retries, or a degraded mode.
3. Keep your **prompts and evals portable**, so switching is possible (topic `15`). Test the fallback model too. It will behave differently.

---

#### 10. Common Interview Questions

1. **What drives the cost of an LLM feature?**
   Input and output tokens: prompt size, history, retrieved context, tool results, and number of agent steps.
2. **How would you reduce latency?**
   Stream, shorten prompts and outputs, cache, use a smaller model, and run independent calls in parallel.
3. **How would you reduce cost?**
   Cache, prompt caching, shorter context, model routing, batch APIs for offline work, and limits per user.
4. **What if the LLM provider is down?**
   Timeouts, retries with backoff, a fallback model or cached answer, and a graceful message. The rest of the app keeps working.
5. **How do you prevent a surprise bill?**
   Per-user quotas, per-run agent limits, rate limits, cost alerts, and a global cap.
6. **What goes into a queue and what stays synchronous?**
   Synchronous only what the user is waiting on. Everything else goes to a queue.
7. **What is time to first token?**
   How long until the first part of the answer appears. Streaming keeps it low.

---

#### 11. Common Mistakes

1. No cost estimate before launch.
2. Sending the full history and full documents every time.
3. No timeout, no fallback.
4. No cap on `max_tokens` or on agent steps.
5. Using the largest model for everything.
6. Caching personal answers with a shared key.
7. No per-user limit, so one user can burn the budget.

---

#### 12. Related Topics

1. `02` How LLMs Work
2. `05` Calling an LLM API
3. `13` Memory & Context Management
4. `15` Evaluation & Quality
5. `18` Observability & LLMOps
6. `SD 15` Caching
7. `SD 21` Queues, Events & Background Jobs
8. `SD 22` Reliable Requests & External Services
9. `SD 25` Overload & Failure Handling

---

#### 13. Interview Must Remember

1. **Tokens = cost + latency.** Estimate them.
2. **Stream** to lower perceived wait. Watch **TTFT**.
3. **Cache:** responses, prompt prefix, tool results.
4. **Timeout, retry with backoff, fallback,** degrade gracefully.
5. **Queue** what the user is not waiting for.
6. **Budgets:** per user, per run, global alerts.
