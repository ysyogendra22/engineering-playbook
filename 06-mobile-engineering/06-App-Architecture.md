# App Architecture

Roadmap topic 6 · Stage 2: Building the App

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** architecture on mobile is really one idea repeated everywhere: state flows down to the UI, events flow up from it, and there's exactly one place that owns the truth. Once you can explain that clearly, you can explain your whole app.

---

#### 1. Layers — 🟢 Must Know

```text
UI (Compose)  →  ViewModel  →  [ optional: domain / use cases ]  →  data (repository)
   ↑ state flows down                         events flow up ↓
```

1. **UI** — renders state, sends events up (a button tap becomes a call into the `ViewModel`).
2. **`ViewModel`** — holds UI state, talks to the data layer (directly or via use cases).
3. **Data (repository)** — the single source of truth, hiding whether data comes from network, database, or cache.
4. See `ARCH 19` for the architect-level view of this same layering.

---

#### 2. MVVM and MVI — 🟢 Must Know

1. **MVVM (Model-View-ViewModel)** — the `ViewModel` exposes state; the View observes and renders it.
2. **MVI (Model-View-Intent)** — a stricter, more explicit variant: the View sends **intents** (user actions) to the `ViewModel`, which produces a new immutable **state**, always through one clear reducer-like path.
3. Both share the same core idea: **one direction of data flow** (topic `3`).

---

#### 3. Unidirectional Data Flow — 🟢 Must Know

State flows **down** (`ViewModel` → UI), events flow **up** (UI → `ViewModel`) — always in one direction, never a view mutating state directly. This is what makes state changes traceable and testable.

---

#### 4. Repository Pattern and Single Source of Truth — 🟢 Must Know

1. The **repository** hides where data actually comes from — network, local database, in-memory cache — behind one clean interface.
2. The **local database is usually the single source of truth** in an offline-first design (topic `9`): the UI observes the database, and the repository's job is to keep the database in sync with the network, not to hand network results straight to the UI.

```kotlin
class NotesRepository(private val dao: NoteDao, private val api: NotesApi) {
    fun observeNotes(): Flow<List<Note>> = dao.getAllNotes()   // UI observes the DB, not the network directly

    suspend fun refresh() {
        val remote = api.getNotes()
        dao.insertAll(remote)          // DB is updated; the Flow above emits automatically
    }
}
```

---

#### 5. Modelling UI State with Sealed Types — 🟢 Must Know

Loading, content, error, and empty states as a sealed hierarchy (see the example in `02-Kotlin-Essentials/3`) — the compiler forces every screen to handle every case, so a forgotten error state is a compile error, not a bug report.

---

#### 6. One-Time Events — 🟢 Must Know

*A navigation trigger or a toast message must fire exactly once — not on every recomposition or every new collector.*

1. `StateFlow` isn't right for this — a new collector immediately re-receives the current value, which can re-trigger an event.
2. Use a `SharedFlow` with no replay, a `Channel`, or an explicit "consumed" flag in the state to make sure an event fires once and is then cleared.

```kotlin
private val _events = MutableSharedFlow<UiEvent>()   // no replay — new collectors don't get old events
val events: SharedFlow<UiEvent> = _events.asSharedFlow()
```

---

#### 7. Error Handling: One Clear Model — 🟢 Must Know

Map every kind of failure (network, HTTP status, parsing, business rule) into **one consistent error type** the UI layer understands, instead of letting raw exceptions or provider-specific errors leak up to the screen (full detail in topic `8`).

---

#### 8. Use Cases (Interactors) — 🟢 Must Know

1. A **use case** wraps one piece of business logic (`GetNotesUseCase`, `SyncNotesUseCase`), sitting between the `ViewModel` and the repository.
2. **When they help:** logic reused across several `ViewModel`s, or business rules complex enough to deserve their own test file.
3. **When they're extra layers:** a screen with simple, single-use logic — wrapping every repository call in a one-line use case just for consistency adds indirection without real benefit.

---

#### 9. Clean Architecture and Dependency Direction — 🟡 Good to Know

Dependencies point **inward**: UI depends on domain, domain doesn't depend on UI or data frameworks. This keeps business logic free of Android/Compose types, so it's easier to test and reuse.

---

#### 10. Mapping Between Layers — 🟡 Good to Know

**DTO** (raw network shape) → **entity** (database shape) → **domain model** (business shape) → **UI model** (exactly what a screen needs). Not every app needs all four — but knowing the distinction prevents leaking a network field name straight onto a screen.

---

#### 11. Navigation Architecture — 🟡 Good to Know

Where navigation decisions live (in the `ViewModel` via events, or in the UI layer directly) is itself an architecture decision — be consistent across the app.

---

#### 12. Explaining Architecture Decisions — 🟡 Good to Know

Frame any choice as: the problem, the options considered, the trade-off accepted (`ARCH 3`) — "I chose X because Y; the cost is Z" is a stronger answer than naming a pattern alone.

---

#### 13. Anti-Patterns — 🟡 Good to Know

1. **Logic in composables** — business rules belong in the `ViewModel`/domain layer, not scattered through UI code.
2. **God `ViewModel`** — one `ViewModel` doing everything for a huge screen; split by responsibility.
3. **Leaking Android types into domain** — a `Context` or `View` reference inside business logic couples it to the framework and makes it hard to test.

---

#### 14. Common Interview Questions

1. **How would you explain your app's architecture?**
   Layers with one-directional data flow: UI renders state and sends events up; `ViewModel` holds state and talks to a repository; repository is the single source of truth, usually backed by the local database.
2. **MVVM vs MVI?**
   Both share unidirectional flow. MVI is stricter — explicit intents in, one immutable state out, through one clear path — while MVVM is looser about how events are handled.
3. **How do you handle a one-time event like navigation without it firing again on rotation?**
   Use a `SharedFlow` with no replay (or a `Channel`), not `StateFlow` — a `StateFlow` re-delivers its current value to any new collector.
4. **When would you skip a use-case layer?**
   For a simple screen with logic used in exactly one place — a use case there adds indirection without reuse or testing benefit.
5. **Why keep DTOs, entities, and domain models separate?**
   So a change in the API's field names doesn't ripple straight through to the UI, and business logic doesn't depend on network/database-specific shapes.

---

#### 15. Common Mistakes

1. Business logic living inside composables.
2. Using `StateFlow` for one-time events.
3. The `ViewModel` talking to the network directly, bypassing the repository as source of truth.
4. Over-applying use cases and clean architecture layers to a simple screen.
5. No consistent error model — different screens handling failures completely differently.

---

#### 16. Related Topics

1. `2` Kotlin Essentials — sealed classes as the UI state foundation
2. `5` UI with Jetpack Compose — where this architecture connects to the screen
3. `9` Local Storage & Offline-First — the database as source of truth in practice
4. `ARCH 19` Mobile App Architecture — the architect-level summary of this same topic

---

#### 17. Interview Must Remember

1. **State flows down, events flow up** — one direction, always.
2. **Repository = single source of truth**, usually the local database in an offline-first app.
3. **Sealed types model UI state**; the compiler enforces handling every case.
4. **One-time events need `SharedFlow`/`Channel`, not `StateFlow`.**
5. Use cases are a tool, **not a mandatory layer** — apply them where they add real value.
