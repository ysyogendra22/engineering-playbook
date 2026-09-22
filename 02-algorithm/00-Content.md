# Algorithms: Learning & Interview Roadmap

How each algorithm works and why its complexity is what it is — recognising and applying it in an interview is `03-leetcode-patterns`. Named data structures (trees, heaps, tries, graphs) live in `01-data-structure`.

- **Numbering:** own, 1–11. Every topic has a folder; topics 1–2 have full per-algorithm notes, 3–11 currently have an index only.
- **References:** `7` = this folder · `DS` = `01-data-structure` (e.g. `DS Graph`) · `LC` = `03-leetcode-patterns` · `BE`/`SD` = `04-backend-engineering`/`05-system-design`
- **Marks:** 🟢 must have · 🟡 good to have · ⚪ awareness only — know the name and idea, don't implement from memory

---

## Index

| #   | Topic                                   | Stage                     | Folder                              |
| --- | --------------------------------------- | ------------------------- | ------------------------------------ |
| 1   | Sorting Algorithms                      | 1. Foundations            | `01-sorting`                         |
| 2   | Searching Algorithms                    | 1. Foundations            | `02-searching`                       |
| 3   | Recursion & Divide and Conquer          | 2. Paradigms              | `03-Recursion & Divide and Conquer`  |
| 4   | Greedy Algorithms                       | 2. Paradigms              | `04-Greedy Algorithms`               |
| 5   | Dynamic Programming                     | 2. Paradigms              | `05-Dynamic Programming`             |
| 6   | Backtracking & Branch and Bound         | 2. Paradigms              | `06-Backtracking & Branch and Bound` |
| 7   | Graph Algorithms                        | 3. Specialized Algorithms | `07-Graph Algorithms`                |
| 8   | String Algorithms                       | 3. Specialized Algorithms | `08-String Algorithms`               |
| 9   | Bit Manipulation                        | 3. Specialized Algorithms | `09-Bit Manipulation`                |
| 10  | Math & Number Theory                    | 3. Specialized Algorithms | `10-Math & Number Theory`            |
| 11  | Complexity Classes (P, NP, NP-Complete) | 4. Theory                 | `11-Complexity Classes`              |

**Short on time:** 1, 2, 3, 4, 5, 7 (the 🟢 items only), then go straight to `03-leetcode-patterns` for practice.

**Glossary:** the terms to learn first are listed at the end, each with a priority mark and the topic that explains it.

---

# How to Study Any Algorithm

*The same six steps work for every algorithm in this folder.*

| Step | What to do | Output |
|---|---|---|
| 1. Problem it solves | What input does it take, and what does it guarantee about the output? | One sentence |
| 2. Work a small example | Trace it by hand on 5 to 8 elements | A worked trace |
| 3. Find the technique | What is the core idea: compare and swap, split and combine, choose the best now, remember subproblems, try and undo? | The paradigm it belongs to |
| 4. Derive the complexity | Count the steps or use the recurrence. Do not memorise the answer without seeing why | Time and space complexity, with the reason |
| 5. Know the named versions | Which real algorithms use this technique, and when each is preferred | A short list with one line each |
| 6. Know the pitfalls | Where it goes wrong: edge cases, when it does not apply, common bugs | A short list |

**Then practise it as an interview pattern** in `03-leetcode-patterns`, where the signal-to-pattern cheat sheet and the classic problems live.

---

# Stage 1: Foundations

## 1. Sorting Algorithms

*Existing folder: `01-sorting`. This entry is a quick index, not a replacement for it.*

