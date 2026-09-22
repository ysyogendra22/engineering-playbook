# Background Work & Notifications

Roadmap topic 10 · Stage 3: Data & Background

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** background work on mobile is restricted on purpose — the OS is protecting battery life. Picking the right tool (a coroutine, WorkManager, a foreground service) for the actual urgency and duration of the work is the whole skill here.

---

#### 1. Why Background Work Is Restricted — 🟢 Must Know

Unlike a server, a phone runs on a battery the user cares about — the OS aggressively limits what background code can do, and for how long, to protect it. Fighting these restrictions (rather than working with them) is a common source of battery complaints and app kills.

---

#### 2. WorkManager — 🟢 Must Know

*The standard tool for deferrable, guaranteed background work.*

1. **Deferrable** — doesn't need to run this exact instant.
2. **Guaranteed** — WorkManager persists the request and runs it even if the app process dies or the device reboots, once constraints are met.
3. **Constraints** — run only when conditions are met (network available, charging, battery not low).
4. **Retries** — built-in retry with backoff on failure.

```kotlin
class SyncWorker(context: Context, params: WorkerParameters) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        return try {
            repository.sync()
            Result.success()
        } catch (e: Exception) {
            Result.retry()   // WorkManager retries with backoff
        }
    }
}

val syncRequest = OneTimeWorkRequestBuilder<SyncWorker>()
    .setConstraints(Constraints.Builder().setRequiredNetworkType(NetworkType.CONNECTED).build())
    .build()
WorkManager.getInstance(context).enqueue(syncRequest)
```

---

#### 3. Choosing the Right Tool — 🟢 Must Know

| Need | Tool |
|---|---|
| Work tied to a screen, cancelled when it's gone | A coroutine in `viewModelScope`/`lifecycleScope` (topic `3`) |
| Deferrable, must survive app closing/reboot | WorkManager |
| Must run now, user-visible, ongoing (music playback, an active upload) | Foreground service |
| Must fire at an exact wall-clock time | An exact alarm (rare, restricted — see item 9) |

---

#### 4. Push Notifications with FCM — 🟢 Must Know

1. **FCM (Firebase Cloud Messaging)** delivers push notifications to the device.
2. The app registers and receives a **device token**, which the backend uses to target that device — the token can change, and the app must handle **token refresh** by sending the new one to the backend.
3. Message types: a **notification message** the OS can display automatically even if the app isn't running, vs a **data message** the app itself must handle in code (`SD 24`).

---

#### 5. Notification Channels and Permission — 🟢 Must Know

1. **Notification channels** group notifications by category, and the user can control each channel's behaviour (sound, importance) independently.
2. On recent Android versions, showing a notification requires the **notification runtime permission** — request it in context, like any other permission (topic `19`).

---

#### 6. Handling a Push — 🟢 Must Know

1. **Data message** — the app's code decides what to show and do (useful when the app needs custom logic, like updating local data before showing a notification).
2. **Notification message** — the OS displays it directly when the app isn't in the foreground.
3. Tapping a notification should deep link (topic `4`) to the relevant screen, not always just open the app's home screen.

---

#### 7. Doze Mode, App Standby, Battery Optimization — 🟡 Good to Know

Android reduces background activity — network access, wakelocks, job execution — for apps that have been idle, to save battery. WorkManager and FCM's high-priority messages are designed to work correctly even under these restrictions; raw background threads or alarms often aren't.

---

#### 8. Foreground Services — 🟡 Good to Know

A foreground service shows a persistent, user-visible notification while it runs, in exchange for fewer background restrictions. Recent Android versions require declaring a **service type** (location, media playback, data sync) matching the actual work being done.

---

#### 9. Exact Alarms — 🟡 Good to Know

Scheduling work at a precise wall-clock time is heavily restricted on recent Android versions and often requires a specific, user-granted permission — reach for WorkManager's flexible scheduling instead unless exact timing is genuinely required.

---

#### 10. Periodic Sync and Its Cost — 🟡 Good to Know

A periodic `WorkRequest` (e.g. sync every few hours) has a real, ongoing battery and data cost — set the interval based on actual need, and prefer push-triggered sync over frequent polling where possible.

---

#### 11. Push Reliability: Best Effort — 🟡 Good to Know

Push delivery is **not guaranteed** — messages can be delayed or dropped, especially under battery restrictions or a poor connection (`SD 30`). Never design a feature that depends on a push always arriving; pair it with a periodic or on-open sync as a fallback.

---

#### 12. iOS Equivalents — 🟡 Good to Know

Background tasks (`BGTaskScheduler`) and APNs (Apple Push Notification service) play the same roles as WorkManager and FCM — see topic `16`.

---

#### 13. Common Interview Questions

1. **How would you sync data reliably even if the app is killed?**
   WorkManager with a network constraint — it persists the request and survives process death and reboots, running once conditions are met.
2. **What's the difference between a notification message and a data message in FCM?**
   A notification message can be shown by the OS automatically without app code running. A data message is delivered to the app's code, which decides what to do — needed for any custom handling.
3. **Why can't you rely on push notifications arriving reliably?**
   Delivery is best-effort — the OS can delay or drop messages, especially under battery optimisation. Always have a fallback sync path.
4. **When would you use a foreground service instead of WorkManager?**
   When the work must start immediately, run continuously, and be visibly ongoing to the user (active music playback, a live upload) — not for deferrable background work.
5. **What happens to the FCM device token over time?**
   It can change (app reinstall, data clear, token rotation) — the app must detect refresh and send the new token to the backend, or that device stops receiving pushes.

---

#### 14. Common Mistakes

1. Using a raw background thread instead of WorkManager for work that must survive app closure.
2. Assuming push notifications always arrive, with no fallback sync.
3. Not handling FCM token refresh, silently losing push delivery for that device.
4. Requesting the notification permission at app launch instead of in context.
5. Running frequent, unnecessary periodic sync, draining battery and data.

---

#### 15. Related Topics

1. `3` Coroutines & Flow — screen-scoped work vs WorkManager's deferrable work
2. `4` App Components & Lifecycle — deep linking from a tapped notification
3. `9` Local Storage & Offline-First — sync is the usual reason for background work
4. `SD 24` Real-Time Communication & Push — the backend side of push delivery
5. `19` Device Capabilities & Permissions — the notification permission flow

---

#### 16. Interview Must Remember

1. **WorkManager = deferrable, guaranteed, constraint-based background work.**
2. **Match the tool to the urgency**: screen-scoped coroutine, WorkManager, or a foreground service.
3. **Push is best-effort, not guaranteed** — always have a fallback.
4. **Handle FCM token refresh**, or that device silently stops receiving pushes.
5. Background restrictions exist to **protect battery** — work with them, not around them.
