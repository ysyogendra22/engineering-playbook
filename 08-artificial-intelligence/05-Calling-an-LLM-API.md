# Calling an LLM API

Roadmap topic 5 · Stage 2: Build with LLMs

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** an LLM is called like any other web API: send a request, get a response. The differences are that it is slow, it is paid per token, it can stream its answer, and the model remembers nothing, so you send the history each time.

---

#### 1. Request and Response — 🟢 Must Know

*A list of messages goes in. A message and a token count come out.*

Request (shape, not a real provider format):

```json
{
  "model": "some-model-name",
  "system": "You are a note-taking assistant.",
  "messages": [
    { "role": "user", "content": "Summarize my meeting notes." }
  ],
  "max_tokens": 300,
  "temperature": 0.2
}
```

Response (shape):

```json
{
  "content": "Here is a summary ...",
  "stop_reason": "end_of_turn",
  "usage": { "input_tokens": 420, "output_tokens": 95 }
}
```

1. You choose the **model**, the **messages**, and settings such as `max_tokens` and `temperature`.
2. The response has the **content**, the **stop reason** (finished, hit the length limit, or wants to call a tool), and **token usage**.
3. **Log the usage.** It is your cost and your latency (topic `18`).
4. Field names differ by provider, but the idea is the same.

---

#### 2. Streaming — 🟢 Must Know

*Show the answer as it is written, instead of waiting for all of it.*

1. Without streaming, the user waits for the whole answer. For long answers, that is many seconds.
2. With **streaming**, the server sends tokens as they are produced, usually as **server-sent events** (`SD 24`).
3. **Time to first token (TTFT)** is what the user feels. Streaming makes it short.
4. Total time and cost stay about the same. The app just feels faster.

```text
Without streaming:  [ ........ wait 8 s ........ ] full answer
With streaming:     [ 0.6 s ] "Here" "is" "a" "summary" ...
```

**Mobile view:** consume the stream like a `Flow` (Kotlin) or an `AsyncSequence` (Swift) and append text to the UI. Handle cancel and network drops (topic `20`).

---

#### 3. Structured Output — 🟢 Must Know

*When code will use the answer, ask for a fixed format and check it.*

1. Ask for **JSON that matches a schema**, or use the provider's structured-output feature.
2. **Always validate** the result in your code. Never assume it is correct.
3. If it is invalid: retry once with the error message, or fall back.
4. Keep the schema simple. Use fixed choices (enums) where you can.

```text
Extract: { "title": string, "due_date": "YYYY-MM-DD" | null, "priority": "low"|"med"|"high" }
```

Free-form text is for people. Structured output is for programs.

---

#### 4. Conversation State and Context Limits — 🟢 Must Know

*The model remembers nothing. You resend the history, and it must fit.*

1. Each request must include the earlier messages the model needs.
2. History grows with every turn, so cost and latency grow too.
3. When it gets long, **truncate** (drop the oldest) or **summarize** older turns (topic `13`).
4. Store the conversation in **your** database, not only in memory (`BE 8`).
5. Keep the system prompt and key facts. Cut the least useful messages first.

---

#### 5. Keep the API Key on Your Server — 🟢 Must Know

*A key inside the app can be extracted. Then anyone can spend your money.*

```text
Mobile app  →  Your backend  →  LLM provider
             (auth, limits,     (holds the API key)
              logging, cost)
```

1. **Never** ship a provider API key in the app. Decompiling an APK or IPA can reveal it.
2. The app calls **your backend**. The backend adds the key, checks who the user is, applies limits, and calls the provider.
3. This also lets you log, cache, filter, and switch providers without an app update.

---

#### 6. Rate Limits, Timeouts, Retries — 🟢 Must Know

*Same rules as any external service (`SD 22`), with slower calls.*

1. **Rate limit (`429`)** — you are sending too much. Wait, then retry.
2. Retry **transient** errors (`429`, `5xx`, timeouts) with **exponential backoff and jitter**. Do not retry `400`-style errors (your request is wrong).
3. LLM calls are slow. Set a **timeout that fits** (streaming helps), and always have one.
4. Add a **fallback**: a second model, a cached answer, or a clear error message (topic `17`).
5. Limit **concurrency** so a spike does not trigger the provider's limits.
6. Retrying a request that triggers actions (tool calls that send email) needs **idempotency** (`BE 3`).

---

#### 7. Prompt Caching and Batch APIs — 🟡 Good to Know

*Two ways to pay less: reuse a repeated prompt start, or run work in bulk later.*

1. **Prompt caching** — if the start of your prompt is the same each time (system prompt, tool definitions, a long document), the provider can reuse the work. It is cheaper and faster. Put the **stable part first** and the changing part last.
2. **Batch APIs** — send many requests to be processed later, usually at a lower price. Good for offline jobs (tagging thousands of notes overnight). Not for live chat.

---

#### 8. Model Routing — 🟡 Good to Know

*Send easy requests to a small model and hard ones to a large model.*

1. Send **easy** requests to a small, cheap model and **hard** ones to a large model.
2. A simple router: rules (length, type of task) or a small classifier model.
3. Test that quality holds on the easy path (topic `15`).

---

#### 9. Output Length and Stop Sequences — 🟡 Good to Know

*Cap the answer length, and know when it was cut off.*

1. **`max_tokens`** caps the answer length. Set it. It limits cost, and stops runaway answers.
2. If the stop reason says "length", the answer was **cut off**. Handle that case.
3. **Stop sequences** are strings that make the model stop when it writes them. Useful for formats with a clear end marker.

---

#### 10. Common Interview Questions

1. **How do you call an LLM from a mobile app?**
   The app calls your backend, and the backend calls the LLM with the key. Never put the key in the app.
2. **How do you make a chat feel fast?**
   Stream the answer, so the first words appear quickly.
3. **The model has no memory. How does a chat work?**
   The backend stores the conversation and sends the needed history with each request.
4. **What if the history gets too long?**
   Truncate old messages or summarize them, keeping the system prompt and key facts.
5. **How do you get reliable JSON from a model?**
   Ask for a schema, use structured output, validate in code, and retry or fall back on failure.
6. **How do you handle rate limits and failures?**
   Retry transient errors with backoff and jitter, set timeouts, limit concurrency, and add a fallback.
7. **How do you reduce cost on repeated prompts?**
   Prompt caching, response caching, shorter prompts, and a smaller model for easy tasks.

---

#### 11. Common Mistakes

1. API key inside the mobile app.
2. No timeout, or no `max_tokens`.
3. Trusting model JSON without validation.
4. Resending the entire history forever.
5. Retrying non-transient errors, or retrying without backoff.
6. Not logging token usage.

---

#### 12. Related Topics

1. `02` How LLMs Work
2. `04` Prompting & Context Engineering
3. `13` Memory & Context Management
4. `17` Cost, Latency & Reliability
5. `20` AI Features in the App
6. `SD 22` Reliable Requests & External Services
7. `SD 24` Real-Time Communication & Push (streaming)

---

#### 13. Interview Must Remember

1. **Key on the server**, never in the app.
2. **Stream** for perceived speed. Watch **time to first token**.
3. **Stateless model:** you resend history. Trim or summarize.
4. **Validate** structured output.
5. **Backoff + jitter + timeout + fallback.**
6. **Log tokens.** They are your cost and latency.
