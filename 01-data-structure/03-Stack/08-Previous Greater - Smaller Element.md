# Previous Greater / Smaller Element

#### 1. What Is It?

For each number, find the **nearest bigger (or smaller) number to its LEFT**. If there is none, the answer is `-1`.

```text
nums = [3, 1, 4, 2]

previous greater:  [-1, 3, -1, 4]     (for 1 the nearest bigger on the left is 3; for 4 there is none)
previous smaller:  [-1, -1, 1, 1]     (for 4 the nearest smaller on the left is 1)
```

It is the same monotonic stack as "next greater", but the **answer is read from the top of the stack**, not written to popped items. Read the "Monotonic Stack" note first.

Why it matters: the previous and next smaller items give the **left and right limits** of each item. Histogram and "sum of subarray minimums" problems use exactly these limits.

#### 2. How It Works

Previous **greater** of `[3, 1, 4, 2]`.

For each number: pop everything that is **smaller than or equal to** it (they can never be an answer for this number or any later one). Then the top, if any, is the answer. Then push the number.

```text
3: stack empty → answer -1          push 3         stack: [3]
1: top 3 is bigger → answer 3       push 1         stack: [3, 1]
4: pop 1, pop 3 (both <= 4)
   stack empty → answer -1          push 4         stack: [4]
2: top 4 is bigger → answer 4       push 2         stack: [4, 2]

result: [-1, 3, -1, 4]
```

Previous **smaller**: same idea, but pop everything **bigger than or equal to** the number.

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea | for each item, scan to the left | stack, read the top after popping |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` extra | `O(n)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
fun previousGreaterBrute(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    for (i in nums.indices) {
        for (j in i - 1 downTo 0) {
            if (nums[j] > nums[i]) { result[i] = nums[j]; break }
        }
    }
    return result
}
```

The stack throws away items that can never be an answer, so nothing is scanned twice.

#### 4. Kotlin Code

```kotlin
// Index of the previous greater element (-1 if none)
fun previousGreaterIndex(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                          // indexes, values decreasing
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] <= nums[i]) stack.removeLast()
        result[i] = if (stack.isEmpty()) -1 else stack.last()
        stack.addLast(i)
    }
    return result
}

// Index of the previous smaller element (-1 if none)
fun previousSmallerIndex(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                          // indexes, values increasing
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) stack.removeLast()
        result[i] = if (stack.isEmpty()) -1 else stack.last()
        stack.addLast(i)
    }
    return result
}
```

Checks: `previousGreaterIndex([3,1,4,2])` → `[-1, 0, -1, 2]` (indexes of 3 and 4). `previousSmallerIndex([3,1,4,2])` → `[-1, -1, 1, 1]`.

**Both sides in one pass.** When an index is popped, the new item is its **next** smaller. The item below it in the stack is its **previous** smaller:

```kotlin
fun smallerBounds(nums: IntArray): Pair<IntArray, IntArray> {
    val n = nums.size
    val left = IntArray(n) { -1 }      // previous smaller index
    val right = IntArray(n) { n }      // next smaller-or-equal index
    val stack = ArrayDeque<Int>()
    for (i in 0 until n) {
        while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) {
            right[stack.removeLast()] = i
        }
        left[i] = if (stack.isEmpty()) -1 else stack.last()
        stack.addLast(i)
    }
    return left to right
}
```

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Monotonic stack | `O(n)` | `O(n)` |
| Brute force | `O(n²)` | `O(1)` |

#### 6. Common Mistakes

1. **Reading the top before popping.** First pop, then read the top.
2. **Wrong direction.** Previous greater pops `<=`. Previous smaller pops `>=`.
3. **Forgetting `-1`** when the stack is empty.
4. **Equal values.** Be consistent: strict on one side and non-strict on the other (explained in the contribution note).
5. **Mixing "previous" (left) with "next" (right).**

#### 7. Say This in the Interview

1. "I scan left to right with a monotonic stack. After popping the useless items, the top is the nearest bigger item on the left."
2. "Each index is pushed and popped once, so it is `O(n)`."

#### 8. Quick Check

1. What is the previous greater of the first item?
2. For `[5, 3, 4]`, what is the previous greater of `4`?

<details>
<summary>Answers</summary>

1. Always `-1`. There is nothing to its left.
2. `5`. The `3` is popped because it is smaller than `4`, and `5` is the nearest bigger one.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) (Medium) | previous greater, as a count |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (Hard) | previous and next smaller bars |
| 907 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) (Medium) | previous and next smaller |
| 1944 | [Number of Visible People in a Queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) (Hard) | stack with both sides |
