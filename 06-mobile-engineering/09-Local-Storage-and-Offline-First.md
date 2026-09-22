# Local Storage & Offline-First

Roadmap topic 9 · Stage 3: Data & Background

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** offline-first means the local database isn't a cache of the truth — it **is** the truth, as far as the UI is concerned. The network's job is to keep that local truth in sync, not to hand data straight to the screen. This is the single idea that separates apps that feel solid on bad networks from ones that don't.

---

#### 1. Choosing the Storage — 🟢 Must Know

| Storage | Use for |
|---|---|
| Preferences / DataStore | Small key-value settings (a theme choice, a feature flag cache) |
| Room (SQLite) | Structured, queryable data — notes, messages, any real entity |
| Files | Large blobs — images, downloaded documents |
| In-memory cache | Short-lived, screen-scoped data that doesn't need to survive the process |

Deeper database internals live in `DB 21` (mobile databases).

---

#### 2. Room: Entities, DAOs, Observing as `Flow` — 🟢 Must Know

```kotlin
@Entity(tableName = "notes")
data class NoteEntity(@PrimaryKey val id: String, val title: String, val body: String)

@Dao
interface NoteDao {
    @Query("SELECT * FROM notes ORDER BY updatedAt DESC")
    fun getAllNotes(): Flow<List<NoteEntity>>   // observed — UI updates automatically on any change

    @Upsert
    suspend fun upsertAll(notes: List<NoteEntity>)
}
```

Returning a `Flow` from a DAO query means the UI automatically re-renders whenever the underlying table changes — no manual "refresh" call needed.

---

#### 3. Room Migrations — 🟢 Must Know

1. Every schema change needs a **migration**, and **every version in the wild must be able to upgrade** — a user on version 12 opening an app now at version 20 needs all the migrations in between to run in sequence.
2. Test migrations explicitly (topic `12`) — a broken migration corrupts or loses local data for real users.

---

#### 4. Offline-First — 🟢 Must Know

*The local database is the source of truth (topic `6`); the network keeps it in sync.*

```text
UI observes  ←  Room (source of truth)  ←  sync worker  ←  network
```

1. The UI never talks to the network directly — it observes the database.
2. A sync process (often WorkManager, topic `10`) fetches remote changes and writes them into the database; writing to the database is what makes them appear on screen.
3. This means the app works — reading, and often writing — even with no network at all.

---

#### 5. Cache Strategies — 🟢 Must Know

1. **Cache-first** — show local data immediately, refresh in the background.
2. **Network-first** — try the network first, fall back to cache on failure.
3. **Stale-while-revalidate** — show stale local data immediately, and refresh silently, updating the UI when fresh data arrives (a good default for most feeds).

---

#### 6. Sync — 🟢 Must Know

1. **Send local changes**: queue writes made offline, and push them when connectivity returns.
2. **Fetch remote changes**: usually "give me everything changed since timestamp/cursor X".
3. **Handle failures**: a failed sync should retry (`SD 22`), not silently drop the local change.

---

#### 7. Conflict Resolution — 🟢 Must Know

1. **Last-write-wins** — the most recent change (by timestamp) wins; simple, but can silently discard a user's edit.
2. **Merge rules** — combine both changes where possible (appending to a list, merging non-overlapping fields) — more correct, more work to design.
3. Decide this **per feature** — a note's title might be fine with last-write-wins; a shared shopping list's items probably need a merge rule.

---

#### 8. Never Block the Main Thread — 🟢 Must Know

Room enforces this by default — a query on the main thread throws unless you explicitly allow it (don't). All database and file work runs via coroutines on `Dispatchers.IO` (topic `3`).

---

#### 9. DataStore vs `SharedPreferences` — 🟡 Good to Know

DataStore is the modern replacement: asynchronous (no main-thread reads), transactional, and (in its typed form) schema-safe — prefer it over `SharedPreferences` for new code.

---

#### 10. Indexes and Query Performance — 🟡 Good to Know

The same indexing principles as any SQL database (`DB 5`) apply locally too — an unindexed query over thousands of local rows can visibly lag a screen.

---

#### 11. Encrypted Storage — 🟡 Good to Know

Sensitive local data (tokens, personal info) should be encrypted at rest — see topic `13` and `ARCH 11` for the security-architecture view.

---

#### 12. Large Data: Files vs Blobs — 🟡 Good to Know

Store large binary data (images, documents) as **files**, with only a path or reference stored in the database — storing large blobs directly in SQLite rows bloats the database and slows queries.

---

#### 13. Deletes and Tombstones — 🟡 Good to Know

A hard local delete doesn't tell the server anything. Sync needs to know what was deleted too — either an explicit "delete" sync event, or a **tombstone** (a marked-deleted row kept around briefly so the delete can propagate before being fully removed).

---

#### 14. Testing Room and Migrations — 🟡 Good to Know

Covered in topic `12` — an in-memory Room database for fast repository tests, and dedicated migration tests that actually run each migration against real sample data.

---

#### 15. iOS Equivalents — 🟡 Good to Know

Core Data and SwiftData play the same "local source of truth" role on iOS — see topic `16`.

---

#### 16. Common Interview Questions

1. **What does "offline-first" actually mean?**
   The local database is the source of truth the UI observes; the network's job is to keep that database in sync, not to feed the UI directly. The app works, at least for reads, without connectivity.
2. **How do you observe local data changes automatically?**
   A Room DAO query returning `Flow<List<T>>` — Room re-emits automatically whenever the underlying table changes, no manual refresh needed.
3. **How would you handle a sync conflict on a shared note?**
   Depends on the feature: last-write-wins is simple but can discard changes; a merge strategy (per-field, or operational) preserves more, at the cost of design complexity.
4. **Why do deletes need special handling in a sync system?**
   A plain local delete leaves no record for sync to notice — you need an explicit delete event or a tombstone so the deletion propagates to the server (and to other devices) too.
5. **Why must every Room migration path still work for old app versions?**
   Users update infrequently — the app must be able to migrate a database from any historical version straight to the current one.

---

#### 17. Common Mistakes

1. Feeding network results straight to the UI, treating the local database as a mere cache rather than the source of truth.
2. Forgetting to test a Room migration against real, populated data.
3. Handling deletes only locally, with no way for the server (or sync) to learn about them.
4. Doing file or database I/O on the main thread.
5. Storing large binary blobs directly in database rows instead of files.

---

#### 18. Related Topics

1. `3` Coroutines & Flow — `Flow`-based DAO queries
2. `6` App Architecture — the repository/source-of-truth pattern this builds on
3. `10` Background Work & Notifications — WorkManager as the usual sync mechanism
4. `DB 21` Mobile Databases — deeper database internals and mobile-specific detail
5. `SD 30` Mobile-Specific Topics — offline-first from the system design side

---

#### 19. Interview Must Remember

1. **Local database = source of truth.** UI observes it; the network syncs it.
2. **Room DAO `Flow` queries** auto-update the UI on any data change.
3. **Every historical schema version must still migrate correctly** — test migrations.
4. **Deletes need explicit sync handling** — a plain local delete alone doesn't propagate.
5. **Never touch the database or files on the main thread.**
