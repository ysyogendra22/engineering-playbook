# Architecting AI-Enabled Systems

Roadmap topic 20 · Stage 6: Your Domain · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** an AI feature is still a system with all the normal architectural concerns — data ownership, security, cost, resilience — plus a few genuinely new ones, because the "dependency" is a model that can be wrong, slow, or expensive in new ways. Full depth lives in `08-artificial-intelligence`; this topic is the architecture-level summary.

---

#### 1. Where the Model Sits — 🟢 Must Know

The model sits **behind your backend**, never called directly from a client with an embedded key (`AI 5`) — the exact same "never trust the client, keep secrets server-side" principle from `11`'s security architecture, applied to an AI provider's API key specifically.

```text
Client  →  Your backend  →  Model provider
        (auth, limits,      (holds the API key)
         logging, filters)
```

---

#### 2. Building Blocks — 🟢 Must Know

The standard architectural components of an AI-enabled system: **prompts** (the instructions), **retrieval** (RAG — grounding answers in real data, `AI 7`), **tools** (letting the model take actions, `AI 8`), **agents** (multi-step tool-using loops, `AI 10`), and **evals** (testing quality, `AI 15`). Treat these as real architectural components to be designed deliberately, not implementation details to figure out ad hoc.

---

#### 3. Design for Wrong Answers — 🟢 Must Know

*The genuinely new architectural concern AI introduces — unlike a normal dependency, this one can be confidently wrong.*

**Grounding** (retrieval-based answers, tied to real sources), **validation** (checking model output before using it, the same principle as never trusting client input, `11`), and **human approval** for consequential actions (`AI 16`) — design these in from the start, since a model being wrong is a normal, expected condition, not a rare edge case.

---

#### 4. Cost, Latency, and Reliability as First-Class Requirements — 🟢 Must Know

Model calls are slower and more expensive than a typical API call, and provider outages happen — treat cost, latency, and reliability as **quality attributes** (topic `2`) to be explicitly measured and ranked for this specific feature, not assumed to be fine (`AI 17`).

---

#### 5. Privacy and Data Flow to Third-Party Models — 🟢 Must Know

Every prompt sent to a model is data sent to a **third party** — the same data-architecture and privacy concerns from `9` apply directly: what data actually needs to be sent, where it's processed, and how that's documented and controlled.

---

#### 6. Model Gateway — 🟡 Good to Know

A dedicated backend layer that centralises API keys, rate limits, routing (to different models/providers), and logging for all AI calls — the AI-specific instance of the API gateway pattern (`6`, item 7), giving one place to control cost, reliability, and observability across every AI feature.

---

#### 7. Swappable Providers and Model Versions — 🟡 Good to Know

Design the integration so the underlying model or provider can be swapped without a major rearchitecture (`AI 18`) — model quality, pricing, and availability all change quickly in this space; an architecture locked to one specific model is taking on real, ongoing risk.

---

#### 8. On-Device vs Cloud — 🟡 Good to Know

For mobile specifically, whether inference happens on the device or in the cloud is itself an architectural decision, with real trade-offs in privacy, latency, cost, and capability (`AI 19`, `06-mobile-engineering/20`).

---

#### 9. Evaluation as Part of the Delivery Pipeline — 🟡 Good to Know

Automated evals (`AI 15`) should run as part of CI/CD (`13`), the same way tests do — a prompt or model change that regresses quality should be caught before it ships, not discovered from user complaints afterward.

---

#### 10. Common Interview Questions

1. **How would you architect a system that adds an AI feature to an existing product?**
   The model sits behind your backend, never called directly from the client with an embedded key. Build in the standard blocks (prompting, retrieval, tools/agents as needed, evals), and treat cost, latency, and reliability as explicit, measured quality attributes for this feature.
2. **What's architecturally different about AI as a dependency, compared to a normal backend dependency?**
   It can be confidently wrong, not just unavailable or slow — this requires designing for grounding, output validation, and human approval on consequential actions, not just the usual timeout/retry/circuit-breaker toolkit alone.
3. **How do you avoid being locked into one AI provider?**
   Design the integration behind an internal interface (often via a model gateway) so the underlying provider or model version can be swapped without a major rearchitecture — the same "depend on an abstraction, not a concrete detail" principle from `4` and `8`.
4. **What privacy considerations apply specifically to AI features?**
   Every prompt sent to a model is data sent to a third party — apply the same data-architecture and minimal-data principles as `9`, deciding deliberately what's actually sent and how that's documented and controlled.

---

#### 11. Common Mistakes

1. An AI provider's API key embedded directly in a client app.
2. No output validation — trusting model output the same way you'd trust your own database.
3. Treating cost and latency as afterthoughts instead of measured, ranked quality attributes.
4. Building tightly coupled to one specific model or provider, with no swap path.

---

#### 12. Related Topics

1. `08-artificial-intelligence` (the whole folder) — full depth behind every item here
2. `11` Security Architecture — the client-secret and validation principles this topic applies to AI
3. `2` Requirements, Constraints & Quality Attributes — cost/latency/reliability as ranked quality attributes

---

#### 13. Interview Must Remember

1. **Model sits behind your backend** — never a key in the client.
2. **Design for wrong answers**: grounding, validation, human approval.
3. **Cost, latency, reliability are quality attributes** — measure and rank them, don't assume.
4. **Keep the provider swappable** — don't get architecturally locked to one model.
