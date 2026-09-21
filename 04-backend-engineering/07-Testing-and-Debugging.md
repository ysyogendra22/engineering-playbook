# Testing & Debugging

Roadmap topic 7 · Stage 2: Build a Backend

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** tests prove the code works and keep it working. Debugging is a calm process: reproduce, find the cause, fix, and add a test.

---

#### 1. Types of Tests — 🟢 Must Know

*Like unit tests and UI tests in your app, but for the server.*

```text
        /  API tests  \      few, slower
       / Integration   \
      /   Unit tests    \    many, fast
```

| Type | Tests | Uses real DB / network? |
|---|---|---|
| Unit | One function or business rule | No |
| Integration | Code + real database | Yes (test database) |
| API | Full HTTP request → response | Yes (test server + database) |

---

#### 2. Unit Tests — 🟢 Must Know

*Fast tests for one piece of logic, with no database or network.*

1. Test **business rules** (for example, "a user can't book a seat that is taken").
2. Fast, no database, no network.
3. Test the normal case **and** edge cases (empty, null, limits, invalid).
4. Pattern: **Arrange** (set up) → **Act** (call) → **Assert** (check).

---

#### 3. Integration Tests — 🟢 Must Know

*Tests that check your code works together with a real database.*

1. Test that your code works with a **real database**: queries, constraints, transactions.
2. Use a separate test database (often a temporary container).
3. Reset data between tests so they don't affect each other.
4. Catches mistakes unit tests can't: wrong SQL, missing column, constraint errors.

---

#### 4. API Tests — 🟢 Must Know

*Send real requests and check the answers.*

Test each endpoint for:

| Case | Expected |
|---|---|
| Valid request | `200` / `201` + correct body |
| Invalid input | `400` + error format |
| No token | `401` |
| Other user's record | `403` / `404` |
| Not found | `404` |
| Duplicate | `409` |

The list above (especially permissions) is what interviewers like to hear.

---

#### 5. Good Test Habits — 🟢 Must Know

*Simple rules that keep tests useful instead of flaky.*

1. Tests are **independent**: they don't depend on order.
2. Tests are **repeatable**: same result every time (no random data, no real clock, no internet).
3. One clear reason to fail. Descriptive names (`rejects_booking_when_seat_taken`).
4. Test failure cases, not only success.

---

#### 6. Debugging Process — 🟢 Must Know

*A calm, repeatable way to find a bug instead of guessing.*

```text
1. Reproduce   → make it fail on demand
2. Read        → error message, stack trace, logs (with request ID)
3. Narrow      → which layer? controller / service / database
4. Inspect     → breakpoint or log the values
5. Fix         → smallest change
6. Prove       → write a failing test first, then see it pass
```

1. Logs show what happened. Breakpoints show why.
2. A bug fixed without a test can come back.
3. Check the simple causes first: wrong input, missing config, expired token.

---

#### 7. Mocking External Services — 🟡 Good to Know

*Fake the things you do not control, so tests are fast and repeatable.*

1. Replace things you don't control (payment API, email, SMS) with a fake or mock.
2. Don't mock everything. Too many mocks make tests pass while real code is broken.
3. Prefer a real database in integration tests.

---

#### 8. Load Testing & Profiling — 🟡 Good to Know

*See how the system behaves under many users before real users do.*

1. **Load test** — send many requests (tools: k6, JMeter) and watch p95 latency and errors.
2. **Profiler** — shows which code or query uses the most time.
3. **Measure first, then optimize.**

---

#### 9. Common Interview Questions

1. **What kinds of tests do you write for a backend?**
   Unit tests for business rules, integration tests with a real database, API tests for validation, permissions, and errors.
2. **What would you test for an endpoint?**
   Success, invalid input, missing token, other user's data, not found, duplicate.
3. **What do you mock?**
   Only external services like payments or email. Use a real database for integration tests.
4. **How do you debug a failing endpoint?**
   Reproduce, read logs by request ID, narrow to a layer, inspect with a breakpoint, fix, and add a test.
5. **What makes a test flaky?**
   Depends on time, randomness, order, or the network.

---

#### 10. Common Mistakes

1. Testing only the happy path.
2. Tests that depend on each other or on shared data.
3. Mocking the database and calling it an integration test.
4. Not testing permissions.
5. Fixing a bug without adding a test.
6. Tests that call real external services.

---

#### 11. Related Topics

1. `04` Backend Building Blocks (dependency injection makes tests easy)
2. `05` Authentication & Authorization
3. `09` Connecting API to Database
4. `11` Transactions & Concurrency
5. Observability (system design roadmap)

---

#### 12. Interview Must Remember

1. **Unit → Integration → API** tests.
2. Test **failures and permissions**, not only success.
3. Tests must be **independent and repeatable**.
4. Debug: **reproduce → logs → narrow → fix → add test**.
5. **Mock only external boundaries.**
