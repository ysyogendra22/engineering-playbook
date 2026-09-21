# Backend Security Essentials

Roadmap topic 6 · Stage 2: Build a Backend

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** assume every request may be hostile. Check all input, never build SQL from user text, protect secrets, and don't leak information.

---

#### 1. Input Validation & Size Limits — 🟢 Must Know

*Never trust anything that comes from outside.*

1. Validate type, length, range, and format on the server.
2. Set a **maximum request body size** and a **maximum page size**.
3. Set **upload limits** (size and file type).
4. Accept only the fields you expect. A user must not be able to send `"role": "admin"` or `"isPaid": true` (called mass assignment).

---

#### 2. SQL Injection — 🟢 Must Know

*Never glue user text into a SQL string.*

Bad:

```text
query = "SELECT * FROM users WHERE email = '" + email + "'"
email = ' OR '1'='1     → returns every user
```

Good: **parameterized query**. The database treats the value as data, not as SQL.

```sql
SELECT * FROM users WHERE email = $1;   -- value passed separately
```

1. Always use parameters or a safe ORM method.
2. ORMs are safe by default, but **raw queries** built with string concatenation are not.

---

#### 3. HTTPS & Secret Handling — 🟢 Must Know

1. HTTPS everywhere. Never send tokens over plain HTTP.
2. Secrets (database password, API keys) go in **environment variables or a secrets manager**, not in code or Git.
3. Never put secrets inside the mobile app. Anyone can extract them.
4. Rotate a secret if it leaks.

---

#### 4. No Sensitive Data in Logs or Errors — 🟢 Must Know

1. Never log passwords, tokens, full card numbers, or personal data.
2. Don't send stack traces or SQL errors to the client. Return a safe message and log the details on the server.
3. Login errors should be generic: say "Invalid email or password", not "No such user".

---

#### 5. Login Rate Limiting — 🟢 Must Know

*Stop attackers from trying thousands of passwords.*

1. Limit login attempts per account and per IP.
2. Slow down or temporarily lock after repeated failures.
3. Return `429 Too Many Requests`.
4. Also limit expensive endpoints (password reset, OTP, search).

---

#### 6. CORS, CSRF, XSS — 🟡 Good to Know

*These are mostly web-browser problems.*

1. **CORS** — a browser rule about which websites may call your API. It is **not authentication**. Mobile apps ignore it.
2. **CSRF** — a malicious site makes the browser send your cookies to your API. Affects cookie-based logins. Apps using a Bearer token in a header are not affected by it.
3. **XSS** — an attacker injects a script into a web page. Fix: escape output.

---

#### 7. SSRF — 🟡 Good to Know

1. Server-side request forgery: your server fetches a URL that a user gave you (for example, "import image from URL").
2. An attacker gives an internal address (`http://localhost/admin`) and your server fetches it.
3. Fix: allow only expected hosts, block internal addresses, set timeouts.

---

#### 8. Encryption at Rest & Privacy — 🟡 Good to Know

1. **In transit** = HTTPS. **At rest** = encrypted disks and backups.
2. Collect only the personal data you need. Protect it and allow deletion on request.
3. Mask sensitive data in the app and in logs.

---

#### 9. OWASP API Top 10 — 🟡 Good to Know

Know the names of the top risks. The first ones show up most:

1. **Broken object-level authorization** — missing ownership checks (topic `05`).
2. **Broken authentication** — weak login, token, or password handling.
3. **Unrestricted resource consumption** — no rate limits or size limits.
4. **Broken function-level authorization** — normal users calling admin endpoints.
5. **Security misconfiguration** — debug mode on, open ports, default passwords.

Also: keep dependencies updated to receive security fixes.

---

#### 10. Common Interview Questions

1. **How do you prevent SQL injection?**
   Parameterized queries. Never concatenate user input into SQL.
2. **What are common API security mistakes?**
   Missing ownership checks, no input validation, secrets in code, no rate limiting, leaking errors and logs.
3. **Is CORS a security feature for APIs?**
   It only controls browsers. It does not replace authentication.
4. **What is SSRF?**
   Tricking the server into calling an internal or unwanted URL. Fix with an allow list and blocking internal addresses.
5. **How do you protect a login endpoint?**
   Rate limit, generic error message, hashed passwords, optional MFA.
6. **Where should secrets live?**
   Environment variables or a secrets manager. Never in Git or the app.

---

#### 11. Common Mistakes

1. Building SQL from strings.
2. No ownership checks.
3. Trusting the client's input and fields.
4. Secrets in Git or inside the app.
5. Detailed error messages sent to the client.
6. No rate limit on login.
7. Logging tokens or passwords.

---

#### 12. Related Topics

1. `03` API Design (validation)
2. `05` Authentication & Authorization
3. `08` Databases, SQL & Data Modeling
4. `09` Connecting API to Database
5. Rate limiting, secrets management (system design roadmap)

---

#### 13. Interview Must Remember

1. **Validate all input**; limit sizes.
2. **Parameterized queries** stop SQL injection.
3. **HTTPS + secrets outside code.**
4. **No sensitive data** in logs or errors.
5. **Rate limit** login and expensive endpoints.
6. **CORS is not authentication.**
