# Practice: Projects & Exercises

Roadmap topic 22 · Stage 8: Interview & Practice

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** reading is not enough. One running project — the notes app — carries you through almost this entire folder, growing one capability at a time. Build it in order, and each topic becomes something you did, not just something you read.

---

#### 1. The Notes App — 🟢 Must Know

*The running project. Build it on the Notes API from `BE 12`, in this order.*

1. **Base app** (topics `5`, `6`, `7`, `8`): Compose UI, MVVM, Retrofit calling the Notes API, Hilt for DI.
2. **Offline-first** (topic `9`): local Room database as the source of truth, WorkManager (topic `10`) syncing with the backend, a conflict rule chosen and justified.
3. **Tests** (topic `12`): a `ViewModel` unit test, a repository test with a fake network and in-memory Room, one Compose UI test.
4. **Feed with paging and images** (topics `5`, `8`): cursor pagination via the Paging library, image loading with a caching library.

```kotlin
// A good milestone check after step 2: does the app still show notes
// with the network fully disabled? If yes, offline-first is really working.
```

---

#### 2. Extend It — 🟡 Good to Know

5. **Chat screen** (topic `8`, `SD 24`): WebSocket connection, reconnect with backoff, missed-message recovery.
6. **Photo upload** (topic `8`, `10`): background work, retry, progress reporting.
7. **Modularize** (topic `7`): split into feature modules, and actually measure the build-time difference before and after.
8. **Performance pass** (topic `11`): measure cold start and scrolling with the Profiler/Macrobenchmark, add a Baseline Profile, find and fix one real memory leak with LeakCanary.
9. **Security pass** (topic `13`): audit token storage, permissions, network config, and exported components against a checklist.
10. **Release pass** (topic `15`): build flavors, signing, an internal release track, a staged rollout, crash reporting wired up.
11. **A small AI feature** (topic `20`, `AI 22`): streaming chat through your own backend, with cancel/retry and proper states.
12. **Cross-platform stretch** (topic `16`, `17`): rebuild one screen in SwiftUI, or extract one module to share with Kotlin Multiplatform.

---

#### 3. Exercises — 🟢 Must Know

1. **Explain the lifecycle out loud** — start, rotate, background, kill, in order, without notes (topic `4`, `21`).
2. **Debug a memory leak** — deliberately introduce one (a static Activity reference), then find it with the Profiler or LeakCanary (topic `11`).
3. **Find and fix a slow list** — load a few thousand items into a `LazyColumn`/`RecyclerView` without a `key` or with a heavy per-item composable, then measure and fix it (topics `5`, `11`).

---

#### 4. More Exercises — 🟡 Good to Know

4. **Callback to `Flow`** — take an old callback-based API (a location listener, a Bluetooth scan callback) and wrap it with `callbackFlow` (topic `3`).
5. **Write and test a Room migration** — add a column to an existing entity, write the migration, and write a test that runs it against real sample data (topics `9`, `12`).
6. **Draw your current app's architecture** — layers, module dependencies, and honestly mark where the debt and anti-patterns are (topic `6`, `ARCH 14`).

---

#### 5. How to Use This Project List — 🟢 Must Know

1. Don't skip ahead to the AI feature or cross-platform stretch before the base app and offline-first are solid — later steps assume the earlier architecture is already in place.
2. After each milestone, go back to that topic's **Common Interview Questions** section and answer them using what you just built, not from memory.
3. Keep a short note per milestone: what surprised you, what you'd do differently — this becomes real material for topic `21`'s decision stories and `07-behavioral-leadership`.

---

#### 6. A Suggested Order — 🟢 Must Know

| Stage | Do |
|---|---|
| Week 1–2 | Topics 1–7, build the base notes app |
| Week 3 | Topics 8–10, make it offline-first with sync |
| Week 4 | Topics 11–14, profile, test, and audit the security of what you built |
| Week 5 | Topic 15, ship it to an internal release track |
| Week 6 | Topics 16–20 as reading, plus one stretch build (AI feature, or a KMP/SwiftUI extension) |
| Ongoing | Topics 21–22, mock interviews and mobile system design practice, alongside `SD 30`/`SD 31` |

---

#### 7. Common Interview Questions

1. **Tell me about a project where you implemented offline-first sync.**
   Walk through the notes app milestone: Room as source of truth, WorkManager sync, the conflict rule chosen and why, and one real problem hit along the way.
2. **How did you find and fix a memory leak?**
   Describe the deliberate-leak exercise (or a real one found later): the symptom, using LeakCanary/Profiler to trace the retained reference, and the fix.
3. **What would you do differently if you rebuilt this project?**
   A genuine, specific answer drawn from the milestone notes — shows reflection, not just execution.
4. **How do you approach learning a new mobile topic?**
   Read the concept, then build the smallest real thing that exercises it (this project list's actual method) rather than only reading or only doing isolated tutorials.

---

#### 8. Common Mistakes

1. Reading every topic in this folder before writing any code.
2. Jumping to advanced milestones (AI, cross-platform) before the fundamentals are solid.
3. Never revisiting a topic's interview questions after actually building the related feature.
4. Building without keeping any notes, so decision stories (topic `21`) end up vague later.

---

#### 9. Related Topics

1. `1`–`22` — every topic in this folder feeds into this one running project
2. `BE 12` Checkpoint Project: Notes API — the backend this project is built against
3. `21` Mobile Interview Answer Points — where these projects become interview stories
4. `SD 32` Practice: Projects & Designs — the equivalent backend/system-design practice list

---

#### 10. Interview Must Remember

1. **One running project (the notes app), grown milestone by milestone** — this is the fastest way through the whole folder.
2. **Don't skip the fundamentals** for the stretch goals.
3. **Keep notes per milestone** — they become your decision stories.
4. **Revisit each topic's interview questions** after building the related feature, not from memory alone.
