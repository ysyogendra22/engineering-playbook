# Mobile System Design

Roadmap topic 18 · Stage 7: Mobile in the System

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** a mobile system design question is the same design process as `SD 31`, plus a client half that's easy to forget: what happens on a bad network, an old app version, or a dying battery. Interviewers specifically watch for whether you bring up the client side unprompted.

---

#### 1. The Steps — 🟢 Must Know

Follow the same structure as `SD 31`: **requirements → APIs → local data → architecture → caching → sync → failures → performance.** The client-specific additions are what fill out steps 3, 5, 6, and 7 with real mobile substance, covered below.

---

#### 2. Client-Side Concerns — 🟢 Must Know

*Bring these up without being asked — they're the signal that separates a mobile-aware answer from a generic backend answer (full detail in `SD 30`).*

1. **Flaky networks** — timeouts, retries, offline states (topic `8`).
2. **Offline support** — what works with no connectivity, and what's clearly disabled.
3. **Old app versions** — the design must keep working for versions already in the wild (topic `1`).
4. **Battery** — background sync frequency, location usage, and polling all have a real battery cost.

---

#### 3. Data Flow — 🟢 Must Know

```text
UI (Compose)  →  ViewModel  →  Repository  →  Local database (source of truth)  →  Network
```

The same layering as topic `6` and `9` — walk through this explicitly in the design, since it's exactly what an interviewer wants to see you reach for by default.

---

#### 4. Pagination and Infinite Scroll — 🟢 Must Know

Cursor-based pagination (topic `8`) combined with `LazyColumn`/Paging (topic `5`) — prefetch the next page before the user hits the bottom, so scrolling never visibly pauses to load.

---

#### 5. Image Loading and Caching — 🟢 Must Know

A dedicated library (Coil/Glide, topic `8`) handling memory/disk caching, resizing, and cancellation — call this out specifically rather than describing a custom image pipeline, unless the question is specifically about building one.

---

#### 6. Real-Time Updates — 🟢 Must Know

Polling, WebSocket, or push (`SD 24`) — pick based on how real-time the feature truly needs to be, and the battery/data cost of each option (topic `10`).

---

#### 7. Uploads — 🟢 Must Know

Chunking (for large files), resume support (so a dropped connection doesn't restart from zero), retry, and running through background work rather than blocking a screen (topics `8`, `10`).

---

#### 8. Sync Design — 🟢 Must Know

What to sync, when (on open, periodically, on a push trigger), how conflicts are resolved, and how deletes propagate — the same detail as topic `9`, applied to the specific feature being designed.

---

#### 9. Analytics and Logging Pipeline — 🟡 Good to Know

How client events reach the backend (batched, on a schedule, respecting metered connections) — worth a brief mention as part of "how do we know this works in production" (topic `15`).

---

#### 10. Feature Flags and Config Delivery — 🟡 Good to Know

How the app fetches remote config/feature flags (topic `15`) — relevant when the design includes anything you'd want to disable remotely without a release.

---

#### 11. Location-Based Features — 🟡 Good to Know

Precision needed, foreground vs background usage, and the real battery cost of continuous location tracking (topic `19`).

---

#### 12. Video Playback and Adaptive Streaming — 🟡 Good to Know

Covered in `SD 30` from the system design side — relevant if the design includes any media playback.

---

#### 13. Client-Side Rate Limiting and Back-off — 🟡 Good to Know

The client's own responsibility to not hammer the backend — debouncing, request coalescing, and backing off on repeated failures (topic `8`), not just relying on the server to reject excess requests.

---

#### 14. Designs to Practise — 🟢 / 🟡 Must and Good to Know

**Practise these, in order (🟢 first):**

1. 🟢 **News feed** — pagination, caching, fan-out concerns from the backend side (`SD 21`)
2. 🟢 **Chat app** — real-time delivery, offline queuing, message ordering
3. 🟢 **Offline-first notes app** — the running example throughout this whole folder
4. 🟢 **Photo or file upload** — chunking, resume, background work
5. 🟡 Search with autocomplete, ride tracking with live location, a video player, a checkout flow, an image gallery with caching

---

#### 15. Common Interview Questions

1. **How is a mobile system design question different from a general system design question?**
   It adds a genuine client-side half: flaky networks, offline support, old app versions, and battery — an interviewer expects these raised without prompting.
2. **Design an offline-first notes app.**
   Local database as source of truth (topic `9`), a repository syncing it with the backend, conflict resolution for concurrent edits, and background sync via WorkManager (topic `10`).
3. **How would you design image loading for a photo-heavy feed?**
   A caching image library (memory + disk cache), resized/downsampled loads matching the display size, prefetching alongside pagination, and cancellation tied to the visible viewport.
4. **How do you handle real-time chat delivery reliably on a flaky mobile connection?**
   WebSocket with reconnect and backoff, a local queue for messages sent while offline, message IDs for deduplication, and a fallback (push notification) when the socket isn't connected.
5. **What would you say about backward compatibility in a mobile design?**
   Any API or data-format change must keep working for app versions already in the wild — plan additive changes and versioning (`SD 30`) rather than assuming everyone is on the latest release.

---

#### 16. Common Mistakes

1. Answering like it's a pure backend design question, never mentioning the client side.
2. Forgetting offline behaviour entirely.
3. Ignoring battery and data cost when proposing real-time or background features.
4. Designing as if every user is on the latest app version.
5. Skipping the local-database-as-source-of-truth pattern in favour of "the UI just calls the API".

---

#### 17. Related Topics

1. `6` App Architecture, `9` Local Storage & Offline-First — the layering this design walks through
2. `SD 30` Mobile-Specific Topics, `SD 31` Interview Answer Structure — the system-design-side counterparts
3. `22` Practice: Projects & Exercises — hands-on projects that build toward these designs

---

#### 18. Interview Must Remember

1. **Same steps as `SD 31`, plus the client half** — bring up flaky networks, offline, old versions, and battery unprompted.
2. **Local database as source of truth**, synced with the backend — the default data flow to reach for.
3. **Cursor pagination + a caching image library** for feeds — name-drop the specific tools, don't reinvent them.
4. **Backward compatibility** is a standing constraint on every mobile design.
