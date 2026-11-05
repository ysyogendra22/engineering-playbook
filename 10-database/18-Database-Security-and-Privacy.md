# Database Security & Privacy

> The database holds the crown jewels. Use parameterized queries, least-privilege users, a private network, encryption, managed secrets, minimal personal data, and row-level isolation for tenants and users. Plan for deletion and audit from the start.

Roadmap topic 18 · Stage 5: Operating

**Go deeper:** `04-backend-engineering/06-Backend-Security-Essentials` · `09-architecture/11-Security-Architecture` and `09-Data-Architecture` · `05-system-design/29-Backup-Recovery-Security-and-Cost` · `06-mobile-engineering/13-Security` · `3` SQL Fundamentals · `17` Backup & Recovery.

**Marks:** 🟢 must know · 🟡 good to know

**How the examples are checked:** SQL-injection and tenant-leak behaviour, an audit trigger and masking are run on SQLite 3.54; PostgreSQL features (roles, row-level security, `pgcrypto`, TLS settings) are shown and not run.

---

#### 1. What Is It?

*Protecting stored data and the access paths to it.*

| 🟢 Must know | 🟡 Good to know |
|---|---|
| SQL injection and parameterized queries | row-level security |
| least privilege: separate users for app, migrations, reporting | multi-tenancy models |
| never expose the database to the internet | column encryption, masking, tokenization |
| encryption in transit and at rest | audit logs and access reviews |
| secrets for credentials: manager and rotation | compliance basics (GDPR-style rules) |
| personal data: minimum, protect, delete on request | |

1. **SQL injection:** attacker-controlled input changes the meaning of your SQL.
2. **Least privilege:** each user/service gets only the access it needs.
3. **PII:** personally identifiable information.
4. **Multi-tenancy:** many customers sharing one system, kept apart.

**Signals in an interview:** "how do you prevent SQL injection?", "which database user does the app use?", "how do you keep tenants' data apart?", "how do you handle a GDPR deletion request?".

---

#### 2. How It Works

**SQL injection and parameterized queries.** If you build SQL by concatenating input, an attacker can add their own SQL (`x' OR '1'='1` makes the condition always true; other payloads read or destroy data). A **parameterized query** sends the SQL text and the values separately, so input is always data, never code. Also: validate input, avoid dynamic table/column names from input (allow-list them), and use an ORM/query builder carefully (raw fragments are still dangerous).

**Least privilege.** Use separate database users:

| User | Privileges |
|---|---|
| `app` | `SELECT, INSERT, UPDATE, DELETE` on application tables only; no DDL, no superuser |
| `migrator` | DDL on the schema, used only by the migration job (topic 10) |
| `reporting` | read-only (on a replica), maybe on a restricted view |
| `backup` | read access/replication role, nothing else |
| humans | individual accounts via SSO, time-limited elevated access, audited |

An application that runs as the database owner turns any injection or bug into a total compromise.

**Never expose the database to the internet.** Put it in a private network/subnet, allow connections only from the application hosts (security groups, firewall, private endpoints), require TLS, no default or shared passwords, and no public IP. Admin access through a bastion or a secure proxy.

**Encryption.**

| | Meaning | How |
|---|---|---|
| In transit | data on the network is encrypted | TLS between app and database (`sslmode=verify-full` in PostgreSQL), and for replication and backups |
| At rest | data on disk is encrypted | disk/volume encryption or transparent database encryption with keys in a KMS; encrypted backups |
| In use / field level | sensitive columns encrypted by the app | application-level encryption for highly sensitive fields; harder to query |

**Secrets for credentials.** Store database passwords in a secrets manager (not in code, Git, images or the mobile app), inject at runtime, **rotate** regularly and after exposure, prefer short-lived or IAM-based credentials, separate per environment.

**Personal data (PII).** Collect and store the minimum; classify it; protect it (access control, encryption, masking in non-production); keep it only as long as needed; support **access and deletion** requests across the database, caches, search indexes, analytics, logs and backups (by expiry); never copy production PII into test environments without masking.

🟡 **Row-level security (RLS).** The database itself filters rows by the current user/tenant: PostgreSQL `CREATE POLICY`, Supabase uses it so clients can talk to the database safely. It protects against application bugs that forget a `WHERE tenant_id = ?`.

🟡 **Multi-tenancy.**

| Model | How | Isolation | Cost |
|---|---|---|---|
| Shared tables with a `tenant_id` column | one schema; every query filtered | weakest (needs RLS and discipline) | lowest |
| Schema per tenant | separate schemas in one database | medium | medium; many schemas get heavy |
| Database per tenant | separate databases | strongest; easy per-tenant backup/restore | highest |

Choose by number of tenants, size, isolation and compliance needs. Always enforce the tenant filter in one place (a repository layer, RLS), not by memory in every query.

