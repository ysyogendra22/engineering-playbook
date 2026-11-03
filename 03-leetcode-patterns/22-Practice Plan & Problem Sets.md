# Practice Plan & Problem Sets

> Depth beats volume. 80 to 120 problems you truly understand are worth more than 500 you half remember.

#### 1. What Is It?

A plan for **how** to practise, a six-week schedule, and a topic-wise problem set (Easy → Medium → one harder) with direct links.

**Principles**

1. **One pattern at a time.** Read the note, write the template from memory, then solve problems.
2. **Per pattern:** 3 easy, 3 medium, 1 harder variant.
3. **Struggle first, then compare.** Try for 20 to 30 minutes. Then read a better solution and write down the difference.
4. **Repeat.** Redo a problem after 3 days and after 2 weeks, from a blank editor.
5. **Name the pattern first.** Before coding, say the pattern and the signal that told you.
6. **Finish with mixed and timed sets,** then mock interviews out loud.

#### 2. How It Works

**Daily routine (about 90 minutes)**

| Minutes | Step |
|---|---|
| 10 | Redo one old problem (spaced repetition) |
| 40 | One new problem: pattern, brute force, plan, code, test |
| 20 | Read the best solution. Write 2 lines: what you missed, the key insight |
| 20 | One extra problem from the same pattern, or a variant |

**Spaced repetition**

| After | Redo |
|---|---|
| 1 day | only if you got it wrong |
| 3 days | problems you needed hints on |
| 2 weeks | all problems, from a blank editor, timed |

**Tracker (keep it in a note)**

| Problem | Pattern | Date | Result | What I missed / key insight | Redo on |
|---|---|---|---|---|---|
| 3 Longest Substring | sliding window | | solved with a hint | forgot `prev >= left` | |

**How to rate yourself**

| Result | Meaning |
|---|---|
| A | solved alone, optimal, tested |
| B | solved with one hint, or not optimal |
| C | needed the solution |

Redo every B and C.

**Mock interviews.** In the last two weeks, do timed 45-minute sessions: random medium, speak the 9 steps aloud (note 01), no autocomplete. Use a friend, or record yourself.

#### 3. Weak Plan vs Strong Plan

| Weak | Strong |
|---|---|
| Solve 500 random problems | 100 problems by pattern, each understood |
| Read the solution after 5 minutes | Struggle 20 to 30 minutes, then learn |
| Never redo problems | Redo after 3 days and 2 weeks |
| Memorise code | Memorise the template and the reason |
| Practise only with autocomplete | Practise in a plain editor |
| Skip failed problems | Log them and revisit |

#### 4. Six-Week Plan

| Week | Topics | Goal | Problems |
|---|---|---|---|
| 1 | 1, 2, 3, 4, 5 | The method, Kotlin tools, two pointers, sliding window | about 15 |
| 2 | 6, 7, 8, 9 | Fast and slow, prefix sum, binary search, intervals | about 20 |
| 3 | 10, 11, 12, 13 | Monotonic stack, heap, BFS, DFS | about 20 |
| 4 | 14, 15, 16, 17 | Backtracking, graphs, topological sort, union find | about 20 |
| 5 | 18, 19 | Dynamic programming and greedy | about 20 |
| 6 | 20, 21, mixed | Extra patterns, timed mixed sets, mock interviews | about 15 + mocks |

**Short on time (2 weeks):** topics 1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 15, 18, 21. Do only the 🟢 problems.

**Named lists to follow later:** Blind 75, NeetCode 150, Grind 75. They overlap heavily with the sets below.

#### 5. Brute Force vs Optimized

For practice problems the same idea applies: after solving, ask "what was my first brute force, and what removed the extra work?" Write one line per problem in the tracker. Over time you see the same few moves: **hash map, sort, two pointers, heap, prefix sum, memoization**.

#### 6. Common Mistakes

1. **Collecting solutions** instead of understanding them.
2. **Only easy problems,** or only hard ones.
3. **Changing topics every day.** Stay on one pattern until the template is automatic.
4. **No review.** Without redo, most of it is gone in two weeks.
5. **No timing.** Interviews are 45 minutes. Practise at that speed near the end.
6. **Skipping edge cases** in practice, then missing them in the interview.
7. **Skipping speaking out loud.** It is a separate skill.

