# Monotonic Queue

#### 1. Definition — Must Know

1. A **monotonic queue** is a deque whose items are kept in **sorted order** (always decreasing, or always increasing) from front to back.
2. Before adding a new item, it **removes from the back** every item that can never be the answer again.
3. The **front** is always the current maximum (in a decreasing queue) or minimum (in an increasing queue) of the window.

#### 2. Why It Is Used — Must Know

1. It gives the **maximum or minimum of every sliding window in `O(n)`** total. A heap needs `O(n log n)`.
2. It is the classic answer to *Sliding Window Maximum* (LeetCode 239).
3. Each item is added once and removed once, so the work is linear.

#### 3. How It Works — Must Know

`nums = [1, 3, -1, -3, 5, 3, 6, 7]`, window size `k = 3`. The deque stores **indexes**; the values at those indexes decrease from front to back.

```text
i=0 (1):   deque [0]                       values [1]
i=1 (3):   3 > 1 → remove 1 from back      deque [1]            values [3]
i=2 (-1):  -1 < 3 → keep                   deque [1,2]          values [3,-1]        window full → max = 3
i=3 (-3):  keep                            deque [1,2,3]        values [3,-1,-3]     max = 3
i=4 (5):   front index 1 left the window (1 <= 4-3) → remove it
           then remove -1 and -3 (smaller than 5)    deque [4]            values [5]           max = 5
i=5 (3):   keep                            deque [4,5]          values [5,3]         max = 5
i=6 (6):   remove 3, 5                     deque [6]            values [6]           max = 6
i=7 (7):   remove 6                        deque [7]            values [7]           max = 7

result: [3, 3, 5, 5, 6, 7]
```

Two rules at each step:

```text
1. Front is out of the window?  (index <= i - k)  →  remove it from the front.
2. Back is not bigger than the new value?          →  remove it from the back (it can never be a max again).
Then add the new index at the back.
```

Why we can discard smaller items: if `5` comes after `3` and both are in the same window, `3` can never be the maximum while `5` is still there, and `3` leaves the window first anyway.

#### 4. Core Concepts — Must Know

1. **Store indexes** (not values) so you can tell when the front has left the window.
2. **Decreasing deque** → front is the **maximum**. **Increasing deque** → front is the **minimum**.
3. **Pop from the back** while the back is worse than (or equal to) the new item.
4. **Pop from the front** when the front's index is outside the window.
5. **Each item enters and leaves once** → `O(n)` total.
6. **It is a "monotonic stack" that also removes from the front.** The stack version is in `03-leetcode-patterns`, topic 10.
7. **Ties:** with `<=` on the back check, equal values are removed (keeps only the newest). With `<`, equal values stay. Both work for window max.

| Question | Deque order | Front gives |
|---|---|---|
| Max of each window | decreasing | window maximum |
| Min of each window | increasing | window minimum |
| Oldest valid candidate | by index | first valid index |

#### 5. Algorithm — Must Know

