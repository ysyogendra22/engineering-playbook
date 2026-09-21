# Client, Server & Request Flow

Roadmap topic 1 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** the app asks, the backend does the work and answers. Interviews test whether you can explain this whole trip and what can go wrong on the way.

---

#### 1. Basic Terms — 🟢 Must Know

*Think of a restaurant: the app is the customer, the API is the menu, the backend is the kitchen, and the database is the pantry.*

1. **Client** — the app that sends requests. Your Android, iOS, or web app.
2. **Server** — a computer that receives requests, does the work, and sends back a response.
3. **Backend** — all the code that runs on the server side: APIs, business rules, login, data access.
4. **API** — the list of requests the backend accepts (for example, `GET /posts`). It is the contract between the app and the backend.
5. **Database** — where the backend stores data permanently (users, posts, orders).

```text
Mobile App  →  API  →  Backend Logic  →  Database
(client)                 (server)
```

**Mobile view:** your app is the client. Everything behind the API URL is "the backend".

---

#### 2. Why Client–Server Is Used — 🟢 Must Know

*One shared backend keeps rules and data in one place, so every app behaves the same way.*

1. One backend can serve Android, iOS, and web.
2. Business rules and data live in **one place**, not copied into every app.
3. You can update the backend without waiting for users to update the app.
4. Apps and backend can **scale separately**.

```text
Android ─┐
iOS ─────┼──→ Backend → Database
Web ─────┘
```

---

#### 3. What Happens When the App Calls an API — 🟢 Must Know

*Every screen that loads data makes the same trip: app → network → server → data → back to the app.*

```text
User taps / opens screen
        ↓
App builds an HTTPS request
        ↓
Network (DNS → connection → TLS)      ← details in topic 02
        ↓
Server receives the request
        ↓
Check identity (authentication)
        ↓
Validate input
        ↓
Business logic
        ↓
Read / write database (or cache)
        ↓
Build response (status code + JSON)
        ↓
App receives response
        ↓
App parses data and updates UI
```

Short version to remember:
**Request → Validate → Logic → Data → Response → UI**

---

#### 4. Example: Load a Feed of Posts — 🟢 Must Know

*Use this example in interviews. It shows the whole flow on one simple screen.*

Request:

```http
GET /posts?limit=20
Authorization: Bearer <token>
```

Server steps:

```text
1. Read the token → find the user
2. Validate limit (for example, max 50)
3. Check cache for this user's feed
4. Cache miss → query the database
5. Build the JSON
6. Return 200 OK
```

Response:

```json
{
  "posts": [
    { "id": 1, "title": "Hello", "author": "Asha" },
    { "id": 2, "title": "System Design", "author": "Ravi" }
  ]
}
```

App side:

```text
Show loading → send request → success: show list
                            → error: show retry / cached data
```

---

#### 5. Why the App Must Not Talk to the Database Directly — 🟢 Must Know

*The API is a guard at the door: it checks who you are and what you may see before touching any data.*

1. **Security** — a database password inside the app can be extracted by anyone who decompiles it.
2. **No rules** — the database can't check login, permissions, or validation for each user.
3. **Every phone connects** — thousands of devices opening database connections will overload it.
4. **Hard to change** — if the app knows the table structure, you can't change the database without breaking old app versions.
5. **No control** — you can't add rate limiting, logging, or caching.

**Remember:** the API is the only door to the data. The database is never exposed to the internet.

🟡 **Good to know: Firebase / Supabase.** These tools look like the app talks to the database directly. In reality a managed API sits in front, and **security rules** (Firebase rules, Supabase row-level security) decide who can read or write each row. The app never gets raw database credentials. If the rules are wrong, data leaks, so the idea "the server must check everything" still applies.

---

#### 6. Network Failures & Latency — 🟢 Must Know

*The network is the weakest link. Plan for failure, not only for success.*

A network call can fail in many ways:

1. No internet or a weak connection.
2. Timeout (no answer in time).
3. Server down or overloaded (`5xx`).
4. Login expired (`401`).
5. Too many requests (`429`).

Response time is a sum:

```text
Network time  +  Server processing  +  Database / cache time
```

