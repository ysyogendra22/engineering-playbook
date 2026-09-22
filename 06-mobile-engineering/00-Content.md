# Mobile Engineering: Learning & Interview Roadmap

For a mobile engineer preparing for Android and mobile interviews, and growing toward senior and architect level.
**Android with Kotlin is the main path.** Each topic gives the iOS equivalent where it exists, so you can talk about both. Topic 16 is a short iOS guide.
This folder has **its own numbering, 1 to 22**. Each topic gets its own doc later.

**How to read references:** a plain number (`7`) is a topic in this folder. `BE 3` is topic 3 in `04-backend-engineering`. `SD 30` is topic 30 in `05-system-design`. `ARCH 19` is topic 19 in `09-architecture`. `DB 21` is topic 21 in `10-database`. `AI 19` is topic 19 in `08-artificial-intelligence`.

**How this fits with the other folders:** `SD 30` (mobile-specific system design), `ARCH 19` (mobile app architecture overview), `DB 21` (mobile databases), and `AI 19–20` (AI on mobile) give short overviews. This folder is the **full mobile path** and goes deeper on each. Where a topic already exists there, it links instead of repeating.

**Marks:**

| Mark | Meaning |
|---|---|
| 🟢 | **Must have.** Expected in most mobile interviews. Learn first. |
| 🟡 | **Good to have.** Learn after the 🟢 items are solid. |
| (New) | Added beyond the basics, or a newer area that is still changing. |

---

## Index

| #   | Topic                                       | Stage                    |
| --- | ------------------------------------------- | ------------------------ |
| 1   | Mobile Platform Basics                      | 1. Foundations           |
| 2   | Kotlin Essentials                           | 1. Foundations           |
| 3   | Coroutines & Flow                           | 1. Foundations           |
| 4   | App Components & Lifecycle                  | 2. Building the App      |
| 5   | UI with Jetpack Compose                     | 2. Building the App      |
| 6   | App Architecture                            | 2. Building the App      |
| 7   | Dependency Injection & Modularization       | 2. Building the App      |
| 8   | Networking                                  | 3. Data & Background     |
| 9   | Local Storage & Offline-First               | 3. Data & Background     |
| 10  | Background Work & Notifications             | 3. Data & Background     |
| 11  | Performance & Memory                        | 4. Quality               |
| 12  | Testing                                     | 4. Quality               |
| 13  | Security                                    | 4. Quality               |
| 14  | Accessibility, Localization & Adaptive UI   | 4. Quality               |
| 15  | Build, Release & Monitoring                 | 5. Shipping              |
| 16  | iOS & Swift Essentials (New)                | 6. Beyond Android        |
| 17  | Cross-Platform & Kotlin Multiplatform (New) | 6. Beyond Android        |
| 18  | Mobile System Design                        | 7. Mobile in the System  |
| 19  | Device Capabilities & Permissions           | 7. Mobile in the System  |
| 20  | AI in Mobile Apps (New)                     | 7. Mobile in the System  |
| 21  | Mobile Interview Answer Points (New)        | 8. Interview & Practice  |
| 22  | Practice: Projects & Exercises              | 8. Interview & Practice  |

**Short on time:** 1, 2, 3, 4, 5, 6, 8, 9, 11, 13, 18, 21. 🟢 items only.

**Glossary:** the terms to learn first are listed at the end, each with a priority mark and the topic that explains it.

---

# What to Follow on Any Feature or App

*The same ten steps work for a new screen, a new feature, or a new app. Write each output down, briefly.*

| Step | Question to answer | Output |
|---|---|---|
| 1. Understand the flow | What does the user do? What are all the states: loading, empty, error, offline, partial? | User flow and a list of screen states |
| 2. Agree the data contract | What does the backend send? How is it paged, versioned, and how do errors look? | API contract and error model (`BE 3`, topic 8) |
| 3. Choose the structure | Where does each piece of logic live? What is the source of truth? | UI state model, layers, repository (topics 6, 7) |
| 4. Survive the system | What happens on rotation, process death, and when the app goes to the background? | Lifecycle and state-restoration plan (topic 4) |
| 5. Design for failure and offline | What if the network is slow or gone, or a request repeats? | Cache, retry, sync rules (topics 8, 9) |
| 6. Set a performance budget | What must stay off the main thread? How fast must it start and scroll? | Threading plan, startup and frame targets (topics 3, 11) |
| 7. Protect the user | What data is stored, where, and who can read it? Which permissions are needed? | Storage and permission decisions (topics 13, 19) |
| 8. Plan the tests | What must never break? | Unit, integration, and UI test plan (topic 12) |
| 9. Plan the release | How does it roll out? How do old app versions keep working? | Feature flag, staged rollout, backward-compatibility check (topic 15, `SD 30`) |
| 10. Measure after launch | Is it working for real users? | Crash-free rate, slow starts, analytics, feedback (topic 15) |