```text
deque = empty (holds indexes)
for i in 0 until n:
    if deque.first() <= i - k: removeFirst()                 // left the window
    while deque is not empty and nums[deque.last()] <= nums[i]: removeLast()
    addLast(i)
    if i >= k - 1: result[i - k + 1] = nums[deque.first()]
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Sliding Window Maximum
fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
    val deque = ArrayDeque<Int>()                    // indexes, values decreasing
    val result = IntArray(nums.size - k + 1)

    for (i in nums.indices) {
        if (deque.isNotEmpty() && deque.first() <= i - k) deque.removeFirst()
        while (deque.isNotEmpty() && nums[deque.last()] <= nums[i]) deque.removeLast()
        deque.addLast(i)
        if (i >= k - 1) result[i - k + 1] = nums[deque.first()]
    }
    return result
}

// Sliding Window Minimum — flip the comparison
fun minSlidingWindow(nums: IntArray, k: Int): IntArray {
    val deque = ArrayDeque<Int>()
    val result = IntArray(nums.size - k + 1)
    for (i in nums.indices) {
        if (deque.isNotEmpty() && deque.first() <= i - k) deque.removeFirst()
        while (deque.isNotEmpty() && nums[deque.last()] >= nums[i]) deque.removeLast()
        deque.addLast(i)
        if (i >= k - 1) result[i - k + 1] = nums[deque.first()]
    }
    return result
}

// A reusable monotonic max queue for values (push / max / pop)
class MonotonicMaxQueue {
    private val deque = ArrayDeque<Int>()

    fun push(x: Int) {
        while (deque.isNotEmpty() && deque.last() < x) deque.removeLast()
        deque.addLast(x)
    }

    fun max(): Int = deque.first()

    fun pop(x: Int) {                                // call with the value that leaves the window
        if (deque.isNotEmpty() && deque.first() == x) deque.removeFirst()
    }
}

fun maxSlidingWindowValues(nums: IntArray, k: Int): IntArray {
    val q = MonotonicMaxQueue()
    val result = IntArray(nums.size - k + 1)
    for (i in nums.indices) {
        q.push(nums[i])
        if (i >= k - 1) {
            result[i - k + 1] = q.max()
            q.pop(nums[i - k + 1])                   // the oldest value leaves next
        }
    }
    return result
}
```

Check: `maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)` → `[3, 3, 5, 5, 6, 7]`. `minSlidingWindow` on the same input → `[-1, -3, -3, -3, 3, 3]`.

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Brute force (scan each window) | `O(n · k)` | `O(1)` |
| Heap with lazy deletion | `O(n log n)` | `O(n)` |
| **Monotonic deque** | **`O(n)`** | `O(k)` |

#### 8. Common Monotonic Queue Patterns — Must Know

1. **Sliding Window Maximum** (LeetCode 239).
2. **Sliding Window Minimum** (same code, flipped).
3. **Longest Continuous Subarray With Absolute Diff ≤ Limit** (LeetCode 1438) — two deques (see the advanced note).
4. **Jump Game VI** (LeetCode 1696) and **Constrained Subsequence Sum** (LeetCode 1425) — DP with a window max.
5. **Shortest Subarray with Sum at Least K** (LeetCode 862) — increasing deque on prefix sums.
6. **Moving max/min of a data stream** (e.g. peak signal in the last 10 seconds).
7. **Android example:** highest FPS spike or maximum latency in the last N samples.

#### 9. Edge Cases / Common Mistakes

1. Storing values instead of indexes. You cannot tell when the front expires.
2. Checking the window expiry with the wrong boundary (`< i - k` instead of `<= i - k`).
3. Forgetting to read the answer only after the first `k` items (`i >= k - 1`).
4. Using `<` and `>` the wrong way round for max vs min.
5. `k = 1` (each item is its own window) and `k = n` (one window).
6. Empty input; `k > n`.
7. Calling `max()` on an empty deque.
8. In the value-based class: `pop(x)` removes only if `x` is at the front. That is correct, but you must call it with the exact value that leaves.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the max/min of every window of a fixed or limited size, in `O(n)`.

**Use a heap when:**

1. The rule for leaving the window is not "oldest first" (arbitrary expiry).

**Avoid when:**

1. You need the median or the k-th largest of a window. Use two heaps or a balanced tree.

#### 11. Related Topics

1. Deque
2. Advanced Monotonic Queue Patterns
3. Heap + Sliding Window (`01-data-structure/08-Heap/24-Heap + Sliding Window.md`)
4. Monotonic Stack (`03-leetcode-patterns`, topic 10)
5. Sliding Window (`03-leetcode-patterns`, topic 5)

#### 12. Interview Must Remember

1. **Deque of indexes, values decreasing. Front = window max.**
2. Pop the **front** when its index leaves the window. Pop the **back** while it is not bigger than the new value.
3. Each item enters and leaves once → **`O(n)`**.
4. Flip the comparison for the minimum.
