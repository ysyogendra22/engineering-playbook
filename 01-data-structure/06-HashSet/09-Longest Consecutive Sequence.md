# Longest Consecutive Sequence

> Put every number in a set. Start counting **only from numbers that begin a run** (no `x − 1` in the set). That makes it `O(n)`, not `O(n log n)`.

#### 1. What Is It?

Given an **unsorted** array, find the length of the longest run of **consecutive integers** (`x, x + 1, x + 2, ...`), in **`O(n)`** time. (LeetCode 128.)

`[100, 4, 200, 1, 3, 2]` → the run `1, 2, 3, 4` has length `4`.

The `O(n)` requirement rules out sorting (`O(n log n)`). A `HashSet` gives `O(1)` membership, which is the key.

**Signals:** "consecutive", "longest streak", "in O(n)", "unsorted array".

#### 2. How It Works

1. Put all numbers in a set (this also removes duplicates).
2. For each number `x` in the set, check if `x − 1` is in the set.
   - **If yes**, `x` is in the middle of a run. **Skip it.** Another number is the start of that run.
   - **If no**, `x` **starts a run**. Count upwards: `x + 1`, `x + 2`, ... while they are in the set.
3. The answer is the longest count.

```text
set = {100, 4, 200, 1, 3, 2}
100: is 99 in the set? no  → start. count 100 → 1.            length 1
4:   is 3 in the set? yes → skip (not a start)
200: is 199? no → start. length 1
1:   is 0? no → start. 1, 2, 3, 4 are all in the set → length 4  ← best
3:   is 2? yes → skip
2:   is 1? yes → skip
answer 4
```

```text
number line:   1  2  3  4 ............ 100 ............ 200
runs:         [1..4] (length 4)       [100]            [200]
```

**Why `O(n)` and not `O(n²)`?** The inner `while` only runs from a **run start**. Each number is visited by the inner loop **at most once** (as part of one run). So the total work across all runs is `O(n)`, plus `O(n)` for the outer loop.

**Alternatives**

| Method | Time | Space |
|---|---|---|
| Sort, then count runs | `O(n log n)` | `O(1)` or `O(n)` |
| Set + run starts | **`O(n)`** | `O(n)` |
| Union-Find (merge `x` with `x + 1`) | `O(n α(n))` | `O(n)` |

#### 3. Brute Force vs Optimized

| Approach | Time | Space |
|---|---|---|
| For each `x`, extend upward with a `list.contains` | `O(n³)` | `O(1)` |
| For each `x`, extend upward with a set (no start check) | `O(n²)` worst | `O(n)` |
| Sort + scan | `O(n log n)` | `O(1)` to `O(n)` |
| **Set + only start from run starts** | **`O(n)`** | `O(n)` |

```kotlin
// Sort and scan: simple, O(n log n)
fun longestConsecutiveSort(nums: IntArray): Int {
    if (nums.isEmpty()) return 0
    val sorted = nums.distinct().sorted()
    var best = 1
    var run = 1
    for (i in 1 until sorted.size) {
        run = if (sorted[i] == sorted[i - 1] + 1) run + 1 else 1
        best = maxOf(best, run)
    }
    return best
}
```

#### 4. Kotlin Code

```kotlin
// Longest Consecutive Sequence (LeetCode 128): O(n)
fun longestConsecutive(nums: IntArray): Int {
    val set = nums.toHashSet()
    var best = 0
    for (x in set) {
        if (x - 1 in set) continue                 // not the start of a run
        var end = x
        while (end + 1 in set) end++               // extend the run
        best = maxOf(best, end - x + 1)
    }
    return best
}
```

Checks: `longestConsecutive(intArrayOf(100, 4, 200, 1, 3, 2))` → `4`. `longestConsecutive(intArrayOf(0, 3, 7, 2, 5, 8, 4, 6, 0, 1))` → `9` (`0..8`, with a duplicate `0`). `longestConsecutive(intArrayOf())` → `0`. `longestConsecutive(intArrayOf(5))` → `1`. `longestConsecutive(intArrayOf(1, 2, 0, 1))` → `3`. `longestConsecutive(intArrayOf(-1, -2, -3, 5))` → `3`. `longestConsecutiveSort(...)` gives the same answers.

Overflow note: `x - 1` and `end + 1` on `Int.MIN_VALUE` / `Int.MAX_VALUE` wrap around. For extreme inputs use `Long`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Set + run starts | `O(n)` | `O(n)` |
| Sort + scan | `O(n log n)` | `O(n)` (with `distinct`) |

#### 6. Common Mistakes

1. **Starting the count from every number** (no `x − 1` check). It becomes `O(n²)` on a long run.
2. **Sorting** when the question requires `O(n)`.
3. **Counting duplicates** twice in a run (`[1, 2, 2, 3]` is length `3`, not `4`).
4. **Iterating the array** (with duplicates) instead of the set (harmless for correctness, but repeats work).
5. **Empty array** returning `1` instead of `0`.
6. **Overflow** at the `Int` limits.

#### 7. Say This in the Interview

1. "Sorting is `O(n log n)`. To get `O(n)` I put the numbers in a set, and only start counting from numbers whose predecessor `x − 1` is not in the set."
2. "The inner `while` only runs from run starts, so each number is touched at most once by it, giving `O(n)` overall."
3. "Duplicates don't matter because the set removes them."

#### 8. Quick Check

1. Which numbers start a run in `{1, 2, 3, 10, 11}`?
2. Why skip a number whose `x − 1` is in the set?
3. The answer for `[1, 1, 1]`?

<details>
<summary>Answers</summary>

1. `1` and `10`.
2. It is in the middle of a run that is counted from its start. Counting from it would repeat work and cause `O(n²)`.
3. `1`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (Medium) | set + run starts |
| 298 | [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) (Medium, premium) | tree DFS |
| 549 | [Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) (Medium, premium) | tree DFS, both ways |
| 674 | [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) (Easy) | one pass |
| 1887 | [Reduction Operations to Make the Array Elements Equal](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/) (Medium) | sorting by values |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy) | the basic set idea |
