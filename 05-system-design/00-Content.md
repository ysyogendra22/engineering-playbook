# System Design: Interview Roadmap

For a mobile engineer preparing for system design interviews.
This is **part 2 (topics 13–33)**. Finish **part 1 (topics 1–12)** in `04-backend-engineering` first, including the Notes API. Each topic gets its own doc later.

**Marks:**

| Mark | Meaning |
|---|---|
| 🟢 | **Must have.** Expected in most interviews. Learn first. |
| 🟡 | **Good to have.** Learn after the 🟢 items are solid. |
| (New) | Added beyond the original two roadmaps. |

---

## Index

| #   | Topic                                 | Stage                        |
| --- | ------------------------------------- | ---------------------------- |
| 13  | Requirements & Estimation             | 4. Scale                     |
| 14  | Scaling & Load Balancing              | 4. Scale                     |
| 15  | Caching                               | 4. Scale                     |
| 16  | File Storage & CDN                    | 4. Scale                     |
| 17  | Choosing a Database                   | 4. Scale                     |
| 18  | Replication                           | 4. Scale                     |
| 19  | Partitioning & Sharding               | 4. Scale                     |
| 20  | Unique ID Generation (New)            | 4. Scale                     |
| 21  | Queues, Events & Background Jobs      | 5. Async & Reliability       |
| 22  | Reliable Requests & External Services | 5. Async & Reliability       |
| 23  | Consistency & CAP                     | 5. Async & Reliability       |
| 24  | Real-Time Communication & Push        | 5. Async & Reliability       |
| 25  | Overload & Failure Handling           | 5. Async & Reliability       |
| 26  | Service Boundaries & Architecture     | 6. Architecture & Production |
| 27  | Observability                         | 6. Architecture & Production |
| 28  | Deployment & Release                  | 6. Architecture & Production |
| 29  | Backup, Recovery, Security & Cost     | 6. Architecture & Production |
| 30  | Mobile-Specific Topics (New)          | 7. Mobile                    |
| 31  | Interview Answer Structure            | 8. Interview                 |
| 32  | Practice: Projects & Designs          | 8. Interview                 |
| 33  | Follow-Up Topics                      | 8. Interview                 |

**Short on time (2 weeks):** after topics 1, 2, 3, 5, 8, 10, 11 in `04-backend-engineering`, do 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 30, 31, 32. 🟢 items only.

---

# Stage 4: Scale

## 13. Requirements & Estimation

- 🟢 Functional vs non-functional requirements
- 🟢 Scope and exclusions
- 🟢 DAU, concurrent users, QPS, peak traffic
- 🟢 Read-heavy vs write-heavy systems
- 🟢 Storage and bandwidth estimates
- 🟢 Latency vs throughput, p50 / p95 / p99
- 🟢 Availability vs durability
- 🟡 (New) Numbers to remember

## 14. Scaling & Load Balancing

- 🟢 Vertical vs horizontal scaling
- 🟢 Stateless servers, shared session state
- 🟢 Load balancer and health checks
- 🟢 Single points of failure
- 🟢 Finding the bottleneck
- 🟡 Load balancing algorithms, sticky sessions, L4 vs L7
- 🟡 Reverse proxy, API gateway, auto-scaling

## 15. Caching

