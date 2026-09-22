# iOS & Swift Essentials

Roadmap topic 16 · Stage 6: Beyond Android · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** if Android is your main platform, this topic is a translation guide — most of what you already know has a direct iOS equivalent. Learning the mapping is far faster than learning iOS from zero.

---

#### 1. Concept Map — 🟢 Must Know

| Android (Kotlin) | iOS (Swift) |
|---|---|
| Activity / Fragment | View controller / scene |
| Jetpack Compose | SwiftUI |
| Room | Core Data or SwiftData |
| Coroutines, `Flow` | Swift concurrency (`async`/`await`), `AsyncSequence` |
| `ViewModel` | Same term, same role, in an MVVM-style SwiftUI app |
| Hilt/Koin | Manual DI, or a lightweight framework — no single dominant standard |
| WorkManager | `BGTaskScheduler` |
| FCM | APNs (Apple Push Notification service) |
| Android Keystore | Keychain |
| Gradle | Xcode build system / Swift Package Manager |

Keep this table as the anchor — nearly everything else in this topic is filling in the right-hand column.

---

#### 2. Swift Basics — 🟢 Must Know

1. **Optionals** (`String?`) — Swift's null safety, directly analogous to Kotlin's nullable types (`06-mobile-engineering/2`).
2. **Structs vs classes** — structs are value types (copied on assignment), classes are reference types (shared on assignment) — a bigger everyday distinction in Swift than in Kotlin, where most things are reference types.
3. **Enums with associated values** — Swift's enums can carry different data per case, playing the same role Kotlin's sealed classes play for modelling state (topic `2`).
4. **Protocols** — Swift's equivalent of Kotlin interfaces.

```swift
enum UiState {
    case loading
    case content([Note])       // associated value — like a sealed class subtype
    case error(String)
}
```

---

#### 3. ARC and Retain Cycles — 🟢 Must Know

1. **ARC (Automatic Reference Counting)** — Swift's memory management: an object is deallocated once nothing references it, tracked by counting references.
2. A **retain cycle** happens when two objects hold strong references to each other, so neither's count ever reaches zero — a memory leak, conceptually similar to Android's "held `Context`" leaks (topic `11`).
3. **`weak`** and **`unowned`** references break the cycle — `weak` for a reference that can become `nil`, `unowned` when you're certain the referenced object always outlives the reference.

```swift
class ViewModel {
    var onUpdate: (() -> Void)?
}
// A closure capturing `self` strongly, stored on self, is a retain cycle:
viewModel.onUpdate = { self.refresh() }              // leak
viewModel.onUpdate = { [weak self] in self?.refresh() }   // fixed
```

---

#### 4. Swift Concurrency — 🟢 Must Know

1. **`async`/`await`** — directly analogous to Kotlin's `suspend` functions (topic `3`).
2. **Actors** — a Swift concurrency primitive that protects mutable state from concurrent access automatically, similar in purpose to Kotlin's `Mutex`.
3. **`@MainActor`** — marks code that must run on the main thread, the Swift equivalent of `Dispatchers.Main`.

---

#### 5. UIKit vs SwiftUI — 🟢 Must Know

