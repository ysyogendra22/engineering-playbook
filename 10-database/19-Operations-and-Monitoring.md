# Operations & Monitoring

> A database needs care after launch: watch the right numbers, find slow queries, plan capacity, run routine maintenance, upgrade safely, and keep runbooks for the incidents that will happen.

Roadmap topic 19 · Stage 5: Operating

**Go deeper:** `6` Query Performance (pooling, slow queries) · `7` Storage Engines (vacuum, bloat) · `14` Replication · `17` Backup & Recovery · `05-system-design/27-Observability` · `09-architecture/13-Operations-Deployment-and-Cost`.

**Marks:** 🟢 must know · 🟡 good to know

**How the examples are checked:** capacity arithmetic and alert logic are checked in plain Kotlin/Python; PostgreSQL views and maintenance commands are shown for the idea and not run.

---

#### 1. What Is It?

*Keeping a production database healthy.*

| 🟢 Must know | 🟡 Good to know |
|---|---|
| connection pooling and limits with many servers | routine maintenance: vacuum, analyze, reindex, archive |
| what to monitor: latency, slow queries, connections, locks, replication lag, disk, CPU, cache hit | version upgrades and maintenance windows |
| slow-query log and query statistics | runbooks for common incidents |
| capacity planning | managed database features and limits |
| | cost control: right-sizing and storage tiers |

1. **Monitoring:** metrics, logs and alerts that show health.
2. **Capacity planning:** predicting when you run out of disk, memory, CPU or connections.
3. **Runbook:** step-by-step instructions for a known problem.

**Signals in an interview:** "what do you monitor on a database?", "the database is slow right now, what do you check?", "disk is 90% full", "how do you upgrade?".

---

#### 2. How It Works

**What to monitor (the golden signals for a database).**

| Area | Metrics | Alert when |
|---|---|---|
| Latency | query p50/p95/p99, slow-query count | p95 above target; sudden jump |
| Throughput | queries/s, transactions/s, rows read/written | unusual drop or spike |
| Errors | failed queries, deadlocks, timeouts, constraint violations | rising rate |
| Connections | active, idle, waiting; usage vs limit | > 80% of the limit; waiting > 0 for minutes |
| Locks | blocked queries, longest lock wait, long transactions | transaction open > 5 min; blocked > 30 s |
| Replication | lag (time and bytes), replica state, slot size | lag > 5–60 s; replica down |
| Storage | disk used, growth per day, WAL size, table/index bloat | disk > 80%; < 7 days to full |
| Memory/cache | cache hit ratio, buffer pool, swap | hit ratio < 95–99%; swapping |
| CPU/IO | CPU, IOPS, IO wait, throughput limits | saturation for minutes |
| Backups | last success, age, restore test result | last backup older than the RPO |

**Slow-query log and query statistics.** Log queries slower than a threshold (100 ms) and keep aggregate statistics (`pg_stat_statements`, MySQL performance schema): calls, total time, mean time, rows. Sort by **total time** to find what matters most; fix with indexes, rewrites or caching (topic 6).

**Connection pooling and limits with many servers.** Each connection costs memory (PostgreSQL ≈ several MB); the server has a maximum (`max_connections`). `servers × pool size` plus admin, migration and replication needs must stay under it. Use an external pooler (PgBouncer, RDS Proxy) when you have many instances, serverless functions or spiky traffic; watch "waiting for a connection" in the app pool.

**Capacity planning.** Track growth of data size, rows, index size, traffic and connections. Forecast: `days to full = free space ÷ daily growth`. Plan before you hit limits: add storage, partition/archive, scale up, add replicas or a cache. Load-test with realistic data volumes.

🟡 **Routine maintenance.**

| Task | Why |
|---|---|
| `VACUUM` / autovacuum (PostgreSQL) | reclaim dead row versions, prevent bloat and transaction-id wraparound |
| `ANALYZE` | refresh planner statistics after big changes |
| `REINDEX` / rebuild bloated indexes | restore index efficiency (concurrently) |
| archive or partition-drop old data | keep tables and indexes small (topic 15) |
| rotate logs, backups, credentials | housekeeping and security |
| check unused indexes and duplicates | cut write cost and space |

🟡 **Version upgrades and maintenance windows.** Minor versions: security fixes, routinely applied (managed services can automate). Major versions: test on a copy (extensions, query plans, application compatibility), choose in-place upgrade or logical replication to a new cluster, schedule a window, keep a rollback path, and don't fall out of support. Announce downtime or use rolling approaches.

🟡 **Runbooks for common incidents.** Write them before you need them:

