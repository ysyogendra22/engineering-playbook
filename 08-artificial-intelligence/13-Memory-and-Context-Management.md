# Memory & Context Management

Roadmap topic 13 · Stage 3: Tools & Agents

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** the context window is the agent's working memory, and it is small and expensive. Long tasks fill it up. Good agents keep the important things, summarize the old things, and store the rest outside the window to load only when needed.

---

#### 1. The Context Window Is Working Memory — 🟢 Must Know

*It fills up, and a full window means worse and costlier answers.*

1. Everything the model sees sits in the window: rules, tools, history, tool results, documents (topic `02`).
2. In an agent, **tool results are the biggest growth**: file contents, search results, web pages.
3. As it fills, cost and latency rise, and quality can fall as important details get buried.
4. The job: keep the window **small, relevant, and organized**.

```text
Turn 1:  [rules][tools][goal]                              small
Turn 20: [rules][tools][goal][20 turns of results...........]   big
```

---

#### 2. Short-Term vs Long-Term Memory — 🟢 Must Know

*Inside the window, or stored outside it.*

| | Short-term memory | Long-term memory |
|---|---|---|
| Where | In the context window | Outside: database, files, vector index |
| Lasts | This conversation or run | Across sessions |
| Example | The last 10 messages | "User prefers metric units", "Project uses Kotlin" |
| Cost | Tokens on every call | Only when retrieved |

1. Without long-term memory, every new conversation starts fresh (topic `02`).
2. Long-term memory works by **saving** facts, then **retrieving** the relevant ones into the context when needed (topic `06`).

---

#### 3. Compaction — 🟢 Must Know

*Summarize older turns to free space.*

1. **Compaction** — replace old conversation and tool output with a short summary, then continue.
2. When: when the context reaches a size threshold, or at natural breaks.
3. Keep: the goal, decisions made, key facts, open tasks, and important file or record names.
4. Drop: repeated results, long raw outputs, dead ends.
5. Risk: a bad summary loses something important. Keep the summary structured, and keep the original in storage if it matters.

---

#### 4. Keep Big Data Outside the Context — 🟢 Must Know

*Give the agent a way to look things up, not the whole library.*

1. Do not paste whole files, tables, or web pages into the context.
2. Give **tools** that return small pieces: search, read a range, list titles.
3. **Load on demand:** first list, then open only what matters.
4. Store large results in a file or database, and put only a **reference and a short summary** in the context.

---

#### 5. Notes Files and To-Do Lists — 🟡 Good to Know

*Notes outside the window keep a long task on track.*

1. For long tasks, let the agent write its own **notes**: a plan, a checklist, decisions so far.
2. The notes live outside the window (a file or a state store). The agent rereads them when needed, or after compaction.
3. A visible to-do list also helps the user follow progress and keeps the agent on track.

---

#### 6. Memory Stores — 🟡 Good to Know

*What to remember, and when to forget.*

1. **What to save:** stable facts and preferences, decisions, corrections the user gave. Not every message.
2. **How to find it:** by keyword, by embedding similarity, or by category (topic `06`).
3. **Forgetting:** memories go stale. Add dates, allow updates, and delete old or wrong ones.
4. **User control:** the user can **see, edit, and delete** what is remembered.
5. **Privacy:** memory is personal data. Store it securely, per user, and never mix users (topic `16`).

---

#### 7. Context Pollution — 🟡 Good to Know

*Bad text in the context makes answers worse.*

1. **Pollution** — old, wrong, or irrelevant text in the context that misleads the model.
2. Examples: an early wrong guess kept in the history, a failed attempt, outdated tool results, a long unrelated discussion.
3. Fixes: remove or correct bad content, restart with a clean summary, and use subagents for side tasks (topic `14`).

---

#### 8. Prompt Caching for Stable Context — 🟡 Good to Know

*Keep the start of the context stable so it can be cached.*

1. The **stable start** of the context (system prompt, tool definitions, project rules) can be cached by the provider. It becomes cheaper and faster on each turn (topic `05`).
2. Keep that part **unchanged and first**. Changing it breaks the cache.
3. Put the changing content (new messages, new results) after it.

---

#### 9. Common Interview Questions

1. **What is the context window and why does it matter for agents?**
   It is the model's working memory. Tool results fill it fast, and a full window raises cost and lowers quality.
2. **Short-term vs long-term memory?**
   Short-term is inside the context window. Long-term is stored outside and retrieved when needed.
3. **How do you handle a long-running task?**
   Compact old turns, keep big data outside the context, load on demand, and keep notes outside the window.
4. **What is compaction and what can go wrong?**
   Summarizing older context to free space. A poor summary can lose key facts, so keep the goal, decisions, and open tasks.
5. **How would you add memory to a chat assistant?**
   Save stable facts and preferences, retrieve the relevant ones per request, and let users view and delete them.
6. **What is context pollution?**
   Wrong or irrelevant text in the context that misleads the model. Clean it, or restart with a summary.
7. **What are the privacy issues with memory?**
   It is personal data. Keep it per user, secured, visible to the user, and deletable.

---

#### 10. Common Mistakes

1. Letting tool output pile up until the window is full.
2. Pasting whole documents instead of retrieving pieces.
3. Summaries that drop the goal or key decisions.
4. Saving every message as "memory".
5. Memory the user cannot see or delete.
6. Mixing memory between users.

---

#### 11. Related Topics

1. `02` How LLMs Work (context window)
2. `04` Prompting & Context Engineering
3. `05` Calling an LLM API (history, caching)
4. `06` Embeddings & Vector Search
5. `11` Agent Harness
6. `14` Multi-Agent Systems
7. `16` Safety, Security & Privacy

---

#### 12. Interview Must Remember

1. **Context window = working memory.** It fills, and cost and quality suffer.
2. **Short-term** in the window. **Long-term** stored outside and retrieved.
3. **Compact** old turns. Keep goal, decisions, open tasks.
4. **Load on demand.** Big data stays outside.
5. **Memory = personal data:** per user, visible, deletable.
6. **Keep the stable prefix first** for caching.
