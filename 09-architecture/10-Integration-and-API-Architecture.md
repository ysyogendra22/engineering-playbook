# Integration & API Architecture

> Systems talk through contracts. Design the API first, make changes backward compatible, expect retries and duplicates, and protect your system from the failures and models of the services you call.

Roadmap topic 10 · Stage 3: Cross-Cutting Concerns

**Go deeper:** `04-backend-engineering/03-API-Design` · `05-system-design/22-Reliable-Requests-and-External-Services`, `24-Real-Time-Communication-and-Push`, `26-Service-Boundaries-and-Architecture`, `30-Mobile-Specific-Topics` · `6` Patterns · `7` DDD (ACL) · `8` Boundaries.

**Marks:** 🟢 must know · 🟡 good to know

---

#### 1. What Is It?

*How systems exchange data and requests, reliably and over time.*

| 🟢 Must know | 🟡 Good to know |
|---|---|
| synchronous vs asynchronous integration | REST, GraphQL, gRPC: when each fits |
| API-first: contract before code | events and messaging contracts, schema registries |
| versioning and backward compatibility | API gateway responsibilities |
| idempotency and retries across boundaries | anti-corruption layer around external systems |
| third-party integration: rate limits, failures, webhooks, reconciliation | |

1. **Contract:** the agreed requests, responses, errors and behaviour.
2. **Synchronous:** the caller waits (HTTP request/response). **Asynchronous:** the caller sends a message and continues (queue, event).
3. **Backward compatibility:** old clients keep working with new servers.

**Signals in an interview:** "REST or GraphQL?", "how do you version an API for mobile?", "what if the payment provider times out?", "how do you handle webhooks?", "sync or async between services?".

---

#### 2. How It Works

**Synchronous vs asynchronous.**

| | Synchronous (request/response) | Asynchronous (events, queues) |
|---|---|---|
| Coupling | caller needs the callee up now | loose in time |
| Latency | caller waits | caller continues |
| Failure | propagates to the caller | buffered, retried |
| Consistency | immediate answer | eventual |
| Good for | queries, user-facing actions needing a result | notifications, fan-out, slow work, integration |

Use a synchronous call when the user needs the answer now; use async for anything that can happen later or that many consumers need. Mix them: a synchronous "accepted" response (`202`) plus asynchronous completion and a push (`SD 26`).

**API-first.** Design the contract first (OpenAPI, GraphQL schema, protobuf), review it with clients, generate mocks and clients, and write the server against it. Parallel work, fewer surprises, and a documented contract (`BE 3`).

**Versioning and backward compatibility.** Old app versions never go away, so:

1. **Add, never remove or rename** fields; new fields optional.
2. Clients **ignore unknown fields**.
3. Version breaking changes (`/v2`, header, or schema evolution) and keep `/v1` until usage drops.
4. Declare a **minimum supported version** and a **force-update** path.
5. Run **contract tests**: every consumer's expectations are checked against the provider.
6. Use feature flags/server config to roll out behaviour changes.

**Idempotency and retries across boundaries.** Networks fail; clients and brokers retry; the same request can arrive twice. Make writes idempotent with an **idempotency key** (stored with the result), use natural keys/unique constraints, and design consumers to be idempotent (`SD 22`). Use exponential backoff with jitter and limits.

**Third-party integration.**

| Concern | Practice |
|---|---|
| Rate limits | respect them; queue and throttle; handle `429` and `Retry-After` |
| Failures | timeouts, retries, circuit breakers, fallbacks |
| Webhooks | verify the signature; accept duplicates and out-of-order delivery; respond fast and process asynchronously |
| Reconciliation | periodically compare your records with theirs; repair differences |
| Sandbox/test | use the provider's sandbox in CI and staging |
| Isolation | wrap in an adapter / anti-corruption layer so their model doesn't leak |
| Exit | keep the integration replaceable |

🟡 **REST, GraphQL, gRPC.**

| | REST | GraphQL | gRPC |
|---|---|---|---|
| Style | resources + HTTP verbs | one endpoint, client picks fields | typed RPC over HTTP/2 with protobuf |
| Strength | simple, cacheable, ubiquitous | fewer round trips, flexible for varied clients | fast, streaming, strict contracts |
| Cost | over/under-fetching, many calls | complexity, caching, query cost control | tooling for browsers/mobile, harder to debug |
| Fit | public and mobile APIs | complex UIs, several clients | service-to-service, low latency |

