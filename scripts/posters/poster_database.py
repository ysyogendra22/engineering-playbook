from poster_lib import *
from poster_svg import *

btree = """<svg viewBox="0 0 330 130" width="300"><g fill="none" stroke="#27479b" stroke-width="2">
<rect x="125" y="6" width="80" height="26" rx="3"/><rect x="20" y="52" width="80" height="26" rx="3"/><rect x="125" y="52" width="80" height="26" rx="3"/><rect x="230" y="52" width="80" height="26" rx="3"/>
<path d="M150 32 L70 52 M165 32 L165 52 M180 32 L260 52"/></g>
<g fill="none" stroke="#b3261e" stroke-width="2"><rect x="10" y="98" width="100" height="24" rx="3"/><rect x="115" y="98" width="100" height="24" rx="3"/><rect x="220" y="98" width="100" height="24" rx="3"/><path d="M60 78 L60 98 M165 78 L165 98 M270 78 L270 98"/></g>
<g font-size="15" text-anchor="middle"><text x="165" y="25">50 | 120</text><text x="60" y="71">10 | 30</text><text x="165" y="71">60 | 90</text><text x="270" y="71">130 | 160</text>
<text x="60" y="115">leaf rows →</text><text x="165" y="115">leaf rows →</text><text x="270" y="115">leaf rows →</text></g></svg>"""

repl = """<svg viewBox="0 0 330 110" width="300"><g fill="#fff" stroke="#17703a" stroke-width="2.2"><rect x="8" y="35" width="90" height="40" rx="6"/></g>
<g fill="#fff" stroke="#27479b" stroke-width="2"><rect x="200" y="6" width="120" height="30" rx="6"/><rect x="200" y="42" width="120" height="30" rx="6"/><rect x="200" y="78" width="120" height="30" rx="6"/></g>
<g stroke="#444" stroke-width="2" fill="none"><path d="M98 50 L198 22 M98 55 L198 57 M98 62 L198 92"/></g>
<g font-size="15"><text x="22" y="52">LEADER</text><text x="26" y="68" font-size="13">writes</text><text x="228" y="26" font-size="13">follower</text><text x="228" y="62" font-size="13">follower</text><text x="206" y="98" font-size="12">lag = stale reads</text><text x="120" y="40" font-size="13" fill="#b3261e">WAL</text></g></svg>"""

cache = """<svg viewBox="0 0 330 100" width="300"><g fill="#fff" stroke-width="2"><rect x="6" y="34" width="62" height="32" rx="6" stroke="#444"/><rect x="130" y="6" width="74" height="32" rx="6" stroke="#b3261e"/><rect x="130" y="62" width="74" height="32" rx="6" stroke="#27479b"/></g>
<g stroke="#444" stroke-width="2" fill="none"><path d="M68 44 L130 24 M68 56 L130 78"/><path d="M204 22 L260 22"/><path d="M204 78 L260 78"/></g>
<g font-size="15"><text x="14" y="55">app</text><text x="140" y="27">cache</text><text x="144" y="83">DB</text><text x="268" y="27" font-size="14">hit</text><text x="268" y="83" font-size="14">miss</text></g></svg>"""

expand = flow(["expand", "migrate", "contract"], ["#27479b", "#17703a", "#b3261e"])

