# Advanced Subarray Counting

> A powerful trick for "count subarrays with **exactly** k ..." questions. Learn it after notes 05, 11 and 26.

#### 1. What Is It?

Some questions count subarrays with **exactly `k`** of something (exactly `k` distinct numbers, exactly `k` odd numbers). A sliding window handles "**at most** `k`" easily, but "exactly `k`" is hard because shrinking the window can break the rule in both directions.

The trick:

```text
exactly(k) = atMost(k) − atMost(k − 1)
```

- `atMost(k)` counts subarrays with **at most** `k`. A window can do this.
- Subtract the ones with **at most** `k − 1`. What is left has **exactly** `k`.

Why the window counts correctly: when the window `[left, right]` is valid (at most `k`), **every** subarray that ends at `right` and starts between `left` and `right` is valid too. That is `right − left + 1` subarrays. Add this for each `right`.

How to spot it: "number of subarrays with **exactly** k distinct / odd / ones", and the numbers are non-negative.

#### 2. How It Works

*Count Number of Nice Subarrays* (LeetCode 1248): count subarrays with exactly `k` odd numbers. `nums = [1, 1, 2, 1, 1]`, `k = 3`.

```text
atMost(3) = 14   every subarray except the whole array (it has 4 odd numbers)
atMost(2) = 12   the 15 subarrays minus the 3 that have 3 or more odd numbers
answer = atMost(3) - atMost(2) = 14 - 12 = 2          ([1,1,2,1] and [1,2,1,1])
```

How `atMost(k)` counts (window):

```text
for each right:
    add nums[right]
    while the window has more than k odd numbers: remove nums[left]; left++
    answer += right - left + 1        // all subarrays ending at right that start at left..right
```

#### 3. Brute Force vs Optimized

| | Brute force | `atMost` difference |
|---|---|---|
| Idea | count the odd numbers in every subarray | two sliding-window passes |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` | `O(1)` (or `O(k)` for distinct counts) |

```kotlin
fun numberOfSubarraysBrute(nums: IntArray, k: Int): Int {
    var count = 0
    for (i in nums.indices) {
        var odd = 0
        for (j in i until nums.size) {
            if (nums[j] % 2 != 0) odd++
            if (odd == k) count++
            if (odd > k) break
        }
    }
    return count
}
```

#### 4. Kotlin Code

```kotlin
// Count Number of Nice Subarrays (LeetCode 1248): exactly k odd numbers
fun numberOfSubarrays(nums: IntArray, k: Int): Int = atMostOdd(nums, k) - atMostOdd(nums, k - 1)

private fun atMostOdd(nums: IntArray, k: Int): Int {
    if (k < 0) return 0
    var left = 0
    var odd = 0
    var count = 0
    for (right in nums.indices) {
        if (nums[right] % 2 != 0) odd++
        while (odd > k) {
            if (nums[left] % 2 != 0) odd--
            left++
        }
        count += right - left + 1               // every subarray ending at right that is still valid
    }
    return count
}

// Subarrays with K Different Integers (LeetCode 992): exactly k distinct values
fun subarraysWithKDistinct(nums: IntArray, k: Int): Int = atMostDistinct(nums, k) - atMostDistinct(nums, k - 1)

private fun atMostDistinct(nums: IntArray, k: Int): Int {
    if (k == 0) return 0
    val count = HashMap<Int, Int>()
    var left = 0
    var result = 0
    for (right in nums.indices) {
        count[nums[right]] = (count[nums[right]] ?: 0) + 1
        while (count.size > k) {
            val c = count.getValue(nums[left]) - 1
            if (c == 0) count.remove(nums[left]) else count[nums[left]] = c
            left++
        }
        result += right - left + 1
    }
    return result
}

// Binary Subarrays With Sum (LeetCode 930): exactly `goal` ones
fun numSubarraysWithSum(nums: IntArray, goal: Int): Int = atMostSum(nums, goal) - atMostSum(nums, goal - 1)

private fun atMostSum(nums: IntArray, goal: Int): Int {
    if (goal < 0) return 0
    var left = 0
    var sum = 0
    var count = 0
    for (right in nums.indices) {
        sum += nums[right]
        while (sum > goal) sum -= nums[left++]
        count += right - left + 1
    }
    return count
}
```

Checks: `numberOfSubarrays([1,1,2,1,1], 3)` → `2`. `subarraysWithKDistinct([1,2,1,2,3], 2)` → `7`. `numSubarraysWithSum([1,0,1,0,1], 2)` → `4`.

Other counting ideas in this family: *Number of Subarrays with Bounded Maximum* (LeetCode 795) is `count(max ≤ right) − count(max ≤ left − 1)`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| `atMost(k) − atMost(k − 1)` | `O(n)` | `O(1)`, or `O(k)` with a map |

#### 6. Common Mistakes

1. **Trying to count "exactly" with one window.** Use the difference of two "at most" counts.
2. **Counting only `1` per `right`.** Add `right − left + 1`.
3. **`atMost(k − 1)` with `k − 1 < 0`.** Return `0` (the code above does this).
4. **Using it with negative numbers** (for sums). The window breaks. Use prefix sum + HashMap.
5. **Not removing keys with zero count** in the distinct version (`count.size` is then wrong).
6. **Mixing up** this trick with prefix sum + HashMap. Both count subarrays, but this one needs non-negative values.

#### 7. Say This in the Interview

1. "Counting 'exactly `k`' is hard with a window, but 'at most `k`' is easy. So `exactly(k) = atMost(k) − atMost(k − 1)`."
2. "For each `right`, the number of valid subarrays ending there is `right − left + 1`. Time `O(n)`."

#### 8. Quick Check

1. How many subarrays end at `right = 4` when the valid window starts at `left = 2`?
2. What is `exactly(2)` if `atMost(2) = 9` and `atMost(1) = 5`?

<details>
<summary>Answers</summary>

1. `4 − 2 + 1 = 3`.
2. `9 − 5 = 4`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 713 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) (Medium) | the "at most" window |
| 930 | [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) (Medium) | exactly = atMost − atMost |
| 1248 | [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) (Medium) | exactly `k` odd numbers |
| 795 | [Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/) (Medium) | difference of two counts |
| 992 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) (Hard) | exactly `k` distinct |
