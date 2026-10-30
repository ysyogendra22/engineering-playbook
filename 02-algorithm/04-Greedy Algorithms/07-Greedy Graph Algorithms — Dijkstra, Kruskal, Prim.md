# Greedy Graph Algorithms — Dijkstra, Kruskal, Prim

> Three famous algorithms that are greedy at heart. The full versions are in the Graph folder (`Dijkstra's Algorithm`, `Kruskal's Algorithm`, `Prim's Algorithm`). This note shows the **greedy idea** and the code you should be able to write.

#### 1. What Is It?

| Algorithm | Problem | Greedy rule |
|---|---|---|
| **Dijkstra** | shortest path from one node, edges `>= 0` | always finalize the **closest** unfinished node |
| **Kruskal** | minimum spanning tree (MST) | add the **cheapest edge** that does not make a cycle |
| **Prim** | minimum spanning tree (MST) | grow one tree by adding the **cheapest edge leaving it** |

A **minimum spanning tree** connects all nodes with the smallest total edge weight and has no cycles.

#### 2. How It Works

**Dijkstra.** Keep `dist[]`. Put `(node, distance)` in a min-heap. Pop the closest node. It is final (no shorter path can come later, because all edges are non-negative). Relax its neighbours.

```text
0→1 (4), 0→2 (1), 2→1 (2), 1→3 (1), 2→3 (5)

pop 0 (0): dist[1] = 4, dist[2] = 1
pop 2 (1): dist[1] = 3, dist[3] = 6
pop 1 (3): dist[3] = 4
pop 3 (4)
dist = [0, 3, 1, 4]
```

**Kruskal.** Sort edges by weight. For each edge, if its two ends are in different groups (use **Union-Find**), add the edge and join the groups.

```text
edges: (0,1,1) (1,2,2) (0,2,3) (2,3,4) (1,3,5)
take (0,1,1)   take (1,2,2)   skip (0,2,3) cycle   take (2,3,4)   done: 1 + 2 + 4 = 7
```

**Prim** starts at one node and uses a min-heap of edges leaving the tree. It is Dijkstra-like. Use Kruskal when edges are given as a list, and Prim for dense graphs.

#### 3. Brute Force vs Optimized

| | Brute force | Greedy |
|---|---|---|
| Shortest path | try all paths (DFS), exponential | Dijkstra `O((V + E) log V)` |
| MST | try all subsets of edges, exponential | Kruskal `O(E log E)` |
| Negative edges | Dijkstra is **wrong** | use Bellman-Ford `O(V · E)` |

#### 4. Kotlin Code

```kotlin
import java.util.PriorityQueue

// Dijkstra: edges are [from, to, weight]; returns the distance to every node
fun dijkstra(n: Int, edges: List<IntArray>, src: Int): IntArray {
    val graph = Array(n) { mutableListOf<IntArray>() }
    for ((u, v, w) in edges) graph[u].add(intArrayOf(v, w))

    val dist = IntArray(n) { Int.MAX_VALUE }
    dist[src] = 0
    val heap = PriorityQueue<IntArray>(compareBy<IntArray> { it[1] })   // [node, distance]
    heap.add(intArrayOf(src, 0))
    while (heap.isNotEmpty()) {
        val (u, d) = heap.poll()
        if (d > dist[u]) continue                          // an older, longer entry
        for ((v, w) in graph[u]) {
            if (d + w < dist[v]) {
                dist[v] = d + w
                heap.add(intArrayOf(v, dist[v]))
            }
        }
    }
    return dist
}

// Kruskal with Union-Find: edges are [u, v, weight]; returns the MST weight, or -1 if not connected
fun kruskal(n: Int, edges: List<IntArray>): Int {
    val parent = IntArray(n) { it }
    fun find(x: Int): Int {
        var r = x
        while (parent[r] != r) { parent[r] = parent[parent[r]]; r = parent[r] }
        return r
    }
    var total = 0
    var used = 0
    for ((u, v, w) in edges.sortedBy { it[2] }) {
        val ru = find(u)
        val rv = find(v)
        if (ru != rv) { parent[ru] = rv; total += w; used++ }
    }
    return if (used == n - 1) total else -1
}
```

Checks: `dijkstra(4, [[0,1,4],[0,2,1],[2,1,2],[1,3,1],[2,3,5]], 0)` → `[0, 3, 1, 4]`. `kruskal(4, [[0,1,1],[1,2,2],[0,2,3],[2,3,4],[1,3,5]])` → `7`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Dijkstra (heap) | `O((V + E) log V)` | `O(V + E)` |
| Kruskal | `O(E log E)` | `O(V)` |
| Prim (heap) | `O(E log V)` | `O(V + E)` |

#### 6. Common Mistakes

1. **Dijkstra with negative edges.** The "closest is final" rule breaks.
2. **Forgetting `if (d > dist[u]) continue`.** Old heap entries get processed again (slower, not wrong).
3. **`Int.MAX_VALUE + w` overflow** if you relax from an unreached node. Skip nodes that were not reached.
4. **Kruskal without Union-Find** (cycle check by DFS is too slow).
5. **Not checking that the graph is connected** for an MST (`used == n − 1`).
6. **Using BFS** for a weighted graph.

#### 7. Say This in the Interview

1. "Dijkstra is greedy: the closest unfinished node cannot be improved later because there are no negative edges."
2. "Kruskal sorts the edges and uses Union-Find to skip any edge that would make a cycle."
3. "With negative edges I would use Bellman-Ford."

#### 8. Quick Check

1. Why does Dijkstra fail with negative edges?
2. What does Kruskal's Union-Find check?

<details>
<summary>Answers</summary>

1. A later, negative edge could make a "finished" node shorter.
2. Whether the two ends of an edge are already connected (a cycle).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium) | Dijkstra |
| 1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) (Medium) | Dijkstra on a grid |
| 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) (Medium) | Kruskal or Prim |
| 1135 | [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) (Medium, premium) | Kruskal |
| 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Medium) | Bellman-Ford style |
