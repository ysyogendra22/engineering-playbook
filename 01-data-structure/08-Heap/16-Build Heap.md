# Build Heap

#### 1. Definition — Must Know

1. **Build Heap** turns an unordered array into a valid heap **in place**.
2. The method: start at the **last parent** and **heapify down** every node, going backwards to the root.
3. It runs in **`O(n)`**, which is faster than inserting the items one by one (`O(n log n)`).

#### 2. Why It Is Used — Must Know

1. It is the first phase of heap sort.
2. It is how `PriorityQueue(collection)` is built quickly.
3. It is a classic interview question: "why is building a heap `O(n)` and not `O(n log n)`?"

#### 3. How It Works — Must Know

Build a **min-heap** from `[4, 10, 3, 5, 1]`:

```text
Array:  [4, 10, 3, 5, 1]            n = 5, last parent = n/2 - 1 = 1

        4
      /   \
    10     3
   /  \
  5    1
```

```text
Step 1: heapify down node at index 1 (value 10).
        Children: 5 and 1. Smallest is 1 → swap.     [4, 1, 3, 5, 10]

Step 2: heapify down node at index 0 (value 4).
        Children: 1 and 3. Smallest is 1 → swap.     [1, 4, 3, 5, 10]
        Node 4 is now at index 1, children 5 and 10. 4 is smaller than both → stop.

Result: [1, 4, 3, 5, 10]   ← a valid min-heap
```

Leaves (indexes 2, 3, 4) are already valid heaps, so they are skipped.

#### 4. Core Concepts — Must Know

1. **Start at `n / 2 - 1`.** Every node after it is a leaf.
2. **Go backwards to index 0**, so the children of a node are already heaps when you reach it (the precondition for heapify).
3. **Heapify down**, not up.
4. Why it is `O(n)`: most nodes are near the bottom and move very little.

| Height of node | Number of nodes (about) | Max work per node |
|---|---:|---:|
| 0 (leaves) | `n / 2` | 0 |
| 1 | `n / 4` | 1 |
| 2 | `n / 8` | 2 |
| `h` | `n / 2^(h+1)` | `h` |

Total work = `Σ (n / 2^(h+1)) · h` = `O(n)`.

5. Inserting `n` items one at a time costs `O(n log n)`, because each insert may sift up `log n` levels.

#### 5. Algorithm — Must Know

```text
buildHeap(array):
    n = array.size
    for i from n/2 - 1 down to 0:
        heapifyDown(array, i, n)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun buildMinHeap(arr: IntArray) {
    val n = arr.size
    for (i in n / 2 - 1 downTo 0) {
        heapifyDown(arr, i, n)
    }
}

fun heapifyDown(arr: IntArray, start: Int, size: Int) {
    var i = start
    while (true) {
        val left = 2 * i + 1
        val right = left + 1
        var smallest = i
        if (left < size && arr[left] < arr[smallest]) smallest = left
        if (right < size && arr[right] < arr[smallest]) smallest = right
        if (smallest == i) return
        val temp = arr[i]; arr[i] = arr[smallest]; arr[smallest] = temp
        i = smallest
    }
}

// Usage
val data = intArrayOf(4, 10, 3, 5, 1)
buildMinHeap(data)
println(data.toList())   // [1, 4, 3, 5, 10]
```

With the library:

```kotlin
import java.util.PriorityQueue

val heap = PriorityQueue<Int>(listOf(4, 10, 3, 5, 1))   // builds in O(n)
// heap.addAll(...) on an empty queue would be O(n log n)
```

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Extra space |
|---|---:|---:|
| **Bottom-up build heap** | **`O(n)`** | `O(1)` |
| Insert `n` items one by one | `O(n log n)` | `O(n)` for the new heap |

#### 8. Common Build-Heap Patterns — Must Know

1. First step of **heap sort**.
2. Start a `PriorityQueue` from existing data.
3. Create a Top K heap from the first `k` items, then process the rest.
4. Convert a min-heap into a max-heap by building again with the opposite comparison.

#### 9. Edge Cases / Common Mistakes

1. Starting at the last index instead of `n / 2 - 1`. It works but wastes time on leaves.
2. Going **forwards** (from index 0). The children are not heaps yet, so the result is wrong.
3. Using heapify **up** instead of down.
4. Saying it is `O(n log n)`. The tight bound is `O(n)`.
5. Empty array or one element. The loop does nothing, which is correct.
6. Using `addAll` on a `PriorityQueue` and expecting `O(n)`.

#### 10. When to Use / When Not to Use

**Use when:**

1. All data is available at the start.
2. You want a heap, or a heap sort, quickly.

**Avoid when:**

1. Data arrives one item at a time. Use normal inserts.

#### 11. Related Topics

1. Heapify — Basic Concept
2. Heap Sort — Concept
3. Heap Operations & Complexity
4. Complete Binary Tree Property

#### 12. Interview Must Remember

1. **Heapify down from `n/2 - 1` to `0`.**
2. Build Heap is **`O(n)`**. Repeated insertion is `O(n log n)`.
3. Going backwards guarantees that the children are already heaps.
4. Explain `O(n)`: most nodes are near the bottom and sift very little.
