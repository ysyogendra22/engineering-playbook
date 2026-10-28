# Sliding Window

> Very common in FAANG interviews. Use it for the longest, shortest or best **continuous** part of an array or string.

#### 1. What Is It?

A **sliding window** is a continuous range `[left, right]` of the array. You **slide** it by moving `right` forward (the window grows) and `left` forward (the window shrinks). You keep a running value for the window (a sum, a count) and update it in `O(1)` when the window moves.

Two kinds:

| Kind | Window size | Example |
|---|---|---|
| **Fixed size** | always `k` | maximum sum of `k` numbers |
| **Variable size** | grows and shrinks to keep a rule true | longest substring without repeats |

How to spot it: "longest / shortest / maximum / count of a **continuous** part (subarray or substring) that satisfies a rule". With numbers, the rule usually needs **non-negative** values. If negatives are allowed, use prefix sums (notes 06, 26).

#### 2. How It Works

**Fixed size.** Maximum sum of 3 numbers in `[2, 1, 5, 1, 3, 2]`:

```text
window [2,1,5] sum 8
slide: add 1, remove 2 → [1,5,1] sum 7
slide: add 3, remove 1 → [5,1,3] sum 9   ← best
slide: add 2, remove 5 → [1,3,2] sum 6
answer 9
```

**Variable size.** Shortest subarray with sum at least 7 in `[2, 3, 1, 2, 4, 3]` (positive numbers):

```text
Rule for every step: expand right; while the rule holds, record the length and shrink left.

right=0..3: window [2,3,1,2] sum 8 ≥ 7 → length 4, shrink: remove 2 → [3,1,2] sum 6 < 7 stop
right=4:    add 4 → [3,1,2,4] sum 10 ≥ 7 → length 4, shrink: [1,2,4] sum 7 ≥ 7 → length 3, shrink: [2,4] sum 6 stop
right=5:    add 3 → [2,4,3] sum 9 ≥ 7 → length 3, shrink: [4,3] sum 7 ≥ 7 → length 2 ← best
answer 2
```

The template for a variable window:

```text
left = 0
for right in 0 until n:
    add nums[right] to the window
    while the window breaks the rule (or, for "shortest", while it satisfies the rule):
        remove nums[left] from the window; left++
    update the answer using the window
```

Each index enters and leaves once, so the total is `O(n)` even with the inner `while`.

#### 3. Brute Force vs Optimized

| | Brute force | Sliding window |
|---|---|---|
| Idea | try every start and end | move two pointers once |
| Time | `O(n²)` or `O(n · k)` | `O(n)` |
| Space | `O(1)` | `O(1)` (or `O(k)` with a map) |

```kotlin
fun maxSumBrute(nums: IntArray, k: Int): Int {
    var best = Int.MIN_VALUE
    for (i in 0..nums.size - k) {
        var sum = 0
        for (j in i until i + k) sum += nums[j]          // recomputed every time: O(k)
        best = maxOf(best, sum)
    }
    return best
}
```

#### 4. Kotlin Code

```kotlin
// Fixed size: maximum sum of k consecutive numbers (Maximum Average Subarray I is the same / k)
fun maxSumOfSizeK(nums: IntArray, k: Int): Int {
    var sum = 0
    for (i in 0 until k) sum += nums[i]
    var best = sum
    for (i in k until nums.size) {
        sum += nums[i] - nums[i - k]                      // add the new item, remove the old one
        best = maxOf(best, sum)
    }
    return best
}

// Variable size, shortest: Minimum Size Subarray Sum (LeetCode 209), positive numbers
fun minSubArrayLen(target: Int, nums: IntArray): Int {
    var left = 0
    var sum = 0
    var best = Int.MAX_VALUE
    for (right in nums.indices) {
        sum += nums[right]
        while (sum >= target) {
            best = minOf(best, right - left + 1)
            sum -= nums[left]
            left++
        }
    }
    return if (best == Int.MAX_VALUE) 0 else best
}

// Variable size, longest: Longest Substring Without Repeating Characters (LeetCode 3)
fun lengthOfLongestSubstring(s: String): Int {
    val lastSeen = HashMap<Char, Int>()
    var left = 0
    var best = 0
    for (right in s.indices) {
        val prev = lastSeen[s[right]]
        if (prev != null && prev >= left) left = prev + 1       // jump left past the repeat
        lastSeen[s[right]] = right
        best = maxOf(best, right - left + 1)
    }
    return best
}

// Variable size with a budget: Max Consecutive Ones III (LeetCode 1004): flip at most k zeros
fun longestOnes(nums: IntArray, k: Int): Int {
    var left = 0
    var zeros = 0
    var best = 0
    for (right in nums.indices) {
        if (nums[right] == 0) zeros++
        while (zeros > k) {                                     // too many zeros: shrink
            if (nums[left] == 0) zeros--
            left++
        }
        best = maxOf(best, right - left + 1)
    }
    return best
}
```

Checks: `maxSumOfSizeK([2,1,5,1,3,2], 3)` → `9`. `minSubArrayLen(7, [2,3,1,2,4,3])` → `2`. `lengthOfLongestSubstring("abcabcbb")` → `3`. `longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)` → `6`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Fixed window | `O(n)` | `O(1)` |
| Variable window | `O(n)` | `O(1)`, or `O(k)` with a map of counts |

#### 6. Common Mistakes

1. **Using a window with negative numbers** for sum rules. Shrinking does not fix the sum. Use prefix sum + HashMap.
2. **`if` instead of `while`** when shrinking.
3. **Window length:** it is `right - left + 1`.
4. **Updating the answer at the wrong time:** for "longest", update after the window is valid. For "shortest", update inside the shrink loop.
5. **Forgetting to remove the item** that leaves the window from the map or the sum.
6. **`k` bigger than the array** (fixed window).

#### 7. Say This in the Interview

1. "The part must be continuous, so I use a sliding window with `left` and `right`."
2. "I expand `right`. If the rule breaks, I move `left` until it is valid again."
3. "Each index enters and leaves the window once, so time is `O(n)`."

#### 8. Quick Check

1. What is the length of the window from `left = 2` to `right = 5`?
2. Why does the window method fail for sums with negative numbers?

<details>
<summary>Answers</summary>

1. `5 - 2 + 1 = 4`.
2. With negatives, adding a number can make the sum smaller, so you can no longer decide when to shrink.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) (Easy) | fixed window |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Medium) | shortest, positive numbers |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium) | longest, no repeats |
| 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) (Medium) | at most `k` flips |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (Medium) | window size minus the max count |
| 438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (Medium) | fixed window of counts |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard) | shortest, with counts |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Hard) | monotonic deque (Queue folder, note 13) |
