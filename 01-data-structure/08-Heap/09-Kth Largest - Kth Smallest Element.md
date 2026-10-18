# Kth Largest / Kth Smallest Element

#### 1. Definition — Must Know

1. The **Kth largest** element is the item that would be at position `k` if the data were sorted from largest to smallest.
2. The **Kth smallest** is the same, from smallest to largest.
3. Duplicates **count separately**. In `[3, 3, 2]` the 2nd largest is `3`, not `2`.
4. A heap of size `k` gives the answer without sorting.

#### 2. Why It Is Used — Must Know

1. It is the single most asked heap question (*Kth Largest Element in an Array*, LeetCode 215).
2. It is the simplest form of the Top K pattern: the answer is the **root** of the heap.
3. The stream version (*Kth Largest Element in a Stream*, LeetCode 703) shows why a heap beats sorting.

#### 3. How It Works — Must Know

Find the **2nd largest** in `[3, 2, 1, 5, 6, 4]` using a min-heap of size 2:

```text
add 3 → [3]
add 2 → [2, 3]
add 1 → [1, 2, 3]  size 3 > 2 → remove 1   → [2, 3]
add 5 → [2, 3, 5]  size 3 > 2 → remove 2   → [3, 5]
add 6 → [3, 5, 6]  size 3 > 2 → remove 3   → [5, 6]
add 4 → [4, 5, 6]  size 3 > 2 → remove 4   → [5, 6]

Root of the heap = 5   → the 2nd largest
```

The heap holds the 2 largest items. The smaller of the two (the root) is the 2nd largest.

#### 4. Core Concepts — Must Know

| Find | Heap | Answer |
|---|---|---|
| Kth **largest** | Min-heap of size `k` | `peek()` |
| Kth **smallest** | Max-heap of size `k` | `peek()` |

Compare the approaches:

| Method | Time | Space | Note |
|---|---:|---:|---|
| Sort, then index | `O(n log n)` | `O(1)` or `O(n)` | Simplest |
| **Heap of size `k`** | **`O(n log k)`** | **`O(k)`** | Works on streams |
| Quickselect | `O(n)` average, `O(n²)` worst | `O(1)` | Changes the array |

#### 5. Algorithm — Must Know

```text
heap = min-heap
for each n in nums:
    heap.add(n)
    if heap.size > k: heap.poll()
return heap.peek()
```

For the Kth smallest, use a max-heap and the same loop.

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

fun findKthLargest(nums: IntArray, k: Int): Int {
    val heap = PriorityQueue<Int>()              // min-heap
    for (n in nums) {
        heap.add(n)
        if (heap.size > k) heap.poll()
    }
    return heap.peek()
}

fun findKthSmallest(nums: IntArray, k: Int): Int {
    val heap = PriorityQueue<Int>(compareByDescending<Int> { it })   // max-heap
    for (n in nums) {
        heap.add(n)
        if (heap.size > k) heap.poll()
    }
    return heap.peek()
}
```

Stream version, where numbers keep arriving:

```kotlin
class KthLargest(private val k: Int, nums: IntArray) {

    private val heap = PriorityQueue<Int>()

    init {
        for (n in nums) add(n)
    }

    fun add(value: Int): Int {
        heap.add(value)
        if (heap.size > k) heap.poll()
        return heap.peek()
    }
}
```

#### 7. Time & Space Complexity — Must Know

| Case | Time | Space |
|---|---:|---:|
| Array version | `O(n log k)` | `O(k)` |
| Stream version, per new number | `O(log k)` | `O(k)` |

#### 8. Common Kth-Element Patterns — Must Know

1. **Kth Largest Element in an Array** (LeetCode 215).
2. **Kth Largest Element in a Stream** (LeetCode 703).
3. **Kth Smallest Element in a Sorted Matrix** (LeetCode 378) — a max-heap of size `k`, or a K-way merge over the rows.
4. **Kth smallest in a BST** — in-order traversal, no heap needed (`01-data-structure/07-Tree`).
5. Use quickselect when the interviewer asks for `O(n)` on average (`02-algorithm/02-searching/13-Quickselect.md`).

#### 9. Edge Cases / Common Mistakes

1. Using a max-heap for the Kth largest. The size-`k` heap would keep the wrong end.
2. Treating the Kth largest as the Kth **distinct** value. Duplicates count unless stated.
3. `k > n`. `peek()` would return the smallest item, which is wrong. Validate `k`.
4. `k` is `1`-based. The 1st largest is the maximum.
5. Stream version: not handling the first `k - 1` additions, when the heap has fewer than `k` items (`peek()` is then not the Kth).
6. Returning from an empty heap (`peek()` gives `null`).

#### 10. When to Use / When Not to Use

**Use the heap when:**

1. `k` is small, or numbers arrive over time.
2. You must not change the input array.

**Use quickselect when:**

1. You want `O(n)` average time and can reorder the array.

**Use sorting when:**

1. You need several different `k` values from the same data.

#### 11. Related Topics

1. Top K Elements Pattern
2. Min Heap vs Max Heap
3. K Closest Elements / Points
4. Quickselect (`02-algorithm/02-searching/13-Quickselect.md`)

#### 12. Interview Must Remember

1. Kth **largest** → **min**-heap of size `k`, answer is `peek()`.
2. Kth **smallest** → **max**-heap of size `k`.
3. `O(n log k)` time, `O(k)` space. Stream updates cost `O(log k)`.
4. Mention quickselect (`O(n)` average) as the alternative.
