# Operations & Monitoring

Roadmap topic 19 · Stage 5: Operating

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** a database problem you can see coming is a database problem you can fix calmly. This topic is about the specific numbers to watch, so "the database feels slow" becomes "connections are near the limit" — a real, actionable diagnosis instead of a vague feeling.

---

#### 1. Connection Pooling with Many Servers — 🟢 Must Know

*Repeated deliberately — a genuinely common, easy-to-hit operational problem.*

Every database has a **maximum connection limit**. With many application server instances, each running its own connection pool, the **total** connections across all of them can exceed that limit — a problem that has nothing to do with any single query's performance, and everything to do with fleet-wide connection math (`6`, item 5; `BE 9`).

---

#### 2. What to Monitor — 🟢 Must Know

The standard dashboard for any production database: **query latency**, **slow queries**, **connection count**, **lock contention**, **replication lag**, **disk usage**, **CPU**, **cache hit ratio**. Any one of these trending wrong is an early warning, well before it becomes a user-facing incident.

---

#### 3. Slow-Query Log and Query Statistics — 🟢 Must Know

A running log of queries that exceeded a time threshold — the direct, concrete input to `6`'s "measure first" discipline. Query statistics (aggregated by query shape) show which queries, in total, consume the most time across the whole system — often more useful than looking at individual slow instances alone.

---

#### 4. Capacity Planning — 🟢 Must Know

Track the **growth** of data volume, storage usage, and traffic over time — so scaling decisions (a bigger machine, a read replica, sharding, `15` item 1) happen ahead of an actual crunch, based on a visible trend, not reactively once something is already struggling.

---

#### 5. Routine Maintenance — 🟡 Good to Know

**Vacuum** (reclaiming space from dead row versions, `7` item 8), **analyze** (refreshing query planner statistics, `6` item 8), **reindex** (rebuilding a bloated or corrupted index), and **archiving old data** — the regular housekeeping that keeps a database healthy over months and years, not just at launch.

---

#### 6. Version Upgrades and Maintenance Windows — 🟡 Good to Know

Database version upgrades need real planning — testing compatibility, scheduling a maintenance window (or a zero-downtime upgrade strategy for critical systems), and a rollback plan, the same discipline as any other risky, hard-to-reverse change (`ARCH 3`).

---

#### 7. Runbooks for Common Incidents — 🟡 Good to Know

Documented response steps for the recurring failure modes: **locks** (a long-running transaction blocking others), **full disk**, **replica lag spiking**, **connection exhaustion** — the same runbook discipline from `ARCH 13`, applied to the specific incidents a database actually produces.

---

#### 8. Managed Database Features and Their Limits — 🟡 Good to Know

Managed services (`11`, item 5) often provide automated backups, monitoring, and failover out of the box — genuinely valuable, but know their specific limits (what version upgrades they support, what configuration you can and can't control) rather than assuming they handle everything.

---

#### 9. Cost Control — 🟡 Good to Know

**Right-sizing** the database instance to actual load (not over-provisioned "just in case"), and using cheaper **storage tiers** for less frequently accessed data — the database-specific instance of `ARCH 13`'s general cost-as-a-design-constraint guidance.

---

#### 10. Common Interview Questions

1. **The app is throwing connection errors, but individual queries run fine — what's likely happening?**
   Connection pool exhaustion — with many server instances each holding their own pool, the total connections across the fleet can exceed the database's maximum, unrelated to any single query's own performance.
2. **What would you put on a database monitoring dashboard?**
   Query latency, slow-query counts, connection count, lock contention, replication lag, disk usage, CPU, and cache hit ratio — the standard set that gives early warning before a user-facing incident.
3. **How do you plan for database capacity ahead of time?**
   Track data volume, storage, and traffic growth trends over time, and act on scaling (bigger machine, read replica, sharding) based on the visible trend, rather than reacting only once performance already suffers.
4. **What's the difference between vacuum and analyze?**
   Vacuum reclaims space from dead row versions (cleaning up bloat). Analyze refreshes the query planner's statistics about the data, so it makes good execution-plan decisions.

---

#### 11. Common Mistakes

1. Not accounting for total connections across many server instances, only per-instance.
2. No slow-query log or monitoring, discovering performance problems only from user complaints.
3. Skipping routine maintenance (vacuum, analyze) until performance has already visibly degraded.
4. No capacity-planning trend tracking, scaling reactively instead of proactively.

---

#### 12. Related Topics

1. `6` Query Performance & Execution Plans — the "measure first" discipline this topic operationalises
2. `BE 9` Connecting API to Database — connection pooling from the application side
3. `ARCH 13` Operations, Deployment & Cost — the same operational discipline at the architecture level

---

#### 13. Interview Must Remember

1. **Connection limits are a fleet-wide problem**, not a per-instance one.
2. **Standard dashboard**: latency, slow queries, connections, locks, replication lag, disk, CPU, cache hit ratio.
3. **Slow-query log** is the concrete input to measuring before optimising.
4. **Track growth trends** for proactive, not reactive, capacity planning.
