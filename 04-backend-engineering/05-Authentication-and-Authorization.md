# Authentication & Authorization

Roadmap topic 5 · Stage 2: Build a Backend

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** authentication proves who you are. Authorization decides what you can do. Both must be checked on the server for every request.

---

#### 1. Authentication vs Authorization — 🟢 Must Know

*At the airport: your passport check is authentication. Your boarding pass deciding which gate you may enter is authorization.*

| | Authentication (AuthN) | Authorization (AuthZ) |
|---|---|---|
| Question | Who are you? | What are you allowed to do? |
| Example | Login with email + password | Can this user delete this note? |
| Failure code | `401 Unauthorized` | `403 Forbidden` |

```text
Request → AuthN (who?) → AuthZ (allowed?) → Handler
```

---

#### 2. Password Hashing — 🟢 Must Know

*Store a fingerprint of the password, never the password.*

1. **Never** store plain-text passwords.
2. A **hash** is one-way: you can't get the password back from it.
3. Use a slow, password-specific algorithm: **bcrypt, argon2, or scrypt**. Not plain SHA-256.
4. A **salt** (random value per password) makes identical passwords produce different hashes. The library does this for you.
5. Login: hash the typed password and compare it to the stored hash.
6. Hashing is not encryption. Encryption can be reversed; hashing can't.

Use a trusted library. Never write your own.

---

#### 3. Sessions vs Tokens (JWT) — 🟢 Must Know

*After login, the client must prove who it is on every request without sending the password again.*

| | Session | Token (JWT) |
|---|---|---|
| Where is the state? | Server stores it (session ID → user) | Inside the signed token |
| Client sends | Session ID (usually a cookie) | `Authorization: Bearer <token>` |
| Revoke | Easy: delete the session | Hard until it expires |
| Scaling | Needs a shared session store | Stateless: any server can verify |
| Common in | Web apps | Mobile apps and APIs |

**JWT** = three parts: `header.payload.signature`. The server checks the **signature** and the **expiry**. The payload is only encoded, **not secret**.

---

#### 4. Access Token + Refresh Token — 🟢 Must Know

*A short-lived key for daily use, and a long-lived key only for getting new short-lived keys.*

1. **Access token** — short life (for example, 15 minutes). Sent with every API call.
2. **Refresh token** — long life (days or weeks). Used only to get a new access token.
3. Why: if an access token leaks, it stops working soon.

```text
Login → access + refresh tokens
API call with access token → 200
Access token expired → 401
App sends refresh token → new access token → retry the call
Refresh token expired → user logs in again
```

4. **Logout:** delete tokens on the device **and** revoke the refresh token on the server.

**Mobile tip:** when several calls fail with 401 at once, refresh **only once** and let the others wait, then retry them.

---

#### 5. Ownership Checks on Every Record — 🟢 Must Know

*Logged in is not enough. Does this record belong to you?*

```text
GET /notes/99
→ find note 99
→ note.userId == currentUser.id ?  yes → return  |  no → 404 / 403
```

1. Take the user from the **token**, never from a request field like `userId`.
2. Check ownership on **read, update, and delete**.
3. Missing this check is the most common real API bug (IDOR / BOLA): a user changes `99` to `100` and reads someone else's data.
4. Returning `404` for "not yours" avoids revealing that the record exists.

---

#### 6. Roles and Permissions — 🟢 Must Know

1. **Role-based access control (RBAC):** users have roles (`user`, `admin`), and roles have permissions.
2. Check permissions on the server for each action, not only by hiding a button in the app.
3. Give the **least** access needed.

---

#### 7. Secure Token Storage on Mobile — 🟢 Must Know

*The token is the key to the account. Store it safely.*

1. **iOS:** Keychain.
2. **Android:** Keystore-backed encrypted storage.
3. **Not** plain `SharedPreferences` or `UserDefaults`.
4. Never log tokens. Never put them in URLs.
5. Clear tokens on logout.

---

#### 8. OAuth 2.0, OpenID Connect, PKCE — 🟡 Good to Know

1. **OAuth 2.0** — lets an app get limited access to your data at another service without your password ("allow this app to read my calendar").
2. **OpenID Connect (OIDC)** — adds **login** (identity) on top of OAuth. This is "Sign in with Google/Apple".
3. **PKCE** — extra protection for mobile apps, which can't keep a client secret safe. Always use it for OAuth in apps.
4. Use a trusted library or provider. Don't build this yourself.

---

#### 9. JWT Pitfalls, MFA, API Keys — 🟡 Good to Know

1. **JWT pitfalls:** hard to revoke before expiry; don't put secrets in the payload; always verify signature, expiry, and algorithm.
2. **MFA** — a second proof (code, authenticator app). Protects against stolen passwords.
3. **API keys** — identify an **app or service**, not a user. Keep them secret and rotate them.

---

#### 10. Common Interview Questions

1. **AuthN vs AuthZ?**
   AuthN = who you are (401). AuthZ = what you may do (403).
2. **How do you store passwords?**
   Hash with bcrypt or argon2 and a salt. Never plain text.
3. **Session vs JWT?**
   Session keeps state on the server and is easy to revoke. JWT keeps state in the token, so it is stateless and scales easily but is harder to revoke.
4. **How do access and refresh tokens work?**
   Short access token for calls, long refresh token to get new ones. On 401, refresh once and retry.
5. **How do you stop user A from reading user B's note?**
   Get the user from the token and check ownership of the record on every request.
6. **Where does a mobile app store tokens?**
   Keychain (iOS) or Keystore-backed storage (Android).
7. **OAuth vs OIDC?**
   OAuth = delegated access. OIDC = login identity on top of OAuth.

---

#### 11. Common Mistakes

1. Plain-text or fast-hash passwords.
2. Missing ownership checks.
3. Trusting `userId` from the request body.
4. Long-lived access tokens.
5. Tokens in plain storage or logs.
6. Only hiding buttons in the app instead of checking on the server.
7. Building your own crypto or login protocol.

---

#### 12. Related Topics

1. `02` Networking & HTTP (401 vs 403, headers)
2. `03` API Design
3. `06` Backend Security Essentials
4. `07` Testing & Debugging (test permissions)
5. API gateway (system design roadmap)

---

#### 13. Interview Must Remember

1. **AuthN = who. AuthZ = what.** 401 vs 403.
2. **Hash passwords** (bcrypt/argon2 + salt).
3. **Access token (short) + refresh token (long).**
4. **Ownership check on every record**, with the user taken from the token.
5. Store tokens in **Keychain / Keystore**.
6. Use established libraries. **Never invent your own crypto.**