**Priority order when time is short:** steps 1, 3, 4, and 5. Most mobile bugs come from missing states, lost state on process death, and work that assumes a perfect network.

---

# Stage 1: Foundations

## 1. Mobile Platform Basics

- 🟢 App sandbox: each app has its own process and private storage
- 🟢 Runtime permissions: ask when needed, handle "no"
- 🟢 The main (UI) thread rule: never block it
- 🟢 The OS can kill your app at any time in the background
- 🟢 App package and distribution: APK, AAB (App Bundle), Google Play; IPA and the App Store
- 🟢 OS versions and device variety: min SDK, target SDK, screen sizes and densities
- 🟢 Old app versions stay in use for years (`SD 30`)
- 🟡 Android vs iOS: main differences in app model, background rules, and distribution
- 🟡 How an app starts: process, application class, first screen
- 🟡 App stores: review, policies, and store listing basics
- 🟡 Tools: Android Studio, Gradle, ADB, emulator vs real device

## 2. Kotlin Essentials

- 🟢 Null safety: nullable types, `?.`, `?:`, `!!` and why to avoid it
- 🟢 `val` vs `var`, and immutability by default
- 🟢 Data classes, sealed classes and interfaces, enums, and modelling states with them
- 🟢 Functions: default and named arguments, extension functions
- 🟢 Lambdas and higher-order functions
- 🟢 Collections and their operators (`map`, `filter`, `groupBy`, `fold`), and sequences
- 🟢 Scope functions: `let`, `apply`, `also`, `run`, `with`
- 🟡 Generics, variance (`in`, `out`) at a basic level
- 🟡 `object`, `companion object`, and singletons
- 🟡 Delegation: `by lazy`, property delegates, class delegation
- 🟡 `inline`, value classes, and when they matter
- 🟡 Kotlin vs Java interop, and common differences
- 🟡 Coding conventions and idiomatic Kotlin

## 3. Coroutines & Flow

- 🟢 Why concurrency: keep the main thread free
- 🟢 Coroutines and `suspend` functions
- 🟢 Dispatchers: `Main`, `IO`, `Default`, and choosing one
- 🟢 Structured concurrency: scopes, jobs, and child coroutines
- 🟢 `viewModelScope`, `lifecycleScope`, and why not `GlobalScope`
- 🟢 Cancellation is cooperative, and handling it properly
- 🟢 Exceptions: `try/catch`, `CoroutineExceptionHandler`, `supervisorScope`
- 🟢 Flow: cold streams, `collect`, common operators (`map`, `filter`, `combine`, `flatMapLatest`, `debounce`)
- 🟢 `StateFlow` and `SharedFlow`: hot flows for state and events
- 🟢 Collecting flows safely in the UI (lifecycle-aware collection)
- 🟡 `async`/`await` and running work in parallel
- 🟡 Channels, `buffer`, `conflate`, and back-pressure
- 🟡 `callbackFlow` and wrapping callback APIs
- 🟡 Testing coroutines and flows
- 🟡 Race conditions, `Mutex`, and thread-safe state
- 🟡 Legacy names: threads, `Handler`, `AsyncTask`, RxJava
- 🟡 iOS equivalents: `async/await`, actors, `AsyncSequence` (topic 16)

---

# Stage 2: Building the App

## 4. App Components & Lifecycle

- 🟢 Activity, and the single-activity approach
- 🟢 The activity and fragment lifecycle callbacks, and what to do in each
- 🟢 Configuration changes: rotation, language, dark mode, and recreation
- 🟢 Process death and state restoration (`SavedStateHandle`, `rememberSaveable`)
- 🟢 `ViewModel`: what it holds, and what it does not survive
- 🟢 Intents: explicit vs implicit, passing data, and results
- 🟢 Navigation and the back stack
- 🟢 Deep links and app links
- 🟡 Services, and foreground services
- 🟡 Broadcast receivers and content providers
- 🟡 Launch modes and task behaviour
- 🟡 Application class, initialization, and startup libraries
- 🟡 The manifest: components, permissions, and exported flags
- 🟡 iOS equivalents: `UIViewController` lifecycle, scene lifecycle (topic 16)