- 🟢 Bubble, Selection, Insertion Sort: O(n²), simple, and when each is still useful (nearly sorted data, small n)
- 🟢 Merge Sort: divide and conquer, O(n log n), stable, needs O(n) extra space
- 🟢 Quick Sort: divide and conquer with a pivot, O(n log n) average, O(n²) worst case, in-place, unstable
- 🟢 Heap Sort: build a heap, then pop the max repeatedly, O(n log n), in-place, unstable (`DS Heap`)
- 🟡 Counting Sort, Radix Sort, Bucket Sort: not comparison-based, O(n + k) when the data fits their assumptions
- 🟡 Stable vs unstable, and why it matters (sorting objects by a secondary key)
- ⚪ Tim Sort, Shell Sort, Cycle Sort, Comb Sort, Pigeonhole Sort, External Sort: names and the one idea each is known for
- 🟢 Kotlin's built-in `sort`, `sortedBy`, `sortedWith`: know what they use, and that you rarely hand-write a sort in real code

**Complexity quick reference**

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble / Selection / Insertion | O(n) / O(n²) / O(n²) | O(n²) | O(n²) | O(1) | Insertion & Bubble: yes. Selection: no |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting / Radix Sort | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Yes |

**Read the full notes:** `01-sorting/00-Contents.md` and its per-algorithm files.

## 2. Searching Algorithms

*Existing folder: `02-searching`. This entry is a quick index, not a replacement for it.*

- 🟢 Linear Search: O(n), works on unsorted data, the fallback when nothing else applies
- 🟢 Binary Search: O(log n), needs sorted or monotonic data, the template with `left`, `right`, `mid` (`LC 8`)
- 🟢 First and last occurrence, lower bound and upper bound
- 🟢 Binary search on a rotated sorted array, and finding the minimum
- 🟢 Binary search on the answer: search a range of possible answers with a yes/no check
- 🟡 Peak element, search in a 2D matrix, common binary search edge cases
- 🟡 Quickselect: O(n) average to find the Kth smallest or largest, built on the quicksort partition
- 🟡 Searching with a hash map or hash set: O(1) average lookup instead of a search
- ⚪ Jump Search, Exponential Search, Interpolation Search, Fibonacci Search, Ternary Search, Sentinel Search: names and the one idea each is known for

**Read the full notes:** `02-searching/00-Content.md` and its per-algorithm files.

---

# Stage 2: Algorithmic Paradigms

## 3. Recursion & Divide and Conquer

- 🟢 A function that calls itself on a smaller version of the same problem, with a base case that stops it
- 🟢 The three parts: base case, recursive case, and how the results combine
- 🟢 Recursion uses the call stack: depth × frame size is the space cost, and very deep recursion can overflow it
- 🟢 Divide and conquer: split the problem, solve each part recursively, then combine the results (Merge Sort is the classic example)
- 🟢 The Master Theorem, in plain words: a recurrence like `T(n) = a·T(n/b) + f(n)` tells you the complexity without expanding it by hand
- 🟢 Trace recursion with a call tree, and count the nodes to see the complexity
- 🟡 Tail recursion, and why Kotlin does not always optimise it away
- 🟡 Turning recursion into an iterative version with an explicit stack
- 🟡 Memoization as the bridge from plain recursion to Dynamic Programming (`5`)
- 🟡 Classic divide and conquer beyond sorting: binary search, the maximum subarray problem, closest pair of points (name only), fast exponentiation (`10`)

## 4. Greedy Algorithms

- 🟢 Make the locally best choice at each step, and never go back
- 🟢 Greedy only works when the problem has the **greedy choice property**: a local best choice leads to a global best answer
- 🟢 It is usually paired with sorting: sort by some key, then scan once
- 🟢 Proving a greedy algorithm is correct: an exchange argument, in plain words ("if a better solution existed, we could swap in the greedy choice without making it worse")
- 🟢 Classic examples: activity/interval selection, fractional knapsack, Huffman coding (name and idea), coin change with canonical coin systems
- 🟢 Greedy graph algorithms: Dijkstra's shortest path, Kruskal's and Prim's minimum spanning tree (`7`)
- 🟡 Why greedy fails on 0/1 knapsack and general coin change, and what breaks the exchange argument
- 🟡 Complexity: usually the cost of sorting, O(n log n), plus a single O(n) pass
- 🟡 Greedy vs Dynamic Programming: try greedy first, and fall back to DP once a counter-example breaks it (`5`, `LC 19`)

