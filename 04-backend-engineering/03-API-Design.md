# API Design

Roadmap topic 3 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** the API is the contract between your app and the backend. A good contract is predictable, consistent, and doesn't break old app versions.

---

#### 1. REST, Endpoints, JSON — 🟢 Must Know

*Endpoints are nouns (things). The HTTP method is the verb (action).*

```text
GET     /notes          → list notes
POST    /notes          → create a note
GET     /notes/42       → get one note
PATCH   /notes/42       → update a note
DELETE  /notes/42       → delete a note
GET     /users/7/notes  → notes of user 7
```

Rules:

1. Use **nouns, plural**: `/notes`, not `/getNotes` or `/createNote`.
2. Let the **method** carry the action.
3. Keep nesting shallow (one or two levels).
4. Use **JSON**, and keep field names in one style (`camelCase` or `snake_case`).
5. Return `201 Created` for create, `204 No Content` for delete.

---

#### 2. Consistent Responses & Error Format — 🟢 Must Know

*The app should parse every error the same way.*

Success:

```json
{ "id": 42, "title": "Buy milk", "createdAt": "2025-01-10T09:30:00Z" }
```

Error (one shape everywhere):

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Title is required",
    "fields": { "title": "must not be empty" }
  }
}
```

1. Use the right **status code** and a machine-readable **`code`**. The app uses `code`, and humans read `message`.
2. Never leak stack traces or SQL errors.
3. Same shape for every endpoint.

---

#### 3. Pagination: Offset vs Cursor — 🟢 Must Know

*Never return everything. Send a page, and let the app ask for the next one.*

**Offset** — "skip N, give me M":

```text
GET /notes?limit=20&offset=40
```

1. Simple, and easy to jump to page N.
2. Slow on big tables (the database still walks past all skipped rows).
3. If items are added or deleted while scrolling, you get **duplicates or gaps**.

**Cursor** — "give me the items after this one":

```text
GET /notes?limit=20&cursor=eyJpZCI6NDJ9
```

```json
{ "items": [ ... ], "nextCursor": "eyJpZCI6MjJ9" }
```

1. Fast and stable, even when data changes.
2. Can't jump to page 50.
3. `nextCursor` = null means no more data.

**Rule:** feeds and infinite scroll → **cursor**. Small admin tables → offset is fine.

---

#### 4. Filtering & Sorting — 🟢 Must Know

*Let the client narrow and order the list with query parameters.*

```text
GET /notes?status=active&sort=-createdAt&limit=20
```

1. Filter with query params (`status=active`).
2. Sort with `sort=createdAt` (ascending) or `sort=-createdAt` (descending).
3. Allow only **known fields**. Unknown fields are an error, or they open the door to abuse.
4. Always apply a **max page size**.

---

#### 5. Input Validation — 🟢 Must Know

*Never trust the client. Check everything on the server.*

1. Required fields, types, length, range, format (email, date).
2. Reject with `400` (or `422`) and say which field is wrong.
3. Accept only the fields you expect (a user must not be able to send `"role": "admin"`).
4. Validate path and query params too (`limit` must be 1–50).

---

#### 6. Idempotency — 🟢 Must Know

*Doing it twice has the same effect as doing it once.*

1. **GET, PUT, DELETE** are idempotent. **POST** is not: sending it twice can create two items.
2. Problem: the user double-taps "Pay", or the network times out and the app retries.
3. Fix: the app sends an **Idempotency-Key** (a unique ID per action).

```http
POST /payments
Idempotency-Key: 7c9e-4f2a-91b0
```

4. The server saves `key → result`. If the same key comes again, it returns the **saved result** and does not charge twice.

---

#### 7. Versioning & Backward Compatibility — 🟢 Must Know

*Old app versions stay installed for years. Your API must not break them.*

1. **Only add** things (new fields, new endpoints). Never remove, rename, or change the meaning of existing fields.
2. The app should **ignore unknown fields** it doesn't understand.
3. If you must break the contract, create a new version: `/v2/notes`. Keep `/v1` alive until old apps are gone.
4. Use a **force-update** screen for versions you can't support anymore.

---

#### 8. PUT vs PATCH — 🟡 Good to Know

*Two ways to update: replace everything, or change only some fields.*

1. **PUT** — replace the whole resource. Send all fields.
2. **PATCH** — change only some fields. Send only what changed.
3. Mobile apps mostly use PATCH to save bandwidth.

---

#### 9. Long-Running Work — 🟡 Good to Know

*If it takes long, don't keep the request open.*

```text
POST /reports          → 202 Accepted  { "jobId": "abc" }
GET  /reports/jobs/abc → { "status": "processing" } ... { "status": "done", "url": "..." }
```

The app polls the status endpoint, or receives a push notification when it is done.

---

#### 10. OpenAPI Docs — 🟡 Good to Know

*A machine-readable description of your API, so app and backend teams agree.*

1. **OpenAPI** (Swagger) is a file that describes all endpoints, inputs, outputs, and errors.
2. Used for docs, testing, and generating client code (Kotlin/Swift).

---

#### 11. REST vs GraphQL vs gRPC — 🟡 Good to Know

*Three API styles. REST is the default; know when the others fit.*

| | REST | GraphQL | gRPC |
|---|---|---|---|
| Idea | Resources + HTTP methods | Client asks for the exact fields it needs | Typed remote calls, binary format |
| Good for | Default choice, simple, cacheable | Complex screens, many clients | Service-to-service, low latency |
| Watch out | Over/under-fetching | More server complexity, caching is harder | Not browser-friendly, harder to debug |

---

#### 12. ETag & Conditional Requests — 🟡 Good to Know

*Ask the server "has this changed?" and skip downloading the same data again.*

1. Server sends `ETag: "v7"` with the data.
2. Next time the app sends `If-None-Match: "v7"`.
3. If the data has not changed, the server replies `304 Not Modified` with no body. This saves bandwidth and battery.

---

#### 13. Common Interview Questions

1. **Design the API for a notes app.**
   Endpoints (`/notes`, `/notes/{id}`), methods, status codes, cursor pagination, validation, one error format.
2. **Offset vs cursor pagination?**
   Offset is simple but slow and unstable when data changes. Cursor is fast and stable, and is best for feeds.
3. **What is idempotency? How do you make a POST idempotent?**
   Repeating gives the same effect. Use an Idempotency-Key that the server stores with the result.
4. **How do you change an API without breaking old apps?**
   Only add fields, never remove or rename. Use versions if needed. Force-update as a last step.
5. **PUT vs PATCH?**
   PUT replaces the whole resource. PATCH changes some fields.
6. **REST vs GraphQL?**
   REST is simple with fixed responses. GraphQL lets the client choose fields, but the server is more complex.

---

#### 14. Common Mistakes

1. Verbs in URLs (`/getNotes`).
2. Different error shapes in different endpoints.
3. Returning `200` with an error message inside.
4. No pagination, or no max page size.
5. Removing or renaming a field (old apps crash).
6. Changing data with GET.
7. Retrying POST without an idempotency key.

---

#### 15. Related Topics

1. `02` Networking & HTTP (methods, status codes)
2. `05` Authentication & Authorization
3. `06` Backend Security Essentials
4. `10` Indexes & Query Performance (cursor pagination speed)
5. Rate limiting, API gateway (system design roadmap)

---

#### 16. Interview Must Remember

1. **Nouns in the URL, action in the HTTP method.**
2. **One error format**, correct status codes.
3. Feeds → **cursor pagination**.
4. **Validate on the server**; never trust the client.
5. **Idempotency-Key** for safe retries of POST.
6. **Never break old app versions**: add only, version when needed.
