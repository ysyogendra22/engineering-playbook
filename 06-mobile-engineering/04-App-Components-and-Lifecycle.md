# App Components & Lifecycle

Roadmap topic 4 · Stage 2: Building the App

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** an Android screen doesn't just run once and stop — the OS creates it, pauses it, destroys and recreates it, sometimes several times per minute. Knowing exactly when each of those happens, and what to do at each point, is what stops your app from losing data or crashing on rotation.

---

#### 1. Activity and the Single-Activity Approach — 🟢 Must Know

1. An **Activity** is a screen or entry point in the traditional Android model.
2. Most modern apps use a **single Activity**, with **Compose** (topic `5`) or **Fragments/Navigation** handling the actual screens inside it — simpler lifecycle management, one place to own navigation.

---

#### 2. The Lifecycle Callbacks — 🟢 Must Know

```text
onCreate → onStart → onResume → [ running, visible, interactive ]
   → onPause → onStop → onDestroy
```

1. **`onCreate`** — one-time setup (view binding, reading initial arguments).
2. **`onStart`/`onStop`** — visible but maybe not interactive / no longer visible.
3. **`onResume`/`onPause`** — fully interactive / losing focus (a dialog appears, another app comes forward).
4. **`onDestroy`** — final cleanup, may not always be called (the process can just be killed — see topic 4).

---

#### 3. Configuration Changes — 🟢 Must Know

*Rotation, language change, dark mode toggle — the Activity is destroyed and recreated.*

1. By default, a **configuration change** (screen rotation is the classic one) destroys and recreates the Activity, re-running `onCreate`.
2. This is **not** the same as process death (item 4) — the process stays alive, only the Activity instance is recreated. `ViewModel`s survive this automatically.

---

#### 4. Process Death and State Restoration — 🟢 Must Know

*The harder case: the whole process is gone, and `ViewModel`s don't survive it either.*

1. `ViewModel` survives configuration changes, but **not** process death (topic `1`).
2. **`SavedStateHandle`** — a small key-value store tied to the Activity/Fragment, saved and restored across process death, accessible from inside a `ViewModel`.
3. **`rememberSaveable`** — the Compose equivalent, for UI-local state that should survive both configuration changes and process death.

```kotlin
class NotesViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {
    var searchQuery: String
        get() = savedStateHandle["query"] ?: ""
        set(value) { savedStateHandle["query"] = value }   // survives process death
}
```

```text
Configuration change:  process alive → Activity destroyed → recreated → ViewModel survives
Process death:         process killed → everything gone → SavedStateHandle/rememberSaveable
                        is what's left to restore from
```

---

#### 5. `ViewModel`: What It Holds, What It Doesn't Survive — 🟢 Must Know

1. Holds UI state and business logic, outliving Activity recreation from configuration changes.
2. Does **not** survive process death, and does **not** hold a reference to a `View`, `Context`, or `Activity` — that would leak them.
3. Full architecture role covered in topic `6`.

---

#### 6. Intents — 🟢 Must Know

1. An **Intent** is a message that starts a component (an Activity, a Service) or requests an action.
2. **Explicit** — names the exact component to start (within your own app). **Implicit** — describes an action, and the OS finds an app that can handle it (share, open a URL).
3. Passing data and getting results back uses `Intent` extras and the `ActivityResult` APIs.

---

#### 7. Navigation and the Back Stack — 🟢 Must Know

1. The **back stack** tracks the screens the user has visited, so the system back button/gesture returns to the previous one.
2. The Navigation library (or Compose Navigation, topic `5`) manages this declaratively, instead of manual fragment transactions.

---

#### 8. Deep Links and App Links — 🟢 Must Know

1. A **deep link** is a URL that opens a specific screen inside the app.
2. **App links** are deep links verified to belong to your domain, so Android opens your app directly instead of a chooser dialog.
3. Deep links are untrusted input — validate them before acting on their data (`SD` security notes apply here too).

---

#### 9. Services — 🟡 Good to Know

1. A **Service** runs in the background without a UI. A **foreground service** shows a persistent notification and gets more leeway from the OS to keep running (covered further in topic `10`).

---

#### 10. Broadcast Receivers and Content Providers — 🟡 Good to Know

1. **Broadcast receiver** — responds to system-wide or app-wide events (network changed, boot completed).
2. **Content provider** — a structured way to share data between apps.

---

#### 11. Launch Modes and Task Behaviour — 🟡 Good to Know

Launch modes (`standard`, `singleTop`, `singleTask`, `singleInstance`) control whether a new Activity instance is created or an existing one is reused when navigating — relevant mainly for deep links and notification taps.

---

#### 12. Application Class and Startup — 🟡 Good to Know

The `Application` class runs once per process, before any screen — the place for one-time global setup (DI graph initialization, crash reporting). Keep it fast; it directly delays cold start (topic `11`).

---

#### 13. The Manifest — 🟡 Good to Know

The `AndroidManifest.xml` declares every component, requested permissions, and which components are `exported` (reachable from outside the app) — an important, often-overlooked security surface (topic `13`).

---

#### 14. iOS Equivalents — 🟡 Good to Know

`UIViewController`'s lifecycle (`viewDidLoad`, `viewWillAppear`, etc.) and the scene lifecycle map to Android's Activity/Fragment lifecycle — see topic `16`.

---

#### 15. Common Interview Questions

1. **What's the difference between a configuration change and process death?**
   A configuration change destroys and recreates the Activity, but the process stays alive — `ViewModel` survives it. Process death kills the whole process — only `SavedStateHandle`/`rememberSaveable` or persisted data survives.
2. **Where should you NOT store a reference to a `View` or `Activity`?**
   In a `ViewModel` — it outlives the Activity across configuration changes, so holding a reference to the old one leaks it.
3. **How would you restore a search query after the app is killed and reopened?**
   Store it in `SavedStateHandle` (or `rememberSaveable` in Compose) so it survives process death, not just a plain in-memory field.
4. **What's the danger of an "exported" component?**
   It can be triggered by other apps or the system — always validate any data it receives, the same way you'd validate untrusted network input.
5. **Explicit vs implicit intent?**
   Explicit names the exact component. Implicit describes an action and lets the OS pick a handler.

---

#### 16. Common Mistakes

1. Only testing rotation, and never testing actual process death (which can be forced from developer options) — many "it works on rotation" bugs fail under real process death.
2. Holding an Activity/View reference inside a `ViewModel`.
3. Treating deep link data as trusted without validation.
4. Doing heavy work in the `Application` class, slowing cold start.
5. Assuming `onDestroy` will always be called before the process ends.

---

#### 17. Related Topics

1. `1` Mobile Platform Basics — the process death this topic covers in depth
2. `5` UI with Jetpack Compose — `rememberSaveable` and Compose Navigation
3. `6` App Architecture — where `ViewModel` fits into the layers
4. `16` iOS & Swift Essentials — the `UIViewController` lifecycle equivalent

---

#### 18. Interview Must Remember

1. **Configuration change: process alive, Activity recreated, `ViewModel` survives.**
2. **Process death: everything gone — only `SavedStateHandle`/persisted data survives.**
3. Never hold a `View`/`Activity`/`Context` reference in a `ViewModel`.
4. Deep links and exported components are **untrusted input** — validate them.