🟡 **Column encryption, masking, tokenization.** *Encrypt* sensitive columns (keys held outside the database). *Mask* data shown to people who don't need the full value (`a***@x.com`). *Tokenize* very sensitive values (card numbers) by replacing them with tokens held in a vault, so your database never holds the real value (and falls out of PCI scope).

🟡 **Audit logs and access reviews.** Log who accessed or changed sensitive data (database audit extensions, triggers, or application-level audit tables); protect logs from tampering; review access regularly (who still needs what?).

🟡 **Compliance basics.** GDPR-style rights (access, rectification, deletion, portability), data residency, retention limits, breach notification; PCI-DSS for card data; HIPAA for health data; SOC 2 evidence. Design for them early (`ARCH 9`, `ARCH 11`).

---

#### 3. Naive vs Better Design

| Naive | Better |
|---|---|
| `"... WHERE name = '" + input + "'"` | parameterized queries |
| the app connects as the owner/superuser | a restricted `app` user; separate `migrator` |
| a public database endpoint with a password | private network, TLS, allow-listed hosts |
| a password in the repository or in the mobile app | secrets manager, rotation; the app calls the API |
| tenant filter written by hand in each query | one place: repository layer or row-level security |
| production data copied to a laptop | masked/synthetic test data |
| logging full queries with personal data | redacted logs |
| no audit trail | audit logs for sensitive tables |

```kotlin
// Naive: SQL injection waiting to happen
val rows = db.query("SELECT * FROM users WHERE name = '$name'")
```

---

#### 4. SQL & Code

SQL injection demonstrated and fixed (SQLite; users `ann`, `bob`):

```sql
-- String-built with input   x' OR '1'='1
SELECT name FROM users WHERE name = 'x' OR '1'='1';          -- returns ann, bob  (the whole table)
-- Parameterized
SELECT name FROM users WHERE name = ?;                        -- ? = "x' OR '1'='1"  → no rows (it is only a name that doesn't exist)
```

Checks: the string-built query returns `[ann, bob]`; the parameterized one returns `[]`. A driver also refuses stacked statements (`SELECT 1; DROP TABLE users` fails: "You can only execute one statement at a time"), which blocks one class of attack but not the always-true trick above.

Kotlin with parameters, and an allow-list for dynamic parts:

```kotlin
fun findByName(conn: Connection, name: String): List<String> =
    conn.prepareStatement("SELECT name FROM users WHERE name = ?").use { ps ->
        ps.setString(1, name)
        ps.executeQuery().use { rs -> generateSequence { if (rs.next()) rs.getString(1) else null }.toList() }
    }

private val sortable = setOf("created_at", "title")
fun orderBy(column: String) = if (column in sortable) column else "created_at"        // table/column names can't be parameters: allow-list them
```

Checks: `findByName(conn, "x' OR '1'='1")` → `[]`; `orderBy("title; DROP TABLE users")` → `created_at`.

Least-privilege roles (PostgreSQL, not run):

```sql
CREATE ROLE app LOGIN PASSWORD :'pw' NOSUPERUSER NOCREATEDB NOCREATEROLE;
GRANT CONNECT ON DATABASE notes TO app;  GRANT USAGE ON SCHEMA public TO app;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app;       -- no DDL
CREATE ROLE migrator LOGIN PASSWORD :'pw2';  GRANT ALL ON SCHEMA public TO migrator;
CREATE ROLE reporting LOGIN PASSWORD :'pw3'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO reporting;   -- connect only to a replica
REVOKE ALL ON DATABASE notes FROM PUBLIC;
```

Row-level security for tenants (PostgreSQL, not run):

```sql
ALTER TABLE notes ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON notes
  USING (tenant_id = current_setting('app.tenant_id')::bigint)
  WITH CHECK (tenant_id = current_setting('app.tenant_id')::bigint);
-- per request:  SET LOCAL app.tenant_id = '42';   (inside the transaction)  → every query sees only tenant 42
```

The shared-table leak it prevents (SQLite): `SELECT title FROM notes` returns both tenants' notes (`a`, `b`); with the filter `WHERE tenant = ?` only tenant 1's note (`a`). Forgetting the filter once is a breach; RLS makes the safe path automatic.

One place for the tenant filter in the application:

```kotlin
class NotesRepository(private val conn: Connection, private val tenantId: Long) {          // the tenant comes from the verified token, never from the request body
    fun all(): List<Note> = conn.prepareStatement("SELECT id, title FROM notes WHERE tenant_id = ?").use { ps ->
        ps.setLong(1, tenantId); ps.executeQuery().use { rs -> generateSequence { if (rs.next()) Note(rs.getLong(1), rs.getString(2)) else null }.toList() }
    }
}
```

Masking and a simple redaction helper:

```kotlin
fun maskEmail(email: String): String {
    val at = email.indexOf('@'); if (at <= 1) return "***" + email.substring(maxOf(at, 0))
    return email[0] + "***" + email.substring(at)
}
```

Checks: `maskEmail("ann@x.com")` → `a***@x.com`; `maskEmail("a@x.com")` → `***@x.com`.

Audit trigger (SQLite, runnable):

```sql
CREATE TABLE audit (id INTEGER PRIMARY KEY, acc_id INT, old INT, new INT, at TEXT DEFAULT (datetime('now')));
CREATE TRIGGER acc_audit AFTER UPDATE ON acc BEGIN INSERT INTO audit(acc_id, old, new) VALUES (OLD.id, OLD.bal, NEW.bal); END;
UPDATE acc SET bal = 70 WHERE id = 1;                          -- audit now has (acc 1, old 100, new 70)
```

TLS and secrets (JDBC URL; credentials come from the environment or a secrets manager):

```kotlin
val url = "jdbc:postgresql://db.internal:5432/notes?sslmode=verify-full&sslrootcert=/etc/ssl/rds-ca.pem"
val cfg = HikariConfig().apply { jdbcUrl = url; username = System.getenv("DB_USER"); password = secrets.get("notes/db-password") }
```

A privacy deletion fan-out (topic 17 and `ARCH 9`):

```kotlin
suspend fun deleteUser(userId: Long, holders: List<suspend (Long) -> Boolean>): Boolean = holders.all { it(userId) }       // database, cache, search, analytics, files
```

---

#### 5. Numbers & Limits

| Item | Rule of thumb |
|---|---|
| Database privileges | the application user has no DDL, no superuser |
| Network | no public IP; inbound only from app subnets; TLS 1.2+ |
| Credential rotation | at least every 90 days; immediately after exposure |
| Key management | keys in a KMS; rotate annually; test key recovery |
| Audit log retention | per regulation (1–7 years), tamper-evident |
| Deletion requests | fulfil within the legal period (often 30 days) |
| Multi-tenancy | shared tables + RLS for many small tenants; DB per tenant for few large/regulated ones |
| Injection defence | 100% of queries parameterized; raw SQL fragments reviewed |
| Backups | encrypted, access-controlled, tested |

---

#### 6. Common Mistakes & Edge Cases

1. Building SQL by string concatenation.
2. The application connecting as a superuser.
3. A publicly reachable database.
4. Credentials in code, images, logs or the app.
5. Shared tables with the tenant filter written by hand.
6. PII in logs, test data and analytics copies.
7. Encrypting at rest only and ignoring transit.
8. No deletion or audit plan.

Edge cases: ORM raw queries; dynamic sorting/filtering columns; admin tools with broad access; backups holding deleted users' data; replicas and read-only users with write privileges; connection strings printed in stack traces; tokens that grant database access directly to mobile clients (backend-as-a-service rules must be airtight).

---

#### 7. Say This in the Interview

1. "SQL injection is prevented by parameterized queries everywhere, allow-lists for dynamic identifiers, and an application user with least privilege."
2. "The database lives in a private network with TLS, encryption at rest, credentials in a secrets manager with rotation, and separate users for app, migrations and reporting."
3. "For multi-tenancy I enforce the tenant in one place: a repository layer taking the tenant from the verified token, backed by row-level security, so a missed `WHERE` can't leak data."
4. "I minimise personal data, mask it outside production, log access to sensitive tables, and support deletion across the database, caches, search, analytics and backups by expiry."

---

#### 8. Quick Check

1. How do parameterized queries stop injection?
2. Which database privileges should the app user have?
3. What does row-level security protect against?
4. Where should database passwords live?

<details>
<summary>Answers</summary>

1. The SQL text and values travel separately, so input can never be interpreted as SQL.
2. Only the DML it needs (`SELECT/INSERT/UPDATE/DELETE`) on application tables; no DDL or superuser rights.
3. A forgotten tenant or user filter in application code leaking other users' rows.
4. In a secrets manager, injected at runtime and rotated; never in code, Git or the mobile app.

</details>

---

#### 9. Practice

**Interview questions**

1. How do you prevent SQL injection?
2. What users and privileges does your database have?
3. How do you isolate tenants in one database?
4. How do you protect personal data and honour deletion requests?
5. How do you secure database credentials?
6. What would you log for audit?

**Hands-on**

1. Reproduce injection against a string-built query, then fix it with parameters and an allow-list.
2. Create `app`, `migrator` and `reporting` roles and confirm `app` cannot `DROP TABLE`.
3. Turn on row-level security for a tenant table and test that one tenant cannot read another's rows.
4. Add an audit trigger on a sensitive table.

**Remember:** parameters always · least-privilege users · private network + TLS + encryption at rest · secrets manager and rotation · enforce tenants in one place + RLS · minimise, mask and delete PII · audit sensitive access.