| Incident | First steps |
|---|---|
| Connection exhaustion | check pool sizes and leaks, find idle-in-transaction sessions, kill the offenders, raise limits or add a pooler |
| Lock pile-up | find the blocking query, check the long transaction, cancel/terminate it, review the code path |
| Full disk | free space (WAL, logs, old backups), add storage, find the growth source, archive/partition |
| Replica lag | check long queries on the replica, network, write bursts, replication slots |
| Slow queries after a deploy | compare plans, check missing indexes/stale statistics, roll back the change |
| Failover | follow the failover runbook (topic 14), verify, rebuild the old leader |

🟡 **Managed database features and their limits.** Automated backups, patching, failover, monitoring dashboards, read replicas, storage autoscaling; limits on extensions, superuser access, parameters and maintenance timing; understand them and what is still your job (indexes, queries, pool sizes, schema changes, cost).

🟡 **Cost control.** Right-size instances from real utilisation (CPU, memory, IOPS), use storage tiers and archive old partitions, delete idle replicas and old snapshots, buy commitments for steady load, watch IOPS and data-transfer charges (`ARCH 13`).

---

#### 3. Naive vs Better Design

| Naive | Better |
|---|---|
| "it's up, so it's fine" | dashboards and alerts on latency, locks, lag, disk |
| find out the disk is full when it stops | alert at 80% and on days-to-full |
| default `max_connections` with 50 app instances | pool sizing, an external pooler |
| never look at slow queries | slow-query log reviewed weekly |
| upgrade the major version on Friday | tested, scheduled, with a rollback plan |
| tribal knowledge for incidents | runbooks and rehearsal |
| over-provisioned "just in case" | right-sized from metrics |
| ignore autovacuum | monitor bloat and long transactions |

---

#### 4. SQL & Code

PostgreSQL monitoring queries (not run):

```sql
-- top queries by total time
SELECT query, calls, round(total_exec_time::numeric, 0) AS total_ms, round(mean_exec_time::numeric, 2) AS mean_ms
FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 10;

-- connections by state and the oldest idle-in-transaction sessions
SELECT state, count(*) FROM pg_stat_activity GROUP BY state;
SELECT pid, now() - xact_start AS open_for, query FROM pg_stat_activity WHERE state = 'idle in transaction' ORDER BY xact_start LIMIT 5;

-- who is blocking whom
SELECT blocked.pid AS blocked_pid, blocking.pid AS blocking_pid, blocked.query AS blocked_query
FROM pg_stat_activity blocked JOIN pg_stat_activity blocking ON blocking.pid = ANY(pg_blocking_pids(blocked.pid));

-- cache hit ratio and bloat watch
SELECT sum(blks_hit) * 100.0 / nullif(sum(blks_hit) + sum(blks_read), 0) AS cache_hit_pct FROM pg_stat_database;
SELECT relname, n_live_tup, n_dead_tup FROM pg_stat_user_tables ORDER BY n_dead_tup DESC LIMIT 10;
```

Capacity arithmetic:

```kotlin
fun daysToFull(freeGb: Double, growthGbPerDay: Double) = if (growthGbPerDay <= 0) Double.POSITIVE_INFINITY else freeGb / growthGbPerDay
fun yearlyGrowthGb(rowsPerDay: Long, bytesPerRow: Int, indexFactor: Double = 1.5) = rowsPerDay * bytesPerRow * indexFactor * 365 / 1e9
```

Checks: `daysToFull(120.0, 4.0)` → `30.0` days: alert and plan now. `yearlyGrowthGb(1_000_000, 500)` → `273.75` GB a year (with a 1.5× index factor; the raw data alone is `182.5` GB).

Connection budget:

```kotlin
fun connectionBudget(dbMax: Int, instances: Int, poolPerInstance: Int, reserved: Int = 10): Pair<Int, Boolean> {
    val used = instances * poolPerInstance
    return used to (used <= dbMax - reserved)
}
```

Checks: `connectionBudget(100, 8, 10)` → `(80, true)`; `connectionBudget(100, 12, 10)` → `(120, false)`: shrink pools, add a pooler, or raise the limit (and memory).

Alert rules as data (checked in a unit test):

```kotlin
data class Metrics(val p95Ms: Int, val connPct: Int, val lagSec: Int, val diskPct: Int, val lastBackupAgeH: Int)

fun alerts(m: Metrics, p95TargetMs: Int = 200, rpoHours: Int = 24): List<String> = buildList {
    if (m.p95Ms > p95TargetMs) add("p95 latency high")
    if (m.connPct > 80) add("connections near limit")
    if (m.lagSec > 30) add("replication lag")
    if (m.diskPct > 80) add("disk filling")
    if (m.lastBackupAgeH > rpoHours) add("backup older than RPO")
}
```

Checks: healthy `Metrics(80, 40, 1, 55, 6)` → `[]`; `Metrics(450, 92, 3, 85, 6)` → `[p95 latency high, connections near limit, disk filling]`; `Metrics(100, 30, 90, 40, 30)` → `[replication lag, backup older than RPO]`.

