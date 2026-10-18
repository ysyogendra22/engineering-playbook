# Heap + Sliding Window

#### 1. Definition — Must Know

1. A **sliding window** is a range of `k` consecutive items that moves one step at a time over an array.
2. A **heap** can give the **maximum or minimum of the current window** quickly.
3. The problem: when the window moves, some heap items are **no longer inside it**. They must be ignored (lazy deletion).

The standard example is **Sliding Window Maximum** (LeetCode 239). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is the easiest way to get the window maximum when you already know heaps.
2. It shows lazy deletion in a real problem.
3. It sets up the question: "is there something faster?" The answer is a **monotonic deque** (`O(n)`).

#### 3. How It Works — Must Know

`nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`. The heap stores `[value, index]` and is a **max-heap by value**.

```text
i=0 add (1,0)
i=1 add (3,1)
i=2 add (-1,2)         window [0..2]   top (3,1): index 1 >= 0 → inside   → max 3
i=3 add (-3,3)         window [1..3]   top (3,1): inside                  → max 3
i=4 add (5,4)          window [2..4]   top (5,4): inside                  → max 5
i=5 add (3,5)          window [3..5]   top (5,4): inside                  → max 5
i=6 add (6,6)          window [4..6]   top (6,6): inside                  → max 6
i=7 add (7,7)          window [5..7]   top (7,7): inside                  → max 7

Result: [3, 3, 5, 5, 6, 7]
```

When the top item's index is **before the window start**, pop it and look at the next top. In this example the top never expired, but with `nums = [9, 1, 2, 3]`, `k = 2`, the `9` sits at the top after it has left the window and must be discarded.

#### 4. Core Concepts — Must Know

1. **Store the index** with the value, so you can tell if an item is still in the window.
2. **Window at step `i` is `[i - k + 1, i]`.** A top item with `index <= i - k` is expired.
3. **Lazy discard.** Only remove expired items **when they reach the top**. Expired items below the top do no harm.
4. **Ties:** equal values with different indexes are both stored, which is fine.
5. **Answer starts at `i = k - 1`.** Before that the window is not full.

| Approach | Time | Space |
|---|---:|---:|
| Brute force (scan each window) | `O(n · k)` | `O(1)` |
| **Heap with lazy deletion** | **`O(n log n)`** | `O(n)` |
| **Monotonic deque** | **`O(n)`** | `O(k)` |

The heap may hold up to `n` items, because expired items below the top stay until they surface.

#### 5. Algorithm — Must Know

```text
heap = max-heap by value, entries are (value, index)
for i in 0 until n:
    heap.add((nums[i], i))
    if i >= k - 1:
        while heap.peek().index <= i - k:      // outside the window
            heap.poll()
        result[i - k + 1] = heap.peek().value
```

#### 6. Kotlin Implementation — Must Know

**Heap version**

```kotlin
import java.util.PriorityQueue

fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
    val heap = PriorityQueue<IntArray>(compareByDescending<IntArray> { it[0] })   // [value, index]
    val result = IntArray(nums.size - k + 1)

    for (i in nums.indices) {
        heap.add(intArrayOf(nums[i], i))
        if (i >= k - 1) {
            while (heap.peek()[1] <= i - k) heap.poll()     // drop expired tops
            result[i - k + 1] = heap.peek()[0]
        }
    }
    return result
}
```

**Monotonic deque version (the optimal one)**

```kotlin
fun maxSlidingWindowDeque(nums: IntArray, k: Int): IntArray {
    val deque = ArrayDeque<Int>()            // indexes; values decrease from front to back
    val result = IntArray(nums.size - k + 1)

    for (i in nums.indices) {
        if (deque.isNotEmpty() && deque.first() <= i - k) deque.removeFirst()   // left the window
        while (deque.isNotEmpty() && nums[deque.last()] <= nums[i]) deque.removeLast()
        deque.addLast(i)
        if (i >= k - 1) result[i - k + 1] = nums[deque.first()]
    }
    return result
}
```

The deque keeps only items that could still become the maximum. Each index enters and leaves once, so the total is `O(n)`.

#### 7. Time & Space Complexity — Must Know

| Version | Time | Space |
|---|---:|---:|
| Heap | `O(n log n)` | `O(n)` |
| Deque | `O(n)` | `O(k)` |

#### 8. Common Heap + Window Patterns — Must Know

1. **Sliding Window Maximum / Minimum** — this note.
2. **Sliding Window Median** — two heaps plus lazy deletion (next note).
3. **Constrained Subsequence Sum** (LeetCode 1425) — heap or deque of best earlier sums inside the last `k` positions.
4. **Jump Game VI** (LeetCode 1696) — the same window-maximum idea over a DP array.
5. **Longest subarray with a limited max−min difference** (LeetCode 1438) — two heaps (or two deques) for window max and min.

#### 9. Edge Cases / Common Mistakes

1. Checking only the top once. Use `while`, because several top items may be expired.
2. Using `< i - k` instead of `<= i - k`, which keeps one expired item.
3. Storing only values, so expired items cannot be recognised.
4. Reading results before the first full window (`i < k - 1`).
5. `k > n` or `k == 0`. Check the problem limits.
6. Using the heap for a huge `n` when `O(n)` is expected. Mention the deque.
7. Using a min-heap for the maximum.

#### 10. When to Use / When Not to Use

**Use the heap when:**

1. You need a quick and correct solution, or the window rule is not purely "last `k` items" (for example, expiry by time or by a custom rule).

**Use the monotonic deque when:**

1. The window is the last `k` items and you want `O(n)`.

**Avoid both when:**

1. `k` is tiny. A simple scan of each window is clearer.

#### 11. Related Topics

1. Lazy Deletion with Heap
2. Multiple Heap / Advanced Two-Heaps Patterns
3. Sliding Window (`03-leetcode-patterns`)
4. Monotonic Stack / Queue (`03-leetcode-patterns`)

#### 12. Interview Must Remember

1. **Max-heap of `[value, index]`. Pop the top while its index is outside the window.**
2. Window at `i` is `[i - k + 1, i]`. Expired means `index <= i - k`.
3. Heap `O(n log n)`. Say **monotonic deque `O(n)`** as the better answer.