## 5. UI with Jetpack Compose

- 🟢 Composables: UI as a function of state
- 🟢 State and recomposition: what triggers it, and how to keep it cheap
- 🟢 `remember`, `rememberSaveable`, and state hoisting
- 🟢 Layouts and modifiers: `Row`, `Column`, `Box`, modifier order
- 🟢 Lists: `LazyColumn`, keys, and item state
- 🟢 Side effects: `LaunchedEffect`, `DisposableEffect`, `rememberCoroutineScope`
- 🟢 Connecting a `ViewModel` to the UI with a single UI state
- 🟢 Navigation in Compose
- 🟡 Material theming and design tokens
- 🟡 Stability, `derivedStateOf`, and avoiding needless recomposition
- 🟡 Animations, gestures, and custom drawing
- 🟡 Previews, and UI that is easy to test
- 🟡 The View system basics (XML, `RecyclerView`) and interop with Compose
- 🟡 iOS equivalent: SwiftUI (topic 16)

## 6. App Architecture

- 🟢 Layers: UI, domain (optional), data (`ARCH 19`)
- 🟢 MVVM and MVI: one UI state, events flow up, state flows down
- 🟢 Unidirectional data flow
- 🟢 Repository pattern and a single source of truth
- 🟢 Modelling UI state with sealed types: loading, content, error, empty
- 🟢 One-time events (navigation, messages) without losing or repeating them
- 🟢 Error handling: one clear model from network to screen
- 🟢 Use cases (interactors): when they help, and when they are extra layers
- 🟡 Clean architecture and dependency direction
- 🟡 Mapping between layers: DTO, entity, domain model, UI model
- 🟡 Navigation architecture and feature wiring
- 🟡 Architecture decisions and how to explain them (`ARCH 3`)
- 🟡 Anti-patterns: logic in composables, God `ViewModel`, leaking Android types into domain

## 7. Dependency Injection & Modularization

- 🟢 What DI solves: testable, replaceable dependencies
- 🟢 Hilt (built on Dagger), Koin, and manual DI: how they differ
- 🟢 Scopes: application, activity, `ViewModel`
- 🟢 Constructor injection as the default
- 🟢 Module structure: `app`, feature modules, core and shared modules
- 🟢 Module boundaries: public API vs internal, and dependency direction
- 🟡 API and implementation module split
- 🟡 Build speed: parallel builds, caching, avoiding cycles
- 🟡 Version catalogs and convention plugins
- 🟡 Dynamic feature modules and app size
- 🟡 When modularization is not worth it yet (`ARCH 8`)

---

# Stage 3: Data & Background

## 8. Networking

- 🟢 HTTP client basics from the app's side (`BE 2`)
- 🟢 OkHttp and Retrofit, or Ktor
- 🟢 JSON serialization: kotlinx.serialization or Moshi, and handling unknown fields
- 🟢 Interceptors: auth headers, logging, retries
- 🟢 Auth tokens: attach, refresh on `401`, and avoid refresh storms
- 🟢 Timeouts, retries with backoff, and idempotency for writes (`SD 22`)
- 🟢 Error modelling: network, HTTP, parsing, and business errors
- 🟢 Pagination: cursor-based, and the Paging library
- 🟢 HTTP caching and conditional requests (`ETag`)
- 🟡 Image loading and caching (Coil, Glide)
- 🟡 Uploads and downloads: progress, resume, large files
- 🟡 WebSockets and server-sent events (`SD 24`)
- 🟡 Connectivity checks, and metered vs unmetered networks
- 🟡 GraphQL and gRPC clients
- 🟡 Compression, payload size, and API design that suits mobile (`BE 3`)
- 🟡 iOS equivalent: `URLSession` (topic 16)

## 9. Local Storage & Offline-First

