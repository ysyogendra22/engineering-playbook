# Minimum Spanning Tree (MST)

#### 1. What Is It?

A **spanning tree** of a connected, undirected, weighted graph is a set of edges that:

- connects **all** the vertices,
- has **no cycle**,
- therefore has exactly **`V - 1` edges**.

A **minimum spanning tree (MST)** is the spanning tree with the **smallest total weight**.

Story: connect all cities with roads (or cables, or pipes) so that every city is reachable, and the total cost is as small as possible.

Two algorithms find it:

| Algorithm | Idea | Time | Best for |
|---|---|---|---|
| **Kruskal** (note 27) | sort all edges, add the cheapest edge that does not make a cycle (union-find) | `O(E log E)` | sparse graphs, edge list input |
| **Prim** (note 28) | grow one tree from a start node, always add the cheapest edge leaving the tree (heap) | `O(E log V)` | dense graphs, adjacency list |

Both give the same total weight (the tree itself may differ if several edges have equal weight).

#### 2. How It Works

```text
Graph:   A —1— B      edges: A-B 1, B-C 2, A-C 3, C-D 4, B-D 5
         |   / |
         3  2  5      MST needs 4 - 1 = 3 edges.
         | /   |
         C —4— D      pick A-B (1), B-C (2), C-D (4)  → total 7
                      skip A-C (3): A and C are already connected (cycle)
                      skip B-D (5): B and D are already connected (cycle)
```

The key fact: the cheapest edge that crosses between "inside the tree" and "outside the tree" is always safe to add. Both algorithms use this.

Facts to know:

- An MST has `V - 1` edges. If the graph is not connected, there is no spanning tree (only a spanning forest).
- MST is **not** the shortest path. The MST minimises the **total** weight of the whole tree. Dijkstra minimises the path to **each** node.
- Edges with equal weights can produce different (but equally good) MSTs.

#### 3. Kotlin Code

A tiny check you can write in an interview: given a set of edges, is it a spanning tree, and what is its weight?

```kotlin
// edges are [a, b, weight]. Returns the total weight if the edges form a spanning tree, otherwise -1.
fun spanningTreeWeight(n: Int, edges: List<IntArray>): Int {
    if (edges.size != n - 1) return -1                     // a spanning tree has exactly n - 1 edges
    val parent = IntArray(n) { it }
    fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }
    var total = 0
    for ((a, b, w) in edges) {
        val ra = find(a)
        val rb = find(b)
        if (ra == rb) return -1                            // a cycle
        parent[ra] = rb
        total += w
    }
    return total                                           // n - 1 edges and no cycle → connected
}

// Usage: the MST of the example graph (A=0, B=1, C=2, D=3)
val mst = listOf(intArrayOf(0, 1, 1), intArrayOf(1, 2, 2), intArrayOf(2, 3, 4))
println(spanningTreeWeight(4, mst))                        // 7
```

The full Kruskal and Prim code is in notes 27 and 28.

#### 4. Complexity

| Algorithm | Time | Space |
|---|---|---|
| Kruskal | `O(E log E)` | `O(V)` |
| Prim (binary heap) | `O(E log V)` | `O(V)` |
| Prim (array, dense graph) | `O(V²)` | `O(V)` |

#### 5. Common Mistakes

1. **Confusing MST with shortest path.**
2. **Using MST on a directed graph.** The usual MST algorithms are for undirected graphs.
3. **Expecting a result when the graph is disconnected.** There is no spanning tree. Detect it (fewer than `V - 1` edges were added).
4. **Forgetting that the MST has `V - 1` edges.**
5. **Assuming the MST is unique.** Equal weights can give different trees.

#### 6. Say This in the Interview

1. "I need to connect everything at the lowest total cost with no cycle, which is a minimum spanning tree."
2. "I will use Kruskal's algorithm with union-find: sort the edges and add each edge that joins two different groups. Time `O(E log E)`."
3. "The MST has `V - 1` edges. If I cannot add that many, the graph is disconnected."

#### 7. Quick Check

1. How many edges does an MST of 6 vertices have?
2. Does the MST give the shortest path between two nodes?

<details>
<summary>Answers</summary>

1. `5`.
2. No. It minimises the total weight of all edges, not the distance between two nodes.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1584 | Min Cost to Connect All Points (Medium) | MST on points (Kruskal or Prim) |
| 1135 | Connecting Cities With Minimum Cost (Medium, premium) | Kruskal |
| 1489 | Find Critical and Pseudo-Critical Edges in MST (Hard) | MST with forced/skipped edges |
| 1168 | Optimize Water Distribution in a Village (Hard, premium) | MST with a virtual node |
| 261 | Graph Valid Tree (Medium, premium) | a tree has `n - 1` edges |
