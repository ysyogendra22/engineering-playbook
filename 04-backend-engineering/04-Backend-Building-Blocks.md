# Backend Building Blocks

Roadmap topic 4 · Stage 2: Build a Backend

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** the parts every backend project has: a language and framework, layers, middleware, config, error handling, and a way to handle many requests at once.

---

#### 1. One Language, One Framework — 🟢 Must Know

*Interviewers test concepts, not the framework. Pick one and go deep.*

1. Use **one** language and **one** framework. Don't learn several.
2. Prefer a language you already know.
3. Examples: Kotlin → Ktor or Spring Boot · Swift → Vapor · JavaScript/TypeScript → Node + Express/NestJS · Python → FastAPI.
4. A framework gives you: routing, request parsing, middleware, and error handling.

---

#### 2. Layers: Controller → Service → Repository — 🟢 Must Know

*Same idea as View → ViewModel → Repository in your app.*

```text
HTTP Request
    ↓
Controller / Route   → read request, call service, return response
    ↓
Service              → business rules
    ↓
Repository           → database access only
    ↓
Database
```

| Layer | Does | Must not |
|---|---|---|
| Controller | Parse input, call service, choose status code | Contain business rules or SQL |
| Service | Business rules, decisions | Know about HTTP |
| Repository | Read/write the database | Contain business rules |

Why: easy to test, easy to change, easy to read.

---

#### 3. Middleware — 🟢 Must Know

*Code that runs on every request before or after your handler. Like OkHttp interceptors.*

```text
Request → [Logging] → [Auth] → [Rate limit] → Handler → Response
```

1. Common uses: logging, authentication, rate limiting, error handling, request IDs.
2. **Order matters.** For example, run auth before the handler.
3. Keeps repeated code out of every handler.

---

#### 4. Config, Environment Variables, Secrets — 🟢 Must Know

*Same code, different settings for dev, test, and production.*

1. Put settings (database URL, API keys, ports) in **environment variables**.
2. Keep a `.env` file for local development and **never commit it to Git**.
3. In production, use a **secrets manager** or the platform's secret settings.
4. If a secret leaks, **rotate it** (create a new one).

---

#### 5. Central Error Handling — 🟢 Must Know

*One place turns errors into responses.*

```text
Service throws: NotFoundError
Error handler maps: → 404 + standard error JSON
Unknown error:      → log the details, return a safe 500
```

1. Code throws meaningful errors (`NotFound`, `Validation`, `Conflict`).
2. One handler converts them to status codes and the standard error format.
3. **Log** the details. **Send** a safe message to the client.

---

#### 6. Blocking vs Non-Blocking — 🟢 Must Know

*Same idea as not blocking the main thread in your app.*

1. **Blocking** — the thread waits (for the database, another API, a file). It can't do other work meanwhile.
2. A server has a limited number of threads. If they all wait on slow calls, **new requests wait too**.
3. **Non-blocking / async** — the thread is released while waiting and resumes when the answer comes.
4. Long work (reports, video) should go to a **background job**, not run inside the request.

---

#### 7. Threads, Thread Pools, Async / Coroutines — 🟢 Must Know

*How does one server handle many requests at once?*

| Model | How it works | Examples |
|---|---|---|
| Thread per request | Each request uses a thread from a pool | Spring MVC, Tomcat |
| Event loop | One thread handles many requests using async I/O | Node.js |
| Coroutines | Lightweight tasks on a few threads | Kotlin (Ktor, Spring WebFlux) |

1. Know which model **your** framework uses.
2. Use a **bounded thread pool**. Unlimited threads crash the server.
3. Don't block an event-loop or coroutine thread with slow, blocking calls.
4. Database connections are also limited (see topic `09`).

---

#### 8. Logging Basics — 🟢 Must Know

*Logs are how you see what happened on a server you can't debug live.*

