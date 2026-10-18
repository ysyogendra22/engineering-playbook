# Heap Sort — Concept

#### 1. Definition — Must Know

1. **Heap Sort** sorts an array using a heap.
2. Two phases:
   - **Build a max-heap** from the array.
   - **Repeatedly move the maximum to the end**, shrink the heap by one, and restore the heap.
3. It sorts **in place**, with no extra array.
4. This note covers the concept. The full algorithm notes are in `02-algorithm/01-sorting/06-Heap Sort.md`.

#### 2. Why It Is Used — Must Know

1. It guarantees `O(n log n)` time in every case, with `O(1)` extra space.
2. It is a good example of how a heap gives sorted output.
3. It is a common interview question about sorting algorithms and their trade-offs.

#### 3. How It Works — Must Know

Sort `[4, 10, 3, 5, 1]` in ascending order. `|` separates the heap (left) from the sorted part (right).

```text
start             [4, 10, 3, 5, 1]
build a max-heap  [10, 5, 3, 4, 1]

swap 10 to the end   [1, 5, 3, 4 | 10]   restore heap → [5, 4, 3, 1 | 10]
swap 5  to the end   [1, 4, 3 | 5, 10]   restore heap → [4, 1, 3 | 5, 10]
swap 4  to the end   [3, 1 | 4, 5, 10]   restore heap → [3, 1 | 4, 5, 10]
swap 3  to the end   [1 | 3, 4, 5, 10]

sorted               [1, 3, 4, 5, 10]
```

The root of a max-heap is always the largest remaining item. Swapping it to the end places it in its final position.

#### 4. Core Concepts — Must Know

1. **Ascending order → max-heap.** The largest goes to the end.
2. **The array is split** into a shrinking heap (front) and a growing sorted part (back).
3. **Each round:** swap root with the last heap item, reduce the heap size by one, heapify down from the root.
4. **Build phase** is `O(n)`. **Sort phase** is `n - 1` rounds of `O(log n)`.

| Property | Heap Sort |
|---|---|
| Time (best, average, worst) | `O(n log n)` |
| Extra space | `O(1)` |
| Stable? | **No** |
| Adaptive (faster on nearly sorted data)? | No |

#### 5. Algorithm — Must Know

```text
heapSort(array):
    buildMaxHeap(array)
    for end from n-1 down to 1:
        swap(array[0], array[end])        // largest goes to its place
        heapifyDown(array, 0, size = end) // heap is now array[0 until end]
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun heapSort(arr: IntArray) {
    val n = arr.size

    // 1. Build a max-heap
    for (i in n / 2 - 1 downTo 0) siftDown(arr, i, n)

    // 2. Move the maximum to the end, shrink the heap, restore it
    for (end in n - 1 downTo 1) {
        swap(arr, 0, end)
        siftDown(arr, 0, end)
    }
}

private fun siftDown(arr: IntArray, start: Int, size: Int) {
    var i = start
    while (true) {
        val left = 2 * i + 1
        val right = left + 1
        var largest = i
        if (left < size && arr[left] > arr[largest]) largest = left
        if (right < size && arr[right] > arr[largest]) largest = right
        if (largest == i) return
        swap(arr, i, largest)
        i = largest
    }
}

private fun swap(arr: IntArray, a: Int, b: Int) {
    val temp = arr[a]; arr[a] = arr[b]; arr[b] = temp
}
```

#### 7. Time & Space Complexity — Must Know

| Phase | Time |
|---|---:|
| Build the heap | `O(n)` |
| `n - 1` extractions | `O(n log n)` |
| **Total** | **`O(n log n)`** |
| Space | `O(1)` |

Compare with other sorts:

| Sort | Time (worst) | Space | Stable |
|---|---:|---:|---|
| Heap Sort | `O(n log n)` | `O(1)` | No |
| Merge Sort | `O(n log n)` | `O(n)` | Yes |
| Quick Sort | `O(n²)` | `O(log n)` | No |

#### 8. Common Heap Sort Patterns — Must Know

1. Explaining it as "build a heap, then extract `n` times".
2. A priority-queue version: add everything to a `PriorityQueue`, then `poll()` into a list. It is simpler but uses `O(n)` extra space.
3. Partial sort: `k` extractions give the `k` smallest items in `O(n + k log n)`.

#### 9. Edge Cases / Common Mistakes

1. Using a min-heap and expecting ascending order in place. A min-heap in place gives descending order.
2. Forgetting to shrink the heap size after each swap, so the sorted items get moved again.
3. Not building the heap first.
4. Claiming it is stable. It is not.
5. Claiming it is faster than quicksort in practice. It is usually slower because of poor cache behaviour.
6. Empty or one-element arrays. Both are already sorted, and the loops do nothing.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need a guaranteed `O(n log n)` worst case with `O(1)` extra space.
2. You only need the smallest or largest `k` items (partial sort).

**Avoid when:**

1. Stability matters. Use merge sort or a stable library sort.
2. Speed in practice matters most. Library sorts or quicksort are usually faster.

In everyday Kotlin code, call `sort()` or `sortedBy { ... }`. You will rarely write heap sort by hand.

#### 11. Related Topics

1. Build Heap
2. Heapify — Basic Concept
3. Heap Sort notes (`02-algorithm/01-sorting/06-Heap Sort.md`)
4. Sorting overview (`02-algorithm/01-sorting/00-Contents.md`)

#### 12. Interview Must Remember

1. **Build a max-heap, then swap the root to the end and shrink.**
2. `O(n log n)` always, `O(1)` space, **not stable**.
3. Ascending order uses a **max**-heap.
4. Mention that quicksort and merge sort are usually preferred in practice.
