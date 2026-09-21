# Follow-Up Topics

Roadmap topic 33 · Stage 8: Interview

**Marks:** 🟡 Good to Know (all topics here) · (New) added beyond the original roadmaps

**In simple words:** advanced ideas that senior interviewers sometimes ask. Learn them **after** you are comfortable with the core designs. At this level, know what each one is for, not how to implement it.

---

#### 1. Leader Election and Consensus — 🟡 Good to Know

1. Many machines must agree on **one leader** or one value, even when some fail.
2. **Consensus algorithms** (Raft, Paxos) do this. Know the **purpose only**.
3. Used in tools like ZooKeeper and etcd, and in databases for failover.
4. Skip the proofs and implementation details.

---

#### 2. Distributed Locks, Leases, Fencing Tokens — 🟡 Good to Know

1. **Distributed lock** — only one machine works on a resource at a time (for example, run a job on one server).
2. **Lease** — a lock that **expires automatically**, so a crashed holder doesn't block forever.
3. Problem: a slow holder (long pause) wakes up after its lease expired and still writes.
4. **Fencing token** — a number that increases with every lock. The storage rejects writes with an older token.

---

#### 3. Multi-Region Design — 🟡 Good to Know

1. **Active–passive** — one region serves traffic; another is a standby for disaster recovery. Simpler.
2. **Active–active** — several regions serve traffic. Lower latency and better availability, but data conflicts and consistency are hard.
3. Route users to the nearest region (DNS/geo routing).

---

#### 4. Large Data Migrations — 🟡 Good to Know

Moving to a new database or schema without downtime:

```text
1. Backfill      copy old data to the new store
2. Dual-write    write to both old and new
3. Validate      compare old and new
4. Cut over      switch reads to the new store
5. Clean up      stop writing to the old one, remove it later
```

Always keep a way to roll back.

---

#### 5. Search Basics — 🟡 Good to Know (New)

1. **Inverted index** — maps each word to the documents that contain it (like a book index).
2. Search engines (Elasticsearch, OpenSearch) add ranking and text processing (stemming, typo tolerance).
3. The search index is a **copy** of your data, updated asynchronously from the main database.

---

#### 6. Geospatial — 🟡 Good to Know (New)

*"Find places or drivers near me."*

1. **Geohash** — turns a location into a string; nearby places share a prefix.
2. **Quadtree** — splits the map into smaller squares where there is more data.
3. Query the cell that contains the user plus its neighbors, then sort by exact distance.

---

#### 7. Bloom Filter, HyperLogLog, Trie — 🟡 Good to Know (New)

| Structure | What it does | Trade-off |
|---|---|---|
| **Bloom filter** | Says "definitely not in the set" or "maybe in the set" | Small memory, false positives possible. Used to avoid useless lookups (cache penetration) |
| **HyperLogLog** | Counts approximate unique items (unique visitors) | Tiny memory, small error |
| **Trie** | Tree of characters for prefix lookup | Used for autocomplete |

---

#### 8. Batch vs Stream Processing — 🟡 Good to Know (New)

1. **Batch** — process a large set of data at intervals (nightly reports).
2. **Stream** — process events continuously as they arrive (live fraud detection).
3. Names only: Kafka for the event stream, Spark/Flink for processing.

---

#### 9. Clocks and Ordering — 🟡 Good to Know

1. Clocks on different machines **differ** (clock skew), so timestamps can't fully order events.
2. **Logical clocks** and sequence numbers give a consistent order without relying on time.
3. Be careful with "last write wins" based on client timestamps.

---

#### 10. CQRS — 🟡 Good to Know

1. **Command Query Responsibility Segregation:** separate the model for **writes** from the model for **reads**.
2. Example: write to the main database, and update a read-optimized copy (a search index or feed cache) through events.
3. Name-level only for now.

---

#### 11. Common Interview Questions

1. **Why do we need leader election?**
   So one node coordinates (writes, jobs) and another takes over safely when it fails.
2. **What is a fencing token?**
   An increasing number that lets storage reject writes from an old lock holder.
3. **Active–passive vs active–active?**
   A standby region vs several regions serving traffic (with harder data conflicts).
4. **How do you migrate a large database with no downtime?**
   Backfill, dual-write, validate, cut over, clean up.
5. **How would you find nearby drivers?**
   Geohash or quadtree cells for the user and neighbors, then sort by distance.
6. **What is a Bloom filter used for?**
   A quick "definitely not present" check to avoid unnecessary lookups.

---

#### 12. Common Mistakes

1. Learning these before the core topics.
2. Trying to memorise consensus algorithm details.
3. Using a distributed lock with no expiry (lease).
4. Migrating in one step with no validation or rollback.
5. Trusting clocks across machines.

---

#### 13. Related Topics

1. `15` Caching (Bloom filter, cache penetration)
2. `18` Replication (failover)
3. `23` Consistency & CAP
4. `29` Backup, Recovery, Security & Cost (multi-region, RPO, RTO)
5. `32` Practice Designs (autocomplete, nearby places, crawler)

---

#### 14. Interview Must Remember

1. Know the **purpose** of consensus, locks, leases, and fencing tokens.
2. **Migration:** backfill → dual-write → validate → cut over.
3. **Geohash/quadtree** for location, **inverted index** for search.
4. **Bloom filter / HyperLogLog / trie:** what each is for.
5. **Don't trust clocks** across machines.
