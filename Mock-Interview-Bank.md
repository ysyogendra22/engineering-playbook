# Mock Interview Bank

> Timed practice prompts for every folder in this repo. Use them once you have read the matching notes. Speak out loud, keep a timer, and score yourself at the end.

---

## How to Use This File

1. **Pick one session** from the table below and set a timer.
2. **Do not look at the notes.** Say your answer out loud, or write it on paper or a whiteboard.
3. **Stop when the timer ends**, even if you are not done. Real interviews do the same.
4. **Score yourself** with the scorecard at the bottom, then open the notes in the "Review" column for anything you missed.
5. **Redo a weak prompt** after two or three days. Repeating one prompt twice teaches more than doing two new ones.

| Session | Length | What you do | Where the prompts are |
|---|---|---|---|
| Coding | 45 min | 2 problems: 5 min restate, 30 min solve, 10 min test and complexity | Section 1 |
| SQL | 30 min | 3 queries | Section 2 |
| System design | 45 min | 1 design: clarify, estimate, design, deep dive, trade-offs | Section 3 |
| Mobile deep dive | 30 min | 4 questions, 7 min each | Section 4 |
| Backend and database | 30 min | 4 questions | Section 5 |
| AI engineering | 30 min | 3 questions or 1 design | Section 6 |
| Architecture | 45 min | 1 case, then 2 follow-ups | Section 7 |
| Behavioral | 30 min | 4 stories, 7 min each | Section 8 |

---

## 1. Coding (45 minutes, 2 problems)

Pick one set. Say which pattern you see and why *before* you code. The pattern notes are in `03-leetcode-patterns`.

