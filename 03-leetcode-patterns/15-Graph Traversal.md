# Graph Traversal

> Build the adjacency list, loop over every node, and search from each unvisited one.

#### 1. What Is It?

A **graph** is nodes (vertices) and edges. Traversal means visiting every reachable node once, with BFS (note 12) or DFS (note 13) and a `visited` set.

**Signals**

- Nodes and edges, "network", "friends", "routes", "cities and roads"
- A grid that behaves like a graph (islands, regions)
- "Number of **components**", "provinces", "islands"
- "Is there a **cycle**?", "is it **bipartite**?"
- "**Clone** a graph"
- Weighted shortest path (Dijkstra), minimum cost to connect (MST)

**Pick a representation**

| Representation | Space | Check an edge | Use |
|---|---|---|---|
| Adjacency list | `O(V + E)` | `O(degree)` | default for interviews |
| Adjacency matrix | `O(V²)` | `O(1)` | dense graphs, small `V` |
| Edge list | `O(E)` | `O(E)` | Kruskal, Union Find |

**Terms:** directed vs undirected, weighted vs unweighted, connected vs disconnected, cycle, DAG, component.

#### 2. How It Works

**Always loop over all nodes.** The graph may be disconnected.

```text
visited = {}
count = 0
for node in 0..n-1:
    if node not visited:
        count++
        dfs(node)          // marks the whole component
```

**Cycle detection**

| Graph | Method |
|---|---|
| Undirected | DFS with `parent`. Meeting a visited node that is not the parent is a cycle. (Or Union Find, note 17.) |
| Directed | three colours: 0 unvisited, 1 in the current path, 2 done. Meeting a colour-1 node is a cycle. (Or topological sort, note 16.) |

**Bipartite (two-colourable).** Colour a node 0, its neighbours 1, their neighbours 0, and so on. If an edge joins two nodes with the same colour, it is not bipartite.

**Clone a graph.** Map old node → new node. Copy a node, then copy its neighbours (reuse from the map if present).

**Weighted graphs**

| Need | Algorithm |
|---|---|
| Shortest path, no negative edges | **Dijkstra** with a min-heap, `O((V + E) log V)` |
| Shortest path with at most K edges, or negative edges | **Bellman-Ford**, `O(K · E)` |
| Connect all nodes with the least total weight | **MST**: Kruskal (sort edges + Union Find) or Prim |

**Multi-source search from borders** (Pacific Atlantic): instead of starting from every cell, start from the ocean cells and search *inward* to what can reach them.

#### 3. Brute Force vs Optimized

| Problem | Brute force | Better |
|---|---|---|
| Components | try each pair for connectivity, `O(V² · (V+E))` | one traversal with visited, `O(V + E)` |
| Pacific Atlantic | DFS from every cell, `O((rc)²)` | search from the borders, `O(rc)` |
| Shortest path (weighted) | try all paths | Dijkstra |
| Cheapest flights ≤ K stops | DFS over all routes | Bellman-Ford with K+1 rounds |

```kotlin
// Brute force: BFS from every node. A node counts as a new component only when it is the
// smallest label in everything it can reach. O(V * (V + E)).
fun countComponentsBrute(n: Int, edges: Array<IntArray>): Int {
    val graph = Array(n) { mutableListOf<Int>() }
    for ((a, b) in edges) { graph[a].add(b); graph[b].add(a) }
    var count = 0
    for (start in 0 until n) {
        val seen = BooleanArray(n)
        val queue = ArrayDeque<Int>()
        queue.addLast(start)
        seen[start] = true
        var smallest = start
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            smallest = minOf(smallest, node)
            for (next in graph[node]) if (!seen[next]) { seen[next] = true; queue.addLast(next) }
        }
        if (smallest == start) count++
    }
    return count
}
```

The `visited` set removes the repeated work: after the first search, every node of that component is skipped.

#### 4. Kotlin Code

