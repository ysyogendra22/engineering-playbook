# Greedy Graph Algorithms — Dijkstra, Kruskal, Prim

#### 1. Definition — Must Know

1. Three of the most important graph algorithms are, at their core, greedy: **Dijkstra's** (shortest path), **Kruskal's** and **Prim's** (minimum spanning tree).
2. Each repeatedly picks the "cheapest available next step" and never revisits that choice.

#### 2. Why It Is Used — Must Know

1. Knowing that these are greedy connects this whole topic family together — the same "sort or pick the cheapest option" idea scales up to real, widely-used graph algorithms.
2. Full detail on each lives in this folder's Graph Algorithms topic (7); this page is the "why is this greedy?" summary.

#### 3. How It Works — Must Know

```text
Dijkstra:  repeatedly pick the unvisited node with the smallest known distance,
           and "lock in" that distance as final — never reconsidered.

Kruskal:   sort all edges by weight, ascending. Repeatedly add the cheapest edge
           that doesn't create a cycle (checked with Union-Find).

Prim:      start from any node. Repeatedly add the cheapest edge that connects
           the growing tree to a new node.
```

1. All three make a **locally cheapest** choice at each step.
2. All three never undo a choice — once a node's shortest distance is finalised (Dijkstra), or an edge is added to the tree (Kruskal, Prim), it's locked in.

#### 4. Algorithm — Must Know

*(Shown here at the level of "why is this the same shape as other greedy algorithms" — the full algorithms are in Graph Algorithms, topic 7.)*

```text
Dijkstra:
  priority queue of (distance, node), starting with (0, source)
  while queue not empty:
      pick the node with smallest distance (the greedy choice)
      finalise its distance
      relax its neighbours' distances

Kruskal:
  sort edges by weight
  for each edge, smallest first:
      if it doesn't form a cycle (Union-Find check): add it (the greedy choice)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// Kruskal's greedy step — the shape, not the full algorithm (see Graph Algorithms, topic 7)
fun kruskalGreedyStep(edges: List<Triple<Int, Int, Int>>): List<Triple<Int, Int, Int>> {
    val sorted = edges.sortedBy { it.third }   // sort by weight — the greedy setup
    val mst = mutableListOf<Triple<Int, Int, Int>>()
    // for each edge in `sorted`, add it if it doesn't create a cycle (Union-Find, topic 7 in `01-data-structure/10-Graph`)
    return mst
}
```

#### 6. Complexity — Must Know

| Algorithm | Complexity | Greedy step |
|---|---|---|
| Dijkstra | O((V + E) log V) | pick smallest known distance |
| Kruskal | O(E log E) | pick smallest edge, skip if it forms a cycle |
| Prim | O(E log V) | pick smallest edge that grows the tree |

#### 7. Common Mistakes — Must Know

1. Using Dijkstra on a graph with **negative edge weights** — the greedy "lock in the smallest distance" step breaks, because a longer path found later could still turn out cheaper. Use Bellman-Ford instead (Graph Algorithms, topic 7).
2. Forgetting that Kruskal needs a cycle check (Union-Find) — without it, "add the cheapest edge" alone doesn't build a valid tree.
3. Treating these as unrelated named algorithms to memorise separately, instead of recognising the shared greedy shape.

#### 8. Related Topics

1. `7` Graph Algorithms (its own folder) — the full algorithms, complexity table, and when to use each
2. `1` The Greedy Choice Property — why these work (non-negative weights, no cycles)
3. `DS Graph` — traversal and Union-Find, which Kruskal depends on

#### 9. Interview Must Remember

1. Dijkstra, Kruskal, and Prim are all **greedy** — say this when asked to classify them.
2. Dijkstra's greedy step only works with **non-negative** weights — always mention this limitation.
3. Kruskal's greedy step needs a **cycle check** (Union-Find) to actually build a valid tree, not just "add cheap edges".