🟡 **Events and messaging contracts.** Events are contracts too: name them as business facts (`NoteShared`), version the schema, keep changes backward compatible, and consider a **schema registry** to validate producers and consumers. Include an event id (for deduplication) and a timestamp.

🟡 **API gateway responsibilities.** Authentication, rate limiting, routing, request/response transformation, TLS, logging. Keep business logic out of it.

🟡 **Anti-corruption layer.** A translation layer so an external or legacy model doesn't spread through your code (topics 6, 7).

---

#### 3. Naive vs Better Design

| Naive | Better |
|---|---|
| code first, API as a by-product | contract first, mocks and generated clients |
| rename a field "because it's cleaner" | add a new field, deprecate the old |
| retry any failed `POST` | idempotency key |
| process webhooks inline with no verification | verify signature, store, process asynchronously, de-duplicate |
| trust the provider's data as is | reconcile |
| 20 sequential calls for one screen | an aggregated endpoint or BFF |
| every service calls every other synchronously | async events for fan-out and decoupling |
| a vendor SDK's model in your domain | adapter / ACL |

---

#### 4. Templates & Examples

**Idempotent write handler.**

```kotlin
class IdempotentHandler<R>(private val store: MutableMap<String, R> = HashMap()) {
    fun handle(key: String, work: () -> R): R = store.getOrPut(key, work)               // first call does the work; repeats return the stored result
}
```

Checks: calling `handle("pay-123") { charge() }` twice runs `charge` once and returns the same result both times; a different key runs it again. (Production: persist the key and result in the database with a unique constraint, and handle two concurrent requests with the same key.)

**Backward-compatibility check for a response schema.**

```kotlin
data class Field(val type: String, val required: Boolean)

fun breakingChanges(old: Map<String, Field>, new: Map<String, Field>): List<String> = buildList {
    old.forEach { (name, f) ->
        val n = new[name]
        when {
            n == null -> add("removed field: $name")
            n.type != f.type -> add("type changed: $name ${f.type} → ${n.type}")
        }
    }
    new.forEach { (name, f) -> if (name !in old && f.required) add("new required field: $name") }
}
```

