# Choosing the Right Algorithm for the Weights You Have

#### 1. Definition — Must Know

A short decision guide: which shortest-path (or spanning-tree) algorithm to reach for, based entirely on what the edge weights look like.

#### 2. Why It Is Used — Must Know

Graph algorithm questions are often really "do you know which tool fits which weight situation?" — this is the single table that answers that, fast.

#### 3. How It Works — Must Know

```text
No weights at all (just "connected" or "reachable")?
    → BFS  (DS Graph)                              O(V + E)

Weights, but all non-negative?
    → Dijkstra's                                   O((V + E) log V)

Weights, and some could be NEGATIVE?
    → Bellman-Ford                                 O(V · E)

Need shortest path between EVERY pair of nodes, small graph?
    → Floyd-Warshall                               O(V³)

Need to connect ALL nodes as cheaply as possible (not point-to-point)?
    → Kruskal's or Prim's (Minimum Spanning Tree)  O(E log E) / O(E log V)

Have a good guess ("heuristic") for remaining distance to a specific target?
    → A* Search                                    Same worst case as Dijkstra, often faster in practice
```

#### 4. Algorithm — Must Know

```text
Ask, in order:
1. Are there weights at all?                    no → BFS
2. Could any weight be negative?                yes → Bellman-Ford
3. Do I need ALL-pairs shortest paths?           yes → Floyd-Warshall
4. Is the goal "connect everything cheaply", not "shortest path to one node"?
                                                  yes → Kruskal's / Prim's
5. Otherwise, and I have a good heuristic to one target → A*
6. Otherwise → Dijkstra's
```

#### 5. Kotlin Implementation — Must Know

*(This topic is a decision process — see the individual algorithm topics for their implementations.)*

#### 6. Complexity — Must Know

| Algorithm | Complexity | Negative weights? |
|---|---|---|
| BFS | O(V + E) | n/a (unweighted) |
| Dijkstra | O((V + E) log V) | No |
| Bellman-Ford | O(V · E) | Yes, and detects negative cycles |
| Floyd-Warshall | O(V³) | Yes |
| Kruskal | O(E log E) | n/a (MST, not shortest path) |
| Prim | O(E log V) | n/a (MST, not shortest path) |

#### 7. Common Mistakes — Must Know

1. Reaching for Dijkstra by default without checking whether negative weights are possible in the problem.
2. Using Floyd-Warshall (O(V³)) when only a single source's shortest paths are needed — Dijkstra or Bellman-Ford is a far better fit.
3. Confusing "shortest path" problems (point A to point B, or point A to everywhere) with "minimum spanning tree" problems (connect every node together as cheaply as possible) — they sound similar but solve different questions.

#### 8. Related Topics

1. `1` Dijkstra's Algorithm — Shortest Path, Non-Negative Weights
2. `4` Bellman-Ford — Handles Negative Weights, Detects Negative Cycles
3. `5` Floyd-Warshall — All-Pairs Shortest Path
4. `2` Kruskal's & Prim's Algorithms — Minimum Spanning Tree
5. `DS Graph` — BFS for the unweighted case

#### 9. Interview Must Remember

1. **Negative weights possible? → Bellman-Ford. All-pairs? → Floyd-Warshall. Connect everything cheaply? → MST (Kruskal/Prim). Otherwise → Dijkstra.**
2. Say your reasoning out loud, not just the algorithm name — "I'll use Dijkstra since all weights are non-negative and I only need distances from one source."
3. When unsure, ask the interviewer directly: "can any edge weight be negative?" — it's a fair, expected clarifying question.
