# Prefix Sum

> Pre-compute running totals once. Any range sum becomes one subtraction.

#### 1. What Is It?

`prefix[i]` is the sum of the first `i` elements. Then:

```text
sum(l..r) = prefix[r + 1] − prefix[l]
```

**Signals**

- Many **range sum** queries on a fixed array
- "Number of subarrays with sum = K" (works with **negative numbers**)
- "Longest subarray with equal 0s and 1s" (turn 0 into −1)
- "Product of all except self"
- Many range updates on an array (difference array)

#### 2. How It Works

```text
nums   = [ 3, 1, 4, 1, 5 ]
prefix = [ 0, 3, 4, 8, 9, 14 ]       (prefix[0] = 0 on purpose)
sum(1..3) = prefix[4] − prefix[1] = 9 − 3 = 6     (1 + 4 + 1)
```

**Prefix sum + hash map** for "subarray sum equals K":

- A subarray `(j, i]` has sum `K` when `prefix[i] − prefix[j] = K`, so `prefix[j] = prefix[i] − K`.
- Walk once. At each `i`, count how many earlier prefixes equal `prefix[i] − K`.
- Start the map with `{0 : 1}` so subarrays starting at index 0 are counted.

```text
nums = [1, 2, 3], K = 3
running 1: need −2 → 0 times.  store {0:1, 1:1}
running 3: need  0 → 1 time (subarray [1,2]).  store 3
running 6: need  3 → 1 time (subarray [3]).
answer 2
```

**Variants**

| Variant | Idea |
|---|---|
| 2D prefix | `p[i+1][j+1] = m[i][j] + p[i][j+1] + p[i+1][j] − p[i][j]` |
| Prefix product | left products and right products (product except self) |
| Equal 0s and 1s | treat 0 as −1, find equal prefix sums, map stores the first index |
| Divisible by K | store `prefix % K`; equal remainders mean the part in between is divisible |
| Difference array | `diff[l] += v; diff[r+1] −= v`, then prefix-sum `diff` to get the final array |

#### 3. Brute Force vs Optimized

| Problem | Brute force | Prefix sum |
|---|---|---|
| `q` range-sum queries | sum each range `O(q·n)` | build `O(n)`, each query `O(1)` |
| Subarray sum = K | all subarrays `O(n²)` | prefix + map `O(n)` |
| Product except self | multiply the rest for each `i`, `O(n²)` | two passes `O(n)` |
| Range updates | loop each range `O(q·n)` | difference array `O(n + q)` |

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
// Range Sum Query - Immutable (LeetCode 303)
class NumArray(nums: IntArray) {
    private val prefix = IntArray(nums.size + 1)
    init {
        for (i in nums.indices) prefix[i + 1] = prefix[i] + nums[i]
    }
    fun sumRange(left: Int, right: Int): Int = prefix[right + 1] - prefix[left]
}

// Subarray Sum Equals K (LeetCode 560)
fun subarraySum(nums: IntArray, k: Int): Int {
    val seen = HashMap<Int, Int>()             // prefix sum -> how many times
    seen[0] = 1
    var sum = 0
    var count = 0
    for (x in nums) {
        sum += x
        count += seen[sum - k] ?: 0
        seen[sum] = (seen[sum] ?: 0) + 1
    }
    return count
}

// Product of Array Except Self (LeetCode 238)
fun productExceptSelf(nums: IntArray): IntArray {
    val n = nums.size
    val result = IntArray(n)
    result[0] = 1
    for (i in 1 until n) result[i] = result[i - 1] * nums[i - 1]       // product of everything to the left
    var right = 1
    for (i in n - 1 downTo 0) {
        result[i] *= right                                             // times product of everything to the right
        right *= nums[i]
    }
    return result
}

// Contiguous Array (LeetCode 525): longest subarray with equal 0s and 1s
fun findMaxLength(nums: IntArray): Int {
    val first = HashMap<Int, Int>()            // balance -> earliest index
    first[0] = -1
    var balance = 0
    var best = 0
    for (i in nums.indices) {
        balance += if (nums[i] == 1) 1 else -1
        val j = first[balance]
        if (j != null) best = maxOf(best, i - j) else first[balance] = i
    }
    return best
}

