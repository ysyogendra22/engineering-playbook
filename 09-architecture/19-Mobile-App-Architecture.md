# Mobile App Architecture

Roadmap topic 19 · Stage 6: Your Domain · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** everything in Stages 1–5 of this roadmap applies to a mobile app too — it's just architecture with a specific, constrained deployment target: a device you don't control, that can't be instantly updated. This topic is where the general theory meets that reality. Full implementation-level detail lives in `06-mobile-engineering`.

---

#### 1. Layers — 🟢 Must Know

```text
UI (Compose)  →  ViewModel  →  [ optional: domain ]  →  data (repository)
```

The same layered/clean architecture shape from topics `4` and `5`, applied to a mobile app — full concrete detail in `06-mobile-engineering/6`.

---

#### 2. Patterns: MVVM, MVI, Clean Architecture on Mobile — 🟢 Must Know

The UI patterns from `6`, item 5, applied specifically to mobile: MVVM and MVI both separate a screen's presentation from its state and logic; clean architecture (`5`, item 5) keeps business rules independent of the Android/iOS framework itself, testable without it.

---

#### 3. Unidirectional Data Flow and Single Source of Truth — 🟢 Must Know

State flows down to the UI, events flow up — the same principle as `06-mobile-engineering/6`. The **single source of truth** for app state is usually the local database (item 6), not the network response directly.

---

#### 4. Dependency Injection — 🟢 Must Know

Hilt, Koin, or manual DI (`06-mobile-engineering/7`) — the same Dependency Inversion principle from `4`, applied concretely at the mobile app level.

---

#### 5. Modularization — 🟢 Must Know

By feature, with clear module APIs (`8`, `06-mobile-engineering/7`) — the same module-boundary discipline as any other system, with mobile-specific benefits: build time, and enabling multiple teams to work on one app independently.

---

#### 6. Offline-First — 🟢 Must Know

*The single most distinctive mobile-architecture pattern, worth being able to explain clearly.*

The local database is the source of truth; the network's job is to **sync** it, not feed the UI directly (`06-mobile-engineering/9`). This is what lets a mobile app keep working through the flaky, intermittent connectivity that's a normal, expected condition on a phone — not an edge case.

---

#### 7. Backward Compatibility with Old App Versions — 🟢 Must Know

*The constraint that shapes almost every other mobile architecture decision.*

Unlike a backend service you can redeploy instantly, an app version, once installed, can stay in active use for **years** (`SD 30`, `06-mobile-engineering/1`). Every API and data-format decision (`10`) must account for clients that will never update, sometimes indefinitely.

---

#### 8. Networking Layer — 🟡 Good to Know

Caching, error handling, and interceptors (`06-mobile-engineering/8`) — the client-side half of the integration architecture from topic `10`.

---

#### 9. Navigation and Feature Wiring — 🟡 Good to Know

How features, built as independent modules (item 5), are actually connected and navigated between — a real architectural decision about coupling between modules, not just a UI implementation detail.

---

#### 10. Feature Flags, Remote Config, Staged Rollouts — 🟡 Good to Know

Since an app can't be instantly redeployed (item 7), **remote control over behaviour without a new release** becomes an architectural necessity, not a nice-to-have (`06-mobile-engineering/15`) — the mobile equivalent of a backend's ability to deploy a fix quickly.

---

#### 11. Security — 🟡 Good to Know

Token storage, certificate pinning, obfuscation — the mobile-specific instance of `11`'s security architecture, full detail in `06-mobile-engineering/13`.

---

#### 12. Testing Strategy — 🟡 Good to Know

The same test pyramid principle from `BE 7`, with mobile-specific tooling — full detail in `06-mobile-engineering/12`.

---

#### 13. Cross-Platform Options — 🟡 Good to Know

Kotlin Multiplatform and other options, with real trade-offs (`06-mobile-engineering/17`) — an architecture-level decision about how much platform-specific code to maintain versus share.

---

#### 14. Where the Deeper Detail Lives — 🟡 Good to Know

This topic is deliberately a **summary** — every implementation-level detail (Compose specifics, Room, coroutines, Gradle, and so on) lives in `06-mobile-engineering`. Use this topic to connect mobile decisions back to the general architecture principles from Stages 1–5; use that folder for the concrete how-to.

---

#### 15. Common Interview Questions

1. **What makes mobile app architecture different from backend architecture?**
   The deployment target is a device you don't control, that can't be instantly updated — this single fact drives offline-first design, backward compatibility with old app versions, and remote config/feature flags as architectural necessities, not nice-to-haves.
2. **Why is offline-first the default recommendation for most mobile apps?**
   It makes the local database the source of truth, so the app keeps working through the flaky, intermittent connectivity that's a normal condition on a phone, not an edge case — and the network's job becomes syncing that database, not feeding the UI directly.
3. **How do you handle a backend change that would break older app versions?**
   Treat old app versions as a long-lived, permanent constraint (they can be in active use for years) — prefer additive, backward-compatible API changes, and use remote feature flags to control new behaviour without requiring a release.
4. **How would you decide whether to modularize a mobile app?**
   The same module-boundary reasoning as topic `8`, plus mobile-specific payoffs: build time and letting multiple teams work independently on one app.

---

#### 16. Common Mistakes

1. Treating the network as the source of truth instead of the local database in an offline-first design.
2. Making a backend change that assumes every client is on the latest app version.
3. No remote way to control behaviour without shipping a new release.
4. Modularizing (or not modularizing) without a real, specific reason tied to build time or team structure.

---

#### 17. Related Topics

1. `06-mobile-engineering` (the whole folder) — full implementation-level detail behind every item here
2. `4`, `5`, `6` — the general design principles, styles, and patterns this topic applies to mobile
3. `SD 30` — backward compatibility and mobile-specific system design from the backend's perspective

---

#### 18. Interview Must Remember

1. **Same architecture principles as any system**, applied to a device you don't control.
2. **Offline-first**: local database as source of truth, network syncs it.
3. **Old app versions are a permanent constraint** — design for years of coexistence.
4. **Remote flags/config** substitute for the instant redeploy a backend has.
