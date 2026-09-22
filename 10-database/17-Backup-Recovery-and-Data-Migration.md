# Backup, Recovery & Data Migration

Roadmap topic 17 · Stage 5: Operating

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** a backup you've never restored is a guess, not a plan. This topic is about the two numbers that actually define a recovery plan — how much data you can afford to lose, and how long you can afford to be down — and moving data safely without either one.

---

#### 1. Backups Stored Away, Restores Tested — 🟢 Must Know

Backups kept in a **separate location** from the live database (a different region, a different account) — a backup stored next to the thing it's backing up doesn't protect against the failure that takes out both at once. **Test the restore, regularly** — an untested backup is only a guess that it would actually work (`SD 29`).

---

#### 2. RPO and RTO — 🟢 Must Know

*The two numbers that define a real recovery plan.*

```text
   last good backup          disaster           service restored
────────────●──────────────────✕─────────────────────●──────────►
            |←──── RPO ───────→|←────── RTO ─────────→|
```

1. **RPO** (recovery point objective) — how much **data** you can afford to lose, measured in time (5 minutes of writes, an hour of writes).
2. **RTO** (recovery time objective) — how long you can afford to be **down**.

Both should be explicit, agreed numbers with the business — not assumed or left vague.

---

#### 3. Point-in-Time Recovery — 🟢 Must Know

Using the write-ahead log (`7`, item 2), a database can be restored to **any specific moment**, not just to the last full backup — critical for recovering from a mistake ("restore to right before that bad `DELETE` ran") rather than only from a hardware failure.

---

#### 4. Replication Is Not a Backup — 🟢 Must Know

*Repeated deliberately — it's that important, and it's the single most common confusion in this topic.*

A replica (`14`) copies mistakes too, usually within seconds. A real backup is a separate, point-in-time, independently-stored copy.

---

#### 5. Logical vs Physical Backups — 🟡 Good to Know

**Logical** — a backup of the actual data (as SQL statements or a portable export), restorable to a different database version, but generally slower to create and restore. **Physical** — a backup of the raw underlying files, faster, but usually tied to the exact same database version and configuration.

---

#### 6. Backup Encryption and Retention — 🟡 Good to Know

Backups need the **same** security care as the live database — encryption, access control — since a backup is a full copy of everything, including anything sensitive. **Retention rules** decide how long backups are kept, balancing recovery needs against storage cost and (for personal data) privacy obligations.

---

#### 7. Disaster Recovery — 🟡 Good to Know

**Multi-AZ** (surviving one data center failing) is the standard default for most production systems. **Multi-region** (surviving a whole region failing) is far more complex and costly — reserved for requirements that genuinely justify it (`ARCH 12`).

---

#### 8. Moving Data Between Databases Without Downtime — 🟡 Good to Know

A live migration to a new database uses **dual writes** (write to both old and new during the transition), **change data capture** (streaming changes from old to new, `20` item 5), and thorough **validation** before fully cutting over (`SD 33`) — the same expand-and-contract discipline from schema migrations (topic `10`), applied to an entire database move.

---

#### 9. Deleting Data on Request — 🟡 Good to Know

Privacy regulations often require the ability to delete a specific user's data completely — including from **backups**, which is genuinely hard, since backups are typically immutable snapshots. Plan for this explicitly (short retention windows, or a documented process for handling deletion requests against historical backups) rather than discovering the problem only once a real request arrives.

---

#### 10. Common Interview Questions

1. **What's the difference between RPO and RTO?**
   RPO is how much data you can afford to lose (measured in time since the last good backup). RTO is how long you can afford to be down. Both should be explicit, agreed numbers, not assumptions.
2. **Why isn't replication a backup?**
   A replica copies mistakes and corruption too, usually within seconds — it protects against a machine failing, not against a bad delete or data corruption. A real backup is a separate, point-in-time, independently stored copy.
3. **How would you recover from an accidental `DELETE` that already replicated everywhere?**
   Point-in-time recovery, using the write-ahead log to restore the database to the moment right before the bad delete ran, rather than relying on a replica (which has the same bad state) or only the last full backup (which may be too old).
4. **How do you know your backups actually work?**
   Test the restore process regularly, in a real environment — an untested backup is only an assumption, not a verified recovery capability.

---

#### 11. Common Mistakes

1. Never actually testing a restore.
2. Backups stored in the same location/account as the live database.
3. Treating replication as sufficient disaster recovery.
4. No agreed RPO/RTO, discovered only during a real incident when it's too late to plan calmly.
5. No plan for deleting a user's data from backups when a privacy request requires it.

---

#### 12. Related Topics

1. `SD 29` Backup, Recovery, Security & Cost — the same core content, first pass
2. `14` Replication & High Availability — the contrast point for "replication is not a backup"
3. `7` Storage Engines & Internals — the WAL that makes point-in-time recovery possible
4. `10` Schema Migrations & Evolution — the same expand-and-contract discipline applied here to whole-database moves

---

#### 13. Interview Must Remember

1. **Backups stored separately, restores tested regularly.**
2. **RPO** = data you can lose. **RTO** = time you can be down. Both explicit numbers.
3. **Point-in-time recovery** uses the WAL to restore to any specific moment.
4. **Replication is NOT a backup** — say this whenever the topic comes up.
