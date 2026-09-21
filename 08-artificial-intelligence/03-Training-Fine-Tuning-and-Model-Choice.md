# Training, Fine-Tuning & Model Choice

Roadmap topic 3 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** big labs train the model. You usually do not. Your job is to choose a model that fits, then get the result you need in the cheapest way: prompt first, then retrieval, then fine-tuning only if needed.

---

#### 1. Pretraining, Fine-Tuning, Prompting: Cheapest First — 🟢 Must Know

*Fix problems with the cheapest tool that works.*

1. **Pretraining** — the model learns language and general knowledge from huge amounts of text. Very expensive. Done by model providers. The result is a **foundation model**: a general-purpose model that can later be adapted to many jobs.
2. **Fine-tuning** — extra training of an existing model on your examples, to teach it a style, format, or narrow skill.
3. **Prompting** — telling the model what to do at request time. No training.

The ladder:

```text
1. Better prompt + examples          (minutes, cheap)
2. Add your data with RAG            (hours, moderate)
3. Fine-tune a model                 (days, costs more, needs good data)
4. Train your own model              (almost never)
```

1. Move down a step only when the step above is not enough.
2. Fine-tuning changes **behaviour and style**. It is a poor way to add **facts**. Use RAG for facts (topic `07`).

---

#### 2. Open-Weight vs Closed Models — 🟢 Must Know

*Can you download and run it, or only call it through an API?*

| | Closed (API-only) | Open-weight |
|---|---|---|
| How you use it | Call the provider's API | Download the weights, run them yourself |
| Setup | Easy | You manage servers, GPUs, updates |
| Data | Sent to the provider | Stays where you run it |
| Control | Provider decides versions and limits | You control the version and can fine-tune freely |
| Cost | Pay per token | Pay for hardware; can be cheaper at high volume |

1. Start with an API to learn and prototype.
2. Consider open-weight when privacy, cost at scale, offline use, or on-device use matters.

---

#### 3. Small vs Large Models — 🟢 Must Know

*Bigger is usually smarter, slower, and more expensive.*

1. **Large models** — better at hard reasoning and messy tasks. Slower and costlier.
2. **Small models (SLMs, small language models)** — faster and cheaper. Good for simple, clear tasks. Some run on a phone or laptop.
3. Match the model to the task. Classify a message with a small model. Plan a complex task with a large one.

How to choose (check these):

1. **Quality on your task**, tested with your own examples (topic `15`).
2. **Latency** and **cost per request**.
3. **Context window** size.
4. **Features you need:** tool calling, structured output, images, streaming.
5. **Privacy** and where the data goes.
6. **Reliability** and the provider's limits.

You can also mix models: small for easy steps, large for hard ones (model routing, topic `05`).

---

#### 4. Reasoning Models — 🟢 Must Know

*Models that "think" before answering.*

1. A **reasoning model** spends extra tokens working through a problem step by step before giving the final answer.
2. Better at math, logic, code, and multi-step planning.
3. Cost: slower and more expensive, because the thinking tokens count.
4. Use them for hard problems. Use a normal model for simple ones.
5. You usually do not need to say "think step by step". The model already does.

---

#### 5. Multimodal Models — 🟢 Must Know

*Models that handle more than text.*

1. **Multimodal** — accepts or produces text, images, audio, or video.
2. Examples of use: describe a photo, read text from a receipt, transcribe audio, answer questions about a screenshot.
3. Images and audio cost tokens too, and can be large. Resize before sending.

**Mobile view:** the phone has a camera and microphone, so multimodal features fit mobile very well.

---

#### 6. Base vs Instruction-Tuned, and RLHF — 🟡 Good to Know

*Two names you will hear: how a raw model becomes a helpful chat model.*

1. A **base model** just continues text. An **instruction-tuned (chat) model** is trained to follow instructions. You almost always use the chat kind.
2. **RLHF (reinforcement learning from human feedback)** — people rate answers, and the model is trained to prefer the higher-rated ones. It makes models more helpful and safer.
3. The general steps: pretrain → instruction-tune → preference-tune. Know the names and the purpose. Nothing more.

---

#### 7. Distillation, Quantization, LoRA — 🟡 Good to Know

*Ways to make a model smaller or cheaper to adapt.*

1. **Distillation** — a small model is trained to copy a large one. The small one is faster and cheaper, and nearly as good on that task.
2. **Quantization** — store the numbers in the model with less precision. The model uses less memory and runs faster, with a small quality loss. Example: 8 GB down to about 2 GB.
3. **LoRA** — a cheap way to fine-tune by training only a small add-on instead of the whole model. Name only.

Quantization is important for on-device models (topic `19`).

---

#### 8. Benchmarks vs Your Own Task — 🟡 Good to Know

*Public scores help shortlist. Your own examples decide.*

1. Public **benchmarks** compare models on standard tests. They help to shortlist.
2. They may not match your task, and models can be tuned to score well on them.
3. Always try your shortlist on **your own examples** and choose from those results.

---

#### 9. Common Interview Questions

1. **Prompting, RAG, or fine-tuning: how do you decide?**
   Start with prompting. Add RAG when the model needs your data or fresh facts. Fine-tune for a consistent style, format, or narrow skill when prompting is not enough.
2. **Can you teach a model new facts by fine-tuning?**
   Poorly. Use RAG for facts. Fine-tuning is better for behaviour and format.
3. **Open-weight or closed model?**
   Closed for speed of building. Open-weight for privacy, control, cost at scale, or on-device use.
4. **When do you use a smaller model?**
   For simple, high-volume tasks where speed and cost matter more than peak quality.
5. **What is a reasoning model and when do you use it?**
   A model that thinks before answering. Use it for hard, multi-step problems, and accept higher cost and latency.
6. **What are quantization and distillation?**
   Quantization shrinks a model by using lower-precision numbers. Distillation trains a small model to imitate a large one.
7. **How do you pick a model?**
   Shortlist by features and cost, then test on your own examples for quality and latency.

---

#### 10. Common Mistakes

1. Fine-tuning first, before trying a better prompt or RAG.
2. Fine-tuning to add facts.
3. Using the largest model for every task.
4. Choosing a model from a leaderboard without testing your own cases.
5. Ignoring where user data is sent.
6. Forgetting that multimodal inputs cost tokens.

---

#### 11. Related Topics

1. `02` How LLMs Work
2. `04` Prompting & Context Engineering
3. `05` Calling an LLM API (model routing)
4. `07` RAG
5. `15` Evaluation & Quality
6. `19` On-Device vs Cloud AI

---

#### 12. Interview Must Remember

1. **Ladder:** prompt → RAG → fine-tune → train your own.
2. **Fine-tune for behaviour, RAG for facts.**
3. **Open-weight** = you run it. **Closed** = API only.
4. **Small models** for simple tasks. **Reasoning models** for hard ones.
5. **Quantization** shrinks, **distillation** copies, **RLHF** shapes behaviour.
6. **Test on your own data**, not just benchmarks.
