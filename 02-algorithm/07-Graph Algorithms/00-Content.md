# Graph Algorithms

Algorithm topic `7` in `02-algorithm`. Traversal, representation, cycle detection, topological sort, and Union-Find already live in `DS Graph`. This is the shortest-path and spanning-tree layer on top.

## Index

| # | Sub-topic | Mark |
|---|---|---|
| 1 | Dijkstra's Algorithm — Shortest Path, Non-Negative Weights | 🟢 |
| 2 | Kruskal's & Prim's Algorithms — Minimum Spanning Tree | 🟢 |
| 3 | Choosing the Right Algorithm for the Weights You Have | 🟢 |
| 4 | Bellman-Ford — Handles Negative Weights, Detects Negative Cycles | 🟡 |
| 5 | Floyd-Warshall — All-Pairs Shortest Path | 🟡 |
| 6 | A* Search — Dijkstra Plus a Heuristic | 🟡 |
| 7 | Network Flow (Max Flow / Min Cut) — Name & Problem Shape Only | ⚪ |

**Complexity quick reference**

| Algorithm | Complexity | Negative weights | Use for |
|---|---|---|---|
| BFS | O(V + E) | n/a (unweighted) | Shortest path, unweighted graph |
| Dijkstra | O((V + E) log V) | No | Shortest path, non-negative weights |
| Bellman-Ford | O(V · E) | Yes, detects negative cycles | Shortest path with negative weights |
| Floyd-Warshall | O(V³) | Yes | All-pairs shortest path, small graphs |
| Kruskal | O(E log E) | n/a | Minimum spanning tree, sparse graph |
| Prim | O(E log V) | n/a | Minimum spanning tree, dense graph |

**Related:** `DS Graph` (traversal, representation, cycle detection, Union-Find) · `4` Greedy Algorithms (Dijkstra, Kruskal, and Prim are all greedy) · `LC 12`, `LC 13`, `LC 15`, `LC 16`, `LC 17` Graph traversal patterns and problems
