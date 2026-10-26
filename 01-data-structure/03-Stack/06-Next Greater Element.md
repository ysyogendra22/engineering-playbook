# Next Greater Element

#### 1. What Is It?

For each number in an array, find the **first bigger number to its right**. If there is none, the answer is `-1`.

```text
nums   = [2, 1, 2, 4, 3]
answer = [4, 2, 4, -1, -1]

2 → next bigger to the right is 4
1 → 2
2 → 4
4 → none → -1
3 → none → -1
```

The slow way checks everything to the right of each number (`O(n²)`). The fast way uses a **monotonic stack** (`O(n)`). Read the "Monotonic Stack" note first.

#### 2. How It Works

Keep a stack of indexes of numbers **still waiting** for a bigger number.

```text
nums = [2, 1, 2, 4, 3]

i=0 (2): push 0                                  waiting: [2]
i=1 (1): 1 < 2, push 1                           waiting: [2, 1]
i=2 (2): 2 > 1 → 1 gets answer 2.  push         waiting: [2, 2]
i=3 (4): 4 > 2 → that 2 gets 4.  4 > 2 → the first 2 gets 4.  push
                                                 waiting: [4]
i=4 (3): 3 < 4, push                             waiting: [4, 3]

4 and 3 are left → -1
```

**Circular version** (the array wraps around, so after the last item you look again from the start). Loop `2 × n` times and use `i % n`. Push only in the first `n` steps.

```text
nums = [1, 2, 1]
the last 1 wraps around and finds 2 → answer [2, -1, 2]
```

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea | for each number of `nums1`, find it in `nums2`, then scan right | stack over `nums2` + a map |
| Time | `O(n · m)` | `O(n + m)` |
| Space | `O(1)` extra | `O(m)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
fun nextGreaterElementBrute(nums1: IntArray, nums2: IntArray): IntArray =
    IntArray(nums1.size) { i ->
        val start = nums2.indexOf(nums1[i])
        var answer = -1
        for (j in start + 1 until nums2.size) {
            if (nums2[j] > nums1[i]) { answer = nums2[j]; break }
        }
        answer
    }
```

The stack answers every number of `nums2` in one pass, and the map gives each query in `O(1)`.

#### 4. Kotlin Code

```kotlin
// Basic version
fun nextGreaterElements(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                        // indexes
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] < nums[i]) {
            result[stack.removeLast()] = nums[i]
        }
        stack.addLast(i)
    }
    return result
}

// LeetCode 496: answers for nums1, whose numbers all appear in nums2
fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
    val nextOf = HashMap<Int, Int>()                     // number → its next greater
    val stack = ArrayDeque<Int>()                        // values (they are all different)
    for (n in nums2) {
        while (stack.isNotEmpty() && stack.last() < n) {
            nextOf[stack.removeLast()] = n
        }
        stack.addLast(n)
    }
    return IntArray(nums1.size) { nextOf[nums1[it]] ?: -1 }
}

// LeetCode 503: circular array
fun nextGreaterCircular(nums: IntArray): IntArray {
    val n = nums.size
    val result = IntArray(n) { -1 }
    val stack = ArrayDeque<Int>()
    for (i in 0 until 2 * n) {
        val idx = i % n
        while (stack.isNotEmpty() && nums[stack.last()] < nums[idx]) {
            result[stack.removeLast()] = nums[idx]
        }
        if (i < n) stack.addLast(idx)                    // push only during the first pass
    }
    return result
}
```

Checks: `nextGreaterElements([2,1,2,4,3])` → `[4,2,4,-1,-1]`. `nextGreaterElement([4,1,2], [1,3,4,2])` → `[-1,3,-1]`. `nextGreaterCircular([1,2,1])` → `[2,-1,2]`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Monotonic stack | `O(n)` | `O(n)` |
| Circular version | `O(n)` (about `2n` steps) | `O(n)` |
| Brute force | `O(n²)` | `O(1)` |

#### 6. Common Mistakes

1. **`<=` instead of `<`.** "Greater" means strictly bigger. With `<=`, equal numbers get wrong answers.
2. **Forgetting `-1`** as the starting value for numbers that never get an answer.
3. **Circular:** looping only `n` times, or pushing indexes again in the second pass.
4. **`stack.last()` on an empty stack.** Check `isNotEmpty()` first.
5. **LeetCode 496:** it asks for answers about `nums1` only, so use a map from number to answer.

#### 7. Say This in the Interview

1. "Brute force is `O(n²)`. I can do `O(n)` with a monotonic stack."
2. "The stack holds indexes of items still waiting for a bigger item. A bigger item pops them and becomes their answer."
3. "Each item is pushed and popped once. Time `O(n)`, space `O(n)`."
4. "For a circular array I loop twice, using `i % n`."

#### 8. Quick Check

1. What is the next greater element of the last item in a normal (non-circular) array?
2. What does `[5, 4, 3]` give?

<details>
<summary>Answers</summary>

1. Always `-1`. There is nothing to its right.
2. `[-1, -1, -1]`. Nothing is ever bigger than the item before it.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) (Easy) | stack + map |
| 503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) (Medium) | circular array |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (Medium) | distance instead of value |
| 1019 | [Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/) (Medium) | same idea on a linked list |
| 901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) (Medium) | the "previous" direction |
