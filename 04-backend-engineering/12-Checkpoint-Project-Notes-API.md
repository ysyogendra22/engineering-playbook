# Checkpoint Project: Notes API

Roadmap topic 12 · Stage 3: Data

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** build a small, real backend with everything from topics 1–11. If you can build it and explain it without looking at the code, you are ready for the system design topics.

---

#### 1. Goal — 🟢 Must Know

1. One server, one SQL database, one mobile app.
2. Users register and log in, and manage **only their own** notes.
3. Finish it, don't just start it. A small finished project beats many half-done ones.

---

#### 2. API — 🟢 Must Know

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Is the server alive? |
| POST | `/auth/register` | Create an account |
| POST | `/auth/login` | Get a token |
| POST | `/notes` | Create a note |
| GET | `/notes?limit=20&cursor=...` | List my notes (paginated) |
| GET | `/notes/{id}` | Get one note |
| PATCH | `/notes/{id}` | Update a note |
| DELETE | `/notes/{id}` | Delete a note |

---

#### 3. Data Model — 🟢 Must Know

```sql
CREATE TABLE users (
  id            BIGSERIAL PRIMARY KEY,
  email         TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE notes (
  id         BIGSERIAL PRIMARY KEY,
  user_id    BIGINT NOT NULL REFERENCES users(id),
  title      TEXT NOT NULL,
  body       TEXT NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_notes_user_created ON notes (user_id, created_at DESC, id DESC);
```

---

#### 4. Build Steps (in order) — 🟢 Must Know

1. **Health endpoint** and project structure (controller / service / repository).
2. **In-memory notes API** (a list in memory). Get the routes working.
3. **Validation and one error format** (topic `03`).
4. **Add the SQL database**, migrations, and a connection pool (topics `08`, `09`).
5. **Cursor pagination** for `GET /notes`.
6. **Register and login**: hashed passwords and tokens (topic `05`).
7. **Ownership checks**: a user can only touch their own notes.
8. **Tests**: unit, integration, and API tests (topic `07`).
9. **One basic deployment.** Any simple platform is fine. (Deployment details come in the system design roadmap.)
10. **Connect a mobile app**, with timeouts, loading, error, and empty states.

---

#### 5. Definition of Done — 🟢 Must Know

- [ ] All endpoints work with correct status codes.
- [ ] Invalid input returns `400` with the standard error shape.
- [ ] No token → `401`. Someone else's note → `404`/`403`.
- [ ] Passwords are hashed. Secrets are in environment variables.
- [ ] List uses cursor pagination with a max page size.
- [ ] Index exists for the list query. `EXPLAIN` checked.
- [ ] Tests cover success, validation, and permissions.
- [ ] Deployed once, and the mobile app talks to it.
- [ ] You can explain the whole flow **without looking at the code**.

---

#### 6. Explain It Without Code — 🟢 Must Know

Practise saying this in 2 minutes:

```text
1. App sends GET /notes over HTTPS with a Bearer token.
2. Middleware checks the token and finds the user.
3. Controller validates limit and cursor and calls the service.
4. Service asks the repository for this user's notes.
5. Repository runs a parameterized SQL query using the composite index.
6. Result is turned into JSON with a nextCursor.
7. App shows the list, or shows an error/retry state.
```

Then add: what happens if the token expired, the database is slow, or the user asks for someone else's note.

---

#### 7. Stretch Goals — 🟡 Good to Know

1. Refresh tokens and logout.
2. Rate limiting on login.
3. Search notes by title.
4. Optimistic locking on note updates (`version` column).
5. OpenAPI documentation.
6. Docker image and a CI pipeline that runs the tests.

---

#### 8. Common Interview Questions

1. **Walk me through a project you built.**
   Use section 6, and be ready for follow-ups.
2. **How did you handle authentication and permissions?**
   Hashed passwords, access token, ownership check on every record.
3. **How is pagination done? Why that choice?**
   Cursor pagination on `(created_at, id)` for stable, fast pages.
4. **How would this design change with 1 million users?**
   Cache, read replicas, a load balancer with stateless servers. (Covered in the system design roadmap.)
5. **What would you test?**
   Success, validation, unauthorized, another user's note, not found.

---

#### 9. Common Mistakes

1. Starting the mobile app before the API is stable.
2. Skipping ownership checks and tests.
3. Committing secrets.
4. Adding features before finishing the basics.
5. Using an ORM without knowing the SQL it generates.
6. Not deploying it once.

---

#### 10. Related Topics

1. `01`–`11` (this project uses all of them)
2. Scaling, caching, deployment (system design roadmap)

---

#### 11. Interview Must Remember

1. **One server + one SQL database + auth + tests.**
2. **Layers, validation, one error format, cursor pagination.**
3. **Hashed passwords, tokens, ownership checks.**
4. **Explain the full flow without code.**
5. Finish and deploy it once.
