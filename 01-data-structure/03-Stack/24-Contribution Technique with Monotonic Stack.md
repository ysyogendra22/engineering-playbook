# Contribution Technique with Monotonic Stack

#### 1. Definition — Must Know

1. The **contribution technique** answers "sum over all subarrays of something" by asking, for **each element**: **in how many subarrays is this element the minimum (or maximum)?**
2. Each element then **contributes** `value × (number of such subarrays)` to the total.
3. A **monotonic stack** finds, for every element, how far it can extend **left** and **right** while staying the minimum (or maximum). The number of subarrays is `left × right`.

#### 2. Why It Is Used — Must Know

1. Checking every subarray is `O(n²)` or `O(n³)`. The contribution method is `O(n)`.
2. It is the key idea behind *Sum of Subarray Minimums*, *Sum of Subarray Ranges*, and many "count subarrays where X is the max" problems.
3. It reuses the previous/next smaller or greater element machinery.

#### 3. How It Works — Must Know

`arr = [3, 1, 2, 4]`. All 10 subarrays and their minimums:

```text
[3] 3     [1] 1     [2] 2     [4] 4
[3,1] 1   [1,2] 1   [2,4] 2
[3,1,2] 1   [1,2,4] 1
[3,1,2,4] 1

sum of minimums = 3 + 1 + 2 + 4 + 1 + 1 + 2 + 1 + 1 + 1 = 17
```

Now count per element. For element `arr[i]`:

```text
left[i]  = number of positions to the left (including i) it can extend before meeting a SMALLER element
right[i] = number of positions to the right (including i) it can extend before meeting a smaller-or-equal element
number of subarrays where arr[i] is the minimum = left[i] × right[i]
contribution = arr[i] × left[i] × right[i]
```

```text
i=0 (3): left 1 (stops at the start),   right 1 (next smaller is 1)    → 3 × 1 × 1 = 3
i=1 (1): left 2 (3 and 1),              right 3 (1, 2, 4)              → 1 × 2 × 3 = 6
i=2 (2): left 1 (previous smaller is 1), right 2 (2, 4)                → 2 × 1 × 2 = 4
i=3 (4): left 1,                         right 1 (end)                 → 4 × 1 × 1 = 4

total = 3 + 6 + 4 + 4 = 17  ✓
```

Why `left × right`? A subarray where `arr[i]` is the minimum chooses a start among `left` positions and an end among `right` positions, independently.

#### 4. Core Concepts — Must Know

1. **Pick the role:** "minimum of the subarray" or "maximum of the subarray".
2. **Find two boundaries per element** with a monotonic stack:
   - `left[i]` = `i − (index of previous smaller element)`
   - `right[i]` = `(index of next smaller-or-equal element) − i`
3. **Tie rule is essential.** Use **strict** on one side and **non-strict** on the other. Then each subarray is counted exactly once, even with equal values.
4. **Contribution = value × left × right.** Sum over all `i`.
5. **For maximums:** flip the comparisons, or negate the array and reuse the minimum code.
6. **Sum of ranges:** `Σ (max − min) = (sum of maximums) − (sum of minimums)`.
7. **Use `Long`** for the total: counts and sums grow fast.
8. **One pass:** when an index is popped, the incoming index gives its `right` boundary, and the stack top below it gives its `left` boundary.

| Goal | For each element, count subarrays where it is... | Boundary pair |
|---|---|---|
| Sum of minimums | the minimum | previous smaller (strict) / next smaller-or-equal |
| Sum of maximums | the maximum | previous greater (strict) / next greater-or-equal |
| Sum of ranges | max and min separately | both of the above |
| Count subarrays with a max ≤ limit | the maximum | greater boundaries |

#### 5. Algorithm — Must Know

```text
left[i]  = i - (previous strictly smaller index, or -1)
right[i] = (next smaller-or-equal index, or n) - i
total = Σ arr[i] * left[i] * right[i]
```

One pass with a stack:

