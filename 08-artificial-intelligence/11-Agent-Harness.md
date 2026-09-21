# Agent Harness

Roadmap topic 11 · Stage 3: Tools & Agents

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** the model alone only writes text. The harness is all the code around it that turns it into a working agent: it builds the prompt, calls the model, runs the tools, manages the context, and enforces the rules. **Model + harness = agent.** A good harness matters as much as a good model.

---

#### 1. What Is a Harness — 🟢 Must Know (New)

*The model is the engine. The harness is the rest of the car.*

1. The **harness** (also called scaffolding or the agent runtime) is everything except the model.
2. It runs the agent loop (topic `10`) and decides what the model sees and what it may do.
3. Examples: a coding assistant in your terminal or IDE, an agent SDK, or a loop you write yourself.

**Mobile view:** like the Android or iOS framework around your app code. Your code (the model) does the thinking. The framework handles lifecycle, permissions, threads, and resources.

---

#### 2. What It Does Each Turn — 🟢 Must Know (New)

*One turn of the loop.*

```text
Build the prompt (system prompt + tool list + history + new input)
        ↓
Call the model
        ↓
Reply has a tool call?  ── no ──→  show the final answer, done
        │ yes
        ↓
Check permissions  →  run the tool (in a sandbox)  →  get the result
        ↓
Add the result to the history, trim the context if needed
        ↓
Check limits (steps, cost, time)  →  next turn
```

---

#### 3. What the Harness Supplies — 🟢 Must Know (New)

*The harness decides everything the model sees.*

1. **System prompt** — the rules, role, and how to behave.
2. **Tool definitions** — the list of tools and their schemas (topic `08`).
3. **Loop rules** — when to stop, how to handle errors, what to do on limits.
4. **Environment** — where the tools run (a folder, a project, an account).

The model only sees what the harness chooses to show it.

---

#### 4. Context Management — 🟢 Must Know (New)

*The harness decides what stays in the window (topic `13`).*

1. The context fills as tool results pile up.
2. **Trim** — cut old or large outputs.
3. **Compaction** — summarize older turns into a short note and continue.
4. **Load on demand** — read a file or fetch a record only when needed, instead of loading everything.
5. Keep the goal, the rules, and key facts safe from being trimmed.

---

#### 5. Permissions — 🟢 Must Know (New)

*Which actions run alone, which need approval, which are never allowed.*

| Rule | Meaning | Example |
|---|---|---|
| **Allow** | Runs without asking | Read a file, search notes |
| **Ask** | Needs the user's approval | Edit a file, send an email |
| **Deny** | Never allowed | Delete the production database |

1. Decide per tool and per action, not once for everything.
2. Show the user what will happen before approval.
3. Remember choices carefully. "Always allow" should be narrow.

**Mobile view:** the same idea as Android runtime permissions and iOS permission prompts.

---

#### 6. Sandboxing — 🟢 Must Know (New)

*Run tools where they cannot do much harm.*

1. A **sandbox** is a restricted environment: limited files, limited network, limited time and memory.
2. It reduces the damage of a bad command, a bug, or a prompt-injection attack.
3. Examples: a container, a temporary folder, a restricted user account.
4. Permissions decide **whether** to run. The sandbox limits **what** can go wrong when it runs.

**Mobile view:** like the app sandbox: an app can only touch its own files.

---

#### 7. Limits and Errors — 🟢 Must Know (New)

*Keep every run bounded and recoverable.*

1. **Max turns**, **max cost**, and **timeout** for each run.
2. **Retries** for transient model and tool errors (`SD 22`).
3. **Cancellation** — the user can stop a run cleanly.
4. **Tool errors** go back to the model as short messages, so it can adjust.
5. **Repeat detection** — stop identical calls that keep repeating.

---

#### 8. Hooks — 🟡 Good to Know

*Your code that runs automatically at set points in the loop.*

