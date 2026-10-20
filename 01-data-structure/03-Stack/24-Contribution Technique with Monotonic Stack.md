# Contribution Technique with Monotonic Stack

> An advanced idea. Learn notes 05, 07 and 08 first.

#### 1. What Is It?

Some questions ask for a **sum over all subarrays**, for example "add up the minimum of every subarray". Checking every subarray is too slow.

The **contribution technique** flips the question. Instead of asking "what is the minimum of this subarray?", ask:

> **For each number, in how many subarrays is it the minimum?**

Then that number **contributes** `value × (number of such subarrays)` to the total.

A monotonic stack finds, for each number, how far it can stretch **left** and **right** while staying the minimum. The number of subarrays is `left × right`.

#### 2. How It Works

`arr = [3, 1, 2, 4]`. All 10 subarrays and their minimums:

```text
[3]=3   [1]=1   [2]=2   [4]=4
[3,1]=1   [1,2]=1   [2,4]=2
[3,1,2]=1   [1,2,4]=1
[3,1,2,4]=1

total = 3+1+2+4 + 1+1+2 + 1+1 + 1 = 17
```

Now count per number. For `arr[i]`:

- `left[i]` = how many positions to the left (including `i`) it can start from, before meeting a **smaller** number.
- `right[i]` = how many positions to the right (including `i`) it can end at, before meeting a **smaller** number.
- Subarrays where `arr[i]` is the minimum = `left[i] × right[i]`. (Choose any start and any end independently.)

```text
3 at i=0: left 1, right 1 → 1 subarray   contributes 3 × 1 = 3
1 at i=1: left 2, right 3 → 6 subarrays  contributes 1 × 6 = 6
2 at i=2: left 1, right 2 → 2 subarrays  contributes 2 × 2 = 4
4 at i=3: left 1, right 1 → 1 subarray   contributes 4 × 1 = 4

total = 3 + 6 + 4 + 4 = 17  ✓
```

**Equal values need one rule.** If two equal numbers could both claim the same subarray, it would be counted twice. So use **strict** on one side and **non-strict** on the other:

- `left`: stretch until a **strictly smaller** number.
- `right`: stretch until a **smaller-or-equal** number.

Then each subarray is counted exactly once.

#### 3. Kotlin Code

```kotlin
// Sum over all subarrays of the minimum (isMin = true) or the maximum (isMin = false)
fun sumOfSubarrayExtremes(arr: IntArray, isMin: Boolean): Long {
    val n = arr.size
    val left = IntArray(n)
    val right = IntArray(n)
    val stack = ArrayDeque<Int>()                            // indexes

    for (i in 0 until n) {
        while (stack.isNotEmpty() &&
            (if (isMin) arr[stack.last()] >= arr[i] else arr[stack.last()] <= arr[i])
        ) {
            val j = stack.removeLast()
            right[j] = i - j                                 // i is the next smaller/greater-or-equal
        }
        left[i] = i - (stack.lastOrNull() ?: -1)             // distance to the previous strictly smaller/greater
        stack.addLast(i)
    }
    for (j in stack) right[j] = n - j                        // nothing stopped them on the right

    var total = 0L
    for (i in 0 until n) total += arr[i].toLong() * left[i] * right[i]
    return total
}

// Sum of Subarray Ranges (LeetCode 2104): sum of (max - min) over all subarrays
fun subArrayRanges(nums: IntArray): Long =
    sumOfSubarrayExtremes(nums, isMin = false) - sumOfSubarrayExtremes(nums, isMin = true)
```

Checks: `sumOfSubarrayExtremes([3,1,2,4], isMin = true)` → `17`. `subArrayRanges([1,2,3])` → `4`. `subArrayRanges([4,-2,-3,4,1])` → `59`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Contribution + stack | `O(n)` | `O(n)` |
| Check every subarray | `O(n²)` or worse | `O(1)` |

#### 5. Common Mistakes

1. **Ties.** Strict on both sides counts equal values twice. Non-strict on both sides misses subarrays. Use strict on one side only.
2. **Forgetting `right[j] = n - j`** for numbers left in the stack.
3. **Wrong `left` when the stack is empty.** The previous index is `-1`, so `left = i + 1`.
4. **`Int` overflow.** Use `Long` for `value × left × right` and for the total.
5. **Using the min code for a max question** without flipping the comparisons.

#### 6. Say This in the Interview

1. "Instead of looking at every subarray, I count for each element in how many subarrays it is the minimum."
2. "That count is `left × right`, where left and right come from the previous and next smaller elements, found with a monotonic stack."
3. "I use strict on one side and non-strict on the other so equal values are counted once."
4. "Sum of ranges is the sum of maximums minus the sum of minimums. Time `O(n)`."

#### 7. Quick Check

1. In `[3, 1, 2, 4]`, in how many subarrays is `1` the minimum?
2. Why do we multiply `left × right`?

<details>
<summary>Answers</summary>

1. `6`. It can start at 2 positions (`3` or `1`) and end at 3 positions (`1`, `2` or `4`).
2. A subarray is a start and an end, chosen independently. Every start works with every end.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 907 | Sum of Subarray Minimums (Medium) | next note |
| 2104 | Sum of Subarray Ranges (Medium) | maximums minus minimums |
| 795 | Number of Subarrays with Bounded Maximum (Medium) | counting with maximum limits |
| 2281 | Sum of Total Strength of Wizards (Hard) | contribution + prefix sums |
| 84 | Largest Rectangle in Histogram (Hard) | same left and right limits |
