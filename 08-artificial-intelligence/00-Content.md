# AI: Interview Roadmap

For a mobile engineer preparing for AI-related interview questions and building AI features into apps.
This is **part 3 (topics 34–47)**. Finish **part 1 (topics 1–12)** in `04-backend-engineering` and the core of **part 2** in `05-system-design` first. Each topic gets its own doc later.

**What you need from earlier parts:** API basics (1–3), auth (5), caching (15), queues (21), retries (22), real-time and streaming (24), observability (27).

**Marks:**

| Mark | Meaning |
|---|---|
| 🟢 | **Must have.** Expected in most interviews. Learn first. |
| 🟡 | **Good to have.** Learn after the 🟢 items are solid. |
| (New) | Added beyond the original roadmaps. |

---

## Index

| #   | Topic                                    | Stage                |
| --- | ---------------------------------------- | -------------------- |
| 34  | AI, ML & LLM Basics                      | 9. AI Foundations    |
| 35  | How LLMs Work (Interview Level)          | 9. AI Foundations    |
| 36  | Prompting & Structured Output            | 10. Build with LLMs  |
| 37  | Calling an LLM API                       | 10. Build with LLMs  |
| 38  | Tool Use & Function Calling              | 10. Build with LLMs  |
| 39  | Embeddings, Vector Search & RAG          | 10. Build with LLMs  |
| 40  | Agents                                   | 10. Build with LLMs  |
| 41  | Evaluation & Quality                     | 11. AI in Production |
| 42  | Safety, Security & Privacy               | 11. AI in Production |
| 43  | Cost, Latency & Reliability              | 11. AI in Production |
| 44  | On-Device vs Cloud AI (New)              | 12. AI on Mobile     |
| 45  | AI Features in the App (New)             | 12. AI on Mobile     |
| 46  | AI Interview Answer Points (New)         | 13. Interview        |
| 47  | Practice: Projects & Designs             | 13. Interview        |

**Short on time (1 week):** 34, 35, 37, 39, 42, 43, 44, 45, 46. 🟢 items only.

---

# Stage 9: AI Foundations

## 34. AI, ML & LLM Basics

- 🟢 Key terms in plain words: model, parameters, prompt, token, embedding, hallucination, inference
- 🟢 AI vs machine learning vs deep learning vs generative AI vs LLM
- 🟢 Training vs inference
- 🟢 Supervised, unsupervised, reinforcement learning (what each means)
- 🟢 Overfitting; train / validation / test data
- 🟡 Precision, recall, accuracy (when accuracy misleads)
- 🟡 Classic ML tasks: classification, regression, clustering, recommendation

## 35. How LLMs Work (Interview Level)

- 🟢 Tokens, context window, prompt vs completion
- 🟢 Next-token prediction; temperature and top-p
- 🟢 Why models hallucinate, and what reduces it
- 🟢 Embeddings: meaning as numbers, similarity between them
- 🟡 Transformers and attention (the idea only, no math)
- 🟡 Pretraining, fine-tuning, RLHF (names and purpose)
- 🟡 Model size, open vs closed models, small vs large trade-offs
- 🟡 (New) Multimodal models (text, image, audio)

---

# Stage 10: Build with LLMs

## 36. Prompting & Structured Output

- 🟢 System prompt vs user prompt
- 🟢 Clear instructions, context, and examples (few-shot)
- 🟢 Structured output: JSON schema, and validating the result
- 🟢 Prompts are code: version them and test them
- 🟡 Reasoning models and step-by-step prompting
- 🟡 Common prompt mistakes (vague, too long, conflicting rules)

## 37. Calling an LLM API

- 🟢 Request and response shape: messages, roles, tokens used
- 🟢 Streaming responses (server-sent events)
- 🟢 API keys stay on your server, never inside the app
- 🟢 Rate limits, timeouts, retries with backoff (topic 22)
- 🟢 Conversation state: the model remembers nothing, so you send the history
- 🟢 Context limits: truncate or summarize old messages
- 🟡 Prompt caching and batch APIs (cost savings)
- 🟡 Model routing: small model for easy tasks, large model for hard ones

## 38. Tool Use & Function Calling

- 🟢 How it works: model asks for a tool, your code runs it, result goes back
- 🟢 Tool descriptions and argument schemas
- 🟢 Validate arguments and check permissions before running a tool
- 🟢 Tools with side effects need confirmation and idempotency
- 🟡 MCP (Model Context Protocol): a standard way to connect tools
- 🟡 Tool errors and how the model recovers

## 39. Embeddings, Vector Search & RAG

- 🟢 Why RAG: private or fresh data, fewer hallucinations
- 🟢 The pipeline: chunk → embed → store → retrieve → prompt → answer
- 🟢 Vector search: nearest neighbours by similarity
- 🟢 Cite sources in the answer
- 🟡 Chunking choices (size, overlap)
- 🟡 Hybrid search (keyword + vector) and reranking
- 🟡 Approximate nearest-neighbour indexes (names only)
- 🟡 RAG vs fine-tuning: when to use which
- 🟡 Keeping the index fresh when documents change

## 40. Agents

