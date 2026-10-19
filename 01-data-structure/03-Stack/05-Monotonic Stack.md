# Monotonic Stack

#### 1. Definition — Must Know

1. A **monotonic stack** is a stack whose items are always in **sorted order** (all increasing, or all decreasing) from bottom to top.
2. Before pushing a new item, you **pop** every item that would break the order.
3. The popped items have just found their **answer**: the new item is their "next greater" or "next smaller" element.
4. Two kinds:
   - **Decreasing stack** (bottom to top: big → small): finds the **next greater** element.
   - **Increasing stack** (bottom to top: small → big): finds the **next smaller** element.

#### 2. Why It Is Used — Must Know

1. It answers "for each item, where is the next bigger/smaller one?" in **`O(n)`**, instead of `O(n²)`.
2. It is the engine behind Next Greater Element, Daily Temperatures, Stock Span, and Largest Rectangle in Histogram.
3. Each item is pushed once and popped once, so the total work is linear.

#### 3. How It Works — Must Know

Find the **next greater element** for `[2, 1, 2, 4, 3]`. The stack holds **indexes** of items that are still waiting for an answer. Their values are decreasing.

```text
i=0 (2): stack empty → push 0                          stack (values): [2]
i=1 (1): 1 < 2 → no pop, push 1                        stack: [2, 1]
i=2 (2): top 1 < 2 → pop 1: its answer is 2            stack: [2]
         top 2 < 2? no (equal) → stop, push 2          stack: [2, 2]
i=3 (4): top 2 < 4 → pop 2 (index 2): answer 4
         top 2 < 4 → pop 2 (index 0): answer 4         stack: []
         push 3                                        stack: [4]
i=4 (3): 3 < 4 → push 4                                stack: [4, 3]

End: items left in the stack have no next greater → -1

result: [4, 2, 4, -1, -1]
```

Rule in one line: **while the stack top is smaller than the new item, pop it and give it the new item as its answer. Then push the new item.**

#### 4. Core Concepts — Must Know

1. **Store indexes** (not values), so you can write the answer into an array and compute distances. You can read the value with `nums[index]`.
2. **Which condition for which question:**

| Question | Stack kind (bottom → top) | Pop while |
|---|---|---|
| Next **greater** element | decreasing | `nums[top] < nums[i]` |
| Next **smaller** element | increasing | `nums[top] > nums[i]` |
| Next greater-or-equal | decreasing | `nums[top] <= nums[i]` |
| Previous greater / smaller | scan the same way, read the top **after** popping | see the "Previous" note |

3. **Each element is pushed once and popped once** → `O(n)` total.
4. **Items left at the end** never found an answer (use `-1` or `n`).
5. **Ties:** decide whether equal values pop (`<=`) or stay (`<`). The problem statement tells you (strictly greater, or greater-or-equal).
6. **Direction:** scan left to right for "next". Scan right to left to build the same answer with a "previous" style.
7. **Circular arrays:** loop `2n` times with `i % n`.

#### 5. Algorithm — Must Know

```text
stack = empty (indexes);  answer = default for all
for i in 0 until n:
    while stack is not empty and nums[stack.top] < nums[i]:   // for "next greater"
        answer[stack.pop()] = nums[i]   (or i - popped index for distances)
    stack.push(i)
leftover indexes keep the default answer
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Next Greater Element (value), -1 if none
fun nextGreater(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                         // indexes, values decreasing
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] < nums[i]) {
            result[stack.removeLast()] = nums[i]
        }
        stack.addLast(i)
    }
    return result
}

// Next Smaller Element (value), -1 if none
fun nextSmaller(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                         // indexes, values increasing
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] > nums[i]) {
            result[stack.removeLast()] = nums[i]
        }
        stack.addLast(i)
    }
    return result
}

// Distance to the next greater element (0 if none) — Daily Temperatures shape
fun distanceToNextGreater(nums: IntArray): IntArray {
    val result = IntArray(nums.size)
    val stack = ArrayDeque<Int>()
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] < nums[i]) {
            val j = stack.removeLast()
            result[j] = i - j
        }
        stack.addLast(i)
    }
    return result
}
```

Checks: `nextGreater([2,1,2,4,3])` → `[4, 2, 4, -1, -1]`. `nextSmaller([4,5,2,10,8])` → `[2, 2, -1, 8, -1]`.

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---:|
| Time | `O(n)` — every index is pushed once and popped once |
| Space | `O(n)` for the stack (worst case: a sorted array) |
| Brute force for comparison | `O(n²)` |

#### 8. Common Monotonic Stack Patterns — Must Know

1. **Next Greater Element I / II** (LeetCode 496, 503).
2. **Daily Temperatures** (LeetCode 739).
3. **Online Stock Span** (LeetCode 901).
4. **Largest Rectangle in Histogram** (LeetCode 84) and **Maximal Rectangle** (LeetCode 85).
5. **Trapping Rain Water** (LeetCode 42) — a stack solution exists beside two pointers.
6. **Sum of Subarray Minimums** (LeetCode 907) — contribution technique.
7. **Remove K Digits** (LeetCode 402), **Remove Duplicate Letters** (LeetCode 316) — greedy plus a monotonic stack.
8. **Car Fleet** (LeetCode 853), **132 Pattern** (LeetCode 456).

#### 9. Edge Cases / Common Mistakes

1. Wrong direction: popping while `>` when the question needs `<`. Draw the first three steps.
2. Storing values and then being unable to compute distances. Store indexes.
3. Ties handled wrongly (`<` vs `<=`).
4. Forgetting that leftover items have no answer.
5. Calling `stack.last()` on an empty stack. Check `isNotEmpty()` in the `while`.
6. Circular array: forgetting that you only push indexes in the first pass (`i < n`).
7. Thinking the nested `while` makes it `O(n²)`. It does not, since each item is popped once.
8. Using a monotonic stack for a sliding window with a fixed size. Use a monotonic **queue** there.

#### 10. When to Use / When Not to Use

**Use when:**

1. For each item you need the nearest bigger/smaller item on one side.
2. You need spans, distances, or areas based on such boundaries.

**Avoid when:**

1. You need the max/min of a sliding window (monotonic queue: `01-data-structure/04-Queue/13-Monotonic Queue.md`).
2. The answer depends on something other than neighbours' order.

#### 11. Related Topics

1. Next Greater Element
2. Next Smaller Element
3. Previous Greater / Smaller Element
4. Largest Rectangle in Histogram
5. Monotonic Stack pattern (`03-leetcode-patterns`, topic 10)

#### 12. Interview Must Remember

1. **Stack of indexes. Pop while the top loses to the new item. The new item is the popped one's answer.**
2. Decreasing stack → next greater. Increasing stack → next smaller.
3. Each item is pushed and popped once → `O(n)`.
4. Leftover items have no answer; decide how ties behave.
