# Building an Agent

Roadmap topic 12 · Stage 3: Tools & Agents

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** an agent is less magic than it looks. It is a loop in your code: call the model, run the tool it asks for, add the result, and repeat. Start with the smallest loop that works, then add limits, permissions, and tests. Build one yourself once, so every harness makes sense.

---

#### 1. Define the Job and Check You Need an Agent — 🟢 Must Know

*Steps 1 and 2. Most bad agents start here.*

1. **Define the job:** one clear goal, who it is for, what "done" looks like, and what it must never do.
2. Write 5 to 10 **real example tasks** now. They become your test set later (topic `15`).
3. **Check that you need an agent.** Try in this order (topic `10`):

```text
One prompt  →  a fixed workflow  →  an agent (only if steps can't be known ahead)
```

Example job used below: a **notes assistant** that answers questions about a user's notes and can create a note, with approval.

---

#### 2. Choose the Model and Write the System Prompt — 🟢 Must Know

*Steps 3 and 4.*

1. **Model:** start with a strong model so you can tell if the design works. Move to a cheaper one after your tests pass (topic `03`).
2. **System prompt** should state:
   - the role and the goal,
   - the rules ("never invent notes", "ask before creating or deleting"),
   - **when to stop** and what a good final answer looks like,
   - **when to ask the user** instead of guessing.
3. Keep it short and clear (topic `04`).

```text
You are a notes assistant. Use the tools to find the user's notes.
Answer only from what the tools return. If nothing matches, say so.
Ask the user before creating a note. Stop when you can answer the question.
```

---

#### 3. Define a Few Tools — 🟢 Must Know

*Step 5. Start read-only.*

| Tool | Type | Description (short) |
|---|---|---|
| `search_notes(query)` | Read | Find notes by topic. Returns up to 5 ids, titles, snippets |
| `get_note(id)` | Read | Get the full text of one note |
| `create_note(title, body)` | Write | Create a note. **Needs user approval** |

1. Clear names, clear descriptions, precise argument schemas (topic `08`).
2. Add **write** tools last, and only with approval and idempotency.
3. Keep the count small. Three well-made tools beat ten vague ones.

---

#### 4. Write the Loop — 🟢 Must Know

*Step 6. This is the whole agent.*

Pseudocode:

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

Kotlin-style sketch (not a real SDK, just the shape):

```kotlin
suspend fun runAgent(goal: String, maxSteps: Int = 10): String {
    val messages = mutableListOf(userMessage(goal))
    repeat(maxSteps) {
        val reply = llm.chat(system = SYSTEM_PROMPT, messages = messages, tools = tools)
        messages += reply.asMessage()
        if (reply.toolCalls.isEmpty()) return reply.text          // final answer
        for (call in reply.toolCalls) {
            val result = if (call.needsApproval && !askUser(call)) "User declined."
                         else runCatching { tools.run(call) }.getOrElse { "Error: ${it.message}" }
            messages += toolResult(call.id, result)
        }
        trimIfTooLong(messages)
    }
    return "Stopped: step limit reached."
}
```

Everything else in this topic is about making this loop safe and reliable.

---

#### 5. Add Limits and Permissions — 🟢 Must Know

*Steps 7 and 8.*

Limits:

1. **Max steps**, **timeout**, and a **cost or token budget** per run.
2. **Repeat detection** — stop if the same call repeats.
3. **Send tool errors back** to the model as short messages ("note not found"), so it can recover. Do not crash the run.

Permissions:

1. **Read-only** tools run alone.
2. **Write** tools ask the user first, showing exactly what will happen.
3. Tools use the **real user's identity**, never one shared super-account (`BE 5`).
4. Log every step (topic `18`).

---

#### 6. Manage the Context — 🟢 Must Know

*Step 9.*

1. Every tool result adds tokens. Long runs fill the window (topic `13`).
2. **Shorten** big tool outputs (return snippets, not whole documents).
3. **Summarize or drop** old turns. Keep the goal and rules.
4. **Load on demand:** `get_note(id)` only for the notes that matter.

---

#### 7. Test It — 🟢 Must Know

*Step 10. Without tests you are guessing.*

