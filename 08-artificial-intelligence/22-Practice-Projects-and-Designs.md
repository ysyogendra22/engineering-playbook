# Practice: Projects & Designs

Roadmap topic 22 · Stage 6: Interview

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** reading is not enough. Build a few small AI projects in order, and practise designs on paper. Each project uses ideas from specific topics, so build it right after you learn them.

---

#### 1. Build These Projects (in order) — 🟢 Must Know

*Small projects. Each one teaches a piece you will be asked about.*

| # | Project | Practises | Build after topic |
|---|---|---|---|
| 1 | **Streaming chat** | Your backend calls an LLM API; the app shows tokens as they arrive; cancel and retry; key on the server | `05` |
| 2 | **Structured extraction** | Text in, validated JSON out; retry on invalid output; a small eval | `05` |
| 3 | **Ask your notes** | RAG over the Notes API data (`BE 12`): chunk, embed, retrieve, cite; per-user filter | `07` |
| 4 | **Tool-using assistant** | Two or three tools and an agent loop you write yourself; step limit; approval for writes | `12` |
| 5 | **Mini harness** (🟡) | Grow project 4: hooks, a sandboxed tool, saved sessions, context compaction | `13` |
| 6 | **Eval set** (🟡) | 20 to 30 cases, a script that scores them, re-run after each change | `15` |
| 7 | **On-device feature** (🟡) | Text classification or image labelling on the phone, with a cloud fallback | `19` |

Tips:

1. Keep each project **small and finished**. A working small project beats a big half-built one.
2. Add **logging and token counting** from the start (topic `18`).
3. Write down **one thing that surprised you** in each project. That is a good interview story.

---

#### 2. How to Practise a Design — 🟢 Must Know

*A simple routine for every design you practise.*

For each design:

1. Set a **timer** (45 minutes).
2. Follow the steps in topic `21` and `SD 31`.
3. Write: requirements (and is AI needed?), estimate (requests, tokens, cost), APIs and data, a diagram, one deep dive.
4. Cover the standard concerns: hallucination, cost, latency, privacy, safety, quality, reliability.
5. Say it **out loud**, then read your notes and find the gaps.
6. Add the **mobile side**: streaming, states, offline, keys, approvals.

---

#### 3. Designs (in order) — 🟢 Must Know

*The main designs, in the order to do them.*

| # | Design | Focus on | Topics |
|---|---|---|---|
| 1 | **Customer-support chatbot** | RAG over help content, citations, escalation to a human, feedback | `06`, `07`, `15` |
| 2 | **Chat with your documents** | Ingestion pipeline, chunking, per-user access, freshness, deletes | `06`, `07`, `16` |
| 3 | **AI writing or summarizing feature in an app** | Streaming, cost and quotas, privacy, offline and error states | `05`, `17`, `20` |
| 4 | **Semantic search** | Embeddings, hybrid search, reranking, relevance evaluation | `06`, `07`, `15` |
| 5 | **Coding or task-running agent** | Harness, tools, permissions, sandbox, context limits, approvals, tracing | `08`, `10`, `11`, `13`, `16`, `18` |

Deep-dive ideas for each: hallucination (1), stale or deleted documents (2), cost per user (3), search quality metrics (4), an unsafe action or injection (5).

---

#### 4. Harder or Specialised Designs — 🟡 Good to Know

*Extra designs for when the main ones feel easy.*

| Design | Focus on | Needs |
|---|---|---|
| **Content moderation pipeline** | Classifier plus LLM, human review queue, false positives and negatives | `01`, `16`, `SD 21` |
| **Recommendation system** | Embeddings, candidate retrieval then ranking, cold start | `01`, `06` |
| **Voice assistant** | Speech-to-text, LLM, text-to-speech, latency budget, on-device parts | `05`, `17`, `19` |
| **Multi-agent research assistant** | Orchestrator and workers, parallel runs, cost, merging results | `10`, `14`, `17` |
| **On-device photo or text feature** | Small model, download and versioning, battery, fallback | `19`, `20` |

---

#### 5. Sample Design Outline: Ask Your Notes — 🟢 Must Know

*What a good 45-minute answer covers.*

```text
1. Clarify     Users search and ask questions about their own notes. Is AI needed?
               Yes for natural questions; also keep plain keyword search.
2. Estimate    100k users × 5 questions/day × ~2,500 tokens = about 1.25B tokens/day
               → cost matters: cache, limit, small model for easy questions
3. API/data    POST /ask (streaming), notes table, chunks + vectors with user_id
4. Design      App → backend → retrieve (filter by user) → prompt → model → stream
               Notes change → queue → worker re-embeds the note
5. Flows       Ask flow; indexing flow; delete flow (remove vectors)
6. Deep dive   Hallucination: ground, cite, allow "not found"
               Privacy: per-user filter, redact, provider policy
7. Trade-offs  RAG vs long context; hybrid search cost; on-device for offline
```

Mobile side: streaming UI, cancel, offline state, quota display, no key in the app.

---

#### 6. Order of Learning — 🟢 Must Know

*When to build, learn, and practise, step by step.*

1. Finish the Notes API (`BE 12`) first, so you have data to work with.
2. Learn topics `1` and `2`, then `4` and `5`. Build **streaming chat** and **structured extraction**.
3. Learn `6` and `7`. Build **ask your notes**.
4. Learn `8` to `12`. Build the **tool-using assistant** and write your own agent loop.
5. Learn `15` to `18`. Add evals, tracing, and limits to your projects.
6. Learn `19` and `20`. Add the mobile parts and one on-device feature.
7. Start design practice after topic `7`, and add the harder designs as you learn their topics. Do not wait to finish all the theory.
8. Learn `21` last, then run full mock designs out loud.

---

#### 7. Common Interview Questions

1. **What AI project have you built and what did you learn?**
   Pick your streaming chat or ask-your-notes project. Explain the design, one problem (hallucination, cost, latency), and how you fixed it.
2. **How did you test it?**
   Describe your eval set, what you measured, and one failure that became a new test case.
3. **What would you change to make it production-ready?**
   Limits and quotas, tracing, evals in CI, privacy handling, fallbacks, and gradual rollout.
4. **What was the hardest part?**
   Usually retrieval quality, context size, or reliability of tool use. Explain how you found and fixed it.
5. **How would you scale it to 1 million users?**
   Caching, queues for indexing, model routing, per-user limits, a sharded or managed vector index, and cost monitoring.

---

#### 8. Common Mistakes

1. Only reading, never building.
2. Building a huge project instead of small finished ones.
3. Projects with no tests or evals.
4. Practising designs without the mobile side.
5. Skipping the estimate (tokens and cost).
6. Not saying the standard concerns out loud.

---

#### 9. Related Topics

1. `05` Calling an LLM API
2. `07` RAG
3. `10`–`12` Agents, Harness, Building an Agent
4. `15` Evaluation & Quality
5. `21` AI Interview Answer Points
6. `BE 12` Checkpoint Project: Notes API
7. `SD 32` Practice: Projects & Designs

---

#### 10. Interview Must Remember

1. **Build small, finish it:** streaming chat, extraction, ask-your-notes, a tool agent.
2. **Practise designs** with a timer, out loud, with the standard concerns and the mobile side.
3. **Estimate tokens and cost** in every design.
4. **Evals and tracing** make a project production-like.
5. Start designs **early,** and add harder ones as you learn.