- 🟢 The agent loop: think → call a tool → observe → repeat
- 🟢 Workflow (fixed steps) vs agent (model decides): prefer the simpler one
- 🟢 Limits: max steps, max cost, timeouts
- 🟢 Human approval for risky actions
- 🟡 Memory: short-term (conversation) vs long-term (stored facts)
- 🟡 Multi-agent setups (names only)
- 🟡 Why agents fail: loops, wrong tool, drifting from the goal

---

# Stage 11: AI in Production

## 41. Evaluation & Quality

- 🟢 Why normal unit tests are not enough for AI output
- 🟢 Build an eval set: real examples with expected results
- 🟢 Re-run evals on every prompt or model change (regression)
- 🟢 What to measure: correctness, groundedness (answers match the sources), format
- 🟡 LLM-as-judge (and its limits)
- 🟡 User feedback: thumbs up/down, edits, retries
- 🟡 A/B testing prompts and models
- 🟡 Retrieval quality vs answer quality (measure separately in RAG)

## 42. Safety, Security & Privacy

- 🟢 Prompt injection: text in a document or web page tries to control the model
- 🟢 Never trust model output: validate it before using it in code, SQL, or shell
- 🟢 Least privilege for tools: the model can only do what the user may do
- 🟢 Personal data: send the minimum, redact, know the provider's retention rules
- 🟢 Input and output filters, moderation
- 🟡 Jailbreaks
- 🟡 Data leakage across users in RAG (per-user access control on retrieval)
- 🟡 Abuse limits: rate limit per user, cost caps

## 43. Cost, Latency & Reliability

- 🟢 Tokens drive both cost and latency
- 🟢 Streaming: faster first word, better perceived speed
- 🟢 Cache repeated answers and repeated prompt parts
- 🟢 Timeouts, retries, and fallbacks (another model, a simple answer, or a clear error)
- 🟢 Move non-urgent work to a queue (topic 21)
- 🟡 Smaller models, shorter prompts, limiting output length
- 🟡 Monitoring: latency, token usage, error rate, cost per user
- 🟡 Logging prompts safely (personal data)

---

# Stage 12: AI on Mobile

## 44. On-Device vs Cloud AI (New)

- 🟢 Where to run the model: on the device, in the cloud, or both
- 🟢 On-device: private, works offline, low latency, no per-call cost
- 🟢 On-device limits: model size, battery, heat, memory, older phones
- 🟢 Cloud: stronger models and easy updates, but needs network and costs per call
- 🟢 Hybrid: on-device first, fall back to the cloud
- 🟡 Platform options (names): Core ML and Apple's on-device models, ML Kit, Gemini Nano, LiteRT (formerly TensorFlow Lite)
- 🟡 Model download size, updates, and versioning
- 🟡 Quantization (smaller models, small quality loss)

## 45. AI Features in the App (New)

- 🟢 Call your own backend, which calls the model. Never ship a provider key in the app
- 🟢 Streaming chat UI: show tokens as they arrive, allow cancel and retry
- 🟢 Clear states: loading, partial answer, error, offline
- 🟢 Tell users the answer may be wrong; let them correct or report it
- 🟢 Per-user rate limits and quotas (enforced on the server)
- 🟡 Keep history locally and sync it (topic 30, offline sync)
- 🟡 Voice and camera input
- 🟡 Battery and data use of long-running AI features

---

# Stage 13: Interview

## 46. AI Interview Answer Points (New)

- 🟢 Start with the user problem, then decide if AI is needed at all
- 🟢 Standard concerns to cover: hallucination, cost, latency, privacy, evaluation
- 🟢 Ready answers: "How do you reduce hallucination?", "How do you control cost?", "How do you test it?"
- 🟢 Fit AI into the normal design steps (topic 31): requirements, API, data, flows, failures
- 🟡 Say what you would build first, and how you would measure success
- 🟡 Common trade-offs: quality vs cost, quality vs latency, on-device vs cloud

## 47. Practice: Projects & Designs

**Build (in order)**

- 🟢 Streaming chat: your backend calls an LLM API, a mobile app shows tokens as they arrive
- 🟢 Ask your notes: RAG over the Notes API data (topic 12)
- 🟡 Assistant with two or three tools (for example, create a note, search notes)
- 🟡 One on-device feature (text classification or image labelling)

**Design (in order)**

- 🟢 Customer-support chatbot
- 🟢 Chat with your documents (RAG)
- 🟢 AI writing or summarizing feature inside an app
- 🟢 Semantic search
- 🟡 Content moderation pipeline
- 🟡 Recommendation system
- 🟡 Voice assistant
- 🟡 Coding or task-running agent

---

## Skip for Now

- Training models from scratch, GPU and CUDA details, the math of transformers
- Detailed fine-tuning methods (LoRA and similar). Know the names only
- Model benchmarks and version-by-version comparisons. They go out of date fast
- Provider-specific product details

## How to Proceed

1. Finish the Notes API (topic 12) first.
2. Do 34 and 35 next. They give the words you need for everything else.
3. After topic 37, build the streaming chat project. After topic 39, build "ask your notes".
4. Do 41 to 43 before any design practice. Interviewers push on quality, cost, and safety.
5. For each topic: what it is, what problem it solves, how it works, one downside.