| Set | Problem 1 | Problem 2 | Review |
|---|---|---|---|
| A: hashing and pointers | [Two Sum](https://leetcode.com/problems/two-sum/) (Easy) | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium) | 03 notes 4, 5; `02-algorithm` 2 |
| B: intervals and stacks | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (Medium) | 03 notes 9, 10 |
| C: search | [Binary Search](https://leetcode.com/problems/binary-search/) (Easy) | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Medium) | 03 note 8; `02-algorithm` 2 |
| D: heaps and prefix sums | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium) | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium) | 03 notes 7, 11 |
| E: trees and graphs | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (Medium) | [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium) | 03 notes 12, 13, 15 |
| F: dependencies | [Course Schedule](https://leetcode.com/problems/course-schedule/) (Medium) | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) | 03 notes 6, 16 |
| G: backtracking | [Subsets](https://leetcode.com/problems/subsets/) (Medium) | [Word Search](https://leetcode.com/problems/word-search/) (Medium) | 03 note 14; `02-algorithm` 6 |
| H: dynamic programming | [Coin Change](https://leetcode.com/problems/coin-change/) (Medium) | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) (Medium) | 03 note 18; `02-algorithm` 5 |
| I: design | [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium) | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) | 03 notes 20, 21 |
| J: stretch (hard) | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) | 03 notes 11, 4 |

**Every time, say out loud:** restate, brute force with Big-O, the pattern and its signal, a plan, code, dry-run with an edge case, time and space.

---

## 2. SQL (30 minutes, 3 queries)

Use a local PostgreSQL or SQLite. Notes: `10-database` 2 to 4 and 22.

| Set | Query 1 | Query 2 | Query 3 |
|---|---|---|---|
| A | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) (Easy) | [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) (Easy) | [Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) (Medium) |
| B | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) (Easy) | [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/) (Medium) | [Movie Rating](https://leetcode.com/problems/movie-rating/) (Medium) |
| C (stretch) | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) (Hard) | [Trips and Users](https://leetcode.com/problems/trips-and-users/) (Hard) | Write: "top 1 order per user" with `ROW_NUMBER()` on your own table |

**Say out loud:** the tables and keys, the join type and why, what happens with `NULL`s and ties, and which index would help.

---

## 3. System Design (45 minutes, 1 prompt)

Plan: clarify 5 · estimate 4 · API and data 6 · high-level design 10 · deep dive 15 · trade-offs 5. Notes: `05-system-design` 13 to 33.

| # | Prompt | Probe questions the interviewer may ask | Review |
|---|---|---|---|
| 1 | Design a URL shortener | How do you make short, unique IDs? What if one link goes viral? How do you cache and expire? | 13, 15, 17, 20 |
| 2 | Design a rate limiter | Per user or per IP? How do you share counters across servers? What happens when the limiter is down? | 14, 15, 25 |
| 3 | Design a news feed | Fan-out on write or on read? How do you handle a celebrity with 10 million followers? | 15, 19, 21 |
| 4 | Design a chat app for mobile | How do messages arrive when the app is closed? Ordering, delivery receipts, offline sync? | 21, 24, 30 |
| 5 | Design a notification system | Retries, duplicates, user preferences, quiet hours, provider outage? | 21, 22, 25 |
| 6 | Design photo upload and sharing | Large uploads on a weak network, thumbnails, CDN, storage cost? | 16, 21, 30 |
| 7 | Design a ticket-booking system | How do you stop two people buying the last seat? Holds, expiry, payment failure? | 23, 22, `10-database` 9 |
| 8 | Design a payment flow | Idempotency, double charges, webhooks, reconciliation, refunds? | 22, 23, 29 |
| 9 | Design a ride-hailing app (location) | Location updates at scale, matching, battery use, surge? | 14, 24, 30 |
| 10 | Design an offline-first notes app | Sync, conflicts, deletes, schema changes on old app versions? | 30, `06-mobile` 9, `10-database` 21 |

---

## 4. Mobile Deep Dive (30 minutes, 4 questions)

Notes: `06-mobile-engineering`.

| # | Question | Review |
|---|---|---|
| 1 | What happens to your screen state on rotation and on process death? How do you keep it? | 4, 5, 6 |
| 2 | A coroutine keeps running after the user leaves the screen. Why, and how do you fix it? | 3 |
| 3 | A `LazyColumn` stutters. How do you find the cause and fix it? | 5, 11 |
| 4 | Walk me through your app architecture. Where do state, errors and caching live? | 6, 7 |
| 5 | Design offline-first for a notes app. How do you handle sync conflicts and deletes? | 9, 18 |
| 6 | A background upload must survive the app being killed. What do you use and why? | 10 |
| 7 | How do you store tokens and secrets on the device? | 13 |
| 8 | You ship a crash to 20% of users. What do you do in the first hour? | 15 |
| 9 | How do you test a ViewModel that uses a repository and coroutines? | 12 |
| 10 | When would you choose Kotlin Multiplatform? When not? | 17 |
| 11 | Design an image-heavy feed for mobile. | 11, 18 |
| 12 | How do you add an AI chat feature to the app safely? | 20, `08-artificial-intelligence` 20 |

---

## 5. Backend and Database (30 minutes, 4 questions)

Notes: `04-backend-engineering`, `10-database`.

| # | Question | Review |
|---|---|---|
| 1 | The user taps Pay twice. How do you avoid charging twice? | `04` 3, 11 |
| 2 | Explain 401 vs 403, and which errors a client should retry. | `04` 2, 3 |
| 3 | User A can read user B's note by changing an ID. What is the bug and the fix? | `04` 5 |
| 4 | An endpoint became slow. Walk me through finding the cause. | `04` 10, `10-database` 5, 6 |
| 5 | Explain composite index column order with an example. | `10-database` 5 |
| 6 | What is a lost update? Give two fixes. | `10-database` 8, 9 |
| 7 | Which isolation level would you use and why? What anomalies remain? | `10-database` 9 |
| 8 | Rename a column on a live system without downtime. | `10-database` 10 |
| 9 | SQL or NoSQL for this product? Defend your choice. | `10-database` 11, 12 |
| 10 | Your read replica is stale. What breaks and how do you handle it? | `10-database` 14 |
| 11 | When would you shard, and what would you shard on? | `10-database` 15 |
| 12 | Someone dropped a table at 14:03. How do you recover? | `10-database` 17 |

---

## 6. AI Engineering (30 minutes, 3 questions or 1 design)

Notes: `08-artificial-intelligence`.

| # | Question | Review |
|---|---|---|
| 1 | Prompt, RAG or fine-tuning? How do you choose? | 3, 7 |
| 2 | Design a "chat with your documents" feature. How do you stop it showing another user's data? | 6, 7, 16 |
| 3 | The model sometimes invents facts. What do you change? | 2, 7, 15 |
| 4 | Design a customer-support agent that can refund orders. What are the limits and approvals? | 8, 10, 16 |
| 5 | How do you know your AI feature got better after a change? | 15 |
| 6 | The AI bill doubled. Where do you look first? | 17 |
| 7 | What is prompt injection and how do you reduce the damage? | 16 |
| 8 | On-device model or cloud model for a mobile feature? | 19 |
| 9 | When is a multi-agent design worth its cost? | 14 |
| 10 | What would you log and monitor in production? | 18 |

---

## 7. Architecture (45 minutes, 1 case then 2 follow-ups)

Notes: `09-architecture`. Always start with the quality attributes you would rank first.

| # | Case | Follow-ups | Review |
|---|---|---|---|
| 1 | A monolith is slow to change. Do we move to microservices? | What would you do first? How would you measure success? | 5, 8, 16 |
| 2 | Choose between building and buying an auth or payments system. | What is the exit plan? Who owns it? | 3 |
| 3 | Design the architecture of a mobile app with 15 engineers. | How do modules depend on each other? How do you release safely? | 8, 19 |
| 4 | Add an AI assistant to an existing product. | How do you protect data? How do you keep cost and latency in check? | 20 |
| 5 | Your system must reach 99.99% availability. | What does it cost? Which parts would you not make highly available? | 12 |
| 6 | Two teams disagree on a technical direction. | How do you decide and record it? | 3, 14, 15 |
| 7 | Tech debt is slowing delivery. | How do you prioritise and prove the payback? | 16 |
| 8 | A third-party API is unreliable. | Timeouts, retries, fallbacks, adapter, reconciliation? | 10, 12 |

---

## 8. Behavioral (30 minutes, 4 stories)

Notes: `07-behavioral-leadership`. Use **STAR + Lesson**, about 2 minutes each, one real number in the result.

| # | Prompt | Review |
|---|---|---|
| 1 | Tell me about a project you are proud of and the hardest part. | 4 |
| 2 | Tell me about a technical decision you made with incomplete information. | 5 |
| 3 | Tell me about a time you failed. What changed afterwards? | 7 |
| 4 | Tell me about a production incident you handled. | 8 |
| 5 | Tell me about a disagreement with a teammate or manager. | 9 |
| 6 | Tell me about working across teams to ship something. | 10 |
| 7 | Tell me about a time you led without being the manager. | 12 |
| 8 | Tell me about a time you mentored someone. | 13 |
| 9 | Tell me about a time you had to cut scope or miss a deadline. | 14 |
| 10 | Tell me about a time things were unclear and you moved anyway. | 17 |
| 11 | Walk me through your career, and why this company. | 16, 19 |
| 12 | What is your biggest weakness, and what are you doing about it? | 18 |

---

## Weekly Mock Rhythm

Follow this beside the plan in the README.

| When | Do |
|---|---|
| Weeks 1–4 | One coding set (Section 1) at the end of each week |
| Weeks 5–7 | One SQL set (Section 2) and one backend/database session (Section 5) |
| Weeks 8–9 | One system design prompt per week (Section 3), and one architecture case (Section 7) |
| Weeks 10–11 | One mobile session (Section 4) and one AI session (Section 6) |
| Week 12 | Two full mixed days: coding + system design + behavioral, with a one-hour break between rounds |

---

## Scorecard

Score each area from 1 (weak) to 4 (strong). Anything at 1 or 2 gets a redo within three days.

| Area | What a 4 looks like | Score |
|---|---|---|
| Communication | Restates, asks questions, explains while working, takes hints well | |
| Problem solving | Names the pattern or the trade-off, compares at least two approaches | |
| Correctness | Works on the examples and on edge cases (empty, one item, duplicates) | |
| Complexity | States time and space and says where each comes from | |
| Depth | Goes one level deeper when asked (failure, scale, security) | |
| Time | Finishes inside the time box and leaves room to test | |
