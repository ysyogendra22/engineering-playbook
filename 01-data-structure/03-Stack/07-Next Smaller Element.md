# Next Smaller Element

#### 1. What Is It?

For each number, find the **first smaller number to its right**. If there is none, the answer is `-1`.

```text
nums   = [4, 5, 2, 10, 8]
answer = [2, 2, -1, 8, -1]

4 → next smaller is 2
5 → 2
2 → none → -1
10 → 8
8 → none → -1
```

It is the **mirror** of Next Greater Element. The code is the same. Only the comparison flips. Use an **increasing** monotonic stack.

#### 2. How It Works

The stack holds indexes of numbers **still waiting** for a smaller number. Their values go up from bottom to top.

```text
nums = [4, 5, 2, 10, 8]

i=0 (4):  push                                   waiting: [4]
i=1 (5):  5 is not smaller → push                waiting: [4, 5]
i=2 (2):  2 < 5 → 5 gets answer 2
          2 < 4 → 4 gets answer 2                waiting: []  then push 2 → [2]
i=3 (10): push                                   waiting: [2, 10]
i=4 (8):  8 < 10 → 10 gets answer 8              waiting: [2]  then push 8 → [2, 8]

2 and 8 are left → -1
```

Rule:

> **While the top of the stack is bigger than the new item, pop it. The new item is the answer for the popped one.**

#### 3. Kotlin Code

```kotlin
// Next smaller element (value), -1 if none
fun nextSmallerElements(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                        // indexes, values increasing
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] > nums[i]) {
            result[stack.removeLast()] = nums[i]
        }
        stack.addLast(i)
    }
    return result
}

// Final Prices With a Special Discount in a Shop (LeetCode 1475)
// The discount for item i is the first later price that is smaller or equal to it.
fun finalPrices(prices: IntArray): IntArray {
    val result = prices.copyOf()
    val stack = ArrayDeque<Int>()
    for (i in prices.indices) {
        while (stack.isNotEmpty() && prices[stack.last()] >= prices[i]) {   // >= : "smaller or equal"
            result[stack.removeLast()] -= prices[i]
        }
        stack.addLast(i)
    }
    return result
}
```

Checks: `nextSmallerElements([4,5,2,10,8])` → `[2,2,-1,8,-1]`. `finalPrices([8,4,6,2,3])` → `[4,2,4,2,3]`.

**Where this idea is used next:** in *Largest Rectangle in Histogram*, the next smaller bar on the right and the previous smaller bar on the left decide how wide a rectangle can be.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Monotonic stack | `O(n)` | `O(n)` |
| Brute force | `O(n²)` | `O(1)` |

#### 5. Common Mistakes

1. **Mixing up greater and smaller.** Next smaller pops when `top > new`. Next greater pops when `top < new`.
2. **Wrong rule for equal values.** "Smaller" is strict (`>`). "Smaller or equal" (like the shop discount) uses `>=`.
3. **Changing the original array** while you still read it. Copy it first (`prices.copyOf()`).
4. **`stack.last()` on an empty stack.** Check `isNotEmpty()` first.
5. **Forgetting `-1`** for numbers left in the stack.

#### 6. Say This in the Interview

1. "This is the mirror of next greater, so I use an increasing monotonic stack of indexes."
2. "When the new item is smaller than the top, the top has found its next smaller element."
3. "Each index is pushed and popped once. Time `O(n)`, space `O(n)`."

#### 7. Quick Check

1. What does `[1, 2, 3]` give for next smaller?
2. In *Final Prices*, why use `>=` and not `>`?

<details>
<summary>Answers</summary>

1. `[-1, -1, -1]`. Nothing to the right is smaller.
2. The discount comes from the first later price that is **smaller or equal**. An equal price also counts.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1475 | Final Prices With a Special Discount in a Shop (Easy) | next smaller or equal |
| 84 | Largest Rectangle in Histogram (Hard) | next and previous smaller bars |
| 907 | Sum of Subarray Minimums (Medium) | next and previous smaller |
| 402 | Remove K Digits (Medium) | pop bigger digits before a smaller one |
| 316 | Remove Duplicate Letters (Medium) | increasing stack with extra rules |