- 🟢 Choose the storage: preferences/DataStore, Room (SQLite), files, and cache (`DB 21`)
- 🟢 Room: entities, DAOs, queries, and observing results as `Flow`
- 🟢 Room migrations, and why every old version must upgrade
- 🟢 Offline-first: the local database is the source of truth (`SD 30`)
- 🟢 Cache strategies: cache-first, network-first, stale-while-revalidate
- 🟢 Sync: send local changes, fetch remote changes, and handle failures
- 🟢 Conflict resolution: last-write-wins and merge rules
- 🟢 Never do database or file work on the main thread
- 🟡 DataStore vs `SharedPreferences`
- 🟡 Indexes and query performance on the device
- 🟡 Encrypted storage (`ARCH 11`, topic 13)
- 🟡 Storing large data: files vs blobs, and clearing caches
- 🟡 Deletes and tombstones in sync
- 🟡 Testing Room and migrations
- 🟡 iOS equivalents: Core Data, SwiftData (topic 16)

## 10. Background Work & Notifications

- 🟢 Why background work is restricted: battery and the OS
- 🟢 WorkManager: deferrable, guaranteed work, constraints, and retries
- 🟢 Choosing the right tool: coroutine, WorkManager, foreground service, alarm
- 🟢 Push notifications with FCM: token, token refresh, message types (`SD 24`)
- 🟢 Notification channels, and the notification permission on recent Android
- 🟢 Handling a push: data vs notification messages, and opening the right screen
- 🟡 Doze mode, App Standby, and battery optimization
- 🟡 Foreground services: types and user-visible notification
- 🟡 Exact alarms and when they are allowed
- 🟡 Periodic sync and its cost
- 🟡 Push reliability: it is best effort (`SD 30`)
- 🟡 iOS equivalents: background tasks, APNs (topic 16)

---

# Stage 4: Quality

## 11. Performance & Memory

- 🟢 Startup: cold, warm, and hot start, and what slows a cold start
- 🟢 Frame rendering: the frame budget (about 16 ms at 60 Hz), and what causes jank
- 🟢 ANR: what blocks the main thread, and how to prevent it
- 🟢 Memory leaks: common causes (context, listeners, static references)
- 🟢 Profiling first: Android Studio Profiler, then fix the measured problem
- 🟢 Lists and images: reuse, sizing, and downsampling
- 🟡 LeakCanary
- 🟡 Baseline Profiles and Macrobenchmark
- 🟡 R8 shrinking, app size, and App Bundle
- 🟡 Battery and network efficiency: batching, avoiding polling
- 🟡 Compose performance: recomposition counts, stability, lazy layouts
- 🟡 Perfetto and system traces
- 🟡 StrictMode to catch main-thread work
- 🟡 Low-end devices: test on them

## 12. Testing

- 🟢 Test pyramid: many fast unit tests, fewer integration tests, few UI tests
- 🟢 Local unit tests for `ViewModel`s, use cases, and mappers
- 🟢 Fakes vs mocks, and preferring fakes
- 🟢 Testing coroutines and flows (`runTest`, test dispatchers, Turbine)
- 🟢 Write code that is testable: injected dependencies, no hidden globals
- 🟢 Compose UI tests and Espresso
- 🟢 Testing repositories with a fake network and an in-memory Room
- 🟡 Robolectric and instrumented tests: when to use each
- 🟡 Screenshot tests
- 🟡 Testing migrations and offline behaviour
- 🟡 CI: run tests on every change, and keep them fast and reliable
- 🟡 Flaky tests: causes and fixes
- 🟡 iOS equivalents: XCTest (topic 16)

## 13. Security

- 🟢 Never ship secrets (API keys, passwords) in the app
- 🟢 Secure token storage: Android Keystore, and encrypted storage (check current recommended APIs)
- 🟢 TLS everywhere, cleartext blocked by default
- 🟢 Validate everything from outside: deep links, intents, WebView content, backend data
- 🟢 Minimal permissions and minimal data collection
- 🟢 Logs and screenshots: no sensitive data in logs, `FLAG_SECURE` where needed
- 🟡 Certificate pinning, and its operational risk (`SD 30`)
- 🟡 Code obfuscation with R8, and its limits
- 🟡 App integrity: Play Integrity API (iOS: App Attest)
- 🟡 Biometric authentication
- 🟡 Backup rules: what gets backed up
- 🟡 WebView risks and safe settings
- 🟡 Root and jailbreak detection: what it can and cannot do
- 🟡 OWASP MASVS and MASTG as checklists
- 🟡 iOS equivalents: Keychain, App Transport Security (topic 16)

## 14. Accessibility, Localization & Adaptive UI

