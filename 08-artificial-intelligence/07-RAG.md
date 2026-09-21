# RAG (Retrieval-Augmented Generation)

Roadmap topic 7 · Stage 2: Build with LLMs

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** RAG is an open-book exam for the model. Before answering, your system searches your own documents, finds the relevant pieces, and puts them in the prompt. The model then answers from them. This is the standard way to make an LLM work with private or fresh data.

---

#### 1. Why RAG — 🟢 Must Know

*The model does not know your data. RAG hands it the right pages.*

1. The model does not know your private documents, and it has a knowledge cutoff (topic `02`).
2. **Private or fresh data** — search your own notes, help pages, or database.
3. **Fewer hallucinations** — the model answers from real text.
4. **Sources** — you can show where the answer came from.
5. **Cheaper and easier than fine-tuning** for adding facts (topic `03`).
6. Access can be controlled per user.

---

#### 2. The Pipeline — 🟢 Must Know

*Two phases: prepare the data once, then retrieve on every question.*

```text
PREPARE (offline, repeat when documents change)
Documents → split into chunks → embed each chunk → store in vector index

ANSWER (on every question)
Question → embed → search index → top chunks
        → prompt = instructions + chunks + question
        → LLM → answer (+ sources)
```

The steps: **load → chunk → embed → store → retrieve → prompt → answer.**

Example prompt:

```text
Answer using only the notes below. If the answer is not in them, say
"I could not find that in your notes." Cite the note IDs.

[note 12] ...text...
[note 31] ...text...

Question: What did we decide about the release date?
```

---

#### 3. Grounding and Citations — 🟢 Must Know

*Make the model stay inside the sources, and show them.*

1. **Grounding** — the answer is tied to the provided text.
2. Tell the model to answer **only** from the context, and to say when the answer is missing.
3. Ask it to **cite** the source IDs, so the app can show links or "from your note X".
4. Check that cited IDs really exist in what you sent.
5. Grounding lowers hallucination. It does not remove it.

---

#### 4. Per-User Access Control — 🟢 Must Know

*Retrieval must respect who is asking.*

1. Store the **owner or permissions** as metadata on every chunk.
2. **Filter at search time** (`user_id = 42`). Do not retrieve everything and hope the model hides it.
3. If a user must not see a document, its text must never reach that user's prompt.
4. Same rule as normal APIs: check permissions on the server (`BE 5`).

This is the most serious RAG bug: one user's data leaking into another user's answer.

---

#### 5. Chunking — 🟡 Good to Know

*Documents are cut into pieces before embedding.*

1. **Chunk** — a small piece of a document (a few paragraphs).
2. **Too big** — vague meaning, wastes context. **Too small** — loses surrounding meaning.
3. **Overlap** — repeat a little text between neighbouring chunks so ideas are not cut in half.
4. Split on natural boundaries (headings, paragraphs), not in the middle of a sentence.
5. Keep metadata with each chunk: source, title, date, owner.

---

#### 6. Hybrid Search and Reranking — 🟡 Good to Know

*Two upgrades that make the retrieved text better.*

1. **Hybrid search** — combine keyword and vector search (topic `06`). It finds exact terms and similar meanings.
2. **Reranking** — retrieve, for example, 30 candidates cheaply, then use a stronger model to reorder them and keep the best 5.
3. Both improve which chunks reach the model. That usually matters more than which LLM you use.

---

#### 7. RAG vs Fine-Tuning vs Long Context — 🟡 Good to Know

*Three ways to give a model your data. Each fits different needs.*

| | RAG | Fine-tuning | Long context (paste everything) |
|---|---|---|---|
| Best for | Facts, private and changing data | Style, format, narrow skills | Small, one-off documents |
| Updating data | Update the index | Retrain | Resend each time |
| Cost per request | Small | Small | High (many tokens) |
| Sources / citations | Yes | No | Yes |
| Per-user access | Easy (filters) | Hard | Easy |

Often the answer is: RAG for knowledge, a good prompt for behaviour, fine-tuning only if still needed.

---

#### 8. Keeping the Index Fresh — 🟡 Good to Know

*The index must change when your documents change.*

1. When a document is **created, changed, or deleted**, update its chunks and vectors.
2. Do it in a **background job** triggered by the change (`SD 21`).
3. **Deletes matter:** remove vectors for deleted or revoked documents, or they will still be retrieved.
4. Store a version or timestamp, so you can spot stale chunks.

---

#### 9. Measuring RAG — 🟡 Good to Know

*Two things can fail: finding the right text, and answering from it.*

1. **Retrieval quality** — did the right chunk appear in the top results?
2. **Answer quality** — given the right chunks, was the answer correct and grounded?
3. Test them **separately**. If retrieval is bad, fixing the prompt will not help (topic `15`).
4. Build a small set of real questions with the expected source documents.

---

#### 10. Agentic RAG (New) — 🟡 Good to Know

*Let the agent decide what to search, and search again if needed.*

1. In basic RAG, retrieval happens **once**, before the answer.
2. In **agentic RAG**, search is a **tool** (topic `08`). The agent decides what to search, searches again with a better query, and stops when it has enough.
3. Better for hard, multi-step questions. Costs more and is slower, so use it only when simple RAG is not enough.

---

#### 11. Common Interview Questions

1. **What is RAG and why use it?**
   Search your documents at question time and give the relevant pieces to the model. It brings private and fresh data and reduces hallucination.
2. **Walk me through a RAG pipeline.**
   Chunk documents, embed them, store them. At query time embed the question, retrieve top chunks, build a prompt, and generate an answer with citations.
3. **RAG or fine-tuning?**
   RAG for facts and changing data. Fine-tuning for style or format.
4. **How do you stop users seeing each other's data?**
   Store owner metadata on chunks and filter at search time on the server.
5. **The answers are wrong. How do you debug it?**
   Check retrieval first (right chunks found?), then the prompt and grounding.
6. **How do you keep it up to date?**
   Re-index changed documents in a background job, and remove deleted ones.
7. **How do you improve retrieval?**
   Better chunking, hybrid search, reranking, and metadata filters.

---

#### 12. Common Mistakes

1. Retrieving without per-user filters.
2. Chunks too large, too small, or cut mid-sentence.
3. No instruction to say "not found", so the model guesses.
4. Never updating or deleting from the index.
5. Blaming the LLM when retrieval is the problem.
6. Fine-tuning to add facts that RAG handles better.

---

#### 13. Related Topics

1. `02` How LLMs Work (knowledge cutoff, hallucination)
2. `06` Embeddings & Vector Search
3. `08` Tool Use & Function Calling (agentic RAG)
4. `15` Evaluation & Quality
5. `16` Safety, Security & Privacy (data leakage, injection)
6. `22` Practice: Projects & Designs (ask your notes)

---

#### 14. Interview Must Remember

1. **RAG = retrieve relevant text, then generate from it.**
2. **Pipeline:** chunk → embed → store → retrieve → prompt → answer.
3. **Ground and cite.** Allow "not found".
4. **Filter by user at search time.**
5. **Facts → RAG. Behaviour → prompt or fine-tune.**
6. **Debug retrieval and answer separately.**
