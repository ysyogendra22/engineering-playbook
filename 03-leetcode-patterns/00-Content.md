# LeetCode Patterns: Learning & Interview Roadmap

For a mobile engineer preparing for coding interviews. The goal is to **recognise the pattern, apply a template, and explain the complexity**, in Kotlin.
This folder has **its own numbering, 1 to 22**. Topics 4 to 18 are the 15 essential patterns from your original list, in the same order. Each topic gets its own doc later.

Source list: https://leetcode.com/discuss/post/7347258/15-essential-dsa-patterns-for-tech-inter-nxem/

**How to read references:** a plain number (`7`) is a topic in this folder. `DS` is `01-data-structure` (for example `DS Graph`). `ALG` is `02-algorithm` (for example `ALG Searching`). `BE`, `SD`, `MOB`, and `ARCH` are the numbered roadmaps in `04-backend-engineering`, `05-system-design`, `06-mobile-engineering`, and `09-architecture`.

**Problem numbers** are LeetCode's. If a number and a title ever disagree, trust the title. Problems marked *(premium)* need a paid account, so use the free alternative.

**How this fits with the other folders:** your notes in `01-data-structure` and `02-algorithm` teach each structure and algorithm on its own. This folder teaches **when to reach for which one**. Read the matching notes first, then use this roadmap to practise the pattern.

**Marks:**

| Mark | Meaning |
|---|---|
| 🟢 | **Must have.** Comes up in most coding interviews. Learn first. |
| 🟡 | **Good to have.** Learn after the 🟢 items are solid. |
| (New) | Added beyond your original 15 patterns. |

---

## Index

| #   | Topic                                     | Stage                 |
| --- | ----------------------------------------- | --------------------- |
| 1   | How to Solve a Coding Problem             | 1. Method             |
| 2   | Complexity & Constraints                  | 1. Method             |
| 3   | Kotlin for Coding Interviews (New)        | 1. Method             |
| 4   | Two Pointers                              | 2. Array & String     |
| 5   | Sliding Window                            | 2. Array & String     |
| 6   | Fast & Slow Pointers                      | 2. Array & String     |
| 7   | Prefix Sum                                | 2. Array & String     |
| 8   | Binary Search                             | 2. Array & String     |
| 9   | Merge Intervals                           | 2. Array & String     |
| 10  | Monotonic Stack                           | 2. Array & String     |
| 11  | Top K Elements                            | 2. Array & String     |
| 12  | BFS                                       | 3. Trees & Graphs     |
| 13  | DFS                                       | 3. Trees & Graphs     |
| 14  | Backtracking                              | 3. Trees & Graphs     |
| 15  | Graph Traversal                           | 3. Trees & Graphs     |
| 16  | Topological Sort                          | 3. Trees & Graphs     |
| 17  | Union Find                                | 3. Trees & Graphs     |
| 18  | Dynamic Programming                       | 4. Optimization       |
| 19  | Greedy (New)                              | 4. Optimization       |
| 20  | More Patterns to Know (New)               | 5. Extra Patterns     |
| 21  | Coding Interview Answer Points (New)      | 6. Interview & Practice |
| 22  | Practice Plan & Problem Sets (New)        | 6. Interview & Practice |

**Short on time:** 1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 15, 18, 21. 🟢 items only.

**Glossary and cheat sheet:** a "signal to pattern" table and the terms to learn first are at the end.

---

# What to Follow on Any Problem

*The same nine steps work for every coding problem. Say each one out loud.*

| Step | What to do | Output |
|---|---|---|
| 1. Clarify | Restate the problem. Ask about input size, ranges, duplicates, negatives, empty input, and what to return | A short list of assumptions |
| 2. Examples | Work one normal example and one edge case by hand | Two examples with expected answers |
| 3. Brute force | Say the simplest solution and its complexity, even if it is slow | Brute force and its Big-O |
| 4. Find the pattern | Look at the signals (see the cheat sheet), and use the constraints as a hint | A named pattern, or a short list of candidates |
| 5. Improve | Say what is repeated or wasted, and what data structure removes it | The better approach and its Big-O |
| 6. Plan before code | Describe the steps in plain words, and confirm with the interviewer | A 3 to 5 line plan |
| 7. Code | Write clean Kotlin with clear names and small helpers | Working code |
| 8. Test | Dry-run the normal example, then the edge cases | Traced results, and any bug fixed |
| 9. Wrap up | State time and space complexity, and one possible improvement | Final complexity and trade-offs |