- 🟢 Accessibility basics: content descriptions, touch target size, contrast, focus order
- 🟢 Screen readers (TalkBack) and testing with them
- 🟢 Font scaling and display size: layouts that do not break
- 🟢 Strings in resources, plurals, and never concatenating text
- 🟢 Dark theme
- 🟡 Right-to-left languages, and locale-aware dates, numbers, and currency
- 🟡 Adaptive layouts: tablets, foldables, window size classes
- 🟡 Edge-to-edge display and insets
- 🟡 Design systems: tokens, components, and Material
- 🟡 Accessibility in Compose (semantics)
- 🟡 Reduced motion and other user settings

---

# Stage 5: Shipping

## 15. Build, Release & Monitoring

- 🟢 Gradle basics: modules, dependencies, build types, and product flavors
- 🟢 Signing and keeping keys safe
- 🟢 Versioning: version code and version name
- 🟢 Release tracks and staged rollout on Google Play (iOS: TestFlight and phased release)
- 🟢 Feature flags and remote config: turn things off without a release (`SD 28`)
- 🟢 Backward compatibility: old app versions with new backends (`SD 30`)
- 🟢 Crash reporting and non-fatal errors (Crashlytics or similar)
- 🟢 App health metrics: crash-free users, ANR rate, cold start time
- 🟡 CI/CD: build, test, sign, and upload (GitHub Actions, Fastlane)
- 🟡 Force update and in-app updates
- 🟡 Analytics: event design, privacy, consent
- 🟡 A/B testing
- 🟡 Logging and correlation IDs from app to backend (`SD 27`)
- 🟡 Store policies, target API level requirements, and review rules
- 🟡 Build performance and reproducible builds

---

# Stage 6: Beyond Android

## 16. iOS & Swift Essentials (New)

- 🟢 Map the concepts: Activity or Fragment vs view controller, Compose vs SwiftUI, Room vs Core Data or SwiftData, Coroutines vs Swift concurrency
- 🟢 Swift basics: optionals, structs vs classes, enums with associated values, protocols
- 🟢 ARC memory management, and retain cycles (`weak`, `unowned`)
- 🟢 Swift concurrency: `async`/`await`, actors, `MainActor`
- 🟢 UIKit vs SwiftUI: what each is used for
- 🟢 Keychain for secrets
- 🟡 SwiftUI state: `@State`, `@Binding`, `@Observable`, `@StateObject`
- 🟡 Combine and `AsyncSequence`
- 🟡 `URLSession` and networking
- 🟡 Core Data and SwiftData
- 🟡 App lifecycle and scenes, background tasks, APNs
- 🟡 Testing with XCTest and Swift Testing
- 🟡 Distribution: Xcode, signing, TestFlight, App Store review
- 🟡 Swift Package Manager

## 17. Cross-Platform & Kotlin Multiplatform (New)

- 🟢 Options: native, Kotlin Multiplatform (KMP), Flutter, React Native
- 🟢 What KMP shares: business logic, data, and networking (UI stays native, or Compose Multiplatform)
- 🟢 How to choose: team skills, performance needs, platform features, speed, and long-term cost
- 🟡 `expect`/`actual` for platform-specific code
- 🟡 Compose Multiplatform (check its current maturity per platform)
- 🟡 Libraries that work in shared code (Ktor, kotlinx.serialization, SQLDelight)
- 🟡 Testing and CI for shared code
- 🟡 Migrating step by step: share one module first
- 🟡 Common problems: platform gaps, debugging, and tooling

---

# Stage 7: Mobile in the System

## 18. Mobile System Design

- 🟢 The steps: requirements, APIs, local data, architecture, caching, sync, failures, performance (`SD 31`)
- 🟢 Client-side concerns: flaky networks, offline, old app versions, battery (`SD 30`)
- 🟢 Data flow: UI, `ViewModel`, repository, local database, network
- 🟢 Pagination and infinite scroll
- 🟢 Image loading and caching
- 🟢 Real-time updates: polling, WebSocket, push
- 🟢 Uploads: chunking, resume, retry, and background upload
- 🟢 Sync design: what to sync, when, conflicts, deletes
- 🟡 Analytics and logging pipeline from the client
- 🟡 Feature flags and config delivery
- 🟡 Location-based features and their battery cost
- 🟡 Video playback and adaptive streaming (`SD 30`)
- 🟡 Client-side rate limiting and back-off

**Designs to practise**

