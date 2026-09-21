# AI: Learning & Interview Roadmap

For a mobile engineer who wants to understand modern AI (LLMs, RAG, agents, harnesses) and answer AI questions in interviews.
This folder has **its own numbering, 1 to 22**. Each topic gets its own doc later.

**How to read references:** a plain number (`7`) is a topic in this folder. `BE 3` is topic 3 in `04-backend-engineering`. `SD 21` is topic 21 in `05-system-design`.

**What you need first:** `BE 1–3` (APIs), `BE 5` (auth), `SD 15` (caching), `SD 21` (queues), `SD 22` (retries), `SD 24` (streaming and real time), `SD 27` (observability).

**Marks:**

| Mark | Meaning |
|---|---|
| 🟢 | **Must have.** Expected in most interviews. Learn first. |
| 🟡 | **Good to have.** Learn after the 🟢 items are solid. |
| (New) | A newer idea that is still changing. Know the idea, not the product. |

---

## Index

| #   | Topic                                | Stage                |
| --- | ------------------------------------ | -------------------- |
| 1   | AI Landscape & ML Basics             | 1. Foundations       |
| 2   | How LLMs Work                        | 1. Foundations       |
| 3   | Training, Fine-Tuning & Model Choice | 1. Foundations       |
| 4   | Prompting & Context Engineering      | 2. Build with LLMs   |
| 5   | Calling an LLM API                   | 2. Build with LLMs   |
| 6   | Embeddings & Vector Search           | 2. Build with LLMs   |
| 7   | RAG                                  | 2. Build with LLMs   |
| 8   | Tool Use & Function Calling          | 3. Tools & Agents    |
| 9   | MCP & Integrations (New)             | 3. Tools & Agents    |
| 10  | Agents                               | 3. Tools & Agents    |
| 11  | Agent Harness (New)                  | 3. Tools & Agents    |
| 12  | Building an Agent                    | 3. Tools & Agents    |
| 13  | Memory & Context Management          | 3. Tools & Agents    |
| 14  | Multi-Agent Systems (New)            | 3. Tools & Agents    |
| 15  | Evaluation & Quality                 | 4. AI in Production  |
| 16  | Safety, Security & Privacy           | 4. AI in Production  |
| 17  | Cost, Latency & Reliability          | 4. AI in Production  |
| 18  | Observability & LLMOps               | 4. AI in Production  |
| 19  | On-Device vs Cloud AI                | 5. AI on Mobile      |
| 20  | AI Features in the App               | 5. AI on Mobile      |
| 21  | AI Interview Answer Points           | 6. Interview         |
| 22  | Practice: Projects & Designs         | 6. Interview         |

**Short on time:** 1, 2, 4, 5, 7, 8, 10, 11, 12, 15, 16, 17, 19, 20, 21. 🟢 items only.

**Glossary:** all key terms are listed at the end, with the topic that explains each one.

---

# Stage 1: Foundations

## 1. AI Landscape & ML Basics

- 🟢 AI vs machine learning vs deep learning vs generative AI vs LLM
- 🟢 Training vs inference
- 🟢 Supervised, unsupervised, reinforcement learning (what each means)
- 🟢 Overfitting; train / validation / test data
- 🟡 Precision, recall, accuracy (when accuracy misleads)
- 🟡 Classic ML tasks: classification, regression, clustering, recommendation
- 🟡 Neural network idea: layers, weights, learning from errors (no math)
- 🟡 Bias and fairness: where they come from in data

## 2. How LLMs Work

- 🟢 Tokens and tokenization
- 🟢 Context window: prompt, history, and answer must all fit
- 🟢 Next-token prediction: the model writes one token at a time
- 🟢 Temperature and top-p: how random the output is
- 🟢 Hallucination: why it happens and what reduces it
- 🟢 The model is stateless: it only knows what is in its context
- 🟢 Knowledge cutoff: it does not know recent events unless you provide them
- 🟡 Transformers and attention (the idea only, no math)
- 🟡 Same prompt can give different answers (probabilistic output)
- 🟡 Very long context can lower quality, and it costs more

## 3. Training, Fine-Tuning & Model Choice

