# UI with Jetpack Compose

Roadmap topic 5 · Stage 2: Building the App

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** Compose describes the UI as a function of state — you don't mutate views, you describe what the screen should look like for the current state, and Compose figures out what to redraw. Understanding recomposition is what separates "Compose that works" from "Compose that's smooth".

---

#### 1. Composables: UI as a Function of State — 🟢 Must Know

1. A **composable** is a function, annotated `@Composable`, that describes part of the UI based on its inputs.
2. Instead of `view.setText(...)` mutating an existing object, you write `Text(state.title)` — when `state.title` changes, Compose re-runs that function to redraw.

```kotlin
@Composable
fun NoteItem(note: Note, onClick: () -> Unit) {
    Text(text = note.title, modifier = Modifier.clickable { onClick() })
}
```

---

#### 2. State and Recomposition — 🟢 Must Know

*Recomposition is Compose re-running the composables whose state changed — and only those.*

1. When state read inside a composable changes, Compose schedules that composable (and only the ones that actually read that state) to run again.
2. Keeping recomposition **cheap** — small, focused composables, stable data types — is the core Compose performance skill (also covered in topic `11`).

---

#### 3. `remember`, `rememberSaveable`, State Hoisting — 🟢 Must Know

1. **`remember`** — keeps a value across recompositions (but not configuration changes or process death).
2. **`rememberSaveable`** — same, but also survives configuration changes and process death (built on `SavedStateHandle`, topic `4`).
3. **State hoisting** — move state up to the caller, so the composable itself becomes stateless and reusable, taking the value and an `onValueChange` callback instead of owning the state.

```kotlin
@Composable
fun SearchField(query: String, onQueryChange: (String) -> Unit) {   // hoisted — stateless, reusable
    TextField(value = query, onValueChange = onQueryChange)
}
```

---

#### 4. Layouts and Modifiers — 🟢 Must Know

1. **`Row`**, **`Column`**, **`Box`** — the three basic layout containers (horizontal, vertical, stacked).
2. **Modifiers** chain together, and **order matters** — `padding` before `clickable` gives a different tap target than the reverse.

```kotlin
Column(modifier = Modifier.padding(16.dp).fillMaxWidth()) { ... }
```

---

#### 5. Lists: `LazyColumn`, Keys, Item State — 🟢 Must Know

1. **`LazyColumn`** — only composes and lays out the items currently visible (like `RecyclerView`), not the whole list at once.
2. **`key`** on each item tells Compose how to track items across list changes — without it, item-level state (like scroll position or an expanded flag) can get scrambled when the list reorders.

```kotlin
LazyColumn {
    items(notes, key = { it.id }) { note ->    // key prevents state mix-ups on reorder
        NoteItem(note)
    }
}
```

---

#### 6. Side Effects — 🟢 Must Know

*Anything that isn't drawing UI — a network call, a log, a coroutine — needs to run inside a defined "effect", not directly in the composable body.*

1. **`LaunchedEffect(key)`** — runs a coroutine when the composable enters composition, and re-runs it if `key` changes.
2. **`DisposableEffect`** — like `LaunchedEffect`, but with explicit cleanup when the composable leaves composition (unregister a listener).
3. **`rememberCoroutineScope`** — a scope tied to the composable's lifecycle, for launching a coroutine from an event handler (like a button click), not automatically.

```kotlin
@Composable
fun NotesScreen(viewModel: NotesViewModel) {
    LaunchedEffect(Unit) {
        viewModel.loadNotes()          // runs once when this composable enters composition
    }
}
```

---

#### 7. Connecting a `ViewModel` with a Single UI State — 🟢 Must Know

The standard pattern: one `StateFlow<UiState>` exposed from the `ViewModel`, collected lifecycle-aware in Compose (topic `3`), driving the whole screen.

```kotlin
@Composable
fun NotesScreen(viewModel: NotesViewModel = hiltViewModel()) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    when (state) {
        is UiState.Loading -> LoadingSpinner()
        is UiState.Content -> NotesList(state.items)
        is UiState.Error -> ErrorMessage(state.message)
    }
}
```

