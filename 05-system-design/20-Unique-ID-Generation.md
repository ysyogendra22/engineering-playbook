# Unique ID Generation

Roadmap topic 20 · Stage 4: Scale (New topic)

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** every row, message, or order needs a unique ID. On one database that is easy. With many servers or shards, you must generate IDs without collisions and without a single bottleneck.

---

#### 1. Options — 🟢 Must Know

*Three common ways to create unique IDs.*

| | Auto-increment | UUID | Snowflake-style |
|---|---|---|---|
| Example | `1, 2, 3...` | `550e8400-e29b-...` | `1789234567890123` |
| Unique across servers? | No (one database) | Yes | Yes |
| Sortable by time? | Yes | No (v4 random) | Yes |
| Size | Small (8 bytes) | Large (16 bytes) | 8 bytes |
| Downside | Bottleneck; guessable | Random → worse index locality | Needs machine IDs and a clock |

---

#### 2. Auto-Increment — 🟢 Must Know

*The database counts up: 1, 2, 3.*

1. The database gives `1, 2, 3...`.
2. Simple and small. Great for a single database.
3. Problems at scale: one database is the bottleneck; with several shards you get **duplicate IDs**; IDs are **guessable** (`/users/101`, `/users/102`).

---

#### 3. UUID — 🟢 Must Know

*A random 128-bit ID that any server or app can create on its own.*

1. 128-bit random value. **Any server or client can generate one** without coordination.
2. Collisions are practically impossible.
3. Downsides: larger, and random values scatter inserts across the index (slower writes on big tables).
4. **UUIDv7** is time-ordered, which fixes the index problem.

**Mobile view:** an offline app can create a UUID on the phone, so a record has an ID before the server has ever seen it.

---

#### 4. Snowflake-Style IDs — 🟢 Must Know

*Build the ID from parts, so servers never collide.*

```text
| timestamp | machine ID | sequence number |
   (ms)       (which server)  (counter within the same ms)
```

1. Each server has a **machine ID** and its own counter, so no coordination is needed.
2. IDs are **roughly sorted by time**, which is good for feeds and indexes.
3. Fits in 64 bits.
4. Watch out for: clock going backwards, assigning unique machine IDs.

---

#### 5. Short Codes for a URL Shortener — 🟢 Must Know

*Turn a number into a short string.*

1. Generate a unique ID, then encode it in **base62** (`a–z`, `A–Z`, `0–9`).
2. 7 characters give about 3.5 trillion codes (62⁷).
3. Alternatives: random code + check for collisions, or a hash of the URL (must handle collisions).
4. Sequential IDs are guessable. Add randomness or a shuffle if URLs must not be guessable.

---

#### 6. Client-Generated IDs for Offline Apps — 🟡 Good to Know

*Mobile advantage.*

1. The app creates a **UUID** for a new item while offline.
2. It syncs later, and the ID stays the same.
3. It also makes **retries safe**: the server sees the same ID and doesn't create a duplicate (idempotency).

---

#### 7. Common Interview Questions

1. **How do you generate unique IDs across many servers?**
   UUIDs, or Snowflake-style IDs (timestamp + machine ID + sequence). Auto-increment only works on one database.
2. **UUID vs auto-increment?**
   UUID is unique everywhere and hard to guess but larger and unordered. Auto-increment is small and ordered, but a bottleneck and guessable.
3. **How would you generate short URLs?**
   Unique ID → base62. About 7 characters for trillions of codes.
4. **Why are sortable IDs useful?**
   Time-ordered inserts are faster on indexes, and you can sort or paginate by ID.
5. **Why not expose sequential IDs?**
   People can guess and enumerate other records.

---

#### 8. Common Mistakes

1. Auto-increment across multiple shards.
2. Random UUIDs as the primary key of a huge, write-heavy table (without considering v7).
3. Guessable IDs for private resources.
4. Ignoring clock problems in time-based IDs.
5. Hashing a URL with no collision handling.

---

#### 9. Related Topics

1. `19` Partitioning & Sharding
2. `22` Reliable Requests & External Services (idempotency)
3. `30` Mobile-Specific Topics (offline creation)
4. `32` Practice Designs (URL shortener)

---

#### 10. Interview Must Remember

1. **Auto-increment** = simple, one database. **UUID** = anywhere. **Snowflake** = sortable and distributed.
2. **Base62** encoding for short codes.
3. **Don't expose sequential IDs.**
4. **Client-generated IDs** help offline apps and safe retries.