**Priority order when time is short:** steps 1, 4, and 8. Most lost interviews come from solving the wrong problem, missing the pattern, or shipping code that was never tested.

---

# Pattern Cheat Sheet: Signal to Pattern

*Read the problem statement and the constraints. Match what you see.*

| If you see... | Try | Topic |
|---|---|---|
| Sorted array, pair or triplet with a target, palindrome, remove duplicates in place | Two pointers | 4 |
| Longest, shortest, or best contiguous subarray or substring with a condition | Sliding window | 5 |
| Cycle in a linked list, middle of a list, repeated value in a sequence | Fast and slow pointers | 6 |
| Many range-sum queries, or "subarray sum equals K" | Prefix sum (with a hash map) | 7 |
| Sorted or monotonic data, "minimum X such that...", target in O(log n) | Binary search | 8 |
| Overlapping ranges, meetings, scheduling, merge or insert | Merge intervals | 9 |
| Next greater or smaller element, temperatures, histogram | Monotonic stack | 10 |
| K largest, K smallest, K most frequent, running median | Heap (top K) | 11 |
| Shortest path with equal weights, level order, minimum steps, spreading | BFS | 12 |
| Tree depth, all paths, subtree values, explore a region | DFS | 13 |
| All combinations, permutations, subsets, or "place things under rules" | Backtracking | 14 |
| Nodes and edges, islands, components, cycle detection, clone a graph | Graph traversal | 15 |
| Prerequisites, dependencies, build order | Topological sort | 16 |
| "Are these connected?", merging groups, cycle in an undirected graph | Union find | 17 |
| Count the ways, min or max cost, choices with overlapping subproblems | Dynamic programming | 18 |
| A local best choice seems to give the global best | Greedy | 19 |
| Need O(1) lookup, counting, or "have I seen this?" | Hash map or set | 20 |
| Reverse or rearrange a linked list in place | Pointer manipulation | 20 |

**Constraints hint at the complexity you need:**

| Input size (n) | Aim for | Likely approach |
|---|---|---|
| up to about 20 | O(2ⁿ) or O(n!) | Backtracking, bitmask |
| up to about 500 | O(n³) | Triple loops, some DP |
| up to about 5,000 | O(n²) | Nested loops, 2D DP |
| up to about 100,000 | O(n log n) or O(n) | Sorting, heap, binary search, hash map, sliding window |
| up to about 1,000,000 | O(n) | Single pass, hash map, prefix sum |
| very large (10⁹) | O(log n) or math | Binary search, formula |

---

# Stage 1: Method

## 1. How to Solve a Coding Problem

- 🟢 The nine-step process above, practised until it is automatic
- 🟢 Ask clarifying questions before writing code
- 🟢 Start with brute force, then improve it
- 🟢 Think out loud, and check in with the interviewer
- 🟢 Test with your own examples, including edge cases
- 🟢 Edge cases to check every time: empty, one element, duplicates, negatives, very large, all the same
- 🟡 Time management for a 45-minute round: understand 5, plan 5, code 20, test 10, wrap up 5
- 🟡 What to do when you are stuck: simplify, draw an example, try a smaller input, ask for a hint
- 🟡 How to recover from a bug without panicking
- 🟡 Turn a solved problem into a template you can reuse

## 2. Complexity & Constraints

- 🟢 Big-O for time and space, and the common classes: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- 🟢 Read the constraints to choose the approach (see the table above)
- 🟢 Count loops, recursion depth, and data structures to get the complexity
- 🟢 Recursion uses stack space: depth times frame size
- 🟢 The cost of common operations: array, list, hash map, set, heap, sorted structures (`DS`)
- 🟡 Amortized cost (for example, dynamic array growth)
- 🟡 Time vs space trade-offs
- 🟡 Best, average, and worst case (for example, quicksort, hash collisions)
- 🟡 Solving recurrences for divide and conquer, at a basic level (`ALG Sorting`)
- 🟡 Integer overflow and precision

## 3. Kotlin for Coding Interviews (New)