- 🟢 Pretraining vs fine-tuning vs prompting. Try the cheapest first: prompt, then RAG, then fine-tune
- 🟢 Open-weight vs closed (API-only) models
- 🟢 Small vs large models: cost, speed, quality
- 🟢 Reasoning models: spend extra "thinking" tokens on hard problems
- 🟢 Multimodal models: text, image, audio, video
- 🟡 Base model vs instruction-tuned (chat) model
- 🟡 RLHF and preference tuning: shaping helpful and safe behaviour
- 🟡 Distillation: a small model learns from a large one
- 🟡 Quantization: smaller numbers, smaller model, small quality loss
- 🟡 LoRA (parameter-efficient fine-tuning): name only
- 🟡 Public benchmarks vs your own task: benchmarks can mislead

---

# Stage 2: Build with LLMs

## 4. Prompting & Context Engineering

- 🟢 System prompt vs user prompt vs assistant messages
- 🟢 Clear instructions, needed context, output format
- 🟢 Zero-shot vs few-shot (examples in the prompt)
- 🟢 Context engineering: choose what goes into the context (instructions, data, tools, history)
- 🟢 Prompts are code: version them and test them
- 🟡 Step-by-step prompting; reasoning models need less of it
- 🟡 Separate parts of a prompt with clear labels or tags
- 🟡 Prompt templates and variables
- 🟡 Common mistakes: vague, conflicting rules, too much text

## 5. Calling an LLM API

- 🟢 Request and response: messages, roles, tokens used, stop reason
- 🟢 Streaming responses (server-sent events, `SD 24`)
- 🟢 Structured output: JSON schema, and validating the result
- 🟢 Conversation state: the model remembers nothing, so send the history each time
- 🟢 Context limits: truncate or summarize old messages
- 🟢 API keys stay on your server, never inside the app
- 🟢 Rate limits, timeouts, retries with backoff (`SD 22`)
- 🟡 Prompt caching and batch APIs (cost savings)
- 🟡 Model routing: small model for easy tasks, large model for hard ones
- 🟡 Max output length and stop sequences

## 6. Embeddings & Vector Search

- 🟢 Embedding: text turned into numbers, where similar meaning means close together
- 🟢 Similarity search (cosine similarity)
- 🟢 Vector database or index: stores embeddings plus metadata
- 🟡 Keyword search vs semantic search, and hybrid
- 🟡 Approximate nearest-neighbour indexes (HNSW): names only
- 🟡 Choosing an embedding model; re-embed everything if you change it
- 🟡 Other uses: recommendations, clustering, duplicate detection

## 7. RAG (Retrieval-Augmented Generation)

- 🟢 Why RAG: private or fresh data, fewer hallucinations, answers with sources
- 🟢 The pipeline: load → chunk → embed → store → retrieve → prompt → answer
- 🟢 Grounding and citations: answer only from the retrieved text
- 🟢 Per-user access control on retrieval (no data leaks between users)
- 🟡 Chunking choices: size and overlap
- 🟡 Hybrid search and reranking
- 🟡 RAG vs fine-tuning vs long context: when to use which
- 🟡 Keeping the index fresh when documents change
- 🟡 Measure retrieval quality and answer quality separately
- 🟡 (New) Agentic RAG: the agent decides what to search and when

---

# Stage 3: Tools & Agents

## 8. Tool Use & Function Calling

- 🟢 How it works: the model asks for a tool → your code runs it → the result goes back to the model
- 🟢 The model never runs anything itself. Your code does
- 🟢 Tool name, description, and argument schema (good descriptions matter)
- 🟢 Validate arguments and check permissions before running
- 🟢 Tools with side effects: confirmation and idempotency (`BE 3`)
- 🟡 Tool errors: return a clear message so the model can recover
- 🟡 Parallel tool calls
- 🟡 Provider-hosted tools (web search, code execution)
- 🟡 Too many tools confuse the model. Keep the set small

## 9. MCP & Integrations (New)

- 🟢 MCP (Model Context Protocol): an open standard to connect AI apps to tools and data
- 🟢 Roles: the AI app (host and client) and the MCP server
- 🟢 What a server offers: tools, resources, prompts
- 🟢 Why: build a tool once, use it in many AI apps
- 🟡 Local servers vs remote servers (transports)
- 🟡 Security: trust only servers you trust; tool descriptions can carry injected text; authenticate remote servers
- 🟡 MCP vs plain function calling vs calling REST APIs directly
- 🟡 A2A (agent-to-agent protocol): name only

