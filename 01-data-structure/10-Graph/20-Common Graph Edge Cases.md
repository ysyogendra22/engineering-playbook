# Common Graph Edge Cases

> Read this list before a graph interview. Run through it at the end of every solution.

#### 1. What Is It?

These are the situations where graph solutions most often **crash**, **loop forever**, or **give a wrong answer**. Interviewers watch if you check them yourself. Most bugs come from five places:

1. **cycles** and the `visited` set,
2. **disconnected** graphs,
3. **edge direction** (directed vs undirected),
4. **weights** (negative, zero, large),
5. **bad or tiny input** (empty, one node, self-loops, duplicates).

#### 2. The Checklist

| # | Edge case | What goes wrong | Fix |
|---|---|---|---|
| 1 | Cycle, no `visited` | infinite loop | keep a `visited` set |
| 2 | BFS marks visited on dequeue | duplicates in the queue, slow | mark on **enqueue** |
| 3 | Disconnected graph | only one component is processed | loop over all nodes |
| 4 | Undirected edge stored one way | half of the graph is unreachable | add both directions |
| 5 | Directed edge stored both ways | wrong paths and cycles | add one direction only |
| 6 | Wrong direction from `[a, b]` | wrong order (Course Schedule) | read: is it `a → b` or `b → a`? |
| 7 | Directed cycle check with a parent check | wrong answer | use 3 states or Kahn |
| 8 | Undirected cycle: parent seen as a cycle | false cycle | ignore the parent |
| 9 | BFS on a weighted graph | wrong "shortest" path | Dijkstra |
| 10 | Dijkstra with negative weights | wrong answer | Bellman-Ford |
| 11 | `Int.MAX_VALUE + w` | overflow | check for infinity first, or use `Long` |
| 12 | Start equals target | wrong answer | return `0` / `true` early |
| 13 | Target unreachable | crash following `parent` | return `-1` / empty |
| 14 | Empty graph, one node, no edges | crash on `graph[0]` | handle early |
| 15 | Self-loop (`a → a`) | counted as a cycle (correct) or ignored | decide from the question |
| 16 | Parallel (duplicate) edges | wrong in-degree or a missed cycle | count every edge, or de-duplicate |
| 17 | Node numbers from `1` | index out of range | allocate `n + 1` |
| 18 | Grid bounds read before checking | index error | check bounds first |
| 19 | `rows` / `cols` mixed in a cell id | wrong cells | decode with the same `cols` |
| 20 | Very deep recursion | `StackOverflowError` | BFS or an explicit stack |
| 21 | Changing the input graph or grid | caller's data is damaged | copy, or use a separate `visited` |

#### 3. Kotlin Code

```kotlin
// 1 and 2. visited, marked when you add to the queue
fun bfsCount(graph: List<List<Int>>, start: Int): Int {
    val visited = BooleanArray(graph.size)
    val queue = ArrayDeque<Int>()
    visited[start] = true                       // mark the start too
    queue.addLast(start)
    var count = 0
    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        count++
        for (next in graph[node]) {
            if (!visited[next]) {
                visited[next] = true            // mark on enqueue
                queue.addLast(next)
            }
        }
    }
    return count
}

// 3. All components
fun countComponents(graph: List<List<Int>>): Int {
    val visited = BooleanArray(graph.size)
    var components = 0
    for (s in graph.indices) {
        if (visited[s]) continue
        components++
        val stack = ArrayDeque<Int>()
        visited[s] = true
        stack.addLast(s)
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            for (next in graph[node]) if (!visited[next]) { visited[next] = true; stack.addLast(next) }
        }
    }
    return components
}

// 11. Safe infinity
val INF = Int.MAX_VALUE
fun relax(dist: IntArray, u: Int, v: Int, w: Int) {
    if (dist[u] != INF && dist[u] + w < dist[v]) dist[v] = dist[u] + w     // never add to INF
}

// 14. Tiny input
fun shortest(graph: List<List<Int>>, src: Int, dst: Int): Int {
    if (graph.isEmpty()) return -1
    if (src == dst) return 0
    // ... BFS ...
    return -1
}

// 16. Parallel edges: in-degree counts every edge
fun indegrees(n: Int, edges: Array<IntArray>): IntArray {
    val indegree = IntArray(n)
    for ((_, to) in edges) indegree[to]++
    return indegree
}
```

#### 4. Complexity

Edge cases do not change the complexity. They change **correctness**. Two exceptions: marking visited on dequeue can make a BFS far slower, and a recursive DFS can use too much stack.

#### 5. Common Mistakes

1. **Testing only the example from the question.** Also test: empty graph, one node, no edges, a cycle, a disconnected graph, start equals target.
2. **Not asking** whether the graph is directed, weighted, or can have duplicates and self-loops.
3. **Assuming node labels** are `0..n-1`.
4. **Returning the number of nodes** when the question asks for edges (or the reverse).

#### 6. Say This in the Interview

1. "Let me clarify: is the graph directed? Weighted? Can it be disconnected, or have cycles, self-loops, or duplicate edges?"
2. "Edge cases I will check: empty input, one node, start equals target, and unreachable targets."
3. "I mark nodes visited when I enqueue them."

#### 7. Quick Check

1. A graph has two separate parts. What must your loop do?
2. What can go wrong with `Int.MAX_VALUE + weight`?

<details>
<summary>Answers</summary>

1. Start a search from every unvisited node, not only from node 0.
2. It overflows to a negative number, so the "distance" looks tiny. Check for infinity before adding.

</details>

#### 8. Related LeetCode Questions

| # | Question | Edge case to watch |
|---|---|---|
| 1971 | Find if Path Exists in Graph (Easy) | start equals target |
| 207 | Course Schedule (Medium) | cycle, edge direction |
| 323 | Number of Connected Components (Medium, premium) | isolated nodes |
| 743 | Network Delay Time (Medium) | unreachable nodes, 1-based labels |
| 133 | Clone Graph (Medium) | empty graph, cycles |
| 200 | Number of Islands (Medium) | empty grid, bounds |
