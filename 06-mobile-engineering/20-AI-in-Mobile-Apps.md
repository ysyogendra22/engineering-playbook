# AI in Mobile Apps

Roadmap topic 20 · Stage 7: Mobile in the System · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** an AI feature in a mobile app is still a mobile feature first — it needs the same streaming UI, error states, and backend-mediated networking as anything else in this folder. `AI 19–20` cover this in more depth; this topic is the mobile-side summary and pointer.

---

#### 1. The App Calls Your Backend — 🟢 Must Know

*Never a provider key in the app — the same rule as topic `13`, applied specifically here (`AI 5`, `AI 20`).*

```text
Mobile app  →  Your backend  →  LLM provider
            (auth, limits,      (holds the API key)
             logging, filters)
```

The app authenticates as the user (topic `13`), the same as any other backend call (topic `8`) — the AI provider's key never leaves your server.

---

#### 2. Streaming Responses into the UI — 🟢 Must Know

Consume the response as a `Flow` (topic `3`), appending text to the UI as tokens arrive, with **cancel** (stop generating) and **retry** (`AI 5`) — the same streaming-consumption pattern used for any other real-time data (topic `8`, `18`).

```kotlin
viewModelScope.launch {
    repository.streamChatResponse(prompt)
        .collect { token -> _uiState.update { it.appendToken(token) } }
}
```

---

#### 3. States for AI Features — 🟢 Must Know

The same sealed-state discipline as any other screen (topic `6`), with a couple of AI-specific additions:

| State | Show |
|---|---|
| Loading | Typing indicator |
| Streaming | Partial answer, a stop button |
| Error | Plain message, retry |
| Offline | Say so; on-device fallback if available |
| Limit reached | Explain, and say when it resets |

---

#### 4. On-Device vs Cloud AI — 🟢 Must Know

The full trade-off (privacy, offline capability, model strength, latency, cost) is covered in `AI 19`. On mobile specifically: on-device models must also account for app size, battery, and device variety (topic `1`, `11`) — a technique that works well on a flagship phone may be unusable on a low-end one.

---

#### 5. On-Device Options — 🟡 Good to Know

Names to know: **ML Kit** and **Gemini Nano** (Android), **LiteRT**, formerly TensorFlow Lite (cross-platform), **Core ML** (iOS, topic `16`). Check current platform/device support before committing — this area changes quickly.

---

#### 6. Model Download, Updates, and Storage — 🟡 Good to Know

An on-device model can be large — download it after install (not bundled in the initial APK/IPA), on an unmetered connection where possible, with progress shown and a fallback if the download fails or the device is unsupported (`AI 19`).

---

#### 7. Voice and Camera Input — 🟡 Good to Know

Feeding microphone or camera input into an AI feature reuses the device-capability handling from topic `19` — request the permission in context, and treat the captured data (voice, image) as sensitive, sent only as needed (item 8).

---

#### 8. Privacy and Third-Party Models — 🟡 Good to Know

Data sent to an AI model is data sent to a third party (`AI 16`) — apply the same minimal-collection principle as topic `13`, and make sure the app's data-safety declaration (topic `19`) reflects it accurately.

---

#### 9. Common Interview Questions

1. **How would you add a streaming AI chat feature to a mobile app?**
   The app calls the backend, which holds the provider key and calls the model; the response streams back as a `Flow`, rendered incrementally with cancel/retry, using the same sealed-state pattern as any other screen.
2. **Why not call the AI provider directly from the app?**
   Same reason as any other secret — an embedded key can be extracted from the app; the backend must mediate access, add limits, and log usage.
3. **What extra mobile constraints apply to an on-device AI model, beyond what `AI 19` already covers?**
   App size (bundling vs downloading), battery cost of local inference, and device variety — a model that runs fine on a flagship phone may need a cloud fallback on older or lower-end hardware.
4. **How do you handle an AI feature when the device is offline?**
   Show a clear offline state, and use an on-device model as a fallback if one is available and suitable — otherwise disable the feature with a clear message rather than hanging indefinitely.
5. **What privacy considerations apply specifically to AI features?**
   Data sent to the model is sent to a third party — send the minimum needed, and make sure it's reflected in the app's data-safety declaration.

---

#### 10. Common Mistakes

1. Embedding an AI provider key directly in the app.
2. No cancel button on a streaming response, wasting tokens (and money) on abandoned generations.
3. Assuming an on-device model that works on a test device works everywhere.
4. Treating an AI feature's error/offline states as an afterthought instead of designing them like any other screen state.
5. Sending more data to a third-party model than the feature actually needs.

---

#### 11. Related Topics

1. `3` Coroutines & Flow — the streaming consumption pattern
2. `6` App Architecture — sealed UI states applied to AI features
3. `8` Networking — the backend-mediated call pattern
4. `AI 5`, `AI 19`, `AI 20` (in `08-artificial-intelligence`) — the full depth on backend-mediated calls, on-device vs cloud, and mobile AI UX

---

#### 12. Interview Must Remember

1. **App → your backend → model.** Never a provider key in the app.
2. **Stream with cancel/retry**, using the same `Flow` and sealed-state patterns as everything else in this folder.
3. **On-device AI adds mobile-specific constraints**: app size, battery, device variety.
4. **Privacy applies to AI features too** — send the minimum, declare it accurately.
