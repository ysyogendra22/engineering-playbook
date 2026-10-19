# Queue Fundamentals

#### 1. Definition — Must Know

1. A **queue** is a collection where items leave in the **same order they arrived**: **FIFO** (First In, First Out).
2. You **add at the back** (enqueue) and **remove from the front** (dequeue).
3. You normally see only the **front** item. There is no random access in the middle.

#### 2. Why It Is Used — Must Know

1. It keeps **fairness and order**: the first request is handled first.
2. It is the data structure behind **BFS** (breadth-first search) and level-order traversal.
3. It connects parts of a system that work at different speeds (task queues, message queues, network buffers).
4. In Android: the main-thread `MessageQueue`, `WorkManager` jobs, `Flow` and `Channel` buffers.

#### 3. How It Works — Must Know

```text
front                    back
  ↓                        ↓
[ A ][ B ][ C ][ D ]   ←  enqueue(E) adds here
  ↑
dequeue() removes A

After enqueue(E) and dequeue():   [ B ][ C ][ D ][ E ]
```

```text
Queue = a line at a ticket counter:
people join at the back, the person at the front is served first.
```

Compare with a **stack** (LIFO): the last item in is the first out. A queue is the opposite.

#### 4. Core Concepts — Must Know

1. **FIFO order** — the oldest item leaves first.
2. **Three main operations:** `enqueue` (add), `dequeue` (remove), `peek` (look at the front). All `O(1)`.
3. **Queue types:**

| Type | What it does |
|---|---|
| Simple queue | plain FIFO |
| Circular queue | fixed array that wraps around |
| Deque | add and remove at both ends |
| Priority queue | the highest priority leaves first (a heap, not FIFO) |
| Blocking queue | `take()` waits when empty, `put()` waits when full |
| Monotonic queue | a deque kept in sorted order (window max/min) |

4. **Kotlin/JVM tools:**

| Tool | Use |
|---|---|
| `kotlin.collections.ArrayDeque<T>` | default queue/deque in Kotlin, fast at both ends |
| `java.util.ArrayDeque<T>` | same idea, no `null` items |
| `java.util.LinkedList<T>` | works as a `Queue`, but uses more memory |
| `java.util.PriorityQueue<T>` | priority order (study under Heap) |
| `BlockingQueue` / `Channel` | threads and coroutines |

5. A Kotlin **`MutableList`** can act as a queue, but `removeAt(0)` is `O(n)`. Avoid it.
6. Queues and stacks can be built from each other (see the later notes).

#### 5. Algorithm — Must Know

The common "process everything in order" loop:

```text
queue = [start items]
while queue is not empty:
    item = dequeue()
    handle item
    enqueue any new items that this item creates
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val queue = ArrayDeque<Int>()

queue.addLast(10)               // enqueue
queue.addLast(20)
queue.addLast(30)

println(queue.first())          // peek → 10
println(queue.removeFirst())    // dequeue → 10
println(queue)                  // [20, 30]
println(queue.size)             // 2
println(queue.isEmpty())        // false

// Safe versions for empty queues
println(queue.firstOrNull())        // 20, or null when empty
println(queue.removeFirstOrNull())  // 20, or null when empty

// Process in order
while (queue.isNotEmpty()) {
    val item = queue.removeFirst()
    println("Handling $item")
}
```

Using the Java `Queue` interface:

```kotlin
import java.util.LinkedList
import java.util.Queue

val q: Queue<String> = LinkedList()
q.offer("a")          // enqueue
q.offer("b")
println(q.peek())     // a
println(q.poll())     // a   (null if empty)
```

#### 7. Time & Space Complexity — Must Know

| Operation | `ArrayDeque` | `LinkedList` | `MutableList.removeAt(0)` |
|---|---:|---:|---:|
| Enqueue (add last) | `O(1)` amortized | `O(1)` | `O(1)` |
| Dequeue (remove first) | `O(1)` amortized | `O(1)` | **`O(n)`** |
| Peek | `O(1)` | `O(1)` | `O(1)` |
| Search | `O(n)` | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(n)`, bigger per item | `O(n)` |

`ArrayDeque` is "amortized" because the array grows sometimes, which is rare.

#### 8. Common Queue Patterns — Must Know

1. **BFS** on graphs, trees, and grids.
2. **Level-by-level processing.**
3. **Shortest path** in an unweighted graph.
4. **Sliding window with a deque** (monotonic queue).
5. **Task scheduling** and producer-consumer.
6. **Simulation:** hot potato, ticket queue, recent calls.
7. **Design questions:** queue from two stacks, circular queue.

#### 9. Edge Cases / Common Mistakes

1. Dequeuing from an empty queue. `removeFirst()` throws; `removeFirstOrNull()` returns `null`.
2. Using `list.removeAt(0)` as dequeue (`O(n)`).
3. Confusing queue (FIFO) with stack (LIFO).
4. Using `java.util.ArrayDeque` and adding `null`. It throws.
5. Iterating a queue while changing it.
6. Forgetting that the size changes inside the loop (see level-by-level).
7. Using a queue where a priority queue is needed.

#### 10. When to Use / When Not to Use

**Use when:**

1. Order of arrival matters.
2. You explore level by level (BFS).
3. You hand work between producers and consumers.

**Avoid when:**

1. You need the most recent item first. Use a stack.
2. You need the best item first. Use a priority queue.
3. You need random access. Use a list or array.

#### 11. Related Topics

1. Queue Operations
2. BFS
3. Stack (`01-data-structure/03-Stack`)
4. Heap / Priority Queue (`01-data-structure/08-Heap`)

#### 12. Interview Must Remember

1. **FIFO: add at the back, remove from the front.**
2. In Kotlin use `ArrayDeque` with `addLast` / `removeFirst`.
3. Never use `removeAt(0)` on a list as a queue.
4. A queue is the tool for BFS and level-order work.
