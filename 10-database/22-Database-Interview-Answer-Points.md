# Database Interview Answer Points

Roadmap topic 22 · Stage 8: Interview & Practice · (New)

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer, or still changing

**In simple words:** database interview questions almost always want the same thing underneath — a schema you can explain, a choice you can justify, and an honest trade-off you're aware of. This topic packages this whole folder into the shape those answers actually need.

---

#### 1. Design a Schema from Requirements — 🟢 Must Know

The standard flow: **entities → keys → relationships → top queries** (`2`, item 4) — always start from what the system needs to store and ask, not from an abstract "correct" schema. Sketch it out loud, narrating each choice as you go.

---

#### 2. Explain Each Choice — 🟢 Must Know

*The single habit that separates a strong answer from a merely correct one.*

"Why this key?" — surrogate over natural, for the reasons in `2` item 2. "Why this index?" — matches the actual query pattern (`5`). "Why this isolation level?" — the specific anomaly it protects against (`9`). Never state a choice without the reasoning behind it.

---

#### 3. Ready Answer: SQL vs NoSQL — 🟢 Must Know

Relational by default (`11`, item 2); NoSQL for a specific, clear reason tied to access pattern, flexible schema needs, or extreme write scale — never "for scale" alone, without real numbers behind it (item 8).

---

#### 4. Ready Answer: Indexes — 🟢 Must Know

What an index is, the read/write trade-off, composite index column order, and how to confirm one is actually being used with `EXPLAIN` (`5`, `6`).

---

#### 5. Ready Answer: Transactions and Isolation Levels — 🟢 Must Know

ACID, the anomalies by name, and optimistic vs pessimistic locking, with a concrete example (double booking, money transfer) ready for each (`8`, `9`).

---

#### 6. Ready Answer: Replication and Sharding — 🟢 Must Know

Leader-follower and the sync/async trade-off (`14`); "shard last, and only for a real reason" (`15`, item 1) plus a good shard key example (chat's `conversation_id`).

---

#### 7. Ready Answer: Prevent Double Booking — 🟢 Must Know

A unique constraint (simplest, works when the "slot" is naturally unique) or `SELECT ... FOR UPDATE` pessimistic locking (when more complex availability logic is involved) — `9`, item 4 and item 10.

---

#### 8. Ready Answer: Make Writes Idempotent — 🟢 Must Know

A unique constraint on an idempotency key, so a retried request fails cleanly instead of duplicating an effect (`8`, item 6).

---

#### 9. Ready Answer: Fix a Slow Query — 🟢 Must Know

`EXPLAIN ANALYZE` → look for a sequential scan or a big gap between estimated and actual rows → check for a missing index, N+1, `SELECT *`, or a large `OFFSET` → fix one thing → re-measure (`6`).

---

#### 10. Always Mention the Trade-Off — 🟢 Must Know

*The same discipline as `09-architecture/3`, applied specifically to database answers.*

Never present a choice as free — "I'd add this index, but it costs write performance on this heavily-written table" is a stronger, more complete answer than the index recommendation alone.

---

#### 11. Reading a Query and Predicting Its Plan — 🟡 Good to Know

Practice: given a query and the known indexes, predict whether it'll be a sequential scan or an index scan, before running `EXPLAIN` to check — a genuinely useful skill to demonstrate live in an interview.

---

#### 12. Estimating Data Size and Query Load — 🟡 Good to Know

The same estimation discipline as `SD 13`, applied to a schema design question — rough numbers for rows, growth rate, and query frequency, stated explicitly, showing the design decisions actually connect to real scale.

---

#### 13. Questions to Ask the Interviewer About the Data — 🟡 Good to Know

```text
"What's the expected read/write ratio for this data?"
"How much historical data needs to stay queryable?"
"Are there existing consistency requirements I should design around?"
```

Good clarifying questions here double as a demonstration that you start from requirements (item 1), not assumptions.

---

#### 14. Common Traps — 🟡 Good to Know

1. **Adding NoSQL "for scale" with no numbers** — the same hype-driven-choice trap from `11`, item 9.
2. **Sharding too early** — before trying indexes, caching, replicas, or a bigger machine (`15`, item 1).

---

#### 15. Common Interview Questions

1. **Design a schema for [some feature].** — use item 1's flow, and narrate the reasoning from item 2 at every step.
2. **How would you prevent double booking a seat?** — item 7's ready answer, with a real code sketch if asked.
3. **A query is slow — walk me through debugging it.** — item 9's `EXPLAIN`-first process.
4. **When would you shard a database?** — item 3 and item 14's "last resort, real reason" framing, and the common trap in item 14.

---

#### 16. Common Mistakes

1. Presenting a schema or choice without explaining the reasoning behind it.
2. Reaching for NoSQL or sharding without real numbers justifying the need.
3. Never mentioning the trade-off or cost of a recommended choice.
4. Diagnosing a slow query by guessing instead of describing the `EXPLAIN`-first process.

---

#### 17. Related Topics

1. `1`–`21` — this entire folder feeds into this one packaged interview structure
2. `21` Architecture Interview Answers (in `09-architecture`) — the same "always name the trade-off" discipline
3. `23` Practice: Projects & Exercises — where these ready answers actually get rehearsed

---

#### 18. Interview Must Remember

1. **Entities → keys → relationships → top queries** — the schema-design flow.
2. **Always explain the "why"** behind every choice.
3. **`EXPLAIN`-first for any slow-query question.**
4. **Never present a choice as free** — always name the trade-off.
