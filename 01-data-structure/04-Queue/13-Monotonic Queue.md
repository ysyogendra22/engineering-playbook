# Monotonic Queue

> A favourite Hard question: Sliding Window Maximum. Learn this pattern well.

#### 1. What Is It?

A **monotonic queue** is a deque whose items are kept in **sorted order** (always going down, or always going up) from front to back.

Before adding a new item at the back, you **remove from the back** every item that can **never be the answer again**.

For a window maximum, the queue goes **down** from front to back, so the **front is always the maximum** of the window.

It gives the **max (or min) of every sliding window in `O(n)`**. A heap needs `O(n log n)`.

#### 2. How It Works

`nums = [1, 3, -1, -3, 5, 3, 6, 7]`, window size `k = 3`.

The deque stores **indexes**. The values at those indexes go down from front to back.

Two rules for each new item at index `i`:

1. **Front too old?** If the front index is `<= i - k`, it left the window. Remove it from the front.
2. **Back not bigger?** While the back value is `<=` the new value, remove it from the back. It is older **and** smaller, so it can never be a maximum while the new item is in the window.

Then add `i` at the back. Once `i >= k - 1`, the front is the answer for the current window.

```text
i=0 (1):   deque [1]                                              (window not full yet)
i=1 (3):   3 > 1 → remove 1.  deque [3]
i=2 (-1):  -1 < 3 → keep.  deque [3, -1]                          window full → max 3
i=3 (-3):  keep.  deque [3, -1, -3]                               max 3
i=4 (5):   front (3 at index 1) is out of the window → remove it.
           5 > -1 and 5 > -3 → remove both.  deque [5]            max 5
i=5 (3):   keep.  deque [5, 3]                                    max 5
i=6 (6):   6 > 3 and 6 > 5 → remove both.  deque [6]              max 6
i=7 (7):   7 > 6 → remove 6.  deque [7]                           max 7

result: [3, 3, 5, 5, 6, 7]
```

Each index is added once and removed once, so the total is `O(n)`.

#### 3. Kotlin Code

```kotlin
// Sliding Window Maximum
fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
    val deque = ArrayDeque<Int>()                         // indexes, values decreasing
    val result = IntArray(nums.size - k + 1)

    for (i in nums.indices) {
        if (deque.isNotEmpty() && deque.first() <= i - k) deque.removeFirst()          // left the window
        while (deque.isNotEmpty() && nums[deque.last()] <= nums[i]) deque.removeLast() // smaller, older items
        deque.addLast(i)
        if (i >= k - 1) result[i - k + 1] = nums[deque.first()]
    }
    return result
}

// Sliding Window Minimum: flip the comparison
fun minSlidingWindow(nums: IntArray, k: Int): IntArray {
    val deque = ArrayDeque<Int>()                         // indexes, values increasing
    val result = IntArray(nums.size - k + 1)
    for (i in nums.indices) {
        if (deque.isNotEmpty() && deque.first() <= i - k) deque.removeFirst()
        while (deque.isNotEmpty() && nums[deque.last()] >= nums[i]) deque.removeLast()
        deque.addLast(i)
        if (i >= k - 1) result[i - k + 1] = nums[deque.first()]
    }
    return result
}
```

Checks: `maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)` → `[3,3,5,5,6,7]`. `minSlidingWindow` on the same input → `[-1,-3,-3,-3,3,3]`.

#### 4. Complexity

| Way | Time | Space |
|---|---|---|
| Brute force (scan each window) | `O(n · k)` | `O(1)` |
| Heap with lazy deletion | `O(n log n)` | `O(n)` |
| **Monotonic deque** | **`O(n)`** | `O(k)` |

#### 5. Common Mistakes

1. **Storing values instead of indexes.** You cannot tell when the front left the window.
2. **Wrong expiry check.** The front is out when `index <= i - k`.
3. **Reading the answer too early.** Only when `i >= k - 1`.
4. **Wrong comparison direction** for max versus min.
5. **Special sizes:** `k = 1`, `k = n`, empty array.
6. **Calling `first()` on an empty deque.** It is never empty right after you add `i`.

#### 6. Say This in the Interview

1. "Brute force is `O(n·k)`. A heap is `O(n log n)`. A monotonic deque is `O(n)`."
2. "The deque keeps indexes with decreasing values. The front is the window maximum."
3. "I remove from the back anything smaller than the new item, and from the front anything that left the window."
4. "Each index enters and leaves once, so it is `O(n)`."

#### 7. Quick Check

1. Why can we throw away a smaller, older item when a bigger new item arrives?
2. For `[4, 2]` with `k = 2`, what is in the deque after both items and what is the max?

<details>
<summary>Answers</summary>

1. The older item leaves the window first, and while it is still inside, the bigger new item is always better. It can never be the maximum.
2. Indexes `[0, 1]` (values 4, 2). The max is `4` (the front).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 239 | Sliding Window Maximum (Hard) | this note |
| 1438 | Longest Continuous Subarray With Absolute Diff ≤ Limit (Medium) | two deques (note 19) |
| 1696 | Jump Game VI (Medium) | dp + window maximum (note 19) |
| 1425 | Constrained Subsequence Sum (Hard) | dp + window maximum |
| 862 | Shortest Subarray with Sum at Least K (Hard) | prefix sums + deque (note 19) |
