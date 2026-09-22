# Schema Migrations & Evolution

Roadmap topic 10 · Stage 3: Correctness

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** a schema change on a live system is a live-surgery problem — old code and new code both need to keep working while the change rolls out, because you can never update every server (or every app, `MOB 1`) at exactly the same instant.

---

#### 1. Versioned Migration Scripts — 🟢 Must Know

Every schema change is a **numbered, versioned script**, kept in source control alongside the application code — never a manual, undocumented change made directly against a production database.

```text
001_create_users.sql
002_add_email_index.sql
003_add_notes_table.sql
```

---

#### 2. Forward-Only, Tested on a Copy of Production — 🟢 Must Know

Migrations generally move **forward only** (rollback plans exist, item 9, but "forward fix" is often safer than reverse-migrating). Test a migration against a **real copy of production data** before running it for real — a migration that works fine on an empty test database can fail or behave very differently against real data volume and shape.

---

#### 3. Backward-Compatible Changes — 🟢 Must Know

*The core discipline of this whole topic.*

During a rollout, **old and new server versions run at the same time** (`SD 28`), and — for mobile especially — **old app versions may run against the new schema for years** (`MOB 1`). A migration must not break code that hasn't been updated yet.

---

#### 4. Expand and Contract — 🟢 Must Know

*The standard safe pattern for any schema change that isn't trivially backward compatible.*

```text
1. EXPAND:   add the new column/table, alongside the old one
             (old code keeps working, unaware of the new shape)
2. MIGRATE:  backfill data into the new shape; write to BOTH old and new
             (dual writes, so both stay in sync during the transition)
3. SWITCH:   update application code to read from the new shape
             (deploy this once all servers/clients can handle it)
4. CONTRACT: remove the old column/table, once nothing reads it anymore
```

Each step is small and independently safe — no single step requires "everything changes atomically, everywhere, at once".

---

#### 5. Risky Changes — 🟢 Must Know

1. **Renaming** a column or table — looks like one operation, but is really a drop-and-add to anything still using the old name; treat it as expand-and-contract, not a simple rename.
2. **Dropping** a column — irreversible once done; make sure nothing reads it first.
3. **Changing a type** — can silently truncate or reject data that fit the old type.
4. **Adding `NOT NULL`** to an existing column — fails immediately if any existing row has `NULL` there; backfill first (item 7).

---

#### 6. Changing Big Tables Without Downtime — 🟡 Good to Know

A naive schema change can lock a huge table for the whole operation, blocking all reads and writes for that duration. **Batching** (changing rows in small chunks) or **online schema change tools** (which build a new table structure alongside the old one and swap it in) avoid this on large tables.

---

#### 7. Backfilling Data Safely — 🟡 Good to Know

Filling a new column for existing rows — do it in **batches**, not one giant `UPDATE` touching millions of rows at once (which would lock heavily and risk timing out or bloating the transaction log).

---

#### 8. Migration Tools — 🟡 Good to Know

Dedicated tools (Flyway, Liquibase) or framework-built-in migration systems track which migrations have run, in what order, and apply new ones automatically and consistently across environments — far more reliable than manually tracking schema state.

---

#### 9. Rollback Plans, and Why "Forward Fix" Is Often Better — 🟡 Good to Know

A true rollback (reversing a migration) can be riskier than it sounds, especially once new data has already been written in the new shape — often, writing a **new forward migration that fixes the problem** is safer and clearer than trying to reverse-migrate live data.

---

#### 10. Schema and API Versioning Together — 🟡 Good to Know

A schema change and the API change that exposes it should be planned together, using the same backward-compatibility discipline (`ARCH 10`) — a schema change alone doesn't guarantee the API built on top of it stays compatible.

---

#### 11. Common Interview Questions

1. **How do you safely rename a database column with zero downtime?**
   Treat it as expand-and-contract: add the new column, dual-write to both old and new, backfill, switch reads to the new column once all consumers are updated, then drop the old one — never a direct, one-step rename on a live system.
2. **Why is adding a `NOT NULL` constraint to an existing column risky?**
   It fails immediately if any existing row has `NULL` in that column — backfill a default value first, then add the constraint.
3. **Why should migrations be backward compatible, specifically for a mobile product?**
   Old app versions can stay in active use for years and can't be forced to update instantly — a schema or API change that breaks them would break real users with no way to fix it on their end.
4. **What's the "expand and contract" pattern?**
   A four-step safe migration approach: expand (add the new shape), migrate (backfill and dual-write), switch (move reads to the new shape), contract (remove the old shape) — each step independently safe.

---

#### 12. Common Mistakes

1. A direct rename or type change on a live table with active traffic.
2. Adding `NOT NULL` without backfilling existing `NULL` values first.
3. One giant `UPDATE` backfilling millions of rows instead of batching.
4. Assuming a schema change is safe just because it works against an empty local database.
5. Not considering old app versions when changing an API/schema exposed to mobile clients.

---

#### 13. Related Topics

1. `2` Relational Model & Data Modeling — the schema being evolved
2. `SD 28` Deployment & Release — old and new server versions running together
3. `MOB 1`, `MOB 9` — old app versions and Room migrations, the mobile-side equivalent of this discipline
4. `ARCH 10` Integration & API Architecture — schema and API versioning together

---

#### 14. Interview Must Remember

1. **Versioned migration scripts, tested on a copy of real data.**
2. **Expand and contract** — the standard safe pattern for any non-trivial change.
3. **Renaming, dropping, type changes, and adding `NOT NULL`** are all risky — treat them carefully.
4. **Old app versions and old server versions run together** — every change must stay backward compatible.