- 🟢 Hit vs miss, where caches live
- 🟢 Cache-aside
- 🟢 TTL, eviction, invalidation
- 🟢 Stale data
- 🟢 Cache stampede and hot keys
- 🟡 Write-through / write-back
- 🟡 Cache penetration (keys that don't exist)
- 🟡 In-process vs shared cache
- 🟡 HTTP cache headers

## 16. File Storage & CDN

- 🟢 Object storage; metadata in the database
- 🟢 Upload and download flow
- 🟢 Signed URLs
- 🟢 CDN basics
- 🟡 Multipart, large and resumable uploads
- 🟡 Thumbnails, cleanup

## 17. Choosing a Database

- 🟢 Relational vs non-relational
- 🟢 Key-value, document, wide-column use cases
- 🟢 Choose by access pattern, not popularity
- 🟡 Graph, search, time-series

## 18. Replication

- 🟢 Leader–follower, read replicas
- 🟢 Sync vs async
- 🟢 Replication lag and stale reads
- 🟢 Failover
- 🟢 Replication is not a backup
- 🟡 Multi-leader and leaderless (names only)

## 19. Partitioning & Sharding

- 🟢 Why and when to shard
- 🟢 Hash vs range
- 🟢 Choosing a shard key
- 🟢 Hotspots and rebalancing
- 🟢 Consistent hashing
- 🟢 Cross-shard queries and transactions
- 🟡 Resharding, directory-based sharding

## 20. Unique ID Generation (New)

- 🟢 Auto-increment vs UUID vs Snowflake-style
- 🟢 Short codes (URL shortener)
- 🟡 Client-generated IDs for offline apps

---

# Stage 5: Async & Reliability

## 21. Queues, Events & Background Jobs

- 🟢 Producers, consumers, workers
- 🟢 Queue vs publish–subscribe
- 🟢 Ack, retry, dead-letter queue
- 🟢 At-least-once delivery, idempotent handlers
- 🟢 Ordering guarantees (per queue / partition)
- 🟢 Fan-out on write vs read (news feed, celebrity problem)
- 🟡 Event streams (Kafka), partitions, replay
- 🟡 Scheduled and delayed jobs

## 22. Reliable Requests & External Services

- 🟢 Timeouts
- 🟢 Retries with backoff and jitter
- 🟢 Idempotency keys
- 🟢 At-most-once vs at-least-once vs "exactly-once" effect
- 🟡 Webhooks: signature, duplicates
- 🟡 Reconciliation

## 23. Consistency & CAP

- 🟢 Strong vs eventual consistency
- 🟢 Read-your-writes
- 🟢 CAP during a network partition
- 🟢 Choose consistency per feature
- 🟡 Quorums
- 🟡 Conflict handling (last-write-wins, merge)

## 24. Real-Time Communication & Push

- 🟢 Short polling, long polling
- 🟢 WebSockets, SSE
- 🟢 Choosing a method
- 🟢 Reconnect and missed-message recovery
- 🟢 (New) Push notifications (FCM / APNs)
- 🟡 Scaling WebSockets, presence

## 25. Overload & Failure Handling

- 🟢 Rate limiting: token bucket, sliding window
- 🟢 Rate limiter placement and shared state (Redis, atomic updates)
- 🟢 Backpressure
- 🟢 Circuit breaker
- 🟢 Load shedding
- 🟢 Graceful degradation
- 🟡 Bulkheads

---

# Stage 6: Architecture & Production

## 26. Service Boundaries & Architecture

- 🟢 Monolith vs microservices
- 🟢 Sync vs async service communication
- 🟢 API gateway, BFF
- 🟡 Transactional outbox, change data capture (CDC)
- 🟡 Sagas
- 🟡 Business states and valid transitions
- 🟡 Service discovery, data ownership per service
- 🟡 Code structure and low-level design basics (separate prep)

## 27. Observability

- 🟢 Logs with request IDs, metrics, tracing
- 🟢 Health and readiness checks
- 🟢 Actionable alerts
- 🟢 SLI and SLO
- 🟡 Incident debugging, postmortems
- 🟡 Mobile crash reporting

## 28. Deployment & Release

- 🟢 CI/CD
- 🟢 Rolling, blue-green, canary releases; rollback
- 🟢 Backward compatibility, safe DB migrations
- 🟡 Docker basics
- 🟡 Feature flags, force-update
- 🟡 Graceful shutdown

## 29. Backup, Recovery, Security & Cost

- 🟢 Backups and tested restores
- 🟢 RPO and RTO
- 🟡 Multi-AZ vs multi-region
- 🟡 Encryption, least privilege, secrets manager
- 🟡 Compute, storage, bandwidth costs

---

# Stage 7: Mobile

## 30. Mobile-Specific Topics (New)

- 🟢 Flaky network: timeouts, retries, offline states
- 🟢 Old app versions and backward compatibility
- 🟢 Offline-first and sync
- 🟢 Infinite scroll and image loading
- 🟢 Push notifications and token refresh
- 🟡 Battery and data saving, delta sync
- 🟡 Adaptive video streaming
- 🟡 Certificate pinning, app attestation

---

# Stage 8: Interview

## 31. Interview Answer Structure

- 🟢 Clarify requirements and scope
- 🟢 Estimate only what changes the design
- 🟢 APIs and data model
- 🟢 High-level design
- 🟢 Deep-dive bottlenecks and failures
- 🟢 Trade-offs and evolution
- 🟢 (New) Time split for a 45-minute round

## 32. Practice: Projects & Designs

**Build (in order)**

- 🟢 Notes API (topic 12 in `04-backend-engineering`)
- 🟢 Add auth, ownership, tests, deployment
- 🟢 Notification workflow (queue + worker)
- 🟢 Reservation / inventory API
- 🟢 External integration with webhooks

**Design (in order)**

- 🟢 Notes app
- 🟢 URL shortener
- 🟢 File storage and sharing
- 🟢 Rate limiter
- 🟢 Notification system
- 🟢 Chat app
- 🟢 News feed
- 🟡 Video streaming (needs transcoding, adaptive streaming)
- 🟡 Search autocomplete (needs trie, search basics from topic 33)
- 🟢 Ticket booking
- 🟢 Payment system
- 🟢 (New) Offline-first sync
- 🟡 (New) Nearby places / ride hailing
- 🟡 (New) Web crawler
- 🟡 (New) Key-value store / distributed cache

## 33. Follow-Up Topics

- 🟡 Leader election and consensus (purpose only)
- 🟡 Distributed locks, leases, fencing tokens
- 🟡 Multi-region: active–passive vs active–active
- 🟡 Large data migrations
- 🟡 Clocks and ordering (clock skew, logical clocks)
- 🟡 CQRS (name only)
- 🟡 (New) Search basics (inverted index)
- 🟡 (New) Geospatial (geohash, quadtree)
- 🟡 (New) Bloom filter, HyperLogLog, trie
- 🟡 (New) Batch vs stream processing

---

## Skip for Now

- Consensus proofs, Kubernetes internals, service mesh, event sourcing
- Cloud product comparisons and certifications

## How to Proceed

1. Finish the Notes API (topic 12) before starting this part.
2. Start practice designs after topic 16 (notes app, file storage, rate limiter). Revisit the URL shortener after topics 18–20.
3. Add the remaining designs as you learn their concepts. Don't wait to finish all theory.
4. For each topic: what it is, what problem it solves, how it works, one downside.
