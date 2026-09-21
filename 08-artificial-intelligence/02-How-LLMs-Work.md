# How LLMs Work

Roadmap topic 2 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** an LLM reads text as small pieces called tokens and predicts what token should come next, one at a time. It knows nothing beyond its training and what you put in front of it right now. Almost every design choice in an AI app comes from these two facts.

---

#### 1. Tokens and Tokenization — 🟢 Must Know

*The model does not read letters or words. It reads tokens.*

1. **Tokenization** — splitting text into small pieces before the model sees it.
2. A **token** can be a whole word, part of a word, or a punctuation mark.
3. Rough rule for English: 1 token is about ¾ of a word. 100 words is about 130 tokens. Code and other languages often use more tokens.
4. **Everything is counted in tokens:** the size limit, the speed, and the price.

```text
"Unbelievable news!"  →  [ Un ] [ believ ] [ able ] [ news ] [ ! ]
```

**Mobile view:** think of tokens as the "bytes" of an LLM. You measure limits and cost in them, not in characters.

---

#### 2. Context Window — 🟢 Must Know

*The context window is the model's whiteboard. If it is full, something must be erased.*

1. The **context window** is the maximum number of tokens the model can consider at once.
2. It holds **everything**: system prompt, chat history, documents you added, tool definitions, and the answer being written.
3. If you go over the limit, the request fails or old content must be cut.
4. A bigger window helps, but it costs more and can make answers slower.

```text
| system prompt | history | documents | your question | ← answer grows here |
|<------------------ must fit inside the context window ------------------>|
```

---

#### 3. Next-Token Prediction — 🟢 Must Know

*The model writes one token at a time, each based on all the tokens before it.*

1. Given the text so far, the model scores every possible next token, picks one, adds it, and repeats.
2. It is not looking up facts. It is producing the most likely continuation.
3. This is why long answers take time, and why answers can be **streamed** token by token (topic `05`).

```text
"The capital of France is"  →  " Paris"  →  "."  →  (stop)
```

---

#### 4. Temperature, Top-K, Top-P — 🟢 Must Know

*Dials that control how random the next-token choice is.*

1. **Temperature** — low means predictable and focused. High means varied and creative.
2. **Top-K** — pick only from the K most likely tokens.
3. **Top-P** — pick from the smallest group of tokens whose probabilities add up to P (for example 0.9).
4. Rules of thumb: low temperature for extraction, classification, and tool use. Higher for brainstorming and creative writing.
5. Even at low temperature, results are not guaranteed to be identical every time.

---

#### 5. The Model Is Stateless — 🟢 Must Know

*The model remembers nothing between calls. You send the history every time.*

1. Each API call is independent. "Memory" in a chat app is your app sending the earlier messages again.
2. If it is not in the context, the model does not know it.
3. This is why history grows, cost grows, and you must trim or summarize (topics `05` and `13`).

**Mobile view:** like a stateless server (`BE 1`). The "session" lives in your app or backend, not in the model.

---

#### 6. Knowledge Cutoff — 🟢 Must Know

*The model only knows what was in its training data, up to a date.*

1. It does not know events after its **knowledge cutoff**.
2. It does not know your private data: your users, your documents, your database.
3. Fix: put the needed information in the context (prompt, RAG, or a tool that fetches it).

---

#### 7. Hallucination — 🟢 Must Know

*The model produces text that sounds right. It does not check that it is right.*

1. **Hallucination** — a confident answer that is wrong or made up (fake facts, fake links, fake function names).
2. Why: it predicts likely text. Nothing inside checks the facts.
3. It happens more when the model lacks the information, or when the question is vague.

What reduces it:

1. **Give sources** in the prompt (RAG, topic `07`) and tell it to answer only from them.
2. Allow **"I don't know"** as a valid answer.
3. Use **tools** for facts and calculations (topic `08`).
4. **Check the output** with code or a second step (validate JSON, verify a citation exists).
5. Keep temperature low for factual tasks.

It cannot be fully removed. Design for it.

---

#### 8. Transformers and Attention — 🟡 Good to Know

*The design behind modern LLMs. Idea only.*

1. A **transformer** is the neural network design used by most LLMs.
2. **Attention** lets each token look at other tokens in the input to decide which ones matter for it. This is how the model connects "it" to the right noun.
3. It processes the whole input in parallel, which made training on huge data practical.
4. For interviews, this one paragraph is enough. No math is needed.

---

#### 9. Non-Determinism and Long Context — 🟡 Good to Know

*The same prompt can give different answers, and very long prompts can hurt quality.*

1. The same prompt can give different answers, because the next token is chosen with some randomness.
2. For tests and pipelines, do not depend on exact wording. Validate the structure or key facts instead.
3. Very long context can lower quality: the model may miss or mix up details buried in a huge prompt. It also costs more and is slower.
4. Prefer sending the **right** information, not **all** the information (topic `04`).

---

#### 10. Common Interview Questions

1. **How does an LLM generate text?**
   It predicts the next token from all previous tokens, adds it, and repeats.
2. **What is a token and why does it matter?**
   A piece of text. Limits, latency, and cost are all measured in tokens.
3. **What is a context window?**
   The maximum tokens the model can consider at once, including prompt, history, and output.
4. **Why does the model "forget" between messages?**
   It is stateless. Your app must resend the history each time.
5. **What is hallucination and how do you reduce it?**
   Confident but wrong text. Reduce with sources (RAG), tools, "I don't know" instructions, validation, and low temperature.
6. **What does temperature do?**
   It controls randomness. Low for factual and structured tasks, higher for creative ones.
7. **Why can't an LLM answer questions about my private data or last week's news?**
   It was not trained on them. You must supply that information in the context.

---

#### 11. Common Mistakes

1. Assuming the model remembers earlier calls.
2. Trusting confident answers without checks.
3. Ignoring token counts until the bill or the limit hits.
4. Filling the context with everything "just in case".
5. Expecting identical output every run.
6. Asking about recent or private facts without providing them.

---

#### 12. Related Topics

1. `01` AI Landscape & ML Basics
2. `03` Training, Fine-Tuning & Model Choice
3. `04` Prompting & Context Engineering
4. `05` Calling an LLM API
5. `07` RAG
6. `13` Memory & Context Management

---

#### 13. Interview Must Remember

1. **Tokens** are the unit of everything: limits, speed, cost.
2. The model **predicts the next token**. It does not look up facts.
3. **Context window** = everything must fit: prompt, history, documents, answer.
4. **Stateless:** you resend the history every call.
5. **Hallucination is normal.** Reduce it with sources, tools, and validation.
6. **Temperature:** low = predictable, high = creative.
