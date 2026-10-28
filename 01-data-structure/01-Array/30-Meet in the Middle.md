# Meet in the Middle

> A rare, advanced idea. Read it so you can recognise it. It is for small `n` (about 30–40) when brute force is `2^n`.

#### 1. What Is It?

**Meet in the middle** splits the input into **two halves**, solves each half separately, and then **combines** the answers.

If the brute force tries all `2^n` subsets, that is too slow for `n = 40` (about a trillion). Each half has only `2^(n/2)` subsets (a million for `n = 40`). Combining two sorted lists of a million sums is fast. So the total is about `2^(n/2)` work instead of `2^n`.

How to spot it: `n` is **around 30 to 40** (too big for `2^n`, but small enough for `2^(n/2)`), and the question asks about **subsets or subsequences** (subset sum, closest sum, split into two groups).

#### 2. How It Works

*Subset sum with `n = 40`*: is there a subset with sum `target`?

```text
1. Split the array into a left half and a right half (20 numbers each).
2. List all subset sums of the left half  → up to 2^20 values.
3. List all subset sums of the right half → up to 2^20 values.
4. Sort the right sums.
5. For each left sum s, binary search the right sums for (target − s).
   If found → yes.
```

Example: `nums = [3, 34, 4, 12]`, `target = 16`

```text
left half  [3, 34]  → sums {0, 3, 34, 37}
right half [4, 12]  → sums {0, 4, 12, 16}   sorted
for s = 0:  need 16 → found in the right sums  ✓   (the subset {4, 12})
```

The same idea is used to find the subset sum **closest** to a target: for each left sum, find the closest right sum with binary search.

#### 3. Brute Force vs Optimized

| | Brute force | Meet in the middle |
|---|---|---|
| Idea | try all subsets | split in two, combine |
| Time | `O(2^n)` | `O(2^(n/2) · n)` |
| Space | `O(n)` | `O(2^(n/2))` |
| Works for `n` up to | about 20–25 | about 40 |

```kotlin
fun subsetSumBrute(nums: IntArray, target: Long): Boolean {
    fun go(i: Int, sum: Long): Boolean {
        if (i == nums.size) return sum == target
        return go(i + 1, sum) || go(i + 1, sum + nums[i])         // skip it, or take it
    }
    return go(0, 0)
}
```

#### 4. Kotlin Code

```kotlin
// All subset sums of an array
private fun subsetSums(a: IntArray): LongArray {
    var sums = longArrayOf(0)
    for (x in a) {
        val next = LongArray(sums.size * 2)
        for (i in sums.indices) {
            next[i] = sums[i]                       // without x
            next[sums.size + i] = sums[i] + x       // with x
        }
        sums = next
    }
    return sums
}

// Is there a subset with the exact sum `target`? n up to about 40.
fun subsetSumExists(nums: IntArray, target: Long): Boolean {
    val half = nums.size / 2
    val left = subsetSums(nums.copyOfRange(0, half))
    val right = subsetSums(nums.copyOfRange(half, nums.size))
    right.sort()
    for (s in left) {
        if (right.binarySearch(target - s) >= 0) return true      // a negative result means "not found"
    }
    return false
}

// Closest subset sum to the target (the idea behind LeetCode 1755 Closest Subsequence Sum)
fun closestSubsetSum(nums: IntArray, goal: Long): Long {
    val half = nums.size / 2
    val left = subsetSums(nums.copyOfRange(0, half))
    val right = subsetSums(nums.copyOfRange(half, nums.size))
    right.sort()
    var best = Long.MAX_VALUE
    var answer = 0L
    for (s in left) {
        val need = goal - s
        var idx = right.binarySearch(need)
        if (idx < 0) idx = -idx - 1                                // the first right sum >= need
        for (j in intArrayOf(idx - 1, idx)) {                      // check both neighbours
            if (j in right.indices) {
                val total = s + right[j]
                val diff = Math.abs(total - goal)
                if (diff < best) { best = diff; answer = total }
            }
        }
    }
    return answer
}
```

Checks: `subsetSumExists([3,34,4,12], 16)` → `true`. `subsetSumExists([3,34,4,12], 30)` → `false`. `closestSubsetSum([5,-7,3,5], 6)` → `6`.

**Related idea:** *4Sum II* (LeetCode 454) is a meet-in-the-middle in disguise: sums of two arrays go into a HashMap, and the other two arrays look up the complement (HashMap folder, note 08).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Subset sums of each half | `O(2^(n/2))` | `O(2^(n/2))` |
| Sort + binary search | `O(2^(n/2) · n)` | — |
| Brute force | `O(2^n)` | — |

#### 6. Common Mistakes

1. **Using it when `n` is large** (for example 100). Even `2^50` is too much.
2. **Forgetting to sort** before the binary search.
3. **Using `Int` for sums.** They can overflow. Use `Long`.
4. **Splitting unevenly** and ending up with one huge half.
5. **Mixing it up with dynamic programming.** If the *sum* is small (not `n`), use DP (knapsack).
6. **Not handling the empty subset** (sum `0`).

#### 7. Say This in the Interview

1. "`n` is about 40, so `2^n` is too slow. I split the array in two halves, list the subset sums of each half (`2^20` each), sort one list, and binary search for the match. That is about `O(2^(n/2) · n)`."
2. "If the target sum were small instead, I would use dynamic programming."

#### 8. Quick Check

1. About how many subset sums does a half of 40 numbers have?
2. For which size of `n` is meet in the middle useful?

<details>
<summary>Answers</summary>

1. `2^20`, about a million.
2. Around 30 to 40, where `2^n` is too big but `2^(n/2)` is fine.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 454 | [4Sum II](https://leetcode.com/problems/4sum-ii/) (Medium) | two halves + HashMap |
| 1755 | [Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/) (Hard) | closest subset sum, `n ≤ 40` |
| 2035 | [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/) (Hard) | halves grouped by subset size |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (Medium) | dynamic programming, for comparison |