## 10. Agents

- 🟢 Agent = model + tools + a loop that works toward a goal
- 🟢 The loop: think → act (call a tool) → observe the result → repeat until done
- 🟢 Workflow vs agent: code decides the steps vs the model decides. Prefer the simpler one
- 🟢 Workflow patterns: prompt chaining, routing, parallelization, orchestrator–workers, evaluator–optimizer
- 🟢 Stop conditions: goal reached, max steps, max cost, timeout
- 🟢 Human-in-the-loop for risky actions
- 🟡 Planning, and the ReAct pattern (reason, act, observe)
- 🟡 Reflection: the agent checks its own work
- 🟡 Why agents fail: loops, wrong tool, losing the goal, small errors adding up
- 🟡 Levels of autonomy: suggest, ask first, act alone
- 🟡 (New) Coding agents
- 🟡 (New) Computer-use and browser agents

## 11. Agent Harness (New)

- 🟢 Harness = all the code around the model that turns it into a working agent. **Model + harness = agent**
- 🟢 What it does each turn: build the prompt, call the model, run the requested tools, add results, repeat
- 🟢 What it supplies: system prompt, tool definitions, and the rules of the loop
- 🟢 Context management: what stays, what is trimmed, what is summarized (compaction, topic 13)
- 🟢 Permissions: allow, ask, or deny each tool or action
- 🟢 Sandboxing: run tools in a restricted environment
- 🟢 Limits and errors: max turns, retries, cancellation
- 🟡 Hooks: your code runs automatically at set points (before or after a tool call, at start, at stop)
- 🟡 Skills: packaged instructions and scripts loaded only when relevant
- 🟡 Project instruction files (for example `CLAUDE.md`, `AGENTS.md`): standing rules the harness loads
- 🟡 Subagents (topic 14)
- 🟡 Sessions, checkpoints, and resuming work
- 🟡 Permission modes (for example plan-only vs auto-approve)
- 🟡 Same model, different harness gives different results. Harness design matters
- 🟡 Examples of harnesses: coding CLIs, IDE agents, agent SDKs, and one you write yourself

## 12. Building an Agent

*How to make one: start with the smallest loop that works, then add limits, permissions, and tests.*

**Steps, in order**

- 🟢 1. Define the job: one clear goal, who it is for, what "done" means, and what it must never do
- 🟢 2. Check that you need an agent. Try one prompt, then a fixed workflow, before an agent (topic 10)
- 🟢 3. Pick a model. Start with a strong one to get it working, and move to a cheaper one once tests pass (topic 3)
- 🟢 4. Write the system prompt: role, goal, rules, when to stop, and when to ask the user (topic 4)
- 🟢 5. Define a few tools with clear names, descriptions, and argument schemas. Start with read-only tools (topic 8)
- 🟢 6. Write the loop (below): call the model, run the tools it asks for, add the results, repeat
- 🟢 7. Add limits: max steps, timeout, max cost. Send tool errors back to the model so it can recover
- 🟢 8. Add permissions: ask the user before any action that changes something (send, delete, pay)
- 🟢 9. Manage context: shorten big tool outputs and keep the history inside the window (topic 13)
- 🟢 10. Test with an eval set of real tasks, and read the traces to see where it goes wrong (topics 15 and 18)
- 🟡 11. Treat tool results as untrusted text, and sandbox risky tools (topic 16)
- 🟡 12. Add logging, tracing, and cost tracking (topic 18)
- 🟡 13. Improve in this order: tool descriptions first, then the prompt, then add or remove tools

**The minimal agent (pseudocode)**

```text
messages = [system prompt, user goal]
repeat up to MAX_STEPS:
    reply = model(messages, tools)
    if reply has no tool call:
        return reply                      # done
    for each tool call in reply:
        ask the user first if it is risky
        result = run the tool (catch errors)
        add the tool call and result to messages
    shorten messages if they are too long
report that the step limit was reached
```

**Also know**

- 🟢 The agent runs on your backend, not inside the app. The app only talks to your backend (topic 20)
- 🟡 Build it from scratch once to learn how it works, then use an agent SDK or framework
- 🟡 Common first mistakes: too many tools, vague tool descriptions, no step limit, no evals, write access too early