- 🟢 Collections: `IntArray`, `Array<IntArray>`, `List`, `MutableList`, `HashMap`, `HashSet`, `ArrayDeque`, `PriorityQueue`
- 🟢 Sorting with comparators: `sortedBy`, `sortedWith`, `compareBy`, sorting arrays of pairs or intervals
- 🟢 `PriorityQueue` with a custom comparator (min-heap vs max-heap)
- 🟢 Maps: `getOrPut`, `getOrDefault`, `merge`, `groupBy`, `countBy` patterns
- 🟢 Strings: `StringBuilder`, `toCharArray`, `chars`, and character arithmetic
- 🟢 Ranges: `until`, `..`, `downTo`, `step`, and off-by-one care
- 🟢 Overflow: use `Long` for sums and products, and know the `Int` limits
- 🟡 Data classes for state, `Pair` and `Triple`, and destructuring
- 🟡 Sequences vs lists for large data
- 🟡 Recursion depth limits, and converting to an explicit stack
- 🟡 Extension functions to keep code short and readable
- 🟡 Common pitfalls: `IntArray` is not a `List<Int>`, `equals` on arrays, `substring` cost, mutation while iterating
- 🟡 Reading input format for online judges vs functions in interviews

---

# Stage 2: Array & String Patterns

## 4. Two Pointers

*Notes: `DS Array`, `ALG Searching`.*

- 🟢 Recognise it: a sorted array, a pair or triplet with a target, a palindrome, in-place removal
- 🟢 Opposite ends: `left` and `right` move toward each other
- 🟢 Same direction: a read pointer and a write pointer (remove duplicates, move zeroes)
- 🟢 Why it works: the sorted order lets you decide which pointer to move
- 🟢 Complexity: O(n) time, O(1) space, after any sort
- 🟡 Skipping duplicates in 3Sum and 4Sum
- 🟡 Two pointers on two arrays or two strings (merge, compare)
- 🟡 Partitioning (Dutch national flag)

**Classic problems**

- 🟢 Valid Palindrome (125)
- 🟢 Two Sum II: Input Array Is Sorted (167)
- 🟢 3Sum (15)
- 🟢 Container With Most Water (11)
- 🟢 Remove Duplicates from Sorted Array (26)
- 🟢 Move Zeroes (283)
- 🟡 Trapping Rain Water (42)
- 🟡 Sort Colors (75)

## 5. Sliding Window

*Notes: `DS Array` (fixed and variable size).*

- 🟢 Recognise it: a contiguous subarray or substring, with "longest", "shortest", "at most K", or "of size K"
- 🟢 Fixed-size window: add one element, remove one element
- 🟢 Variable-size window: expand the right side, shrink the left side while the window is invalid
- 🟢 Track window state with a running sum, a count, or a frequency map
- 🟢 Complexity: O(n) time, because each element enters and leaves once
- 🟡 "At most K" minus "at most K−1" for "exactly K"
- 🟡 Windows with a monotonic deque (window maximum)
- 🟡 Common bugs: shrinking at the wrong time, and updating the answer in the wrong place

**Classic problems**

- 🟢 Maximum Average Subarray I (643)
- 🟢 Best Time to Buy and Sell Stock (121)
- 🟢 Longest Substring Without Repeating Characters (3)
- 🟢 Longest Repeating Character Replacement (424)
- 🟢 Permutation in String (567)
- 🟡 Minimum Window Substring (76)
- 🟡 Sliding Window Maximum (239)

## 6. Fast & Slow Pointers

*Notes: `DS LinkedList`.*

- 🟢 Recognise it: a cycle in a linked list, the middle of a list, or a sequence that may repeat
- 🟢 Two pointers move at different speeds (one step and two steps)
- 🟢 Detect a cycle: they meet if there is one
- 🟢 Find the middle: when the fast pointer ends, the slow pointer is in the middle
- 🟢 Complexity: O(n) time, O(1) space, instead of a hash set
- 🟡 Find where the cycle starts (a second phase)
- 🟡 Cycle detection on a number sequence (happy number)
- 🟡 Combine with reversal (palindrome linked list)

**Classic problems**

- 🟢 Linked List Cycle (141)
- 🟢 Middle of the Linked List (876)
- 🟢 Linked List Cycle II (142)
- 🟢 Happy Number (202)
- 🟡 Find the Duplicate Number (287)
- 🟡 Palindrome Linked List (234)

## 7. Prefix Sum

*Notes: `DS Array`, `DS HashMap`.*

