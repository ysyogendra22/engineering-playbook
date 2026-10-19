# BFS

#### 1. Definition — Must Know

1. **BFS** (Breadth-First Search) visits nodes **in rings around the start**: first the start, then everything 1 step away, then 2 steps away, and so on.
2. It uses a **queue** to remember which nodes to visit next, and a **visited** set so no node is visited twice.
3. It works on graphs, trees, grids, and implicit "state" graphs.
4. The full graph view is in `01-data-structure/10-Graph/09-BFS — Breadth First Search.md`. This note focuses on the **queue mechanics**.

#### 2. Why It Is Used — Must Know

1. It finds the **fewest steps** in an unweighted graph.
2. It explores a tree **level by level**.
3. It is one of the most asked interview patterns (`03-leetcode-patterns`, topic 12).

#### 3. How It Works — Must Know

```text
Graph:   0 — 1 — 3
         |        |
         2 ———————┘

adjacency: 0:[1,2]  1:[0,3]  2:[0,3]  3:[1,2]

queue [0]            visited {0}
take 0 → add 1, 2    queue [1, 2]       visited {0,1,2}
take 1 → add 3       queue [2, 3]       visited {0,1,2,3}
take 2 → 3 is seen   queue [3]
take 3 →             queue []

visit order: 0, 1, 2, 3
```

The queue is FIFO, so nodes closer to the start are always handled before nodes farther away.

#### 4. Core Concepts — Must Know

1. **Queue** = the frontier (nodes waiting to be processed).
2. **Visited** = nodes already queued or processed.
3. **Mark visited when you add to the queue**, not when you take it out. Otherwise the same node may enter the queue many times.
4. **Start:** put the start node in the queue and mark it visited.
5. **Disconnected graph:** run BFS from every unvisited node.
6. **Trees need no visited set** (no cycles) unless the tree is given as a graph.
7. **BFS vs DFS:**

| | BFS | DFS |
|---|---|---|
| Structure | queue | stack / recursion |
| Order | level by level | deep first |
| Shortest path (unweighted) | **yes** | no |
| Memory | wide graphs use more | deep graphs use more |

#### 5. Algorithm — Must Know

```text
BFS(start):
    queue = [start]; visited = {start}
    while queue is not empty:
        node = queue.removeFirst()
        process(node)
        for each neighbour of node:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.addLast(neighbour)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// BFS on an adjacency list, returns the visit order
fun bfs(graph: List<List<Int>>, start: Int): List<Int> {
    val visited = BooleanArray(graph.size)
    val order = mutableListOf<Int>()
    val queue = ArrayDeque<Int>()

    visited[start] = true
    queue.addLast(start)

    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        order.add(node)
        for (next in graph[node]) {
            if (!visited[next]) {
                visited[next] = true            // mark when adding
                queue.addLast(next)
            }
        }
    }
    return order
}

// BFS over every component (disconnected graph)
fun bfsAll(graph: List<List<Int>>): List<List<Int>> {
    val visited = BooleanArray(graph.size)
    val components = mutableListOf<List<Int>>()
    for (s in graph.indices) {
        if (visited[s]) continue
        val component = mutableListOf<Int>()
        val queue = ArrayDeque<Int>()
        visited[s] = true
        queue.addLast(s)
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            component.add(node)
            for (next in graph[node]) {
                if (!visited[next]) {
                    visited[next] = true
                    queue.addLast(next)
                }
            }
        }
        components.add(component)
    }
    return components
}

// Usage
val graph = listOf(listOf(1, 2), listOf(0, 3), listOf(0, 3), listOf(1, 2))
println(bfs(graph, 0))      // [0, 1, 2, 3]
```

#### 7. Time & Space Complexity — Must Know

For `V` nodes and `E` edges (adjacency list):

| Part | Cost |
|---|---:|
| Time | `O(V + E)` |
| Space (queue + visited) | `O(V)` |

With an adjacency matrix the time is `O(V²)`.

#### 8. Common BFS Patterns — Must Know

1. **Level-order traversal** of a tree (LeetCode 102).
2. **Shortest path** in an unweighted graph.
3. **Grid BFS:** islands, rotting oranges, shortest path in a binary matrix.
4. **Multi-source BFS:** start from many nodes at once.
5. **Word Ladder** and other "state" graphs.
6. **Bipartite check** (two-colour with BFS) (LeetCode 785).
7. **Topological sort with Kahn's algorithm** (BFS on in-degrees).
8. **0-1 BFS** and **bidirectional BFS** (advanced notes in this folder).

#### 9. Edge Cases / Common Mistakes

1. Marking visited **after** taking from the queue. The same node can be queued many times.
2. Forgetting to mark the start node.
3. Missing the disconnected parts.
4. Using BFS for shortest path in a **weighted** graph. Use Dijkstra.
5. Not checking bounds in a grid.
6. Empty graph or a single node.
7. Mixing `0-based` and `1-based` node numbers.
8. Using a `List` and `removeAt(0)` for the queue.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the fewest steps or the nearest target.
2. You need level-by-level output.

**Avoid when:**

1. Edges have different costs (Dijkstra).
2. You need all paths or a full deep exploration (DFS or backtracking).

#### 11. Related Topics

1. Level-by-Level Processing
2. Queue for Shortest Path
3. Graph BFS (`01-data-structure/10-Graph/09-BFS — Breadth First Search.md`)
4. Tree BFS (`01-data-structure/07-Tree/05-BFS - Level Order Traversal.md`)
5. BFS pattern (`03-leetcode-patterns`, topic 12)

#### 12. Interview Must Remember

1. **Queue + visited. Mark visited when you enqueue.**
2. Level by level; shortest path in an unweighted graph.
3. `O(V + E)` time, `O(V)` space.
4. Weighted edges → Dijkstra.
