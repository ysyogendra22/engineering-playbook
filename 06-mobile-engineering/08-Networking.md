# Networking

Roadmap topic 8 · Stage 3: Data & Background

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** the app's networking layer is where "the backend can be slow, flaky, or wrong" meets "the user should never see that". Interceptors, timeouts, retries, and clean error models are what turn a raw HTTP client into something an app can build on.

---

#### 1. HTTP Client Basics from the App's Side — 🟢 Must Know

The app is the **client** in the request-response flow (`BE 2`): it builds a request, sends it over HTTPS, and parses the response — everything in this topic is about doing that reliably on an unreliable mobile network.

---

#### 2. OkHttp, Retrofit, Ktor — 🟢 Must Know

1. **OkHttp** — the underlying HTTP client for most Android networking: connection pooling, interceptors, caching.
2. **Retrofit** — sits on top of OkHttp, turning HTTP endpoints into typed Kotlin interfaces.
3. **Ktor** — a Kotlin-first networking library, usable on Android and in Kotlin Multiplatform shared code (topic `17`).

```kotlin
interface NotesApi {
    @GET("notes")
    suspend fun getNotes(@Query("cursor") cursor: String?): NotesResponse
}
```

---

#### 3. JSON Serialization — 🟢 Must Know

1. **kotlinx.serialization** or **Moshi** convert JSON to Kotlin objects and back.
2. **Handle unknown fields gracefully** — the backend can add new fields at any time (old app versions must not crash parsing a response with fields they don't know about, `SD 30`).

---

#### 4. Interceptors — 🟢 Must Know

An **interceptor** sees every request and response passing through the client — used for attaching auth headers, logging, and retry logic, in one central place instead of repeating it at every call site.

```kotlin
class AuthInterceptor(private val tokenProvider: () -> String?) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val request = chain.request().newBuilder()
            .apply { tokenProvider()?.let { addHeader("Authorization", "Bearer $it") } }
            .build()
        return chain.proceed(request)
    }
}
```

---

#### 5. Auth Tokens: Attach, Refresh, Avoid Storms — 🟢 Must Know

1. Attach the access token to every authenticated request via an interceptor.
2. On a `401`, refresh the token and retry the original request once.
3. **Avoid a refresh storm** — if ten requests fail with `401` at once, don't trigger ten separate refresh calls; coordinate so only one refresh happens, and the others wait for it and reuse the new token.

---

#### 6. Timeouts, Retries, Idempotency — 🟢 Must Know

1. Set connect/read/write **timeouts** — never wait forever on a request.
2. **Retry with backoff** on transient failures (`SD 22`), but only for requests that are safe to repeat.
3. **Idempotency matters more on mobile, not less** — a flaky connection makes retries routine, so a "create order" request needs an idempotency key or it can create duplicates on retry.

---

#### 7. Error Modelling — 🟢 Must Know

Map every kind of failure into one consistent app-level error type, the same principle as topic `6`'s architecture guidance:

```kotlin
sealed interface NetworkError {
    data class Http(val code: Int, val message: String) : NetworkError
    object Timeout : NetworkError
    object NoConnection : NetworkError
    data class Parsing(val cause: Throwable) : NetworkError
    data class Business(val code: String, val message: String) : NetworkError   // app-level error from the API
}
```

---

#### 8. Pagination — 🟢 Must Know

1. **Cursor-based pagination** is preferred over offset-based on mobile (`BE 3`) — stable under inserts/deletes, cheaper for the backend.
2. The **Paging library** (`Pager`, `PagingSource`) integrates cursor pagination with `LazyColumn` (topic `5`), handling loading states and prefetching automatically.

---

#### 9. HTTP Caching — 🟢 Must Know

`Cache-Control` and `ETag`/conditional requests let the client reuse a cached response, or ask "has this changed?" and get a cheap `304 Not Modified` instead of re-downloading — saves both data and battery.

---

#### 10. Image Loading and Caching — 🟡 Good to Know

Libraries like **Coil** or **Glide** handle downloading, memory/disk caching, resizing, and lifecycle-aware cancellation for images — writing this by hand is rarely worth it.

---

#### 11. Uploads and Downloads — 🟡 Good to Know

Large file transfers need progress reporting, resume support (so a dropped connection doesn't restart from zero), and should generally run through **background work** (topic `10`) rather than blocking a screen.

---

#### 12. WebSockets and Server-Sent Events — 🟡 Good to Know

For real-time updates (a chat screen, live scores), see `SD 24` for the backend side and topic `18` for how this fits into a mobile system design.

---

#### 13. Connectivity Checks — 🟡 Good to Know

Check for a metered vs unmetered (Wi-Fi) connection before starting large, non-urgent transfers, and react to connectivity changes rather than only failing silently when offline.

---

#### 14. GraphQL and gRPC — 🟡 Good to Know

Alternatives to REST, each with their own Android client libraries — know the names and general trade-offs (`SD` API design notes) even if REST is the default.

---

#### 15. Compression and Payload Size — 🟡 Good to Know

Smaller payloads and gzip/Brotli compression directly reduce data usage and latency on mobile networks — API design decisions here (`BE 3`) have a real, felt impact on the client.

---

#### 16. iOS Equivalent — 🟡 Good to Know

`URLSession` is iOS's networking foundation, roughly analogous to OkHttp — see topic `16`.

---

#### 17. Common Interview Questions

1. **How do you handle token refresh without triggering many redundant refresh calls?**
   Coordinate refreshes through a single in-flight request (a mutex or shared `Deferred`), so concurrent `401`s wait for one refresh and reuse its result.
2. **Why prefer cursor pagination over offset pagination?**
   Stable under concurrent inserts/deletes, and doesn't require the database to skip and count rows.
3. **How do you keep the app resilient to a flaky mobile network?**
   Timeouts, retries with backoff for safe (idempotent) requests, a clear error model, and cached/offline data shown while retrying.
4. **Why must the client tolerate unknown JSON fields?**
   Old app versions stay in use for years; the backend evolves independently, and a strict parser would crash on any new field (`SD 30`).
5. **What's the role of an interceptor?**
   Central place to modify every outgoing request or inspect every response — auth headers, logging, retry logic — instead of duplicating that logic at each call site.

---

#### 18. Common Mistakes

1. No timeout set, so a hung connection blocks a screen indefinitely.
2. Retrying non-idempotent requests (like a payment) without an idempotency key.
3. A strict JSON parser that crashes on unknown fields.
4. Triggering a separate token refresh for every concurrent `401`.
5. Loading full-resolution images without a library handling resizing and caching.

---

#### 19. Related Topics

1. `3` Coroutines & Flow — `suspend` functions as the natural shape for network calls
2. `6` App Architecture — the error model feeding into UI state
3. `9` Local Storage & Offline-First — how cached/offline data backs up flaky networking
4. `SD 22` Reliable Requests & External Services — the backend-side view of retries and idempotency

---

#### 20. Interview Must Remember

1. **Interceptors centralise auth, logging, and retry logic.**
2. **Coordinate token refresh** to avoid a refresh storm on concurrent `401`s.
3. **Cursor pagination** over offset, on mobile.
4. **One consistent error model**, mapped from every possible failure type.
5. Tolerate **unknown JSON fields** — old app versions must survive backend evolution.
