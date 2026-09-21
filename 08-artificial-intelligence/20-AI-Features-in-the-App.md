# AI Features in the App

Roadmap topic 20 · Stage 5: AI on Mobile

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** the model lives behind your backend. The app's job is to send the request, show the answer as it arrives, handle slow and broken networks, ask the user before risky actions, and be honest that the answer may be wrong. This is the mobile-engineer half of every AI design question.

---

#### 1. The App Talks to Your Backend — 🟢 Must Know

*Never put the provider key in the app.*

```text
Mobile app  →  Your backend  →  LLM provider / your tools
            (login, limits,      (keys live here)
             logging, filters)
```

1. The app sends the user's request to **your backend**, with the user's normal login token (`BE 5`).
2. The backend adds the API key, applies limits, calls the model and tools, and streams the answer back.
3. Benefits: no key in the app, per-user limits, logging, filters, easy provider or model changes with no app release.

---

#### 2. Streaming Chat UI — 🟢 Must Know

*Show words as they arrive. Let the user cancel and retry.*

1. Read the response as a **stream** (topic `05`) and append text to the message.
2. Show a **typing indicator** until the first token arrives.
3. **Cancel** — a stop button closes the request. The backend should stop the model call too, so you do not pay for unused tokens.
4. **Retry** on failure. Keep the partial answer visible if the stream breaks.
5. Render markdown carefully: code blocks, lists, and links. Do not auto-open links from model text without care (topic `16`).
6. Update the UI in small batches, not once per token, to avoid needless redraws.

**Mobile view:** consume with a `Flow` and `collect` (Kotlin), or an `AsyncSequence` with `for await` (Swift). Cancel the coroutine or task to cancel the request.

---

#### 3. Clear States — 🟢 Must Know

*AI features have more states than a normal screen.*

| State | What to show |
|---|---|
| Loading | Typing indicator or skeleton |
| Streaming | Partial answer, stop button |
| Done | Full answer, actions (copy, retry, feedback) |
| Error | Plain message and a retry button |
| Rate limited or quota reached | Explain, and say when it resets |
| Offline | Say so. Show history, or use an on-device fallback (topic `19`) |
| Blocked or refused | A short, kind explanation |

Design all of them before you start coding.

---

#### 4. Long Agent Tasks — 🟢 Must Know

*Agents can take seconds or minutes.*

1. **Show progress:** "Searching notes…", "Reading 3 notes…", "Writing summary…".
2. Let the user **cancel**.
3. **Ask approval** before actions that change things (send, delete, pay). Show exactly what will happen, then Approve or Cancel (topics `10` and `16`).
4. For very long runs, use a **background job** and a **push notification** when done (`SD 21`, `SD 24`).
5. Handle **app background, kill, and reconnect:** the run continues on the server, so the app fetches the current status when it returns.

---

#### 5. Tell Users the Answer May Be Wrong — 🟢 Must Know

*Be honest with users about what AI can and cannot do.*

1. Show a short notice that AI answers can be wrong, especially for health, money, or legal topics.
2. Show **sources** when you have them (RAG, topic `07`), so users can check.
3. Give easy ways to **correct, regenerate, or report** an answer.
4. Never present model output as verified fact when it is not.
5. Label AI-generated content where required or expected.

---

#### 6. Per-User Limits and Quotas — 🟢 Must Know

*Limits belong on the server, and the app only shows them.*

1. Enforce **rate limits and quotas on the server**. The app can only show them.
2. Show the user how much they have left, and what happens at the limit.
3. Different limits per plan (free, paid) are a product decision, enforced by the backend.
4. Protects your bill and the provider quota (topic `17`, `SD 25`).

---

#### 7. Local History and Sync — 🟡 Good to Know

*Keep chats on the device, and sync them.*

1. Keep the chat history in a **local database** so it opens instantly and works offline (`SD 30`).
2. Sync with the server, and resolve conflicts simply (the server is the source of truth for history).
3. Let users **delete** conversations, locally and on the server (topic `16`).
4. Do not store secrets or sensitive tool results on the device unencrypted.

---

#### 8. Voice and Camera Input — 🟡 Good to Know

*Use the phone's microphone and camera, with care.*

1. **Voice:** speech-to-text, then send text. Or send audio to a multimodal model.
2. **Camera:** send a photo (a receipt, a document, a plant). Resize and compress first (topic `03`).
3. Ask for **permissions** at the moment they are needed, with a clear reason.
4. Photos and audio are personal data. Send only what is needed, and tell the user (topic `16`).

---

#### 9. Battery and Data Use — 🟡 Good to Know

*AI features can drain data and battery. Keep them light.*

1. Long streams and repeated calls use data and battery.
2. Do not poll. Use a stream or a push notification.
3. Cache and reuse answers where it makes sense.
4. Compress images before upload. Respect data-saver mode.
5. Be careful with on-device inference in the background (topic `19`).

---

#### 10. Common Interview Questions

1. **How do you add an LLM chat to a mobile app?**
   The app calls your backend, which calls the model. Stream the answer to the UI, with cancel and retry, and handle all the states.
2. **Why not call the LLM directly from the app?**
   The API key would be exposed, and you would lose per-user limits, logging, and control.
3. **How do you make it feel fast?**
   Stream tokens, show a typing indicator, and update the UI in small batches.
4. **How do you handle a long-running agent task?**
   Show progress, allow cancel, ask approval for risky actions, and use a background job with a push notification for very long runs.
5. **What if the user goes offline mid-answer?**
   Keep the partial answer, show a clear state, and offer retry. For long runs, the server continues and the app fetches the result later.
6. **How do you handle wrong answers?**
   Say answers may be wrong, show sources, allow correction and reporting, and log feedback.
7. **How do you control cost from the client side?**
   The server enforces quotas and limits. The app shows remaining usage and avoids unnecessary calls.

---

#### 11. Common Mistakes

1. Provider key inside the app.
2. Waiting for the whole answer before showing anything.
3. No cancel button, so users keep paying for a run they abandoned.
4. Only designing the happy path (no error, offline, or limit states).
5. Running risky agent actions with no user approval.
6. Limits enforced only in the app.
7. Redrawing the whole screen for every token.

---

#### 12. Related Topics

1. `05` Calling an LLM API
2. `10` Agents
3. `16` Safety, Security & Privacy
4. `17` Cost, Latency & Reliability
5. `19` On-Device vs Cloud AI
6. `SD 24` Real-Time Communication & Push
7. `SD 30` Mobile-Specific Topics

---

#### 13. Interview Must Remember

1. **App → your backend → model.** Never a key in the app.
2. **Stream** the answer, with **cancel** and **retry**.
3. **Design every state:** loading, streaming, error, offline, limit.
4. **Agents:** show progress, ask approval, notify when done.
5. **Be honest:** answers may be wrong. Show sources.
6. **Limits and quotas are enforced on the server.**
