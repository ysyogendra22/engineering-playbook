# Previous Greater / Smaller Element

#### 1. Definition — Must Know

1. For each item, the **previous greater element** is the **nearest larger value to its left**. The **previous smaller element** is the **nearest smaller value to its left**. If none exists, the answer is `-1`.
2. Example, previous greater of `[3, 1, 4, 2]` → `[-1, 3, -1, 4]`.
3. The method: scan **left to right** with a monotonic stack. **After popping**, the item on top of the stack (if any) is the answer.

#### 2. Why It Is Used — Must Know

1. It gives the **left boundary** for each item. Together with the next greater/smaller (right boundary) it defines the range where the item is the maximum/minimum.
2. It solves Stock Span, histogram areas, and sum-of-minimums problems.
3. It is still `O(n)` with a stack.

#### 3. How It Works — Must Know

Previous **greater** for `[3, 1, 4, 2]`. Keep a **decreasing** stack of values.

```text
i=0 (3): stack empty → previous greater = -1         push 3        stack: [3]
i=1 (1): top 3 > 1 → nothing to pop → answer 3        push 1        stack: [3, 1]
i=2 (4): pop 1 (1 <= 4), pop 3 (3 <= 4) → stack empty → answer -1     push 4     stack: [4]
i=3 (2): top 4 > 2 → answer 4                         push 2        stack: [4, 2]

result: [-1, 3, -1, 4]
```

Previous **smaller** for the same array. Keep an **increasing** stack:

```text
i=0 (3): empty → -1             push      stack: [3]
i=1 (1): pop 3 (3 >= 1) → empty → -1      push      stack: [1]
i=2 (4): top 1 < 4 → answer 1             push      stack: [1, 4]
i=3 (2): pop 4 (4 >= 2); top 1 < 2 → answer 1      push      stack: [1, 2]

result: [-1, -1, 1, 1]
```

The difference from "next": here the answer is **read from the stack top** while scanning, not written to popped items.

#### 4. Core Concepts — Must Know

1. **Pop the items that cannot be the answer** for this or any later item (they are not greater/smaller enough).
2. **What remains on top is the nearest valid item** to the left.
3. **Previous greater:** pop while `nums[top] <= nums[i]`. **Previous smaller:** pop while `nums[top] >= nums[i]`.
4. **Strict vs non-strict:** with `<=` / `>=` the answer is *strictly* greater/smaller. With `<` / `>`, equal values count as an answer.
5. **Store indexes** if you need distances or spans (`i - previousIndex`).
6. **One pass can give both sides:** when an index is popped, the new item is its **next** smaller, and the stack top below it is its **previous** smaller.

| Question | Pop while | Answer is |
|---|---|---|
| Previous greater (strict) | `nums[top] <= nums[i]` | top after popping |
| Previous smaller (strict) | `nums[top] >= nums[i]` | top after popping |
| Previous greater or equal | `nums[top] < nums[i]` | top after popping |

#### 5. Algorithm — Must Know

```text
stack = empty
for i in 0 until n:
    while stack not empty and nums[stack.top] <= nums[i]:   // for previous greater
        stack.pop()
    previous[i] = if stack is empty then -1 else stack.top (index or value)
    stack.push(i)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Previous Greater Element (index), -1 if none
fun previousGreaterIndex(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                         // indexes, values decreasing
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] <= nums[i]) stack.removeLast()
        result[i] = if (stack.isEmpty()) -1 else stack.last()
        stack.addLast(i)
    }
    return result
}

// Previous Smaller Element (index), -1 if none
fun previousSmallerIndex(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                         // indexes, values increasing
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) stack.removeLast()
        result[i] = if (stack.isEmpty()) -1 else stack.last()
        stack.addLast(i)
    }
    return result
}

// Previous AND next smaller index in one pass: left[i] and right[i]
fun smallerBounds(nums: IntArray): Pair<IntArray, IntArray> {
    val n = nums.size
    val left = IntArray(n) { -1 }        // previous strictly smaller index
    val right = IntArray(n) { n }        // next smaller-or-equal index
    val stack = ArrayDeque<Int>()
    for (i in 0 until n) {
        while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) {
            right[stack.removeLast()] = i                 // i is the NEXT smaller-or-equal of the popped index
        }
        left[i] = if (stack.isEmpty()) -1 else stack.last()   // top is the PREVIOUS strictly smaller
        stack.addLast(i)
    }
    return left to right
}
```

Checks: `previousGreaterIndex([3,1,4,2])` → `[-1, 0, -1, 2]` (values `[-1, 3, -1, 4]`). `previousSmallerIndex([3,1,4,2])` → `[-1, -1, 1, 1]`. `smallerBounds([3,1,2,4])`: `left = [-1,-1,1,2]`, `right = [1,4,4,4]`.

#### 7. Time & Space Complexity — Must Know

| Version | Time | Space |
|---|---:|---:|
| Brute force (scan left for each item) | `O(n²)` | `O(1)` |
| **Monotonic stack** | **`O(n)`** | `O(n)` |

#### 8. Common Previous-Boundary Patterns — Must Know

1. **Online Stock Span** (LeetCode 901) — previous greater; span = `i - previousGreaterIndex`.
2. **Largest Rectangle in Histogram** (LeetCode 84) — left and right smaller bounds.
3. **Sum of Subarray Minimums** (LeetCode 907) — left and right spans.
4. **Maximum Width Ramp**, **Trapping Rain Water** — boundaries.
5. **Number of Visible People in a Queue** (LeetCode 1944) — stack with both sides.
6. **Next Greater** and **Previous Greater** together: count subarrays where an item is the maximum.
7. **Android example:** for each item in a feed, the nearest earlier item with a higher priority.

#### 9. Edge Cases / Common Mistakes

1. Reading the stack top **before** popping instead of after.
2. Strict vs non-strict comparison (the problem decides).
3. Forgetting `-1` when the stack is empty.
4. Mixing up the sign: previous greater pops `<=`, previous smaller pops `>=`.
5. Using the wrong tie rule in boundary pairs (see the contribution note). One side strict, one side non-strict, or equal values are double counted or missed.
6. Storing values when distances are needed.
7. Confusing "previous" (left side) with "next" (right side).

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the nearest larger/smaller value to the left of every item.
2. You need left and right boundaries for areas or counts.

**Avoid when:**

1. You need the answer for a window of fixed size (use a deque).

#### 11. Related Topics

1. Monotonic Stack
2. Stock Span Pattern
3. Largest Rectangle in Histogram
4. Contribution Technique with Monotonic Stack

#### 12. Interview Must Remember

1. **Scan left to right, pop the useless items, then the top is the answer.**
2. Previous greater pops `<=`; previous smaller pops `>=`.
3. Left bound + right bound = the range where an item is the max/min.
4. Be consistent about ties.
