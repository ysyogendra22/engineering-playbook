# Performance & Memory

Roadmap topic 11 · Stage 4: Quality

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** mobile performance has two faces: how long until the app is usable (startup), and how smooth it feels while in use (frames, memory). Measure first, then fix the specific, measured problem — guessing wastes effort and often makes nothing better.

---

#### 1. Startup: Cold, Warm, Hot — 🟢 Must Know

| Start type | What's already alive | Speed |
|---|---|---|
| Cold | Nothing — new process | Slowest |
| Warm | Process alive, Activity destroyed | Faster |
| Hot | Process and Activity both alive, just backgrounded | Fastest |

1. **What slows a cold start**: heavy `Application` class setup (topic `4`), too much work before the first frame is drawn, large dependency graphs initialising eagerly.
2. Users judge the app by cold start — it's the first impression, every time the app was fully closed.

---

#### 2. Frame Rendering and Jank — 🟢 Must Know

1. The **frame budget** is roughly 16ms at 60Hz (less at 90/120Hz) — the time to produce one frame before the next is due.
2. **Jank** — a dropped or delayed frame, felt as stutter. Caused by doing too much work on the main thread within that budget (topic `1`).

---

#### 3. ANR — 🟢 Must Know

**ANR (Application Not Responding)** — the OS detects the main thread has been blocked too long (input not processed, or a broadcast handler running too long) and offers to close the app. Prevented by never doing slow work synchronously on the main thread (topic `3`).

---

#### 4. Memory Leaks — 🟢 Must Know

*Objects kept alive after they're no longer needed, because something still references them.*

Common causes:
1. A **`Context`** (especially an Activity) held by a long-lived object (a singleton, a static field).
2. A **listener or callback** registered but never unregistered.
3. A coroutine in `GlobalScope` (topic `3`) holding a reference to a destroyed screen.

```kotlin
// Leak: static field holds an Activity reference across its own destruction
companion object { var activityRef: Activity? = null }   // never do this

// Fix: use application context, or don't hold a long-lived reference at all
```

---

#### 5. Profile First — 🟢 Must Know

*Always measure before optimising — the same discipline as `10-Indexes-and-Query-Performance` in backend engineering.*

The **Android Studio Profiler** shows CPU, memory, and network activity over time — find the actual bottleneck before changing code, rather than guessing.

---

#### 6. Lists and Images — 🟢 Must Know

1. **Reuse** — `LazyColumn` (topic `5`) and `RecyclerView` only compose/bind the visible items, not the whole list.
2. **Sizing and downsampling** — never load a full-resolution image into a small thumbnail; decode at the target size (image loading libraries like Coil do this automatically, topic `8`).

---

#### 7. LeakCanary — 🟡 Good to Know

A library that automatically detects and reports memory leaks during development — the standard way to actually find leaks rather than guess at them.

---

#### 8. Baseline Profiles and Macrobenchmark — 🟡 Good to Know

1. A **Baseline Profile** tells the Android runtime which code paths to precompile ahead of time, speeding up cold start and reducing early jank.
2. **Macrobenchmark** measures real startup and scrolling performance on an actual release-like build, not just in the IDE.

---

#### 9. R8 Shrinking and App Size — 🟡 Good to Know

**R8** shrinks, optimises, and obfuscates release code, reducing app size and startup class-loading cost — see topic `13` for its security angle (obfuscation) too.

---

#### 10. Battery and Network Efficiency — 🟡 Good to Know

Batch network requests instead of many small ones; avoid polling in favour of push or WorkManager (topic `10`) — both battery and data usage matter to real users.

---

#### 11. Compose Performance — 🟡 Good to Know

Recomposition counts, stable types, and lazy layouts (topic `5`) are the Compose-specific side of this topic — a UI that recomposes far more than necessary feels janky even with otherwise fast code.

---

#### 12. Perfetto and System Traces — 🟡 Good to Know

A deeper, system-wide tracing tool for diagnosing performance issues that cross app and OS boundaries — used when the Profiler alone isn't enough.

---

#### 13. StrictMode — 🟡 Good to Know

A developer-mode tool that flags accidental main-thread disk/network access during development, catching threading mistakes before they ship.

---

#### 14. Test on Low-End Devices — 🟡 Good to Know

A flagship phone hides performance problems that a budget device will expose immediately — always test on real, low-end hardware before shipping, not only an emulator or a high-end phone.

---

#### 15. Common Interview Questions

1. **What's the difference between cold, warm, and hot start, and what slows a cold start?**
   Cold = new process, slowest. Warm = process alive, Activity recreated. Hot = both alive. Heavy `Application` class or eager dependency setup slows cold start most.
2. **What causes an ANR?**
   The main thread blocked too long — slow synchronous work, a long-running broadcast handler, or a deadlock — preventing input from being processed.
3. **How would you find and fix a memory leak?**
   Use LeakCanary or the Profiler to identify what's holding the reference (often a `Context`, an unregistered listener, or `GlobalScope` work), then remove or properly scope that reference.
4. **How do you approach a performance problem?**
   Profile first to find the actual bottleneck, fix that specific measured issue, then re-measure — never guess-and-optimise blind.
5. **Why test on low-end devices?**
   Performance and memory problems that are invisible on a flagship phone show up immediately on constrained hardware — real users often have older or cheaper devices.

---

#### 16. Common Mistakes

1. Optimising before profiling — fixing a guess instead of the real bottleneck.
2. A static or long-lived reference holding an Activity/`Context`.
3. Loading full-resolution images into small views.
4. Only testing on a high-end phone or emulator.
5. Heavy, synchronous work in the `Application` class, slowing every cold start.

---

#### 17. Related Topics

1. `1` Mobile Platform Basics — the main-thread rule underlying jank and ANRs
2. `4` App Components & Lifecycle — where memory leaks often originate
3. `5` UI with Jetpack Compose — recomposition performance
4. `12` Testing — where performance regressions should be caught early

---

#### 18. Interview Must Remember

1. **Cold/warm/hot start** — know the difference and what slows cold start.
2. **ANR = main thread blocked too long.** **Jank = a frame missed its budget.**
3. **Profile first, fix the measured problem, re-measure.**
4. Memory leaks usually trace back to a **held `Context`, listener, or `GlobalScope` coroutine.**
5. **Test on real, low-end devices** — not just a flagship or emulator.