- 🟢 News feed
- 🟢 Chat app
- 🟢 Offline-first notes app
- 🟢 Photo or file upload
- 🟡 Search with autocomplete
- 🟡 Ride tracking with live location
- 🟡 Video player
- 🟡 Payments and checkout flow
- 🟡 Image gallery with caching

## 19. Device Capabilities & Permissions

- 🟢 Runtime permission flow: ask in context, explain why, and handle denial and "don't ask again"
- 🟢 Location: precision, foreground vs background, and battery cost
- 🟢 Camera and media: capture, picker APIs, and large images
- 🟢 Connectivity and network changes
- 🟡 Biometrics and device credentials
- 🟡 Files and scoped storage
- 🟡 Contacts, calendar, and other sensitive data
- 🟡 Bluetooth, NFC, and sensors (names and purpose)
- 🟡 Privacy dashboards, permission auto-reset, and one-time permissions
- 🟡 Data-safety and privacy declarations in the stores

## 20. AI in Mobile Apps (New)

- 🟢 The app calls your backend, and your backend calls the model. No provider key in the app (`AI 5`, `AI 20`)
- 🟢 Streaming responses into the UI, with cancel and retry
- 🟢 States for AI features: loading, streaming, error, offline, limit reached
- 🟢 On-device vs cloud AI (`AI 19`)
- 🟡 On-device options by name: ML Kit, Gemini Nano, LiteRT, Core ML
- 🟡 Model download, updates, and storage
- 🟡 Voice and camera input
- 🟡 Privacy and data sent to third-party models

---

# Stage 8: Interview & Practice

## 21. Mobile Interview Answer Points (New)

- 🟢 Explain the lifecycle, configuration changes, and process death, and how state survives
- 🟢 Explain coroutines, cancellation, and `Flow` vs `StateFlow` in simple words
- 🟢 Explain recomposition, state hoisting, and how you avoid needless recomposition
- 🟢 Explain your architecture and why: layers, UI state, repository, source of truth
- 🟢 Ready answers: ANR, memory leaks, jank, cold start, and how you find each
- 🟢 Ready answers: offline-first, sync conflicts, old app versions, and token refresh
- 🟢 Ready answers: how you test, how you secure tokens, how you release safely
- 🟡 Coding warm-ups in Kotlin: debounce, retry with backoff, LRU cache, thread-safe counter
- 🟡 Tell decision stories: a hard bug, a performance win, a migration (`07-behavioral-leadership`)
- 🟡 Questions to ask about the team's app: architecture, release cadence, quality metrics
- 🟡 Common traps: logic in the UI, ignoring process death, only the happy path

## 22. Practice: Projects & Exercises

**Build (in order)**

- 🟢 Notes app: Compose, MVVM, Room, Retrofit, Hilt, with the Notes API (`BE 12`)
- 🟢 Make it offline-first: local database as the source of truth, WorkManager sync, conflict rule
- 🟢 Add tests: `ViewModel`, repository, and one UI test
- 🟢 Feed with paging and image loading
- 🟡 Chat screen with WebSocket, reconnect, and missed-message recovery (`SD 24`)
- 🟡 Photo upload with background work, retry, and progress
- 🟡 Split the app into feature modules and measure the build time
- 🟡 Performance pass: measure startup and jank, add a Baseline Profile, fix one leak
- 🟡 Security pass: storage, permissions, network config, and a checklist review
- 🟡 Release pass: flavors, signing, an internal track, staged rollout, crash reporting
- 🟡 A small AI feature: streaming chat through your backend (`AI 22`)
- 🟡 Rebuild one screen in SwiftUI, or share one module with KMP

**Exercises**

- 🟢 Explain the lifecycle order for start, rotate, background, and kill, out loud
- 🟢 Debug a memory leak with the Profiler or LeakCanary
- 🟢 Find and fix a slow list with Compose or `RecyclerView`
- 🟡 Turn callback code into `Flow` with `callbackFlow`
- 🟡 Write a Room migration and test it
- 🟡 Draw the architecture of your current app: layers, dependencies, and problems (`ARCH 14`)

---

# Glossary: Terms to Learn First

Plain meanings, with a priority. The last column is the topic that explains the term.

