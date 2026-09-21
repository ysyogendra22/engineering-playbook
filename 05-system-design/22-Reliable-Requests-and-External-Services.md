# Reliable Requests & External Services

Roadmap topic 22 · Stage 5: Async & Reliability

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** networks and other services fail. Set timeouts, retry the right way, and make repeated requests safe, so a retry never charges someone twice.

---

#### 1. Timeouts — 🟢 Must Know

*Never wait forever.*

1. Set a timeout on **every** call: app → server, server → database, server → another service.
2. Without a timeout, slow calls pile up and use all threads (the system freezes).
3. Set timeouts smaller than the caller's own timeout, so failures are handled from the inside out.

---

#### 2. Retries with Backoff and Jitter — 🟢 Must Know

*Retry the right errors, wait longer each time, and add randomness.*

1. Retry only **transient** failures (timeouts, `503`, connection reset). Not `400` or `404`.
2. Retry only if the operation is **safe to repeat** (idempotent).
3. **Exponential backoff** — wait longer each time: 1 s, 2 s, 4 s, 8 s.
4. **Jitter** — add randomness, so thousands of clients don't retry at the same moment (a retry storm).
5. **Limit** the number of retries.

```text
wait = random(0, base × 2^attempt)   (capped at a maximum)
```

**Mobile view:** the app follows the same rule: exponential backoff with jitter, and the same idempotency key on every retry of a payment.

---

#### 3. Idempotency Keys — 🟢 Must Know

*Same request twice → same result, one effect.*

Problem: the app sends a payment, the network times out, the app retries. Was the user charged once or twice?

```text
1. App creates a unique key (UUID) for this payment attempt
2. App sends: POST /payments  + Idempotency-Key: abc-123
3. Server checks: have I seen abc-123?
     no  → process, save key → result
     yes → return the saved result, do NOT charge again
```

1. Store the key with the result (with an expiry).
2. Use the same key for every retry of the same action.

---

#### 4. Delivery Guarantees — 🟢 Must Know

*At-most-once, at-least-once, exactly-once: what each one means.*

| | Meaning | Risk |
|---|---|---|
| **At-most-once** | Sent once, never retried | May be **lost** |
| **At-least-once** | Retried until acknowledged | May be **duplicated** |
| **"Exactly-once"** | Processed once | Very hard to guarantee end to end |

In practice: **at-least-once delivery + idempotent processing = exactly-once effect.**

---

#### 5. Third-Party APIs and Webhooks — 🟡 Good to Know

*External services fail and set limits. Plan for both.*

1. Respect the provider's **rate limits**, and handle their downtime (queue and retry later).
2. **Webhook** — the provider calls your endpoint when something happens (a payment succeeded).
   - **Verify the signature** so you know it's real.
   - Expect **duplicates** and **out-of-order** events.
   - Reply `2xx` **quickly**, and process the event in the background.
3. Keep external calls **outside database transactions**.

---

#### 6. Reconciliation — 🟡 Good to Know

*Compare your records with theirs to catch what went wrong.*

1. Periodically compare **your records** with the provider's (for example, every payment).
2. It catches missed webhooks and mismatches.
3. Common in payments and other money flows.

---

#### 7. Common Interview Questions

1. **The payment call times out. Did the user get charged? What do you do?**
   Unknown. Retry with the same idempotency key, or query the payment status. The provider returns the original result instead of charging twice. Reconcile later.
2. **How do you retry safely?**
   Only transient errors and idempotent operations, with exponential backoff, jitter, and a retry limit.
3. **What is a retry storm?**
   Many clients retrying together and overloading a recovering service. Backoff and jitter prevent it.
4. **At-most-once vs at-least-once?**
   At-most-once may lose messages. At-least-once may duplicate them. Use at-least-once with idempotent handlers.
5. **How do you handle webhooks?**
   Verify the signature, be idempotent about duplicates, respond fast, and process asynchronously.

---

#### 8. Common Mistakes

1. No timeouts.
2. Retrying immediately and forever.
3. Retrying non-idempotent operations (payments) without an idempotency key.
4. Retrying errors that will never succeed (`400`).
5. Trusting webhooks without checking the signature.
6. Calling slow external services inside a database transaction.

---

#### 9. Related Topics

1. `03` API Design (idempotency, in `04-backend-engineering`)
2. `21` Queues, Events & Background Jobs
3. `25` Overload & Failure Handling
4. `32` Practice Designs (payment system)

---

#### 10. Interview Must Remember

1. **Timeouts on every call.**
2. **Retry** transient failures with **backoff + jitter + limit.**
3. **Idempotency key** = safe retries.
4. **At-least-once + idempotent processing** = exactly-once effect.
5. **Webhooks:** verify, dedupe, respond fast.