## 5. Dynamic Programming

- 🟢 Solve a problem by solving and remembering the answers to its overlapping subproblems
- 🟢 Two conditions: optimal substructure (the best answer is built from best answers to smaller parts) and overlapping subproblems (the same smaller problem appears many times)
- 🟢 Top-down (recursion plus memoization) and bottom-up (iterative table filling), and why they give the same answer
- 🟢 The four steps: define the state, write the recurrence, set base cases, decide the fill order
- 🟢 1D DP (Fibonacci, climbing stairs), 2D DP (grid paths, edit distance), and knapsack-style DP
- 🟢 Space optimisation: when the recurrence only needs the last row or two, drop the extra dimension
- 🟢 Complexity: number of distinct states × work to compute each one
- 🟡 Reconstructing the actual solution, not only its value, by remembering choices as you fill the table
- 🟡 Why plain recursion without memoization is exponential, and memoization brings it down to polynomial
- 🟡 Interval DP, digit DP, and bitmask DP: names and the shape of problem each fits
- 🟡 Practice the DP patterns and classic problems in `LC 18`

## 6. Backtracking & Branch and Bound

- 🟢 Explore choices one at a time, and undo a choice when it cannot lead to a valid answer
- 🟢 The template: choose, explore, un-choose (`LC 14`)
- 🟢 Backtracking searches the full space of choices; it differs from DP because the subproblems are not reused, only explored and discarded
- 🟢 Complexity is usually exponential, O(2ⁿ) or O(n!), because it is exploring a decision tree
- 🟢 Pruning: stop exploring a branch as soon as you know it cannot work, which is what keeps backtracking usable in practice
- 🟡 Branch and bound: like backtracking, but also tracks a "best so far" bound and prunes any branch that cannot beat it (used in optimisation problems, not just yes/no ones)
- 🟡 Classic examples: N-Queens, Sudoku, subset sum, the travelling salesman problem (name and idea only for TSP)
- 🟡 When a backtracking solution has repeated subproblems, it is a sign that DP could replace it (`5`)

---

# Stage 3: Specialized Algorithms

## 7. Graph Algorithms

*Graph traversal (BFS, DFS), representation, cycle detection, topological sort, and Union-Find already live in `DS Graph`. This topic adds the shortest-path and spanning-tree algorithms, and a comparison of when to use each.*

- 🟢 Dijkstra's algorithm: shortest path from one source, non-negative weights only, O((V + E) log V) with a heap (`DS Graph`)
- 🟢 Kruskal's and Prim's algorithms: minimum spanning tree, and how Union-Find makes Kruskal's efficient (`DS Graph`)
- 🟢 Know which algorithm fits which situation: unweighted → BFS, non-negative weights → Dijkstra, negative weights → Bellman-Ford, all-pairs → Floyd-Warshall
- 🟡 Bellman-Ford: shortest path that also works with negative weights, O(V·E), and can detect a negative cycle
- 🟡 Floyd-Warshall: shortest path between every pair of nodes at once, O(V³), simple to code, fine for small graphs
- 🟡 A* search: Dijkstra plus a heuristic that guesses the remaining distance, used in pathfinding and maps
- ⚪ Network flow (max flow / min cut): name and the one problem shape it solves (capacities on edges, maximum throughput)
- 🟡 Complexity comparison table below; the graph traversal patterns and problems live in `LC 12`, `LC 13`, `LC 15`, `LC 16`, `LC 17`

**Complexity quick reference**

| Algorithm | Complexity | Handles negative weights | Use for |
|---|---|---|---|
| BFS | O(V + E) | n/a (unweighted) | Shortest path, unweighted graph |
| Dijkstra | O((V + E) log V) | No | Shortest path, non-negative weights |
| Bellman-Ford | O(V · E) | Yes, and detects negative cycles | Shortest path with negative weights |
| Floyd-Warshall | O(V³) | Yes | All-pairs shortest path, small graphs |
| Kruskal | O(E log E) | n/a | Minimum spanning tree, sparse graph |
| Prim | O(E log V) | n/a | Minimum spanning tree, dense graph |

