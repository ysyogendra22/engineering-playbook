# LeetCode Patterns: Learning & Interview Roadmap

Recognise the pattern, apply the template, explain the complexity, in Kotlin. `01-data-structure` and `02-algorithm` teach how each structure or algorithm works and why it is fast; this folder teaches **when to reach for which one**, and how to say it in an interview.

Source list: https://leetcode.com/discuss/post/7347258/15-essential-dsa-patterns-for-tech-inter-nxem/

- **Numbering:** own, 1–22. Topics 4–18 are your original 15 patterns, in order.
- **References:** `LC` = this folder · `DS` = `01-data-structure` (e.g. `DS Graph`) · `ALG` = `02-algorithm`, written `ALG <topic>.<note>` (e.g. `ALG 7.2` = Graph Algorithms, note 2) · `BE`/`SD`/`MOB`/`ARCH` = the other numbered roadmaps
- **Every `ALG` folder has a `99-… Cheat Sheet`.** Read it after the pattern note, and again the night before.
- **Problem numbers** are LeetCode's. Trust the title if they disagree. *(premium)* needs a paid account; use the free alternative given
- **Marks:** 🟢 must have · 🟡 good to have · (New) beyond your original 15

---

## Index

| #   | Topic                                | Stage                   | Mark | Learn the tool first in                                      |
| --- | ------------------------------------ | ----------------------- | ---- | ------------------------------------------------------------ |
| 1   | How to Solve a Coding Problem        | 1. Method               | 🟢   |                                                              |
| 2   | Complexity & Constraints             | 1. Method               | 🟢   | `ALG 3.4`, `ALG 3.5`, `ALG 11.1` (growth rates, recurrences) |
| 3   | Kotlin for Coding Interviews (New)   | 1. Method               | 🟢   | `ALG 8.1` (strings), `ALG 10.7` (`Int` vs `Long`)            |
| 4   | Two Pointers                         | 2. Array & String       | 🟢   | `ALG 1.12`, `ALG 8.3`, `ALG 8.4`                             |
| 5   | Sliding Window                       | 2. Array & String       | 🟢   | `ALG 8.3`, `DS HashMap`                                      |
| 6   | Fast & Slow Pointers                 | 2. Array & String       | 🟡   | `DS LinkedList`                                              |
| 7   | Prefix Sum                           | 2. Array & String       | 🟢   | `ALG 10.5`, `ALG 9.3` (prefix remainders, prefix XOR)        |
| 8   | Binary Search                        | 2. Array & String       | 🟢   | `ALG 2` (all notes), `ALG 2.11`, `ALG 2.15`                  |
| 9   | Merge Intervals                      | 2. Array & String       | 🟡   | `ALG 1.12`, `ALG 4`                                          |
| 10  | Monotonic Stack                      | 2. Array & String       | 🟡   | `DS Stack`                                                   |
| 11  | Top K Elements                       | 2. Array & String       | 🟢   | `DS Heap`, `ALG 1.7`, `ALG 2.13`, `ALG 1.10`                 |
| 12  | BFS                                  | 3. Trees & Graphs       | 🟢   | `DS Queue`, `DS Graph`, `ALG 7.3` (0-1 BFS)                  |
| 13  | DFS                                  | 3. Trees & Graphs       | 🟢   | `DS Tree`, `ALG 3.7`, `ALG 3.10`                             |
| 14  | Backtracking                         | 3. Trees & Graphs       | 🟢   | `ALG 6` (all notes)                                          |
| 15  | Graph Traversal                      | 3. Trees & Graphs       | 🟢   | `DS Graph`, `ALG 7.1`, `ALG 7.2`, `ALG 7.8`                  |
| 16  | Topological Sort                     | 3. Trees & Graphs       | 🟡   | `DS Graph` (topological sort, Kahn's algorithm)              |
| 17  | Union Find                           | 3. Trees & Graphs       | 🟡   | `DS Graph` (Union-Find notes), `ALG 7.2`                     |
| 18  | Dynamic Programming                  | 4. Optimization         | 🟢   | `ALG 5` (all notes), `ALG 3.8`                               |
| 19  | Greedy (New)                         | 4. Optimization         | 🟡   | `ALG 4` (all notes)                                          |
| 20  | More Patterns to Know (New)          | 5. Extra Patterns       | 🟡   | `DS Trie`, `ALG 9`, `ALG 10`, `ALG 8.5`–`8.7`                |
| 21  | Coding Interview Answer Points (New) | 6. Interview & Practice | 🟢   | `ALG 11.5` (what to say for an NP-hard problem)              |
| 22  | Practice Plan & Problem Sets (New)   | 6. Interview & Practice | 🟡   |                                                              |
| 99  | LeetCode Patterns Cheat Sheet        | Revision                | 🟢   |                                                              |

Each note has the same layout: what it is and how to spot it, how it works, brute force vs optimized, Kotlin code with checked outputs, complexity, common mistakes, what to say in the interview, a quick check, and Easy → Medium LeetCode links.

**Short on time:** 1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 15, 18, 21, then the cheat sheet (99).

**Where things moved:** the nine-step routine is in note 1. The "signal to pattern" table, the constraints table and the templates are in the cheat sheet (99). The six-week plan and the topic-wise problem sets are in note 22.

**Pattern to algorithm map:** each pattern here is the interview-facing side of a tool you learn properly in `ALG`. The table below shows which `ALG` note explains why it works, so you can go back when a template feels like memorisation.

| Pattern (`LC`) | Why it works (`ALG` / `DS`) |
|---|---|
| 4 Two Pointers | sorted order makes pointer moves safe: `ALG 1`; palindromes: `ALG 8.4` |
| 5 Sliding Window | each index enters and leaves once, so `O(n)`: `ALG 8.3` |
| 7 Prefix Sum | equal prefix remainders give divisible subarrays: `ALG 10.5`; prefix XOR: `ALG 9.3` |
| 8 Binary Search | monotonic check, bounds, search on the answer: `ALG 2.3`–`2.15` |
| 9 Merge Intervals | sort by start, then one sweep: `ALG 1.12` |
| 11 Top K | heap of size `k`: `DS Heap`; quickselect: `ALG 2.13` |
| 12 BFS / 15 Graph Traversal | weights choose the algorithm: `ALG 7.3`; Dijkstra, Bellman-Ford, MST: `ALG 7.1`, `7.4`, `7.2` |
| 13 DFS | recursion on trees (top-down vs bottom-up): `ALG 3.10`; explicit stack: `ALG 3.7` |
| 14 Backtracking | choose, explore, un-choose; duplicates; pruning: `ALG 6` |
| 17 Union Find | cycle edges and spanning trees: `ALG 7.2` |
| 18 Dynamic Programming | state, recurrence, base case, fill order; LIS; knapsack: `ALG 5` |
| 19 Greedy | greedy choice property and exchange argument: `ALG 4` |
| 20 More Patterns | bitmask: `ALG 9.6`, `9.7`; cyclic sort: `ALG 1.11`; math tricks: `ALG 10.10` |

---

# Six-Week Plan

| Week | Topics | Goal |
|---|---|---|
| 1 | 1, 2, 3, 4, 5 | The method, Kotlin tools, two pointers, sliding window |
| 2 | 6, 7, 8, 9 | Fast and slow, prefix sum, binary search, intervals |
| 3 | 10, 11, 12, 13 | Monotonic stack, heap, BFS, DFS |
| 4 | 14, 15, 16, 17 | Backtracking, graphs, topological sort, union find |
| 5 | 18, 19 | Dynamic programming and greedy |
| 6 | 20, 21, plus mixed sets | Extra patterns, timed mixed practice, and mock interviews |

**Each week, in this order:** read the `LC` pattern note → read the matching `ALG` or `DS` notes from the table above → write the template from memory → solve the Easy then Medium links → finish with the `ALG` cheat sheet.

---

# Glossary: Terms to Learn First

Plain meanings, with a priority. The last column is the topic that explains the term.

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Big-O | How time or space grows as the input grows | 2 |
| 🟢 | Time / space complexity | Steps taken / extra memory used | 2 |
| 🟢 | In-place | Changing the input itself, using O(1) extra space | 4 |
| 🟢 | Two pointers | Two indexes moving through the data, often from both ends | 4 |
| 🟢 | Sliding window | A moving range over a sequence, updated as it slides | 5 |
| 🟢 | Prefix sum | Running totals that make any range sum an O(1) subtraction | 7 |
| 🟢 | Binary search | Halving a sorted or monotonic search space each step | 8 |
| 🟢 | Search on answer | Binary search over possible answers, with a yes/no check | 8 |
| 🟢 | Monotonic stack | A stack kept in sorted order to find the next greater or smaller value | 10 |
| 🟢 | Heap / priority queue | A structure that gives the smallest or largest item fast | 11 |
| 🟢 | BFS | Explore level by level with a queue. Finds shortest paths in unweighted graphs | 12 |
| 🟢 | DFS | Go as deep as possible, then backtrack, using recursion or a stack | 13 |
| 🟢 | Visited set | Remembers what you have seen so you never loop forever | 12, 15 |
| 🟢 | Backtracking | Try a choice, explore, then undo it and try the next | 14 |
| 🟢 | Pruning | Stopping a branch early because it cannot lead to an answer | 14 |
| 🟢 | Connected component | A group of nodes that can all reach each other | 15 |
| 🟢 | Cycle | A path that returns to where it started | 15 |
| 🟢 | DAG | Directed acyclic graph: directed edges with no cycles | 16 |
| 🟢 | Topological order | An ordering where every dependency comes before what needs it | 16 |
| 🟢 | In-degree | The number of edges coming into a node | 16 |
| 🟢 | Union find (DSU) | A structure that tracks groups and merges them quickly | 17 |
| 🟢 | Dynamic programming | Solving a problem by solving and remembering smaller subproblems | 18 |
| 🟢 | Overlapping subproblems | The same smaller problem appears many times | 18 |
| 🟢 | Optimal substructure | The best answer is built from best answers to smaller parts | 18 |
| 🟢 | State / transition | What defines a subproblem / how one state leads to another | 18 |
| 🟢 | Memoization / tabulation | Cache recursive results / fill a table bottom-up | 18 |
| 🟢 | Base case | The simplest case that is answered directly | 13, 18 |
| 🟢 | Greedy | Take the best local choice at each step | 19 |
| 🟢 | Edge case | An unusual input such as empty, one item, or duplicates | 1 |
| 🟢 | Overflow | A number too big for its type wraps around silently (`Int` over 2.1 billion) | 2, 3 |
| 🟡 | Amortized cost | The average cost per operation over a long sequence | 2 |
| 🟡 | Stable sort | A sort that keeps equal items in their original order | 4, 9 |
| 🟡 | Fast and slow pointers | Two pointers at different speeds, used for cycles and middles | 6 |
| 🟡 | Difference array | Store changes at range ends so many range updates are cheap | 7 |
| 🟡 | Lower / upper bound | The first position not less than / greater than a value | 8 |
| 🟡 | Quickselect | Find the Kth smallest in O(n) on average by partitioning | 11 |
| 🟡 | Multi-source BFS | BFS that starts from several nodes at the same time | 12 |
| 🟡 | Dijkstra | Shortest path in a weighted graph with non-negative weights | 15 |
| 🟡 | Bellman-Ford | Shortest path that allows negative weights and "at most K edges" | 15 |
| 🟡 | MST | Minimum spanning tree: connects all nodes with the least total weight | 15, 17 |
| 🟡 | Kahn's algorithm | Topological sort by repeatedly removing nodes with in-degree 0 | 16 |
| 🟡 | Path compression / union by rank | Two tricks that keep union find nearly constant time | 17 |
| 🟡 | Knapsack | Choosing items under a limit to get the best value | 18 |
| 🟡 | Kadane's algorithm | Maximum subarray sum in one pass | 18, 20 |
| 🟡 | Exchange argument | A way to show a greedy choice is safe: swapping it in cannot make things worse | 19 |
| 🟡 | Trie | A tree of characters used for prefix search | 20 |
| 🟡 | Bitmask | Using the bits of an integer to represent a set | 14, 20 |
| 🟡 | Rolling hash | A hash updated in O(1) as a window slides | 20 |
| 🟡 | Modular arithmetic | Keeping numbers small by taking the remainder after every step | 3, 20 |
| 🟡 | Sweep line | Process events in sorted order to handle overlaps | 9, 20 |
| ⚪ | NP-hard | A problem with no known fast exact algorithm; say so, then approximate or use a small-`n` exact method | 21 |

---

## Skip for Now

- Very hard problems (rated hard with rare tricks) until the 🟢 patterns feel easy
- Advanced data structures: segment trees, suffix arrays, and heavy graph algorithms such as max flow
- Competitive-programming speed tricks. Interviews reward clarity
- Memorizing solutions. Learn the pattern and the reason it works
- Language-specific micro-optimizations
- Writing KMP, Rabin-Karp, Z-algorithm, matrix exponentiation or extended Euclid from memory. Know when they apply (`ALG 8`, `ALG 10`)

## How to Proceed

1. Do topics 1 to 3 first. The method and Kotlin tools make every later topic easier.
2. Take one pattern at a time, in order. Read the matching notes from the index column "Learn the tool first in", write the template from memory, then solve the classic problems.
3. After each pattern, do one mixed problem and try to name the pattern before you read any hints.
4. Do topics 12 to 17 (trees and graphs) carefully. They cover a large share of medium and hard questions.
5. Do topic 18 slowly. Practise defining the state and the transition on paper before coding. Use the `ALG 5` cheat sheet to check your choice between DP, greedy and backtracking.
6. Finish with topics 21 and 22: timed mixed sets and mock interviews out loud.
7. For each pattern: what it is, when the signals appear, the template, the complexity, and one way it fails.
8. The night before an interview, read only the cheat sheets: `LC` 99 first, then the `ALG` ones for your weakest areas.
