# Heap Operations & Complexity

#### 1. Definition — Must Know

1. A heap has three core operations:
   - **Insert** — add an item.
   - **Peek** — read the best item without removing it.
   - **Extract Min / Max** — remove and return the best item.
2. Two repair moves keep the heap valid:
   - **Sift up** — move an item up while it is better than its parent.
   - **Sift down** — move an item down while a child is better than it.

#### 2. Why It Is Used — Must Know

1. These three operations are everything a priority queue needs.
2. Knowing how sift up and sift down work lets you explain *why* each costs `O(log n)`.
3. Interviews often ask you to write a small heap by hand.

#### 3. How It Works — Must Know

Min-heap `[2, 5, 4, 9, 7]`:

```text
      2
     / \
    5   4
   / \
  9   7
```

**Insert `1`:**

```text
1. Put 1 at the end:        [2, 5, 4, 9, 7, 1]      (child of 4)
2. Sift up: 1 < 4 → swap    [2, 5, 1, 9, 7, 4]
3. Sift up: 1 < 2 → swap    [1, 5, 2, 9, 7, 4]
4. 1 is the root → stop
```

**Peek:** return the root → `1`.

**Extract min:**

```text
1. Save the root (1).
2. Move the last item (4) to the root:   [4, 5, 2, 9, 7]
3. Sift down: smaller child of 4 is 2 → swap  [2, 5, 4, 9, 7]
4. 4 has no children left in range → stop
5. Return 1
```

#### 4. Core Concepts — Must Know

1. **Insert** = add at the end + sift **up**.
2. **Extract** = move the last item to the root + sift **down**.
3. **Sift down picks the better (smaller, for a min-heap) child.** Swapping with the wrong child breaks the order.
4. Each sift moves at most the height of the tree, which is `log n`.
5. **Peek** reads index `0`. It changes nothing.

#### 5. Algorithm — Must Know

```text
insert(x):
    append x
    siftUp(last index)

peek():
    return array[0]

extract():
    top = array[0]
    array[0] = last item, remove the last slot
    siftDown(0)
    return top

siftUp(i):
    while i > 0 and array[i] is better than array[parent(i)]:
        swap(i, parent(i)); i = parent(i)

siftDown(i):
    loop:
        pick the better of the two children (if any)
        if that child is better than array[i]: swap and continue from the child
        else: stop
```

#### 6. Kotlin Implementation — Must Know

A small min-heap you can write in an interview:

```kotlin
class MinHeap {

    private val data = ArrayList<Int>()

    val size: Int get() = data.size

    fun peek(): Int? = data.firstOrNull()

    fun add(value: Int) {
        data.add(value)
        siftUp(data.lastIndex)
    }

    fun poll(): Int? {
        if (data.isEmpty()) return null
        val top = data[0]
        val last = data.removeAt(data.lastIndex)
        if (data.isNotEmpty()) {
            data[0] = last
            siftDown(0)
        }
        return top
    }

    private fun siftUp(start: Int) {
        var i = start
        while (i > 0) {
            val parent = (i - 1) / 2
            if (data[parent] <= data[i]) break
            swap(parent, i)
            i = parent
        }
    }

    private fun siftDown(start: Int) {
        var i = start
        while (true) {
            val left = 2 * i + 1
            val right = left + 1
            var smallest = i
            if (left < data.size && data[left] < data[smallest]) smallest = left
            if (right < data.size && data[right] < data[smallest]) smallest = right
            if (smallest == i) break
            swap(i, smallest)
            i = smallest
        }
    }

    private fun swap(a: Int, b: Int) {
        val temp = data[a]; data[a] = data[b]; data[b] = temp
    }
}
```

In real code, use `PriorityQueue` (see "Kotlin `PriorityQueue`").

#### 7. Time & Space Complexity — Must Know

| Operation | Time | Space |
|---|---:|---:|
| `peek` | `O(1)` | `O(1)` |
| `add` (insert) | `O(log n)` | `O(1)` |
| `poll` (extract) | `O(log n)` | `O(1)` |
| Whole heap | | `O(n)` |

Why `O(log n)`?

```text
The tree has height log n. A sift moves one level per step,
so it does at most log n swaps.
```

Insert is `O(1)` on average for random data, because most new items stay near the bottom. The worst case is still `O(log n)`.

#### 8. Common Operation Patterns — Must Know

1. **Repeated extract** gives items in sorted order. Doing it `n` times is heap sort.
2. **Insert then extract** in a loop keeps a heap at a fixed size (Top K).
3. **Peek then decide** is used before processing, for example "is the earliest deadline due yet?".
4. **Replace the root** (extract then insert) can be done in one sift down.

#### 9. Edge Cases / Common Mistakes

1. Calling `peek` or `poll` on an empty heap. `PriorityQueue` returns `null`. `remove()` throws.
2. Sifting down toward the **larger** child in a min-heap.
3. Forgetting to check that the right child exists before reading it.
4. Not removing the last slot before sifting down.
5. Using `remove(value)` and assuming `O(log n)`. Finding the value is `O(n)`.
6. Changing an item's priority after it is in the heap. The heap does not notice and becomes invalid.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need only the best item, again and again.

**Avoid when:**

1. You need to find, update, or delete arbitrary items quickly. See "Lazy Deletion with Heap" and "Heap + HashMap Pattern".

#### 11. Related Topics

1. Complete Binary Tree Property
2. Heapify — Basic Concept
3. Kotlin `PriorityQueue`
4. Build Heap

#### 12. Interview Must Remember

1. Insert = **add at the end, sift up**. Extract = **last item to the root, sift down**.
2. Peek `O(1)`. Insert and extract `O(log n)`.
3. Sift down swaps with the **better child**.
4. Empty-heap and "change priority later" are the two classic bugs.
