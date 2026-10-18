# Heap Fundamentals

#### 1. Definition — Must Know

1. A **heap** is a tree-based structure that follows two rules:
   - **Shape rule:** it is a **complete binary tree** (every level is full, except possibly the last, which fills from the left).
   - **Order rule (heap property):** every parent is "better" than its children. In a **min-heap** the parent is smaller or equal. In a **max-heap** the parent is larger or equal.
2. Its job is to give you the **smallest** (or **largest**) element immediately, at the root.
3. A heap is **not sorted**. Only the root is guaranteed to be the best element.

#### 2. Why It Is Used — Must Know

1. It answers "what is the next smallest / largest item?" in `O(1)`.
2. Adding an item and removing the best item both cost only `O(log n)`.
3. It is the standard structure for **priority queues**, **Top K** problems, **running medians**, **merging sorted lists**, and **scheduling**.
4. It is the right tool when you keep asking for "the best item" while the data keeps changing. Sorting once does not help there.

#### 3. How It Works — Must Know

A min-heap holding `1, 3, 2, 7, 4, 5`:

```text
        1
      /   \
     3     2
    / \   /
   7   4 5
```

1. `1` is the root, so it is the minimum.
2. Each parent is smaller than its children: `1 ≤ 3, 2`, `3 ≤ 7, 4`, `2 ≤ 5`.
3. Siblings have **no order** between them (`3` and `2`).
4. The tree is stored in a plain array: `[1, 3, 2, 7, 4, 5]` (see "Complete Binary Tree Property").

#### 4. Core Concepts — Must Know

1. **Root** — holds the minimum (min-heap) or maximum (max-heap).
2. **Heap property** — parent vs child only. It says nothing about left vs right.
3. **Complete tree** — keeps the height at `log n` and allows array storage.
4. **Sift up / sift down** — the two moves that repair the heap after an insert or a removal.
5. **Priority** — whatever you compare: a number, a deadline, a distance, a frequency.

#### 5. Algorithm — Must Know

The four basic operations (details in "Heap Operations & Complexity"):

```text
peek:     return the root
insert:   put the new item at the end, then sift it UP
extract:  take the root, move the last item to the root, then sift it DOWN
build:    heapify the whole array in O(n)
```

#### 6. Kotlin Implementation — Must Know

Use the built-in `PriorityQueue` (a min-heap by default):

```kotlin
import java.util.PriorityQueue

val heap = PriorityQueue<Int>()
heap.add(5)
heap.add(1)
heap.add(3)

println(heap.peek())   // 1  (smallest)
println(heap.poll())   // 1  (removes the smallest)
println(heap.poll())   // 3
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| Peek min / max | `O(1)` |
| Insert | `O(log n)` |
| Extract min / max | `O(log n)` |
| Build a heap from `n` items | `O(n)` |
| Search for an arbitrary value | `O(n)` |
| Space | `O(n)` |

Why `O(log n)`?

```text
A complete binary tree with n nodes has height about log₂ n.
Sift up and sift down move at most one level per step.
```

#### 8. Heap vs Other Structures — Must Know

| Need | Heap | Sorted array | Unsorted array |
|---|---:|---:|---:|
| Get the best item | `O(1)` | `O(1)` | `O(n)` |
| Insert | `O(log n)` | `O(n)` | `O(1)` |
| Remove the best item | `O(log n)` | `O(1)` or `O(n)` | `O(n)` |
| Find an arbitrary value | `O(n)` | `O(log n)` | `O(n)` |

The heap is the balanced choice when you insert and remove the best item many times.

#### 9. Edge Cases / Common Mistakes

1. Believing a heap is sorted. Printing the array does **not** give sorted order.
2. Confusing a heap with a **BST**. A BST orders left < parent < right. A heap has no left/right order.
3. Expecting `O(log n)` search for a given value. It is `O(n)`.
4. Using a min-heap when the problem needs a max-heap (or the reverse).
5. Forgetting that equal priorities may come out in any order. A heap is not stable.

#### 10. When to Use / When Not to Use

**Use when:**

1. You repeatedly need the smallest or largest item.
2. You need the best `k` items out of many, or the best item from a stream.
3. You merge several sorted sources.

**Avoid when:**

1. You need all items in sorted order once. Just sort.
2. You need to search for arbitrary values, or update the priority of arbitrary items often.
3. You need a range query (use a balanced tree).

#### 11. Related Topics

1. Min Heap vs Max Heap
2. Complete Binary Tree Property
3. Heap Operations & Complexity
4. Priority Queue
5. Binary Tree (`01-data-structure/07-Tree`)

#### 12. Interview Must Remember

1. A heap = **complete binary tree + heap property**.
2. The **root is the best item**. Nothing else is ordered.
3. Peek `O(1)`. Insert and extract `O(log n)`. Build `O(n)`.
4. Use a heap for "repeatedly give me the min / max".
