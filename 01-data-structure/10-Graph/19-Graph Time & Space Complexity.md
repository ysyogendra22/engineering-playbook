# Graph Time & Space Complexity

> Interviewers always ask "what is the complexity?". Learn this table and the reason behind each row.

#### 1. What Is It?

Graph complexity is written with two letters:

- **`V`** = the number of vertices,
- **`E`** = the number of edges.

The size of the input is `V + E`, so most graph walks are `O(V + E)`: each vertex and each edge is handled a fixed number of times.

A graph can be:

| Kind | `E` is about | Best storage |
|---|---|---|
| **Sparse** (few edges) | `V` | adjacency list |
| **Dense** (many edges) | `V²` | adjacency matrix |

For a **grid** with `R` rows and `C` columns: `V = R · C` and `E` is about `4 · R · C`, so grid walks are `O(R · C)`.

#### 2. How It Works

Why BFS and DFS are `O(V + E)`:

```text
for each vertex (visited once)              → V
    for each neighbour in its list          → all lists together hold 2E (undirected) or E (directed) entries
→ total work V + E
```

The complexity table to remember:

| Algorithm | Time | Space | Note |
|---|---|---|---|
| BFS / DFS | `O(V + E)` | `O(V)` | adjacency list |
| BFS / DFS with a matrix | `O(V²)` | `O(V)` | scanning a row costs `V` |
| Connected components | `O(V + E)` | `O(V)` | |
| Cycle detection (DFS) | `O(V + E)` | `O(V)` | |
| Topological sort (DFS or Kahn) | `O(V + E)` | `O(V)` | |
| Shortest path, unweighted (BFS) | `O(V + E)` | `O(V)` | |
| 0-1 BFS | `O(V + E)` | `O(V)` | |
| **Dijkstra** (binary heap) | `O((V + E) log V)` | `O(V)` | no negative weights |
| Bellman-Ford | `O(V · E)` | `O(V)` | allows negative weights |
| Floyd-Warshall | `O(V³)` | `O(V²)` | all pairs |
| Union-Find (with both tricks) | `O(α(V))` per operation | `O(V)` | almost constant |
| **Kruskal** (MST) | `O(E log E)` | `O(V)` | sorting the edges |
| **Prim** (MST, binary heap) | `O(E log V)` | `O(V)` | |
| Bipartite check | `O(V + E)` | `O(V)` | |
| Clone graph | `O(V + E)` | `O(V)` | |

Memory for storing the graph:

| Storage | Memory |
|---|---|
| Adjacency list | `O(V + E)` |
| Adjacency matrix | `O(V²)` |
| Edge list | `O(E)` |

`α(V)` (inverse Ackermann) is below 5 for any input you will ever see, so treat it as constant.

#### 3. Kotlin Code

A BFS with the cost of each line written next to it:

```kotlin
fun bfs(graph: List<List<Int>>, start: Int) {
    val visited = BooleanArray(graph.size)          // O(V) memory
    val queue = ArrayDeque<Int>()
    visited[start] = true
    queue.addLast(start)
    while (queue.isNotEmpty()) {                    // each vertex enters the queue once → V times
        val node = queue.removeFirst()
        for (next in graph[node]) {                 // over the whole run, the lists hold E entries → E checks
            if (!visited[next]) {
                visited[next] = true
                queue.addLast(next)
            }
        }
    }
}
// Total time: O(V + E).   Extra memory: O(V) for visited and the queue.
```

Dijkstra's extra `log V` comes from the heap: each of the up to `E` pushes costs `O(log V)`.

#### 4. Complexity

This whole note is the complexity table above.

#### 5. Common Mistakes

1. **Saying `O(V²)` for BFS on an adjacency list.** It is `O(V + E)`.
2. **Forgetting the `log` in Dijkstra.**
3. **Counting a grid as `O(V + E)` with the wrong `V`.** Use `O(R · C)`.
4. **Forgetting recursion memory.** Recursive DFS uses `O(V)` stack space in the worst case.
5. **Not saying what `V` and `E` are** in the answer.
6. **Calling union-find `O(1)` without saying "amortized, almost constant".**

#### 6. Say This in the Interview

1. "Let `V` be the number of nodes and `E` the number of edges. BFS and DFS are `O(V + E)` time and `O(V)` space."
2. "Dijkstra with a binary heap is `O((V + E) log V)`."
3. "For a grid with `R` rows and `C` columns, it is `O(R · C)`."

#### 7. Quick Check

1. What is the time of BFS on an adjacency list?
2. Which is bigger for a dense graph, `E` or `V`?

<details>
<summary>Answers</summary>

1. `O(V + E)`.
2. `E` (it can be close to `V²`).

</details>

#### 8. Related LeetCode Questions

| # | Question | Complexity to state |
|---|---|---|
| 200 | Number of Islands (Medium) | `O(R · C)` |
| 207 | Course Schedule (Medium) | `O(V + E)` |
| 743 | Network Delay Time (Medium) | `O((V + E) log V)` |
| 1584 | Min Cost to Connect All Points (Medium) | `O(n² log n)` with Kruskal on all pairs |
| 684 | Redundant Connection (Medium) | `O(E · α(V))` |
