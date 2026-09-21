# Queues, Events & Background Jobs

Roadmap topic 21 · Stage 5: Async & Reliability

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** don't make the user wait for slow work. Put a message on a queue, reply immediately, and let workers finish the job in the background.

---

#### 1. Producers, Consumers, Workers — 🟢 Must Know

*The basic picture: one side adds jobs, another side does them.*

```text
API (producer) → [ Queue ] → Worker (consumer)
   returns fast                 does the slow job
```

1. **Producer** — adds a message (job) to the queue.
2. **Queue** — holds messages until a worker takes them.
3. **Consumer / worker** — takes a message and processes it.

Why use a queue:

1. The user gets a **fast response**.
2. It **absorbs traffic spikes** (the queue grows, workers catch up).
3. **Decouples** services: the producer doesn't need the consumer to be up.
4. Failed jobs can be **retried**.

Examples: send email or push notification, resize an image, generate a report, update a search index.

**Mobile view:** WorkManager (Android) and BGTaskScheduler (iOS) are the same idea on the phone: hand the work to a system that runs and retries it later.

---

#### 2. Queue vs Publish–Subscribe — 🟢 Must Know

*One worker per message, or a copy for every subscriber.*

| | Queue | Pub/Sub |
|---|---|---|
| Delivery | Each message goes to **one** worker | Each message goes to **every subscriber** |
| Use | Share the work | Broadcast an event |
| Example | Resize image jobs | "Order placed" → email service, analytics, inventory |

---

#### 3. Ack, Retry, Dead-Letter Queue — 🟢 Must Know

*How a queue handles failure without losing messages.*

1. **Ack (acknowledge)** — the worker confirms success. Only then is the message removed.
2. If the worker crashes or fails, no ack → the message is **redelivered**.
3. **Retry with backoff** — wait longer between attempts.
4. **Dead-letter queue (DLQ)** — messages that keep failing go here for investigation, so they don't block everything else.

```text
Queue → Worker → fails → retry → retry → retry → Dead-Letter Queue
```

---

#### 4. At-Least-Once Delivery and Idempotent Handlers — 🟢 Must Know

*A message can arrive twice, so processing it twice must be safe.*

1. Most queues guarantee **at-least-once**: a message may be delivered **more than once**.
2. So handlers must be **idempotent**: processing twice gives the same result as once.

```text
Bad:   "add 100 to balance"                → double credit on retry
Good:  "set payment 123 to PAID" / check the message ID was already processed
```

3. Store processed message IDs, or use unique constraints.

---

#### 5. Ordering Guarantees — 🟢 Must Know

*When order matters, and where the queue keeps it.*

1. A simple queue does not always keep global order, especially with several workers.
2. Ordering is usually guaranteed **only within one queue or partition**.
3. If order matters for one entity (all events of one order), send them to the same partition using a key (`order_id`).
4. Full global ordering limits scale. Avoid needing it.

---

#### 6. Fan-out on Write vs Read (News Feed) — 🟢 Must Know

*How does a post reach the followers' feeds?*

| | Fan-out on write (push) | Fan-out on read (pull) |
|---|---|---|
| When | When a user posts, copy the post into every follower's feed | When a user opens the feed, fetch posts from everyone they follow |
| Read | Very fast | Slower |
| Write | Heavy (one post × many followers) | Cheap |
| Problem | Celebrity with 50M followers | Slow feed for users following many accounts |

**Hybrid (common answer):** fan-out on write for normal users, fan-out on read for celebrities, merged at read time. Workers do the fan-out through queues.

---

#### 7. Event Streams (Kafka) — 🟡 Good to Know

*A queue that keeps a log of events, so many consumers can read and re-read them.*

1. **Topic** split into **partitions**. Order is guaranteed **within a partition**.
2. **Consumer group** — the partitions are shared among the group's consumers; each partition is read by one consumer in the group.
3. Messages are **kept for a period** (retention), so consumers can **replay** from an earlier position (offset).
4. Good for high volume, analytics, and event-driven systems.
5. Simple queues (SQS, RabbitMQ) are enough for basic background jobs.

---

#### 8. Scheduled and Delayed Jobs — 🟡 Good to Know

*Jobs that run at a set time, or after a delay.*

1. **Scheduled** — run at a time or interval (nightly cleanup, daily report).
2. **Delayed** — run after N minutes (release an unpaid ticket hold after 10 minutes).
3. Limit worker concurrency so you don't overload the database or third-party APIs.

---

#### 9. Common Interview Questions

1. **Sending a notification is slow. How do you keep the API fast?**
   The API saves the request and puts a job on a queue, then returns. Workers send the notification with retries and a dead-letter queue.
2. **Queue vs pub/sub?**
   Queue: one worker per message. Pub/sub: every subscriber gets a copy.
3. **What if a worker crashes halfway?**
   No ack, so the message is redelivered. The handler must be idempotent.
4. **What if a message keeps failing?**
   Retry with backoff, then move it to a dead-letter queue.
5. **How do you keep the order of events for one order?**
   Use a partition key (`order_id`) so its events go to the same partition.
6. **Fan-out on write or read for a news feed?**
   Hybrid: push for normal users, pull for celebrities.
7. **Kafka vs a simple queue?**
   Kafka keeps a replayable log with partitions and consumer groups. A simple queue is enough for basic job processing.

---

#### 10. Common Mistakes

1. Non-idempotent handlers with at-least-once delivery.
2. No dead-letter queue, so one bad message blocks everything.
3. Assuming global ordering.
4. Unbounded retries with no backoff.
5. Using a queue for work the user needs immediately.
6. No monitoring of queue length.

---

#### 11. Related Topics

1. `22` Reliable Requests & External Services
2. `25` Overload & Failure Handling (backpressure)
3. `26` Service Boundaries & Architecture (outbox)
4. `32` Practice Designs (notification system, news feed)

---

#### 12. Interview Must Remember

1. **Producer → queue → worker.** Fast response, spike protection, retries.
2. **Ack, retry with backoff, DLQ.**
3. **At-least-once → idempotent handlers.**
4. Order is guaranteed **only within a partition.**
5. **Feed fan-out:** push for normal users, pull for celebrities.