**Platform and lifecycle**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | App sandbox | Each app runs in its own process with private storage | 1 |
| 🟢 | Runtime permission | A permission the user grants while using the app | 1, 19 |
| 🟢 | Main (UI) thread | The thread that draws the UI. It must never be blocked | 1, 3 |
| 🟢 | APK / AAB | The installable Android package / the bundle Google Play turns into device-specific APKs | 1, 15 |
| 🟢 | Activity | An Android screen or entry point | 4 |
| 🟢 | Lifecycle | The callbacks as a component is created, shown, hidden, and destroyed | 4 |
| 🟢 | Configuration change | Rotation, language, or theme change that recreates the screen | 4 |
| 🟢 | Process death | The OS kills the app in the background, so state must be restorable | 4 |
| 🟢 | `ViewModel` | Holds UI state and survives configuration changes, but not process death | 4, 6 |
| 🟢 | Intent | A message that starts a component or passes data | 4 |
| 🟢 | Deep link | A URL that opens a specific screen in the app | 4 |
| 🟡 | Fragment | A reusable part of a screen hosted by an activity | 4 |
| 🟡 | Service / foreground service | Background component / long task with a visible notification | 4, 10 |
| 🟡 | Manifest | The file that declares components, permissions, and app information | 4 |
| 🟡 | Min SDK / target SDK | Oldest supported OS version / the version the app is built and tested for | 1 |

**Kotlin and concurrency**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Null safety | The type system separates values that can be null from those that cannot | 2 |
| 🟢 | Data class / sealed class | A class for holding data / a closed set of subtypes, great for states | 2 |
| 🟢 | Extension function | Add a function to an existing type without changing it | 2 |
| 🟢 | Coroutine | A lightweight unit of work that can pause and resume | 3 |
| 🟢 | `suspend` function | A function that can pause without blocking a thread | 3 |
| 🟢 | Dispatcher | Decides which threads a coroutine runs on | 3 |
| 🟢 | Structured concurrency | Coroutines belong to a scope, and cancelling the scope cancels its children | 3 |
| 🟢 | Cancellation | Stopping a coroutine. It is cooperative, so code must check | 3 |
| 🟢 | Flow | An asynchronous stream of values, started when collected | 3 |
| 🟢 | `StateFlow` / `SharedFlow` | A hot flow holding the latest state / a hot flow that broadcasts events | 3 |
| 🟡 | Scope function | `let`, `apply`, `also`, `run`, `with`: run code with an object as context | 2 |
| 🟡 | Back-pressure | What to do when values arrive faster than they are consumed | 3 |
| 🟡 | Mutex | A lock that lets one coroutine at a time enter a section | 3 |

**UI and architecture**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Composable | A function that describes part of the UI in Compose | 5 |
| 🟢 | Recomposition | Compose re-running the composables whose state changed | 5 |
| 🟢 | State hoisting | Moving state up so a composable becomes stateless and reusable | 5 |
| 🟢 | Side effect | Work that is not drawing UI, such as `LaunchedEffect` | 5 |
| 🟢 | `LazyColumn` / `RecyclerView` | Lists that create only the visible items | 5 |
| 🟢 | MVVM / MVI | Patterns that separate the screen from its state and logic | 6 |
| 🟢 | Unidirectional data flow | State flows down and events flow up, in one direction | 6 |
| 🟢 | UI state | One object that describes everything a screen shows | 6 |
| 🟢 | Repository | The layer that hides where data comes from (network, database, cache) | 6 |
| 🟢 | Single source of truth | One place owns each piece of data, usually the local database | 6, 9 |
| 🟢 | Dependency injection | Give a class its dependencies instead of letting it create them | 7 |
| 🟡 | Use case (interactor) | A class for one piece of business logic | 6 |
| 🟡 | Hilt / Koin | A compile-time DI framework built on Dagger / a lightweight Kotlin DI library | 7 |
| 🟡 | Modularization | Splitting the app into modules with clear boundaries | 7 |
| 🟡 | Convention plugin | Shared Gradle build settings applied to many modules | 7 |

