# Analytics, Warehouses & Data Pipelines

Roadmap topic 20 · Stage 6: Beyond the App Database

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** the database that runs your app and the database that powers your dashboards want fundamentally different things from their storage — and running both jobs on one system means one of them eventually loses. This topic is about keeping them separate, deliberately.

---

#### 1. Why Analytics Shouldn't Slow the App Database — 🟢 Must Know

*The single most important reason this topic exists.*

**OLTP** (the app's database, topic `1`) is optimised for many small, fast transactions. A large analytical query scanning millions of rows for a report can consume enough resources to visibly slow down the app's normal traffic — running analytics against a **separate system** (a read replica at minimum, ideally a dedicated warehouse) protects production performance.

---

#### 2. Row Store vs Column Store — 🟢 Must Know

```text
Row store (app database):      Column store (analytics):
id | name  | age                id column:   [1, 2, 3, ...]
1  | Asha  | 30                 name column: [Asha, Ravi, ...]
2  | Ravi  | 25                 age column:  [30, 25, ...]

Reading ONE full row is fast     Scanning ONE column across
(everything's together)          millions of rows is fast
                                  (only that column is read)
```

Analytical queries typically scan **one or a few columns across huge numbers of rows** (average age of all users) — a column store reads only the needed columns, skipping everything else, which is exactly why analytics-focused systems use this layout.

---

#### 3. Data Warehouse vs Data Lake — 🟢 Must Know

1. **Data warehouse** — structured, cleaned, schema-defined data, optimised for known analytical queries and reporting.
2. **Data lake** — raw data of many formats (structured, semi-structured, unstructured), stored cheaply, schema applied later when actually read ("schema on read" vs a warehouse's "schema on write").

---

#### 4. ETL vs ELT — 🟢 Must Know

**ETL** (extract, transform, load) — transform the data **before** loading it into the destination. **ELT** (extract, load, transform) — load the raw data first, transform it afterward inside the destination system. ELT has become more common as warehouses have gotten powerful enough to do heavy transformation work themselves.

---

#### 5. Change Data Capture (CDC) — 🟢 Must Know

Stream row-level changes **out of** the app database (often by reading the write-ahead log, `7` item 2) as they happen, in near real time — feeding a warehouse, a search index, or another system, without needing a slow, heavy batch query against the live production database (`ARCH 6`, item 9; `SD 26`).

---

#### 6. Star Schema — 🟡 Good to Know

A common warehouse modeling pattern: a central **fact table** (the actual events or transactions, one row per event) surrounded by **dimension tables** (descriptive context — customer, product, date) — designed specifically to make common analytical queries fast and intuitive to write.

---

#### 7. Batch vs Stream Processing — 🟡 Good to Know

**Batch** — process a large, accumulated set of data on a schedule (a nightly report). **Stream** — process data continuously, as it arrives (`SD 33`). CDC (item 5) is often the *source* that feeds a stream-processing pipeline.

---

#### 8. Lakehouse and Open Table Formats — 🟡 Good to Know

A newer category (names only) blending data lake flexibility with data warehouse structure and query performance, built on open table formats that add transactional guarantees on top of raw file storage — worth recognising as an evolving space, not needed in implementation depth.

---

#### 9. Reporting from a Replica vs a Warehouse — 🟡 Good to Know

For lightweight reporting needs, a **read replica** (`14`) of the app database may be sufficient — cheaper and simpler than a full warehouse. Move to a real warehouse once reporting needs grow (heavy transformation, long history, complex joins across many sources) beyond what a replica of the live schema comfortably supports.

---

#### 10. Data Quality Checks and Lineage — 🟡 Good to Know

Automated checks that data flowing through a pipeline meets expected quality (no unexpected nulls, values in expected ranges), and **lineage** — the ability to trace exactly where a given piece of data originated and what transformed it — both increasingly important as pipelines and their downstream consumers grow more numerous.

---

#### 11. Common Interview Questions

1. **Why shouldn't analytical queries run directly against the production app database?**
   OLTP databases are optimised for many small transactions; a large analytical scan can consume enough resources to visibly degrade normal app traffic — run analytics against a separate replica or warehouse instead.
2. **Why do column stores suit analytics better than row stores?**
   Analytical queries typically scan one or a few columns across huge numbers of rows — a column store reads only those columns, skipping the rest, while a row store would have to read every full row regardless of how many columns are actually needed.
3. **What is change data capture, and what's it used for?**
   Streaming row-level changes out of a database (often via its write-ahead log) in near real time, feeding a warehouse or another system without a slow, heavy batch query against production.
4. **ETL vs ELT — what changed to make ELT more common?**
   ETL transforms before loading; ELT loads raw data first and transforms afterward inside the destination. Modern warehouses became powerful enough to do the transformation work themselves efficiently, making ELT's simpler pipeline more attractive.

---

#### 12. Common Mistakes

1. Running heavy analytical queries directly against the production OLTP database.
2. Choosing a row-store-based system for a genuinely analytics-heavy workload.
3. Building a full CDC pipeline for a reporting need a simple read replica would have satisfied.
4. No data quality checks, letting a pipeline silently propagate bad data downstream.

---

#### 13. Related Topics

1. `1` Database Basics & Landscape — OLTP vs OLAP, introduced there
2. `7` Storage Engines & Internals — row store vs column store, and the WAL that CDC often reads from
3. `14` Replication & High Availability — read replicas as a lighter-weight reporting option
4. `SD 26` Service Boundaries & Architecture — CDC and the transactional outbox pattern

---

#### 14. Interview Must Remember

1. **Analytics runs on a separate system** from the production OLTP database.
2. **Column store for analytics** — scanning one column across millions of rows is the common analytical access pattern.
3. **CDC streams changes out of the database in near real time**, often from the WAL.
4. **Warehouse for structured, cleaned data. Lake for raw data of many formats.**
