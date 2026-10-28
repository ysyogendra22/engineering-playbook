# Kadane's Algorithm / Maximum Subarray

> A classic. The idea is also the base of many dynamic programming questions.

#### 1. What Is It?

**Kadane's algorithm** finds the **maximum sum of a continuous subarray** in one pass.

The idea: at each position decide, "is it better to **extend** the best subarray ending at the previous position, or to **start fresh** here?"

```text
currentBest(i) = max( nums[i],  currentBest(i - 1) + nums[i] )
answer = the largest currentBest seen
```

If the running sum becomes negative, it only hurts the next numbers, so drop it and start again.

How to spot it: "maximum sum subarray", "best contiguous segment", "best time to buy and sell once", or any "maximum of the best ending here".

#### 2. How It Works

`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

```text
i  nums[i]  extend (cur + x)   start fresh (x)   cur   best
0    -2                         -2                -2    -2
1     1       -2 + 1 = -1        1                 1     1     (start fresh)
2    -3        1 - 3 = -2       -3                -2     1
3     4       -2 + 4 =  2        4                 4     4     (start fresh)
4    -1        4 - 1 =  3       -1                 3     4
5     2        3 + 2 =  5        2                 5     5
6     1        5 + 1 =  6        1                 6     6     ← best
7    -5        6 - 5 =  1       -5                 1     6
8     4        1 + 4 =  5        4                 5     6

answer 6   (the subarray [4, -1, 2, 1])
```

If **all numbers are negative**, the answer is the largest single number (so start `best` with `nums[0]`, not `0`).

#### 3. Brute Force vs Optimized

| | Brute force | Kadane |
|---|---|---|
| Idea | try every subarray | extend or restart |
| Time | `O(n²)` (running sum) or `O(n³)` | `O(n)` |
| Space | `O(1)` | `O(1)` |

```kotlin
fun maxSubArrayBrute(nums: IntArray): Int {
    var best = Int.MIN_VALUE
    for (i in nums.indices) {
        var sum = 0
        for (j in i until nums.size) {
            sum += nums[j]
            best = maxOf(best, sum)
        }
    }
    return best
}
```

#### 4. Kotlin Code

```kotlin
// Maximum Subarray (LeetCode 53)
fun maxSubArray(nums: IntArray): Int {
    var current = nums[0]
    var best = nums[0]
    for (i in 1 until nums.size) {
        current = maxOf(nums[i], current + nums[i])         // start fresh or extend
        best = maxOf(best, current)
    }
    return best
}

// The same, also returning where the subarray is
fun maxSubArrayRange(nums: IntArray): Triple<Int, Int, Int> {
    var current = nums[0]
    var best = nums[0]
    var start = 0
    var bestStart = 0
    var bestEnd = 0
    for (i in 1 until nums.size) {
        if (nums[i] > current + nums[i]) { current = nums[i]; start = i } else current += nums[i]
        if (current > best) { best = current; bestStart = start; bestEnd = i }
    }
    return Triple(best, bestStart, bestEnd)
}

// Maximum Product Subarray (LeetCode 152): keep both the max and the min (a negative flips them)
fun maxProduct(nums: IntArray): Int {
    var curMax = nums[0]
    var curMin = nums[0]
    var best = nums[0]
    for (i in 1 until nums.size) {
        val x = nums[i]
        val a = curMax * x
        val b = curMin * x
        curMax = maxOf(x, a, b)
        curMin = minOf(x, a, b)
        best = maxOf(best, curMax)
    }
    return best
}

// Best Time to Buy and Sell Stock (LeetCode 121): the same idea, with prices
fun maxProfit(prices: IntArray): Int {
    var minPrice = Int.MAX_VALUE
    var best = 0
    for (p in prices) {
        minPrice = minOf(minPrice, p)
        best = maxOf(best, p - minPrice)
    }
    return best
}
```

Checks: `maxSubArray([-2,1,-3,4,-1,2,1,-5,4])` → `6`. `maxSubArray([-3,-1,-2])` → `-1`. `maxProduct([2,3,-2,4])` → `6`. `maxProfit([7,1,5,3,6,4])` → `5`.

For a **circular** array (LeetCode 918) the answer is `max(normal Kadane, total - minimum subarray)`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Kadane | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Starting `best` at `0`.** If all numbers are negative, the answer is wrong. Start with `nums[0]`.
2. **Resetting to `0` instead of to `nums[i]`** (fails for all-negative arrays).
3. **Maximum product:** forgetting the minimum. Two negatives make a positive.
4. **Mixing up subarray and subsequence.** Kadane is for **continuous** parts.
5. **Empty array.**

#### 7. Say This in the Interview

1. "At each index I choose the better of two options: extend the previous subarray or start a new one at this index."
2. "That is one pass: `O(n)` time and `O(1)` space. Brute force is `O(n²)`."

#### 8. Quick Check

1. What is the answer for `[-5, -2, -9]`?
2. Why start `best` with `nums[0]` and not `0`?

<details>
<summary>Answers</summary>

1. `-2` (the best single number).
2. A subarray must contain at least one number. `0` would give an answer that does not exist.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy) | track the minimum so far |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Medium) | Kadane |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (Medium) | track max and min |
| 918 | [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) (Medium) | total minus the minimum subarray |
| 1749 | [Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) (Medium) | max Kadane and min Kadane |
| 1493 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) (Medium) | window variant |