// Range Sum Query 2D - Immutable (LeetCode 304)
class NumMatrix(matrix: Array<IntArray>) {
    private val p = Array(matrix.size + 1) { IntArray(matrix[0].size + 1) }
    init {
        for (i in matrix.indices) {
            for (j in matrix[0].indices) {
                p[i + 1][j + 1] = matrix[i][j] + p[i][j + 1] + p[i + 1][j] - p[i][j]
            }
        }
    }
    fun sumRegion(r1: Int, c1: Int, r2: Int, c2: Int): Int =
        p[r2 + 1][c2 + 1] - p[r1][c2 + 1] - p[r2 + 1][c1] + p[r1][c1]
}

// Continuous Subarray Sum (LeetCode 523): length >= 2 and sum is a multiple of k
fun checkSubarraySum(nums: IntArray, k: Int): Boolean {
    val firstIndex = HashMap<Int, Int>()       // remainder -> earliest index
    firstIndex[0] = -1
    var sum = 0
    for (i in nums.indices) {
        sum += nums[i]
        val rem = ((sum % k) + k) % k
        val j = firstIndex[rem]
        if (j != null) { if (i - j >= 2) return true } else firstIndex[rem] = i
    }
    return false
}

// Corporate Flight Bookings (LeetCode 1109): difference array
fun corpFlightBookings(bookings: Array<IntArray>, n: Int): IntArray {
    val diff = IntArray(n + 1)
    for ((first, last, seats) in bookings) {
        diff[first - 1] += seats
        diff[last] -= seats
    }
    val result = IntArray(n)
    var running = 0
    for (i in 0 until n) {
        running += diff[i]
        result[i] = running
    }
    return result
}
```

Checks: `NumArray([-2,0,3,-5,2,-1])`: `sumRange(0,2)` → `1`, `sumRange(2,5)` → `-1`, `sumRange(0,5)` → `-3`. `subarraySum([1,1,1], 2)` → `2`; `([1,2,3], 3)` → `2`. `productExceptSelf([1,2,3,4])` → `[24,12,8,6]`. `findMaxLength([0,1])` → `2`; `([0,1,0])` → `2`. `NumMatrix([[1,2],[3,4]])`: `sumRegion(0,0,1,1)` → `10`, `sumRegion(1,1,1,1)` → `4`, `sumRegion(0,1,1,1)` → `6`. `checkSubarraySum([23,2,4,6,7], 6)` → `true`; `([23,2,6,4,7], 13)` → `false`. `corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5)` → `[10,55,45,25,25]`.

#### 5. Complexity

| Problem | Time | Space |
|---|---|---|
| Build 1D prefix | `O(n)` | `O(n)` |
| Range query | `O(1)` | none extra |
| Subarray sum = K | `O(n)` | `O(n)` |
| Product except self | `O(n)` | `O(1)` extra (output not counted) |
| 2D prefix | build `O(m·n)`, query `O(1)` | `O(m·n)` |

#### 6. Common Mistakes

1. **Forgetting `{0 : 1}`** in the map. Subarrays that start at index 0 are missed.
2. **Off-by-one in the range formula.** With `prefix[0] = 0`, use `prefix[r+1] − prefix[l]`.
3. **Using a sliding window when numbers can be negative.** Use prefix + map.
4. **Storing the latest index instead of the earliest** in the longest-subarray version (this shortens the answer).
5. **Negative remainders:** `(-1) % 6` is `-1` in Kotlin. Normalise with `((x % k) + k) % k`.
6. **Overflow:** use `Long` when sums can be large.
7. **2D prefix:** forgetting to add back the overlap `p[r1][c1]`.

#### 7. Say This in the Interview

1. "I pre-compute prefix sums in `O(n)`, so every range query is `O(1)`."
2. "Because the array can contain negatives, a sliding window won't work. I use prefix sums with a hash map of counts."
3. "I seed the map with `0 → 1` so a subarray starting at index 0 is counted."

#### 8. Quick Check

1. `nums = [2, 4, 6]`. What is `sum(1..2)` using prefix sums?
2. Why does `findMaxLength` store only the first index for each balance?

<details>
<summary>Answers</summary>

1. `prefix = [0, 2, 6, 12]`, so `prefix[3] − prefix[1] = 12 − 2 = 10`.
2. The earliest index gives the longest subarray between two equal balances.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) (Easy) | 1D prefix |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) | left and right products |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium) | prefix + map |
| 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) (Medium) | 0 as −1, first index |
| 523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) (Medium) | remainder map |
| 304 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) (Medium) | 2D prefix |
| 1109 | [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) (Medium) | difference array |
