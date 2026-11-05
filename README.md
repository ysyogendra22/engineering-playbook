#READ 

---

Structured notes for Software Engineering interview preparation, built for a mobile engineer growing toward senior and architect roles. Written in simple English for a beginner, aimed at FAANG-style interviews, with Kotlin for the code.

## Contents

| # | Folder | What it covers | Start here | Poster |
|---|---|---|---|---|
| 01 | `01-data-structure` | Array, Linked List, Stack, Queue, HashMap, HashSet, Tree, Heap, Trie, Graph | [00-data-structure](01-data-structure/00-data-structure.md) | [DS](01-data-structure/data_structure.jpeg) |
| 02 | `02-algorithm` | Sorting, searching, recursion, greedy, dynamic programming, backtracking, graphs, strings, bits, math, complexity classes (11 topic folders) | [00-Content](02-algorithm/00-Content.md) | [Algorithms](02-algorithm/algorithm_cheatsheet.png) |
| 03 | `03-leetcode-patterns` | The essential coding patterns, the method, and Kotlin tools (22 topics) | [00-Content](03-leetcode-patterns/00-Content.md) | [Patterns](03-leetcode-patterns/leetcode_patterns_cheatsheet.png) |
| 04 | `04-backend-engineering` | APIs, auth, security, testing, SQL, and the first pass on transactions (topics 1–12) | [00-Content](04-backend-engineering/00-Content.md) | [Backend](04-backend-engineering/backend_cheatsheet.png) |
| 05 | `05-system-design` | Requirements, scaling, caching, storage, queues, consistency, observability, mobile design (topics 13–33) | [00-Content](05-system-design/00-Content.md) | [System design](05-system-design/system_design_cheatsheet.png) |
| 06 | `06-mobile-engineering` | Android with Kotlin, Compose, architecture, offline-first, quality, iOS and KMP (22 topics) | [00-Content](06-mobile-engineering/00-Content.md) | [Mobile](06-mobile-engineering/mobile_cheatsheet.png) |
| 07 | `07-behavioral-leadership` | STAR, stories, decisions, incidents, conflict, leadership, offers (21 topics) | [00-Content](07-behavioral-leadership/00-Content.md) | [Behavioral](07-behavioral-leadership/behavioral_cheatsheet.png) |
| 08 | `08-artificial-intelligence` | LLMs, RAG, tools, agents, harnesses, evals, safety, AI on mobile (22 topics) | [00-Content](08-artificial-intelligence/00-Content.md) | [AI](08-artificial-intelligence/ai_cheatsheet.png) |
| 09 | `09-architecture` | The architect's role, quality attributes, trade-offs, styles, patterns, DDD, governance, mobile and AI architecture (22 topics) | [00-Content](09-architecture/00-Content.md) | [Architecture](09-architecture/architecture_cheatsheet.png) |
| 10 | `10-database` | Data modeling, SQL, indexes, internals, transactions, NoSQL, scaling, backups, security, mobile databases (23 topics) | [00-Content](10-database/00-Content.md) | [Database](10-database/database_cheatsheet.png) |


## Repository Structure

```text
engineering-playbook/
│
├── 01-data-structure/          topic folders + data_structure.jpeg
├── 02-algorithm/               11 topic folders, each with its own cheat sheet + algorithm_cheatsheet.png
├── 03-leetcode-patterns/       00-Content, notes 1–22, 99 cheat sheet, poster
├── 04-backend-engineering/     00-Content, notes 1–12, 99 cheat sheet, poster
├── 05-system-design/           00-Content, notes 13–33, 99 cheat sheet, poster
├── 06-mobile-engineering/      00-Content, notes 1–22, 99 cheat sheet, poster
├── 07-behavioral-leadership/   00-Content, notes 1–21, 99 cheat sheet, poster
├── 08-artificial-intelligence/ 00-Content, notes 1–22, 99 cheat sheet, poster
├── 09-architecture/            00-Content, notes 1–22, 99 cheat sheet, poster
├── 10-database/                00-Content, notes 1–23, 99 cheat sheet, poster
│
└── README.md
```

Each of folders 03 to 10 has:

- `00-Content.md`: the index with marks, a "short on time" list, a study path, and a glossary of terms to learn first.
- numbered topic notes, all in the same layout (see below).
- `99-*-Cheat-Sheet.md`: a one-page revision for the night before an interview.
- a poster image of that cheat sheet.

---

## Status

