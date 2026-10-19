# Sum of Subarray Minimums / Maximums

#### 1. Definition — Must Know

1. Given an array, find the **sum of the minimum of every contiguous subarray**. The answer can be huge, so the problem asks for it **modulo `10^9 + 7`**.
2. It is *Sum of Subarray Minimums* (LeetCode 907). The mirror problem, the **sum of subarray maximums**, is solved by flipping the comparisons. The related *Sum of Subarray Ranges* (LeetCode 2104) is `sum of maximums − sum of minimums`.
3. The method: the **contribution technique** with a monotonic stack (previous note).

#### 2. Why It Is Used — Must Know

1. A direct solution looks at all `n(n+1)/2` subarrays: `O(n²)` at best. The stack solution is `O(n)`.
2. It is the standard "hard-looking, short-code" monotonic stack question.
3. It is a common follow-up when an interviewer wants to see if you know the contribution idea.

#### 3. How It Works — Must Know

`arr = [3, 1, 2, 4]`. The 10 subarray minimums add to `17`.

For each element, count the subarrays in which it is the minimum:

```text
element 3 at i=0: left 1, right 1  → 1 subarray   ([3])                      3 × 1 = 3
element 1 at i=1: left 2, right 3  → 6 subarrays  (start 3|1, end 1|2|4)     1 × 6 = 6
element 2 at i=2: left 1, right 2  → 2 subarrays  ([2], [2,4])               2 × 2 = 4
element 4 at i=3: left 1, right 1  → 1 subarray   ([4])                      4 × 1 = 4

total = 3 + 6 + 4 + 4 = 17
```

How `left` and `right` come out of one stack pass (increasing stack of indexes):

```text
i=0 (3): stack empty → left=1; push 0                         stack: [0]
i=1 (1): 3 >= 1 → pop 0: right[0] = 1-0 = 1
         stack empty → left = 1-(-1) = 2; push 1              stack: [1]
i=2 (2): top 1 < 2 → left = 2-1 = 1; push 2                   stack: [1, 2]
i=3 (4): top 2 < 4 → left = 3-2 = 1; push 3                   stack: [1, 2, 3]
end: right[1] = 4-1 = 3, right[2] = 4-2 = 2, right[3] = 4-3 = 1
```

**Ties (equal values):** `[2, 2]`. Pop on `>=` for the right boundary and measure the left boundary to the previous **strictly** smaller element. Then each subarray is counted exactly once.

```text
i=0 (2): left 1, right 1  → 1 subarray  ([2] at index 0)
i=1 (2): left 2, right 1  → 2 subarrays ([2] at index 1 and [2,2])
total subarrays = 3 ✓   sum = 2×1 + 2×2 = 6   (the minimums are 2, 2, 2)
```

#### 4. Core Concepts — Must Know

1. **Contribution:** `arr[i] × left[i] × right[i]`.
2. **`left[i]`** = `i − index of previous strictly smaller element` (or `i + 1` if none).
3. **`right[i]`** = `index of next smaller-or-equal element − i` (or `n − i` if none).
4. **Strict on the left, non-strict on the right** (or the reverse). Never the same on both.
5. **Maximum version:** flip the comparisons (pop while `arr[top] <= arr[i]`).
6. **Modulo:** the final sum can exceed `Long` for big inputs in other problems; LeetCode 907 fits in `Long` before taking the modulo (values up to `3 × 10^4`, `n` up to `3 × 10^4`). Take `% MOD` at the end, or after each addition to be safe.
7. **Use `Long`** for `arr[i] * left * right`.
8. **Alternative DP:** `dp[i]` = sum of minimums of subarrays ending at `i`, using the previous smaller index: `dp[i] = dp[prev] + arr[i] * (i − prev)`. Also `O(n)` with a stack.

#### 5. Algorithm — Must Know

```text
left[i], right[i] via one pass with an increasing stack:
    while stack not empty and arr[stack.top] >= arr[i]: right[stack.pop()] = i - that index
    left[i] = i - (stack empty ? -1 : stack.top)
    push i
for indexes left in the stack: right[j] = n - j

answer = (Σ arr[i] * left[i] * right[i]) % MOD
```

#### 6. Kotlin Implementation — Must Know

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

// Sum of Subarray Maximums — flip the comparisons
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

// DP version for minimums: dp[i] = sum of minimums of subarrays ending at i
fun sumSubarrayMinsDp(arr: IntArray): Int {
    val n = arr.size
    val dp = LongArray(n)
    val stack = ArrayDeque<Int>()
    var total = 0L
    for (i in 0 until n) {
        while (stack.isNotEmpty() && arr[stack.last()] >= arr[i]) stack.removeLast()
        val prev = stack.lastOrNull() ?: -1
        dp[i] = (if (prev >= 0) dp[prev] else 0L) + arr[i].toLong() * (i - prev)
        total = (total + dp[i]) % MOD
        stack.addLast(i)
    }
    return total.toInt()
}
```

Checks: `sumSubarrayMins([3,1,2,4])` → `17`. `sumSubarrayMins([11,81,94,43,3])` → `444`. `sumSubarrayMaxs([3,1,2,4])` → `30` (the maximums are `3, 1, 2, 4, 3, 2, 4, 3, 4, 4`). `sumSubarrayMins([2,2])` → `6`.

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Brute force over all subarrays | `O(n²)` (running min) | `O(1)` |
| **Contribution + monotonic stack** | **`O(n)`** | `O(n)` |
| DP with a stack | `O(n)` | `O(n)` |

#### 8. Common Variations — Must Know

1. **Sum of Subarray Minimums** (LeetCode 907).
2. **Sum of Subarray Ranges** (LeetCode 2104) — maximums minus minimums.
3. **Sum of Total Strength of Wizards** (LeetCode 2281) — add prefix sums of prefix sums.
4. **Number of Subarrays With Bounded Maximum** (LeetCode 795).
5. **Maximum Subarray Min-Product** (LeetCode 1856) — the same boundaries plus prefix sums.
6. **Largest Rectangle in Histogram** — the same boundaries with a different formula.
7. **Sum of all substrings** of a string by their smallest character.

#### 9. Edge Cases / Common Mistakes

1. **Tie handling:** strict on both sides double counts equal values; non-strict on both sides misses subarrays. One side strict, the other non-strict.
2. Forgetting to set `right` for the indexes left in the stack.
3. `Int` overflow in `arr[i] * left * right`. Convert to `Long` first.
4. Forgetting the modulo, or applying it only to part of the sum.
5. Mixing `left` as a **count** (`i − prev`) with `left` as an **index** (`prev`).
6. Single element: answer is the element itself.
7. Using the minimum code for the maximum question without flipping both comparisons.
8. Negative modulo results (this problem has positive values; for negative values use `((x % MOD) + MOD) % MOD`).

#### 10. When to Use / When Not to Use

**Use when:**

1. You need a sum over all subarrays of their min or max.

**Avoid when:**

1. The array is tiny and the brute force is clearer (still mention the stack solution).
2. The quantity is not decided by one extreme element.

#### 11. Related Topics

1. Contribution Technique with Monotonic Stack
2. Monotonic Stack
3. Largest Rectangle in Histogram
4. Previous Greater / Smaller Element

#### 12. Interview Must Remember

1. **Answer = Σ `arr[i] × left[i] × right[i]`.**
2. `left` = distance to the previous strictly smaller; `right` = distance to the next smaller-or-equal. One side strict only.
3. Maximum version: flip both comparisons. Ranges = max sum − min sum.
4. `O(n)` with a stack; use `Long` and take the modulo.
