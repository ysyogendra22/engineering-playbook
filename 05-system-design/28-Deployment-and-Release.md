# Deployment & Release

Roadmap topic 28 · Stage 6: Architecture & Production

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** getting new code to production safely. Automate build and tests, release to a few users first, and always be able to roll back. Old app versions must keep working.

---

#### 1. CI/CD — 🟢 Must Know

*Every change is built, tested, and deployed by a pipeline.*

1. **CI (continuous integration)** — on every change, automatically **build and test**. Bad code is caught early.
2. **CD (continuous delivery/deployment)** — automatically deliver passing builds to staging and production.
3. Use separate **environments**: development, staging (a production copy for testing), production.
4. Same idea as your app's CI pipeline (build, tests, release).

```text
Commit → Build → Tests → Deploy to staging → Checks → Deploy to production
```

---

#### 2. Safe Release Strategies — 🟢 Must Know

*Ways to ship new code with less risk.*

| Strategy | How | Good | Bad |
|---|---|---|---|
| **Rolling** | Replace servers a few at a time | No downtime, simple | Old and new versions run together for a while |
| **Blue-green** | Two full environments. Switch traffic from blue (old) to green (new) | Instant switch and rollback | Needs double resources |
| **Canary** | Send 1–5% of traffic to the new version first, then increase | Catches problems with small impact | More setup and monitoring |

1. Always have a **rollback plan** (redeploy the previous version quickly).
2. Watch error rate and latency right after a release.

**Mobile view:** app releases use the same ideas: staged rollout on Google Play, phased release on the App Store, and feature flags to switch a feature off without a new build.

---

#### 3. Backward Compatibility and Safe Migrations — 🟢 Must Know

*Old and new versions run together, so changes must work with both.*

1. **During a rollout, old and new server versions run together**, and **old app versions** still call your API. Never break the contract (topic `03`).
2. **Database changes: expand → migrate → contract.**

```text
1. EXPAND    add the new column (nullable); old code still works
2. MIGRATE   deploy code that writes both; backfill old rows
3. CONTRACT  once nothing uses the old column, remove it later
```

3. Never make a change that the **previous** code version can't work with, or you can't roll back.

---

#### 4. Docker Basics — 🟡 Good to Know

*Package the app so it runs the same everywhere.*

1. **Image** — a packaged app with everything it needs. **Container** — a running image.
2. Same package runs the same way everywhere (laptop, staging, production).
3. Know: ports (which port the app listens on), volumes (data outside the container), environment variables (config).
4. Kubernetes (a system to run many containers) is only a name at this level.

---

#### 5. Feature Flags, Force-Update — 🟡 Good to Know

*You know these from app releases.*

1. **Feature flag** — turn a feature on or off without deploying. Roll out to a % of users, or switch off quickly if it breaks.
2. **Staged rollout / A/B test** — release to a few users, compare results.
3. **Force-update** — make very old app versions update when the API can no longer support them.

---

#### 6. Graceful Shutdown — 🟡 Good to Know

*Finish current work before the server stops.*

1. When a server is stopped (during a deploy), finish the requests in progress instead of cutting them.
2. Stop accepting new requests, wait for current ones to finish (with a time limit), close connections, then exit.

---

#### 7. Common Interview Questions

1. **How do you deploy a breaking database change without downtime?**
   Expand, migrate, contract. Add the new column, deploy code that works with both, backfill, then remove the old column later.
2. **Rolling vs blue-green vs canary?**
   Rolling replaces gradually. Blue-green switches between two environments. Canary tests on a small share of traffic first.
3. **How do you roll back?**
   Redeploy the previous version (or switch back in blue-green). Keep database changes backward compatible so rollback works.
4. **How do old app versions affect a release?**
   The API must stay backward compatible. Use versioning and force-update as a last step.
5. **What is a feature flag?**
   A switch to turn a feature on or off, or roll it out gradually, without deploying.

---

#### 8. Common Mistakes

1. Manual, untested deployments.
2. Database changes that break the previous version.
3. No rollback plan.
4. Releasing to 100% at once.
5. Removing a field or endpoint that old apps still use.
6. Killing servers without a graceful shutdown.

---

#### 9. Related Topics

1. `03` API Design (backward compatibility, in `04-backend-engineering`)
2. `27` Observability (watch releases)
3. `29` Backup, Recovery, Security & Cost
4. `30` Mobile-Specific Topics (old app versions, force-update)

---

#### 10. Interview Must Remember

1. **CI** builds and tests. **CD** deploys.
2. **Canary / blue-green / rolling** plus a **rollback plan**.
3. **Expand → migrate → contract** for database changes.
4. **Backward compatible** for old servers and old apps.
5. **Feature flags** for safe rollouts.