1. **UIKit** — the older, imperative UI framework (roughly the View system's role, topic `5`).
2. **SwiftUI** — the modern, declarative framework: UI as a function of state, recomposition-like updates — directly analogous to Compose.

---

#### 6. Keychain — 🟢 Must Know

iOS's secure storage for secrets (tokens, credentials), backed by the device's secure hardware where available — the direct equivalent of Android Keystore-backed encrypted storage (topic `13`).

---

#### 7. SwiftUI State — 🟡 Good to Know

`@State` (local, owned state), `@Binding` (a hoisted, two-way connection to a parent's state — like Compose's state hoisting, topic `5`), `@Observable`/`@StateObject` (external, observable state sources, like a `ViewModel`).

---

#### 8. Combine and `AsyncSequence` — 🟡 Good to Know

**Combine** was Apple's reactive streams framework (playing a role similar to `Flow`); **`AsyncSequence`** is the newer, `async`/`await`-native way to represent a stream of values over time — increasingly the preferred choice in new code.

---

#### 9. `URLSession` — 🟡 Good to Know

iOS's foundational networking API, the rough equivalent of OkHttp (topic `8`).

---

#### 10. Core Data and SwiftData — 🟡 Good to Know

Core Data is the long-established local persistence framework; SwiftData is Apple's newer, more Swift-native alternative — both play Room's role (topic `9`) as the local source of truth.

---

#### 11. App Lifecycle and APNs — 🟡 Good to Know

Scene-based app lifecycle callbacks map to Activity/Fragment lifecycle (topic `4`); `BGTaskScheduler` maps to WorkManager, and **APNs** maps to FCM for push notifications (topic `10`).

---

#### 12. Testing — 🟡 Good to Know

**XCTest** (established) and **Swift Testing** (newer) play the role of JUnit/Compose testing tools (topic `12`).

---

#### 13. Distribution — 🟡 Good to Know

Xcode handles building and signing; **TestFlight** is the staged-rollout/beta-testing equivalent of a Google Play release track; App Store review tends to be stricter and slower than Google Play's (topic `15`, `1`).

---

#### 14. Swift Package Manager — 🟡 Good to Know

Apple's dependency and modularization tool — the rough equivalent of Gradle modules and dependency management (topic `7`).

---

#### 15. Common Interview Questions

1. **How would you explain Kotlin coroutines to someone who only knows Swift?**
   Directly analogous to `async`/`await`: a `suspend` function pauses without blocking a thread, the same way an `async` Swift function does.
2. **What's the iOS equivalent of a memory leak from a held `Context`?**
   A retain cycle — two objects (often a closure capturing `self` strongly) holding strong references to each other, fixed with `weak`/`unowned`, the same way Android fixes it by not holding a long-lived `Context` reference.
3. **SwiftUI vs Jetpack Compose — how similar are they really?**
   Both are declarative, state-driven UI frameworks with a similar recomposition/re-render model; the concepts map closely even though the exact APIs (`@State` vs `remember`, for example) differ.
4. **What's the iOS equivalent of WorkManager?**
   `BGTaskScheduler`, for deferrable background work — though iOS's background execution model is generally more restrictive than Android's.
5. **If you know Room well, how fast could you pick up Core Data or SwiftData?**
   The core ideas transfer directly — entities, migrations, observing changes to update the UI — the main work is learning the new API surface, not the underlying concepts.

---

#### 16. Common Mistakes

1. Assuming iOS has no equivalent restrictions (background work, main-thread rules) just because they're less familiar — most Android constraints have a real iOS counterpart.
2. Forgetting `weak self` in a closure stored on the object it captures, creating a retain cycle.
3. Treating SwiftUI and Compose as unrelated, instead of leaning on the strong conceptual overlap to learn faster.
4. Assuming Combine is still the default choice for new code — `async`/`await` and `AsyncSequence` are increasingly preferred.

---

#### 17. Related Topics

1. `2` Kotlin Essentials — the Swift optionals/sealed-class comparisons in this topic
2. `3` Coroutines & Flow — the async/await and Mutex/actor comparisons
3. `5` UI with Jetpack Compose — the SwiftUI comparison
4. `11` Performance & Memory — retain cycles vs Android memory leaks
5. `17` Cross-Platform & Kotlin Multiplatform — sharing code between both platforms instead of maintaining two apps

---

#### 18. Interview Must Remember

1. **Use the concept map** — most Android knowledge has a direct iOS analogue.
2. **ARC + retain cycles** is iOS's version of memory leaks; `weak`/`unowned` is the fix.
3. **`async`/`await`** ≈ Kotlin coroutines. **SwiftUI** ≈ Compose. **Keychain** ≈ Android Keystore.
4. Learning iOS on top of solid Android knowledge is mostly **learning new APIs for concepts you already understand**.
