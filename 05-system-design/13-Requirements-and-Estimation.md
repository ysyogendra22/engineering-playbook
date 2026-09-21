# Requirements & Estimation

Roadmap topic 13 · Stage 4: Scale

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) added beyond the original roadmaps

**In simple words:** before drawing boxes, find out what you are building and how big it must be. Ask questions, then do quick math, but only the math that changes the design.

---

#### 1. Functional vs Non-Functional Requirements — 🟢 Must Know

*Functional = what the system does. Non-functional = how well it does it.*

| Functional | Non-functional |
|---|---|
| Upload a photo | Photo loads in under 300 ms |
| Follow a user | 99.9% available |
| See a feed | Never lose an uploaded photo |
| Send a message | Handles 10M users |

Common non-functional needs: **latency, availability, durability, scalability, consistency, security, cost**.

---

#### 2. Scope and Exclusions — 🟢 Must Know

*You can't design everything in 45 minutes. Agree on the scope.*

1. Ask: who are the users? What are the 2–3 main flows? How many users? Mobile, web, or both?
2. Say what is **out of scope** ("no video in v1, no admin panel").
3. Confirm the scope with the interviewer before designing.

---

#### 3. Users and Traffic — 🟢 Must Know

*Turn users into requests per second.*

1. **DAU** — daily active users. **Concurrent users** — online at the same moment (much smaller than DAU).
2. **QPS** (queries per second) = requests per day ÷ 86,400.
3. **Peak traffic** is usually 2–10× the average. Design for the peak.

```text
10M DAU × 10 requests/day = 100M requests/day
100M ÷ 86,400 ≈ 1,200 QPS average
Peak ×5 ≈ 6,000 QPS
```

---

#### 4. Read-Heavy vs Write-Heavy — 🟢 Must Know

*The read:write ratio shapes the design.*

1. **Read-heavy** (feeds, product pages, URL redirects): use caching, replicas, CDN.
2. **Write-heavy** (logs, chat, sensor data): use queues, partitioning, write-friendly storage.
3. Ask for the ratio, or estimate it (a feed is often 100 reads to 1 write).

---

#### 5. Storage and Bandwidth — 🟢 Must Know

*Estimate how much data you store and how much you send.*

```text
Storage   = records × size per record × retention
Bandwidth = requests per second × size per response
```

```text
1M photos/day × 2 MB      = 2 TB/day
2 TB/day × 365            ≈ 730 TB/year
2 TB/day ÷ 86,400 seconds ≈ 23 MB/s upload
```

1. Round numbers. Precision is not the goal.
2. State your assumptions out loud.
3. The result tells you: one database enough, or storage in object storage, or sharding needed?

---

#### 6. Latency vs Throughput, Percentiles — 🟢 Must Know

*Speed of one request versus how many you can handle. Use percentiles, not averages.*

1. **Latency** — time for one request (ms). **Throughput** — requests handled per second.
2. **p50** — half of the requests are faster than this. **p95 / p99** — the slowest 5% / 1%.
3. **Averages hide slow users.** Set targets on p95 or p99.

---

#### 7. Availability vs Durability — 🟢 Must Know

*Up and answering versus never losing data. They are not the same.*

1. **Availability** — the system is up and answering.
2. **Durability** — saved data is not lost.
3. They are different: a system can be down (unavailable) yet lose no data (durable).

| Uptime | Downtime per year |
|---|---|
| 99% | ~3.7 days |
| 99.9% | ~8.8 hours |
| 99.99% | ~53 minutes |
| 99.999% | ~5 minutes |

---

#### 8. Numbers to Remember — 🟡 Good to Know (New)

*A few round numbers help you estimate fast.*

```text
1 day ≈ 86,400 s ≈ 100K s        1M requests/day ≈ 12 QPS
1 KB × 1M = 1 GB                 1 MB × 1M = 1 TB
Memory read      ~100 ns
SSD read         ~100 µs
Same data center round trip ~0.5 ms
Across continents           ~150 ms
```

Use them to judge quickly: memory is far faster than disk, disk far faster than the network.

---

#### 9. Common Interview Questions

1. **Estimate QPS and storage for a photo app with 10M users.**
   Use the steps in sections 3 and 5. State assumptions and round.
2. **Functional vs non-functional requirements?**
   What it does vs how well (latency, availability, scale).
3. **Why p99, not the average?**
   The average hides the slowest users. p99 shows the worst common experience.
4. **Availability vs durability?**
   Up and answering vs data not lost.
5. **How do you decide if you need sharding?**
   Estimate data size and write QPS. If one database can't hold or handle it, consider sharding.

---

#### 10. Common Mistakes

1. Starting to draw before asking questions.
2. No stated assumptions.
3. Very exact math that doesn't change the design.
4. Designing for average traffic, not the peak.
5. Mixing up DAU and concurrent users.
6. Ignoring the read:write ratio.

---

#### 11. Related Topics

1. `14` Scaling & Load Balancing
2. `15` Caching
3. `19` Partitioning & Sharding
4. `31` Interview Answer Structure

---

#### 12. Interview Must Remember

1. **Clarify first:** functional, non-functional, scope, exclusions.
2. **QPS = requests/day ÷ 86,400.** Peak is 2–10× average.
3. **Read-heavy vs write-heavy** decides the design.
4. **Storage = records × size × retention.**
5. Use **p95 / p99**, not the average.
6. Estimate **only what changes the design.**
