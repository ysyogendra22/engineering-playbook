# Heapify — Basic Concept

#### 1. Definition — Must Know

1. **Heapify** means fixing a heap at **one node**, by moving that node to its correct place.
2. The usual form is **heapify down** (sift down): when a node is worse than one of its children, swap it with the better child and repeat.
3. The precondition is important: **both subtrees of the node are already valid heaps**. Only the node itself may be out of place.

#### 2. Why It Is Used — Must Know

1. It is the repair step behind `extract`, `build heap`, and `heap sort`.
2. It restores the order rule without rebuilding anything.
3. Understanding it makes "Build Heap" and "Heap Sort" easy.

#### 3. How It Works — Must Know

A min-heap where only the root is wrong. Subtrees at `3` and `4` are valid heaps:

```text
        9                       3                      3
      /   \     swap 9 and 3   /   \   swap 9 and 5   /   \
     3     4    ───────────►  9     4  ───────────►  5     4
    / \                      / \                    / \
   5   6                    5   6                  9   6
```

1. Compare `9` with its children `3` and `4`. The smaller child is `3`. `3 < 9`, so swap.
2. Now `9` sits where `3` was, with children `5` and `6`. The smaller child is `5`. `5 < 9`, so swap.
3. `9` is now a leaf. Stop.

**Heapify up** is the mirror image. A new item at the bottom moves up while it is better than its parent. It is used by `insert`.

#### 4. Core Concepts — Must Know

1. **Precondition:** both child subtrees are valid heaps.
2. **Pick the better child** (smaller for a min-heap, larger for a max-heap) before comparing with the node.
3. **Stop** when the node is as good as both children, or it has none.
4. **Work moves down one level per step**, so the cost is at most the height of the node.
5. **Heapify down** is for removals and building. **Heapify up** is for insertions.

#### 5. Algorithm — Must Know

```text
heapifyDown(array, i, size):
    loop:
        left = 2*i + 1, right = 2*i + 2
        smallest = i
        if left < size and array[left] < array[smallest]: smallest = left
        if right < size and array[right] < array[smallest]: smallest = right
        if smallest == i: stop
        swap(array[i], array[smallest])
        i = smallest
```

For a max-heap, change `<` to `>` and name the variable `largest`.

#### 6. Kotlin Implementation — Must Know

```kotlin
// Min-heap heapify down on an IntArray, looking only at the first `size` items
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

// Heapify up, used after adding an item at index `start`
fun heapifyUp(arr: IntArray, start: Int) {
    var i = start
    while (i > 0) {
        val parent = (i - 1) / 2
        if (arr[parent] <= arr[i]) return
        val temp = arr[i]; arr[i] = arr[parent]; arr[parent] = temp
        i = parent
    }
}
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time | Space |
|---|---:|---:|
| Heapify down from node `i` | `O(height of i)`, at most `O(log n)` | `O(1)` |
| Heapify up from node `i` | `O(depth of i)`, at most `O(log n)` | `O(1)` |

Why `O(log n)`?

```text
Each swap moves the item one level. A heap has about log n levels.
```

#### 8. Common Heapify Patterns — Must Know

1. After `extract`: put the last item at the root, then heapify down.
2. After `insert`: heapify up from the last index.
3. For `build heap`: heapify down from every parent, starting at the last parent (see "Build Heap").
4. For `heap sort`: swap the root to the end, shrink the size, heapify down (see "Heap Sort — Concept").

#### 9. Edge Cases / Common Mistakes

1. Calling heapify on a node whose subtrees are **not** valid heaps. The result is wrong.
2. Comparing the node with the **first** child instead of the **better** child.
3. Not passing a `size`, so the loop reads items that were already removed (in heap sort).
4. Stopping after one swap. Keep going until the item is in place.
5. Mixing up heapify up and heapify down.

#### 10. When to Use / When Not to Use

**Use when:**

1. A single item is out of place in an otherwise valid heap.
2. You build or sort a heap in place.

**Avoid when:**

1. Many items are out of place in an unordered array. Use the "Build Heap" loop.

#### 11. Related Topics

1. Heap Operations & Complexity
2. Build Heap
3. Heap Sort — Concept
4. Complete Binary Tree Property

#### 12. Interview Must Remember

1. Heapify = repair **one node**, assuming both subtrees are valid heaps.
2. **Down** after a removal. **Up** after an insertion.
3. Swap with the **better child** each time.
4. Cost is at most `O(log n)` per call.
