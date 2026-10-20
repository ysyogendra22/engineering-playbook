# BFS

> The most important use of a queue. Many Medium and Hard interview questions are BFS in disguise.

#### 1. What Is It?

**BFS** (Breadth-First Search) visits nodes in **rings around the start**: first the start, then everything 1 step away, then everything 2 steps away, and so on.

It uses:

- a **queue** to remember which nodes to visit next,
- a **visited** set so no node is visited twice.

It works on graphs, trees, grids, and "state" problems (words, puzzles, lock codes). The full graph note is in `01-data-structure/10-Graph/09-BFS — Breadth First Search.md`.

Because nodes closer to the start are always handled first, BFS finds the **fewest steps** when every step costs the same.

#### 2. How It Works

```text
Graph:   0 — 1 — 3          adjacency list:
         |        |         0: [1, 2]
         2 ———————┘         1: [0, 3]
                            2: [0, 3]
                            3: [1, 2]

queue [0]           visited {0}
take 0 → add 1, 2   queue [1, 2]      visited {0, 1, 2}
take 1 → add 3      queue [2, 3]      visited {0, 1, 2, 3}
take 2 → 3 is seen  queue [3]
take 3 →            queue []

visit order: 0, 1, 2, 3
```

**The rule that avoids most bugs:** mark a node visited **when you add it to the queue**, not when you take it out. Otherwise the same node can be added many times.

BFS or DFS?

| | BFS | DFS |
|---|---|---|
| Uses | queue | stack or recursion |
| Order | level by level | deep first |
| Shortest path (equal steps) | **yes** | no |

#### 3. Kotlin Code

```kotlin
// BFS on an adjacency list. Returns the order in which nodes are visited.
fun bfs(graph: List<List<Int>>, start: Int): List<Int> {
    val visited = BooleanArray(graph.size)
    val order = mutableListOf<Int>()
    val queue = ArrayDeque<Int>()

    visited[start] = true                    // mark when you ADD
    queue.addLast(start)

    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        order.add(node)
        for (next in graph[node]) {
            if (!visited[next]) {
                visited[next] = true
                queue.addLast(next)
            }
        }
    }
    return order
}

// Usage
val graph = listOf(listOf(1, 2), listOf(0, 3), listOf(0, 3), listOf(1, 2))
println(bfs(graph, 0))      // [0, 1, 2, 3]
```

If the graph can be **disconnected**, start a BFS from every node that is not yet visited:

```kotlin
fun countComponents(graph: List<List<Int>>): Int {
    val visited = BooleanArray(graph.size)
    var components = 0
    for (s in graph.indices) {
        if (visited[s]) continue
        components++
        val queue = ArrayDeque<Int>()
        visited[s] = true
        queue.addLast(s)
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            for (next in graph[node]) {
                if (!visited[next]) {
                    visited[next] = true
                    queue.addLast(next)
                }
            }
        }
    }
    return components
}
```

#### 4. Complexity

For `V` nodes and `E` edges:

| | Time | Space |
|---|---|---|
| BFS with an adjacency list | `O(V + E)` | `O(V)` |

#### 5. Common Mistakes

1. **Marking visited after taking the node out of the queue.** The same node enters the queue many times.
2. **Forgetting to mark the start node.**
3. **Missing parts of a disconnected graph.**
4. **Using BFS for shortest path in a weighted graph.** Use Dijkstra.
5. **Not checking grid bounds** (index out of range).
6. **Using `list.removeAt(0)`** as the queue. It is `O(n)`.

#### 6. Say This in the Interview

1. "I will use BFS with a queue and a visited set, because I need the fewest steps."
2. "I mark nodes visited when I enqueue them to avoid duplicates."
3. "Time is `O(V + E)` and space is `O(V)`."
4. "If edges have different costs I would use Dijkstra instead."

#### 7. Quick Check

1. Does BFS use a queue or a stack?
2. Why mark a node visited when adding it to the queue?

<details>
<summary>Answers</summary>

1. A queue.
2. If you wait until you take it out, another node may add the same node again before that happens. The queue then holds duplicates.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 102 | Binary Tree Level Order Traversal (Medium) | BFS on a tree (note 06) |
| 133 | Clone Graph (Medium) | BFS with a map from old node to copy |
| 785 | Is Graph Bipartite? (Medium) | colour with BFS |
| 200 | Number of Islands (Medium) | BFS on a grid (note 09) |
| 207 | Course Schedule (Medium) | BFS on in-degrees (Kahn's algorithm) |
| 127 | Word Ladder (Hard) | BFS on words (note 07) |
