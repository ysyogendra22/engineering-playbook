# Subarray Problems

> The key skill: look at the question and pick the right tool. This note is the decision guide.

#### 1. What Is It?

A **subarray** is a **continuous** part of an array. For an array of length `n` there are `n(n + 1) / 2` subarrays, so checking all of them costs `O(n²)` or more.

Most subarray questions fit one of a few patterns. The first job in an interview is to **pick the right one**.

| Question type | Tool | Needs | Note |
|---|---|---|---|
| maximum sum subarray | **Kadane** | any numbers | 10 |
| longest / shortest subarray with a rule (sum ≥ k, at most k zeros, no repeats) | **sliding window** | non-negative numbers (for sums) | 05 |
| count subarrays with sum `= k` | **prefix sum + HashMap** | any numbers (negatives OK) | 26 |
| many range-sum queries | **prefix sum** | — | 06 |
| product less than `k` | sliding window | positive numbers | this note |
| count subarrays with "at most k" then "exactly k" | `atMost(k) − atMost(k − 1)` | — | 27 |
| subarray with a sorted rule, monotonic | scan with two pointers | — | 04 |

**Decision rule for sums:**

```text
Are all numbers positive (or the rule is monotonic)?   → sliding window
Can numbers be negative?                                → prefix sum + HashMap
Do you want the maximum sum?                            → Kadane
```

#### 2. How It Works

*Subarray Product Less Than K* (LeetCode 713): count subarrays whose product is `< k`. Numbers are positive, so a window works: when you add a number the product grows, and when you remove one it shrinks.

`nums = [10, 5, 2, 6]`, `k = 100`

```text
right=0 (10): product 10   → window [10]          → 1 subarray ending here
right=1 (5):  product 50   → window [10,5]        → 2 subarrays ending here ([5], [10,5])
right=2 (2):  product 100 ≥ 100 → shrink: divide by 10 → 10, window [5,2]
              product 10   → 2 subarrays ending here ([2], [5,2])
right=3 (6):  product 60   → window [5,2,6]       → 3 subarrays ending here

total = 1 + 2 + 2 + 3 = 8
```

The trick: for every `right`, the number of **valid subarrays ending at `right`** is `right - left + 1`.

#### 3. Brute Force vs Optimized

| | Brute force | Window |
|---|---|---|
| Idea | check every start and end | slide two pointers |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` | `O(1)` |

```kotlin
fun productLessThanKBrute(nums: IntArray, k: Int): Int {
    var count = 0
    for (i in nums.indices) {
        var product = 1L
        for (j in i until nums.size) {
            product *= nums[j]
            if (product >= k) break
            count++
        }
    }
    return count
}
```

#### 4. Kotlin Code

```kotlin
// Subarray Product Less Than K (LeetCode 713)
fun numSubarrayProductLessThanK(nums: IntArray, k: Int): Int {
    if (k <= 1) return 0
    var product = 1
    var left = 0
    var count = 0
    for (right in nums.indices) {
        product *= nums[right]
        while (product >= k) product /= nums[left++]
        count += right - left + 1                         // all subarrays ending at right
    }
    return count
}

// Longest subarray with sum <= k (non-negative numbers): window
fun longestSubarraySumAtMost(nums: IntArray, k: Int): Int {
    var left = 0
    var sum = 0
    var best = 0
    for (right in nums.indices) {
        sum += nums[right]
        while (sum > k) sum -= nums[left++]
        best = maxOf(best, right - left + 1)
    }
    return best
}

// Longest Subarray of 1's After Deleting One Element (LeetCode 1493): at most one zero in the window
fun longestSubarray(nums: IntArray): Int {
    var left = 0
    var zeros = 0
    var best = 0
    for (right in nums.indices) {
        if (nums[right] == 0) zeros++
        while (zeros > 1) { if (nums[left] == 0) zeros--; left++ }
        best = maxOf(best, right - left)                  // minus 1 because one element must be deleted
    }
    return best
}

// Count all subarrays with sum k (negatives allowed): prefix sum + map (full note: 26)
fun subarraySum(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1
    var sum = 0
    var answer = 0
    for (x in nums) {
        sum += x
        answer += count[sum - k] ?: 0
        count[sum] = (count[sum] ?: 0) + 1
    }
    return answer
}
```

Checks: `numSubarrayProductLessThanK([10,5,2,6], 100)` → `8`. `longestSubarraySumAtMost([1,2,1,0,1], 3)` → `3`. `longestSubarray([1,1,0,1])` → `3`. `subarraySum([1,1,1], 2)` → `2`.

#### 5. Complexity

| Tool | Time | Space |
|---|---|---|
| Sliding window | `O(n)` | `O(1)` |
| Prefix sum + HashMap | `O(n)` | `O(n)` |
| Kadane | `O(n)` | `O(1)` |
| All subarrays (brute) | `O(n²)` | `O(1)` |

#### 6. Common Mistakes

1. **A sliding window with negative numbers** for a sum rule.
2. **Counting only one subarray per `right`.** There are `right - left + 1` that end there.
3. **`k <= 1` in the product problem** (division loop never ends). Return `0`.
4. **Confusing subarray (continuous) with subsequence.**
5. **Product overflow.** Use `Long` or compare with division.

#### 7. Say This in the Interview

1. "A subarray is continuous. Let me check: are the numbers all positive? If yes, a sliding window works in `O(n)`. If negatives are possible, I use prefix sums with a HashMap."
2. "For a maximum sum I use Kadane."
3. "Brute force is `O(n²)` over all start and end pairs."

#### 8. Quick Check

1. Which tool counts subarrays with sum `k` when negatives are allowed?
2. How many subarrays end at `right` when the window is `[left, right]`?

<details>
<summary>Answers</summary>

1. Prefix sum + HashMap.
2. `right - left + 1`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Medium) | Kadane |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Medium) | window, positives |
| 713 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) (Medium) | window, count |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium) | prefix sum + map |
| 974 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) (Medium) | remainders in a map |
| 1493 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) (Medium) | window with one zero |
| 862 | [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) (Hard) | prefix sums + deque |
