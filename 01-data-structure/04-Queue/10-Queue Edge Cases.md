# Queue Edge Cases

> Read this list before a queue or BFS interview. Run through it at the end of every solution.

#### 1. What Is It?

These are the situations where queue and BFS solutions most often **crash**, **run too slowly**, or **give a wrong answer**. Interviewers watch if you check them yourself. Most bugs come from five places:

1. an **empty** queue,
2. **when you mark visited** in BFS,
3. **when you read the queue size** for levels,
4. a **bad start** (blocked start, start equals target, disconnected graph),
5. the **wrong structure** (list as a queue, Deque ends mixed).

#### 2. The Checklist

| # | Edge case | What goes wrong | Fix |
|---|---|---|---|
| 1 | Dequeue or peek on an empty queue | `NoSuchElementException` | `isNotEmpty()` or `removeFirstOrNull()` |
| 2 | Visited marked when **removing** from the queue | duplicates in the queue, slow | mark when **adding** |
| 3 | Start node not marked visited | start is added again | mark it before the loop |
| 4 | Level size read inside the loop | levels mix together | `repeat(queue.size)` |
| 5 | Changing a queue inside `for (x in queue)` | `ConcurrentModificationException` | use a `while` loop |
| 6 | Disconnected graph | only one part is visited | start BFS from every unvisited node |
| 7 | Grid bounds | index out of range | check bounds **before** reading the cell |
| 8 | `rows` and `cols` mixed in `r * cols + c` | wrong cells on non-square grids | decode with the same `cols` |
| 9 | Blocked start or target; start equals target | wrong answer or crash | handle before the loop |
| 10 | Weighted edges with plain BFS | wrong "shortest" path | Dijkstra or 0-1 BFS |
| 11 | `list.removeAt(0)` as a dequeue | `O(n)` per call, slow | `ArrayDeque` |
| 12 | `null` in `java.util.ArrayDeque` | `NullPointerException` | use Kotlin's `ArrayDeque` |
| 13 | Java `Deque.push` adds to the **front** | order reversed | use `addLast` / `removeFirst` |
| 14 | Circular queue: full and empty look the same | wrong state | keep a `size` counter |
| 15 | A queue shared by threads | lost items | `BlockingQueue` or `Channel` |
| 16 | Unbounded queue | out of memory | bound the queue |
| 17 | Counting nodes vs counting moves | off-by-one answer | re-read the question |
| 18 | `Int` overflow in sums | wrong values | use `Long` |

#### 3. Kotlin Code

```kotlin
// 1. Empty queue
val q = ArrayDeque<Int>()
println(q.removeFirstOrNull())          // null  (q.removeFirst() would crash)

// 2 and 3. Mark visited when you ADD, and mark the start
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

// 4. Level size: read once
val queue = ArrayDeque(listOf(1, 2, 3))
repeat(queue.size) {                    // runs exactly 3 times
    val x = queue.removeFirst()
    queue.addLast(x * 10)               // new items do not extend this loop
}
println(queue)                          // [10, 20, 30]

// 13. Java Deque: push adds to the FRONT
val dq = java.util.ArrayDeque<Int>()
dq.addLast(1); dq.addLast(2)
dq.push(0)                              // goes to the front
println(dq)                             // [0, 1, 2]
```

#### 4. Complexity

Edge cases do not change the complexity. They change **correctness** and sometimes **speed**. For example, marking visited on dequeue can make a BFS far slower, and `removeAt(0)` makes each dequeue `O(n)`.

#### 5. Common Mistakes

1. **Testing only the example from the question.** Also test: empty input, one node, start equals target, no path, a cycle, a disconnected graph.
2. **Returning the number of nodes** when the question asks for edges (or the reverse).
3. **Storing `Pair<Int, Int>` in a huge BFS.** It creates many objects. An `Int` cell id is lighter.
4. **Printing a `PriorityQueue`** and thinking it is sorted. Only `poll()` gives the right order.

#### 6. Say This in the Interview

1. "Edge cases I will check: empty input, one node, start equals target, no path, and a disconnected graph."
2. "I mark nodes visited when I enqueue them, including the start."
3. "I read the queue size once per level."

#### 7. Quick Check

1. What goes wrong if you mark a node visited only after taking it out of the queue?
2. What does `repeat(queue.size)` protect you from?

<details>
<summary>Answers</summary>

1. The same node can be added by several neighbours before it is taken out. The queue gets duplicates and the work grows.
2. New items added during the round extending the current round. The size is read once at the start.

</details>

#### 8. Related LeetCode Questions

| # | Question | Edge case to watch |
|---|---|---|
| 1091 | Shortest Path in Binary Matrix (Medium) | blocked start, one cell |
| 994 | Rotting Oranges (Medium) | no fresh or no rotten oranges |
| 127 | Word Ladder (Hard) | target not in the list |
| 102 | Binary Tree Level Order Traversal (Medium) | empty tree |
| 622 | Design Circular Queue (Medium) | full versus empty |
