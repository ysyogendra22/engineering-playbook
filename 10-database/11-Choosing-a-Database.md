# Choosing a Database

Roadmap topic 11 · Stage 4: Choosing & Scaling

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** most real systems don't use one database — they use several, each doing what it's good at. The skill isn't picking "the best database"; it's picking the right store for each specific job, with a relational database as the default until a real reason says otherwise.

---

#### 1. Ask First — 🟢 Must Know

Before choosing, answer: **data shape** (structured? flexible?), **query patterns** (what will actually be asked of it?), **consistency needs** (topic `16`), **scale** (real numbers), and **team skills** (can the team actually run this well? — `ARCH 3`).

---

#### 2. Relational as the Default — 🟢 Must Know

*The single most important guidance in this topic.*

Start with a relational database (PostgreSQL) unless there's a **clear, specific reason** to choose otherwise. Relational databases handle the general case well: structured data, relationships, strong consistency, flexible querying — most applications never outgrow this default.

---

#### 3. Polyglot Persistence — 🟢 Must Know

Real systems use **several stores together**, each for what it does best (`SD 17`):

```text
PostgreSQL   → the source of truth for structured application data
Redis        → cache, sessions, rate limiting (topic 13)
Elasticsearch → full-text search
S3 (object storage) → files, images, backups
```

This isn't a failure of "picking one database" — it's the normal, expected shape of a real system.

---

#### 4. Source of Truth vs Derived Data — 🟢 Must Know

Exactly one store is the **source of truth** for a given piece of data (`ARCH 9`) — everything else (a cache, a search index, a read model) is a **derived** copy, rebuildable from the source if it's ever lost or corrupted. Never let a derived store quietly become the only place data exists.

---

#### 5. Managed Service vs Self-Hosted — 🟢 Must Know

The same build-vs-buy trade-off from `ARCH 3`, applied to databases: a managed service (a cloud provider running and patching PostgreSQL for you) trades **cost and some control** for far less **operational effort**. For most teams without a dedicated database operations function, managed is the sensible default.

---

#### 6. A Decision Table — 🟡 Good to Know

| Need | Reach for |
|---|---|
| General application data, relationships, strong consistency | Relational (PostgreSQL) |
| Flexible/nested schema, document-shaped data | Document store (topic `12`) |
| Simple, very fast key lookups | Key-value store (topic `12`) |
| Full-text search with relevance ranking | Search engine (topic `12`) |
| Caching, counters, rate limits, sessions | Redis (topic `13`) |
| Analytics over historical data | Data warehouse (topic `20`) |

---

#### 7. Cost and Licensing — 🟡 Good to Know

Beyond the obvious hosting cost: some databases have licensing models that charge by usage in ways that surprise teams at scale — check pricing model, not just the headline "free and open source" claim, before committing.

---

#### 8. Migration Cost of Switching Later — 🟡 Good to Know

Switching a production database later is expensive and risky — worth weighing at decision time, not discovered only once you're deep into a choice that isn't working out.

---

#### 9. Hype-Driven Choices — 🟡 Good to Know

The same failure mode from `ARCH 3`, item 8 — choosing a trendy database because it's exciting, not because it fits this system's actual requirements. A boring, well-understood relational database that fits the need beats an exciting one that doesn't.

---

#### 10. Common Interview Questions

1. **How do you decide what database to use for a new feature?**
   Start from data shape, query patterns, consistency needs, scale, and team skills — default to relational unless a specific, clear reason points elsewhere.
2. **Why do most real systems use more than one type of database?**
   Polyglot persistence — different stores are good at different things (a relational database for structured data, Redis for caching, a search engine for full-text search) — one database rarely does everything well.
3. **What's the difference between a source of truth and derived data?**
   The source of truth is the one authoritative store for a piece of data. Derived data (a cache, a search index) is a rebuildable copy — losing it should never mean losing the real data.
4. **When would you choose a managed database service over self-hosting?**
   When the team doesn't have dedicated database operations capacity, or when the operational effort of self-hosting outweighs the extra cost and reduced control of a managed service — often the sensible default.

---

#### 11. Common Mistakes

1. Choosing a non-relational database without a clear, specific reason.
2. Letting a derived store (a cache) quietly become the only copy of important data.
3. Choosing a database because it's trending, not because it fits the requirements.
4. Not accounting for the real cost of migrating away from a database choice later.

---

#### 12. Related Topics

1. `12` NoSQL Families — the alternatives to relational, in depth
2. `SD 17` Choosing a Database — the same core content, first pass
3. `ARCH 3`, `ARCH 9` — trade-off decision-making and data architecture at the architect level

---

#### 13. Interview Must Remember

1. **Relational by default** — deviate only for a clear, specific reason.
2. **Polyglot persistence is normal** — several stores, each doing what it's good at.
3. **Exactly one source of truth** per piece of data; everything else is derived and rebuildable.
4. **Managed service is the sensible default** without dedicated database operations capacity.
