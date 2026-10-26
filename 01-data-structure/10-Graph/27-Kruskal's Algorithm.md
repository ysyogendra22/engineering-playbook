# Kruskal's Algorithm

> The simplest way to build a minimum spanning tree. It uses sorting and union-find (note 23).

#### 1. What Is It?

**Kruskal's algorithm** builds a minimum spanning tree (note 26) by this greedy rule:

1. **Sort all edges** by weight, smallest first.
2. Go through them in order. **Add an edge if it joins two different groups** (no cycle). Skip it otherwise.
3. Stop when you have `V - 1` edges.

The "different groups?" check is exactly what **union-find** answers in almost constant time.

#### 2. How It Works

```text
Edges (sorted):  A-B 1,  B-C 2,  A-C 3,  C-D 4,  B-D 5        V = 4 → need 3 edges

A-B 1:  A and B are in different groups → add.     groups: {A,B} {C} {D}      total 1
B-C 2:  B and C are in different groups → add.     groups: {A,B,C} {D}        total 3
A-C 3:  A and C are in the SAME group → skip (it would make a cycle).
C-D 4:  C and D are in different groups → add.     groups: {A,B,C,D}          total 7
        3 edges added → stop.

MST weight = 7
```

If you finish all the edges and have fewer than `V - 1` edges, the graph is **not connected** and has no spanning tree.

*Min Cost to Connect All Points* (LeetCode 1584): the points are the vertices. The edge between two points costs their **Manhattan distance** (`|x1 - x2| + |y1 - y2|`). Every pair of points is an edge (a complete graph), so build all `n(n-1)/2` edges, then run Kruskal.

#### 3. Kotlin Code

```kotlin
// Kruskal on an edge list: edges are [a, b, weight]. Returns the MST weight, or -1 if the graph is not connected.
fun kruskal(n: Int, edges: Array<IntArray>): Int {
    val parent = IntArray(n) { it }
    fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    val sorted = edges.sortedBy { it[2] }                  // 1. sort by weight
    var total = 0
    var used = 0
    for ((a, b, w) in sorted) {
        val ra = find(a)
        val rb = find(b)
        if (ra != rb) {                                     // 2. joins two different groups
            parent[ra] = rb
            total += w
            used++
            if (used == n - 1) break                        // 3. enough edges
        }
    }
    return if (used == n - 1) total else -1
}

// Min Cost to Connect All Points (LeetCode 1584)
fun minCostConnectPoints(points: Array<IntArray>): Int {
    val n = points.size
    val edges = ArrayList<IntArray>()
    for (i in 0 until n) for (j in i + 1 until n) {
        val cost = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1])
        edges.add(intArrayOf(i, j, cost))
    }
    return kruskal(n, edges.toTypedArray())
}
```

Checks: `kruskal(4, [[0,1,1],[1,2,2],[0,2,3],[2,3,4],[1,3,5]])` → `7`. `minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])` → `20`. `kruskal(3, [[0,1,5]])` → `-1` (node 2 is not connected).

The edge count for 1584 is about `n²/2`. For `n = 1000` that is 500,000 edges, which is fine. For a larger `n`, use Prim's algorithm with an array (note 28).

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Sorting the edges | `O(E log E)` | `O(E)` |
| Union-find over `E` edges | `O(E · α(V))` | `O(V)` |
| **Total** | **`O(E log E)`** | `O(V + E)` |

For 1584: `E = n²/2`, so `O(n² log n)`.

#### 5. Common Mistakes

1. **Not sorting the edges.**
2. **Adding an edge without the union-find check**, so cycles appear.
3. **Not checking** that exactly `V - 1` edges were used (disconnected graph).
4. **Unions on nodes instead of roots.** Always `find` first.
5. **Counting each undirected edge twice** when building from an adjacency list. Build the edge list once.
6. **Overflow in the total weight.** Use `Long` when weights are large.

#### 6. Say This in the Interview

1. "I sort the edges by weight and take each edge that joins two different components. Union-find tells me that quickly."
2. "I stop after `V - 1` edges. If I cannot reach that, the graph is not connected."
3. "Time `O(E log E)`, dominated by sorting."

#### 7. Quick Check

1. Why do we skip an edge whose two ends are already in the same group?
2. What does the algorithm do when it has `V - 1` edges?

<details>
<summary>Answers</summary>

1. Adding it would create a cycle, and a tree has no cycle.
2. It stops. A spanning tree is complete.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1584 | Min Cost to Connect All Points (Medium) | Kruskal on all pairs |
| 1135 | Connecting Cities With Minimum Cost (Medium, premium) | Kruskal; `-1` if not connected |
| 1489 | Find Critical and Pseudo-Critical Edges in MST (Hard) | run Kruskal with an edge forced or skipped |
| 684 | Redundant Connection (Medium) | the union-find part alone |
| 1168 | Optimize Water Distribution in a Village (Hard, premium) | add a virtual node, then Kruskal |