- 🟢 Recognise it: many range-sum queries, or a subarray sum condition
- 🟢 Build `prefix[i]` = sum of the first `i` elements, so `sum(l..r) = prefix[r+1] - prefix[l]`
- 🟢 Prefix sum plus a hash map for "subarray sum equals K", including negative numbers
- 🟢 Complexity: O(n) to build, O(1) per query
- 🟡 2D prefix sums for matrix regions
- 🟡 Prefix product and "product except self"
- 🟡 Difference array for many range updates (`20`)
- 🟡 Prefix counts of a value (for example, equal 0s and 1s)

**Classic problems**

- 🟢 Range Sum Query: Immutable (303)
- 🟢 Subarray Sum Equals K (560)
- 🟢 Product of Array Except Self (238)
- 🟢 Contiguous Array (525)
- 🟡 Range Sum Query 2D: Immutable (304)
- 🟡 Continuous Subarray Sum (523)

## 8. Binary Search

*Notes: `ALG Searching` (including rotated arrays and binary search on the answer).*

- 🟢 Recognise it: sorted or monotonic data, or a yes/no condition that flips once
- 🟢 The standard template with `left`, `right`, and `mid`, and avoiding infinite loops and overflow
- 🟢 First and last occurrence, lower bound and upper bound
- 🟢 Rotated sorted array
- 🟢 Binary search on the answer: "smallest value that works", with a check function
- 🟢 Complexity: O(log n) per search, and O(n log range) for search on the answer
- 🟡 Search in a 2D matrix
- 🟡 Peak element, and searching on a mountain array
- 🟡 Search with duplicates
- 🟡 Real-world uses: finding the first bad version, time-based lookups

**Classic problems**

- 🟢 Binary Search (704)
- 🟢 Search Insert Position (35)
- 🟢 Find First and Last Position of Element in Sorted Array (34)
- 🟢 Search in Rotated Sorted Array (33)
- 🟢 Find Minimum in Rotated Sorted Array (153)
- 🟢 Koko Eating Bananas (875)
- 🟡 Capacity To Ship Packages Within D Days (1011)
- 🟡 Time Based Key-Value Store (981)
- 🟡 Median of Two Sorted Arrays (4)

## 9. Merge Intervals

*Notes: sorting in `ALG Sorting`.*

- 🟢 Recognise it: ranges that overlap, meetings, schedules, insert or merge
- 🟢 Sort by start time first
- 🟢 Overlap test: `next.start <= current.end`
- 🟢 Merge by extending the end: `max(current.end, next.end)`
- 🟢 Complexity: O(n log n) for the sort, O(n) for the pass
- 🟡 Insert an interval into a sorted list
- 🟡 Counting the most overlaps at once (a heap of end times, or a sweep of start and end events)
- 🟡 Intersections of two interval lists
- 🟡 Greedy interval problems: keep the earliest end (`19`)

**Classic problems**

- 🟢 Merge Intervals (56)
- 🟢 Insert Interval (57)
- 🟢 Non-overlapping Intervals (435)
- 🟡 Minimum Number of Arrows to Burst Balloons (452)
- 🟡 Interval List Intersections (986)
- 🟡 Meeting Rooms II (253, premium). Free alternative: Car Pooling (1094)

## 10. Monotonic Stack

*Notes: `DS Stack`.*

- 🟢 Recognise it: "next greater element", "next smaller element", "how many days until...", or spans
- 🟢 Keep a stack whose values stay in increasing or decreasing order
- 🟢 Pop while the current value breaks the order, and each pop is an answer
- 🟢 Store indexes, not only values
- 🟢 Complexity: O(n), because each element is pushed and popped once
- 🟡 Circular arrays (go around twice)
- 🟡 Largest rectangle in a histogram
- 🟡 Monotonic deque for sliding-window maximum (`5`)
- 🟡 Basic stack problems first: matching brackets, min stack

**Classic problems**

- 🟢 Valid Parentheses (20)
- 🟢 Daily Temperatures (739)
- 🟢 Next Greater Element I (496)
- 🟢 Online Stock Span (901)
- 🟡 Car Fleet (853)
- 🟡 Largest Rectangle in Histogram (84)

## 11. Top K Elements

*Notes: `DS Heap`.*

