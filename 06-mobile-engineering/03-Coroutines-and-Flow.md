# Coroutines & Flow

Roadmap topic 3 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** coroutines let you write asynchronous code that reads like normal, sequential code, without blocking the main thread. Flow is how you observe a stream of values — a database query's results, a text field's changes — over time. Together they're the backbone of almost every other topic in this folder.

---

#### 1. Why Concurrency: Keep the Main Thread Free — 🟢 Must Know

*Everything here exists because of one rule: never block the UI thread (topic `1`).*

1. Network calls, database queries, and heavy computation must run off the main thread.
2. Coroutines are Kotlin's answer: lightweight, cheap to create by the thousands, and they let you write that off-thread code **sequentially**, without nested callbacks.

---

#### 2. Coroutines and `suspend` — 🟢 Must Know

1. A **coroutine** is a unit of work that can **pause** at a `suspend` function call and resume later, without blocking the thread it was running on.
2. A `suspend` function can only be called from another `suspend` function, or from a coroutine builder (`launch`, `async`).

```kotlin
suspend fun fetchNotes(): List<Note> {
    return api.getNotes()   // suspends here; the thread is free to do other work meanwhile
}
```

---

#### 3. Dispatchers — 🟢 Must Know

*Which thread pool a coroutine actually runs on.*

| Dispatcher | Use for |
|---|---|
| `Main` | UI work — updating views, Compose state |
| `IO` | Network calls, database, file I/O |
| `Default` | CPU-heavy work — sorting, parsing, computation |

```kotlin
viewModelScope.launch(Dispatchers.IO) {
    val notes = repository.getNotes()          // runs on IO
    withContext(Dispatchers.Main) {
        updateUi(notes)                         // switch back to Main to touch UI
    }
}
```

---

#### 4. Structured Concurrency — 🟢 Must Know

*Coroutines live inside a scope, and cancelling the scope cancels everything inside it.*

1. Every coroutine belongs to a **scope**. A scope tracks its child coroutines, and cancelling it cancels all of them — no orphaned background work.
2. This is what prevents leaks: when a screen is destroyed, its scope is cancelled, and every coroutine it started stops too.

---

#### 5. `viewModelScope`, `lifecycleScope` — 🟢 Must Know

1. `viewModelScope` — tied to a `ViewModel`'s lifetime; cancelled automatically when the `ViewModel` is cleared.
2. `lifecycleScope` — tied to an Activity/Fragment's lifecycle.
3. **Avoid `GlobalScope`** — it has no lifecycle, so coroutines started there outlive the screen that started them, leaking work and potentially crashing on a destroyed view.

---

#### 6. Cancellation Is Cooperative — 🟢 Must Know

*Cancelling a coroutine only works if the code inside actually checks for it.*

1. Calling `.cancel()` on a scope sets a flag — it doesn't forcibly stop the coroutine mid-instruction.
2. `suspend` functions from Kotlin's own libraries check for cancellation automatically at suspension points. A **tight, non-suspending loop** will not notice cancellation unless you check `isActive` or call `ensureActive()` yourself.

```kotlin
while (isActive) {          // cooperative check — stops promptly when the scope is cancelled
    doWork()
}
```

---

#### 7. Exceptions — 🟢 Must Know

1. Normal `try/catch` works around `suspend` calls, same as regular code.
2. A `CoroutineExceptionHandler` catches uncaught exceptions from a coroutine's root.
3. `supervisorScope` — unlike a regular scope, one child's failure doesn't cancel its siblings. Use it when independent child tasks shouldn't take each other down.

```kotlin
supervisorScope {
    launch { riskyTask1() }   // if this fails, riskyTask2 still runs
    launch { riskyTask2() }
}
```

---

#### 8. Flow: Cold Streams and Operators — 🟢 Must Know

1. A `Flow` is a **cold** asynchronous stream — the code inside only runs when a collector calls `.collect()`. Nothing happens until then.
2. Common operators work like their collection equivalents, but over time: `map`, `filter`, `combine` (merge two flows), `flatMapLatest` (switch to a new inner flow, cancelling the previous one), `debounce` (wait for a pause before emitting — perfect for search-as-you-type).

```kotlin
searchQueryFlow
    .debounce(300)                    // wait for typing to pause
    .flatMapLatest { query -> repository.search(query) }   // cancel the old search, start a new one
    .collect { results -> updateUi(results) }
```

---

#### 9. `StateFlow` and `SharedFlow` — 🟢 Must Know

*Cold `Flow` is for data streams. Hot flows are for state and events.*

1. **`StateFlow`** — always has a current value, and new collectors immediately get the latest one. Used for UI state (topic `6`).
2. **`SharedFlow`** — broadcasts values to all active collectors, with configurable replay — used for one-time events (navigation, a toast message).

```kotlin
private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
val uiState: StateFlow<UiState> = _uiState.asStateFlow()   // expose read-only to the UI
```