1. Levels: `DEBUG` (detail), `INFO` (normal events), `WARN` (odd), `ERROR` (failure).
2. Log each request with a **request ID** so you can follow one request.
3. **Never** log passwords, tokens, or personal data.
4. Log errors with their cause (stack trace) on the server only.

---

#### 9. Terminal, Git, curl, Local Debugging — 🟢 Must Know

*Everyday tools of a backend engineer. Know the basics.*

1. **Terminal:** `cd`, `ls`, `cat`, `grep`, `ps`, `kill`, file permissions.
2. **Git:** branch, commit, pull request, resolve conflicts.
3. **Call your API without the app:**

```bash
curl -X POST http://localhost:8080/notes \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title":"Buy milk"}'
```

4. Run the server locally, set breakpoints, read logs, stop it cleanly.
5. Use Postman or similar for saved requests.

---

#### 10. Dependency Injection — 🟡 Good to Know

*Give a class what it needs instead of letting it create things itself. Same idea as Hilt or Koin.*

1. A class receives what it needs (repository, clients) from outside instead of creating them itself.
2. Makes testing easy: give it a fake repository.
3. Same idea as Hilt/Koin (Android) or protocol-based injection (iOS).

---

#### 11. Memory, Garbage Collection, Thread Safety — 🟡 Good to Know

*Many requests run at the same time in one server, so shared data needs care.*

1. Shared **mutable** data used by many requests causes race conditions. Prefer stateless services and immutable data.
2. If you must share state, protect it (locks, concurrent collections).
3. Memory leaks (things you keep forever) slowly crash the server.
4. Garbage collection can cause short pauses. Know it exists.

---

#### 12. Serialization, Null Handling, Date/Time — 🟡 Good to Know

*Small details that cause real bugs: JSON conversion, null values, and dates.*

1. **Serialization** — turning objects into JSON and back.
2. Decide how to treat **missing vs null** fields.
3. Send dates in **ISO 8601, UTC**: `2025-01-10T09:30:00Z`. The app converts to local time.

---

#### 13. Timeouts, Cancellation, Cleanup — 🟡 Good to Know

*Never wait forever. Stop work nobody is waiting for, and clean up.*

1. Set a **timeout** on every call to another service or database.
2. If the client disconnects, stop the work if you can.
3. Always close connections, files, and streams (use `try/finally` or the language's equivalent).

---

#### 14. Common Interview Questions

1. **How do you structure a backend project?**
   Controller → Service → Repository. Controllers handle HTTP, services hold business rules, repositories talk to the database.
2. **What is middleware?**
   Code that runs around every request: logging, auth, rate limiting. Like interceptors in OkHttp.
3. **Where do you keep secrets and config?**
   Environment variables or a secrets manager. Never in Git or in the app.
4. **Blocking vs non-blocking?**
   Blocking holds the thread while waiting. Non-blocking frees it. Blocking calls in a limited thread pool make the server slow.
5. **How does your framework handle many requests?**
   Explain your model: thread pool, event loop, or coroutines.
6. **How do you handle errors?**
   Throw meaningful errors, one central handler maps them to status codes, log details, return a safe message.

---

#### 15. Common Mistakes

1. Business logic inside controllers.
2. SQL inside controllers.
3. Secrets committed to Git.
4. Blocking calls on a non-blocking thread.
5. Unlimited threads or connections.
6. Returning raw exceptions to the client.
7. Logging sensitive data.

---

#### 16. Related Topics

1. `01` Client, Server & Request Flow
2. `03` API Design
3. `07` Testing & Debugging
4. `09` Connecting API to Database
5. Background jobs, observability (system design roadmap)

---

#### 17. Interview Must Remember

1. **Controller → Service → Repository.**
2. **Middleware** runs on every request; order matters.
3. **Config and secrets** in environment variables, never in Git.
4. **One central error handler.**
5. Don't **block** worker threads; use pools with limits.
6. Know your runtime's **concurrency model**.
