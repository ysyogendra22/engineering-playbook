# Data Architecture

Roadmap topic 9 · Stage 3: Cross-Cutting Concerns

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** data outlives code — a service gets rewritten every few years, but its data often survives for decades. Getting data ownership, consistency, and lifecycle right at the architecture level matters more, and is harder to fix later, than almost any other decision.

---

#### 1. Data Ownership and Single Source of Truth — 🟢 Must Know

Every piece of data should have **exactly one** owning service or system that's authoritative for it — everything else holds a read replica, a cache, or a derived view, never a competing "truth" (the same principle as `4`, item 9, at the architecture scale).

---

#### 2. Choose the Store by Data Shape and Access Pattern — 🟢 Must Know

Relational, document, key-value, graph, search, time-series — the choice should follow from how the data is actually shaped and queried, not from familiarity alone (full detail in `SD 17`). A relational default is reasonable; deviate only for a real, specific reason.

---

#### 3. Consistency Needs Per Feature — 🟢 Must Know

**Strong consistency** (a bank balance) and **eventual consistency** (a social media like count) are not the same requirement, and forcing every feature onto the same consistency model wastes either correctness or performance somewhere (full depth in `SD 23`). Decide this **per feature**, not once for the whole system.

---

#### 4. Schema Evolution and Migrations Without Downtime — 🟢 Must Know

Real systems change their schema constantly while staying live — the **expand and contract** pattern (add the new shape, migrate data, switch reads/writes, remove the old shape) is the standard safe approach, mirroring `DB 10`'s migration guidance at the architecture level.

---

#### 5. Data Lifecycle — 🟢 Must Know

**Retention** (how long is data kept), **archiving** (moving old data to cheaper storage), and **deletion** (including handling deletion requests, item 6) — a deliberate lifecycle policy, not an afterthought once storage costs or compliance pressure force the question.

---

#### 6. Privacy and Compliance — 🟢 Must Know

Regulations (GDPR-style rules) directly shape data architecture: where data can be stored geographically, how long it can be kept, and the technical ability to delete a specific user's data on request — these aren't just legal concerns, they're real architectural requirements that must be designed in from the start, not bolted on later.

---

#### 7. OLTP vs OLAP — 🟡 Good to Know

**OLTP** (online transaction processing) — many small, fast reads and writes, the shape of most application databases. **OLAP** (online analytical processing) — large, complex queries over historical data, typically served from a separate **data warehouse** or **data lake** so analytics never competes with production traffic.

---

#### 8. Data Flow Diagrams and Lineage — 🟡 Good to Know

A diagram of how data moves and transforms across systems, and **data lineage** — being able to trace exactly where a given piece of data originated and what transformed it along the way — increasingly important for both debugging and compliance.

---

#### 9. Caching and Read Models — 🟡 Good to Know

A cache (`SD 15`) or a dedicated read-optimised model (related to CQRS, `6`, item 8) is part of the data architecture, not an implementation detail bolted on afterward — decide deliberately what's cached, for how long, and how it's invalidated.

---

#### 10. Data Governance and Master Data — 🟡 Good to Know

**Data governance** — organisation-wide policies for data quality, ownership, and access. **Master data** — the authoritative, shared reference data (a canonical customer or product record) that many systems depend on — names worth knowing for larger organisations, less critical for smaller ones.

---

#### 11. Common Interview Questions

1. **How do you decide data ownership across services?**
   Each piece of data gets exactly one owning service; every other system holds a replica, cache, or derived view — never a second source of truth for the same data.
2. **How do you handle a schema change on a live system with no downtime?**
   Expand and contract: add the new shape alongside the old, migrate data, switch reads and writes over, then remove the old shape — never a single, risky in-place change.
3. **Does every feature need the same consistency guarantee?**
   No — decide per feature. Money and inventory usually need strong consistency; feeds and counters can usually tolerate eventual consistency, and forcing uniformity wastes either correctness or performance.
4. **How does privacy regulation shape data architecture, concretely?**
   It constrains where data can live, how long it's retained, and requires a real technical capability to delete a specific user's data on request — designed in from the start, not retrofitted under compliance pressure.

---

#### 12. Common Mistakes

1. Multiple services each treating their own copy of the same data as authoritative.
2. A risky, single-step schema migration instead of expand-and-contract.
3. Forcing one consistency model across every feature, regardless of actual need.
4. Treating data deletion and retention as an afterthought instead of a designed capability.

---

#### 13. Related Topics

1. `7` Domain-Driven Design Essentials — bounded contexts and data ownership are closely linked
2. `SD 17`, `SD 23` — choosing a database and consistency models, in full depth
3. `11` Security Architecture — privacy and data protection overlap directly here

---

#### 14. Interview Must Remember

1. **One owning service per piece of data** — everything else is a replica or derived view.
2. **Expand and contract** for schema changes with no downtime.
3. **Consistency is a per-feature decision**, not a system-wide default.
4. **Privacy and deletion capability are architectural requirements**, designed in from the start.
