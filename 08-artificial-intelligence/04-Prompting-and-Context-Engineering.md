# Prompting & Context Engineering

Roadmap topic 4 · Stage 2: Build with LLMs

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** the model can only work with what you put in front of it. A prompt is your instruction. Context engineering is the bigger job: choosing all the information the model sees, so it has what it needs and nothing that gets in the way.

---

#### 1. Message Roles — 🟢 Must Know

*A conversation is a list of messages. Each has a role.*

| Role | Who writes it | What it is for |
|---|---|---|
| **System** | You (the developer) | Standing rules: role, tone, limits, output format |
| **User** | The user | The request or question |
| **Assistant** | The model | Earlier replies (part of the history you resend) |

```text
system:    You are a note-taking assistant. Answer briefly. Never invent notes.
user:      Summarize my notes about the Kotlin meetup.
assistant: (the model's reply)
user:      Make it three bullet points.
```

1. The **system prompt** is hidden from the user and sets behaviour for the whole conversation.
2. Put stable rules in the system prompt, and the changing request in the user message.
3. Do not treat the system prompt as a secret or a security barrier. Users may find ways to reveal or override it.

---

#### 2. Writing a Clear Prompt — 🟢 Must Know

*Say what you want, give the needed information, and describe the output.*

A good prompt has:

1. **Task** — what to do.
2. **Context** — the information needed to do it.
3. **Constraints** — what to avoid, length, tone, audience.
4. **Output format** — bullets, JSON, a table, a single word.

Weak vs better:

```text
Weak:   "Fix this."
Better: "Rewrite this error message for a mobile app user. Max 15 words.
         Friendly tone. No technical terms. Return only the message."
```

1. Be specific. Vague prompts get vague answers.
2. Say what to do, not only what not to do.
3. If the model may not know the answer, say what to do then ("reply: NOT_FOUND").

---

#### 3. Zero-Shot vs Few-Shot — 🟢 Must Know

*Show, don't only tell.*

1. **Zero-shot** — you give instructions only.
2. **Few-shot** — you also give a few examples of input and the output you want.
3. Examples fix format and edge cases better than long explanations.

```text
Classify the message as BUG, QUESTION, or PRAISE.

"App crashes on launch"      → BUG
"How do I export my notes?"  → QUESTION
"Love the new dark mode"     → PRAISE

"Login button does nothing"  →
```

Use 2 to 5 varied examples. Include a tricky case.

---

#### 4. Context Engineering — 🟢 Must Know

*Choose what goes into the context window, not just how the prompt is worded.*

Everything the model sees is context:

```text
System prompt · Tool definitions · Retrieved documents · Examples
Conversation history · Tool results · The user's request
```

1. The goal: give the **smallest set of information** that lets the model do the job well.
2. **Too little** — the model guesses and hallucinates.
3. **Too much** — cost and latency rise, and the important part gets lost.
4. Decide for each request: what does the model need to see, and what can be left out?
5. Ways to control it: retrieve only relevant documents (RAG), summarize old history, shorten big tool outputs, load tools only when needed (topic `13`).

**Simple test:** if a new colleague got the same text, could they do the task? If not, the model cannot either.

---

#### 5. Prompts Are Code — 🟢 Must Know

*A small prompt change can break behaviour. Treat prompts like code.*

1. Keep prompts in the repository, not typed into a dashboard.
2. **Version** them and review changes.
3. **Test** them with a set of example inputs (evals, topic `15`) before and after any change.
4. Record which prompt version produced which output (topic `18`).
5. Do not edit a live prompt without running the tests.

---

#### 6. Step-by-Step Prompting — 🟡 Good to Know

*Asking the model to work through a problem in steps, and when it helps.*

1. For multi-step problems, asking the model to reason step by step (or write its plan first) can improve results.
2. **Reasoning models** already do this internally, so they need less of this kind of prompt (topic `03`).
3. For a simple task, extra reasoning only adds cost and delay.

---

#### 7. Structuring the Prompt — 🟡 Good to Know

*Label the parts of a prompt so instructions and data do not mix.*

1. **Label the parts** so the model can tell instructions from data, using clear headings or tags:

```text
<instructions> Summarize the note in one sentence. </instructions>
<note> ...user's text... </note>
```

2. This also helps against **prompt injection**: text inside the data block is data, not instructions (topic `16`). It does not fully solve it.
3. Use **templates with variables** so the same prompt is reused with different inputs.
4. Put long documents first and the question last, or as the model's docs recommend.

---

#### 8. Common Interview Questions

1. **What is the difference between a system prompt and a user prompt?**
   The system prompt holds the developer's standing rules. The user prompt is the request for this turn.
2. **What makes a good prompt?**
   A clear task, the needed context, constraints, and an output format. Examples help.
3. **Zero-shot vs few-shot?**
   Zero-shot gives instructions only. Few-shot adds examples to fix format and edge cases.
4. **What is context engineering?**
   Choosing what information goes into the context window: instructions, data, tools, and history, so the model has what it needs and no noise.
5. **How do you manage prompts in a real project?**
   Store in the repo, version them, and run evals on every change.
6. **Why not just put everything in the prompt?**
   Cost, latency, and quality all get worse. Important details get lost in long context.
7. **Is the system prompt secure?**
   No. Do not put secrets in it, and do not rely on it as the only safety control.

---

#### 9. Common Mistakes

1. Vague instructions.
2. Contradicting rules in the same prompt.
3. Pasting whole documents when a few paragraphs are enough.
4. Editing prompts in production with no tests.
5. Putting secrets or API keys in the prompt.
6. Mixing user-supplied text into instructions with no separation.

---

#### 10. Related Topics

1. `02` How LLMs Work (context window)
2. `05` Calling an LLM API
3. `07` RAG
4. `13` Memory & Context Management
5. `15` Evaluation & Quality
6. `16` Safety, Security & Privacy

---

#### 11. Interview Must Remember

1. **Roles:** system (rules), user (request), assistant (history).
2. **Clear prompt = task + context + constraints + format.**
3. **Few-shot examples** fix format and edge cases.
4. **Context engineering** = the right information, the smallest set.
5. **Prompts are code:** version and test them.
6. The system prompt is **not** a security boundary.
