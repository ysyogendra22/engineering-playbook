# Embeddings & Vector Search

Roadmap topic 6 · Stage 2: Build with LLMs

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** an embedding turns a piece of text into a list of numbers that captures its meaning. Texts with similar meaning get similar numbers. That lets you search by meaning, not just by matching words. It is the base of RAG.

---

#### 1. What Is an Embedding — 🟢 Must Know

*Meaning as numbers. Similar meaning means close together.*

1. An **embedding** is a **vector** (a list of numbers, for example 768 or 1,536 of them) that represents the meaning of a text.
2. An **embedding model** creates it. It is a different model from the chat model, and cheaper.
3. Texts with similar meaning have vectors that are **close**.

```text
"cheap phone"            → [0.12, -0.40, 0.83, ...]
"affordable smartphone"  → [0.10, -0.38, 0.80, ...]   ← very close
"banana bread recipe"    → [-0.65, 0.22, -0.10, ...]  ← far away
```

4. You can embed sentences, paragraphs, documents, and also images or audio (with a multimodal embedding model).

---

#### 2. Similarity: Cosine — 🟢 Must Know

*How close are two vectors? Compare their direction.*

1. **Cosine similarity** measures the angle between two vectors. A higher score means more similar meaning.
2. You do not need the formula. Know: "vectors pointing the same way = similar meaning".
3. Searching means: embed the **query**, then find the stored vectors with the **highest similarity**. These are the **nearest neighbours**.

```text
Query: "how do I reset my password"
   ↓ embed
Find nearest stored chunks  →  "Forgot password? Tap Settings > Account ..."
```

---

#### 3. Vector Database or Index — 🟢 Must Know

*A place to store vectors and find the nearest ones fast.*

1. A **vector database** (or vector index) stores each item as: an ID, its vector, the original text, and **metadata** (owner, date, source, type).
2. You query with a vector and get the **top-K** most similar items.
3. Metadata lets you **filter**: "only this user's notes", "only documents after 2024".
4. Options: a dedicated vector database, or a vector feature in a database you already use (for example, pgvector in PostgreSQL). Start with what you already run if the data is small.

```text
Store:  id=17 | vector=[...] | text="..." | user_id=42 | created=2025-03-01
Query:  vector + filter(user_id=42) + top_k=5
```

---

#### 4. Keyword vs Semantic vs Hybrid Search — 🟡 Good to Know

*Each finds things the other misses.*

| | Keyword search | Semantic search | Hybrid |
|---|---|---|---|
| How | Matches the exact words | Matches meaning (vectors) | Both, results combined |
| Finds | "error 4032", product codes, names | "cheap phone" ≈ "affordable smartphone" | Most of both |
| Weak at | Different wording | Exact IDs and rare terms | More work to set up |

1. **Semantic search** looks for meaning, not exact words.
2. For real products, **hybrid** search often gives the best results (topic `07`).

---

#### 5. Approximate Nearest Neighbour (ANN) — 🟡 Good to Know

*Exact search compares with every vector. That is too slow at scale.*

1. **Exact search** — compare the query to every vector. Correct, but slow for millions of items.
2. **ANN** — uses a smart index to find vectors that are very likely the nearest, much faster. You accept a tiny accuracy loss.
3. **HNSW** is a popular ANN index. Name only.
4. For a few thousand items, exact search is fine. Do not over-engineer.

---

#### 6. Choosing and Changing Embedding Models — 🟡 Good to Know

*Vectors from different models do not match, so a model change is a big change.*

1. Vectors from **different models cannot be compared**. Store which model made each vector.
2. If you change the embedding model, you must **re-embed everything**. Plan for it (a background job, `SD 21`).
3. Choose by quality on **your** data, cost, vector size, and languages supported. Bigger vectors cost more storage and are slower to search.
4. Embed the same way for documents and queries (same model, similar text cleaning).

---

#### 7. Other Uses of Embeddings — 🟡 Good to Know

*Embeddings help with more than search.*

1. **Recommendations** — "items close to what the user liked".
2. **Clustering** — group similar texts.
3. **Duplicate detection** — find near-identical items.
4. **Classification** — nearest labelled examples.
5. **Long-term memory for agents** — store notes as vectors and retrieve the relevant ones (topic `13`).

---

#### 8. Common Interview Questions

1. **What is an embedding?**
   A vector of numbers representing meaning. Similar meanings are close together.
2. **How does semantic search work?**
   Embed the query, find the nearest stored vectors, and return their text.
3. **Keyword vs semantic search?**
   Keyword matches exact words. Semantic matches meaning. Hybrid uses both.
4. **What is a vector database?**
   A store built to find the nearest vectors quickly, with metadata filters.
5. **Why use approximate search?**
   Comparing against every vector is too slow at scale. ANN is much faster with a small accuracy loss.
6. **What happens if you change the embedding model?**
   The old vectors no longer match. You must re-embed all data.
7. **Do you always need a vector database?**
   No. For small data, exact search or an extension on your existing database is enough.

---

#### 9. Common Mistakes

1. Mixing vectors from different embedding models.
2. Using semantic search alone for exact terms such as IDs and error codes.
3. Forgetting metadata filters, so users can see each other's data.
4. Adding a vector database for a tiny dataset.
5. No plan to re-embed when the model or the documents change.
6. Embedding very long text as one vector, which blurs the meaning.

---

#### 10. Related Topics

1. `02` How LLMs Work
2. `07` RAG
3. `13` Memory & Context Management
4. `SD 17` Choosing a Database
5. `SD 21` Queues, Events & Background Jobs (re-embedding jobs)
6. `SD 33` Follow-Up Topics (search basics)

---

#### 11. Interview Must Remember

1. **Embedding** = meaning as numbers. Close vectors = similar meaning.
2. **Search:** embed the query → nearest vectors → return their text.
3. **Vector DB** = vectors + metadata + fast nearest search.
4. **Hybrid** (keyword + semantic) is often best.
5. **Change the model = re-embed everything.**
6. **Filter by metadata** for per-user data.
