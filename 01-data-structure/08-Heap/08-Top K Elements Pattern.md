# Top K Elements Pattern

#### 1. Definition — Must Know

1. The **Top K Elements** pattern finds the `k` best items (largest, smallest, most frequent, closest) from a collection.
2. The method: keep a **heap of size `k`**. Each new item is compared with the **weakest item currently kept**.
3. You never sort everything. You only track the best `k` seen so far.

#### 2. Why It Is Used — Must Know

1. It costs `O(n log k)` time and `O(k)` space. When `k` is small, that is much better than sorting (`O(n log n)`).
2. It works on **streams**: you do not need all the data at once.
3. It is one of the most common heap interview patterns.

#### 3. How It Works — Must Know

Find the **3 largest** numbers in `[4, 9, 1, 7, 3, 8]`. Use a **min-heap** of size 3. The root is the weakest of the kept items:

```text
add 4 → [4]
add 9 → [4, 9]
add 1 → [1, 4, 9]
add 7 → [1, 4, 7, 9]  size 4 > 3 → remove the smallest (1)   → [4, 7, 9]
add 3 → [3, 4, 7, 9]  size 4 > 3 → remove the smallest (3)   → [4, 7, 9]
add 8 → [4, 7, 8, 9]  size 4 > 3 → remove the smallest (4)   → [7, 8, 9]

Answer: 7, 8, 9
```

Why a **min**-heap for the **largest** items? The root is the first item to throw away, and it is the smallest of the best `k`.

#### 4. Core Concepts — Must Know

1. **Signal words:** "k largest", "k smallest", "k most frequent", "k closest", "top k", "kth".
2. **Heap choice:**

| Find | Heap | Root is |
|---|---|---|
| `k` largest | Min-heap of size `k` | The smallest of the `k` kept |
| `k` smallest | Max-heap of size `k` | The largest of the `k` kept |

3. **Keep the size at `k`.** If `size > k`, remove the root.
4. The comparison key can be a value, a count, a distance, or a score.
5. Heap vs the alternatives:

| Method | Time | Space | Good for |
|---|---:|---:|---|
| Sort everything | `O(n log n)` | `O(1)` or `O(n)` | Small data, simple code |
| **Heap of size `k`** | **`O(n log k)`** | **`O(k)`** | Small `k`, streams |
| Quickselect | `O(n)` average | `O(1)` | One-time answer, data in memory |

#### 5. Algorithm — Must Know

```text
heap = empty heap (min-heap for k largest)
for each item in the data:
    add item to heap
    if heap.size > k:
        remove the root
return the items in the heap
```

Faster variant: if the heap is full and the new item is not better than the root, skip it without touching the heap.

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

fun kLargest(nums: IntArray, k: Int): List<Int> {
    if (k <= 0) return emptyList()
    val heap = PriorityQueue<Int>()              // min-heap
    for (n in nums) {
        heap.add(n)
        if (heap.size > k) heap.poll()           // drop the smallest
    }
    return heap.sortedDescending()
}

fun kSmallest(nums: IntArray, k: Int): List<Int> {
    if (k <= 0) return emptyList()
    val heap = PriorityQueue<Int>(compareByDescending<Int> { it })   // max-heap
    for (n in nums) {
        heap.add(n)
        if (heap.size > k) heap.poll()           // drop the largest
    }
    return heap.sorted()
}
```

Skip variant for `k` largest:

```kotlin
if (heap.size < k) heap.add(n)
else if (n > heap.peek()) { heap.poll(); heap.add(n) }
```

#### 7. Time & Space Complexity — Must Know

| Case | Time |
|---|---:|
| Each item | `O(log k)` |
| Whole input of `n` items | `O(n log k)` |
| Space | `O(k)` |

Why `O(n log k)`?

```text
n items, and each add or poll works on a heap that never grows beyond k + 1 items.
```

If `k` is close to `n`, the heap gives no real saving. Sorting is simpler.

#### 8. Common Top K Patterns — Must Know

1. **Kth Largest / Kth Smallest Element** — the heap root after processing.
2. **Top K Frequent Elements** — count first, then a heap by count.
3. **K Closest Points** — heap by distance.
4. **Top K from a stream** — keep the heap alive between updates.
5. **Merge K Sorted Lists** — related, but a different heap pattern (K-way merge).

#### 9. Edge Cases / Common Mistakes

1. Using a max-heap for the `k` largest.
2. `k` larger than `n`. The heap simply keeps everything, so return all items.
3. `k = 0` or negative.
4. Duplicates. They count as separate items unless the problem says "distinct".
5. Ties at the boundary. Decide how to break them (for example by smaller value or alphabetical order).
6. Forgetting to sort the final heap when the answer must be ordered.
7. Overflow when the key is a computed value such as a squared distance.

#### 10. When to Use / When Not to Use

**Use when:**

1. `k` is much smaller than `n`.
2. Data arrives as a stream, or you cannot sort all of it.

**Avoid when:**

1. You need all items sorted anyway.
2. Only the single best item is needed. Track one variable.
3. The data is small enough that sorting is clear and fast.

#### 11. Related Topics

1. Min Heap vs Max Heap
2. Kth Largest / Kth Smallest Element
3. Top K Frequent Elements
4. K Closest Elements / Points
5. Quickselect (`02-algorithm/02-searching/13-Quickselect.md`)
6. Top K Elements in `03-leetcode-patterns` (topic 11)

#### 12. Interview Must Remember

1. **`k` largest → min-heap of size `k`. `k` smallest → max-heap of size `k`.**
2. Add, then remove the root when the size passes `k`.
3. `O(n log k)` time, `O(k)` space.
4. Mention sorting and quickselect as alternatives, and say why the heap fits (small `k`, streams).
