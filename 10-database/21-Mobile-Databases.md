# Mobile Databases

Roadmap topic 21 · Stage 7: Mobile · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** everything in Stages 1–3 of this folder — modeling, SQL, indexes, transactions, migrations — applies inside your phone too. The database is just embedded (`1`, item 4) instead of a network service, and every user's copy has to upgrade itself, alone, with no DBA watching over it.

---

#### 1. SQLite: the Embedded Database in Every Phone — 🟢 Must Know

SQLite runs **inside** the app's own process (`1`, item 4), reading and writing a local file — no server, no network. It's the foundation underneath both platforms' local persistence libraries (item 2).

---

#### 2. Room and Core Data / SwiftData — 🟢 Must Know

**Room** (Android) is a type-safe layer built directly on top of SQLite — entities, DAOs, and queries in Kotlin, with compile-time checking of your SQL. **Core Data** and **SwiftData** (iOS) play the equivalent role. Full implementation detail lives in `06-mobile-engineering/9` and `06-mobile-engineering/16`; this topic connects that concrete detail back to general database theory.

```kotlin
@Entity(tableName = "notes")
data class NoteEntity(@PrimaryKey val id: String, val title: String, val updatedAt: Long)

@Dao
interface NoteDao {
    @Query("SELECT * FROM notes ORDER BY updatedAt DESC")
    fun getAllNotes(): Flow<List<NoteEntity>>   // the same SQL fundamentals from topic 3, underneath
}
```

---

#### 3. Never Access the Database on the Main Thread — 🟢 Must Know

The same rule as `06-mobile-engineering/1`'s main-thread discipline, applied specifically to the database: any disk I/O (even a small local query) can be slow enough to jank the UI or trigger an ANR if done synchronously on the main thread. Room enforces this by default.

---

#### 4. Schema Versions and On-Device Migrations — 🟢 Must Know

*The mobile-specific twist on topic `10`'s migration discipline — genuinely harder here.*

**Every old app version, installed on a real user's device, must be able to upgrade its local schema on its own** — there's no DBA running a migration script; the migration code ships inside the app itself and runs automatically the first time the updated app opens against the old local database. A broken migration doesn't just fail loudly — it can silently corrupt or lose a real user's local data.

---

#### 5. Offline-First: the Local Database as Source of Truth — 🟢 Must Know

The single most distinctive mobile database pattern (`06-mobile-engineering/9`, `SD 30`): the local database **is** the source of truth for the UI; the network's job is to **sync** it, not to feed the UI directly. This is what makes the app usable through flaky, intermittent connectivity — a normal phone condition, not an edge case.

---

#### 6. Indexes and Query Design Apply on the Device Too — 🟢 Must Know

Topic `5`'s indexing principles are not just a "big server database" concern — a local table with a few thousand unindexed rows can visibly lag a screen on a phone's much more limited hardware. Design the local schema from the actual queries the app runs, exactly as `2`, item 4 recommends generally.

---

#### 7. Key-Value Settings Storage vs a Real Database — 🟢 Must Know

For simple settings (a theme preference, a feature flag cache), a lightweight key-value store (DataStore on Android) is more appropriate than a full relational database — reserve Room/SQLite for genuinely structured, queryable data (notes, messages, any real entity with relationships).

---

#### 8. Sync Design — 🟡 Good to Know

**Changes since a timestamp/cursor** (the same keyset-pagination idea from `3`, item 7, applied to sync), **conflict resolution** (last-write-wins or a merge rule, `16` item 9), and **deletes** — handled with **tombstones** (a marker for a deleted record, so the delete itself can sync, `06-mobile-engineering/9`).

---

#### 9. Encryption on Device — 🟡 Good to Know

**SQLCipher** (an encrypted SQLite variant) or platform-provided encrypted storage options protect local data at rest — relevant for genuinely sensitive local data, connecting to `18`'s "encryption at rest" principle and `06-mobile-engineering/13`'s mobile security guidance.

---

#### 10. Storing Large Data: Files vs Blobs — 🟡 Good to Know

The same principle from `2`, item 13, applied locally: store large binary data (downloaded images, documents) as **files**, with only a path or reference in the database — bloating local SQLite rows with large blobs slows queries and wastes app storage.

---

#### 11. Testing Database Code and Migrations — 🟡 Good to Know

An in-memory Room database for fast repository tests, and **dedicated migration tests** that actually run each migration against real sample data (`06-mobile-engineering/12`) — the mobile-specific application of topic `10`'s "test migrations on a copy of real data" principle, made even more important given item 4's stakes.

---

#### 12. Other Options and Their Status — 🟡 Good to Know

Realm and Firebase's local persistence are alternative options — **check each library's current support and maintenance status before choosing**, since this specific area of the mobile ecosystem changes over time.

---

#### 13. Local IDs Mapping to Server IDs — 🟡 Good to Know

When a record is created offline before ever reaching the server, it needs a **local ID** that later reconciles with the **server-assigned ID** once synced (`SD 20`) — a real design detail in any offline-first sync system, not an afterthought.

---

#### 14. Common Interview Questions

1. **Why is a broken Room/SQLite migration more dangerous on mobile than a broken server migration?**
   It ships inside the app and runs automatically on a real user's device, with no DBA supervising it — a failure can silently corrupt or lose that specific user's local data, and there's no way to intervene remotely.
2. **What makes "offline-first" the recommended default for mobile apps?**
   The local database is the source of truth the UI observes; the network syncs it in the background — this keeps the app working through the flaky, intermittent connectivity that's a normal phone condition, not a rare edge case.
3. **Do indexing principles from server databases apply to a local mobile database?**
   Yes — a local table with even a few thousand unindexed rows can visibly lag a screen, especially on more limited phone hardware; design local schema and indexes from the app's actual queries.
4. **How would you design sync for an offline-first notes app?**
   Track changes since a cursor/timestamp, choose a conflict resolution rule appropriate to the feature, and use tombstones so deletes propagate correctly — the same core ideas as server-side sync, applied locally.

---

#### 15. Common Mistakes

1. Querying the local database synchronously on the main thread.
2. Shipping a schema migration untested against real, populated sample data.
3. Feeding the UI from the network directly instead of treating the local database as the source of truth.
4. Storing large binary blobs (photos) directly in SQLite rows instead of as files.

---

#### 16. Related Topics

1. `06-mobile-engineering/9` Local Storage & Offline-First — full implementation-level detail
2. `06-mobile-engineering/16` iOS & Swift Essentials — Core Data and SwiftData
3. `10` Schema Migrations & Evolution — the general migration discipline this topic specialises for mobile
4. `SD 30` Mobile-Specific Topics — offline-first from the system design side

---

#### 17. Interview Must Remember

1. **SQLite is embedded** (`1`, item 4) — no server, runs inside the app's own process.
2. **Every old app version must self-migrate its local schema** — no DBA supervising it.
3. **Offline-first**: local database is the source of truth, network syncs it.
4. **Indexing and query design matter locally too** — phone hardware is more limited, not exempt from the same principles.
