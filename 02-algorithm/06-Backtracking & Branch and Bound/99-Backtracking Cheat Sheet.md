# Backtracking Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–11.

#### 1. Key Takeaways

1. Backtracking = **choose, explore, un-choose**. It is a depth-first walk of a **decision tree**.
2. **Draw the tree first**: what does one level decide, what are the options, when is a path complete?
3. **Save a copy** of the path (`path.toList()`), and **always undo** the choice.
4. **Prune early**: check constraints before recursing. Sort first when you can `break`.
5. Complexity = number of nodes: **subsets `2ⁿ`**, **permutations `n!`**, combinations `C(n, k)`. The output size sets a floor.
6. **Duplicates:** sort, then skip `nums[i] == nums[i − 1]` when `i > start` (siblings only).
7. **Repeated state `(index, remaining)`?** Add a memo, and it becomes DP. If you must **list** all answers, stay with backtracking.
8. **Optimisation** problems: branch and bound (a best-so-far and an optimistic bound).

#### 2. Complexity Table

| Problem | Time | Space |
|---|---|---|
| Subsets | `O(n · 2ⁿ)` | `O(n)` |
| Permutations | `O(n · n!)` | `O(n)` |
| Combinations (size `k`) | `O(k · C(n, k))` | `O(k)` |
| Combination Sum | up to `O(2^(target / min))` | `O(target / min)` |
| Generate Parentheses | `O(4ⁿ / √n)` | `O(n)` |
| Word Search | `O(m · n · 3^L)` | `O(L)` |
| Palindrome Partitioning | `O(n · 2ⁿ)` | `O(n)` |
| N-Queens | about `O(n!)` | `O(n)` |
| Sudoku | `O(9^empty)` worst | `O(1)` |
| TSP brute force / Held-Karp | `O(n!)` / `O(2ⁿ · n²)` | `O(n)` / `O(2ⁿ · n)` |

Practical limits: `n!` up to about 10, `2ⁿ` up to about 20 to 25.

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Note |
|---|---|---|
| "all subsets" | include / exclude or start index, save at every node | 01, 09 |
| "all combinations of size k", "sum equals target" | start index; reuse → recurse `i` | 09 |
| "all permutations / arrangements" | `used[]` array | 01, 09 |
| "unique" with duplicates in the input | sort + skip equal siblings | 10 |
| "all valid strings of length n" | build constraints into the options | 02 |
| "find a word / path in a grid" | mark, explore 4 neighbours, restore | 11 |
| "all ways to split a string" | cut positions, prune on validity | 11 |
| "place n items without conflict" | attacked sets, one item per row | 07 |
| "fill the blanks under rules" | next empty cell, try digits | 07 |
| "maximise / minimise" over a subset | branch and bound, or DP | 06 |
| "visit every city once, shortest" | TSP: brute force, or bitmask DP | 08 |
| "count the ways" | DP, not backtracking | 05 |

#### 4. Templates to Memorise

**Generic**

```kotlin
fun backtrack(/* level state */) {
    if (complete) { result.add(path.toList()); return }
    for (choice in options) {
        if (invalid(choice)) continue          // prune
        path.add(choice)                       // choose
        backtrack(/* next level */)            // explore
        path.removeAt(path.size - 1)           // un-choose
    }
}
```

**Subsets / combinations (start index)**

```kotlin
fun backtrack(start: Int) {
    result.add(path.toList())
    for (i in start until nums.size) { path.add(nums[i]); backtrack(i + 1); path.removeAt(path.size - 1) }
}
```

**Permutations (`used`)**

```kotlin
for (i in nums.indices) {
    if (used[i]) continue
    used[i] = true; path.add(nums[i]); backtrack(); path.removeAt(path.size - 1); used[i] = false
}
```

**Skip duplicates (sorted)**

```kotlin
if (i > start && nums[i] == nums[i - 1]) continue          // subsets / combinations
if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue   // permutations
```

