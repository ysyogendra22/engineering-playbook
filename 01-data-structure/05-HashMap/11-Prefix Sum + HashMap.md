# Prefix Sum + HashMap

> One of the most important HashMap patterns for FAANG. Learn it well.

#### 1. What Is It?

A **prefix sum** at position `i` is the sum of all elements from the start up to `i`.

The sum of any subarray from `j + 1` to `i` is:

```text
sum(j+1 .. i) = prefix[i] - prefix[j]
```

A **HashMap** remembers the earlier prefix sums. So for each new position `i` you can check in `O(1)` whether some earlier `j` makes the subarray sum equal to `k`.

Why it matters: a normal sliding window needs **non-negative** numbers. Prefix sum + HashMap works **with negative numbers too**.

#### 2. How It Works

You want a subarray ending at `i` with sum `k`:

```text
prefix[i] - prefix[j] = k      →      prefix[j] = prefix[i] - k
```

So at each step, look up `prefix[i] - k` in the map. The count stored there is the number of subarrays that end at `i` and have sum `k`.

*Subarray Sum Equals K* (LeetCode 560): `nums = [1, 2, 3]`, `k = 3`

```text
count = {0: 1}         ← the empty prefix (sum 0) has happened once
sum = 0, answer = 0

x=1: sum = 1   need sum - k = -2   count[-2] = 0   → answer 0     count = {0:1, 1:1}
x=2: sum = 3   need sum - k = 0    count[0] = 1    → answer 1     count = {0:1, 1:1, 3:1}     (subarray [1,2])
x=3: sum = 6   need sum - k = 3    count[3] = 1    → answer 2     count = {0:1, 1:1, 3:1, 6:1} (subarray [3])

answer = 2
```

Three rules:

1. **Start with `{0: 1}`.** It handles subarrays that start at index 0.
2. **Look up first, then store** the current prefix.
3. **Count questions** store *how many times*. **Longest-length questions** store the *first index* of each prefix.

#### 3. Kotlin Code

```kotlin
// Subarray Sum Equals K (LeetCode 560): count the subarrays
fun subarraySum(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1                                     // the empty prefix
    var sum = 0
    var answer = 0
    for (x in nums) {
        sum += x
        answer += count[sum - k] ?: 0                // look up first
        count[sum] = (count[sum] ?: 0) + 1           // then store
    }
    return answer
}

// Longest subarray with sum k: store the FIRST index of each prefix
fun longestSubarrayWithSum(nums: IntArray, k: Int): Int {
    val firstIndex = HashMap<Int, Int>()
    firstIndex[0] = -1                               // the empty prefix ends before index 0
    var sum = 0
    var best = 0
    for ((i, x) in nums.withIndex()) {
        sum += x
        val j = firstIndex[sum - k]
        if (j != null) best = maxOf(best, i - j)
        firstIndex.putIfAbsent(sum, i)               // keep the earliest index
    }
    return best
}
```

Checks: `subarraySum([1,1,1], 2)` → `2`. `subarraySum([1,2,3], 3)` → `2`. `subarraySum([1,-1,0], 0)` → `3`. `longestSubarrayWithSum([1,-1,5,-2,3], 3)` → `4`.

If the numbers can be large, use `Long` for `sum`.

#### 4. Complexity

| Way | Time | Space |
|---|---|---|
| Brute force (all subarrays) | `O(n²)` | `O(1)` |
| **Prefix sum + HashMap** | **`O(n)`** | `O(n)` |
| Sliding window (only non-negative numbers) | `O(n)` | `O(1)` |

#### 5. Common Mistakes

1. **Forgetting `count[0] = 1`.** Subarrays that start at index 0 are missed.
2. **Storing the current prefix before the lookup.** With `k = 0` it counts empty subarrays.
3. **Using a sliding window when numbers can be negative.**
4. **Overwriting the first index** in the "longest" version. Use `putIfAbsent`.
5. **Starting with `{0: 0}` instead of `{0: -1}`** in the "longest" version.
6. **`Int` overflow** of the running sum.

#### 6. Say This in the Interview

1. "A subarray sum is the difference of two prefix sums. So I look for `prefix - k` among earlier prefixes."
2. "I keep a map from prefix sum to how many times it appeared, starting with `{0: 1}`."
3. "It works with negative numbers. Time `O(n)`, space `O(n)`."

#### 7. Quick Check

1. Why start the map with `{0: 1}`?
2. Why can't a sliding window solve this when there are negative numbers?

<details>
<summary>Answers</summary>

1. So subarrays that start at index 0 are counted. Their prefix sum itself equals `k`, and `prefix - k = 0` must be found in the map.
2. With negatives, adding an element can make the sum smaller, so you cannot decide when to shrink the window.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 560 | Subarray Sum Equals K (Medium) | this note |
| 525 | Contiguous Array (Medium) | balance + first index (note 12) |
| 523 | Continuous Subarray Sum (Medium) | remainders (note 12) |
| 974 | Subarray Sums Divisible by K (Medium) | remainders (note 12) |
| 930 | Binary Subarrays With Sum (Medium) | same shape as 560 |
| 325 | Maximum Size Subarray Sum Equals k (Medium, premium) | first index |
| 303 | Range Sum Query - Immutable (Easy) | prefix sum alone, no map |
