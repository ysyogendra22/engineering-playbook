# Next Greater Element

#### 1. Definition — Must Know

1. For each item in an array, the **next greater element** is the **first larger value to its right**. If there is none, the answer is `-1`.
2. Example: `[2, 1, 2, 4, 3]` → `[4, 2, 4, -1, -1]`.
3. The method: a **decreasing monotonic stack** of indexes.
4. Problems: *Next Greater Element I* (LeetCode 496) and *II* (LeetCode 503, circular). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. The brute force check for every item is `O(n²)`. The stack makes it `O(n)`.
2. It is the first problem to learn after the basic monotonic stack.
3. It is the base of Daily Temperatures and Stock Span.

#### 3. How It Works — Must Know

`nums = [2, 1, 2, 4, 3]`

```text
i=0 (2): push 0                         stack values: [2]
i=1 (1): 1 < 2 → push 1                 stack: [2, 1]
i=2 (2): pop idx1 (1): answer 2         stack: [2]    then push idx2: [2, 2]
i=3 (4): pop idx2 (2): answer 4
         pop idx0 (2): answer 4         stack: []     then push idx3: [4]
i=4 (3): 3 < 4 → push                   stack: [4, 3]

Left in the stack (idx3 = 4, idx4 = 3): no greater element → -1
result: [4, 2, 4, -1, -1]
```

**Circular version** (the array wraps around): *Next Greater Element II* with `[1, 2, 1]`.

```text
Loop i from 0 to 2n - 1 and use index i % n.
First pass (i = 0..2): push indexes, resolve answers.
Second pass (i = 3..5): only resolve answers, do not push again.

[1, 2, 1] → [2, -1, 2]      the last 1 wraps around and finds 2
```

#### 4. Core Concepts — Must Know

1. **Decreasing stack of indexes** (bottom to top: big → small).
2. **Pop while `nums[top] < nums[i]`.** Each popped index gets `nums[i]` as its answer.
3. **Strictly greater** uses `<`. For "greater or equal", use `<=`.
4. **Default `-1`** for items that never get popped.
5. **Circular:** iterate `2n` times, push only when `i < n`.
6. **Two-array version** (LeetCode 496): compute next greater for `nums2` with the stack and store it in a map `value → next greater`, then look up each value of `nums1`.
7. **Going right to left** is another way: keep a stack of candidates and pop those that are not greater than the current item; the top is the answer.

#### 5. Algorithm — Must Know

```text
result = all -1; stack = empty
for i in 0 until n:
    while stack not empty and nums[stack.top] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.push(i)
return result
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Next Greater Element for one array
fun nextGreaterElements(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] < nums[i]) {
            result[stack.removeLast()] = nums[i]
        }
        stack.addLast(i)
    }
    return result
}

// Next Greater Element I — answers for nums1, whose values are inside nums2
fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
    val nextOf = HashMap<Int, Int>()
    val stack = ArrayDeque<Int>()
    for (n in nums2) {
        while (stack.isNotEmpty() && stack.last() < n) {
            nextOf[stack.removeLast()] = n               // stack holds values here (unique values)
        }
        stack.addLast(n)
    }
    return IntArray(nums1.size) { nextOf[nums1[it]] ?: -1 }
}

// Next Greater Element II — circular array
fun nextGreaterCircular(nums: IntArray): IntArray {
    val n = nums.size
    val result = IntArray(n) { -1 }
    val stack = ArrayDeque<Int>()
    for (i in 0 until 2 * n) {
        val idx = i % n
        while (stack.isNotEmpty() && nums[stack.last()] < nums[idx]) {
            result[stack.removeLast()] = nums[idx]
        }
        if (i < n) stack.addLast(idx)                    // push only in the first pass
    }
    return result
}

// Right-to-left version
fun nextGreaterRightToLeft(nums: IntArray): IntArray {
    val result = IntArray(nums.size)
    val stack = ArrayDeque<Int>()                        // values, candidates for "next greater"
    for (i in nums.indices.reversed()) {
        while (stack.isNotEmpty() && stack.last() <= nums[i]) stack.removeLast()
        result[i] = if (stack.isEmpty()) -1 else stack.last()
        stack.addLast(nums[i])
    }
    return result
}
```

Checks: `nextGreaterElements([2,1,2,4,3])` → `[4,2,4,-1,-1]`. `nextGreaterElement([4,1,2], [1,3,4,2])` → `[-1,3,-1]`. `nextGreaterCircular([1,2,1])` → `[2,-1,2]`.

#### 7. Time & Space Complexity — Must Know

| Version | Time | Space |
|---|---:|---:|
| Brute force | `O(n²)` | `O(1)` |
| **Monotonic stack** | **`O(n)`** | `O(n)` |
| Circular | `O(n)` (about `2n` steps) | `O(n)` |

#### 8. Common Next-Greater Patterns — Must Know

1. **Next Greater Element I** (LeetCode 496) — stack + map.
2. **Next Greater Element II** (LeetCode 503) — circular.
3. **Daily Temperatures** (LeetCode 739) — distance instead of value.
4. **Online Stock Span** (LeetCode 901) — previous greater, counted.
5. **Next Greater Node in Linked List** (LeetCode 1019).
6. **Largest rectangle / water problems** — need both next and previous bounds.
7. **Android example:** for each message in a list, find the next message from a different day (to show a date header).

#### 9. Edge Cases / Common Mistakes

1. Using `<=` when the problem needs strictly greater (equal values then get a wrong answer).
2. Forgetting the default `-1`.
3. Circular: pushing indexes again in the second pass (it adds duplicates and wastes time).
4. Circular: looping `n` times instead of `2n`.
5. `stack.last()` on an empty stack. The `while` must check `isNotEmpty()`.
6. In the two-array version, assuming values are unique. LeetCode 496 guarantees it; otherwise store indexes.
7. Looking for the next greater to the **left** with the same code (that is "previous greater").

#### 10. When to Use / When Not to Use

**Use when:**

1. For each item you need the nearest larger value on its right.

**Avoid when:**

1. You need the largest value in a window (monotonic queue).
2. You need the next greater of a *specific query value* many times on changing data. Use a balanced tree.

#### 11. Related Topics

1. Monotonic Stack
2. Next Smaller Element
3. Daily Temperatures Pattern
4. HashMap — index tracking (`01-data-structure/05-HashMap/10-Mapping - Index Tracking.md`)

#### 12. Interview Must Remember

1. **Decreasing stack of indexes. Pop while `top < current` and set their answer to current.**
2. Leftovers → `-1`.
3. Circular: loop `2n`, push only in the first `n`.
4. `O(n)` time, `O(n)` space.
