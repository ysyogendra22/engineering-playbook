#READ 

---

Structured notes for Software Engineering interview preparation, built for a mobile engineer growing toward senior and architect roles.

## Contents

| # | Folder | What it covers | Start here |
|---|---|---|---|
| 01 | `01-data-structure` | Array, Linked List, Stack, Queue, HashMap, HashSet, Tree, Heap, Trie, Graph | [00-data-structure](01-data-structure/00-data-structure.md) |
| 02 | `02-algorithm` | Sorting and searching | Folder notes |
| 03 | `03-leetcode-patterns` | The 15 essential coding patterns, the method, and Kotlin tools (22 topics) | [00-Content](03-leetcode-patterns/00-Content.md) |
| 04 | `04-backend-engineering` | APIs, auth, security, testing, SQL, and the first pass on transactions (topics 1–12) | [00-Content](04-backend-engineering/00-Content.md) |
| 05 | `05-system-design` | Scaling, caching, storage, queues, consistency, observability, mobile design (topics 13–33) | [00-Content](05-system-design/00-Content.md) |
| 06 | `06-mobile-engineering` | Android with Kotlin, Compose, architecture, offline-first, quality, iOS and KMP (22 topics) | [00-Content](06-mobile-engineering/00-Content.md) |
| 07 | `07-behavioral-leadership` | STAR, stories, decisions, incidents, conflict, leadership, offers (21 topics) | [00-Content](07-behavioral-leadership/00-Content.md) |
| 08 | `08-artificial-intelligence` | LLMs, RAG, tools, agents, harnesses, evals, safety, AI on mobile (22 topics) | [00-Content](08-artificial-intelligence/00-Content.md) |
| 09 | `09-architecture` | The architect's role, principles, styles, decisions, documentation, governance (22 topics) | [00-Content](09-architecture/00-Content.md) |
| 10 | `10-database` | Data modeling, SQL, indexes, internals, transactions, NoSQL, scaling, mobile databases (23 topics) | [00-Content](10-database/00-Content.md) |


## Repository Structure

```text
engineering-playbook/
│
├── 01-data-structure/
├── 02-algorithm/
├── 03-leetcode-patterns/
├── 04-backend-engineering/
├── 05-system-design/
├── 06-mobile-engineering/
├── 07-behavioral-leadership/
├── 08-artificial-intelligence/
├── 09-architecture/
├── 10-database/
│
└── README.md
```

Each of folders 03 to 10 has a `00-Content.md`: an index, the marks, a "what to follow" checklist or study path, and a glossary of terms to learn first.

---

## Status

| Folder | Roadmap | Topic docs |
|---|---|---|
| `01-data-structure`, `02-algorithm` | Notes per topic | Written |
| `03-leetcode-patterns` | Done | Not yet |
| `04-backend-engineering` | Done | 12 written |
| `05-system-design` | Done | 21 written |
| `06-mobile-engineering` | Done | Not yet |
| `07-behavioral-leadership` | Done | Not yet |
| `08-artificial-intelligence` | Done | 22 written |
| `09-architecture` | Done | Not yet |
| `10-database` | Done | Not yet |


## How the Roadmaps Work

**Marks used in every roadmap**

| Mark | Meaning |
|---|---|
| 🟢 | Must have. Expected in most interviews. Learn first |
| 🟡 | Good to have. Learn after the 🟢 items are solid |
| (New) | Added beyond the original lists, or a newer idea that is still changing |

**Numbering**

- `04-backend-engineering` and `05-system-design` share one sequence: backend is topics 1–12, system design is topics 13–33.
- Folders `03`, `06`, `07`, `08`, `09`, and `10` each number their own topics from 1.

**Reference shorthand** used inside the roadmaps

| Prefix | Folder |
|---|---|
| `DS` | `01-data-structure` |
| `ALG` | `02-algorithm` |
| `BE` | `04-backend-engineering` |
| `SD` | `05-system-design` |
| `MOB` | `06-mobile-engineering` |
| `AI` | `08-artificial-intelligence` |
| `ARCH` | `09-architecture` |
| `DB` | `10-database` |

A plain number, such as `7`, means a topic in the same folder. For example, `SD 21` is system design topic 21.

**Topic file format:** title, roadmap topic and stage, marks, "In simple words", numbered sections each with a one-line explainer, then Common Interview Questions, Common Mistakes, Related Topics, and Interview Must Remember.


## Suggested Study Order

1. **Coding, all the way through:** `01` and `02` for the basics, then `03` for patterns. Practise a little every day.
2. **Backend then system design:** `04` topics 1–12, then `05` topics 13–33. Use `10-database` as the deeper pass on data topics.
3. **Mobile depth:** `06`, using your own app as the practice project.
4. **AI:** `08`, after `04` and the core of `05` (caching, queues, retries, streaming).
5. **Architecture:** `09`, once you have some backend and system design behind you.
6. **Behavioral:** `07`. Start collecting stories early, and practise out loud as interviews get close.


## Focus

- Core concepts
    
- Algorithms & patterns
    
- Kotlin implementations
    
- Time & space complexity
    
- System design
    
- Engineering trade-offs
    
- Interview questions



## Goal

**Understand → Implement → Analyze → Explain**

> Understand the concept. Recognize the pattern. Explain the trade-off. Then write the code.

