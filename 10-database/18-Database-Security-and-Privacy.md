# Database Security & Privacy

Roadmap topic 18 · Stage 5: Operating

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** the database is where the actual valuable data lives, so it deserves the strictest care of anything in the system. Most database security is a handful of unglamorous, foundational habits — done consistently, they close off the majority of real-world attacks.

---

#### 1. SQL Injection and Parameterized Queries — 🟢 Must Know

*Repeated deliberately from topic `3` — the single most important database security rule.*

```sql
-- Dangerous: user input concatenated directly into SQL
"SELECT * FROM users WHERE email = '" + input + "'"

-- Safe: parameterized
SELECT * FROM users WHERE email = $1;
```

An attacker who can inject SQL through unvalidated string concatenation can read, modify, or delete arbitrary data — always use parameterized queries, never string-build SQL from user input (`BE 6`).

---

#### 2. Least Privilege — 🟢 Must Know

**Separate database users** for different jobs: the application's normal runtime user (limited to exactly what the app needs), a migration user (schema-change permissions, used rarely), a reporting/analytics user (read-only). No single user should have more access than its specific job requires (`ARCH 11`).

---

#### 3. Never Expose the Database to the Internet — 🟢 Must Know

The database should live on a **private network**, reachable only from the application servers that need it — never with a public IP and open port directly reachable from anywhere. This single practice closes off a huge share of real-world database breaches.

---

#### 4. Encryption in Transit and at Rest — 🟢 Must Know

**In transit** — TLS for every connection to the database. **At rest** — the underlying storage (and backups, `17` item 6) encrypted on disk. Both are close to non-negotiable for any production system handling real user data.

---

#### 5. Secrets for Database Credentials — 🟢 Must Know

Database credentials belong in a **secrets manager**, never hardcoded or committed to a repository (`ARCH 11`) — and should be **rotated** periodically, so a leaked credential has a limited window of usefulness.

---

#### 6. Personal Data (PII) — 🟢 Must Know

**Store the minimum** actually needed, **protect** what you do store, and support **deletion on request** — a direct application of `ARCH 9`'s privacy-shapes-data-architecture principle, at the database level specifically.

---

#### 7. Row-Level Security — 🟡 Good to Know

A database feature (PostgreSQL, and the mechanism behind Supabase's security model, `12` item 11) that enforces **per-row access rules directly in the database** — a user's query automatically only sees rows they're allowed to see, enforced at the lowest level rather than trusted to application code alone.

---

#### 8. Multi-Tenancy — 🟡 Good to Know

| Approach | Isolation | Operational cost |
|---|---|---|
| Shared tables with a `tenant_id` column | Weakest — a missing `WHERE tenant_id = ?` leaks data | Lowest |
| Separate schemas per tenant | Stronger | Medium |
| Separate databases per tenant | Strongest | Highest |

The right choice depends on how strict the isolation requirement genuinely is — a shared-table approach needs row-level security (item 7) or very disciplined query-writing to be safe.

---

#### 9. Column Encryption, Masking, Tokenization — 🟡 Good to Know

Beyond whole-database encryption at rest: encrypting **specific sensitive columns** individually, **masking** values in non-production environments (so a staging database doesn't leak real personal data to every developer), and **tokenization** (replacing a sensitive value with a non-sensitive reference token) — extra layers for especially sensitive fields.

---

#### 10. Audit Logs and Access Reviews — 🟡 Good to Know

A record of **who accessed or changed what, and when** — both a security detective control (catching misuse after the fact) and often a compliance requirement (`ARCH 11`, item 10).

---

#### 11. Compliance Basics — 🟡 Good to Know

GDPR-style regulations shape real database decisions: data residency (where data can physically be stored), retention limits, and the technical capability to delete a specific user's data — the same theme as `9`, item 6 and `17`, item 9, now from the security/compliance angle.

---

#### 12. Common Interview Questions

1. **How do you prevent SQL injection?**
   Always use parameterized queries — send the SQL structure and the data values separately, so user input can never be interpreted as SQL syntax.
2. **Why should the application, migration, and reporting roles use separate database users?**
   Least privilege — each gets only the access its specific job needs, limiting the damage if any one credential is compromised.
3. **How do you handle multi-tenancy securely with shared tables?**
   Row-level security enforced at the database level is the strongest safety net — relying purely on every application query remembering to filter by `tenant_id` is fragile and one missed filter away from a data leak.
4. **What does "least privilege" mean for a database, concretely?**
   Separate users per job function, each scoped to only what that job requires — the app's runtime user shouldn't have schema-change permissions, and the reporting user shouldn't have write access.

---

#### 13. Common Mistakes

1. Building SQL from string concatenation with user input.
2. One shared, over-privileged database user for everything — app, migrations, and reporting alike.
3. A database with a public IP directly reachable from the internet.
4. Multi-tenant data isolated only by application-code discipline, with no database-level enforcement.
5. No deletion capability for personal data, discovered only when a request arrives.

---

#### 14. Related Topics

1. `3` SQL Fundamentals — where parameterized queries are first introduced
2. `BE 6` Backend Security Essentials — SQL injection in full depth
3. `ARCH 11` Security Architecture — least privilege and defense in depth at the architecture level
4. `9` Data Architecture (in `09-architecture`) — privacy shaping data design

---

#### 15. Interview Must Remember

1. **Always parameterize queries** — never build SQL from string concatenation.
2. **Least privilege**: separate users for app, migrations, and reporting.
3. **Never expose the database to the internet directly.**
4. **PII: minimum stored, protected, deletable on request.**
