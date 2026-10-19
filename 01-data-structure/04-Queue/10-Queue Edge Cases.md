# Queue Edge Cases

#### 1. Definition — Must Know

1. These are the situations where queue code most often **breaks or gives wrong answers**.
2. Most come from five places: **empty queue**, **mutating while looping**, **visited timing in BFS**, **performance of the wrong structure**, and **boundaries** (grids, levels, windows).
3. Run this list before you say "done".

#### 2. Why It Is Used — Must Know

1. Interviewers watch if you test the empty and one-item cases yourself.
2. A single wrong line in BFS (visited timing) can cause duplicate work or a timeout.
3. In real apps, queue bugs show up as stuck tasks, lost events, and memory growth.

#### 3. How It Works — Must Know

The most common BFS bug:

```text
Wrong: mark visited when you REMOVE a node from the queue
       a node reachable from several nodes is added several times
       → queue grows, answer may still be right, but time can explode (and levels can be wrong)

Right: mark visited when you ADD a node to the queue
```

The most common level bug:

```text
while (i < queue.size) { ... queue.addLast(child) ... }     size changes every step
repeat(queue.size) { ... }                                   size is read once, before the loop
```

#### 4. Core Concepts — Must Know

| # | Edge case | What happens | Fix |
|---|---|---|---|
| 1 | Dequeue / peek on an empty queue | `NoSuchElementException` (Kotlin), or `null` (Java `poll`/`peek`) | check `isEmpty()`, or use `removeFirstOrNull()` / `poll()` |
| 2 | `null` item in `java.util.ArrayDeque` | `NullPointerException` | use Kotlin's `ArrayDeque`, or a wrapper type |
| 3 | `list.removeAt(0)` as dequeue | `O(n)` per call, slow | use `ArrayDeque` |
| 4 | Visited marked on dequeue | duplicates in the queue | mark on enqueue |
| 5 | Start node not marked | start is added again | mark the start before the loop |
| 6 | Level size read inside the loop | levels mix together | `repeat(queue.size)` |
| 7 | Changing the queue inside `for (x in queue)` | `ConcurrentModificationException` | use a drain loop |
| 8 | Disconnected graph | only one component visited | loop over all start nodes |
| 9 | Grid bounds | index out of range | bounds check before reading |
| 10 | `rows` vs `cols` in `r * cols + c` | wrong cells on non-square grids | decode with the same `cols` |
| 11 | Blocked start or target; start == target | wrong answer / crash | handle before the loop |
| 12 | Single element / empty input | loops skipped, result `null` | return early |
| 13 | Weighted edges with plain BFS | wrong "shortest" path | Dijkstra / 0-1 BFS |
| 14 | Unbounded queue growth | out-of-memory | bound the queue, or process faster |
| 15 | Shared queue across threads | lost or duplicated items | `BlockingQueue` / `Channel` |
| 16 | Using a queue where a priority queue is needed | wrong order | `PriorityQueue` |
| 17 | Expecting `PriorityQueue` to iterate in order | unordered | `poll` repeatedly |
| 18 | Circular queue full vs empty | `head == tail` is ambiguous | keep a `size` counter |
| 19 | Integer overflow in sums or ids | wrong values | `Long` |
| 20 | Mixing deque ends (`push`/`pop` on `Deque`) | order reversed | use `addLast` / `removeFirst` consistently |

#### 5. Algorithm — Must Know

Checklist before you finish:

```text
1. Can the queue be empty when I dequeue/peek?
2. Is visited marked at enqueue time (and for the start node)?
3. For levels: do I read queue.size once per level?
4. Could the graph be disconnected / the grid have blocked start or target?
5. Am I using the right end of the deque for each action?
6. Is a plain queue enough, or do I need priorities / weights?
7. Did I use ArrayDeque (not removeAt(0))?
8. Could ids or counts overflow Int?
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// 1. Empty queue
val q = ArrayDeque<Int>()
// q.removeFirst()                      // NoSuchElementException
println(q.removeFirstOrNull())          // null
println(q.firstOrNull())                // null

// 2. Java ArrayDeque rejects null
val jq = java.util.ArrayDeque<Int?>()
// jq.add(null)                         // NullPointerException

// 3. Level size: read once
val queue = ArrayDeque(listOf(1, 2, 3))
repeat(queue.size) {                    // runs exactly 3 times
    val x = queue.removeFirst()
    queue.addLast(x * 10)               // new items do not extend this loop
}
println(queue)                          // [10, 20, 30]

// 4. Do not modify while iterating
// for (x in queue) queue.addLast(x)    // ConcurrentModificationException

// 5. Mark visited on enqueue
fun bfsCount(graph: List<List<Int>>, start: Int): Int {
    val visited = BooleanArray(graph.size)
    val queue = ArrayDeque<Int>()
    visited[start] = true               // mark the start
    queue.addLast(start)
    var count = 0
    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        count++
        for (next in graph[node]) {
            if (!visited[next]) {
                visited[next] = true    // mark on enqueue
                queue.addLast(next)
            }
        }
    }
    return count
}

// 6. Deque ends: java.util.Deque.push adds to the FRONT
val dq = java.util.ArrayDeque<Int>()
dq.addLast(1); dq.addLast(2)
dq.push(0)                              // front!
println(dq)                             // [0, 1, 2]

// 7. PriorityQueue is not in insertion or sorted iteration order
val pq = java.util.PriorityQueue(listOf(5, 1, 3))
println(pq.poll())                      // 1  (smallest first, but only through poll)
```

#### 7. Time & Space Complexity — Must Know

| Concern | Impact |
|---|---|
| `removeAt(0)` as dequeue | `O(n)` per call → `O(n²)` total |
| Visited on dequeue | many duplicate entries → time and memory blow up |
| `contains` on a queue | `O(n)` each; keep a separate visited set |
| Unbounded queue | memory grows with the backlog |

#### 8. Common Bug Families — Must Know

1. **Empty-state bugs:** dequeue / peek on empty.
2. **Visited bugs:** wrong timing, missing start, missing components.
3. **Level bugs:** size read at the wrong time.
4. **Structure bugs:** wrong end of a deque; wrong queue type.
5. **Bounds bugs:** grid index, start/target blocked.
6. **Performance bugs:** `removeAt(0)`, `contains` in loops.
7. **Concurrency bugs:** unsynchronised queue.

#### 9. Edge Cases / Common Mistakes

1. Testing only the example from the problem.
2. Returning the number of nodes when the question wants edges (or the reverse).
3. Using `==` on `IntArray` items in a queue to check visited.
4. Storing `Pair<Int, Int>` in a huge BFS (many objects). Use an `Int` id.
5. Treating `ArrayDeque.remove(x)` as "dequeue". It removes a specific item.
6. Forgetting to handle a result when the queue ends without finding the target.
7. Printing a `PriorityQueue` and thinking it is sorted.

#### 10. When to Use / When Not to Use

**Use this checklist when:**

1. You finish any queue or BFS solution.

**Remember:**

1. Most queue bugs are about *when* you mark visited and *when* you read the size.

#### 11. Related Topics

1. Queue Operations
2. BFS
3. Level-by-Level Processing
4. Grid BFS

#### 12. Interview Must Remember

1. **Mark visited on enqueue, including the start.**
2. **`repeat(queue.size)` once per level.**
3. Check empty before `removeFirst()`, or use `removeFirstOrNull()`.
4. No `removeAt(0)`. No modifying a queue inside `for (x in queue)`.