---

## 13. Memory & Context Management

- 🟢 The context window is the agent's working memory, and it fills up
- 🟢 Short-term memory (the conversation) vs long-term memory (stored outside, retrieved later)
- 🟢 Compaction: summarize older turns to free space
- 🟢 Keep big data outside the context and load only what is needed (files, retrieval, tools)
- 🟡 Notes files and to-do lists to keep track during long tasks
- 🟡 Memory stores: what to save, when to forget, and letting users view and delete it
- 🟡 Context pollution: old, wrong, or irrelevant text hurts answers
- 🟡 Prompt caching makes a stable context cheaper

## 14. Multi-Agent Systems (New)

- 🟢 One agent is usually enough. Split only when there is a clear reason
- 🟢 Orchestrator–worker: a lead agent gives subtasks to subagents
- 🟢 A subagent has its own context and returns a short result, so the main context stays clean
- 🟡 Parallel agents for independent tasks. They use more tokens
- 🟡 Handoffs between specialised agents, and routers
- 🟡 Shared state and coordination; conflicts when two agents change the same thing
- 🟡 When one worker fails: retry, skip, or report
- 🟡 Agent-to-agent protocols (A2A): name only

---

# Stage 4: AI in Production

## 15. Evaluation & Quality

- 🟢 Why normal unit tests are not enough for AI output
- 🟢 Build an eval set: real examples with expected results
- 🟢 Re-run evals on every prompt or model change (regression)
- 🟢 What to measure: correctness, groundedness, format, task success
- 🟢 Agent evals: did it finish the task, use the right tools, take few steps, stay in budget
- 🟡 LLM-as-judge, and its limits
- 🟡 User feedback: thumbs up or down, edits, retries
- 🟡 A/B testing prompts and models
- 🟡 Retrieval quality vs answer quality in RAG
- 🟡 Public benchmarks vs your own evals

## 16. Safety, Security & Privacy

- 🟢 Prompt injection: text in a document, web page, or tool result tries to control the model (direct and indirect)
- 🟢 Never trust model output: validate before using it in code, SQL, or shell
- 🟢 Least privilege: the agent can only do what the user may do
- 🟢 Human approval for irreversible or costly actions
- 🟢 Personal data: send the minimum, redact, know the provider's retention rules
- 🟢 Guardrails: input and output checks, moderation
- 🟡 Dangerous mix: private data + untrusted content + a way to send data out
- 🟡 Jailbreaks
- 🟡 Data leakage across users (retrieval, memory, caches)
- 🟡 Never put secrets in prompts or logs
- 🟡 Abuse limits: rate limits per user, cost caps

## 17. Cost, Latency & Reliability

- 🟢 Tokens (input and output) drive both cost and latency
- 🟢 Time to first token vs total time. Streaming improves perceived speed
- 🟢 Caching: repeated answers, and prompt caching for repeated prompt parts
- 🟢 Timeouts, retries, and fallbacks (another model, a simple answer, or a clear error)
- 🟢 Move non-urgent work to a queue (`SD 21`)
- 🟡 Smaller models, model routing, shorter prompts, capped output
- 🟡 Budgets: per-user limits, max steps for agents, cost alerts
- 🟡 Batch processing for offline work
- 🟡 Provider outages: multiple providers or a degraded mode

## 18. Observability & LLMOps

- 🟢 Log each call: prompt version, model, tokens, latency, errors (mind personal data)
- 🟢 Tracing: see every step of an agent run (model calls, tool calls, results)
- 🟢 Version prompts, models, and tool definitions
- 🟢 Model upgrades: re-run evals before switching. Models get retired
- 🟡 Dashboards: cost per user and feature, error rate, p95 latency (`SD 27`)
- 🟡 Feedback loop: turn real failures into new eval cases
- 🟡 Gradual rollout and feature flags for AI features (`SD 28`)

---

# Stage 5: AI on Mobile

## 19. On-Device vs Cloud AI

