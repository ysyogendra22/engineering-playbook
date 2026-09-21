# Backend Engineering: Interview Roadmap

For a mobile engineer preparing for backend and system design interviews.
This is **part 1 (topics 1–12)**: build a working backend. Continue with **part 2 (topics 13–33)** in `05-system-design`. Each topic gets its own doc later.

**Marks:**

| Mark | Meaning |
|---|---|
| 🟢 | **Must have.** Expected in most interviews. Learn first. |
| 🟡 | **Good to have.** Learn after the 🟢 items are solid. |
| (New) | Added beyond the original two roadmaps. |

---

## Index

| #   | Topic                          | Stage              |
| --- | ------------------------------ | ------------------ |
| 1   | Client, Server & Request Flow  | 1. Foundations     |
| 2   | Networking & HTTP              | 1. Foundations     |
| 3   | API Design                     | 1. Foundations     |
| 4   | Backend Building Blocks        | 2. Build a Backend |
| 5   | Authentication & Authorization | 2. Build a Backend |
| 6   | Backend Security Essentials    | 2. Build a Backend |
| 7   | Testing & Debugging            | 2. Build a Backend |
| 8   | Databases, SQL & Data Modeling | 3. Data            |
| 9   | Connecting API to Database     | 3. Data            |
| 10  | Indexes & Query Performance    | 3. Data            |
| 11  | Transactions & Concurrency     | 3. Data            |
| 12  | Checkpoint Project: Notes API  | 3. Data            |

**Short on time (2 weeks):** topics 1, 2, 3, 4, 5, 8, 10, 11. 🟢 items only. Then follow the short list in `05-system-design`.

---

# Stage 1: Foundations

## 1. Client, Server & Request Flow

- 🟢 Client, server, backend, API, database
- 🟢 How a mobile app calls a backend
- 🟢 Request → response lifecycle
- 🟢 Trace one example: load a feed of posts
- 🟢 Why the app never talks to the database directly
- 🟢 Network failures and latency
- 🟢 Stateless requests
- 🟢 Synchronous vs background work

## 2. Networking & HTTP

- 🟢 IP, domain, port, DNS
- 🟢 TCP vs UDP
- 🟢 HTTP vs HTTPS (TLS)
- 🟢 Request: method, headers, body
- 🟢 Response: status codes (2xx, 4xx, 5xx, 401 vs 403)
- 🟢 Timeouts and connection reuse
- 🟡 HTTP/2 and HTTP/3
- 🟡 Cookies, content types, compression
- 🟡 Reverse proxy

## 3. API Design

- 🟢 REST, endpoints, JSON
- 🟢 Consistent responses and error format
- 🟢 Pagination: offset vs cursor
- 🟢 Filtering and sorting
- 🟢 Input validation
- 🟢 Idempotency
- 🟢 Versioning and backward compatibility
- 🟡 PUT vs PATCH
- 🟡 Long-running work: 202 Accepted + status endpoint
- 🟡 OpenAPI docs
- 🟡 REST vs GraphQL vs gRPC
- 🟡 ETag and conditional requests

---

# Stage 2: Build a Backend

## 4. Backend Building Blocks

- 🟢 Pick one language and one framework
- 🟢 Layers: controller → service → repository
- 🟢 Middleware
- 🟢 Config, environment variables, secrets
- 🟢 Central error handling
- 🟢 Blocking vs non-blocking work
- 🟢 Threads, thread pools, async / coroutines
- 🟢 Logging basics
- 🟢 Terminal, Git, curl/Postman, local debugging
- 🟡 Dependency injection
- 🟡 Memory, garbage collection, thread safety
- 🟡 Serialization, null handling, date/time
- 🟡 Timeouts, cancellation, resource cleanup

## 5. Authentication & Authorization

- 🟢 Authentication vs authorization
- 🟢 Password hashing
- 🟢 Sessions vs tokens (JWT)
- 🟢 Access token + refresh token, expiry, logout
- 🟢 Ownership checks on every record
- 🟢 Roles and permissions
- 🟢 Secure token storage on mobile (Keychain / Keystore)
- 🟡 OAuth 2.0, OpenID Connect, PKCE
- 🟡 JWT pitfalls, MFA, API keys

## 6. Backend Security Essentials

- 🟢 Input validation and size limits
- 🟢 SQL injection and parameterized queries
- 🟢 HTTPS and secret handling
- 🟢 No sensitive data in logs or errors
- 🟢 Login rate limiting
- 🟡 CORS, CSRF, XSS
- 🟡 SSRF
- 🟡 Encryption at rest, personal data privacy
- 🟡 OWASP API Top 10

## 7. Testing & Debugging

- 🟢 Unit, integration, and API tests
- 🟢 Debug with logs, breakpoints, failing tests
- 🟡 Mocking external services
- 🟡 Load testing and profiling

---

# Stage 3: Data

## 8. Databases, SQL & Data Modeling

- 🟢 Tables, rows, columns, primary and foreign keys
- 🟢 Constraints
- 🟢 CRUD, joins, group by, NULL
- 🟢 1-1, 1-many, many-many relationships
- 🟢 Design the schema from the queries
- 🟢 Normalization vs denormalization
- 🟢 Money and time zones
- 🟡 Subqueries, CTEs, window functions (basic)
- 🟡 Schema migrations
- 🟡 Soft delete

## 9. Connecting API to Database

- 🟢 Connection pool
- 🟢 ORM basics
- 🟢 N+1 query problem
- 🟢 Handle not found and constraint errors
- 🟡 Connection limits with many servers

## 10. Indexes & Query Performance

- 🟢 What an index is; read benefit vs write cost
- 🟢 Composite indexes
- 🟢 EXPLAIN and query plans
- 🟢 Common causes of slow queries
- 🟡 Covering index
- 🟡 Measure before optimizing

## 11. Transactions & Concurrency

- 🟢 ACID
- 🟢 Commit and rollback
- 🟢 Race conditions (double booking, negative stock)
- 🟢 Atomic updates and unique constraints
- 🟢 Optimistic vs pessimistic locking
- 🟡 Isolation levels and anomalies
- 🟡 Deadlocks and retries

## 12. Checkpoint Project: Notes API

- 🟢 CRUD APIs with one server and one SQL database
- 🟢 Validation, errors, pagination
- 🟢 Login and ownership checks
- 🟢 Tests and one basic deployment (details in topic 28)
- 🟢 Connect a mobile app
- 🟢 Explain the full flow without looking at code

---

## Skip for Now

- Custom auth protocols or crypto
- Learning several languages or frameworks at once
- Cloud certifications

## How to Proceed

1. One language, one framework, one SQL database.
2. Finish the Notes API (topic 12) before the distributed-systems topics in `05-system-design`.
3. For each topic: what it is, what problem it solves, how it works, one downside.
