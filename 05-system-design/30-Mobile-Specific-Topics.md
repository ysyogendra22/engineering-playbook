# Mobile-Specific Topics

Roadmap topic 30 · Stage 7: Mobile (New topic)

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** your users are on phones: unreliable networks, limited battery and data, and old app versions that never go away. This is where you can stand out as a mobile engineer in a system design interview.

---

#### 1. Flaky Networks — 🟢 Must Know

*Design as if the network will fail, because it will.*

1. Set **timeouts**, and show clear loading, error, and retry states.
2. **Retry with backoff and jitter**, and only when the request is safe (idempotent).
3. Show **cached data first**, then refresh.
4. Handle offline mode: what works offline and what doesn't.

---

#### 2. Old App Versions and Backward Compatibility — 🟢 Must Know

1. Users don't update. Old versions can stay in use for years.
2. The API must not break them: **add fields, never remove or rename** (topic `03`).
3. The app should ignore unknown fields.
4. Use API versions if needed, and a **force-update** screen for versions you can't support.
5. Use **feature flags** to control new features from the server.

---

#### 3. Offline-First and Sync — 🟢 Must Know

*A common mobile system design question.*

```text
UI  ⇄  Local database (source of truth for the UI)  ⇄  Sync engine  ⇄  Server
```

1. The app reads and writes to a **local database** (Room, Core Data). The UI is always fast and works offline.
2. Changes are stored in a **pending queue** ("outbox") and sent when the network returns.
3. **Client-generated IDs** and **idempotency keys** prevent duplicates when retrying.
4. **Delta sync** — download only what changed since the last sync (`GET /changes?since=<cursor>`); include **deletions** (tombstones).
5. **Conflicts** — the same item was edited on two devices: last-write-wins, merge fields, or ask the user.
6. Push notification can trigger a sync.

---

#### 4. Infinite Scroll and Image Loading — 🟢 Must Know

1. **Cursor pagination** for feeds (topic `03`), and prefetch the next page before the user reaches the end.
2. Serve images through a **CDN**, in the **right size** for the screen (thumbnails in lists).
3. Cache images on the device (memory and disk).
4. Placeholders and lazy loading keep scrolling smooth.

---

#### 5. Push Notifications and Token Refresh — 🟢 Must Know

1. **Push (FCM/APNs)** reaches closed apps. It's best effort (topic `24`).
2. Send small payloads and let the app fetch details.
3. **Token refresh** — when the access token expires (`401`), refresh once, retry the request, and don't refresh in parallel from many requests (topic `05`).

---

#### 6. Battery and Data Saving — 🟡 Good to Know

1. **Batch** requests instead of many small ones. Avoid constant polling.
2. **Compress** responses (`gzip`) and send smaller payloads (only needed fields).
3. Use **delta sync** and conditional requests (`ETag` → `304`).
4. Respect OS **background limits**, and schedule background work sensibly.

---

#### 7. Adaptive Video Streaming — 🟡 Good to Know

1. Video is split into small segments in **several quality levels** (HLS or DASH).
2. The player switches quality based on the current network speed.
3. Segments are served from a CDN.

---

#### 8. Certificate Pinning and App Attestation — 🟡 Good to Know

1. **Certificate pinning** — the app trusts only your server's certificate, blocking man-in-the-middle attacks. Plan certificate rotation carefully.
2. **App attestation** (Play Integrity on Android, App Attest on iOS) — proves the request comes from your genuine app.
3. Never ship secrets in the app.

---

#### 9. Common Interview Questions

1. **Design an offline-first notes app that syncs across devices.**
   Local database as the source of truth, pending-change queue, client-generated IDs, delta sync with a cursor, conflict rule, push to trigger sync.
2. **How do you handle old app versions?**
   Backward compatible API (add only), versioning if needed, feature flags, and force-update.
3. **How would you design an image-heavy infinite feed on mobile?**
   Cursor pagination, prefetch, CDN with multiple image sizes, memory and disk cache, placeholders.
4. **How do you reduce battery and data usage?**
   Batching, compression, delta sync, conditional requests, no constant polling.
5. **What happens when the token expires during many parallel requests?**
   Refresh once, queue the other requests, and retry them with the new token.

---

#### 10. Common Mistakes

1. Assuming a stable network.
2. Breaking the API for old app versions.
3. Full refresh of all data on every sync.
4. No conflict strategy for offline edits.
5. Retrying non-idempotent requests without an idempotency key.
6. Full-size images in list screens.

---

#### 11. Related Topics

1. `03` API Design (compatibility, pagination, in `04-backend-engineering`)
2. `05` Authentication & Authorization (token refresh)
3. `16` File Storage & CDN
4. `20` Unique ID Generation (client-generated IDs)
5. `23` Consistency & CAP (conflicts)
6. `24` Real-Time Communication & Push
7. Mobile client design (`06-mobile-engineering`)

---

#### 12. Interview Must Remember

1. **Plan for failure:** timeouts, retries, cached data, offline mode.
2. **Never break old app versions.**
3. **Offline-first:** local DB, pending queue, delta sync, client IDs, conflict rule.
4. **Cursor pagination + CDN images** for feeds.
5. **Push** reaches closed apps. **Delta sync and batching** save battery.
