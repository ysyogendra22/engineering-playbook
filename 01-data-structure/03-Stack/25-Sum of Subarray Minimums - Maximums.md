# Sum of Subarray Minimums / Maximums

> Read note 24 (Contribution Technique) first. This note is the full interview solution.

#### 1. What Is It?

Given an array, find the **sum of the minimum of every contiguous subarray**. The answer can be very large, so the question asks for it **modulo `10^9 + 7`** (the remainder after dividing by `1,000,000,007`).

```text
arr = [3, 1, 2, 4]   →   17
```

This is *Sum of Subarray Minimums* (LeetCode 907). There are `n(n+1)/2` subarrays, so checking each is too slow for a large array. The stack solution is `O(n)`.

The **maximum** version is the same code with the comparisons flipped.

#### 2. How It Works

**Answer = sum of `arr[i] × left[i] × right[i]`.**

- `left[i]` = `i` − (index of the previous **strictly smaller** number). If none, the previous index is `-1`.
- `right[i]` = (index of the next **smaller-or-equal** number) − `i`. If none, that index is `n`.

Both come out of **one pass** with an increasing stack:

```text
arr = [3, 1, 2, 4]

i=0 (3): stack empty → left = 0-(-1) = 1.  push 0                      stack: [0]
i=1 (1): 3 >= 1 → pop 0, right[0] = 1-0 = 1
         stack empty → left = 1-(-1) = 2.  push 1                      stack: [1]
i=2 (2): top 1 < 2 → left = 2-1 = 1.  push 2                           stack: [1, 2]
i=3 (4): top 2 < 4 → left = 3-2 = 1.  push 3                           stack: [1, 2, 3]
end: right[1] = 4-1 = 3, right[2] = 4-2 = 2, right[3] = 4-3 = 1

contributions: 3×1×1 + 1×2×3 + 2×1×2 + 4×1×1 = 3 + 6 + 4 + 4 = 17
```

Equal values (`[2, 2]`): the tie rule makes each subarray count once.

```text
index 0: left 1, right 1 → 1 subarray
index 1: left 2, right 1 → 2 subarrays
total 3 subarrays, sum = 2×1 + 2×2 = 6   ✓ (the three minimums are 2, 2, 2)
```

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea | for each start, extend the end and keep a running minimum | count the subarrays each element is the minimum of |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` | `O(n)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
fun sumSubarrayMinsBrute(arr: IntArray): Long {
    var total = 0L
    for (i in arr.indices) {
        var minimum = Int.MAX_VALUE
        for (j in i until arr.size) {
            minimum = minOf(minimum, arr[j])      // the minimum of arr[i..j]
            total += minimum
        }
    }
    return total
}
```

This is already `O(n²)`, which times out for large `n`. The contribution method needs only one pass.

#### 4. Kotlin Code

```kotlin
private const val MOD = 1_000_000_007L

// Sum of Subarray Minimums (LeetCode 907)
fun sumSubarrayMins(arr: IntArray): Int {
    val n = arr.size
    val left = IntArray(n)
    val right = IntArray(n)
    val stack = ArrayDeque<Int>()                              // indexes, values increasing

    for (i in 0 until n) {
        while (stack.isNotEmpty() && arr[stack.last()] >= arr[i]) {
            val j = stack.removeLast()
            right[j] = i - j                                   // next smaller-or-equal is i
        }
        left[i] = i - (stack.lastOrNull() ?: -1)               // previous strictly smaller
        stack.addLast(i)
    }
    for (j in stack) right[j] = n - j

    var total = 0L
    for (i in 0 until n) {
        total = (total + arr[i].toLong() * left[i] * right[i]) % MOD
    }
    return total.toInt()
}

// Sum of Subarray Maximums: flip both comparisons
fun sumSubarrayMaxs(arr: IntArray): Int {
    val n = arr.size
    val left = IntArray(n)
    val right = IntArray(n)
    val stack = ArrayDeque<Int>()                              // indexes, values decreasing

    for (i in 0 until n) {
        while (stack.isNotEmpty() && arr[stack.last()] <= arr[i]) {
            val j = stack.removeLast()
            right[j] = i - j
        }
        left[i] = i - (stack.lastOrNull() ?: -1)
        stack.addLast(i)
    }
    for (j in stack) right[j] = n - j

    var total = 0L
    for (i in 0 until n) {
        total = (total + arr[i].toLong() * left[i] * right[i]) % MOD
    }
    return total.toInt()
}
```

Checks: `sumSubarrayMins([3,1,2,4])` → `17`. `sumSubarrayMins([11,81,94,43,3])` → `444`. `sumSubarrayMins([2,2])` → `6`. `sumSubarrayMaxs([3,1,2,4])` → `30` (the maximums are `3, 1, 2, 4, 3, 2, 4, 3, 4, 4`).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Contribution + monotonic stack | `O(n)` | `O(n)` |
| Check every subarray | `O(n²)` | `O(1)` |

#### 6. Common Mistakes

1. **Ties.** Strict on one side, non-strict on the other. Never the same on both.
2. **Forgetting `right[j] = n - j`** for the numbers left in the stack.
3. **Overflow.** Convert to `Long` **before** multiplying: `arr[i].toLong() * left[i] * right[i]`.
4. **Forgetting the modulo**, or applying it to only part of the sum.
5. **Mixing `left` as a distance (`i - prev`) with `left` as an index (`prev`).**
6. **Using the minimum code for the maximum** without flipping both comparisons.

#### 7. Say This in the Interview

1. "For each element I count the subarrays where it is the minimum. That is `left × right`, so it adds `value × left × right` to the answer."
2. "I find the previous strictly smaller and the next smaller-or-equal element with one monotonic stack pass."
3. "Strict on one side and non-strict on the other makes each subarray count once, even with duplicates."
4. "Time `O(n)`, space `O(n)`. I use `Long` and take the modulo."

#### 8. Quick Check

1. What is `sumSubarrayMins([5])`?
2. In `[1, 2]`, what are the subarray minimums, and their sum?

<details>
<summary>Answers</summary>

1. `5`. There is one subarray.
2. Subarrays `[1]`, `[2]`, `[1,2]` have minimums `1`, `2`, `1`. The sum is `4`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 907 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) (Medium) | this note |
| 2104 | [Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/) (Medium) | maximums minus minimums |
| 1856 | [Maximum Subarray Min-Product](https://leetcode.com/problems/maximum-subarray-min-product/) (Medium) | same limits + prefix sums |
| 2281 | [Sum of Total Strength of Wizards](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) (Hard) | contribution + prefix sums of prefix sums |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (Hard) | same left and right limits |