**Data, network, and background**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Interceptor | Code that sees every request and response, for auth, logging, or retries | 8 |
| 🟢 | Token refresh | Getting a new access token when the old one expires | 8 |
| 🟢 | Pagination | Loading a long list in pages | 8 |
| 🟢 | Room | The Android library on top of SQLite | 9 |
| 🟢 | Offline-first | The local database is the source of truth, and it syncs with the server | 9 |
| 🟢 | Migration | A step that upgrades the local schema when the app updates | 9 |
| 🟢 | Conflict resolution | Deciding what wins when local and server changes clash | 9 |
| 🟢 | WorkManager | Android's API for deferrable work that must run even if the app closes | 10 |
| 🟢 | FCM / APNs | The push notification services for Android / iOS | 10 |
| 🟡 | DataStore | A modern key-value and typed storage library | 9 |
| 🟡 | HTTP cache / `ETag` | Reuse responses / ask the server "has this changed?" | 8 |
| 🟡 | Doze / App Standby | Battery modes that limit background work | 10 |
| 🟡 | Notification channel | A user-controllable category of notifications | 10 |

**Quality**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Cold / warm / hot start | Starting with no process / with the process but no activity / with both alive | 11 |
| 🟢 | Jank | Dropped frames that make the UI stutter | 11 |
| 🟢 | ANR | "Application Not Responding": the main thread was blocked too long | 11 |
| 🟢 | Memory leak | Objects kept in memory after they are no longer needed | 11 |
| 🟢 | Test pyramid | Many unit tests, fewer integration tests, few UI tests | 12 |
| 🟢 | Fake vs mock | A simple working replacement / an object that records and checks calls | 12 |
| 🟢 | Android Keystore / Keychain | System storage for cryptographic keys on Android / iOS | 13 |
| 🟢 | Content description | Text a screen reader reads for an image or icon | 14 |
| 🟡 | Baseline Profile | A file that tells the system which code to precompile, to speed up start | 11 |
| 🟡 | Macrobenchmark | A tool to measure startup and scrolling on a real build | 11 |
| 🟡 | R8 | The tool that shrinks, optimizes, and obfuscates release code | 11, 13 |
| 🟡 | Certificate pinning | The app trusts only your server's certificate | 13 |
| 🟡 | Play Integrity API / App Attest | Checks that the app and device are genuine, on Android / iOS | 13 |
| 🟡 | OWASP MASVS | A security checklist standard for mobile apps | 13 |
| 🟡 | Window size class | A way to adapt layouts to small, medium, and large screens | 14 |

**Shipping and beyond**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Build type / product flavor | Debug and release settings / variants such as free and paid | 15 |
| 🟢 | Signing key | The key that proves an update comes from you. Losing it is serious | 15 |
| 🟢 | Staged rollout | Releasing to a growing percentage of users | 15 |
| 🟢 | Feature flag / remote config | Server-controlled switches for features and settings | 15 |
| 🟢 | Crash-free rate | The share of users or sessions with no crash | 15 |
| 🟢 | Backward compatibility | New backends keep working with old app versions | 15, 18 |
| 🟡 | CI/CD | Automatic build, test, and delivery | 15 |
| 🟡 | Force update | Blocking old versions until the user updates | 15 |
| 🟡 | SwiftUI / UIKit | Apple's modern declarative UI framework / the older imperative one | 16 |
| 🟡 | ARC | Automatic reference counting: how Swift manages memory | 16 |
| 🟡 | Kotlin Multiplatform (KMP) | Share Kotlin code between Android, iOS, and other targets | 17 |
| 🟡 | `expect` / `actual` | Declare a platform-specific piece in shared code, then implement it per platform | 17 |
| 🟡 | Compose Multiplatform | Share Compose UI across platforms | 17 |

---

## Skip for Now

- Android OS internals (Binder, ART, custom ROMs) beyond a basic picture
- NDK and C++ development, game engines, and AR/VR
- Wear OS, TV, and Auto specifics
- Writing Gradle plugins from scratch
- Deep XML View customization (know the basics and the Compose interop)
- Every cross-platform framework. Know the options and how to choose

## How to Proceed

1. Do topics 1 to 3 first. Kotlin and coroutines show up in every interview.
2. Do topics 4 to 7 as one set, while building the notes app (exercise 22). Look at the app's states, lifecycle, and layers as you go.
3. Do topics 8 to 10 next, and make the app offline-first with sync. This is the part that separates strong mobile engineers.
4. Do topics 11 to 13 by auditing your own app: profile it, test it, and review its security.
5. Do topic 15 by shipping the app to an internal track, with crash reporting.
6. Read topics 16 and 17 to map what you know to iOS and cross-platform. Deepen them only if your target roles need it.
7. Do topics 18 to 22 last. Practise mobile system designs out loud, and use `SD 30` and `SD 31` alongside.
8. For each topic: what it is, what problem it solves, how it works, one downside.
