# NP-Complete — the Hardest Problems in NP

#### 1. Definition — Must Know

**NP-Complete** problems are the hardest problems within NP (topic 2) — every other problem in NP can be **transformed** (reduced) into any NP-Complete problem, in polynomial time. This means: if anyone ever found a fast (polynomial-time) algorithm for **one** NP-Complete problem, it would instantly give a fast algorithm for **every** problem in NP.

#### 2. Why It Is Used — Must Know

This is why "is this problem NP-Complete?" matters so much practically: if you can show a new problem is NP-Complete, you've proven (using decades of collective effort by others) that no one has ever found a fast exact algorithm for it — so you can stop searching for one and move to an approximation or heuristic instead (topic 5), with real confidence that's the right call.

#### 3. How It Works — Must Know

```text
Well-known NP-Complete problems:
  Travelling Salesman Problem (decision version)
  Subset Sum (with large numbers)
  Graph Coloring (can a graph be colored with k colors, no adjacent same color?)
  Boolean Satisfiability (SAT) — the FIRST problem proven NP-Complete,
                                  everything else is proven via reduction to it

The "Complete" part means: if you could solve ONE of these fast, you
could solve ALL of them fast, and in fact all of NP — because they can
all be translated into each other in polynomial time.
```

```text
Simplified picture of the relationship:

   NP  ─────────────────────────────
   │                                 │
   │   P                             │
   │  ┌──────┐                       │
   │  │      │        NP-Complete    │
   │  │      │       ┌──────────┐    │
   │  └──────┘       │  TSP,    │    │
   │                  │  SAT,    │    │
   │                  │  Sudoku* │    │
   │                  └──────────┘    │
   └─────────────────────────────────
   (* the DECISION version of Sudoku on an n×n board, not the fixed 9×9 puzzle)
```

#### 4. Algorithm — Must Know

```text
To argue a NEW problem is NP-Complete (the standard approach):
1. Show it's in NP (a proposed solution can be checked fast — topic 2).
2. Show a KNOWN NP-Complete problem can be transformed (reduced) into
   your new problem, in polynomial time.
   (This proves your problem is at least as hard as that known one.)
```

#### 5. Kotlin Implementation — Must Know

*(Not applicable — this is a classification and proof concept, not something implemented directly.)*

#### 6. Complexity — Must Know

| | Status |
|---|---|
| Best known exact algorithms for NP-Complete problems | Exponential (or worse) time |
| Is a polynomial-time algorithm known for any of them? | No |
| Is it proven that none can exist? | No — this is exactly the open P vs NP question (topic 7) |

#### 7. Common Mistakes — Must Know

1. Saying a problem is "NP-Complete" when you actually mean "NP-Hard" (topic 6) — NP-Complete specifically requires being **in NP** too; some NP-Hard problems are not.
2. Trying to design a fast, exact algorithm for a known NP-Complete problem in an interview — this is expected to fail, since no one has ever found one; the strong answer is recognising the shape and moving to approximation instead.
3. Treating "NP-Complete" as meaning "literally impossible to solve" — it just means no *fast, exact* algorithm is known; slow exact solutions (backtracking, `06-Backtracking/08`) and fast approximate solutions both still exist.

#### 8. Related Topics

1. `2` NP — Checkable in Polynomial Time — the larger category NP-Complete sits inside
2. `4` Recognising an NP-Complete Shape in an Interview — how to spot one
3. `5` What to Do Instead — Approximation, Heuristics, Smaller Exact Inputs — the practical response

#### 9. Interview Must Remember

1. **NP-Complete = the hardest problems in NP; solving one fast would solve all of NP fast.**
2. TSP, Subset Sum (large numbers), Graph Coloring, and SAT are the classic named examples.
3. Recognising a problem as NP-Complete is a strong, correct interview answer — it means "no known fast exact algorithm", not "I couldn't figure it out".