- 🟢 Recognise it: "K largest", "K smallest", "K most frequent", "K closest"
- 🟢 Use a heap of size K: a min-heap for the K largest, and a max-heap for the K smallest
- 🟢 Count frequencies with a hash map first, then use a heap
- 🟢 Complexity: O(n log K), better than sorting when K is small
- 🟢 Kotlin `PriorityQueue` with a comparator (`3`)
- 🟡 Quickselect: O(n) average (`ALG Searching`)
- 🟡 Bucket sort for frequencies
- 🟡 Merge K sorted lists with a heap
- 🟡 Two heaps for a running median

**Classic problems**

- 🟢 Kth Largest Element in an Array (215)
- 🟢 Top K Frequent Elements (347)
- 🟢 K Closest Points to Origin (973)
- 🟢 Merge k Sorted Lists (23)
- 🟡 Find Median from Data Stream (295)
- 🟡 Task Scheduler (621)
- 🟡 Reorganize String (767)

---

# Stage 3: Trees & Graphs

## 12. BFS

*Notes: `DS Tree` (level-order), `DS Graph` (BFS, multi-source BFS, shortest path in an unweighted graph).*

- 🟢 Recognise it: level by level, the shortest path with equal weights, the minimum number of steps
- 🟢 A queue, a `visited` set, and processing one level at a time
- 🟢 Mark nodes visited when you add them to the queue, not when you remove them
- 🟢 Grids as graphs: four or eight directions, with bounds checks
- 🟢 Complexity: O(V + E) for graphs, O(rows × cols) for grids
- 🟡 Multi-source BFS: start from all sources at once (rotting oranges, 01 matrix)
- 🟡 BFS on states (word ladder, open the lock)
- 🟡 0-1 BFS with a deque, and Dijkstra for weighted edges (`15`)
- 🟡 Bidirectional BFS

**Classic problems**

- 🟢 Binary Tree Level Order Traversal (102)
- 🟢 Binary Tree Right Side View (199)
- 🟢 Rotting Oranges (994)
- 🟢 01 Matrix (542)
- 🟢 Shortest Path in Binary Matrix (1091)
- 🟡 Word Ladder (127)
- 🟡 Open the Lock (752)

## 13. DFS

*Notes: `DS Tree` (DFS traversals, height, path sum, LCA), `DS Graph` (DFS).*

- 🟢 Recognise it: tree depth, all root-to-leaf paths, subtree values, or exploring a whole region
- 🟢 Recursive template, with a clear base case
- 🟢 Preorder, inorder, and postorder, and when each fits
- 🟢 Return values up the recursion (height, sum, boolean) vs pass state down (parameters)
- 🟢 Grid DFS (flood fill), with a `visited` set or in-place marking
- 🟢 Complexity: O(n) time, and O(h) stack space where h is the depth
- 🟡 Iterative DFS with an explicit stack
- 🟡 Global result variables (diameter, maximum path sum)
- 🟡 Tree problems that need both children's results (postorder)
- 🟡 DFS on a BST using the sorted property

**Classic problems**

- 🟢 Maximum Depth of Binary Tree (104)
- 🟢 Invert Binary Tree (226)
- 🟢 Path Sum (112)
- 🟢 Validate Binary Search Tree (98)
- 🟢 Lowest Common Ancestor of a Binary Tree (236)
- 🟢 Diameter of Binary Tree (543)
- 🟢 Number of Islands (200)
- 🟡 Kth Smallest Element in a BST (230)
- 🟡 Binary Tree Maximum Path Sum (124)

## 14. Backtracking

- 🟢 Recognise it: "all combinations", "all permutations", "all subsets", or placing things under rules
- 🟢 The template: choose, explore, un-choose
- 🟢 The decision tree: draw it before coding
- 🟢 Copy the current path when saving a result
- 🟢 Pruning: stop early when a branch cannot work
- 🟢 Skipping duplicates: sort first, then skip equal siblings
- 🟢 Complexity: usually O(2ⁿ) or O(n!) for the number of results
- 🟡 Start index for combinations, `used` array for permutations
- 🟡 Backtracking on a grid (word search)
- 🟡 Constraint problems (N-Queens, Sudoku)
- 🟡 Turning backtracking into DP when subproblems repeat (`18`)

**Classic problems**

- 🟢 Subsets (78)
- 🟢 Permutations (46)
- 🟢 Combination Sum (39)
- 🟢 Letter Combinations of a Phone Number (17)
- 🟢 Generate Parentheses (22)
- 🟢 Word Search (79)
- 🟡 Subsets II (90)
- 🟡 Palindrome Partitioning (131)
- 🟡 N-Queens (51)