- 🟢 Where to run the model: on the device, in the cloud, or both
- 🟢 On-device: private, works offline, low latency, no per-call cost
- 🟢 On-device limits: model size, battery, heat, memory, older phones
- 🟢 Cloud: stronger models and easy updates, but needs network and costs per call
- 🟢 Hybrid: on-device first, fall back to the cloud
- 🟡 Platform options (names): Core ML and Apple's on-device models, ML Kit, Gemini Nano, LiteRT (formerly TensorFlow Lite)
- 🟡 Model download size, updates, and versioning
- 🟡 Quantization for smaller on-device models

## 20. AI Features in the App

- 🟢 The app calls your backend, and your backend calls the model. Never ship a provider key in the app
- 🟢 Streaming chat UI: show tokens as they arrive, allow cancel and retry
- 🟢 Clear states: loading, partial answer, error, offline
- 🟢 Long agent tasks: show progress, allow cancel, ask approval before actions
- 🟢 Tell users the answer may be wrong; let them correct or report it
- 🟢 Per-user rate limits and quotas, enforced on the server
- 🟡 Push notification when a background task finishes (`SD 24`)
- 🟡 Keep history locally and sync it (`SD 30`)
- 🟡 Voice and camera input
- 🟡 Battery and data use of long-running AI features

---

# Stage 6: Interview

## 21. AI Interview Answer Points (New)

- 🟢 Start with the user problem, then decide if AI is needed at all
- 🟢 Standard concerns to cover: hallucination, cost, latency, privacy, safety, evaluation
- 🟢 Ready answers: reduce hallucination, control cost, test it, stop prompt injection
- 🟢 Ready answers: RAG vs fine-tuning, workflow vs agent, one agent vs many
- 🟢 Fit AI into the normal design steps (`SD 31`): requirements, API, data, flows, failures
- 🟡 Explain each in 30 seconds: LLM, RAG, tool use, MCP, agent, harness
- 🟡 Say what you would build first and how you would measure success
- 🟡 Common trade-offs: quality vs cost, quality vs latency, on-device vs cloud, autonomy vs control

## 22. Practice: Projects & Designs

**Build (in order)**

- 🟢 Streaming chat: your backend calls an LLM API, a mobile app shows tokens as they arrive (after 5)
- 🟢 Structured extraction: text in, validated JSON out (after 5)
- 🟢 Ask your notes: RAG over the Notes API data (`BE 12`) (after 7)
- 🟢 Tool-using assistant: two or three tools, and an agent loop you write yourself, following topic 12 (after 12)
- 🟡 Grow that agent into a mini harness: hooks, a sandboxed tool, saved sessions, context compaction (after 13)
- 🟡 A small eval set and a script that runs it (after 15)
- 🟡 One on-device feature: text classification or image labelling (after 19)

**Design (in order)**

- 🟢 Customer-support chatbot
- 🟢 Chat with your documents (RAG)
- 🟢 AI writing or summarizing feature inside an app
- 🟢 Semantic search
- 🟢 Coding or task-running agent (harness, tools, permissions, sandbox)
- 🟡 Content moderation pipeline
- 🟡 Recommendation system
- 🟡 Voice assistant
- 🟡 Multi-agent research assistant

---

# Glossary

Plain meanings. The last column is the topic that explains the term.

**Model basics**

| Term | Plain meaning | Topic |
|---|---|---|
| AI | Software that does tasks that normally need human intelligence | 1 |
| Machine learning (ML) | Learning patterns from data instead of hand-written rules | 1 |
| Deep learning | ML that uses neural networks with many layers | 1 |
| Generative AI | AI that creates new text, images, audio, or code | 1 |
| Training / inference | Training: learning from data. Inference: using the trained model | 1 |
| LLM | Large language model, trained on huge amounts of text to predict the next token | 2 |
| Parameters (weights) | The numbers a model learned during training | 2 |
| Token | A chunk of text (often part of a word) that the model reads and writes | 2 |
| Context window | The most tokens the model can consider at once (input and output) | 2 |
| Temperature / top-p | Settings that control how random the output is | 2 |
| Hallucination | A confident answer that is wrong or made up | 2 |
| Knowledge cutoff | The date after which the model saw no training data | 2 |
| Transformer / attention | The model design behind LLMs. Attention lets each token look at the others | 2 |
| Pretraining / fine-tuning | Broad first training / extra training on narrow data | 3 |
| Open-weight model | A model whose weights you can download and run yourself | 3 |
| Reasoning model | A model that uses extra "thinking" tokens before it answers | 3 |
| Multimodal | Handles more than text: images, audio, video | 3 |
| RLHF | Training with human preference ratings to shape behaviour | 3 |
| Distillation | Training a small model to copy a large one | 3 |
| Quantization | Using lower-precision numbers to make a model smaller | 3 |