What the app should do:

1. Always set a **timeout**.
2. Show a clear error state and a retry option.
3. Show cached data if you have it.
4. Retry only when it is safe (reading data is safe; repeating a payment is not — see Idempotency in topic 03).

**Remember:** mobile networks are slower and less stable than Wi-Fi. Never assume a request succeeds.

---

#### 7. Stateless Requests — 🟢 Must Know

*The server treats every request as new, like meeting a stranger each time. The token proves who you are.*

1. **Stateless** means the server does not remember your previous request.
2. Each request carries everything needed to handle it, mainly the **token**.
3. Data is still saved, but in the **database**, not in the server's memory.

```text
Request 1 (token) → Server A
Request 2 (token) → Server B    ← works, because the token comes with the request
```

Why it matters:

1. Any server can handle any request.
2. Easy to add more servers (scaling).
3. If one server dies, the next request goes to another one.

---

#### 8. Synchronous vs Background Work — 🟢 Must Know

*Do the must-have work now, reply to the user, and finish the rest later.*

1. **Synchronous** — the user waits for it. Do only what is needed for the response.
2. **Background** — slow work done after the response is sent.

Example: user publishes a post.

```text
Synchronous:   validate → save post → return 201 Created
Background:    notify followers, resize image, update search, send email
```

Why:

1. The user gets a fast response.
2. A slow email service can't make the app hang.
3. Background work can be retried if it fails.

**Mobile view:** same idea as not blocking the main thread. Don't block the request on slow work.

(Queues and workers are covered later in the system design roadmap.)

---

#### 9. Client vs Server Responsibilities — 🟢 Must Know

*Client = user experience. Server = rules and security.*

| Client (app) | Server (backend) |
|---|---|
| Show UI | Validate every request |
| Collect input | Check login and permissions |
| Basic input checks (for a better experience) | Business rules |
| Send requests, handle errors | Read/write database |
| Keep screen state, cache | Send responses |

**Golden rule:** never trust the client. Checks in the app are for user experience. Checks on the server are for security.

---

#### 10. Common Interview Questions

1. **What happens when a mobile app calls an API?**
   App sends an HTTPS request → server checks who you are → validates input → runs business logic → reads/writes the database → returns a status code and JSON → app updates the UI.
2. **Why shouldn't the app connect to the database directly?**
   Security, no permission checks, too many connections, and it couples the app to the schema.
3. **What does stateless mean?**
   The server keeps no per-user memory between requests. Each request carries a token. This makes scaling easy.
4. **What can go wrong with a network call, and how do you handle it?**
   Offline, timeout, `5xx`, `401`, `429`. Use timeouts, error states, retry when safe, and cached data.
5. **What should be done synchronously and what in the background?**
   Only what the response needs is synchronous. Notifications, emails, and image processing go to the background.
6. **Trace loading a list of posts from app to database and back.** (Section 4.)
7. **Firebase/Supabase apps seem to talk to the database directly. Is that the same thing?**
   No. A managed API with security rules (or row-level security) sits in front of the database. The app has no raw database access, and the rules do the job of the permission checks.

---

#### 11. Common Mistakes

1. Thinking the app reads the database directly.
2. Assuming every request succeeds.
3. Trusting checks done only in the app.
4. Putting secrets (API keys, database passwords) inside the app.
5. Making the user wait for slow work (emails, notifications).
6. Confusing "stateless" with "no data is stored".

---

#### 12. Related Topics

1. `02` Networking & HTTP
2. `03` API Design
3. `05` Authentication & Authorization
4. `09` Connecting API to Database
5. Caching, queues, load balancer (system design roadmap)

---

#### 13. Interview Must Remember

1. **Client sends requests; server processes and responds.**
2. Full flow: **App → API → Auth → Validate → Logic → Cache/DB → Response → UI**.
3. The app never gets **raw database access**. An API (or a managed layer with rules) always sits in front.
4. Networks are slow and unreliable: **timeouts, error states, retries**.
5. **Stateless:** each request carries its own identity (token).
6. Keep the request fast; move slow work to the **background**.
7. **Never trust the client.**