---

#### 10. Collecting Flows Safely in the UI — 🟢 Must Know

1. Collecting a flow while a screen is stopped (backgrounded) wastes resources and can cause crashes.
2. Use lifecycle-aware collection — `repeatOnLifecycle(Lifecycle.State.STARTED)` in a coroutine, or the Compose equivalent `collectAsStateWithLifecycle()` — so collection pauses and resumes with the screen's lifecycle.

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state -> render(state) }
    }
}
```

---

#### 11. `async`/`await` — 🟡 Good to Know

1. `launch` starts a coroutine and doesn't return a result. `async` starts one and returns a `Deferred`, whose result you get with `.await()`.
2. Use `async` for running independent work **in parallel**:

```kotlin
val notesDeferred = async { repository.getNotes() }
val userDeferred = async { repository.getUser() }
val notes = notesDeferred.await()   // both ran concurrently, not sequentially
val user = userDeferred.await()
```

---

#### 12. Channels and Back-Pressure — 🟡 Good to Know

1. A `Channel` is a way to send values between coroutines, like a queue.
2. `buffer()` and `conflate()` control what happens when a `Flow` produces values faster than they're consumed — buffer keeps them all (up to a limit), conflate drops all but the latest.

---

#### 13. `callbackFlow` — 🟡 Good to Know

Wraps an old-style callback API (like a location listener) into a `Flow`, so it fits the rest of your reactive code.

---

#### 14. Testing Coroutines and Flows — 🟡 Good to Know

Covered fully in topic `12` — `runTest`, a test dispatcher, and Turbine for asserting on `Flow` emissions.

---

#### 15. Race Conditions and `Mutex` — 🟡 Good to Know

1. Even with coroutines, shared mutable state accessed from multiple coroutines can race.
2. `Mutex` provides a suspending lock — one coroutine enters a critical section at a time, without blocking the underlying thread the way a traditional lock would.

---

#### 16. Legacy Names — 🟡 Good to Know

Threads, `Handler`, `AsyncTask`, and RxJava solved the same problem before coroutines. Know the names for reading older code — coroutines are the modern default.

---

#### 17. iOS Equivalents — 🟡 Good to Know

Swift's `async`/`await`, actors, and `AsyncSequence` map closely to Kotlin coroutines, `Mutex`-protected state, and `Flow`. See topic `16`.

---

#### 18. Common Interview Questions

1. **What's the difference between `launch` and `async`?**
   `launch` starts a coroutine with no return value (fire and forget). `async` returns a `Deferred` you can `await()` for a result — used for parallel work.
2. **Why is cancellation "cooperative"?**
   Cancelling sets a flag; the coroutine's code must check it (via suspension points or `isActive`) to actually stop. A tight loop with no suspension point ignores cancellation.
3. **`Flow` vs `StateFlow` vs `SharedFlow`?**
   `Flow` is cold, starts on collection. `StateFlow` is hot, always has a current value, for state. `SharedFlow` is hot, for broadcasting one-time events.
4. **Why not use `GlobalScope`?**
   It has no lifecycle, so its coroutines outlive the screen that launched them — a leak, and a crash risk if it later touches a destroyed view.
5. **How do you collect a `Flow` safely in a screen?**
   With lifecycle-aware collection (`repeatOnLifecycle`, or `collectAsStateWithLifecycle()` in Compose), so it pauses when the screen isn't visible.
6. **What does `debounce` + `flatMapLatest` give you?**
   The standard search-as-you-type pattern: wait for a typing pause, then cancel any in-flight search and start a fresh one for the latest query.

---

#### 19. Common Mistakes

1. Using `GlobalScope` instead of `viewModelScope`/`lifecycleScope`.
2. Writing a loop that never checks `isActive`, so it ignores cancellation.
3. Collecting a `Flow` without lifecycle awareness, wasting resources when the screen is backgrounded.
4. Using `StateFlow` for one-time events (a navigation trigger fires again every time a new collector subscribes) instead of `SharedFlow` or a proper event channel.
5. Blocking a coroutine's thread with non-suspending, long-running code inside `Dispatchers.Main`.

---

#### 20. Related Topics

1. `1` Mobile Platform Basics — the main-thread rule this all exists to protect
2. `6` App Architecture — `StateFlow` as the UI state holder
3. `12` Testing — testing coroutines and flows
4. `16` iOS & Swift Essentials — Swift concurrency equivalents

---

#### 21. Interview Must Remember

1. **Coroutines pause and resume without blocking a thread** — `suspend` functions are the unit of that.
2. **Structured concurrency:** every coroutine belongs to a scope; cancelling the scope cancels its children.
3. **Cancellation is cooperative** — code must check for it.
4. **`Flow` = cold stream. `StateFlow`/`SharedFlow` = hot, for state/events.**
5. Always collect flows **lifecycle-aware** in the UI.
