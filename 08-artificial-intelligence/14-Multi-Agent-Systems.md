# Multi-Agent Systems

Roadmap topic 14 · Stage 3: Tools & Agents

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** sometimes one agent hands parts of a job to other agents. A lead agent splits the work, helper agents do the parts and report back. It can keep the main context clean and speed up independent work, but it costs more and is harder to debug. Use it only when one agent is not enough.

---

#### 1. One Agent Is Usually Enough — 🟢 Must Know (New)

*Add agents only for a clear reason.*

1. A single agent with good tools and prompts solves most problems.
2. Multi-agent systems add cost (more model calls and tokens), complexity, and more ways to fail.
3. Consider splitting only when:
   - the context gets too big for one agent,
   - there are **independent** subtasks that can run in parallel,
   - different parts need **different tools, rules, or permissions**.

**Mobile view:** like splitting one huge screen into several components or modules. Do it when the size or the responsibilities demand it, not by default.

---

#### 2. Orchestrator–Worker — 🟢 Must Know (New)

*A lead agent plans and delegates. Workers do the parts.*

```text
User goal → Orchestrator (lead agent)
                ├─→ Worker A: research topic 1 ─┐
                ├─→ Worker B: research topic 2 ─┼→ short results
                └─→ Worker C: check sources   ─┘
            Orchestrator combines results → final answer
```

1. The **orchestrator** breaks the goal into subtasks, assigns them, and merges the results.
2. **Workers (subagents)** focus on one subtask with their own instructions and tools.
3. This is the same pattern as in topic `10`, with each worker being an agent instead of a single LLM call.

---

#### 3. Subagents Keep the Main Context Clean — 🟢 Must Know (New)

*A subagent works in its own window and returns a short result.*

1. A **subagent** has its **own context**. It can read many files or pages without filling the main agent's window.
2. It returns only a **short summary or answer** to the lead agent.
3. This is the biggest practical benefit: side work does not pollute the main context (topic `13`).
4. Give the subagent a **clear task, the needed context, and the expected output format**. It does not see the main conversation unless you pass it.

---

#### 4. Parallel Agents — 🟡 Good to Know

*Independent work can run at the same time, for more cost.*

1. Independent subtasks can run **at the same time**, reducing total time.
2. Cost is higher: each agent uses its own tokens.
3. Do not parallelize steps that depend on each other.
4. Limit concurrency so you do not hit rate limits (topic `17`).

---

#### 5. Handoffs and Routers — 🟡 Good to Know

*Send each request to the right specialist agent.*

1. **Router** — classifies a request and sends it to the right specialised agent (billing, tech support).
2. **Handoff** — one agent passes the conversation to another, with the needed context and history.
3. Specialised agents can have their **own tools and permissions**, so each one has less access (least privilege, topic `16`).

---

#### 6. Shared State and Coordination — 🟡 Good to Know

*How agents share results without stepping on each other.*

1. Agents need to share results: a shared file, a database, or messages via the orchestrator.
2. **Conflicts** — two agents editing the same file or record. Assign clear ownership, or run them one after another.
3. Keep the shared state simple and visible, so you can debug it.

---

#### 7. Failure Handling — 🟡 Good to Know

*More agents means more ways to fail. Plan for it.*

1. One worker can fail, time out, or return junk.
2. The orchestrator decides: **retry**, **skip and note it**, or **report** the gap to the user.
3. Apply limits at every level: steps, time, and cost per agent and for the whole run.
4. Errors multiply: more agents, more chances that something goes wrong.

---

#### 8. Agent-to-Agent Protocols — 🟡 Good to Know

*Not the same as MCP. Name only.*

1. **A2A** is a protocol for agents to talk to other agents, possibly built by different teams or vendors.
2. Different from MCP, which connects an agent to tools and data (topic `09`).
3. Name only for interviews.

---

#### 9. Common Interview Questions

1. **When would you use multiple agents?**
   When the context is too large for one agent, subtasks are independent and parallel, or parts need different tools and permissions.
2. **What is the orchestrator–worker pattern?**
   A lead agent splits the task, delegates to worker agents, and combines their results.
3. **What is the benefit of subagents?**
   Each has its own context window, so side work does not fill the main agent's context, and it returns a short result.
4. **What are the downsides?**
   More tokens and cost, more complexity, harder debugging, and more failure points.
5. **How do you handle a worker failing?**
   Retry, skip with a note, or report it, with limits at every level.
6. **How do agents share information?**
   Through the orchestrator's messages or shared storage, with clear ownership to avoid conflicts.
7. **How is multi-agent different from a workflow?**
   In a workflow, code fixes the steps. In multi-agent systems, agents decide their own steps, and the lead agent decides how to split work.

---

#### 10. Common Mistakes

1. Using many agents for a task one agent handles well.
2. Giving subagents no context or no output format.
3. Parallelizing dependent steps.
4. No limits per agent or for the whole run.
5. Two agents changing the same thing.
6. Not tracing each agent, so failures are invisible (topic `18`).

---

#### 11. Related Topics

1. `09` MCP & Integrations (A2A)
2. `10` Agents
3. `11` Agent Harness
4. `13` Memory & Context Management
5. `17` Cost, Latency & Reliability
6. `18` Observability & LLMOps

---

#### 12. Interview Must Remember

1. **One agent first.** Split only for a clear reason.
2. **Orchestrator–worker:** lead splits, workers do, lead combines.
3. **Subagents = own context, short result back.**
4. **Parallel** only for independent work.
5. **Costs and failures multiply.** Limit and trace every agent.
6. **A2A** = agent to agent. **MCP** = tools and data.