```text
for i in 0 until n:
    while stack not empty and arr[stack.top] >= arr[i]:
        j = stack.pop();  right[j] = i - j
    left[i] = i - (stack empty ? -1 : stack.top)
    stack.push(i)
for the indexes left in the stack: right[j] = n - j
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Sum over all subarrays of (min if isMin else max), as a Long
fun sumOfSubarrayExtremes(arr: IntArray, isMin: Boolean): Long {
    val n = arr.size
    val left = IntArray(n)
    val right = IntArray(n)
    val stack = ArrayDeque<Int>()

    for (i in 0 until n) {
        while (stack.isNotEmpty() &&
            (if (isMin) arr[stack.last()] >= arr[i] else arr[stack.last()] <= arr[i])
        ) {
            val j = stack.removeLast()
            right[j] = i - j                                  // next smaller/greater-or-equal
        }
        left[i] = i - (stack.lastOrNull() ?: -1)               // previous strictly smaller/greater
        stack.addLast(i)
    }
    for (j in stack) right[j] = n - j                          // no boundary on the right

    var total = 0L
    for (i in 0 until n) total += arr[i].toLong() * left[i] * right[i]
    return total
}

// Sum of Subarray Ranges (LeetCode 2104): sum(max - min) over all subarrays
fun subArrayRanges(nums: IntArray): Long =
    sumOfSubarrayExtremes(nums, isMin = false) - sumOfSubarrayExtremes(nums, isMin = true)
```

A helper that returns how many subarrays each element is the minimum of:

```kotlin
// For every i: in how many subarrays is arr[i] the minimum (ties go to the rightmost equal element)
fun countAsMinimum(arr: IntArray): LongArray {
    val n = arr.size
    val left = IntArray(n)
    val right = IntArray(n)
    val stack = ArrayDeque<Int>()
    for (i in 0 until n) {
        while (stack.isNotEmpty() && arr[stack.last()] >= arr[i]) {
            val j = stack.removeLast()
            right[j] = i - j
        }
        left[i] = i - (stack.lastOrNull() ?: -1)
        stack.addLast(i)
    }
    for (j in stack) right[j] = n - j
    return LongArray(n) { left[it].toLong() * right[it] }
}
```

Checks: `sumOfSubarrayExtremes([3,1,2,4], isMin = true)` → `17`. `countAsMinimum([3,1,2,4])` → `[1, 6, 2, 1]`. `subArrayRanges([1,2,3])` → `4`. `subArrayRanges([4,-2,-3,4,1])` → `59`.

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---:|
| Boundaries via monotonic stack | `O(n)` |
| Summing contributions | `O(n)` |
| **Total** | **`O(n)` time, `O(n)` space** |
| Brute force | `O(n²)` (with running min) to `O(n³)` |

#### 8. Common Contribution Patterns — Must Know

1. **Sum of Subarray Minimums** (LeetCode 907) — the next note.
2. **Sum of Subarray Ranges** (LeetCode 2104).
3. **Number of Subarrays With Bounded Maximum** (LeetCode 795).
4. **Count Subarrays Where Max Element Appears at Least K Times**, and similar.
5. **Sum of Total Strength of Wizards** (LeetCode 2281) — contribution plus prefix sums of prefix sums.
6. **Count of valid subarrays** where the first element is the minimum (LeetCode 1063, premium).
7. **Any "sum over all subarrays" or "over all substrings"** problem: ask "how many times does each element count?".

#### 9. Edge Cases / Common Mistakes

1. **Tie handling:** using strict on both sides (double counts equal values) or non-strict on both sides (misses subarrays). Use strict on one side only.
2. Forgetting `right[j] = n - j` for items left on the stack.
3. `left[i] = i - previousIndex` where `previousIndex = -1` if none (giving `i + 1`).
4. Int overflow: use `Long` for `value × left × right` and for the total.
5. Forgetting the modulo when the problem asks for it (done at the end or per term).
6. Using the "minimum" code for a "maximum" question without flipping the comparisons.
7. Treating the answer as "sum of the minimum **values**" and counting subarrays instead of multiplying by the value.
8. Empty array: total `0`.

#### 10. When to Use / When Not to Use

**Use when:**

1. The total is a sum over all subarrays (or substrings) of a min/max-based quantity.

**Avoid when:**

1. The quantity is not decided by a single extreme element (sum of the subarray, product, etc.). Use prefix sums or DP.
2. The array is tiny. A brute force is easier to get right.

#### 11. Related Topics

1. Sum of Subarray Minimums / Maximums
2. Monotonic Stack
3. Previous Greater / Smaller Element
4. Next Smaller Element

#### 12. Interview Must Remember

1. **Contribution = value × (choices of start) × (choices of end) where the element is the extreme.**
2. `left = i − previous smaller`, `right = next smaller-or-equal − i`. Strict on one side only.
3. Sum of ranges = sum of maximums − sum of minimums.
4. `O(n)`; use `Long`.
