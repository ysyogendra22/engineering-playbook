# Subarray Sum Patterns

> Read note 11 first. Here the same idea is used with different "prefix values".

#### 1. What Is It?

Many subarray problems use the same engine: a **running prefix value** and a **map of earlier prefix values**.

What changes is **what you track** and **what you store**:

| Question | Prefix value | Map stores | Look up |
|---|---|---|---|
| Sum equals `k` (count) | running sum | prefix → count | `sum - k` |
| Longest, sum equals `k` | running sum | prefix → first index | `sum - k` |
| Sum divisible by `k` (count) | `sum mod k` | remainder → count | the **same** remainder |
| Multiple of `k`, length ≥ 2 | `sum mod k` | remainder → first index | the **same** remainder |
| Equal number of 0s and 1s | balance (+1 / −1) | balance → first index | the **same** balance |

The key idea: **two equal prefix values mean the part between them adds to zero** (for balance), or to a **multiple of `k`** (for remainders).

#### 2. How It Works

**Contiguous Array** (LeetCode 525): the longest subarray with equal 0s and 1s. Treat `0` as `-1`, so the balance is `0` exactly when the counts are equal.

```text
nums = [0, 1, 0]     balance after each element: -1, 0, -1

first = {0: -1}      (before the array, balance 0, at index -1)
i=0  balance -1   not seen → first[-1] = 0
i=1  balance  0   seen at -1 → length 1 - (-1) = 2     ([0,1])
i=2  balance -1   seen at 0  → length 2 - 0 = 2        ([1,0])

answer 2
```

**Remainders:** if `prefix[i] % k == prefix[j] % k`, then the part between them has a sum that is a multiple of `k`.

In Kotlin, `-3 % 5` is `-3`, not `2`. Fix negative remainders with `((x % k) + k) % k`.

#### 3. Kotlin Code

```kotlin
// Subarray Sums Divisible by K (LeetCode 974): count
fun subarraysDivByK(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1
    var remainder = 0
    var answer = 0
    for (x in nums) {
        remainder = ((remainder + x) % k + k) % k          // keep it non-negative
        answer += count[remainder] ?: 0
        count[remainder] = (count[remainder] ?: 0) + 1
    }
    return answer
}

// Continuous Subarray Sum (LeetCode 523): a subarray of length >= 2 whose sum is a multiple of k
fun checkSubarraySum(nums: IntArray, k: Int): Boolean {
    val firstIndex = HashMap<Int, Int>()
    firstIndex[0] = -1
    var remainder = 0
    for ((i, x) in nums.withIndex()) {
        remainder = (remainder + x) % k
        val j = firstIndex[remainder]
        if (j != null) {
            if (i - j >= 2) return true                    // length is at least 2
        } else {
            firstIndex[remainder] = i                      // keep only the earliest index
        }
    }
    return false
}

// Contiguous Array (LeetCode 525)
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
```

Checks: `subarraysDivByK([4,5,0,-2,-3,1], 5)` → `7`. `checkSubarraySum([23,2,4,6,7], 6)` → `true`. `findMaxLength([0,1,0])` → `2`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| All of the above | `O(n)` | `O(n)` (for remainders, `O(min(n, k))`) |
| Brute force | `O(n²)` | `O(1)` |

#### 5. Common Mistakes

1. **Negative remainders.** Fix with `((x % k) + k) % k`.
2. **Forgetting the start entry** (`{0: 1}` or `{0: -1}`).
3. **Overwriting the first index.** Store it only if it is missing.
4. **Wrong length check** for "length at least 2": use `i - j >= 2`.
5. **Mixing count maps and first-index maps.** Count questions need counts. Longest/exists questions need first indexes.
6. **Dividing by `k = 0`.** Check what the question allows.
7. **Using a sliding window** here. It fails with negative numbers.

#### 6. Say This in the Interview

1. "The question is about equal prefix states, so I use a map from prefix state to first index (or count)."
2. "For divisibility the state is the remainder. For equal 0s and 1s the state is a balance."
3. "Time `O(n)`, space `O(n)`."

#### 7. Quick Check

1. In Contiguous Array, what do we do with each `0`?
2. Two prefixes have the same remainder mod `k`. What does that tell you about the part between them?

<details>
<summary>Answers</summary>

1. Treat it as `-1`, so equal counts of 0s and 1s give a balance of `0`.
2. Its sum is a multiple of `k`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 560 | Subarray Sum Equals K (Medium) | the base case (note 11) |
| 974 | Subarray Sums Divisible by K (Medium) | remainders, count |
| 523 | Continuous Subarray Sum (Medium) | remainders, first index |
| 525 | Contiguous Array (Medium) | balance, first index |
| 930 | Binary Subarrays With Sum (Medium) | same shape as 560 |
| 1590 | Make Sum Divisible by P (Medium) | remainder + shortest subarray |
