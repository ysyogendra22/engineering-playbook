# Lazy Deletion with Heap

#### 1. Definition — Must Know

1. **Lazy deletion** means you do **not** remove an item from the middle of a heap right away.
2. You **mark** it as deleted (usually in a `HashMap` or a `HashSet`) and **skip it later**, when it reaches the top.
3. The reason: removing an arbitrary item from a heap is `O(n)` (`PriorityQueue.remove(x)`), because the item must be found first.

#### 2. Why It Is Used — Must Know

1. It keeps every operation at `O(log n)` amortized.
2. A heap cannot find items by value. A mark is far cheaper than a search.
3. It is needed in sliding-window problems, Dijkstra, and streams where old items expire or change.

#### 3. How It Works — Must Know

Min-heap with `5, 3, 8`. We want to delete `5`, but it is not at the top.

```text
Heap (min):        3
                  / \
                 5   8

Step 1: remove(5)  → do NOT touch the heap. Record it:  deleted = {5: 1}
Step 2: peek()     → top is 3. Not marked → answer 3.
Step 3: poll()     → removes 3. Heap now has 5 on top.
Step 4: peek()     → top is 5. It is marked → discard it, lower its mark, look again.
                     top is now 8. Not marked → answer 8.
```

The stale item is cleaned **only when it reaches the top**. Items buried deeper never cost anything until then.

#### 4. Core Concepts — Must Know

1. **Mark, don't remove.** Use a `HashMap<T, Int>` (count of pending deletions) for values that can repeat, or a `HashSet<Id>` when every item has a unique id.
2. **Prune before you read the top.** Call `prune()` before every `peek()` and `poll()`.
3. **Keep a separate live size.** `heap.size` counts stale items too, so track `liveSize` yourself.
4. **Cost.** Each stale item is removed once, so the extra work is spread across operations (amortized `O(log n)`).
5. **Stale entries need memory.** The heap can grow bigger than the live data. Rebuild it if stale entries become the majority.

#### 5. Algorithm — Must Know

```text
remove(x):  deleted[x] += 1;  liveSize -= 1

prune():
    while heap is not empty and deleted[heap.peek()] > 0:
        deleted[heap.peek()] -= 1
        heap.poll()

peek():  prune();  return heap.peek()
poll():  prune();  liveSize -= 1;  return heap.poll()
```

#### 6. Kotlin Implementation — Must Know

**A min-heap that supports `remove(x)` in `O(log n)` amortized**

```kotlin
import java.util.PriorityQueue

class LazyMinHeap {
    private val heap = PriorityQueue<Int>()
    private val deleted = HashMap<Int, Int>()    // value → how many copies are marked deleted
    var size = 0                                  // live items only
        private set

    fun add(x: Int) {
        heap.add(x)
        size++
    }

    // The caller must make sure x is really in the heap
    fun remove(x: Int) {
        deleted[x] = (deleted[x] ?: 0) + 1
        size--
    }

    private fun prune() {
        while (heap.isNotEmpty()) {
            val top = heap.peek()
            val pending = deleted[top] ?: break
            if (pending == 1) deleted.remove(top) else deleted[top] = pending - 1
            heap.poll()
        }
    }

    fun peek(): Int? {
        prune()
        return heap.peek()          // null when empty
    }

    fun poll(): Int? {
        prune()
        val value = heap.poll() ?: return null
        size--
        return value
    }
}

// Usage
val h = LazyMinHeap()
h.add(5); h.add(3); h.add(8)
h.remove(5)
println(h.peek())   // 3
h.poll()
println(h.peek())   // 8   (5 was skipped)
```

**Dijkstra uses the same idea**: a node may be pushed several times with different distances. When you pop a stale entry, skip it.

```kotlin
// inside Dijkstra's loop
val (dist, node) = pq.poll()
if (dist > best[node]) continue        // stale entry: a shorter path was found later
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `add` | `O(log n)` |
| `remove` (mark) | `O(1)` |
| `peek` / `poll` | `O(log n)` amortized (includes pruning) |
| `PriorityQueue.remove(x)` for comparison | `O(n)` |
| Space | `O(n)`, including stale items |

#### 8. Common Lazy-Deletion Patterns — Must Know

1. **Sliding window max/min** — discard tops whose index is outside the window (see "Heap + Sliding Window").
2. **Sliding window median** — two heaps with a delayed-deletion map (see "Multiple Heap / Advanced Two-Heaps Patterns").
3. **Dijkstra** — skip entries whose distance is worse than the best known.
4. **Task cancel / reschedule** — mark a task id as cancelled, then skip it when it is popped.
5. **Changing a priority** — push a new entry with the new priority, mark the old one stale.

#### 9. Edge Cases / Common Mistakes

1. Using `heap.size` as the real size. It includes stale items.
2. Reading `peek()` without pruning first.
3. Calling `remove(x)` for a value that is not in the heap, which breaks `size` and leaves a mark that deletes a future item.
4. Only pruning in `poll()` and not in `peek()`.
5. Forgetting to decrease the mark count, so later equal values are skipped wrongly.
6. Not cleaning up when stale entries dominate. The heap grows without a limit in long-running systems.
7. Using lazy deletion with duplicate values but a `HashSet` mark. Use a count map, or unique ids.

#### 10. When to Use / When Not to Use

**Use when:**

1. Items must be deleted or changed in the middle and `O(n)` is too slow.
2. Old entries expire (windows, cancelled tasks, outdated distances).

**Avoid when:**

1. The heap is small and `PriorityQueue.remove(x)` is fast enough.
2. You need exact removal from memory immediately. Use a `TreeSet` / `TreeMap` (`O(log n)` removal by value).

#### 11. Related Topics

1. Heap + Sliding Window
2. Multiple Heap / Advanced Two-Heaps Patterns
3. Heap + HashMap Pattern
4. Priority Queue
5. Dijkstra (`02-algorithm/09-Graph Algorithms`)

#### 12. Interview Must Remember

1. **Mark now, remove later (when it reaches the top).**
2. Prune before `peek` and `poll`. Track your own live size.
3. `PriorityQueue.remove(x)` is `O(n)`. Lazy deletion avoids it.
4. A `TreeMap`/`TreeSet` is the alternative when exact removal is needed.