```kotlin
import java.util.PriorityQueue

fun buildGraph(n: Int, edges: Array<IntArray>, directed: Boolean = false): Array<MutableList<Int>> {
    val graph = Array(n) { mutableListOf<Int>() }
    for ((a, b) in edges) {
        graph[a].add(b)
        if (!directed) graph[b].add(a)
    }
    return graph
}

// Number of Connected Components in an Undirected Graph (LeetCode 323; free alternative: 547)
fun countComponents(n: Int, edges: Array<IntArray>): Int {
    val graph = buildGraph(n, edges)
    val visited = BooleanArray(n)
    fun dfs(node: Int) {
        visited[node] = true
        for (next in graph[node]) if (!visited[next]) dfs(next)
    }
    var count = 0
    for (i in 0 until n) if (!visited[i]) { count++; dfs(i) }
    return count
}

// Number of Provinces (LeetCode 547): the graph is given as a matrix
fun findCircleNum(isConnected: Array<IntArray>): Int {
    val n = isConnected.size
    val visited = BooleanArray(n)
    fun dfs(i: Int) {
        visited[i] = true
        for (j in 0 until n) if (isConnected[i][j] == 1 && !visited[j]) dfs(j)
    }
    var provinces = 0
    for (i in 0 until n) if (!visited[i]) { provinces++; dfs(i) }
    return provinces
}

// Cycle in an undirected graph: parent check
fun hasCycleUndirected(n: Int, edges: Array<IntArray>): Boolean {
    val graph = buildGraph(n, edges)
    val visited = BooleanArray(n)
    fun dfs(node: Int, parent: Int): Boolean {
        visited[node] = true
        for (next in graph[node]) {
            if (!visited[next]) { if (dfs(next, node)) return true }
            else if (next != parent) return true
        }
        return false
    }
    for (i in 0 until n) if (!visited[i] && dfs(i, -1)) return true
    return false
}

// Cycle in a directed graph: colours (0 new, 1 in path, 2 done)
fun hasCycleDirected(n: Int, edges: Array<IntArray>): Boolean {
    val graph = buildGraph(n, edges, directed = true)
    val state = IntArray(n)
    fun dfs(node: Int): Boolean {
        state[node] = 1
        for (next in graph[node]) {
            if (state[next] == 1) return true
            if (state[next] == 0 && dfs(next)) return true
        }
        state[node] = 2
        return false
    }
    for (i in 0 until n) if (state[i] == 0 && dfs(i)) return true
    return false
}

// Clone Graph (LeetCode 133)
class Node(var `val`: Int) {
    var neighbors: MutableList<Node> = mutableListOf()
}

fun cloneGraph(node: Node?): Node? {
    if (node == null) return null
    val copies = HashMap<Node, Node>()
    fun clone(cur: Node): Node {
        copies[cur]?.let { return it }
        val copy = Node(cur.`val`)
        copies[cur] = copy                              // register BEFORE visiting neighbours
        for (next in cur.neighbors) copy.neighbors.add(clone(next))
        return copy
    }
    return clone(node)
}

// Is Graph Bipartite? (LeetCode 785)
fun isBipartite(graph: Array<IntArray>): Boolean {
    val color = IntArray(graph.size) { -1 }
    for (start in graph.indices) {
        if (color[start] != -1) continue
        color[start] = 0
        val queue = ArrayDeque<Int>()
        queue.addLast(start)
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            for (next in graph[node]) {
                if (color[next] == -1) { color[next] = 1 - color[node]; queue.addLast(next) }
                else if (color[next] == color[node]) return false
            }
        }
    }
    return true
}

// Pacific Atlantic Water Flow (LeetCode 417): search inward from each ocean
fun pacificAtlantic(heights: Array<IntArray>): List<List<Int>> {
    val rows = heights.size
    val cols = heights[0].size
    val pacific = Array(rows) { BooleanArray(cols) }
    val atlantic = Array(rows) { BooleanArray(cols) }
    fun dfs(r: Int, c: Int, seen: Array<BooleanArray>) {
        seen[r][c] = true
        for ((dr, dc) in arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))) {
            val nr = r + dr
            val nc = c + dc
            if (nr in 0 until rows && nc in 0 until cols && !seen[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                dfs(nr, nc, seen)                       // water flows down, so we climb up
            }
        }
    }
    for (r in 0 until rows) { dfs(r, 0, pacific); dfs(r, cols - 1, atlantic) }
    for (c in 0 until cols) { dfs(0, c, pacific); dfs(rows - 1, c, atlantic) }
    val result = mutableListOf<List<Int>>()
    for (r in 0 until rows) for (c in 0 until cols) {
        if (pacific[r][c] && atlantic[r][c]) result.add(listOf(r, c))
    }
    return result
}

// Network Delay Time (LeetCode 743): Dijkstra
fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
    val graph = Array(n + 1) { mutableListOf<IntArray>() }          // node -> [neighbour, weight]
    for ((u, v, w) in times) graph[u].add(intArrayOf(v, w))
    val dist = IntArray(n + 1) { Int.MAX_VALUE }
    dist[k] = 0
    val heap = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })   // [distance, node]
    heap.add(intArrayOf(0, k))
    while (heap.isNotEmpty()) {
        val (d, u) = heap.poll()
        if (d > dist[u]) continue                                    // stale entry
        for ((v, w) in graph[u]) {
            if (d + w < dist[v]) { dist[v] = d + w; heap.add(intArrayOf(dist[v], v)) }
        }
    }
    val answer = (1..n).maxOf { dist[it] }
    return if (answer == Int.MAX_VALUE) -1 else answer
}

// Cheapest Flights Within K Stops (LeetCode 787): Bellman-Ford limited to k + 1 edges
fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
    val INF = Int.MAX_VALUE / 2
    var dist = IntArray(n) { INF }
    dist[src] = 0
    repeat(k + 1) {
        val next = dist.clone()                                      // use only last round's values
        for ((u, v, w) in flights) {
            if (dist[u] + w < next[v]) next[v] = dist[u] + w
        }
        dist = next
    }
    return if (dist[dst] >= INF) -1 else dist[dst]
}

// Min Cost to Connect All Points (LeetCode 1584): Prim, O(n^2)
fun minCostConnectPoints(points: Array<IntArray>): Int {
    val n = points.size
    val dist = IntArray(n) { Int.MAX_VALUE }
    val inTree = BooleanArray(n)
    dist[0] = 0
    var total = 0
    repeat(n) {
        var u = -1
        for (i in 0 until n) if (!inTree[i] && (u == -1 || dist[i] < dist[u])) u = i
        inTree[u] = true
        total += dist[u]
        for (v in 0 until n) {
            if (!inTree[v]) {
                val d = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1])
                if (d < dist[v]) dist[v] = d
            }
        }
    }
    return total
}
```

