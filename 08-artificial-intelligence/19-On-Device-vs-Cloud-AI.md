# On-Device vs Cloud AI

Roadmap topic 19 · Stage 5: AI on Mobile

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** on a phone you can run a model on the device or call one in the cloud. On-device is private, fast, and works offline, but the models are small and phones have limits. Cloud models are stronger, but need a network and cost per call. Many products use both. This is where a mobile engineer stands out.

---

#### 1. Where to Run the Model — 🟢 Must Know

*Three choices.*

```text
On-device:   Phone runs the model.             (private, offline, small models)
Cloud:       Your backend calls a big model.   (strong, needs network, pay per call)
Hybrid:      Phone first, cloud when needed.   (best of both, more complex)
```

Related words:

1. **On-device AI** — the model runs on the phone, tablet, or laptop. No internet needed.
2. **Edge AI** — running AI close to where the data is created (a phone, a camera, a sensor) instead of in a data center. On-device AI is one kind.
3. **SLM (small language model)** — a smaller language model. Fast, cheaper, and often small enough for a device.

---

#### 2. On-Device: Strengths — 🟢 Must Know

*Why running the model on the phone is attractive.*

1. **Private** — data stays on the phone.
2. **Works offline** — no network needed.
3. **Low latency** — no network round trip.
4. **No per-call cost** — the user's phone does the work.
5. Good for: text classification, smart replies, summarizing short text, translation, image labelling, speech-to-text, camera features.

---

#### 3. On-Device: Limits — 🟢 Must Know

*Why it is hard to run models on phones.*

1. **Model size** — big models do not fit in phone memory and storage.
2. **Battery and heat** — heavy inference drains battery and warms the phone.
3. **Memory** — competes with your app and the OS.
4. **Device variety** — older or cheaper phones are slower, or cannot run it.
5. **Quality** — smaller models are weaker at reasoning and long tasks.
6. **Updates** — a new model means a download or an app update.

---

#### 4. Cloud: Strengths and Costs — 🟢 Must Know

*Why a cloud model is still often the right choice.*

1. **Stronger models** for hard reasoning, long context, and tool use.
2. **Easy to update** — change the model on the server, no app release.
3. **Consistent** across all devices.
4. **Costs:** pay per token, needs a network, adds latency, and sends data off the device.
5. Never put the provider key in the app. Go through your backend (topic `20`).

---

#### 5. Hybrid — 🟢 Must Know

*Use the device when it is good enough, the cloud when it is not.*

Common patterns:

1. **On-device first, cloud fallback:** try a small local model. If confidence is low or the task is hard, call the cloud.
2. **Split by task:** simple tasks (classification, quick edits) on-device. Heavy tasks (long summaries, agents) in the cloud.
3. **Split by privacy:** sensitive data processed locally, non-sensitive work in the cloud.
4. **Split by connectivity:** on-device when offline, cloud when online.

Decide with a few questions:

| Question | Points to |
|---|---|
| Must it work offline? | On-device |
| Is the data very sensitive? | On-device (or careful cloud) |
| Does it need strong reasoning or long context? | Cloud |
| Is it high volume and simple? | On-device (saves cost) |
| Must it behave the same on all devices? | Cloud |

---

#### 6. Platform Options — 🟡 Good to Know

*Names only. This area changes fast, so check the current docs.*

1. **Apple:** Core ML for running models on iPhone and iPad, plus Apple's own on-device model APIs on supported devices.
2. **Android:** ML Kit for ready-made features, Gemini Nano through Google's on-device AI services on supported devices, and **LiteRT** (formerly TensorFlow Lite) for running your own models.
3. **Cross-platform runtimes** can run open-weight small models on both.
4. Not every device supports every option. Always have a fallback.

---

#### 7. Model Download, Updates, Versioning — 🟡 Good to Know

*Big models need careful delivery to the phone.*

1. Models can be **large**. Do not bundle a huge model in the app download. Download it after install, on Wi-Fi, with progress and resume.
2. **Version** the model and keep it compatible with the app version.
3. Check **storage space** first, and let the user remove it.
4. Have a **fallback** if the download fails or the device is unsupported (cloud, or feature off).
5. Old app versions keep using old models. Plan for both (`SD 30`).

---

#### 8. Quantization for On-Device — 🟡 Good to Know

*How large models become small enough for a phone.*

1. **Quantization** stores the model's numbers with lower precision, so it uses less memory and runs faster. Example: about 8 GB down to about 2 GB.
2. There is a small quality loss, which you must test on your task (topic `15`).
3. It is one of the main ways small models fit on phones (topic `03`).

---

#### 9. Common Interview Questions

1. **On-device or cloud AI for a mobile feature?**
   On-device for privacy, offline use, low latency, and simple tasks. Cloud for strong reasoning, long context, and easy updates. Often hybrid.
2. **What are the limits of on-device models?**
   Model size, battery, heat, memory, device variety, and weaker quality.
3. **What is edge AI?**
   Running AI near where the data is produced instead of in a data center. On-device AI is one kind.
4. **How would you design a hybrid approach?**
   Run a small local model first, and fall back to the cloud when the task is hard, confidence is low, or the device is unsupported.
5. **How do you ship a large model to phones?**
   Download it after install, on Wi-Fi, with progress, versioning, a storage check, and a fallback.
6. **What is quantization?**
   Using lower-precision numbers to make the model smaller and faster, with a small quality loss.
7. **Where do privacy concerns come in?**
   On-device keeps data local. With the cloud, send the minimum, and check the provider's policies.

---

#### 10. Common Mistakes

1. Choosing cloud for everything and paying for simple tasks.
2. Choosing on-device for tasks that need a strong model.
3. Bundling a huge model in the app download.
4. No fallback for unsupported or low-end devices.
5. Ignoring battery, heat, and memory during testing.
6. Not testing quality after quantization.

---

#### 11. Related Topics

1. `03` Training, Fine-Tuning & Model Choice (small models, quantization)
2. `16` Safety, Security & Privacy
3. `17` Cost, Latency & Reliability
4. `20` AI Features in the App
5. `SD 30` Mobile-Specific Topics

---

#### 12. Interview Must Remember

1. **On-device:** private, offline, fast, free per call. Limits: size, battery, quality.
2. **Cloud:** strong, easy to update. Costs: network, money, data leaves the device.
3. **Hybrid** = device first, cloud when needed.
4. **Quantization** makes on-device models fit.
5. **Download models after install,** with versioning and a fallback.
6. **Always have a fallback** for unsupported devices.
