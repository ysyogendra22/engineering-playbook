# Cross-Platform & Kotlin Multiplatform

Roadmap topic 17 · Stage 6: Beyond Android · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** cross-platform tools trade some native control for writing (parts of) an app once instead of twice. Kotlin Multiplatform is the option that lets you keep writing Kotlin and native UI, sharing only what genuinely benefits from being shared — usually the logic, not the screens.

---

#### 1. The Options — 🟢 Must Know

| Option | Approach |
|---|---|
| Native (separate Android + iOS apps) | Full platform control, two codebases |
| Kotlin Multiplatform (KMP) | Share business logic/data in Kotlin; UI can stay fully native, or use Compose Multiplatform |
| Flutter | One UI framework (Dart) rendering its own widgets on both platforms |
| React Native | One UI framework (JavaScript/TypeScript) bridging to native components |

---

#### 2. What KMP Shares — 🟢 Must Know

1. **Business logic, data, and networking** — the layers least tied to platform-specific UI (repository, use cases, networking, serialization) move into a shared Kotlin module.
2. **UI stays native** by default — Compose on Android, SwiftUI/UIKit on iOS — or you can go further with **Compose Multiplatform**, sharing UI code too (item 4).
3. This mirrors the architecture layers from topic `6` closely: the data and domain layers are natural candidates to share; the UI layer is the natural place to keep native.

```text
Android app (Compose UI)  ─┐
                            ├──→  Shared Kotlin module (repository, use cases, networking, models)
iOS app (SwiftUI UI)       ─┘
```

---

#### 3. How to Choose — 🟢 Must Know

1. **Team skills** — a Kotlin-fluent team gets more leverage from KMP than from Dart (Flutter) or JS/TS (React Native).
2. **Performance needs** — KMP compiles to native code on each platform (no bridge/interpreter overhead for shared logic); Flutter and React Native have their own performance characteristics worth evaluating for the specific app.
3. **Platform-specific features** — how much of the app needs deep platform integration (camera, widgets, background work) affects how much value native UI on each side provides.
4. **Speed and long-term cost** — shared logic reduces duplicate bugs and duplicate work over time, at the cost of some initial setup and tooling overhead.

---

#### 4. `expect`/`actual` — 🟡 Good to Know

A mechanism for declaring a piece of functionality in shared code (`expect`) and providing a platform-specific implementation for each target (`actual`) — used when something can't be written in pure shared Kotlin (accessing a platform API directly).

```kotlin
// shared code
expect fun currentTimeMillis(): Long

// androidMain
actual fun currentTimeMillis(): Long = System.currentTimeMillis()

// iosMain
actual fun currentTimeMillis(): Long = NSDate().timeIntervalSince1970.toLong() * 1000
```

---

#### 5. Compose Multiplatform — 🟡 Good to Know

Extends Compose beyond Android, letting UI code (not just logic) be shared across platforms. **Check its current maturity per target platform** before committing — cross-platform UI frameworks evolve quickly, and platform support/stability varies by version and target.

---

#### 6. Libraries That Work in Shared Code — 🟡 Good to Know

**Ktor** (networking, topic `8`), **kotlinx.serialization** (JSON), and **SQLDelight** (typed SQL, generating code for multiple platforms) are commonly used in KMP shared modules — chosen specifically because they don't depend on Android-only or iOS-only APIs.

---

#### 7. Testing and CI for Shared Code — 🟡 Good to Know

Shared module tests can often run on the JVM alone (fast), while platform-specific `actual` implementations need their own platform-specific test runs — plan CI accordingly.

---

#### 8. Migrating Step by Step — 🟡 Good to Know

Don't attempt a big-bang rewrite: **share one module first** (often networking or a well-isolated data layer), prove it works end-to-end on both platforms, then expand — the same incremental philosophy as any large migration (`ARCH 16`).

---

#### 9. Common Problems — 🟡 Good to Know

1. **Platform gaps** — a library or API you need may not have a Kotlin Multiplatform-compatible version yet.
2. **Debugging** — stepping through shared Kotlin code from Xcode (for the iOS side) can be less smooth than native iOS debugging.
3. **Tooling** — the KMP toolchain and build setup add real complexity on top of a normal Android or iOS project.

---

#### 10. Common Interview Questions

1. **What does Kotlin Multiplatform actually share, and what stays native?**
   Business logic, data, networking, and models are shared in Kotlin; UI typically stays native (Compose on Android, SwiftUI/UIKit on iOS), unless also using Compose Multiplatform.
2. **KMP vs Flutter vs React Native — how do you choose?**
   Team's existing skills, performance needs, how much native platform integration the app needs, and long-term maintenance cost of one shared codebase vs the bridge/rendering overhead of the other frameworks.
3. **What is `expect`/`actual` for?**
   Declaring a piece of functionality in shared code without a platform-agnostic implementation, then providing a real implementation per platform.
4. **How would you migrate an existing native Android + iOS app pair to KMP?**
   Incrementally — share one well-isolated module first (often networking or data), validate it on both platforms, then expand outward, rather than rewriting everything at once.
5. **What are the practical downsides of KMP today?**
   Library ecosystem gaps for some Kotlin Multiplatform-specific needs, some debugging friction on the iOS side, and added build/tooling complexity.

---

#### 11. Common Mistakes

1. Trying to share UI code before the team has validated sharing logic works well for the project.
2. A big-bang rewrite into KMP instead of an incremental, module-by-module migration.
3. Choosing a cross-platform approach based on hype rather than the team's actual skills and the app's actual needs.
4. Assuming every library or platform API has a ready Kotlin Multiplatform equivalent.

---

#### 12. Related Topics

1. `6` App Architecture — the layers that map naturally onto "shared" vs "native UI"
2. `8` Networking — Ktor as a KMP-friendly networking choice
3. `16` iOS & Swift Essentials — what stays native alongside a KMP shared module
4. `ARCH 16` Evolutionary Architecture & Technical Debt — the incremental-migration philosophy

---

#### 13. Interview Must Remember

1. **KMP shares logic/data by default; UI is usually still native** — Compose Multiplatform is the option to also share UI.
2. **Choose based on team skills, performance needs, and long-term cost** — not by default or by hype.
3. **`expect`/`actual`** bridges shared code to platform-specific APIs.
4. **Migrate incrementally** — one shared module first, expand from there.