boxes = [
 box(1, "Landscape", "r", ul(["Relational (**PostgreSQL**) – default", "Key-value (Redis)", "Document (MongoDB)", "Wide-column (Cassandra)", "Graph (Neo4j)", "Time-series, Search, Vector", "Mobile: **SQLite** / Room"]) +
      callout("Start with ONE Postgres.\nAdd stores only for a measured need.", "")),
 box(2, "Data Modeling", "g", ul(["Design from the **queries**", "Surrogate PK + `UNIQUE` natural key", "`FK`, `NOT NULL`, `CHECK`: bad data can't exist", "3NF first, denormalize a hot path", "Money = **cents**, time = **UTC**", "`NULL` = unknown → `IS NULL`", "Many-to-many → join table"])),
 box(3, "SQL Basics", "b", h3("Execution order", "b") + p("`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`") + ul(["`LEFT JOIN` + `COUNT(b.id)` keeps zeros", "`NOT EXISTS` beats `NOT IN` (NULLs)", "Keyset paging, not `OFFSET`", "Always parameters, never concat", "No `WHERE` = whole table!"])),
 box(4, "Advanced SQL", "p", pre("""SELECT * FROM (
 SELECT *, ROW_NUMBER() OVER (
   PARTITION BY user_id
   ORDER BY created_at DESC) rn
 FROM orders) WHERE rn = 1;""") + ul(["Top-N per group, dedupe, latest", "`LAG` / running `SUM`", "CTE `WITH` = readable steps", "Gaps & islands: `day - ROW_NUMBER`"])),

 box(5, "Indexes (B-tree)", "r", btree + ul(["Sorted + shallow: depth 3–4 for 1B rows", "Equality cols first, range / sort last", "Leftmost prefix rule", "Skipped: `f(col)`, `LIKE '%x'`, type mismatch", "Every index slows writes (~2.8× for 3)", "Index your foreign keys"])),
 box(6, "Query Performance", "g", ul(["measure → `EXPLAIN ANALYZE` → fix one → measure", "Seq scan vs index: ~**500×**", "`OFFSET` 190k vs keyset: ~**150×**", "N+1: 101 queries → 1 join / `IN`", "`SELECT *`, no `LIMIT` = waste", "Pool ≈ QPS × query secs"]) + callout("p95 matters, not the average", "g")),
 box(7, "Storage Internals", "b", ul(["**WAL**: log first, data later", "Crash recovery = replay the log", "Buffer pool keeps hot pages", "B-tree engine: mixed OLTP", "LSM tree: heavy writes", "Column store: analytics", "MVCC → needs vacuum"])),
 box(8, "Transactions & ACID", "p", table(None, [["**A**tomic", "all or nothing"], ["**C**onsistent", "constraints hold"], ["**I**solated", "no interference"], ["**D**urable", "survives crash"]]) +
      pre("""UPDATE seats SET held_by = :u
 WHERE id = :id AND held_by IS NULL;
-- 1 row => you got it""") + mut("Short tx. No API calls inside.")),

 box(9, "Concurrency", "r", table(["Level", "Anomalies left"], [["Read committed (PG)", "non-repeatable, phantom"], ["Repeatable read", "write skew"], ["Serializable", "none → retry"]]) +
      ul(["Lost update → atomic `UPDATE`", "Double booking → `UNIQUE`", "Edits → `version` column", "Hot section → `FOR UPDATE`", "Deadlock → same lock order + retry"])),
 box(10, "Migrations", "g", expand + ul(["Versioned scripts, never edit applied", "dual-write → backfill in batches", "`lock_timeout`, `CONCURRENTLY`", "Fix forward, not rollback", "Old app versions still run!"]) + callout("Never rename in one deploy", "g")),
 box(11, "Choosing & NoSQL", "b", ul(["Ask: shape, queries, consistency, scale", "Model NoSQL by **access pattern**", "Embed what is read together", "You lose joins & ad-hoc queries", "Search / vector = derived copy", "Managed unless you have scale + people"])),
 box(12, "Caching & Redis", "p", cache + ul(["Cache-aside: read → miss → DB → set", "Write: DB first, then `DEL` key", "TTL + **jitter**; single-flight", "Redis: string, hash, list, set, zset", "Never the only copy"])),

 box(13, "Replication & HA", "r", repl + ul(["Async can lose the lag window", "Read-your-writes needs care", "Failover: freshest + quorum + fencing", "**Replica ≠ backup**"])),
 box(14, "Sharding & CAP", "g", ul(["Last resort: index → cache → replica → bigger box → partition → shard", "Key: high cardinality, even, in main query", "`hash % N`: ~**80%** keys move", "Consistent hashing: ~**20%**", "Partition → pick C **or** A", "Quorum: **R + W > N**", "Saga + outbox + idempotency key"])),
 box(15, "Backup & Security", "b", ul(["Set **RPO / RTO** first", "3-2-1, off-site, immutable", "PITR = base backup + WAL", "Time your restore (1 TB ≈ 83 min)", "Parameterized queries only", "Least-privilege DB users", "TLS, private net, RLS for tenants"])),
 box(16, "Mobile (Room)", "p", ul(["Never on main thread", "Local DB = source of truth", "Client **UUID** + `dirty` flag", "Tombstone for deletes", "Cursor saved **after** the page", "Migrate from every old version", "`MigrationTestHelper`"]) + callout("Test the offline path", "")),

 box(0, "Numbers to Remember", "o", table(["Thing", "Value"], [["Memory / SSD / DC trip / HDD", "100 ns / 100 µs / 0.5 ms / 10 ms"], ["Cache latency", "hit×cache + miss×(cache+db): 95%, 1/50 ms → 3.5 ms"], ["Failover loss (async)", "lag × write rate: 2 s × 500/s = 1,000 tx"], ["Storage", "rows × bytes × 1.5 × replicas; 1M×500 B/day ≈ 274 GB/yr"], ["Requests", "users × req ÷ 86,400; peak 3–10×"], ["Alerts", "conn > 80% · disk > 80% · lag > 5–60 s · tx > 5 min"]]), 2),
 box(0, "Golden Rules", "t", ul(["One source of truth", "Constraints in the DB", "Measure before indexing", "Atomic update, not read-modify-write", "Test your restores", "Expand → migrate → contract"], ok=True)),
 box(0, "Say Out Loud", "r", '<div class="big">"I start with Postgres,<br>design from the queries,<br>and add only what I can measure."</div>' + callout("Think: requirements → schema → indexes\n→ concurrency → scale → backups", "b")),
]
meta = dict(left="Measure &gt; Guess<br>Constraints = Safety", right="Model. Query. Index.<br>Repeat! ☺", title="<b>DATABASE</b> CHEATSHEET", sub="for <u>FAANG interviews</u> · 2026")
if __name__ == "__main__":
    import sys; print(render(page(meta, boxes), sys.argv[1]))