Maintenance commands (PostgreSQL, not run):

```sql
VACUUM (VERBOSE, ANALYZE) notes;                         -- reclaim space, refresh statistics
REINDEX INDEX CONCURRENTLY idx_notes_user;               -- rebuild a bloated index without blocking
ALTER TABLE events DETACH PARTITION events_2024_01;      -- archive old data cheaply
SET statement_timeout = '30s'; SET lock_timeout = '3s';  -- protective settings for maintenance sessions and the app
```

Find unused indexes (candidates to drop; check over a long period and on replicas too):

```sql
SELECT relname AS table, indexrelname AS index, idx_scan FROM pg_stat_user_indexes WHERE idx_scan = 0 ORDER BY pg_relation_size(indexrelid) DESC;
```

Health endpoint in the app (readiness checks the database cheaply):

```kotlin
fun Route.health(ds: DataSource) {
    get("/ready") { runCatching { ds.connection.use { it.createStatement().execute("SELECT 1") } }
        .onSuccess { call.respondText("ok") }.onFailure { call.respond(HttpStatusCode.ServiceUnavailable) } }
}
```

On a phone, "operations" means: database size (`adb shell ls -l /data/data/<pkg>/databases`), migration success rate and crash rate after releases, slow-query traces with Room's query callback, and trimming caches (`MOB 11`, `MOB 15`).

---

#### 5. Numbers & Limits

| Item | Rule of thumb |
|---|---|
| Slow-query threshold | 100–500 ms for OLTP; review weekly |
| Cache hit ratio | > 99% for OLTP working sets |
| Connections | stay under ~80% of `max_connections` |
| Disk | alert at 80%; keep ≥ 20% free for maintenance and growth |
| Replication lag | warn > 5 s; page > 60 s |
| Long transaction | alert > 5 minutes |
| Dead tuples | investigate when > 20% of live rows |
| Backup age | below the RPO |
| Upgrade support window | stay on a supported major version; plan upgrades yearly |
| Right-sizing | 40–70% average CPU/memory use for steady workloads |

---

#### 6. Common Mistakes & Edge Cases

1. No monitoring until the first outage.
2. Alerts that nobody acts on (noise).
3. Disk filling from WAL, logs or an idle replication slot.
4. Connection storms after a deploy or failover.
5. Long-running idle transactions blocking vacuum and DDL.
6. Skipping `ANALYZE` after bulk loads.
7. Upgrading without testing extensions and plans.
8. Not knowing what the managed service handles.

Edge cases: a sudden query-plan change after statistics change; transaction-ID wraparound risk on huge tables; burst credits (cloud IOPS) running out; maintenance windows clashing with traffic peaks; replicas used for reporting causing replication conflicts; clock changes and time-zone settings.

---

#### 7. Say This in the Interview

1. "I monitor latency percentiles, slow queries, connections vs the limit, lock waits, replication lag, disk growth, cache hit ratio and backup age, with alerts tied to action."
2. "I find the worst queries by total time in `pg_stat_statements` and fix them with indexes or rewrites, measuring before and after."
3. "I size the connection pool so `servers × pool` fits under the database limit, and use a pooler for many instances."
4. "I forecast disk and traffic growth and plan before the limit; routine vacuum, analyze, reindex and archiving keep tables healthy."
5. "I keep runbooks for lock pile-ups, connection exhaustion, full disk and replica lag, and test upgrades and failovers before production."

---

#### 8. Quick Check

1. Name five database metrics worth alerting on.
2. How do you find the queries that cost the most?
3. Why do long idle-in-transaction sessions hurt?
4. What does `daysToFull` tell you?

<details>
<summary>Answers</summary>

1. For example: p95 latency, connections vs limit, lock waits, replication lag, disk usage, backup age.
2. Sort `pg_stat_statements` (or the slow-query log) by total time.
3. They hold locks and snapshots, blocking vacuum, DDL and other transactions.
4. How long until storage is full at the current growth rate: when to act.

</details>

---

#### 9. Practice

**Interview questions**

1. The database is slow right now. What do you check, in order?
2. What do you monitor and alert on?
3. How do you plan capacity?
4. How do you upgrade a major version safely?
5. Connection exhaustion: causes and fixes?
6. What routine maintenance does PostgreSQL need?

**Hands-on**

1. Enable `pg_stat_statements` and the slow-query log locally and find the worst query of a load test.
2. Write the alert rules function and unit-test it with the three cases above.
3. Create a lock pile-up with two sessions and find the blocker with `pg_blocking_pids`.
4. Write a runbook for "disk is 90% full" and "replica lag 5 minutes".

**Remember:** monitor latency, locks, connections, lag, disk, cache hit, backup age · worst queries by total time · pool sizes under the limit · forecast days-to-full · routine vacuum/analyze/reindex/archive · test upgrades · write runbooks.