Checks: old `{id: string(req), title: string(req)}`; new adds `dueDate: string(optional)` → `[]` (compatible). New removes `title` → `["removed field: title"]`. New changes `id` to `int` → `["type changed: id string → int"]`. New adds a *required* `owner` → `["new required field: owner"]` (old clients don't send it, for requests; for responses adding a required field is safe, so apply this rule to **requests**). Run this in CI against the published schema.

**Verify a webhook signature (HMAC-SHA256).**

```kotlin
fun hmacHex(secret: String, body: String): String {
    val mac = javax.crypto.Mac.getInstance("HmacSHA256").apply { init(javax.crypto.spec.SecretKeySpec(secret.toByteArray(), "HmacSHA256")) }
    return mac.doFinal(body.toByteArray()).joinToString("") { "%02x".format(it) }
}

fun isValidSignature(secret: String, body: String, header: String) =
    java.security.MessageDigest.isEqual(hmacHex(secret, body).toByteArray(), header.toByteArray())     // constant-time compare
```

Checks: `hmacHex("secret", "{\"id\":1}")` → `03def589620c813f198fd03d7967e292b163ef0435ebf43071ce0e9519763cb7`; a valid header passes; changing one byte of the body or using another secret fails. Also check a timestamp in the signature to prevent replay, and de-duplicate by event id.

**Webhook handler outline.**

```text
1. Read the raw body.  2. Verify signature (and timestamp window).  3. Store the event (unique on event id).
4. Return 200 quickly.  5. Process asynchronously, idempotently.  6. Reconcile nightly with the provider's list API.
```

**Reconciliation.**

```kotlin
data class Diff(val missingHere: Set<String>, val missingThere: Set<String>)

fun reconcile(ours: Set<String>, theirs: Set<String>) = Diff(theirs - ours, ours - theirs)
```

Checks: ours `{p1, p2, p3}`, theirs `{p2, p3, p4}` → `missingHere = {p4}` (we missed a webhook), `missingThere = {p1}` (they never recorded it); repair both, then alert if the numbers grow.

**API change policy (one paragraph for the repo).**

```text
Additive changes are always allowed. Removing or changing a field requires: an ADR, a deprecation notice in the response header and docs,
two release cycles (or the support window of the oldest supported app version), usage below 1%, then removal.
```

**Sync vs async choice.**

```kotlin
fun integrationStyle(userWaits: Boolean, manyConsumers: Boolean, slowWork: Boolean) =
    if (userWaits && !slowWork && !manyConsumers) "synchronous call" else "asynchronous (202 + event/push)"
```

Checks: loading a note `(true, false, false)` → synchronous; exporting a report `(true, false, true)` → asynchronous; publishing `NoteShared` for search, notifications and analytics `(false, true, false)` → asynchronous.

---

#### 5. Numbers & Rules of Thumb

| Item | Guide |
|---|---|
| Timeouts | every outbound call; connect 1 to 5 s, read 5 to 30 s |
| Retries | 3 to 5 with backoff and jitter; idempotent calls only |
| Idempotency key retention | 24 hours to 7 days |
| Webhook response | under a few seconds; process after responding |
| Replay window | signatures valid for about 5 minutes |
| Deprecation period | the support window of the oldest supported app version (often 6 to 12 months) |
| API calls per screen | ideally 1 to 3 |
| Reconciliation | daily or hourly for money |

---

#### 6. Common Mistakes & Edge Cases

1. Breaking old clients.
2. Retrying non-idempotent calls.
3. Trusting unsigned webhooks; not handling duplicates and out-of-order events.
4. No timeouts or circuit breakers on third parties.
5. No reconciliation for payments.
6. Chatty APIs (many round trips from the phone).
7. Letting an external model leak into your domain.
8. Using GraphQL/gRPC because it is new.

Edge cases: a provider outage (queue and retry; degrade); webhook replay attacks; clock skew in signatures; a partner that cannot handle your retry rate; schema changes in events with old consumers still running; long-running operations (return a job id and poll or push).

---

#### 7. Say This in the Interview

1. "I design the contract first, review it with the clients, and keep changes add-only; old app versions never go away, so I add a minimum supported version and a force-update path."
2. "Synchronous when the user needs the answer now; asynchronous for slow work and fan-out, usually with a 202 and a push when done."
3. "Across boundaries I assume duplicates: idempotency keys on writes, idempotent consumers, bounded retries with backoff and jitter."
4. "For third parties: timeouts and breakers, an adapter that protects my model, verified signed webhooks that are stored and processed asynchronously, and reconciliation."
5. "REST is my default for mobile APIs; GraphQL when screens need flexible fields; gRPC between services."

---

#### 8. Quick Check

1. Which API changes are always safe?
2. What does an idempotency key do?
3. How do you secure a webhook?
4. Why reconcile?

<details>
<summary>Answers</summary>

1. Adding optional fields or endpoints.
2. Makes repeated requests have the effect of one by storing the first result.
3. Verify an HMAC signature (and timestamp), de-duplicate by event id, respond fast and process asynchronously.
4. Webhooks and calls can be missed or duplicated; comparing records finds and fixes drift.

</details>

---

#### 9. Practice

**Interview questions**

1. Sync vs async integration: how do you choose?
2. How do you version an API for mobile clients?
3. How do you make a payment call safe to retry?
4. How do you integrate a third-party service safely?
5. REST vs GraphQL vs gRPC?
6. How do you design event contracts?

**Exercises**

1. Write an OpenAPI sketch for two endpoints, then add a field and check it is compatible with the checker above.
2. Implement the webhook verifier and tests for tamper and replay.
3. Draw the sequence for "pay" with a timeout and a retry using an idempotency key.
4. Write the reconciliation job for a provider's transaction list.

**Remember:** contract first · add-only changes, minimum version, force-update · sync when the user waits, async otherwise · idempotency keys and bounded retries · verified, stored, async webhooks · reconcile · adapters protect your model.
