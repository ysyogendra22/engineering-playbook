# Agents

Roadmap topic 10 · Stage 3: Tools & Agents

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** a normal LLM call answers once. An agent is a model that can use tools in a loop: it decides a step, acts, looks at the result, and continues until the job is done. The most useful skill is knowing when you do not need an agent.

---

#### 1. What Is an Agent — 🟢 Must Know

*A model, some tools, and a loop that works toward a goal.*

1. An **agent** = **model + tools + a loop**, aimed at a goal.
2. The model chooses the next step. The tools let it read and change things. The loop lets it keep going.
3. Example goal: "Find my notes about the release, and add a summary note." The agent searches, reads, then creates a note.

| | Single LLM call | Agent |
|---|---|---|
| Steps | One | Many, decided as it goes |
| Tools | Usually none | Yes |
| Predictable | High | Lower |
| Cost and time | Low | Higher |

---

#### 2. The Agent Loop — 🟢 Must Know

*Think, act, observe, repeat.*

```text
        ┌────────────────────────────────────┐
        ↓                                    │
   Model thinks  →  calls a tool  →  gets the result
        │
        └── if no more tools needed → final answer
```

1. **Think** — the model looks at the goal and everything so far.
2. **Act** — it requests a tool call (topic `08`).
3. **Observe** — your code runs the tool and adds the result to the context.
4. **Repeat** until the model gives a final answer, or a limit is reached.
5. The loop code around the model is part of the harness (topic `11`).

---

#### 3. Workflow vs Agent — 🟢 Must Know

*Who decides the steps: your code, or the model?*

| | Workflow | Agent |
|---|---|---|
| Steps decided by | Your code (fixed path) | The model (at run time) |
| Predictable | Yes | Less |
| Cost, latency | Lower | Higher |
| Best for | Known, repeatable tasks | Open-ended tasks where steps are not known in advance |

1. **Prefer the simplest thing that works:** one prompt, then a workflow, then an agent.
2. Many "agents" in real products are really workflows with a few LLM calls.
3. Use an agent only when the number and order of steps truly cannot be known ahead.

---

#### 4. Workflow Patterns — 🟢 Must Know

*Five common shapes. Know the names and one example each.*

| Pattern | What it does | Example |
|---|---|---|
| **Prompt chaining** | Step 1's output feeds step 2 | Write an outline, then write the article from it |
| **Routing** | Classify the input, send it to the right handler | Billing question → billing prompt; bug report → bug prompt |
| **Parallelization** | Run independent steps at the same time, then combine | Check a document for three kinds of problems in parallel |
| **Orchestrator–workers** | A lead model splits the task and hands parts to workers | Changing several files in a codebase |
| **Evaluator–optimizer** | One model writes, another critiques, repeat | Draft a translation, review it, improve it |

---

#### 5. Stop Conditions — 🟢 Must Know

*An agent that cannot stop is a bug and a bill.*

Always set:

1. **Goal reached** — the model gives a final answer.
2. **Max steps** — for example 10 tool calls.
3. **Max cost or tokens** — a budget per run.
4. **Timeout** — a total time limit.
5. **Repeat detection** — stop if it calls the same tool with the same arguments again and again.
6. **User cancel** — let the user stop it.

When a limit hits, report clearly what was done and what is left.

---

#### 6. Human-in-the-Loop — 🟢 Must Know

*A person approves the steps that matter.*

1. **Ask before** actions that are irreversible, costly, or visible to others: send, delete, pay, publish.
2. Show what the agent is about to do, in plain words, and let the user approve, edit, or refuse.
3. Read-only steps can usually run without asking.
4. This is the best cheap safety control (topic `16`).

---

#### 7. Planning and ReAct — 🟡 Good to Know

*Two ways to help an agent handle longer tasks.*

1. **Planning** — the agent writes a short plan first, then follows and updates it. Helps on long tasks.
2. **ReAct** (reason + act) — a pattern where the model alternates a short thought with an action and an observation. It is the basic shape of the agent loop.
3. Reasoning models do some planning internally (topic `03`).

---

#### 8. Reflection — 🟡 Good to Know

*The agent checks its own work before finishing.*

1. The agent **checks its own work**: "Does this answer the question? Are the numbers right?"
2. Better still: check with **code or tests**, not only with the model's opinion (for example, run the unit tests).
3. It adds cost. Use it where mistakes are expensive.

---

#### 9. Why Agents Fail — 🟡 Good to Know

*Know the usual failures so you can design against them.*

1. **Loops** — repeats the same step.
2. **Wrong tool or wrong arguments.**
3. **Losing the goal** — long tasks fill the context and it drifts (topic `13`).
4. **Small errors add up** — 90% right at each of 10 steps is only about 35% right overall.
5. **Bad tool results** — an error the model misreads.
6. **Injected instructions** in content it reads (topic `16`).

Fixes: fewer tools, better descriptions, step limits, checkpoints, tests, and evals of full runs (topic `15`).

---

#### 10. Levels of Autonomy — 🟡 Good to Know

*How much the agent may do without asking.*

| Level | Behaviour | Use when |
|---|---|---|
| Suggest | The agent proposes, the human does | Early stage, high risk |
| Ask first | The agent acts after approval | Most real products |
| Act alone | The agent acts, humans review later | Low risk, reversible, well tested |

Start low. Raise autonomy only as the evals and the track record justify it.

---

#### 11. Coding and Computer-Use Agents (New) — 🟡 Good to Know

*Two popular kinds of agents, and why they need strong limits.*

1. **Coding agents** — read a codebase, edit files, run tests and commands, and iterate. The test results give a strong feedback signal.
2. **Computer-use / browser agents** — look at screenshots and operate a UI by clicking and typing. Powerful, but slower and less reliable, and risky with real accounts.
3. Both need strong permissions and sandboxing (topic `11`).

---

#### 12. Common Interview Questions

1. **What is an agent?**
   A model with tools and a loop that works toward a goal: think, act, observe, repeat.
2. **Agent vs workflow?**
   In a workflow, code decides the steps. In an agent, the model decides. Prefer workflows when steps are known.
3. **When would you not use an agent?**
   When a single prompt or a fixed workflow works. Agents cost more, are slower, and are less predictable.
4. **What workflow patterns do you know?**
   Prompt chaining, routing, parallelization, orchestrator–workers, and evaluator–optimizer.
5. **How do you stop an agent going wrong?**
   Step, cost, and time limits, repeat detection, human approval for risky actions, and testing.
6. **Why do agents fail on long tasks?**
   The context fills and it loses the goal, errors compound, and it may loop or choose wrong tools.
7. **How much autonomy would you give it?**
   Start with ask-first. Increase only for low-risk, reversible actions that are well evaluated.

---

#### 13. Common Mistakes

1. Building an agent when a workflow would do.
2. No step, cost, or time limit.
3. Giving write tools before the read-only version works.
4. No human approval for risky actions.
5. Judging the agent only by its final answer, not the steps it took.
6. Too many tools.

---

#### 14. Related Topics

1. `08` Tool Use & Function Calling
2. `11` Agent Harness
3. `12` Building an Agent
4. `13` Memory & Context Management
5. `14` Multi-Agent Systems
6. `15` Evaluation & Quality
7. `16` Safety, Security & Privacy

---

#### 15. Interview Must Remember

1. **Agent = model + tools + loop.**
2. **Loop:** think → act → observe → repeat.
3. **Simplest first:** prompt → workflow → agent.
4. **Patterns:** chaining, routing, parallelization, orchestrator–workers, evaluator–optimizer.
5. **Always set limits:** steps, cost, time.
6. **Human approval** for risky actions.
