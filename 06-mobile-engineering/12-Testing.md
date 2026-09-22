# Testing

Roadmap topic 12 · Stage 4: Quality

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** mobile testing follows the same test pyramid as backend testing (`BE 7`) — many fast unit tests, fewer integration tests, very few slow UI tests. What's mobile-specific is testing coroutines, Compose UI, and Room, each of which needs its own small set of tools.

---

#### 1. The Test Pyramid — 🟢 Must Know

```text
        /\
       /UI\        few, slow, brittle — the whole screen, real device/emulator
      /----\
     /Integr-\     some — a repository with a real (in-memory) database
    /----------\
   / Unit tests  \  many, fast — ViewModels, use cases, mappers
  /----------------\
```

Most of an app's test coverage should live at the bottom — fast, focused, and reliable.

---

#### 2. Local Unit Tests — 🟢 Must Know

`ViewModel`s, use cases, and mappers are plain Kotlin (or close to it) and testable with fast, JVM-only unit tests — no emulator or device needed.

```kotlin
@Test
fun `loading notes updates state to Content`() = runTest {
    val fakeRepo = FakeNotesRepository(notes = listOf(sampleNote))
    val viewModel = NotesViewModel(fakeRepo)

    viewModel.loadNotes()

    assertEquals(UiState.Content(listOf(sampleNote)), viewModel.uiState.value)
}
```

---

#### 3. Fakes vs Mocks — 🟢 Must Know

1. A **fake** is a real, simplified working implementation (an in-memory repository instead of a network one).
2. A **mock** records calls and lets you assert on them (`verify(api).getNotes()`).
3. **Prefer fakes** — they test real behaviour, not just "was this method called", and tend to be more robust to refactoring.

---

#### 4. Testing Coroutines and Flows — 🟢 Must Know

1. **`runTest`** — a coroutine test builder that runs suspend code on a controlled, virtual-time test dispatcher, so tests involving `delay()` don't actually wait.
2. **Test dispatchers** — inject a test dispatcher in place of `Dispatchers.Main`/`IO` in tests, so coroutine code is deterministic.
3. **Turbine** — a small library for asserting on a sequence of `Flow` emissions cleanly.

```kotlin
@Test
fun `search emits results after debounce`() = runTest {
    viewModel.searchQuery.value = "note"
    viewModel.results.test {                  // Turbine
        assertEquals(emptyList<Note>(), awaitItem())   // initial
        assertEquals(listOf(sampleNote), awaitItem())  // after debounce
    }
}
```

---

#### 5. Write Testable Code — 🟢 Must Know

Injected dependencies (topic `7`) and no hidden globals (singletons accessed directly, static mutable state) are what actually make the tests above possible — testability is a design property, not something added after the fact.

---

#### 6. Compose UI Tests and Espresso — 🟢 Must Know

1. **Compose UI testing** — uses semantic nodes (`onNodeWithText`, `onNodeWithTag`) to find and interact with composables, and assert on what's displayed.
2. **Espresso** — the equivalent for the View-based system, for code not yet migrated to Compose.

```kotlin
@Test
fun clickingNoteOpensDetail() {
    composeTestRule.onNodeWithText("My Note").performClick()
    composeTestRule.onNodeWithTag("detail_screen").assertIsDisplayed()
}
```

---

#### 7. Testing Repositories — 🟢 Must Know

A repository test typically combines a **fake network** (returns canned responses) with an **in-memory Room database** (real SQL behaviour, no disk I/O) — fast, but still exercises real query and mapping logic.

---

#### 8. Robolectric and Instrumented Tests — 🟡 Good to Know

1. **Robolectric** runs Android-framework-dependent tests on the JVM (fast, no emulator) by simulating the framework.
2. **Instrumented tests** run on a real device or emulator — slower, but the only way to test some real platform behaviour.

---

#### 9. Screenshot Tests — 🟡 Good to Know

Render a composable and compare the output pixel-for-pixel against a saved reference image — catches unintended visual regressions that functional tests miss.

---

#### 10. Testing Migrations and Offline Behaviour — 🟡 Good to Know

A dedicated test that runs each Room migration against real, populated sample data (topic `9`) — catching data-loss bugs before they hit real users.

---

#### 11. CI — 🟡 Good to Know

Running the test suite on every change (topic `15`) — keep it **fast** (favour unit tests) and **reliable** (no flaky tests slowing everyone down or eroding trust in CI).

---

#### 12. Flaky Tests — 🟡 Good to Know

Common causes: real time/`delay()` instead of a test dispatcher, un-awaited coroutines, animation timing, or tests that depend on execution order. Fix the root cause — don't just retry a flaky test until it passes.

---

#### 13. iOS Equivalent — 🟡 Good to Know

**XCTest** (and the newer Swift Testing) plays the same role for iOS — see topic `16`.

---

#### 14. Common Interview Questions

1. **How do you test a `ViewModel` that uses coroutines?**
   `runTest` with a test dispatcher, injecting fake dependencies, and asserting on the resulting `StateFlow` value (or `Flow` emissions with Turbine).
2. **Fakes vs mocks — which do you prefer, and why?**
   Fakes, generally — a real, simplified working implementation tests actual behaviour and survives refactors better than asserting on exact method calls.
3. **What makes code hard to test on Android, and how do you avoid it?**
   Hidden dependencies (singletons, static state) and framework coupling (holding a `Context` directly in business logic). Constructor injection (topic `7`) and clean architecture layering (topic `6`) fix both.
4. **How would you test a Room migration?**
   Write a dedicated migration test that creates a database at the old schema version, populates it with sample data, runs the migration, and asserts the data and new schema are both correct.
5. **How do you keep a CI test suite fast and reliable?**
   Lean heavily on the test pyramid's base (fast unit tests), use test dispatchers instead of real delays, and fix flaky tests at the root cause instead of retrying them.

---

#### 15. Common Mistakes

1. Writing mostly slow UI tests instead of leaning on fast unit tests.
2. Using real `delay()`/time in tests instead of a test dispatcher.
3. Business logic tightly coupled to Android framework classes, making it hard to unit test.
4. No migration tests, discovering a broken migration only after users hit it.
5. Tolerating flaky tests instead of fixing their root cause.

---

#### 16. Related Topics

1. `3` Coroutines & Flow — what `runTest` and Turbine are testing
2. `7` Dependency Injection & Modularization — why constructor injection enables testability
3. `9` Local Storage & Offline-First — migration testing
4. `BE 7` Testing & Debugging — the shared testing principles from the backend side

---

#### 17. Interview Must Remember

1. **Test pyramid**: many unit tests, some integration, few UI tests.
2. **`runTest` + a test dispatcher** for deterministic coroutine tests; **Turbine** for `Flow` assertions.
3. **Prefer fakes over mocks** where practical.
4. Testability comes from **injected dependencies and no hidden globals** — a design choice, not an afterthought.
5. **Test Room migrations explicitly**, against real data.
