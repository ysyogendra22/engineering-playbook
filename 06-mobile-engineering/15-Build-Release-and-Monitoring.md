# Build, Release & Monitoring

Roadmap topic 15 · Stage 5: Shipping

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** shipping mobile software is different from shipping a backend — you can't force an instant rollback to every user. Staged rollouts, feature flags, and crash monitoring exist because a bad release lives on people's phones until they update, so the release process itself has to absorb the risk.

---

#### 1. Gradle Basics — 🟢 Must Know

1. **Modules** — separate build units (topic `7`).
2. **Build types** — `debug` vs `release`, with different settings (minification, signing, logging).
3. **Product flavors** — variants of the app (free vs paid, different backends per environment) that can combine with build types.

---

#### 2. Signing — 🟢 Must Know

Every release APK/AAB is cryptographically **signed**, proving updates genuinely come from you. **Losing the signing key is serious** — without it, you can't publish updates to an existing app listing at all; store it securely, with backups.

---

#### 3. Versioning — 🟢 Must Know

1. **Version code** — an internal integer, must increase with every release, used by the store to determine "is this newer?".
2. **Version name** — the human-readable string shown to users (`2.3.1`).

---

#### 4. Staged Rollout — 🟢 Must Know

1. Release to a **small percentage of users first** (Google Play release tracks; iOS TestFlight and phased release), watch crash rate and key metrics, then increase the percentage.
2. This is the mobile equivalent of a canary deployment (`SD 28`) — except a bad release can't be instantly pulled from devices that already downloaded it, so staging the rollout is the main safety net.

---

#### 5. Feature Flags and Remote Config — 🟢 Must Know

Server-controlled switches let you **turn a feature off without shipping a new release** — essential on mobile, where a code fix can't reach users instantly (`SD 28`). Ship risky features behind a flag, so a problem can be mitigated remotely.

---

#### 6. Backward Compatibility — 🟢 Must Know

Old app versions keep calling the backend for years (topic `1`, `SD 30`) — every backend change must keep working with app versions already in the wild, not just the one being released today.

---

#### 7. Crash Reporting — 🟢 Must Know

Tools like Crashlytics capture crashes (and **non-fatal errors** — caught exceptions worth knowing about, even if they didn't crash the app) from real users in production, with stack traces, device info, and breadcrumbs leading up to the failure.

---

#### 8. App Health Metrics — 🟢 Must Know

| Metric | What it tells you |
|---|---|
| Crash-free users/sessions | Overall stability |
| ANR rate | Main-thread blocking issues (topic `11`) in the wild |
| Cold start time | First-impression performance (topic `11`) |

Watch these **after every release**, not just during development.

---

#### 9. CI/CD — 🟡 Good to Know

Automating build, test, sign, and upload (GitHub Actions, Fastlane, or similar) — the same principles as `SD 28`, applied to mobile's extra steps (signing, store upload).

---

#### 10. Force Update and In-App Updates — 🟡 Good to Know

1. **Force update** — block old, unsupported app versions from continuing to work, when a backend change truly can't stay compatible with them.
2. **In-app update prompts** — nudge users toward updating without fully blocking them, a gentler middle ground.

---

#### 11. Analytics — 🟡 Good to Know

Event design, privacy, and consent (respecting what the user has agreed to share) all matter — analytics is genuinely useful, but it's also personal data collection, and should be treated with the same care as any other (`08-artificial-intelligence`'s privacy topics apply the same logic).

---

#### 12. A/B Testing — 🟡 Good to Know

Comparing two versions of a feature with real users, gated by remote config, to make a data-informed decision rather than a guess.

---

#### 13. Logging and Correlation IDs — 🟡 Good to Know

Attaching a request/correlation ID from the app through to backend logs (`SD 27`) makes it possible to trace one user's specific failing request across both sides of the system.

---

#### 14. Store Policies — 🟡 Good to Know

Both stores have review policies and minimum target API level requirements that change over time — an app that ignores them for too long can be removed from the store, not just flagged.

---

#### 15. Build Performance — 🟡 Good to Know

Reproducible, fast builds matter for both developer productivity and CI cost — module structure (topic `7`) is the biggest lever here.

---

#### 16. Common Interview Questions

1. **Why is a staged rollout especially important on mobile, compared to a backend deploy?**
   A backend rollback is near-instant; a bad mobile release stays on every device that already downloaded it until they update. Staging catches problems while exposure is still small.
2. **How do feature flags help with mobile release risk?**
   They let you disable a problematic feature remotely, without shipping a new release — critical since app updates can't reach users instantly.
3. **What would you monitor right after a release?**
   Crash-free rate, ANR rate, and cold start time, watched specifically for the new release compared to the previous one.
4. **Why must backend changes stay compatible with old app versions?**
   Users update slowly and unevenly; some app versions stay in active use for years, and the backend can't assume everyone is on the latest one.
5. **What's the risk of losing a signing key?**
   You can no longer publish updates to that existing app listing — it's effectively permanent, so secure storage and backup of the signing key matters enormously.

---

#### 17. Common Mistakes

1. Releasing to 100% of users immediately instead of staging the rollout.
2. Shipping a risky feature with no flag to disable it remotely if something goes wrong.
3. Breaking backward compatibility for app versions still in active use.
4. Not watching crash-free rate and ANR rate closely right after a release.
5. Treating the signing key casually, with no secure backup.

---

#### 18. Related Topics

1. `1` Mobile Platform Basics — why old app versions persist for years
2. `11` Performance & Memory — the metrics watched post-release
3. `SD 28` Deployment & Release — the shared release-safety principles from the backend side
4. `SD 30` Mobile-Specific Topics — backward compatibility from the system design angle

---

#### 19. Interview Must Remember

1. **Staged rollout** is mobile's substitute for an instant rollback.
2. **Feature flags/remote config** let you mitigate a bad feature without a new release.
3. **Backward compatibility** with old app versions is a permanent backend constraint.
4. **Watch crash-free rate, ANR rate, and cold start** after every release.
5. **Guard the signing key** — losing it is close to irreversible.
