# Interview Answer Structure

Roadmap topic 31 · Stage 8: Interview

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) added beyond the original roadmaps

**In simple words:** a system design interview is a conversation, not an exam. Follow the same steps every time, think out loud, and explain your trade-offs.

---

#### 1. The Steps — 🟢 Must Know

*Follow the same steps every time.*

```text
1. Clarify requirements and scope
2. Estimate (only what changes the design)
3. Define APIs and the data model
4. Draw a simple high-level design
5. Walk through the main flows
6. Deep-dive into bottlenecks and failures
7. Explain trade-offs and how it can grow
```

---

#### 2. Time Split for a 45-Minute Round — 🟢 Must Know (New)

*Split the time so you reach the deep dive.*

| Step | Time | What to do |
|---|---|---|
| Clarify | 5 min | Users, main flows, scale, what is out of scope |
| Estimate | 3–5 min | QPS, storage, read:write ratio |
| APIs + data model | 5–8 min | Main endpoints, core tables |
| High-level design | 10 min | Client, load balancer, servers, DB, cache, queue, storage |
| Deep dive | 10–15 min | The hardest part and failure cases |
| Trade-offs | 5 min | What you chose, what you gave up, how it evolves |

---

#### 3. Step Details — 🟢 Must Know

*What to do in each step.*

**1. Clarify:** ask about users, features, scale, platforms. State what is **out of scope**. (Topic `13`)

**2. Estimate:** DAU → QPS → storage. Round the numbers. Say what decision each number drives.

**3. APIs and data model:** 3–5 main endpoints, the main tables/entities, and the key queries.

**4. High-level design:** start **simple** (client → server → database), then add components as you justify them.

```text
Client → Load Balancer → App Servers → Cache
                                     → Database (+ replicas)
                                     → Queue → Workers
                                     → Object Storage → CDN
```

**5. Main flows:** walk through 1–2 key requests end to end (for example, "post a message" and "load the feed").

**6. Deep dive:** pick the most interesting problem: the hot key, the fan-out, double booking, the consistency issue. Go deeper here.

**7. Trade-offs:** name alternatives and why you did not choose them. Mention how the design grows 10×.

---

#### 4. Habits That Work — 🟢 Must Know

*Small habits that make answers stronger.*

1. **Start simple, then scale** where the numbers demand it.
2. **Say every trade-off out loud:** "I choose X because …; the downside is …".
3. For **every component** ask three questions:
   - What if it **fails**?
   - What if traffic is **10×**?
   - What if a request arrives **twice**?
4. **Don't name technology first.** Say what you need (a queue), then name an example (Kafka/SQS).
5. **Check in** with the interviewer: "Should I go deeper here, or move on?"
6. Use the whiteboard clearly: labelled boxes, arrows for data flow.

---

#### 5. Ready-Made Answer Points — 🟡 Good to Know

*Match the problem you notice with a standard tool.*

Common building blocks and when to bring them up:

| Problem you notice | Say |
|---|---|
| Too many reads | Cache, CDN, read replicas |
| Too many writes / too much data | Queue, sharding |
| Slow work in a request | Background job with a queue |
| Duplicates from retries | Idempotency key |
| Popular item overloads one node | Replicate hot keys, caching |
| Dependency failing | Timeout, circuit breaker, fallback |
| Users on flaky mobile networks | Offline support, retries, delta sync |

---

#### 6. Common Interview Questions

1. **How do you start a system design question?**
   Ask about users, main features, and scale. State what is out of scope. Estimate only what changes the design.
2. **How do you decide what to go deep on?**
   Pick the hardest part of that system (hot key, fan-out, double booking, consistency) and check in with the interviewer.
3. **What if you have never built this kind of system?**
   Use the same steps. Start simple, say what you need (a queue, a cache), then name an example and explain the trade-offs.
4. **What if the interviewer changes a requirement halfway?**
   Say which parts it affects, change only those, and explain the new trade-off. This is normal, not a failure.

---

#### 7. Common Mistakes

1. Jumping straight to the design without questions.
2. Starting with a complicated design.
3. Naming Kafka, microservices, or NoSQL without a reason.
4. Only describing the happy path (no failures).
5. Spending all the time on the diagram and none on the deep dive.
6. Not explaining trade-offs.
7. Silence: not thinking out loud.

---

#### 8. Related Topics

1. `13` Requirements & Estimation
2. `14`–`26` The building blocks you choose from
3. `32` Practice Designs
4. `30` Mobile-Specific Topics

---

#### 9. Interview Must Remember

1. **Clarify → Estimate → API + data → High-level → Flows → Deep dive → Trade-offs.**
2. **Start simple, scale where needed.**
3. **Ask for each part: fails? 10×? twice?**
4. **Explain trade-offs** every time.
5. **Think out loud** and check in with the interviewer.
