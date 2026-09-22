# Relational Model & Data Modeling

Roadmap topic 2 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** modeling data well means designing tables that match how you'll actually query them, enforce the rules that must never break, and avoid storing the same fact in two places where it can quietly disagree with itself.

---

#### 1. Keys — 🟢 Must Know

1. **Primary key** — uniquely identifies a row in its table.
2. **Foreign key** — a column referring to a row in another table, enforcing that the reference actually exists.
3. **Unique key** — like a primary key's uniqueness guarantee, but for a column that isn't the row's main identifier.
4. **Composite key** — a key made of more than one column together.

```sql
CREATE TABLE notes (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id),   -- foreign key
    slug TEXT UNIQUE,                              -- unique key
    title TEXT NOT NULL
);
```

---

#### 2. Surrogate Keys vs Natural Keys — 🟢 Must Know

1. **Surrogate key** — an ID the system generates (an auto-increment integer or a UUID), with no real-world meaning (`SD 20`).
2. **Natural key** — a real-world value used as the key (an email address).
3. **Prefer surrogate keys** — natural keys can change (a user changes their email) or turn out not to be as unique as assumed, and changing a primary key later is painful.

---

#### 3. Relationships — 🟢 Must Know

| Type | Example | How it's modeled |
|---|---|---|
| One-to-one | A user and their profile | Foreign key with a unique constraint |
| One-to-many | A user and their notes | Foreign key on the "many" side |
| Many-to-many | Notes and tags | A join table with two foreign keys |

```sql
CREATE TABLE note_tags (
    note_id UUID REFERENCES notes(id),
    tag_id UUID REFERENCES tags(id),
    PRIMARY KEY (note_id, tag_id)      -- composite key, prevents duplicate links
);
```

---

#### 4. Design the Schema from the Queries You Need — 🟢 Must Know

*The single most important modeling discipline, echoed from `BE 8`.*

Write down your top queries **first**, then design tables and indexes (topic `5`) around them — a schema that looks "textbook correct" but doesn't match real query patterns will need expensive joins or scans everywhere it's actually used.

---

#### 5. Normalization — 🟢 Must Know

*Store each fact exactly once, so it can never disagree with itself.*

```text
1NF: no repeating groups — each column holds one value, not a list
2NF: every non-key column depends on the WHOLE primary key, not part of it
3NF: every non-key column depends ONLY on the key, not on another non-key column
```

Example fix: a `notes` table with a `user_email` column duplicates data already in `users` — if the user changes their email, the note's copy goes stale. Store `user_id` and join to `users` instead.

---

#### 6. Denormalization — 🟢 Must Know

*The deliberate, opposite choice — copy data on purpose.*

Sometimes duplicating a value (storing a product's name directly on an order line, so historical orders don't change if the product is renamed) is the right call for performance or correctness. Denormalize **deliberately and knowingly**, not by accident — and know what it costs: the copies can drift apart if not kept in sync carefully.

---

#### 7. Constraints — 🟢 Must Know

```sql
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    balance_cents INTEGER NOT NULL CHECK (balance_cents >= 0)
);
```

`NOT NULL`, `UNIQUE`, foreign keys, and `CHECK` all enforce rules **inside the database itself** — the strongest possible guarantee, since it holds even if application code has a bug that would otherwise let bad data through.

---

#### 8. Data Types — 🟢 Must Know

1. **Money** — store as integer cents, or a fixed-point `DECIMAL` — **never** a floating-point type, which introduces rounding errors that compound over many transactions.
2. **Time** — store in UTC, convert to a local time zone only at display time.
3. **Text vs enum** — a fixed, small set of values (a status field) is often better as an enum type (or a `CHECK` constraint) than free text, catching typos at the database level.

---

#### 9. `NULL` — 🟢 Must Know

`NULL` means "no value" or "unknown" — not zero, not an empty string. `column = NULL` never matches anything, even another `NULL` — always compare with `IS NULL` or `IS NOT NULL` instead.

```sql
SELECT * FROM notes WHERE archived_at IS NULL;   -- correct
SELECT * FROM notes WHERE archived_at = NULL;    -- always returns nothing
```

---

#### 10. ER Diagrams — 🟡 Good to Know

A picture of tables and how they relate — genuinely useful for communicating a schema design, even a quick hand-drawn one, before or alongside writing the actual `CREATE TABLE` statements.

---

#### 11. Soft Delete vs Hard Delete — 🟡 Good to Know

**Soft delete** — mark a row as deleted (a `deleted_at` timestamp) instead of removing it, preserving history and allowing undo. **Hard delete** — actually remove the row. Soft delete is common, but adds the burden of filtering deleted rows out of every query — decide deliberately per table.

---

#### 12. Audit Columns — 🟡 Good to Know

`created_at`, `updated_at`, `created_by` — small, standard columns that pay for themselves constantly during debugging and support — worth adding as a default habit on most tables.

---

#### 13. Modeling Trees, Hierarchies, Tags, History — 🟡 Good to Know

1. **Trees/hierarchies** (comments, categories) — a self-referencing `parent_id` foreign key is the simplest approach; recursive CTEs (topic `4`) query them.
2. **Tags** — a many-to-many join table (item 3).
3. **History** — either an append-only events table, or a separate `_history` table capturing prior versions of a row.

---

#### 14. Common Interview Questions

1. **How do you design a schema for a new feature?**
   Start from the queries the feature actually needs (item 4), then design tables, keys, and constraints around them — not the reverse.
2. **Why prefer a surrogate key over a natural key?**
   Natural keys can change or turn out not to be as unique as assumed; a surrogate key never needs to change, which matters a lot since changing a primary key later is expensive and risky.
3. **What is normalization, and when would you deliberately denormalize?**
   Normalization stores each fact once, avoiding conflicting copies. Denormalization deliberately duplicates data for performance or historical accuracy, accepting the cost of keeping copies in sync.
4. **Why store money as integer cents instead of a float?**
   Floating-point numbers introduce rounding errors that compound across many transactions — integer cents (or fixed-point decimal) avoid that entirely.
5. **Why does `column = NULL` never work?**
   `NULL` means unknown, and an unknown value can't be confirmed equal to anything, not even another `NULL` — always use `IS NULL`/`IS NOT NULL`.

---

#### 15. Common Mistakes

1. Designing a "textbook normalized" schema that doesn't match how the app actually queries the data.
2. Using a natural key (email) as a primary key.
3. Storing money as a floating-point type.
4. Using `= NULL` instead of `IS NULL`.
5. Denormalizing accidentally (duplicated data nobody decided to duplicate on purpose) instead of deliberately.

---

#### 16. Related Topics

1. `3` SQL Fundamentals — the queries this modeling should be designed around
2. `5` Indexes — indexing the columns your queries actually use
3. `7` Domain-Driven Design Essentials (in `09-architecture`) — bounded contexts and entity modeling at a higher level
4. `SD 20` Unique ID Generation — more on surrogate key strategies

---

#### 17. Interview Must Remember

1. **Design the schema from the queries**, not the other way around.
2. **Surrogate keys by default.** Natural keys change and cause pain later.
3. **Normalize by default; denormalize deliberately**, knowing the cost.
4. **Money as integer cents, never a float. Time in UTC. `IS NULL`, never `= NULL`.**
