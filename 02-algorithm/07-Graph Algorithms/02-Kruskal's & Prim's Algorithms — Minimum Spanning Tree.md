# Kruskal's & Prim's Algorithms — Minimum Spanning Tree

#### 1. Definition — Must Know

A **minimum spanning tree (MST)** connects every node in a weighted, undirected graph using the **smallest possible total edge weight**, with no cycles. **Kruskal's** and **Prim's** are the two standard algorithms that build one.

#### 2. Why It Is Used — Must Know

1. MST problems show up whenever the goal is "connect everything as cheaply as possible" — network cabling, road building, clustering.
2. Kruskal's and Prim's are both greedy (`04-Greedy Algorithms/07`), but build the tree from two different directions — worth knowing both.

#### 3. How It Works — Must Know

```text
Graph edges (node-node: weight): A-B: 4, A-C: 1, B-C: 2, B-D: 1, C-D: 5

Kruskal's (edge by edge, cheapest first, skip if it forms a cycle):
  sort edges: A-C(1), B-D(1), B-C(2), A-B(4), C-D(5)
  add A-C(1)   → no cycle, added
  add B-D(1)   → no cycle, added
  add B-C(2)   → no cycle, added
  add A-B(4)   → would form a cycle (A-C-B-A) → skip
  add C-D(5)   → would form a cycle → skip
  MST edges: A-C, B-D, B-C   total weight = 4

Prim's (grow one tree, always add the cheapest edge leaving it):
  start at A. Tree = {A}
  cheapest edge leaving tree: A-C(1)  → Tree = {A, C}
  cheapest edge leaving tree: B-C(2)  → Tree = {A, C, B}
  cheapest edge leaving tree: B-D(1)  → Tree = {A, C, B, D}
  MST edges: A-C, B-C, B-D   total weight = 4   (same total, different tree shape allowed)
```

1. **Kruskal's** looks at edges globally, sorted by weight, and uses Union-Find (`DS Graph`) to detect and skip cycles.
2. **Prim's** grows one connected tree outward, always picking the cheapest edge that reaches a new, unconnected node.

#### 4. Algorithm — Must Know

```text
Kruskal's:
  sort all edges by weight
  for each edge (u, v), cheapest first:
      if find(u) != find(v):          # doesn't form a cycle
          union(u, v)                  # Union-Find, see DS Graph
          add edge to MST

Prim's:
  pick any start node, add it to the tree
  priority queue of edges leaving the tree, by weight
  while tree doesn't include all nodes:
      pop the cheapest edge (u, v) where u is in the tree, v is not
      add v and that edge to the tree
      push all edges leaving v into the priority queue
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// Kruskal's, using Union-Find (see DS Graph for the full implementation)
fun kruskalMST(n: Int, edges: List<Triple<Int, Int, Int>>): Int {  // (u, v, weight)
    val parent = IntArray(n) { it }
    fun find(x: Int): Int = if (parent[x] == x) x else find(parent[x]).also { parent[x] = it }

    var totalWeight = 0
    for ((u, v, weight) in edges.sortedBy { it.third }) {
        val rootU = find(u)
        val rootV = find(v)
        if (rootU != rootV) {
            parent[rootU] = rootV
            totalWeight += weight
        }
    }
    return totalWeight
}
```

#### 6. Complexity — Must Know

| Algorithm | Complexity | Best for |
|---|---|---|
| Kruskal's | O(E log E) — dominated by sorting edges | Sparse graphs (few edges) |
| Prim's | O(E log V) with a heap | Dense graphs (many edges) |

#### 7. Common Mistakes — Must Know

1. Forgetting the cycle check in Kruskal's — without Union-Find, "add the cheapest edge" alone doesn't guarantee a valid tree.
2. Confusing MST with shortest path (Dijkstra) — MST minimises **total** tree weight; Dijkstra minimises the path to each individual node. They can produce different trees from the same graph.
3. Assuming there's only one correct MST — when edge weights tie, multiple valid MSTs with the same total weight can exist (as shown in the example above).

#### 8. Related Topics

1. `1` Dijkstra's Algorithm — Shortest Path, Non-Negative Weights — the closely related, but different, shortest-path problem
2. `DS Graph` — Union-Find (needed for Kruskal's) and general graph representation
3. `07` Greedy Graph Algorithms (in `04-Greedy Algorithms`) — why both are greedy

#### 9. Interview Must Remember

1. **Kruskal's = sort edges, add if no cycle (Union-Find). Prim's = grow one tree, always add the cheapest edge out.**
2. Kruskal's for sparse graphs, Prim's for dense graphs — say this trade-off if asked to choose.
3. MST ≠ shortest path — don't conflate them with Dijkstra.
