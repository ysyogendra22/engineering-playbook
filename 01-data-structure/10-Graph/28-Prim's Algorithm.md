# Prim's Algorithm

> The second way to build a minimum spanning tree. It grows one tree, like Dijkstra.

#### 1. What Is It?

**Prim's algorithm** builds a minimum spanning tree (note 26) by growing **one tree** from a starting node:

1. Start with any node in the tree.
2. Look at all edges that go from the tree to a node **outside** the tree.
3. Add the **cheapest** one. The new node joins the tree.
4. Repeat until all nodes are in the tree.

It looks like Dijkstra, with one change: the priority is the **edge weight**, not the total distance from the start.

| | Kruskal | Prim |
|---|---|---|
| Idea | sort edges, join groups | grow one tree |
| Needs | union-find | priority queue (or an array) |
| Best for | few edges (sparse) | many edges (dense), adjacency list |

#### 2. How It Works

```text
Edges: A-B 1, B-C 2, A-C 3, C-D 4, B-D 5          start at A

tree = {A}.   Edges leaving the tree: A-B 1, A-C 3          cheapest: A-B 1 → add B      total 1
tree = {A,B}. Edges leaving: A-C 3, B-C 2, B-D 5            cheapest: B-C 2 → add C      total 3
tree = {A,B,C}. Edges leaving: C-D 4, B-D 5                 cheapest: C-D 4 → add D      total 7
all 4 nodes in the tree

MST weight = 7
```

Implementation with a min-heap of `(weight, node)`: pop the cheapest. If the node is already in the tree, skip it (stale entry). Otherwise add it to the tree, add its weight to the total, and push all its edges to nodes outside the tree.

For a **complete graph of points** (LeetCode 1584), there is a simple `O(n²)` version with no heap: keep `minCost[v]` = the cheapest edge from the tree to `v`, and pick the unused node with the smallest `minCost` each round.

#### 3. Kotlin Code

```kotlin
import java.util.PriorityQueue

// Prim with an adjacency list: graph[u] = list of (v, weight). Returns the MST weight, or -1 if not connected.
fun prim(n: Int, graph: List<List<Pair<Int, Int>>>): Int {
    val inTree = BooleanArray(n)
    val pq = PriorityQueue<IntArray>(compareBy { it[0] })      // [weight, node]
    pq.add(intArrayOf(0, 0))                                    // start at node 0 with cost 0
    var total = 0
    var added = 0

    while (pq.isNotEmpty() && added < n) {
        val (w, u) = pq.poll()
        if (inTree[u]) continue                                  // stale entry
        inTree[u] = true
        total += w
        added++
        for ((v, weight) in graph[u]) {
            if (!inTree[v]) pq.add(intArrayOf(weight, v))
        }
    }
    return if (added == n) total else -1
}

// Min Cost to Connect All Points (LeetCode 1584): O(n^2) Prim, no heap needed
fun minCostConnectPoints(points: Array<IntArray>): Int {
    val n = points.size
    val minCost = IntArray(n) { Int.MAX_VALUE }                  // cheapest edge from the tree to each node
    val inTree = BooleanArray(n)
    minCost[0] = 0
    var total = 0

    repeat(n) {
        var u = -1
        for (v in 0 until n) {                                   // pick the cheapest node outside the tree
            if (!inTree[v] && (u == -1 || minCost[v] < minCost[u])) u = v
        }
        inTree[u] = true
        total += minCost[u]
        for (v in 0 until n) {                                   // update the costs through the new node
            if (!inTree[v]) {
                val cost = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1])
                if (cost < minCost[v]) minCost[v] = cost
            }
        }
    }
    return total
}
```

Checks: with the example graph (A=0, B=1, C=2, D=3), `prim(4, graph)` → `7`. `minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])` → `20`.

#### 4. Complexity

| Version | Time | Space |
|---|---|---|
| Heap + adjacency list | `O(E log V)` | `O(V + E)` |
| Array version (dense / complete graph) | `O(V²)` | `O(V)` |

For 1584, `V = n` and `E = n²`, so the array version `O(n²)` beats the heap version `O(n² log n)`.

#### 5. Common Mistakes

1. **Using the total distance** from the start (the Dijkstra rule) instead of the **edge weight**.
2. **Not skipping stale entries** (nodes already in the tree).
3. **Not checking that all nodes were added** (disconnected graph).
4. **Starting from a node that does not exist** (empty graph).
5. **Building a huge edge list** for 1584 when the `O(n²)` array version needs none.

#### 6. Say This in the Interview

1. "Prim grows one tree. Each step I add the cheapest edge that leaves the tree, using a min-heap."
2. "It looks like Dijkstra, but the key is the edge weight, not the path length."
3. "For a dense or complete graph I use the `O(V²)` array version."

#### 7. Quick Check

1. What is the one difference between Prim and Dijkstra?
2. When is Prim better than Kruskal?

<details>
<summary>Answers</summary>

1. Prim uses the **edge weight** as the priority. Dijkstra uses the **total distance** from the start.
2. For dense graphs (many edges), especially when you do not want to sort a huge edge list.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1584 | Min Cost to Connect All Points (Medium) | `O(n²)` Prim |
| 1135 | Connecting Cities With Minimum Cost (Medium, premium) | Prim or Kruskal |
| 1168 | Optimize Water Distribution in a Village (Hard, premium) | MST with a virtual node |
| 743 | Network Delay Time (Medium) | Dijkstra, the similar algorithm |