## 15. Graph Traversal

*Notes: `DS Graph` (representation, connected components, cycle detection, grid as graph, Dijkstra, MST, cloning).*

- 🟢 Represent a graph: adjacency list, adjacency matrix, edge list
- 🟢 Directed vs undirected, weighted vs unweighted, connected vs disconnected
- 🟢 Traverse every component: loop over all nodes and start a search from each unvisited one
- 🟢 Count connected components and islands
- 🟢 Cycle detection: undirected (parent check) and directed (recursion stack or colours)
- 🟢 Clone a graph with a map from old node to new node
- 🟢 Complexity: O(V + E)
- 🟡 Bipartite check with two colours
- 🟡 Dijkstra for weighted shortest paths, with a priority queue
- 🟡 Minimum spanning tree (Kruskal, Prim)
- 🟡 Implicit graphs: states as nodes
- 🟡 Common edge cases: self loops, duplicate edges, disconnected graphs, empty graph

**Classic problems**

- 🟢 Number of Islands (200)
- 🟢 Clone Graph (133)
- 🟢 Number of Provinces (547)
- 🟢 Pacific Atlantic Water Flow (417)
- 🟢 Surrounded Regions (130)
- 🟢 Is Graph Bipartite? (785)
- 🟡 Network Delay Time (743)
- 🟡 Cheapest Flights Within K Stops (787)
- 🟡 Min Cost to Connect All Points (1584)

## 16. Topological Sort

