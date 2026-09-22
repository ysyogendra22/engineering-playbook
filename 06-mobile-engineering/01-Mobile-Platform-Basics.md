# Mobile Platform Basics

Roadmap topic 1 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** a phone is not a small server. The OS owns the process, can kill it at any time, and expects you to ask before touching anything sensitive. Almost every mobile-specific bug traces back to forgetting one of the facts in this topic.

---

#### 1. The App Sandbox — 🟢 Must Know

*Each app is boxed in, for everyone's safety, including yours.*

1. Each app runs in its **own process**, with its **own private storage** — one app cannot read another app's files or memory directly.
2. This is why apps talk to each other through defined channels: intents, content providers, deep links — never by reaching into another app's storage.
3. **Mobile view:** the same idea as a server's process isolation, but enforced per-app, per-device, by the OS itself.

---

#### 2. Runtime Permissions — 🟢 Must Know

*Ask when you need it, not at install time, and always handle "no".*

1. Modern Android (and iOS) ask for sensitive permissions **at the moment they're needed** (camera, location, notifications), not all upfront at install.
2. The user can say **no**, and the app must still work in some reasonable way — don't crash, and don't block the whole app on one declined permission.
3. Full permission flow (asking with context, handling "don't ask again") is covered in topic `19`.

---

#### 3. The Main (UI) Thread Rule — 🟢 Must Know

*Never block it. Everything the user sees depends on it staying free.*

1. All UI drawing happens on **one thread** — the main thread.
2. Any slow work done there (network calls, database queries, heavy computation) freezes the UI and can trigger an **ANR** ("Application Not Responding", topic `11`).
3. This single rule is why coroutines and background work (topics `3`, `10`) exist at all — they exist to keep the main thread free.

---

#### 4. The OS Can Kill Your App Anytime — 🟢 Must Know

*Unlike a server, your process is not guaranteed to keep running.*

1. When the app goes to the background, the OS may kill its process at any time to free memory for whatever's in the foreground.
2. When the user returns, Android **recreates** the app from scratch — any state not explicitly saved is gone.
3. This is **process death**, and it's different from a configuration change (topic `4`) — design for both.

```text
App backgrounded → OS needs memory → process killed → user returns →
new process created → without saved state, the app looks "reset"
```

---

#### 5. App Package and Distribution — 🟢 Must Know

*How the app actually gets onto a phone.*

1. **APK** — the installable Android package. **AAB (App Bundle)** — the format you upload to Google Play, which then builds device-specific APKs for each user (smaller downloads).
2. **iOS**: **IPA** is the installable package, distributed through the App Store (or TestFlight for testing).
3. Distribution isn't just packaging — it also means going through store review, policies, and listing requirements (section `8`).

---

#### 6. OS Versions and Device Variety — 🟢 Must Know

*Your app runs on years-old phones and this year's phone, at the same time.*

1. **Min SDK** — the oldest Android version the app supports. **Target SDK** — the version the app is built and tested against, and whose new behaviours it opts into.
2. Screen sizes and densities vary enormously — layouts must adapt (topic `14`).
3. A feature available on the newest OS version may not exist on a phone running an older one — check availability, don't assume.

---

#### 7. Old App Versions Stay in Use for Years — 🟢 Must Know

*Some users never update. Design like it's permanent, because it is.*

1. Unlike a web app, you cannot force every user onto the latest version overnight.
2. The backend must stay **backward compatible** with old app versions for a long time (`SD 30`).
3. This single fact shapes API versioning, feature flags, and release strategy (topic `15`) across the whole mobile stack.

---

#### 8. Android vs iOS: Main Differences — 🟡 Good to Know

1. **App model:** Android has multiple entry-point components (activities, services, broadcast receivers); iOS centres around a scene/view-controller model.
2. **Background rules:** both restrict background work heavily, but the exact mechanisms differ (topic `10` for Android; topic `16` covers the iOS side).
3. **Distribution:** Google Play review is generally faster and looser than Apple's App Store review.

---

#### 9. How an App Starts — 🟡 Good to Know

1. The OS creates the **process**, runs the **Application class** (any global setup happens here), then launches the **first screen**.
2. Heavy work in the Application class or in a startup library directly slows down cold start (topic `11`) — keep it minimal.

---

#### 10. App Stores — 🟡 Good to Know

1. Both stores review apps before publishing — expect checks on permissions, privacy declarations, content, and stability.
2. A store listing (screenshots, description, privacy labels) is part of the product, not just marketing — plan for it.

---

#### 11. Tools — 🟡 Good to Know

1. **Android Studio** — the main IDE. **Gradle** — the build system. **ADB** — the command-line bridge to a device or emulator, used for installing, logging, and debugging.
2. **Emulator vs real device** — the emulator is convenient, but always test performance, battery, and camera/sensor features on a real device before shipping.

---

#### 12. Common Interview Questions

1. **What happens when the OS kills your app in the background?**
   The process is destroyed. On return, Android creates a new process and recreates the UI — any state not explicitly saved (`SavedStateHandle`, a database) is lost. This is process death, distinct from a configuration change.
2. **Why can't an app read another app's files directly?**
   Each app runs in its own sandboxed process with private storage. Apps interact only through defined channels — intents, content providers, deep links.
3. **What is min SDK vs target SDK?**
   Min SDK is the oldest OS version supported. Target SDK is the version the app is built and tested against, opting into that version's behaviour changes.
4. **Why do old app versions matter so much on mobile?**
   Users don't all update. Some stay on old versions for years, so the backend and the release process must support them (`SD 30`).
5. **What's the difference between an APK and an AAB?**
   APK is the installable package. AAB is the format uploaded to Google Play, which then generates optimised, device-specific APKs.

---

#### 13. Common Mistakes

1. Assuming the app's process stays alive indefinitely in the background.
2. Doing slow work on the main thread "just this once".
3. Designing only for the newest OS version and newest devices.
4. Treating permission denial as an edge case instead of a normal, expected path.
5. Assuming all users are on the latest app version.

---

#### 14. Related Topics

1. `3` Coroutines & Flow — how work is kept off the main thread
2. `4` App Components & Lifecycle — process death and configuration changes in detail
3. `19` Device Capabilities & Permissions — the full runtime permission flow
4. `SD 30` Mobile-Specific Topics — backward compatibility from the backend's side

---

#### 15. Interview Must Remember

1. **Each app is sandboxed** — its own process, its own storage.
2. **Never block the main thread.**
3. **The OS can kill your process at any time** in the background — design for process death, not just configuration changes.
4. **Old app versions live for years** — this shapes backend and release decisions across the whole stack.