Checks: `countComponents(5, [[0,1],[1,2],[3,4]])` → `2`; `(5, [[0,1],[1,2],[2,3],[3,4]])` → `1`. `findCircleNum([[1,1,0],[1,1,0],[0,0,1]])` → `2`. `hasCycleUndirected(3, [[0,1],[1,2],[2,0]])` → `true`; `(3, [[0,1],[1,2]])` → `false`. `hasCycleDirected(3, [[0,1],[1,2],[2,0]])` → `true`; `(3, [[0,1],[1,2]])` → `false`. `cloneGraph` of the square `1–2–3–4–1`: the copy's node 1 has neighbours `[2, 4]` and is a different object. `isBipartite([[1,3],[0,2],[1,3],[0,2]])` → `true`; `[[1,2,3],[0,2],[0,1,3],[0,2]]` → `false`. `pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])` → `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`. `networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)` → `2`; `([[1,2,1]], 2, 2)` → `-1`. `findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)` → `700`; with `k = 0` → `-1`. `minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])` → `20`.

Also in this family (same templates, not repeated here): **Surrounded Regions** (130) is border DFS then flip; **Number of Islands** (200) is note 13.

#### 5. Complexity

| Problem | Time | Space |
|---|---|---|
| DFS / BFS traversal | `O(V + E)` | `O(V)` |
| Grid traversal | `O(rows × cols)` | `O(rows × cols)` |
| Dijkstra (heap) | `O((V + E) log V)` | `O(V + E)` |
| Bellman-Ford (K rounds) | `O(K · E)` | `O(V)` |
| Prim (matrix version) | `O(V²)` | `O(V)` |
| Kruskal | `O(E log E)` | `O(V)` |

#### 6. Common Mistakes

1. **Searching from only one node** when the graph may be disconnected.
2. **No `visited` set**, giving an infinite loop on a cycle.
3. **Undirected edges added only one way** when building the graph.
4. **Cycle detection on a directed graph with the undirected parent trick** (wrong). Use colours.
5. **Clone graph:** registering the copy after visiting neighbours (infinite recursion).
6. **Dijkstra with negative weights.** It gives wrong answers. Use Bellman-Ford.
7. **Dijkstra:** no stale-entry check (`d > dist[u]`) wastes time.
8. **Bellman-Ford with K stops:** updating in place, so one round can use more than one new edge. Copy the array each round.
9. **Mixing 1-indexed node labels** with 0-indexed arrays (Network Delay Time uses `n + 1`).

#### 7. Say This in the Interview

1. "I'll build an adjacency list, then run DFS from every unvisited node. The number of DFS starts is the number of components. Time `O(V + E)`."
2. "For a directed cycle I track nodes on the current path with colours. An edge to a node on the path is a back edge, so there is a cycle."
3. "Every edge costs 1, so BFS. Edges have different non-negative costs, so Dijkstra with a min-heap."

#### 8. Quick Check

1. Which approach detects a cycle in an undirected graph without recursion state?
2. Why does Pacific Atlantic start from the oceans?

<details>
<summary>Answers</summary>

1. Union Find: if both endpoints already share a root, the edge creates a cycle.
2. Starting from every cell is `O((rc)²)`. Starting from the border cells and moving to equal or higher cells visits each cell a constant number of times.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) (Medium) | count components |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) (Medium) | map old → new |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium) | grid components |
| 130 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (Medium) | border DFS |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (Medium) | search from borders |
| 785 | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) (Medium) | two colours |
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium) | Dijkstra |
| 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Medium) | Bellman-Ford |
| 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) (Medium) | Prim / Kruskal |
| 323 | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Medium, premium) | use 547 instead |