---

#### 8. Navigation in Compose — 🟢 Must Know

Compose Navigation defines a `NavHost` with composable destinations, and a `NavController` to move between them — the declarative version of the back stack described in topic `4`.

---

#### 9. Material Theming — 🟡 Good to Know

`MaterialTheme` centralises colours, typography, and shapes as design tokens, so screens stay visually consistent and support light/dark theme switching (topic `14`) from one place.

---

#### 10. Stability and `derivedStateOf` — 🟡 Good to Know

1. Compose skips recomposing a composable whose inputs are "stable" and unchanged — an unstable type (like a plain, mutable `List`) can defeat this optimisation.
2. **`derivedStateOf`** — computes a value from other state, and only triggers recomposition when the *derived* result actually changes, not every time an input changes.

---

#### 11. Animations, Gestures, Custom Drawing — 🟡 Good to Know

Compose has a dedicated animation API (`animate*AsState`, `AnimatedVisibility`), gesture modifiers (`draggable`, `pointerInput`), and a `Canvas` for custom drawing.

---

#### 12. Previews and Testable UI — 🟡 Good to Know

`@Preview` renders a composable in Android Studio without running the app — fastest way to iterate on UI. Keeping composables stateless (via hoisting) also makes them easy to preview and test in isolation.

---

#### 13. The View System and Interop — 🟡 Good to Know

The older XML/View system (`RecyclerView`, `View` classes) still exists in many codebases. `AndroidView`/`ComposeView` let Compose and the View system interoperate during a gradual migration.

---

#### 14. iOS Equivalent — 🟡 Good to Know

SwiftUI is Apple's equivalent declarative UI framework, with very similar core ideas (state-driven views, a comparable side-effect model) — see topic `16`.

---

#### 15. Common Interview Questions

1. **What triggers recomposition?**
   A change to state that was read inside a composable during its last composition — Compose tracks these reads and only recomposes what actually depends on the changed state.
2. **What is state hoisting and why does it matter?**
   Moving state ownership up to the caller so a composable becomes stateless — more reusable, easier to test, and lets the caller (often a `ViewModel`) be the single source of truth.
3. **Why does `LazyColumn` need a `key`?**
   Without it, Compose tracks items by position, so reordering can scramble per-item state (scroll position, animations) that should have followed the item.
4. **`LaunchedEffect` vs `rememberCoroutineScope`?**
   `LaunchedEffect` runs automatically tied to composition and a key. `rememberCoroutineScope` gives you a scope to launch coroutines from event callbacks (like a click), which aren't automatically tied to composition.
5. **How do you keep recomposition cheap?**
   Small, focused composables; stable/immutable data classes; hoisting expensive computation into `derivedStateOf` or the `ViewModel`; avoiding unnecessary state reads high up the tree.

---

#### 16. Common Mistakes

1. Putting business logic directly inside a composable instead of the `ViewModel`.
2. Forgetting `key` on `LazyColumn` items.
3. Launching a coroutine directly in the composable body instead of inside `LaunchedEffect`.
4. Ignoring recomposition counts until performance actually suffers (topic `11`).
5. Not hoisting state, leading to composables that are hard to reuse or test.

---

#### 17. Related Topics

1. `3` Coroutines & Flow — `LaunchedEffect`, `collectAsStateWithLifecycle`
2. `4` App Components & Lifecycle — `rememberSaveable` and process death
3. `6` App Architecture — the single-UI-state pattern this connects to
4. `11` Performance & Memory — Compose-specific performance tuning
5. `16` iOS & Swift Essentials — SwiftUI as the equivalent

---

#### 18. Interview Must Remember

1. **UI is a function of state** — composables re-run (recompose) when the state they read changes.
2. **State hoisting** makes composables stateless and reusable.
3. **`LazyColumn` + `key`** for correct, efficient lists.
4. Side effects (coroutines, cleanup) belong in **`LaunchedEffect`/`DisposableEffect`**, not the composable body directly.