1. Run your 5 to 10 real example tasks. Write down the expected result for each.
2. Judge the **whole run**, not only the answer: right tools, few steps, in budget, no unsafe action (topic `15`).
3. **Read the traces** (every model call and tool call) to see where it goes wrong (topic `18`).
4. Re-run the tests after every change to the prompt, tools, or model.

---

#### 8. Harden and Improve — 🟡 Good to Know

*Steps 11 to 13.*

1. **Treat tool results as untrusted text.** A note or web page can contain instructions (prompt injection, topic `16`).
2. **Sandbox** risky tools (topic `11`).
3. Add **logging, tracing, and cost tracking**.
4. **Improve in this order:**
   1. Tool descriptions and result formats.
   2. The system prompt.
   3. Add, remove, or merge tools.
   4. Only then, a bigger model or a different design.

---

#### 9. A Sample Run — 🟢 Must Know

*What a good trace looks like.*

```text
User:   What did we decide about the release date? Save a summary.

Step 1  model → search_notes("release date decision")
        tool  → [note 12 "Sprint planning", note 31 "Release sync"]
Step 2  model → get_note(31)
        tool  → "…We agreed to ship on the 14th if QA signs off…"
Step 3  model → create_note("Release date summary", "Ship on the 14th if QA signs off.")
        harness → asks user: "Create this note?"   user → Yes
        tool  → created note 58
Step 4  model → "Decision: ship on the 14th if QA signs off. I saved a summary as note 58."
```

Four steps, two read-only, one approved write, then a final answer.

---

#### 10. Where It Runs, and SDK vs From Scratch — 🟢 Must Know

*Where the agent runs, and whether to build it yourself or use a library.*

1. The agent loop runs on **your backend**, not inside the app. The app sends the goal and shows progress (topic `20`).
2. Runs can take a while: use streaming updates, or a background job with a "done" notification (`SD 21`, `SD 24`).
3. 🟡 **Build from scratch once** to learn how it works. Then consider an **agent SDK or framework** for real projects: it handles the loop, streaming, retries, and tracing for you.
4. Whichever you use, you still own the tools, prompts, permissions, and tests.

---

#### 11. Common Interview Questions

1. **How would you build an agent for X?**
   Define the goal and example tasks, pick a model, write the system prompt, add a few tools, write the loop with limits and approvals, then test with an eval set.
2. **What is the core of an agent in code?**
   A loop: call the model, run the requested tools, add results to the context, repeat until a final answer or a limit.
3. **How do you stop it running forever or spending too much?**
   Max steps, timeout, cost budget, repeat detection, and user cancel.
4. **How do you make it safe?**
   Read-only tools first, approval for writes, the real user's permissions, validated arguments, sandboxing, and untrusted-text handling.
5. **How do you test an agent?**
   A set of real tasks with expected outcomes, judging the answer and the steps, re-run after each change.
6. **What do you fix first when it performs badly?**
   Tool descriptions, then the prompt, then the set of tools, before a bigger model.
7. **Where does the agent run in a mobile product?**
   On the backend. The app sends the goal, shows progress, and handles approvals.

---

#### 12. Common Mistakes

1. Starting with many tools, or with write tools.
2. No step or cost limit.
3. Skipping the test set ("it seemed to work").
4. Vague tool descriptions.
5. Running the loop inside the mobile app with a provider key.
6. Crashing the run on a tool error instead of returning it to the model.
7. Reaching for a bigger model before improving tools and prompts.

---

#### 13. Related Topics

1. `03` Training, Fine-Tuning & Model Choice
2. `04` Prompting & Context Engineering
3. `08` Tool Use & Function Calling
4. `10` Agents
5. `11` Agent Harness
6. `13` Memory & Context Management
7. `15` Evaluation & Quality
8. `20` AI Features in the App
9. `22` Practice: Projects & Designs

---

#### 14. Interview Must Remember

1. **Agent = a loop:** model → tool → result → repeat.
2. **Start small:** clear job, few read-only tools, simple prompt.
3. **Limits:** steps, time, cost. **Approvals** for writes.
4. **Tools use the real user's permissions.**
5. **Test on real tasks** and read the traces.
6. **Fix in order:** tool descriptions → prompt → tool set → model.
7. **Run on the backend,** not in the app.
