# Practice: Projects & Designs

Roadmap topic 32 · Stage 8: Interview

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) added beyond the original roadmaps

**In simple words:** reading isn't enough. Build a few small backends, and practise designs on paper in a fixed order. Start practising early. Don't wait until you finish all the theory.

---

#### 1. Build These Projects (in order) — 🟢 Must Know

| # | Project | Practises |
|---|---|---|
| 1 | **Notes API** | CRUD, SQL, migrations, validation, pagination (topic `12`) |
| 2 | **Extend it** | Auth, ownership checks, tests, deployment |
| 3 | **Notification workflow** | Queue, worker, retries, duplicate prevention |
| 4 | **Reservation / inventory API** | Transactions, concurrent requests, expiry, idempotency |
| 5 | **External integration** | Webhooks with signature checks, retries, state transitions (use a sandbox) |

---

#### 2. How to Practise a Design — 🟢 Must Know

For each design:

1. Set a **timer** (45 minutes).
2. Follow the steps in topic `31`.
3. Write requirements, estimate, APIs, data model, diagram, one deep dive.
4. Say it **out loud**.
5. Afterwards, list what you forgot, and repeat the same design a week later.

---

#### 3. Designs (in order) — 🟢 Must Know

| # | Design | Focus on | Topics |
|---|---|---|---|
| 1 | **Notes app** | Request flow, APIs, data model | `01`–`12` |
| 2 | **URL shortener** | Unique IDs (base62), read-heavy → cache, redirect (`301` vs `302`), expiry, scaling | `15`, `19`, `20` |
| 3 | **File storage & sharing** | Signed URLs, metadata, chunked uploads, permissions, CDN, sync | `16` |
| 4 | **Rate limiter** | Token bucket, Redis atomic counters, gateway, `429` | `25` |
| 5 | **Notification system** | API → queue → workers → push/email/SMS providers, preferences, retries, dedup, per-user limits | `21`, `22`, `24` |
| 6 | **Chat app** | WebSockets, message ordering per conversation, delivery states, offline via push, presence | `23`, `24` |
| 7 | **News feed** | Fan-out on write vs read (hybrid), cursor pagination, caching, celebrities | `15`, `19`, `21` |
| 8 | **Ticket booking** | Seat hold with expiry, transactions or locks, no double booking, idempotent payment | `11`, `22` |
| 9 | **Payment system** | Idempotency keys, state machine, ledger, webhooks, reconciliation | `22`, `26` |
| 10 | **Offline-first sync** (New) | Local DB, pending queue, delta sync, conflicts, client IDs | `30` |

Good first designs to repeat: **URL shortener, rate limiter, chat, news feed.** They cover most of the core ideas.

---

#### 4. Harder or Specialised Designs — 🟡 Good to Know

| Design | Focus on | Needs |
|---|---|---|
| **Video streaming** | Upload → transcode into several qualities → segments (HLS) → CDN, adaptive bitrate | Topics `16`, `30`. Learn transcoding inside this design |
| **Search autocomplete** | Prefix lookup (trie), top suggestions, cache, offline aggregation of query logs | Topic `33` (trie, search) |
| **Nearby places / ride hailing** (New) | Geospatial index (geohash, quadtree), location updates | Topic `33` |
| **Web crawler** (New) | URL frontier queue, politeness per site, duplicate detection | Topics `21`, `33` |
| **Key-value store / distributed cache** (New) | Partitioning, consistent hashing, replication, quorum | Topics `18`, `19`, `23` |

---

#### 5. Order of Learning — 🟢 Must Know

1. Finish the **Notes API** (topic `12`).
2. Start the **notes app**, **URL shortener**, **file storage**, and **rate limiter** after topic `16`. Revisit the URL shortener after topics `18`–`20`.
3. Add the remaining designs as you learn their required concepts.
4. Learn specialised concepts (transcoding, geohash) **inside** their design, not separately.

---

#### 6. Common Interview Questions (design prompts)

1. Design a URL shortener.
2. Design a rate limiter.
3. Design a chat app.
4. Design a news feed.
5. Design a notification system.
6. Design a ticket booking system.
7. Design a payment system.
8. Design an offline-first notes app (mobile).

---

#### 7. Common Mistakes

1. Only reading, no timed practice.
2. Practising only easy designs.
3. Never repeating a design.
4. Skipping the deep dive and failure cases.
5. Memorising one "perfect" answer instead of understanding trade-offs.
6. Practising silently.

---

#### 8. Related Topics

1. `31` Interview Answer Structure
2. `13`–`30` The concepts each design uses
3. `33` Follow-Up Topics
4. `12` Checkpoint Project: Notes API (in `04-backend-engineering`)

---

#### 9. Interview Must Remember

1. **Build small backends** and **practise timed designs.**
2. **URL shortener, rate limiter, chat, news feed** first.
3. Each design has **one main idea** (fan-out, idempotency, double booking...). Know it.
4. **Repeat** designs and say them out loud.
5. Learn specialised topics **inside** the design that needs them.
