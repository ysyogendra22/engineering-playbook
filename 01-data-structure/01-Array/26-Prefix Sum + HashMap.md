# Prefix Sum + HashMap

> One of the most important array patterns for FAANG. The full explanation is in `01-data-structure/05-HashMap/11-Prefix Sum + HashMap.md`. This is the array version.

#### 1. What Is It?

You need to **count (or find) subarrays with a given sum**, and the numbers can be **negative**. A sliding window does not work with negatives, so you combine a **prefix sum** with a **HashMap**.

The key idea:

```text
sum(subarray j+1 .. i) = prefix[i] - prefix[j]
we want this to be k  →  prefix[j] = prefix[i] - k
```

So at each position `i`, look in a map for how many earlier prefix sums equal `prefix[i] - k`. Each match is one valid subarray ending at `i`.

How to spot it: "number of subarrays with sum `k`", "longest subarray with sum `k`", "equal number of 0s and 1s", "sum divisible by `k`", and the array may have negatives.

#### 2. How It Works

`nums = [1, 2, 3]`, `k = 3`

```text
map = {0: 1}            ← the empty prefix, seen once
sum = 0, answer = 0

x=1: sum=1  need sum-k = -2  count 0   → answer 0   map {0:1, 1:1}
x=2: sum=3  need sum-k = 0   count 1   → answer 1   map {0:1, 1:1, 3:1}    ([1,2])
x=3: sum=6  need sum-k = 3   count 1   → answer 2   map {..., 6:1}         ([3])

answer 2
```

Three rules:

1. Start the map with `{0: 1}`.
2. Look up **first**, then store the current prefix.
3. For a **count**, store *how many times*. For the **longest** length, store the **first index** of each prefix.

Variations by changing what the "prefix" means:

| Question | Prefix | Look up |
|---|---|---|
| sum equals `k` | running sum | `sum - k` |
| divisible by `k` | `sum mod k` | the same remainder |
| equal 0s and 1s | +1 for 1, −1 for 0 | the same balance |

#### 3. Brute Force vs Optimized

| | Brute force | Prefix sum + HashMap |
|---|---|---|
| Idea | try all start/end pairs | look up `prefix - k` |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` | `O(n)` |

```kotlin
fun subarraySumBrute(nums: IntArray, k: Int): Int {
    var count = 0
    for (i in nums.indices) {
        var sum = 0
        for (j in i until nums.size) {
            sum += nums[j]
            if (sum == k) count++
        }
    }
    return count
}
```

#### 4. Kotlin Code

```kotlin
// Subarray Sum Equals K (LeetCode 560)
fun subarraySum(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1
    var sum = 0
    var answer = 0
    for (x in nums) {
        sum += x
        answer += count[sum - k] ?: 0                   // look up first
        count[sum] = (count[sum] ?: 0) + 1              // then store
    }
    return answer
}

// Longest subarray with sum k: store the FIRST index of each prefix
fun longestSubarrayWithSum(nums: IntArray, k: Int): Int {
    val firstIndex = HashMap<Int, Int>()
    firstIndex[0] = -1
    var sum = 0
    var best = 0
    for ((i, x) in nums.withIndex()) {
        sum += x
        val j = firstIndex[sum - k]
        if (j != null) best = maxOf(best, i - j)
        firstIndex.putIfAbsent(sum, i)
    }
    return best
}

// Contiguous Array (LeetCode 525): longest subarray with equal 0s and 1s
fun findMaxLength(nums: IntArray): Int {
    val firstIndex = HashMap<Int, Int>()
    firstIndex[0] = -1
    var balance = 0
    var best = 0
    for ((i, x) in nums.withIndex()) {
        balance += if (x == 1) 1 else -1
        val j = firstIndex[balance]
        if (j != null) best = maxOf(best, i - j) else firstIndex[balance] = i
    }
    return best
}

// Subarray Sums Divisible by K (LeetCode 974)
fun subarraysDivByK(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1
    var remainder = 0
    var answer = 0
    for (x in nums) {
        remainder = ((remainder + x) % k + k) % k      // keep it non-negative
        answer += count[remainder] ?: 0
        count[remainder] = (count[remainder] ?: 0) + 1
    }
    return answer
}
```

Checks: `subarraySum([1,1,1], 2)` → `2`. `subarraySum([1,-1,0], 0)` → `3`. `longestSubarrayWithSum([1,-1,5,-2,3], 3)` → `4`. `findMaxLength([0,1,0])` → `2`. `subarraysDivByK([4,5,0,-2,-3,1], 5)` → `7`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Prefix sum + HashMap | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Forgetting `{0: 1}`** (or `{0: -1}` for lengths). Subarrays that start at index 0 are missed.
2. **Storing the current prefix before the lookup.** With `k = 0` it counts empty subarrays.
3. **Using a sliding window with negative numbers.**
4. **Overwriting the first index** in the "longest" version. Use `putIfAbsent`.
5. **Negative remainders.** Fix with `((x % k) + k) % k`.
6. **`Int` overflow** of the running sum.

#### 7. Say This in the Interview

1. "A sliding window fails with negatives, so I use prefix sums. A subarray sum is `prefix[i] - prefix[j]`, so I look for `prefix[i] - k` among earlier prefixes."
2. "I keep a HashMap from prefix sum to how many times it appeared, starting with `{0: 1}`. That is `O(n)` time and space."

#### 8. Quick Check

1. For `[3, 4, 7]` and `k = 7`, how many subarrays sum to 7?
2. Why look up before storing the current prefix?

<details>
<summary>Answers</summary>

1. `2`: `[3, 4]` and `[7]`.
2. Otherwise, when `k = 0`, the current prefix would match itself and count an empty subarray.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium) | count |
| 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) (Medium) | balance, first index |
| 523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) (Medium) | remainders, length ≥ 2 |
| 974 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) (Medium) | remainders, count |
| 930 | [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) (Medium) | same shape as 560 |