1. A **hook** is a rule like "before any tool runs, do X" or "after a file is edited, run the formatter".
2. Typical points: session start, before a tool call, after a tool call, when the agent stops.
3. Uses: block dangerous commands, add logging, run checks, inject extra context.
4. Unlike a prompt instruction, a hook runs **every time**. The model cannot forget or skip it.

**Mobile view:** like lifecycle callbacks (`onStart`, `viewWillAppear`), or interceptors in OkHttp.

---

#### 9. Skills — 🟡 Good to Know (New)

*Instructions the agent loads only when they are needed.*

1. A **skill** is a packaged set of instructions, and sometimes scripts and files, for one kind of task ("write a release note", "review an API").
2. The agent sees a short description of each skill and **loads the full text only when it is relevant**.
3. This keeps the context small while giving the agent many abilities.

---

#### 10. Project Instruction Files — 🟡 Good to Know (New)

*Standing rules that load at the start, so you do not repeat them.*

1. A file in the project (for example `CLAUDE.md` or `AGENTS.md`) holds standing rules: how to build, test, code style, things to avoid.
2. The harness loads it at the start of a session, so you do not repeat yourself.
3. Keep it short and specific. Long files waste context.

---

#### 11. Sessions, Checkpoints, Subagents, Modes — 🟡 Good to Know

*Smaller pieces that make long work safer and easier to manage.*

1. **Session** — a saved conversation and state, so you can continue later.
2. **Checkpoint** — a saved point you can go back to if the agent goes wrong (for example, before edits).
3. **Subagents** — helper agents with their own context (topic `14`).
4. **Permission modes** — for example "plan only" (no changes), "ask for edits", or "auto-approve". Choose the mode by risk.

---

#### 12. Why the Harness Matters — 🟡 Good to Know

*The model is only half of the result.*

1. The **same model** in a different harness gives very different results.
2. Better results often come from better tools, better context handling, and better feedback (tests, checks), not a bigger model.
3. When an agent misbehaves, look at the harness first: the tool descriptions, the context, the limits, and the permissions.
4. Building your own loop once (topic `12`) teaches how all harnesses work.

---

#### 13. Common Interview Questions

1. **What is an agent harness?**
   The code around the model that runs the loop, builds the prompt, executes tools, manages context, and enforces permissions and limits. Model plus harness equals agent.
2. **What does a harness do on each turn?**
   Builds the prompt, calls the model, runs any requested tool after permission checks, adds the result, trims the context, and checks the limits.
3. **How do permissions and sandboxes differ?**
   Permissions decide whether an action is allowed to run. A sandbox limits the damage it can do when it does.
4. **What are hooks?**
   Code that runs automatically at set points, such as before a tool call. They are enforced every time, unlike instructions in a prompt.
5. **How do you handle a long task filling the context?**
   Trim tool outputs, compact old turns, load data on demand, and keep the goal and rules protected.
6. **What are skills and instruction files?**
   Skills are packaged instructions loaded when relevant. Instruction files hold standing project rules loaded at the start.
7. **Why can two agents with the same model perform differently?**
   Different harnesses: tools, context handling, feedback, and limits.

---

#### 14. Common Mistakes

1. Blaming the model when the harness (tools, context) is the problem.
2. No permission model: every tool allowed.
3. Running tools with no sandbox.
4. Enforcing important rules only in the prompt, not with hooks or code.
5. Never trimming the context.
6. No step, cost, or time limits.

---

#### 15. Related Topics

1. `08` Tool Use & Function Calling
2. `10` Agents
3. `12` Building an Agent
4. `13` Memory & Context Management
5. `14` Multi-Agent Systems
6. `16` Safety, Security & Privacy
7. `SD 22` Reliable Requests & External Services

---

#### 16. Interview Must Remember

1. **Model + harness = agent.**
2. **Turn:** build prompt → model → permission check → run tool → add result → trim → limits.
3. **Permissions** = may it run. **Sandbox** = limit the damage.
4. **Hooks** run every time. Prompts are only advice.
5. **Skills** and **instruction files** load context only when needed.
6. **Harness design** often matters more than model size.
