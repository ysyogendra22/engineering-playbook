# Mobile Interview Answer Points

Roadmap topic 21 · Stage 8: Interview & Practice · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** interviewers ask for the same handful of explanations over and over — the lifecycle, coroutines, recomposition, your architecture, and how you find bugs. Having a clean, two-minute answer ready for each of these is worth more than knowing ten obscure facts.

---

#### 1. Explain the Lifecycle, Configuration Changes, Process Death — 🟢 Must Know

*The single most common "explain this" question in mobile interviews.*

A strong answer, in order: the lifecycle callbacks (topic `4`), the difference between a configuration change (Activity recreated, process alive, `ViewModel` survives) and process death (everything gone, only `SavedStateHandle`/persisted data survives), and a concrete example of each.

---

#### 2. Explain Coroutines, Cancellation, `Flow` vs `StateFlow` — 🟢 Must Know

In simple words (topic `3`): coroutines pause without blocking a thread; cancellation is cooperative, so tight loops must check for it; `Flow` is cold and starts on collection, `StateFlow` is hot and always has a current value for state.

---

#### 3. Explain Recomposition and State Hoisting — 🟢 Must Know

Recomposition = Compose re-running composables whose read state changed (topic `5`). State hoisting = moving state up so a composable is stateless and reusable. Avoiding needless recomposition = stable types, small focused composables, `derivedStateOf` where useful.

---

#### 4. Explain Your Architecture — 🟢 Must Know

Layers, one-directional data flow, single source of truth (topic `6`) — and be ready to justify **why**, not just name the pattern: "I chose a repository backed by Room as the source of truth because the app needs to work offline."

---

#### 5. Ready Answers: ANR, Memory Leaks, Jank, Cold Start — 🟢 Must Know

For each (topic `11`): what it is, the usual cause, and **how you'd find it** (Profiler, LeakCanary, Macrobenchmark) — the "how you'd find it" part is what separates a memorised definition from real experience.

---

#### 6. Ready Answers: Offline-First, Sync Conflicts, Old App Versions, Token Refresh — 🟢 Must Know

1. **Offline-first** — local database as source of truth (topic `9`).
2. **Sync conflicts** — last-write-wins vs merge rules, chosen per feature.
3. **Old app versions** — why backward compatibility is permanent, not optional (topic `1`, `15`).
4. **Token refresh** — coordinate refresh to avoid a storm on concurrent `401`s (topic `8`).

---

#### 7. Ready Answers: Testing, Token Security, Safe Release — 🟢 Must Know

1. **Testing** — the test pyramid, `runTest`, fakes over mocks (topic `12`).
2. **Token security** — encrypted, Keystore-backed storage, never plain preferences (topic `13`).
3. **Safe release** — staged rollout, feature flags, crash-free rate monitored after every release (topic `15`).

---

#### 8. Coding Warm-Ups in Kotlin — 🟡 Good to Know

Small, common live-coding exercises worth practising cold:

```kotlin
// Debounce a Flow of search queries
fun Flow<String>.debounceSearch() = this.debounce(300).distinctUntilChanged()

// Retry with exponential backoff
suspend fun <T> retryWithBackoff(times: Int = 3, block: suspend () -> T): T {
    repeat(times - 1) { attempt ->
        try { return block() } catch (e: Exception) { delay((2.0.pow(attempt) * 100).toLong()) }
    }
    return block()   // last attempt, let it throw
}

// A tiny LRU cache
class LruCache<K, V>(private val maxSize: Int) : LinkedHashMap<K, V>(16, 0.75f, true) {
    override fun removeEldestEntry(eldest: MutableMap.MutableEntry<K, V>?) = size > maxSize
}

// A thread-safe counter using Mutex
class SafeCounter {
    private val mutex = Mutex()
    private var count = 0
    suspend fun increment() = mutex.withLock { count++ }
}
```

---

#### 9. Tell Decision Stories — 🟡 Good to Know

A hard bug, a performance win, a migration — told as real STAR-form stories (`07-behavioral-leadership/2`), not just technical facts. A performance story lands harder with a real before/after number (topic `11`).

---

#### 10. Questions to Ask the Team — 🟡 Good to Know

1. What does the current app architecture look like, and what's the biggest source of technical debt?
2. What's the release cadence, and how is a bad release caught and mitigated?
3. What quality metrics does the team actually watch (crash-free rate, ANR rate)?

---

#### 11. Common Traps — 🟡 Good to Know

1. **Logic in the UI** — a red flag when describing your own architecture; interviewers listen for whether business logic lives in composables.
2. **Ignoring process death** — only ever discussing configuration changes.
3. **Only the happy path** — never mentioning offline, errors, or old app versions unprompted.

---

#### 12. Common Interview Questions

1. **Walk me through what happens when the OS kills your app in the background and the user returns.**
   Process death — a new process is created, the UI recreated from scratch, and only explicitly saved state (`SavedStateHandle`, database, DataStore) is restored; anything else looks "reset".
2. **How do you keep a Compose screen from recomposing too often?**
   Stable/immutable data types, small focused composables that only read the state they need, `derivedStateOf` for computed values, and profiling recomposition counts rather than guessing.
3. **Tell me about a hard bug you fixed.**
   A real STAR-form story: the symptom, how you found the root cause (a specific tool — Profiler, LeakCanary, logs), the fix, and what changed afterward to prevent a repeat.
4. **How do you decide what to test, given limited time?**
   Lean on the test pyramid — fast unit tests for `ViewModel`s and business logic first, a few integration tests for the repository/database layer, and a handful of UI tests for critical flows.
5. **What's your approach to releasing a risky feature safely?**
   Behind a feature flag, released to a staged rollout percentage, with crash-free rate and ANR rate watched closely before increasing exposure.

---

#### 13. Common Mistakes

1. Only having answers for configuration changes, not process death.
2. Explaining architecture by naming a pattern without justifying the choice.
3. No concrete "how I found it" detail for ANRs/leaks/jank — sounds memorised rather than experienced.
4. Decision stories with no real numbers or outcome.
5. Never mentioning offline, old app versions, or failure states unless directly asked.

---

#### 14. Related Topics

1. `4` App Components & Lifecycle, `3` Coroutines & Flow, `5` UI with Jetpack Compose — the core explanations this topic packages for interviews
2. `11` Performance & Memory, `9` Local Storage & Offline-First — the "ready answers" content
3. `07-behavioral-leadership/2` The STAR Method — how to structure decision stories
4. `22` Practice: Projects & Exercises — where these answers come from real, hands-on work

---

#### 15. Interview Must Remember

1. **Lifecycle, coroutines, recomposition, architecture** — have a clean two-minute answer for each.
2. For failure topics (ANR, leaks, jank), always include **how you'd find it**, not just the definition.
3. **Decision stories need real numbers and outcomes.**
4. **Bring up offline, old versions, and failure states unprompted** — it's the strongest mobile-specific signal you can give.