#### 7. Say This in the Interview

Practise saying, within the first minute of a new problem:

1. "This is a ... problem because I see ..."
2. "A brute force would be ... which is `O(...)`"
3. "To improve it, I'll use ..."

If you can say those three lines in under a minute for most problems, you are ready.

#### 8. Quick Check

1. After you finish a problem, what two things do you write in the tracker?
2. When do you redo a problem you needed a hint for?

<details>
<summary>Answers</summary>

1. What you missed, and the key insight (plus the pattern).
2. After 3 days, and again after 2 weeks.

</details>

#### 9. Problem Sets by Pattern

Easy → Medium → one harder. Premium problems are marked; use the free alternative given.

| # | Pattern | Easy | Medium | Harder |
|---|---|---|---|---|
| 4 | Two Pointers | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/), [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/), [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/), [3Sum](https://leetcode.com/problems/3sum/), [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) |
| 5 | Sliding Window | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/), [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/), [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/), [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| 6 | Fast & Slow | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/), [Happy Number](https://leetcode.com/problems/happy-number/) | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/), [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/), [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | [Reorder List](https://leetcode.com/problems/reorder-list/) |
| 7 | Prefix Sum | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/), [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/), [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/), [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/), [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) |
| 8 | Binary Search | [Binary Search](https://leetcode.com/problems/binary-search/), [Search Insert Position](https://leetcode.com/problems/search-insert-position/), [First Bad Version](https://leetcode.com/problems/first-bad-version/) | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/), [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/), [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) |
| 9 | Merge Intervals | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | [Merge Intervals](https://leetcode.com/problems/merge-intervals/), [Insert Interval](https://leetcode.com/problems/insert-interval/), [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [Car Pooling](https://leetcode.com/problems/car-pooling/) (free version of Meeting Rooms II) |
| 10 | Monotonic Stack | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/), [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/), [Baseball Game](https://leetcode.com/problems/baseball-game/) | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/), [Online Stock Span](https://leetcode.com/problems/online-stock-span/), [Car Fleet](https://leetcode.com/problems/car-fleet/) | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |
| 11 | Top K Elements | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/), [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/), [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/), [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) |
| 12 | BFS | [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/), [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/), [Flood Fill](https://leetcode.com/problems/flood-fill/) | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/), [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/), [01 Matrix](https://leetcode.com/problems/01-matrix/) | [Word Ladder](https://leetcode.com/problems/word-ladder/) |
| 13 | DFS | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/), [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/), [Path Sum](https://leetcode.com/problems/path-sum/) | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/), [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/), [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) |
| 14 | Backtracking | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | [Subsets](https://leetcode.com/problems/subsets/), [Permutations](https://leetcode.com/problems/permutations/), [Combination Sum](https://leetcode.com/problems/combination-sum/), [Word Search](https://leetcode.com/problems/word-search/) | [N-Queens](https://leetcode.com/problems/n-queens/) |
| 15 | Graph Traversal | [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/), [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/), [Clone Graph](https://leetcode.com/problems/clone-graph/), [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/), [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) |
| 16 | Topological Sort | (none) | [Course Schedule](https://leetcode.com/problems/course-schedule/), [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/), [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | [Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/) |
| 17 | Union Find | [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/), [Redundant Connection](https://leetcode.com/problems/redundant-connection/), [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) |
| 18 | Dynamic Programming | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/), [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/), [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | [House Robber](https://leetcode.com/problems/house-robber/), [Coin Change](https://leetcode.com/problems/coin-change/), [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) |
| 19 | Greedy | [Assign Cookies](https://leetcode.com/problems/assign-cookies/), [Lemonade Change](https://leetcode.com/problems/lemonade-change/), [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Jump Game](https://leetcode.com/problems/jump-game/), [Jump Game II](https://leetcode.com/problems/jump-game-ii/), [Gas Station](https://leetcode.com/problems/gas-station/) | [Candy](https://leetcode.com/problems/candy/) |
| 20 | More Patterns | [Two Sum](https://leetcode.com/problems/two-sum/), [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/), [Single Number](https://leetcode.com/problems/single-number/) | [Group Anagrams](https://leetcode.com/problems/group-anagrams/), [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/), [LRU Cache](https://leetcode.com/problems/lru-cache/) | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) |
