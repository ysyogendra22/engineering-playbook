# Monotonic Stack

> The most important stack pattern for interviews. Many Medium and Hard questions use it.

#### 1. What Is It?

A **monotonic stack** is a normal stack where the items are always in **sorted order** (only going up, or only going down, from bottom to top).

To keep the order, **before you push a new item, you pop every item that would break the order**.

Why this is useful: the item you pop has just met **the first bigger (or smaller) item to its right**. So the popped item has found its answer.

Problems it solves in `O(n)` instead of `O(n²)`:

- the **next greater** element for every item,
- the **next smaller** element for every item,
- "how many days until a warmer day", "how far can this bar stretch".

#### 2. How It Works

Find the **next greater element** of `[2, 1, 2, 4, 3]`.

The stack keeps **indexes** of items that are still waiting for a bigger item. Their values go down from bottom to top.

```text
i=0 (2): stack empty → push                      stack: [2]
i=1 (1): 1 is not bigger than 2 → push           stack: [2, 1]
i=2 (2): 2 > 1 → pop 1, its answer is 2
         2 > 2? no (equal) → stop, push          stack: [2, 2]
i=3 (4): 4 > 2 → pop (answer 4)
         4 > 2 → pop (answer 4)                  stack: []  then push 4 → [4]
i=4 (3): 3 > 4? no → push                        stack: [4, 3]

Items left in the stack have no bigger item → answer -1

result: [4, 2, 4, -1, -1]
```

The rule in one line:

> **While the top of the stack is smaller than the new item, pop it. The new item is the answer for the popped one. Then push the new item.**

Which stack for which question:

| Question | Pop while... | Stack goes (bottom → top) |
|---|---|---|
| Next **greater** | `top < new` | big → small |
| Next **smaller** | `top > new` | small → big |

#### 3. Kotlin Code

Store **indexes**, not values. You can always read the value with `nums[index]`, and you need indexes to write answers and to measure distances.

```kotlin
// Next greater element for every item (-1 if none)
fun nextGreater(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                          // indexes
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] < nums[i]) {
            result[stack.removeLast()] = nums[i]           // popped item found its answer
        }
        stack.addLast(i)
    }
    return result                                          // items left in the stack stay -1
}

// Next smaller element: only the comparison changes
fun nextSmaller(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] > nums[i]) {
            result[stack.removeLast()] = nums[i]
        }
        stack.addLast(i)
    }
    return result
}
```

`nextGreater([2, 1, 2, 4, 3])` → `[4, 2, 4, -1, -1]`. `nextSmaller([4, 5, 2, 10, 8])` → `[2, 2, -1, 8, -1]`.

**Distance version** (how many steps until the next bigger item, `0` if none). Write `i - j` instead of the value:

```kotlin
val j = stack.removeLast()
answer[j] = i - j
```

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Monotonic stack | `O(n)` | `O(n)` |
| Brute force | `O(n²)` | `O(1)` |

Why `O(n)` even with a `while` inside a `for`: each index is **pushed once and popped once**.

#### 5. Common Mistakes

1. **Wrong comparison direction.** Draw the first three steps on paper to check.
2. **Storing values instead of indexes.** You cannot compute distances.
3. **Wrong rule for equal values.** `<` means "strictly greater". `<=` means "greater or equal". Read the question.
4. **Forgetting leftovers.** Items still in the stack have no answer. Keep the default (`-1` or `0`).
5. **`stack.last()` on an empty stack.** Always check `isNotEmpty()` first.
6. **Using it for a sliding window.** For a fixed-size window, use a monotonic **queue** (Queue folder, note 13).

#### 6. Say This in the Interview

1. "I will use a monotonic stack of indexes. When the new item is bigger than the top, the top has found its next greater element."
2. "Every index is pushed once and popped once, so the time is `O(n)` and the space is `O(n)`."
3. "Items left on the stack have no greater element to their right."

#### 7. Quick Check

1. Which stack gives the next **smaller** element: decreasing or increasing?
2. Why is the answer for `[3, 2, 1]` all `-1` for next greater?

<details>
<summary>Answers</summary>

1. An **increasing** stack (small → big): pop while `top > new`.
2. Every new item is smaller than the top, so nothing is ever popped. All items stay in the stack and keep `-1`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 496 | Next Greater Element I (Easy) | next greater + map |
| 739 | Daily Temperatures (Medium) | distance to the next warmer day |
| 503 | Next Greater Element II (Medium) | circular array |
| 901 | Online Stock Span (Medium) | previous greater |
| 402 | Remove K Digits (Medium) | pop bigger digits before a smaller one |
| 316 | Remove Duplicate Letters (Medium) | increasing stack with rules |
| 456 | 132 Pattern (Medium) | decreasing stack |
| 84 | Largest Rectangle in Histogram (Hard) | next and previous smaller |
| 42 | Trapping Rain Water (Hard) | decreasing stack (or two pointers) |
| 907 | Sum of Subarray Minimums (Medium) | next and previous smaller |