## 8. String Algorithms

- 🟢 Naive substring search: O(n·m), compare the pattern at every position
- 🟢 When naive search is fine: most interview inputs are small, so know it before reaching for anything cleverer
- 🟡 KMP (Knuth-Morris-Pratt): builds a "failure function" so the search never re-checks a character twice, O(n + m)
- 🟡 Rabin-Karp: rolling hash, compares hashes instead of characters, O(n + m) average, useful for multiple-pattern search
- 🟡 Z-algorithm: builds an array of longest common prefixes with the string itself, O(n), used for pattern matching and string period problems
- 🟢 Common string interview techniques: two pointers on a string, sliding window for substrings, frequency maps for anagrams (`LC 4`, `LC 5`, `LC 20`)
- 🟡 Palindrome checks and palindrome-related DP (`5`)
- 🟡 Trie for prefix matching lives in `DS Trie`, not repeated here
- ⚪ Suffix array and suffix tree: names and the one idea (fast substring queries on one large text), out of scope to implement from memory

## 9. Bit Manipulation

- 🟢 AND, OR, XOR, NOT, left shift, right shift, and what each does to the bits
- 🟢 Common tricks: check a bit (`n shr i and 1`), set a bit (`n or (1 shl i)`), clear a bit, toggle a bit
- 🟢 XOR tricks: XOR of a number with itself is 0, so XOR-ing a list cancels pairs and leaves the odd one out (single number problems)
- 🟢 Count set bits (`Integer.bitCount` in Kotlin/Java, or Brian Kernighan's trick: `n and (n - 1)` clears the lowest set bit)
- 🟢 Check if a number is a power of two: `n > 0 && (n and (n - 1)) == 0`
- 🟡 Bitmask to represent a set of up to about 20 items, used in bitmask DP and subset enumeration
- 🟡 Two's complement, and why negative numbers behave the way they do in shifts
- 🟡 Iterating all subsets of a bitmask
- 🟡 Complexity: bit tricks are O(1) or O(number of bits), and often replace an O(n) loop or extra memory

## 10. Math & Number Theory

- 🟢 GCD and LCM: the Euclidean algorithm, O(log(min(a, b)))
- 🟢 Prime checking: trial division up to √n, O(√n)
- 🟢 Sieve of Eratosthenes: find all primes up to n, O(n log log n), when you need many primes at once
- 🟢 Fast (modular) exponentiation: compute `a^b mod m` in O(log b) instead of O(b), by repeated squaring
- 🟢 Modular arithmetic basics: `(a + b) mod m`, `(a * b) mod m`, and why you take the modulo at each step to avoid overflow
- 🟡 Combinatorics basics: factorial, `nCr`, and computing them with modular inverse for large numbers
- 🟡 Overflow awareness: use `Long` for sums and products in Kotlin, and know `Int` limits (`LC 3`)
- ⚪ Matrix exponentiation for fast recurrences, and the extended Euclidean algorithm (name only)

---

# Stage 4: Theory

## 11. Complexity Classes (P, NP, NP-Complete)

- 🟢 P: problems solvable in polynomial time. NP: problems whose solution can be **checked** in polynomial time
- 🟢 NP-Complete: the hardest problems in NP; if you could solve one quickly, you could solve them all quickly
- 🟢 Why this matters in interviews: if a problem looks like a known NP-complete problem (TSP, subset sum at scale, graph colouring), say so, then discuss an approximation, a heuristic, or a smaller-input exact solution, instead of searching for a fast exact answer that likely does not exist
- 🟡 NP-Hard: at least as hard as NP-Complete, but not necessarily in NP itself
- 🟡 P vs NP is an open problem: nobody has proven whether P equals NP
- ⚪ Reductions: showing one problem is "at least as hard" as another by transforming it into the other. Name only

---

# Glossary: Terms to Learn First

Plain meanings, with a priority. The last column is the topic that explains the term.

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | In-place | An algorithm that rearranges data using O(1) extra space | 1 |
| 🟢 | Stable sort | A sort that keeps equal elements in their original relative order | 1 |
| 🟢 | Monotonic / sorted data | Data that only increases (or only decreases), needed for binary search | 2 |
| 🟢 | Base case | The simplest input a recursive function answers directly, without recursing | 3 |
| 🟢 | Divide and conquer | Split the problem, solve each part, then combine the results | 3 |
| 🟢 | Recurrence relation | An equation describing an algorithm's cost in terms of smaller inputs | 3 |
| 🟢 | Greedy choice property | A problem where the locally best choice always leads to the best overall answer | 4 |
| 🟢 | Optimal substructure | The best answer is built from the best answers to smaller parts | 4, 5 |
| 🟢 | Overlapping subproblems | The same smaller problem is solved again and again | 5 |
| 🟢 | Memoization | Caching the result of a subproblem so it is computed only once | 5 |
| 🟢 | State / transition | What defines a subproblem in DP / how one state leads to the next | 5 |
| 🟢 | Pruning | Stopping a search branch early because it cannot lead to a valid answer | 6 |
| 🟢 | Shortest path | The lowest-cost route between two nodes in a graph | 7 |
| 🟢 | Spanning tree | A subset of edges that connects every node with no cycles | 7 |
| 🟢 | Pattern matching | Finding where a smaller string occurs inside a larger one | 8 |
| 🟢 | Bitmask | Using the bits of an integer to represent a set of items | 9, 5 |
| 🟢 | Modular arithmetic | Arithmetic that wraps around after reaching a fixed value (the modulus) | 10 |
| 🟡 | Master Theorem | A shortcut formula for the complexity of many divide-and-conquer recurrences | 3 |
| 🟡 | Exchange argument | A way to prove a greedy algorithm is correct by showing a swap cannot improve it | 4 |
| 🟡 | Branch and bound | Backtracking that also tracks a best-so-far bound to prune more aggressively | 6 |
| 🟡 | Negative cycle | A cycle in a graph whose total weight is negative, which breaks "shortest path" | 7 |
| 🟡 | Rolling hash | A hash that can be updated in O(1) as a window slides, instead of recomputed | 8 |
| 🟡 | Two's complement | The standard way computers represent negative integers in binary | 9 |
| 🟡 | Sieve | Marking multiples of each number to find all primes up to n at once | 10 |
| 🟡 | P / NP / NP-Complete | Solvable fast / checkable fast / the hardest problems whose solution is checkable fast | 11 |
| 🟡 | Reduction | Transforming one problem into another to show it is at least as hard | 11 |

---

## Skip for Now

- Implementing KMP, Rabin-Karp, or a suffix array from memory. Know the idea and when each is used
- Proving the Master Theorem, or deriving recurrences by hand for anything beyond the classic cases
- Network flow algorithms in full (Ford-Fulkerson, Edmonds-Karp). Know the problem shape only
- Approximation algorithms for NP-hard problems, beyond knowing they exist
- Advanced number theory: extended Euclidean algorithm, Chinese remainder theorem, matrix exponentiation, unless a specific problem needs them

## How to Proceed

1. Use topics 1 and 2 as they exist today: the `01-sorting` and `02-searching` folders. Read them fully before moving on.
2. Do topic 3 (recursion and divide and conquer) next. Nearly every later topic builds on it.
3. Do topics 4 to 6 (greedy, DP, backtracking) as one set. For each, work one classic example fully by hand before coding it.
4. Do topics 7 to 10 as a reference set: read each once, know when to reach for it, and come back when a specific problem needs it.
5. Read topic 11 once. It changes how you answer a question that looks unsolvable in reasonable time.
6. After each topic here, go practise the matching pattern and problems in `03-leetcode-patterns`. This folder teaches the "why it works"; that folder teaches "spot it and solve it fast".
7. For each topic: what it is, what problem it solves, how it works, its complexity and why, and one place it fails.
