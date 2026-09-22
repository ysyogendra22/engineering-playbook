# Dependency Injection & Modularization

Roadmap topic 7 · Stage 2: Building the App

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** DI means a class receives what it needs instead of creating it itself — the same idea as OkHttp interceptors being handed to a client rather than built inside it. Modularization is the same idea at a bigger scale: split the app into pieces with clear, small public APIs, instead of one giant tangle.

---

#### 1. What DI Solves — 🟢 Must Know

1. A class that **creates its own dependencies** (`val api = RetrofitClient()`) is hard to test — you can't swap in a fake for tests, and it's tightly coupled to one specific implementation.
2. A class that **receives** its dependencies (through its constructor) can be given a real implementation in production and a fake one in tests — this is the whole point of DI.

```kotlin
// Hard to test: creates its own dependency
class NotesRepository {
    private val api = RetrofitClient.create()
}

// Testable: dependency is injected
class NotesRepository(private val api: NotesApi) { ... }   // pass a fake NotesApi in tests
```

---

#### 2. Hilt, Koin, Manual DI — 🟢 Must Know

1. **Hilt** (built on Dagger) — compile-time dependency injection; catches missing/circular dependencies at build time, generates the wiring code, integrates deeply with Android components (`@AndroidEntryPoint`, `@HiltViewModel`).
2. **Koin** — a lightweight, Kotlin-DSL-based DI library; wiring is checked at runtime, not compile time — simpler to set up, slower to catch mistakes.
3. **Manual DI** — you wire dependencies together yourself, usually via a simple container class — no library, full control, more boilerplate as the app grows.

---

#### 3. Scopes — 🟢 Must Know

1. **Application scope** — one instance for the whole app's lifetime (a database instance, a network client).
2. **Activity scope** — one instance per Activity.
3. **`ViewModel` scope** — one instance per `ViewModel`, matching its own lifecycle (topic `4`).
4. Picking the right scope avoids both wasteful re-creation and accidental sharing of state that should be screen-local.

---

#### 4. Constructor Injection as the Default — 🟢 Must Know

Prefer passing dependencies through the constructor over field injection or service locators — it makes a class's requirements explicit and visible at a glance, and it's what makes plain unit testing (topic `12`) straightforward, without needing the DI framework running at all.

---

#### 5. Module Structure — 🟢 Must Know

```text
:app                    ← thin, wires everything together, holds the Application class
:feature:notes          ← one feature, its own UI + ViewModel
:feature:profile        ← another feature
:core:network           ← shared networking setup
:core:database          ← shared Room setup
:core:ui                ← shared design system components
```

1. **Feature modules** — one per user-facing feature, so teams can work independently and build times scale better.
2. **Core/shared modules** — cross-cutting concerns used by multiple features.

---

#### 6. Module Boundaries — 🟢 Must Know

1. Keep each module's **public API small** — expose only what other modules genuinely need; keep implementation details internal.
2. **Dependency direction** matters: feature modules depend on core modules, never the reverse; feature modules generally shouldn't depend on each other directly (`ARCH 8`).

---

#### 7. API and Implementation Module Split — 🟡 Good to Know

Splitting a module into an `:api` module (interfaces only) and an `:impl` module (the real implementation) lets other modules depend only on the interface — faster incremental builds, since a change to the implementation doesn't force everything depending on the API to recompile.

---

#### 8. Build Speed — 🟡 Good to Know

1. More, smaller modules let Gradle build and cache them **in parallel**, and skip rebuilding unaffected ones.
2. **Avoid circular module dependencies** — they force Gradle to treat the cycle as one big unit, losing the parallelism benefit entirely.

---

#### 9. Version Catalogs and Convention Plugins — 🟡 Good to Know

1. A **version catalog** (`libs.versions.toml`) centralises dependency versions in one file, instead of repeating them across every module's build file.
2. **Convention plugins** share common Gradle configuration (Kotlin options, lint rules) across modules without copy-pasting build script code.

---

#### 10. Dynamic Feature Modules and App Size — 🟡 Good to Know

A **dynamic feature module** can be downloaded on demand after install, instead of bundled in the initial download — useful for large, optional features, to keep the base app size small.

---

#### 11. When Modularization Isn't Worth It Yet — 🟡 Good to Know

For a small app or an early-stage product, heavy modularization adds real overhead (build config, module boundaries to maintain) before it pays off. A clean **package structure inside one module** is often the right starting point — modularize once the team or codebase size actually demands it (`ARCH 8`).

---

#### 12. Common Interview Questions

1. **Why use dependency injection instead of creating dependencies directly?**
   Testability (swap in fakes), decoupling from specific implementations, and centralised control over object lifetimes/scopes.
2. **Hilt vs Koin?**
   Hilt checks the dependency graph at compile time and integrates tightly with Android components; Koin is a lighter, runtime-checked Kotlin DSL — Hilt catches mistakes earlier, Koin is quicker to set up.
3. **What scope would you use for a database instance?**
   Application scope — one instance shared for the app's whole lifetime.
4. **How do you keep feature modules independent?**
   Small public APIs, no direct feature-to-feature dependencies, shared code lives in core modules that features depend on, never the reverse.
5. **When would you NOT modularize a project?**
   Early-stage or small apps, where the overhead of module boundaries outweighs the build-speed and team-independence benefits.

---

#### 13. Common Mistakes

1. Classes creating their own dependencies instead of receiving them — hard to test.
2. Over-scoping (making everything Application-scoped) or under-scoping (recreating expensive objects per screen).
3. Circular dependencies between modules, killing Gradle's parallel build benefit.
4. Modularizing a tiny app before it needs it, paying the overhead with none of the payoff.
5. Large, leaky public APIs on feature modules, defeating the purpose of the boundary.

---

#### 14. Related Topics

1. `6` App Architecture — the layers DI wires together
2. `12` Testing — why constructor injection matters for testability
3. `ARCH 8` Modularity, Coupling & Boundaries — the architect-level view of module design

---

#### 15. Interview Must Remember

1. **DI = receive dependencies, don't create them** — enables testing with fakes.
2. **Constructor injection is the default** — explicit, testable without a DI framework running.
3. Match the **scope** to the dependency's real lifetime (Application, Activity, `ViewModel`).
4. **Modularize for a reason** (build speed, team independence) — not by default on a small app.