| Folder | Index | Topic notes | Cheat sheet | Poster |
|---|---|---|---|---|
| `01-data-structure` | Done | Written | Per topic | Yes |
| `02-algorithm` | Done | Written (11 topics) | Per topic | Yes |
| `03-leetcode-patterns` | Done | 22 written | Done | Yes |
| `04-backend-engineering` | Done | 12 written | Done | Yes |
| `05-system-design` | Done | 21 written | Done | Yes |
| `06-mobile-engineering` | Done | 22 written | Done | Yes |
| `07-behavioral-leadership` | Done | 21 written | Done | Yes |
| `08-artificial-intelligence` | Done | 22 written | Done | Yes |
| `09-architecture` | Done | 22 written | Done | Yes |
| `10-database` | Done | 23 written | Done | Yes |


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
- `99` is always the cheat sheet of that folder.

**Reference shorthand** used inside the roadmaps

| Prefix | Folder |
|---|---|
| `DS` | `01-data-structure` |
| `ALG` | `02-algorithm` |
| `LC` | `03-leetcode-patterns` |
| `BE` | `04-backend-engineering` |
| `SD` | `05-system-design` |
| `MOB` | `06-mobile-engineering` |
| `AI` | `08-artificial-intelligence` |
| `ARCH` | `09-architecture` |
| `DB` | `10-database` |

A plain number, such as `7`, means a topic in the same folder. For example, `SD 21` is system design topic 21.

**Topic note layout** (folders 03 to 10): a title and one-line goal, then nine numbered sections:

1. What it is and how to spot it in an interview
2. How it works, with a diagram
3. Brute force (naive) vs optimized (better) design
4. Kotlin code (SQL in `10-database`), with the outputs checked
5. Complexity, numbers, or limits
6. Common mistakes and edge cases
7. What to say in the interview
8. Quick check, with answers
9. Practice: related LeetCode problems, exercises, or design tasks

**How facts were checked:** code and SQL examples were run where possible (SQL on SQLite, numbers in Python). Anything not run, such as Redis, PostgreSQL-only syntax, cloud details, or Android and Room snippets, is marked "not run" or "check current". Premium LeetCode problems are marked "(premium)".


## Cheat Sheets

Two forms of quick revision, for every folder:

- **The `99-*-Cheat-Sheet.md` note:** key takeaways, numbers and rules of thumb, patterns and how to identify them (with a flowchart), templates, naive to better, mistakes, what to say out loud, and a practice order.
- **The poster image:** one page, 15 to 20 numbered boxes, in the style of the DSA cheat sheet in `01-data-structure`. Print it or keep it on your phone.

| Folder | Cheat sheet note | Poster |
|---|---|---|
| `02-algorithm` | per-topic `99-*` notes | `algorithm_cheatsheet.png` |
| `03-leetcode-patterns` | `99-LeetCode Patterns Cheat Sheet` | `leetcode_patterns_cheatsheet.png` |
| `04-backend-engineering` | `99-Backend-Cheat-Sheet` | `backend_cheatsheet.png` |
| `05-system-design` | `99-System-Design-Cheat-Sheet` | `system_design_cheatsheet.png` |
| `06-mobile-engineering` | `99-Mobile-Cheat-Sheet` | `mobile_cheatsheet.png` |
| `07-behavioral-leadership` | `99-Behavioral-Cheat-Sheet` | `behavioral_cheatsheet.png` |
| `08-artificial-intelligence` | `99-AI-Cheat-Sheet` | `ai_cheatsheet.png` |
| `09-architecture` | `99-Architecture-Cheat-Sheet` | `architecture_cheatsheet.png` |
| `10-database` | `99-Database-Cheat-Sheet` | `database_cheatsheet.png` |

The posters are drawn from HTML with headless Chrome, so the text stays exact. To change one, edit its content and render it again.


## Suggested Study Order

1. **Coding, all the way through:** `01` and `02` for the basics, then `03` for patterns. Practise a little every day.
2. **Backend then system design:** `04` topics 1–12, then `05` topics 13–33. Use `10-database` as the deeper pass on data topics.
3. **Mobile depth:** `06`, using your own app as the practice project.
4. **AI:** `08`, after `04` and the core of `05` (caching, queues, retries, streaming).
5. **Architecture:** `09`, once you have some backend and system design behind you.
6. **Behavioral:** `07`. Start collecting stories early, and practise out loud as interviews get close.
7. **Short on time:** every `00-Content.md` has a "Short on time" list. Do those, then the `99` cheat sheet.
8. **The night before an interview:** read the `99` cheat sheet or look at the poster for that area, then your own stories.


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

