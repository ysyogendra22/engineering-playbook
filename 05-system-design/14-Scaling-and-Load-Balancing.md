# Scaling & Load Balancing

Roadmap topic 14 · Stage 4: Scale

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** when one server can't handle the traffic, you add more servers and put a load balancer in front. For that to work, servers must be stateless, and you must remove single points of failure.

---

#### 1. Vertical vs Horizontal Scaling — 🟢 Must Know

*Vertical = a bigger machine. Horizontal = more machines.*

| | Vertical (scale up) | Horizontal (scale out) |
|---|---|---|
| How | More CPU / RAM on one server | More servers |
| Easy? | Yes, no code change | Needs a stateless design |
| Limit | Hardware limit, expensive | Almost unlimited |
| Failure | One server = single point of failure | Others keep working |

Typical path: start simple, scale up a bit, then scale out.

---

#### 2. Stateless Servers — 🟢 Must Know

*If any server can serve any request, you can add or remove servers freely.*

1. **Stateless** — the server keeps no user data between requests (see topic `01`).
2. **Stateful** problem: the user's session is in Server A's memory. If the next request goes to Server B, they are "logged out".
3. Fix: keep session/state in a **shared store** (Redis or the database), or inside a signed **token**.

```text
Users → Load Balancer → Server A ─┐
                        Server B ─┼→ Shared Redis / Database
                        Server C ─┘
```

---

#### 3. Load Balancer and Health Checks — 🟢 Must Know

*A traffic police officer that sends each request to a healthy server.*

1. Spreads requests across servers.
2. **Health check** — regularly pings each server (`/health`). A failing server is removed from rotation.
3. Lets you deploy or replace servers without downtime.
4. The load balancer itself must not be a single point of failure (run more than one).

---

#### 4. Single Points of Failure (SPOF) — 🟢 Must Know

*Ask about every box: "If this dies, does the whole system stop?"*

| Component | How to remove the SPOF |
|---|---|
| App server | Several servers behind a load balancer |
| Load balancer | A redundant pair |
| Database | Replica with failover (topic `18`) |
| Cache | Cache cluster |
| Data center | Multiple zones or regions |

---

#### 5. Finding the Bottleneck — 🟢 Must Know

1. Ask: **what breaks first when traffic grows?**
2. It is usually the **database**, before the app servers (app servers are easy to add).
3. Typical order of improvement: **index → cache → read replicas → sharding**.
4. Measure (CPU, memory, DB time, queue length) before you scale.

---

#### 6. Load Balancing Algorithms, Sticky Sessions, L4 vs L7 — 🟡 Good to Know

1. **Round robin** — servers take turns. **Least connections** — the least busy server gets the next request. **Hashing** — the same client goes to the same server.
2. **Sticky sessions** — the same user always goes to the same server. Simple but uneven, and a failure loses the session. Prefer stateless.
3. **L4** — routes by IP and port (fast, simple). **L7** — routes by URL, headers, or cookies (smarter, can do `/api` vs `/images`).

---

#### 7. Reverse Proxy, API Gateway, Auto-scaling — 🟡 Good to Know

1. **Reverse proxy** — sits in front of servers (Nginx). Handles TLS, compression, caching.
2. **API gateway** — one entry point for auth, rate limiting, and routing to services (topic `26`).
3. **Auto-scaling** — add or remove servers automatically based on CPU or request count.

---

#### 8. Common Interview Questions

1. **Vertical vs horizontal scaling?**
   Bigger machine vs more machines. Horizontal scales further and survives failures, but needs stateless servers.
2. **Traffic grows 10×. What do you change, in order?**
   Add servers behind a load balancer (stateless), add caching, indexes and read replicas, then partition the database if still needed.
3. **Why must servers be stateless?**
   So any server can handle any request, and you can add or remove servers freely.
4. **What does a load balancer do?**
   Distributes requests, runs health checks, and removes unhealthy servers.
5. **What are single points of failure? How do you remove them?**
   Any component whose failure stops the system. Add redundancy.
6. **Where do you store sessions with many servers?**
   Shared store (Redis) or in a token.

---

#### 9. Common Mistakes

1. Storing session state in server memory.
2. One load balancer or one database, with no redundancy.
3. Scaling app servers when the database is the bottleneck.
4. Scaling before measuring.
5. Relying on sticky sessions.

---

#### 10. Related Topics

1. `01` Client, Server & Request Flow (stateless)
2. `15` Caching
3. `18` Replication
4. `19` Partitioning & Sharding
5. `26` Service Boundaries & Architecture

---

#### 11. Interview Must Remember

1. **Horizontal scaling needs stateless servers.**
2. **Load balancer** = spread traffic + health checks.
3. **Find and remove every SPOF.**
4. The **database is usually the first bottleneck.**
5. Improvement order: **index → cache → replicas → sharding.**
