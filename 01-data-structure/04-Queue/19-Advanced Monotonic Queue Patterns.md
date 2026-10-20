# Advanced Monotonic Queue Patterns

> Learn note 13 (Monotonic Queue) first. These are Medium and Hard questions that use the same deque.

#### 1. What Is It?

The basic monotonic queue gives the max or min of a **sliding window**. The advanced patterns use the same deque trick in three bigger ways:

| Pattern | Question type | Example |
|---|---|---|
| **Two deques** | window max **and** min together | Longest Subarray, Abs Diff ≤ Limit (1438) |
| **DP + window max** | `dp[i]` needs the best of the last `k` values | Jump Game VI (1696) |
| **Prefix sums + deque** | shortest subarray with a sum rule, negatives allowed | Shortest Subarray with Sum ≥ K (862) |

The rule stays the same: keep only the candidates that can still become the answer, in sorted order. Remove from the **back** when a new item is better. Remove from the **front** when an item expires (or is used up).

#### 2. How It Works

**Pattern A — two deques** (LeetCode 1438). Find the longest subarray where `max - min <= limit`. Keep a decreasing deque (window max at the front) and an increasing deque (window min at the front). If `max - min > limit`, move `left` forward until it is valid again.

```text
nums = [8, 2, 4, 7], limit = 4

right=0 [8]        max 8, min 8, diff 0       length 1
right=1 [8,2]      max 8, min 2, diff 6 > 4 → left moves → [2]    length 1
right=2 [2,4]      max 4, min 2, diff 2       length 2
right=3 [2,4,7]    max 7, min 2, diff 5 > 4 → left moves → [4,7]  length 2

answer 2
```

**Pattern B — DP with a window max** (LeetCode 1696). From index `i` you can jump to any of the next `k` indexes. Maximise the total score.

```text
dp[i] = nums[i] + max(dp[i-k], ..., dp[i-1])
```

The inner `max` is a sliding window maximum over `dp`. Use a decreasing deque of indexes.

**Pattern C — prefix sums + deque** (LeetCode 862). Numbers can be **negative**, so a normal window does not work. Use prefix sums: `sum(i..j-1) = prefix[j] - prefix[i]`. Keep a deque of indexes whose prefix sums are **increasing**.

- **Front:** while `prefix[j] - prefix[front] >= k`, record the length `j - front` and remove the front. A later `j` can never give a shorter subarray for that start.
- **Back:** while `prefix[back] >= prefix[j]`, remove the back. The new index is later and has a smaller (or equal) prefix, so it is a better start.

#### 3. Kotlin Code

```kotlin
// Longest Continuous Subarray With Absolute Diff <= limit (LeetCode 1438)
fun longestSubarray(nums: IntArray, limit: Int): Int {
    val maxDeque = ArrayDeque<Int>()               // indexes, values decreasing
    val minDeque = ArrayDeque<Int>()               // indexes, values increasing
    var left = 0
    var best = 0

    for (right in nums.indices) {
        while (maxDeque.isNotEmpty() && nums[maxDeque.last()] <= nums[right]) maxDeque.removeLast()
        maxDeque.addLast(right)
        while (minDeque.isNotEmpty() && nums[minDeque.last()] >= nums[right]) minDeque.removeLast()
        minDeque.addLast(right)

        while (nums[maxDeque.first()] - nums[minDeque.first()] > limit) {
            left++
            if (maxDeque.first() < left) maxDeque.removeFirst()
            if (minDeque.first() < left) minDeque.removeFirst()
        }
        best = maxOf(best, right - left + 1)
    }
    return best
}

// Jump Game VI (LeetCode 1696)
fun maxResult(nums: IntArray, k: Int): Int {
    val n = nums.size
    val dp = IntArray(n)
    dp[0] = nums[0]
    val deque = ArrayDeque<Int>()                  // indexes, dp values decreasing
    deque.addLast(0)

    for (i in 1 until n) {
        while (deque.first() < i - k) deque.removeFirst()           // too far to jump from
        dp[i] = nums[i] + dp[deque.first()]                          // best earlier score
        while (deque.isNotEmpty() && dp[deque.last()] <= dp[i]) deque.removeLast()
        deque.addLast(i)
    }
    return dp[n - 1]
}

// Shortest Subarray with Sum at Least K (LeetCode 862)
fun shortestSubarray(nums: IntArray, k: Int): Int {
    val n = nums.size
    val prefix = LongArray(n + 1)
    for (i in 0 until n) prefix[i + 1] = prefix[i] + nums[i]

    val deque = ArrayDeque<Int>()                  // indexes, prefix values increasing
    var best = Int.MAX_VALUE

    for (j in 0..n) {
        while (deque.isNotEmpty() && prefix[j] - prefix[deque.first()] >= k) {
            best = minOf(best, j - deque.removeFirst())
        }
        while (deque.isNotEmpty() && prefix[deque.last()] >= prefix[j]) deque.removeLast()
        deque.addLast(j)
    }
    return if (best == Int.MAX_VALUE) -1 else best
}
```

Checks: `longestSubarray([8,2,4,7], 4)` → `2`. `longestSubarray([10,1,2,4,7,2], 5)` → `4`. `maxResult([1,-1,-2,4,-7,3], 2)` → `7`. `shortestSubarray([2,-1,2], 3)` → `3`. `shortestSubarray([1], 1)` → `1`.

#### 4. Complexity

| Problem | Time | Space |
|---|---|---|
| 1438, 1696, 862 | `O(n)` | `O(n)` |
| Brute force versions | `O(n²)` or `O(n · k)` | — |

Each index enters and leaves a deque once.

#### 5. Common Mistakes

1. **Storing values instead of indexes.**
2. **Wrong comparison direction** for max versus min.
3. **862: forgetting prefix sums**, or using `Int` for them. Use `LongArray`.
4. **862: not removing the front after recording a length.** A later `j` cannot be shorter for that start.
5. **Using a plain sliding window with negative numbers.** It fails. Use prefix sums + deque.
6. **1438: forgetting to drop deque fronts that fall left of `left`.**

#### 6. Say This in the Interview

1. "Brute force is `O(n·k)` or `O(n²)`. A monotonic deque makes it `O(n)`."
2. "I keep only candidates that can still be the answer, in sorted order. Each index enters and leaves once."
3. "With negative numbers a normal window fails, so I use prefix sums and an increasing deque."

#### 7. Quick Check

1. Which two deques does Longest Subarray (1438) use?
2. Why are prefix sums needed in 862?

<details>
<summary>Answers</summary>

1. One decreasing (window max) and one increasing (window min).
2. The numbers can be negative, so adding more elements does not always grow the sum. Prefix sums turn "sum of a range" into a difference of two values, which a deque can handle.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 239 | Sliding Window Maximum (Hard) | the base pattern (note 13) |
| 1438 | Longest Continuous Subarray With Absolute Diff ≤ Limit (Medium) | two deques |
| 1696 | Jump Game VI (Medium) | dp + window max |
| 1425 | Constrained Subsequence Sum (Hard) | dp + window max |
| 862 | Shortest Subarray with Sum at Least K (Hard) | prefix sums + deque |
| 2398 | Maximum Number of Robots Within Budget (Hard) | window max + running sum |
