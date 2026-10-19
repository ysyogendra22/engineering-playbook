# Prefix Sum + HashMap

#### 1. Definition — Must Know

1. A **prefix sum** at position `i` is the sum of all elements from the start up to `i`.
2. The sum of any subarray `[j+1 .. i]` is `prefix[i] - prefix[j]`.
3. A **HashMap** remembers earlier prefix sums, so for each new `i` you can find a matching `j` in `O(1)`.

#### 2. Why It Is Used — Must Know

1. It solves "how many subarrays have sum `k`?" in `O(n)`, even with **negative numbers**.
2. Sliding window fails with negatives. Prefix sum + map still works.
3. It is one of the most important HashMap patterns.

#### 3. How It Works — Must Know

Core idea: a subarray ending at `i` has sum `k` when an earlier prefix equals `prefix[i] - k`.

```text
prefix[i] - prefix[j] = k      →      prefix[j] = prefix[i] - k
```

*Subarray Sum Equals K* (LeetCode 560): `nums = [1, 2, 3]`, `k = 3`

```text
count = {0: 1}       ← the empty prefix (sum 0) has happened once
sum = 0, answer = 0

x=1: sum=1   need sum-k = -2   count[-2]? 0       → answer 0     count = {0:1, 1:1}
x=2: sum=3   need sum-k = 0    count[0]? 1        → answer 1     count = {0:1, 1:1, 3:1}     ([1,2])
x=3: sum=6   need sum-k = 3    count[3]? 1        → answer 2     count = {0:1, 1:1, 3:1, 6:1} ([3])

Answer: 2
```

#### 4. Core Concepts — Must Know

1. **Running sum** `sum` is updated as you go.
2. **Map `prefix sum → how many times it appeared`.**
3. **Start with `{0: 1}`.** This handles subarrays that start at index 0.
4. **Order: look up first, then store** the current prefix. (Otherwise, when `k = 0`, an empty subarray would be counted.)
5. **Counting subarrays** → store counts. **Longest subarray** → store the **first index** of each prefix.
6. **Why not sliding window?** Sliding window needs all numbers non-negative so that the sum only grows. With negatives, you must use this pattern.

#### 5. Algorithm — Must Know

```text
count = {0: 1}; sum = 0; answer = 0
for x in nums:
    sum += x
    answer += count[sum - k] (or 0 if missing)
    count[sum] += 1
return answer
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Subarray Sum Equals K — count subarrays
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

// Longest subarray with sum k — store the FIRST index of each prefix
fun longestSubarrayWithSum(nums: IntArray, k: Int): Int {
    val firstIndex = HashMap<Int, Int>()
    firstIndex[0] = -1                       // empty prefix ends before index 0
    var sum = 0
    var best = 0
    for ((i, x) in nums.withIndex()) {
        sum += x
        val j = firstIndex[sum - k]
        if (j != null) best = maxOf(best, i - j)
        firstIndex.putIfAbsent(sum, i)       // keep the first (earliest) index
    }
    return best
}

// Does any subarray have sum 0? (a set of prefixes is enough)
fun hasZeroSumSubarray(nums: IntArray): Boolean {
    val seen = hashSetOf(0)
    var sum = 0
    for (x in nums) {
        sum += x
        if (!seen.add(sum)) return true
    }
    return false
}
```

Use `Long` for `sum` if the values can be large (sums can overflow `Int`).

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Brute force (all subarrays) | `O(n²)` | `O(1)` |
| **Prefix sum + HashMap** | **`O(n)`** | `O(n)` |
| Sliding window (non-negative only) | `O(n)` | `O(1)` |

#### 8. Common Prefix-Sum + Map Patterns — Must Know

1. **Subarray Sum Equals K** (LeetCode 560) — count.
2. **Maximum Size Subarray Sum Equals k** (LeetCode 325, premium) — first index.
3. **Continuous Subarray Sum** (LeetCode 523) — remainders (next note).
4. **Subarray Sums Divisible by K** (LeetCode 974) — remainders.
5. **Contiguous Array** (LeetCode 525) — treat `0` as `-1`.
6. **Binary Subarrays With Sum** (LeetCode 930).
7. **Prefix sum alone (no map):** Range Sum Query (LeetCode 303) — see `03-leetcode-patterns`, topic 7.

#### 9. Edge Cases / Common Mistakes

1. Forgetting `count[0] = 1`. Subarrays that start at index 0 are missed.
2. Storing the current prefix before the lookup. With `k = 0` this counts empty subarrays.
3. Using the sliding window with negative numbers.
4. For the longest subarray: overwriting the first index. Use `putIfAbsent`.
5. For the longest subarray: starting with `{0: 0}` instead of `{0: -1}`.
6. `Int` overflow of the running sum.
7. Using it when all numbers are positive and `O(1)` space is wanted. A sliding window is lighter.

#### 10. When to Use / When Not to Use

**Use when:**

1. You count or measure subarrays by their sum, and numbers may be negative.

**Avoid when:**

1. All numbers are non-negative and you can use a sliding window.
2. You only need many range sums. A prefix array alone is enough.

#### 11. Related Topics

1. Subarray Sum Patterns
2. HashMap + Prefix Sum Advanced Patterns
3. Prefix Sum (`03-leetcode-patterns`, topic 7)
4. Two Sum Pattern

#### 12. Interview Must Remember

1. **`prefix[j] = prefix[i] - k`.** Look up `sum - k` in the map.
2. **Start with `{0: 1}`** (count) or `{0: -1}` (first index).
3. Lookup first, then store.
4. Handles negatives. `O(n)` time, `O(n)` space.