**Building with LLMs**

| Term | Plain meaning | Topic |
|---|---|---|
| Prompt | The input given to the model | 4 |
| System prompt | Standing instructions from the developer that set the model's behaviour | 4 |
| Zero-shot / few-shot | No examples in the prompt / a few examples in the prompt | 4 |
| Context engineering | Choosing what goes into the context window | 4 |
| Structured output | An answer in a fixed format, such as JSON | 5 |
| Streaming | Sending the answer piece by piece as it is produced | 5 |
| Time to first token (TTFT) | How long until the first piece of the answer arrives | 5, 17 |
| Prompt caching | Reusing an unchanged start of a prompt so it costs less and runs faster | 5 |
| Model routing | Sending easy tasks to a small model and hard ones to a large model | 5, 17 |
| Embedding | Numbers that represent meaning. Similar meaning means close together | 6 |
| Vector database | A store built for finding the nearest embeddings | 6 |
| RAG | Retrieve relevant text, then give it to the model along with the question | 7 |
| Chunking | Cutting documents into pieces before embedding them | 7 |
| Reranking | Re-ordering search results by how well they match | 7 |
| Grounding | Tying the answer to the provided sources | 7 |

**Tools and agents**

| Term | Plain meaning | Topic |
|---|---|---|
| Tool use / function calling | The model asks your code to run a function and gets the result back | 8 |
| MCP | Model Context Protocol: an open standard to connect AI apps to tools and data | 9 |
| A2A | A protocol for agents to talk to other agents (name only) | 9, 14 |
| Agent | A model with tools and a loop that works toward a goal | 10 |
| Agent loop | The repeated cycle: call the model, run the tools it asks for, feed results back | 10, 12 |
| Trajectory | The full record of steps, tool calls, and results in one agent run | 12, 15 |
| Workflow | Fixed steps written in code, some of which call an LLM | 10 |
| ReAct | Pattern: reason, act, observe, repeat | 10 |
| Human-in-the-loop | A person approves or guides the key steps | 10 |
| Harness | The code around the model that runs the loop, tools, context, and permissions | 11 |
| Sandbox | A restricted environment where tools run | 11 |
| Hook | Your code that runs automatically at set points in the agent loop | 11 |
| Skill | Packaged instructions or scripts an agent loads when relevant | 11 |
| Permission mode | Rules for which actions run alone and which need approval | 11 |
| Compaction | Summarizing older context to free space | 13 |
| Memory | Information kept across turns or sessions | 13 |
| Subagent | A helper agent with its own context, given one subtask | 14 |
| Orchestrator | The lead agent or code that splits work and assigns it | 14 |

**Production**

| Term | Plain meaning | Topic |
|---|---|---|
| Eval | A test set plus scoring, used to measure AI quality | 15 |
| LLM-as-judge | Using a model to grade another model's output | 15 |
| Guardrails | Checks on inputs and outputs that block unsafe or invalid content | 16 |
| Prompt injection | Hidden instructions in content that try to take over the model | 16 |
| Jailbreak | A prompt that tries to make the model break its rules | 16 |
| PII | Personally identifiable information | 16 |
| Tracing | Recording every step of an agent run | 18 |
| LLMOps | Practices for running LLM apps in production | 18 |
| On-device AI | The model runs on the phone itself | 19 |

---

## Skip for Now

- Training models from scratch, GPU and CUDA details, the math of transformers
- Detailed fine-tuning methods. Know the names only
- Model-by-model comparisons and version numbers. They go out of date fast
- Provider-specific product details

## How to Proceed

1. Do topics 1 and 2 first. They give the words you need for everything else.
2. After topic 5, build the streaming chat. After topic 7, build "ask your notes".
3. After topics 10 and 11, follow topic 12 and build a small agent yourself. Then grow it into a mini harness (topics 13 and 14).
4. Do topics 15 to 17 before any design practice. Interviewers push on quality, cost, and safety.
5. For each topic: what it is, what problem it solves, how it works, one downside.