**Combination Sum (reuse, prune)**

```kotlin
for (i in start until c.size) { if (c[i] > remaining) break; path.add(c[i]); backtrack(i, remaining - c[i]); path.removeAt(path.size - 1) }
```

**Grid DFS**

```kotlin
val saved = board[r][c]; board[r][c] = '#'
val found = dfs(r + 1, c, i + 1) || dfs(r - 1, c, i + 1) || dfs(r, c + 1, i + 1) || dfs(r, c - 1, i + 1)
board[r][c] = saved
```

**N-Queens attacked sets**

```kotlin
if (cols[c] || diag1[row + c] || diag2[row - c + n]) continue
```

**Branch and bound**

```kotlin
if (value > best) best = value
if (bound(i, weight, value) <= best) return               // prune
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Better |
|---|---|---|
| Subsets | bitmask over `2ⁿ` | backtracking (can prune) |
| Combinations (size `k`) | all subsets, keep size `k` | start index + size check |
| Unique subsets | generate all + `Set` | sort + skip equal siblings |
| Valid parentheses | all `2^(2n)` strings, validate | add `)` only if `close < open`: 22 calls vs 127 for `n = 3` |
| N-Queens | `nⁿ` placements, then check | one per row + attacked sets |
| Count subsets with sum `K` | `O(2ⁿ)` recursion | memo / DP `O(n · K)` |
| Knapsack | `O(2ⁿ)` | branch and bound, or DP |
| TSP | `O(n!)` | Held-Karp `O(2ⁿ · n²)` |

#### 6. Common Mistakes and Edge Cases

1. **Saving the path itself, not a copy.**
2. **Forgetting to undo** (list, `used`, grid cell, attacked sets).
3. **Wrong start index** (`i` vs `i + 1`, or `0` for combinations).
4. **No sort** before skipping duplicates; `i > 0` instead of `i > start`.
5. **Pruning after the recursive call**, or with a condition that removes valid answers (negatives).
6. **Checking the grid cell before the bounds check.**
7. **Using backtracking for counting** when DP works.
8. **`Int` overflow** for `n!` (use `Long`; `21!` overflows even that).
9. **Edge cases:** empty input (`[[]]` for subsets), one element, all equal, target `0`, no solution (`[]`).

#### 7. What to Say Out Loud

1. "I'll use backtracking: choose an element, recurse, then undo it. I save a copy of the path when it's complete."
2. "Let me draw the decision tree: each level chooses ..., the base case is ..."
3. "I'll prune early: I sort and break when a candidate exceeds the remaining target."
4. "The tree has `2ⁿ` leaves, so exponential time is expected. If the same state repeats, I'd memoize and it becomes DP."
5. "With duplicates I sort and skip an equal value at the same level."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Medium | [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) | two options per letter |
| Medium | [Subsets](https://leetcode.com/problems/subsets/) | start index |
| Medium | [Permutations](https://leetcode.com/problems/permutations/) | `used[]` |
| Medium | [Combinations](https://leetcode.com/problems/combinations/) | size `k` |
| Medium | [Combination Sum](https://leetcode.com/problems/combination-sum/) | reuse + prune |
| Medium | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | one choice per digit |
| Medium | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | constraints |
| Medium | [Subsets II](https://leetcode.com/problems/subsets-ii/) | skip duplicates |
| Medium | [Permutations II](https://leetcode.com/problems/permutations-ii/) | skip duplicates |
| Medium | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | skip duplicates |
| Medium | [Word Search](https://leetcode.com/problems/word-search/) | grid |
| Medium | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | cuts |
| Medium | [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) | cuts + prune |
| Medium | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | buckets |
| Hard | [N-Queens](https://leetcode.com/problems/n-queens/) | attacked sets |
| Hard | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | digit constraints |
| Hard | [Word Search II](https://leetcode.com/problems/word-search-ii/) | trie + backtracking |
