# Priority Queue

#### 1. Definition — Must Know

1. A **priority queue** is a collection where every element has a **priority**, and removing an element always returns the one with the **highest priority**.
2. It is an **abstract data type** (an idea with operations), not a specific structure.
3. A **heap** is the usual way to implement it.
4. A normal queue returns the **oldest** item (first in, first out). A priority queue returns the **most important** item, whatever its age.

#### 2. Why It Is Used — Must Know

1. Many problems are "always handle the most urgent item next": tasks, events, shortest paths, merging.
2. It separates *what you want* (the best item next) from *how it is stored* (a heap, a sorted list, a tree).
3. In interviews, "priority queue" is the name you say, and "heap" is how you explain the cost.

#### 3. How It Works — Must Know

Smaller number means higher priority:

```text
add("send email", 3)
add("fix crash", 1)
add("update docs", 5)
add("review PR", 2)

poll() → "fix crash"      (priority 1)
poll() → "review PR"      (priority 2)
poll() → "send email"     (priority 3)
poll() → "update docs"    (priority 5)
```

The order of `add` calls does not matter. The order of `poll` calls follows priority.

#### 4. Core Concepts — Must Know

1. **Operations:** `add`, `peek` (look at the best item), `poll` (remove the best item), `isEmpty`, `size`.
2. **Priority** — defined by a comparison: natural order of numbers, or a custom comparator.
3. **Implementations:**

| Implementation | Add | Peek | Poll |
|---|---:|---:|---:|
| Unsorted list | `O(1)` | `O(n)` | `O(n)` |
| Sorted list | `O(n)` | `O(1)` | `O(1)` or `O(n)` |
| **Binary heap** | `O(log n)` | `O(1)` | `O(log n)` |
| Balanced BST | `O(log n)` | `O(log n)` | `O(log n)` |

4. **Ties:** items with the same priority may come out in any order. The heap is **not stable**.
5. To keep first-in-first-out order among equal priorities, add a **sequence number** to the comparison.

#### 5. Algorithm — Must Know

The contract, in pseudocode:

```text
interface PriorityQueue<T>:
    add(item)        // insert with its priority
    peek(): T?       // best item, not removed
    poll(): T?       // best item, removed
    size, isEmpty
```

Typical use:

```text
add all work items
while the queue is not empty:
    item = poll()
    handle item
    (handling may add new items)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

data class Job(val name: String, val priority: Int)

val queue = PriorityQueue<Job>(compareBy<Job> { it.priority })   // smaller number first

queue.add(Job("send email", 3))
queue.add(Job("fix crash", 1))
queue.add(Job("review PR", 2))

while (queue.isNotEmpty()) {
    println(queue.poll().name)   // fix crash, review PR, send email
}
```

More on comparators in "Kotlin `PriorityQueue`".

#### 7. Time & Space Complexity — Must Know

With a binary heap:

| Operation | Time |
|---|---:|
| `add` | `O(log n)` |
| `peek` | `O(1)` |
| `poll` | `O(log n)` |
| Space | `O(n)` |

Processing `n` items from start to finish costs `O(n log n)`.

#### 8. Common Priority Queue Patterns — Must Know

1. Task or job scheduling by importance or deadline.
2. Dijkstra's shortest path (always expand the closest node).
3. Event simulation (always process the earliest event).
4. Top K and Kth element problems.
5. Merging sorted sources (K-way merge).
6. Greedy algorithms that "always pick the best available".

#### 9. Edge Cases / Common Mistakes

1. Assuming first-in-first-out among equal priorities.
2. Changing an item's priority **after** adding it. The queue does not re-order itself.
3. Expecting `PriorityQueue` iteration or `toString` to be sorted. It is not.
4. Polling an empty queue. `poll()` returns `null`; `remove()` throws.
5. Confusing the abstract type with the structure. A priority queue does not have to be a heap.

#### 10. When to Use / When Not to Use

**Use when:**

1. The next item to handle depends on priority, not arrival time.
2. Items keep arriving while you process.

**Avoid when:**

1. Arrival order is what matters. Use a normal queue.
2. All items are known in advance and you need them sorted once. Just sort.
3. You must update or remove arbitrary items often. Add a map (see "Heap + HashMap Pattern").

#### 11. Related Topics

1. Heap Fundamentals
2. Kotlin `PriorityQueue`
3. Heap for Scheduling / Processing by Priority
4. Queue (`01-data-structure/04-Queue`)
5. Dijkstra (`02-algorithm/07-Graph Algorithms/01-Dijkstra's Algorithm — Shortest Path, Non-Negative Weights.md`)

#### 12. Interview Must Remember

1. A priority queue returns the **highest-priority** item, not the oldest.
2. It is an **idea**. A binary **heap** is the usual implementation.
3. `add` and `poll` are `O(log n)`. `peek` is `O(1)`.
4. Equal priorities have no guaranteed order. Add a sequence number if order matters.
