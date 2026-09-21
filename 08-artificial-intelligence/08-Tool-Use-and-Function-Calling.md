# Tool Use & Function Calling

Roadmap topic 8 · Stage 3: Tools & Agents

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** a model can only produce text. Tool use lets it ask your code to do things: search notes, read a database, send an email. The model says which tool it wants and with what arguments. Your code runs it and sends the result back.

---

#### 1. How Tool Use Works — 🟢 Must Know

*The model asks. Your code acts. The result goes back to the model.*

```text
1. You send: user message + list of available tools
2. Model replies: "call search_notes with query='release date'"
3. Your code runs search_notes(...)
4. You send the tool result back to the model
5. Model replies with the final answer (or asks for another tool)
```

1. The model decides **whether** to call a tool, **which one**, and **with what arguments**.
2. Steps 2 to 5 can repeat several times for one question. That repeat is the start of an agent (topic `10`).
3. The stop reason of a response tells you when the model wants a tool instead of giving a final answer (topic `05`).

**Mobile view:** like a screen calling a repository. The model is the UI asking for data. Your code is the repository that does the real work.

---

#### 2. The Model Never Runs Anything — 🟢 Must Know

*It only writes a request. Your code decides whether to run it.*

1. The model produces text that says "call this function with these arguments". Nothing executes by itself.
2. **Your code** runs the tool, on your server, with your permissions.
3. That is your control point: you can check, refuse, log, ask the user, or limit it.
4. Treat the model's tool request like **untrusted input from a user**.

---

#### 3. Defining a Tool — 🟢 Must Know

*A name, a description, and an argument schema. The description is the most important part.*

```json
{
  "name": "search_notes",
  "description": "Search the user's notes by keyword or topic. Use when the user asks about something they wrote. Returns up to 5 notes with id, title, and a short snippet.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": { "type": "string", "description": "What to search for" },
      "limit": { "type": "integer", "description": "Max results, 1 to 10" }
    },
    "required": ["query"]
  }
}
```

1. The model chooses tools by reading the **description**. Say what it does, when to use it, and what it returns.
2. Use clear names (`search_notes`, not `tool1`).
3. Describe each argument. Use fixed choices (enums) where possible.
4. Return **small, useful** results. Do not dump huge data into the context (topic `13`).

---

#### 4. Validate and Check Permissions — 🟢 Must Know

*Same rules as any API endpoint. The model is just another caller.*

1. **Validate** the arguments against the schema. The model can send wrong types or made-up values.
2. **Check permissions for the real user**, not for the model. If the user cannot read note 99, the tool must not return it (`BE 5`).
3. Do not let the model choose the user ID or account. Take it from the logged-in session.
4. Limit what a tool can touch (a folder, a table, a set of URLs).
5. Log every tool call with its arguments and result (topic `18`).

---

#### 5. Tools With Side Effects — 🟢 Must Know

*Reading is safe. Sending, deleting, and paying are not.*

1. Split tools into **read-only** (search, get) and **write** (create, delete, send, pay).
2. Ask the **user to confirm** before a write tool runs, especially if it cannot be undone.
3. Make write tools **idempotent**: retries or repeated calls must not duplicate the action. Use an idempotency key (`BE 3`).
4. Start an agent with read-only tools. Add write tools later, one at a time.

---

#### 6. Tool Errors — 🟡 Good to Know

*When a tool fails, tell the model clearly so it can recover.*

1. Tools fail: timeouts, "not found", bad arguments.
2. Return a **clear, short error message** to the model, such as "Note 99 not found. Use search_notes to find valid IDs."
3. The model can then fix its arguments or try another approach.
4. Do not hide errors, and do not return a raw stack trace.
5. Limit retries so it cannot loop forever (topic `10`).

---

#### 7. Parallel Tool Calls — 🟡 Good to Know

*Run independent tool calls at the same time.*

1. The model may request **several tool calls at once** when they are independent ("get weather in two cities").
2. Run them in parallel if you can, then return all results together.
3. Make sure each result is matched to the right call (by its ID).

---

#### 8. Provider-Hosted Tools — 🟡 Good to Know

*Some tools run on the provider side, not in your system.*

1. Some providers offer **built-in tools** that run on their side: web search, code execution, file search.
2. Easy to use, but you give up some control over data and cost. Check what data leaves your system.
3. Your own tools run in your system, with your rules.

---

#### 9. Keep the Tool Set Small — 🟡 Good to Know

*More tools does not mean better results.*

1. Every tool definition uses **context tokens** and is one more option to choose from.
2. Many similar tools confuse the model and cause wrong picks.
3. Prefer a few well-described tools. Merge overlapping ones. Load rarely used tools only when needed (topic `13`).

---

#### 10. Common Interview Questions

1. **How does function calling work?**
   You send the tools with the question. The model returns a tool request. Your code runs it and returns the result. The model then answers.
2. **Does the model execute the tool?**
   No. Your code does. That is where you enforce checks and limits.
3. **How do you make tool calls safe?**
   Validate arguments, check the real user's permissions, confirm risky actions, use idempotency, and log everything.
4. **What makes a good tool definition?**
   A clear name, a description that says when to use it, and a precise argument schema.
5. **What if a tool fails?**
   Return a short, clear error so the model can recover. Cap the retries.
6. **Why not give the model 50 tools?**
   Too many tools cost tokens and cause wrong choices. Keep the set small and focused.
7. **What is the difference between a tool and RAG?**
   RAG retrieves text for every question. A tool is chosen by the model when it needs something. Search can be a tool (agentic RAG).

---

#### 11. Common Mistakes

1. Letting the model pass the user ID or account.
2. Skipping validation because "the model will send valid input".
3. Write tools with no confirmation and no idempotency.
4. Vague descriptions, so the model picks the wrong tool.
5. Returning huge outputs that fill the context.
6. Hiding tool errors from the model.

---

#### 12. Related Topics

1. `05` Calling an LLM API
2. `07` RAG (agentic RAG)
3. `09` MCP & Integrations
4. `10` Agents
5. `16` Safety, Security & Privacy
6. `BE 3` API Design (idempotency)
7. `BE 5` Authentication & Authorization

---

#### 13. Interview Must Remember

1. **Model asks → your code runs → result goes back.**
2. **The model never runs anything.** Your code is the control point.
3. **Description is the key part** of a tool definition.
4. **Validate, authorize for the real user, log.**
5. **Confirm and make idempotent** anything with side effects.
6. **Few tools, small outputs, clear errors.**