*Notes: `DS Graph` (topological sort, Kahn's algorithm, dependency graphs, DAGs).*

- 🟢 Recognise it: prerequisites, dependencies, build order, "can all tasks finish?"
- 🟢 It works only on a directed acyclic graph (DAG)
- 🟢 Kahn's algorithm (BFS): compute in-degrees, start with in-degree 0, and remove edges as you go
- 🟢 A cycle exists if you cannot process every node
- 🟢 DFS-based version: reverse postorder
- 🟢 Complexity: O(V + E)
- 🟡 Several valid orders, and getting the lexicographically smallest with a heap
- 🟡 Levels and the longest path in a DAG (parallel courses)
- 🟡 Ordering from a custom rule (alien dictionary)

**Classic problems**

- 🟢 Course Schedule (207)
- 🟢 Course Schedule II (210)
- 🟡 Minimum Height Trees (310)
- 🟡 Find All Possible Recipes from Given Supplies (2115)
- 🟡 Alien Dictionary (269, premium)

## 17. Union Find

*Notes: `DS Graph` (Union-Find, path compression, union by rank or size, Kruskal).*

- 🟢 Recognise it: "are these connected?", merging groups, counting components as edges arrive
- 🟢 Two operations: `find` (which group?) and `union` (merge two groups)
- 🟢 Path compression and union by rank or size
- 🟢 Cycle detection in an undirected graph: if `find(a) == find(b)`, adding the edge makes a cycle
- 🟢 Complexity: nearly O(1) per operation (inverse Ackermann)
- 🟡 Counting components after each union
- 🟡 Group things by a key (accounts merge)
- 🟡 Kruskal's minimum spanning tree
- 🟡 Union find vs DFS: when each fits (dynamic connectivity vs one-time traversal)

**Classic problems**

- 🟢 Number of Provinces (547)
- 🟢 Redundant Connection (684)
- 🟢 Accounts Merge (721)
- 🟡 Satisfiability of Equality Equations (990)
- 🟡 Most Stones Removed with Same Row or Column (947)
- 🟡 Number of Connected Components in an Undirected Graph (323, premium). Free alternative: Number of Provinces (547)

---

# Stage 4: Optimization

## 18. Dynamic Programming

- 🟢 Recognise it: "count the ways", "minimum or maximum cost", or choices with repeated subproblems
- 🟢 Two conditions: optimal substructure and overlapping subproblems
- 🟢 The steps: define the state, write the transition, set the base cases, choose the order, and find the answer
- 🟢 Top-down (memoization) and bottom-up (tabulation)
- 🟢 1D DP: climbing stairs, house robber, coin change
- 🟢 2D DP: grid paths, longest common subsequence, edit distance
- 🟢 Subsequence DP: longest increasing subsequence
- 🟢 Knapsack style: subset sum, partition, coin change
- 🟢 Complexity: number of states × work per state
- 🟡 Space optimization: keep only the previous row or two values
- 🟡 String DP: palindromes, word break, decode ways
- 🟡 State machine DP (buy and sell stock with cooldown)
- 🟡 Interval DP and bitmask DP (names only)
- 🟡 Reconstructing the actual answer, not only the value
- 🟡 Why greedy fails, and when DP is needed instead (`19`)

**Classic problems**

- 🟢 Climbing Stairs (70)
- 🟢 House Robber (198)
- 🟢 Coin Change (322)
- 🟢 Maximum Subarray (53)
- 🟢 Unique Paths (62)
- 🟢 Longest Increasing Subsequence (300)
- 🟢 Word Break (139)
- 🟢 Longest Common Subsequence (1143)
- 🟢 Partition Equal Subset Sum (416)
- 🟡 Decode Ways (91)
- 🟡 Longest Palindromic Substring (5)
- 🟡 Minimum Path Sum (64)
- 🟡 Edit Distance (72)
- 🟡 Coin Change II (518)
- 🟡 Target Sum (494)
- 🟡 Best Time to Buy and Sell Stock with Cooldown (309)

## 19. Greedy (New)

- 🟢 Recognise it: a local best choice seems to lead to the global best
- 🟢 Sort first, then make the best choice at each step
- 🟢 Prove it, or find a counter-example: greedy is easy to get wrong
- 🟢 Interval scheduling: pick the interval that ends earliest
- 🟢 Complexity: usually O(n log n) for the sort, and O(n) for the pass
- 🟡 Jump game: track the farthest reachable index
- 🟡 Greedy with a heap (task scheduler, reorganize string)
- 🟡 Greedy vs DP: how to tell (`18`)
- 🟡 Exchange argument as a proof idea

**Classic problems**

- 🟢 Best Time to Buy and Sell Stock II (122)
- 🟢 Jump Game (55)
- 🟢 Jump Game II (45)
- 🟢 Assign Cookies (455)
- 🟡 Gas Station (134)
- 🟡 Partition Labels (763)
- 🟡 Non-overlapping Intervals (435)
- 🟡 Task Scheduler (621)

---

# Stage 5: Extra Patterns

## 20. More Patterns to Know (New)

- 🟢 Hash map and hash set: counting, lookup, "have I seen this?", grouping (`DS HashMap`, `DS HashSet`)
- 🟢 Linked list rearrangement: reverse, merge two lists, remove the nth node from the end (`DS LinkedList`)
- 🟢 Design problems: LRU cache (hash map plus doubly linked list), min stack, insert and delete in O(1)
- 🟢 Kadane's algorithm for the maximum subarray
- 🟢 Trie for prefix search (`DS Trie`)
- 🟡 Bit manipulation: XOR tricks, counting bits, checking and setting a bit
- 🟡 Cyclic sort for numbers in a range (missing number, first missing positive)
- 🟡 Difference array and sweep line for range updates and overlaps
- 🟡 Matrix problems: rotate, spiral, set zeroes
- 🟡 Segment tree and Fenwick tree (names and purpose)
- 🟡 String matching: KMP and rolling hash (names and purpose)
- 🟡 Math: gcd, primes, modular arithmetic, fast power

**Classic problems**

- 🟢 Two Sum (1)
- 🟢 Group Anagrams (49)
- 🟢 Longest Consecutive Sequence (128)
- 🟢 Reverse Linked List (206)
- 🟢 Merge Two Sorted Lists (21)
- 🟢 LRU Cache (146)
- 🟢 Min Stack (155)
- 🟢 Implement Trie (208)
- 🟡 Reorder List (143)
- 🟡 Single Number (136)
- 🟡 Missing Number (268)
- 🟡 Insert Delete GetRandom O(1) (380)
- 🟡 Rotate Image (48)
- 🟡 Spiral Matrix (54)
- 🟡 Word Search II (212)

---

# Stage 6: Interview & Practice

## 21. Coding Interview Answer Points (New)

- 🟢 Restate the problem, and confirm the input and output
- 🟢 Say the brute force first, then the improvement
- 🟢 Name the pattern and the reason: "sorted input and a pair target, so two pointers"
- 🟢 Explain the plan before writing code, and confirm it
- 🟢 Narrate while coding, and use clear variable names
- 🟢 Dry-run with an example, and trace the variables
- 🟢 State time and space complexity, and where they come from
- 🟡 Answer common follow-ups: "can you do better?", "what if the input is huge or streaming?", "what if there are duplicates?", "can you do it in place?"
- 🟡 Handle a hint gracefully, and say what you learned from it
- 🟡 Write code that is easy to test: small helpers and no hidden state
- 🟡 Discuss trade-offs between two valid approaches
- 🟡 Common traps: coding too early, ignoring edge cases, and going silent

## 22. Practice Plan & Problem Sets (New)

- 🟢 Learn one pattern at a time: read the notes, write the template, then solve problems
- 🟢 For each pattern: three easy, three medium, and one harder variant
- 🟢 Solve without looking, then compare with a better solution and write down the difference
- 🟢 Revisit problems after 3 days and after 2 weeks (spaced repetition)
- 🟢 Keep a tracker: problem, pattern, what you missed, and the key insight
- 🟢 Do timed mixed sets and mock interviews out loud, near the end
- 🟡 Depth over volume: 80 to 120 problems you truly understand beat 500 you half remember
- 🟡 Problem lists by name: Blind 75, NeetCode 150, Grind 75
- 🟡 Practise reading a problem and naming the pattern in under a minute
- 🟡 Practise on a plain editor or whiteboard, without autocomplete

**A six-week plan**

| Week | Topics | Goal |
|---|---|---|
| 1 | 1, 2, 3, 4, 5 | The method, Kotlin tools, two pointers, sliding window |
| 2 | 6, 7, 8, 9 | Fast and slow, prefix sum, binary search, intervals |
| 3 | 10, 11, 12, 13 | Monotonic stack, heap, BFS, DFS |
| 4 | 14, 15, 16, 17 | Backtracking, graphs, topological sort, union find |
| 5 | 18, 19 | Dynamic programming and greedy |
| 6 | 20, 21, plus mixed sets | Extra patterns, timed mixed practice, and mock interviews |

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
| 🟡 | Amortized cost | The average cost per operation over a long sequence | 2 |
| 🟡 | Fast and slow pointers | Two pointers at different speeds, used for cycles and middles | 6 |
| 🟡 | Difference array | Store changes at range ends so many range updates are cheap | 7, 20 |
| 🟡 | Lower / upper bound | The first position not less than / greater than a value | 8 |
| 🟡 | Multi-source BFS | BFS that starts from several nodes at the same time | 12 |
| 🟡 | Dijkstra | Shortest path in a weighted graph with non-negative weights | 15 |
| 🟡 | MST | Minimum spanning tree: connects all nodes with the least total weight | 15, 17 |
| 🟡 | Kahn's algorithm | Topological sort by repeatedly removing nodes with in-degree 0 | 16 |
| 🟡 | Path compression / union by rank | Two tricks that keep union find nearly constant time | 17 |
| 🟡 | Knapsack | Choosing items under a limit to get the best value | 18 |
| 🟡 | Kadane's algorithm | Maximum subarray sum in one pass | 20 |
| 🟡 | Trie | A tree of characters used for prefix search | 20 |
| 🟡 | Bitmask | Using the bits of an integer to represent a set | 20 |
| 🟡 | Sweep line | Process events in sorted order to handle overlaps | 20 |

---

## Skip for Now

- Very hard problems (rated hard with rare tricks) until the 🟢 patterns feel easy
- Advanced data structures: segment trees, suffix arrays, and heavy graph algorithms such as max flow
- Competitive-programming speed tricks. Interviews reward clarity
- Memorizing solutions. Learn the pattern and the reason it works
- Language-specific micro-optimizations

## How to Proceed

1. Do topics 1 to 3 first. The method and Kotlin tools make every later topic easier.
2. Take one pattern at a time, in order. Read your matching notes in `01-data-structure` and `02-algorithm`, write the template from memory, then solve the classic problems.
3. After each pattern, do one mixed problem and try to name the pattern before you read any hints.
4. Do topics 12 to 17 (trees and graphs) carefully. They cover a large share of medium and hard questions.
5. Do topic 18 slowly. Practise defining the state and the transition on paper before coding.
6. Finish with topics 21 and 22: timed mixed sets and mock interviews out loud.
7. For each pattern: what it is, when the signals appear, the template, the complexity, and one way it fails.
