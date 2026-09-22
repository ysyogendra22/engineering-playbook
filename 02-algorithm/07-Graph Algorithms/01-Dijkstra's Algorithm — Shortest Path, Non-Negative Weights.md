# Dijkstra's Algorithm — Shortest Path, Non-Negative Weights

#### 1. Definition — Must Know

**Dijkstra's algorithm** finds the shortest path from one source node to every other node in a weighted graph — as long as **no edge weight is negative**.

#### 2. Why It Is Used — Must Know

1. It's the standard answer to "shortest path with weighted edges" — the weighted upgrade from BFS (`DS Graph`), which only handles unweighted graphs.
2. Real systems use it directly: routing, maps, network cost minimisation.

#### 3. How It Works — Must Know

```text
Graph (node: neighbour, weight):
A: (B, 4), (C, 1)
C: (B, 2), (D, 5)
B: (D, 1)

Start at A. distances = {A: 0, B: ∞, C: ∞, D: ∞}

Visit A (dist 0): relax B → 4, relax C → 1
Visit C (dist 1, smallest unvisited): relax B → min(4, 1+2)=3, relax D → 1+5=6
Visit B (dist 3, smallest unvisited): relax D → min(6, 3+1)=4
Visit D (dist 4): done

Final distances: A=0, B=3, C=1, D=4
```

1. Always visit the **unvisited** node with the smallest known distance next (the greedy choice — see `04-Greedy Algorithms/07`).
2. "Relax" an edge means: if going through the current node gives a shorter path to a neighbour, update that neighbour's distance.
3. Once a node is visited, its distance is **final** — never revisited. This is exactly what breaks with negative weights (a later path could still turn out shorter).

#### 4. Algorithm — Must Know

```text
distances = {source: 0, all others: infinity}
priorityQueue = [(0, source)]
while priorityQueue is not empty:
    (dist, node) = priorityQueue.popMin()
    if dist > distances[node]: continue      # stale entry, skip
    for (neighbour, weight) in node's edges:
        newDist = dist + weight
        if newDist < distances[neighbour]:
            distances[neighbour] = newDist
            priorityQueue.push((newDist, neighbour))
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun dijkstra(graph: Map<Int, List<Pair<Int, Int>>>, source: Int, n: Int): IntArray {
    val dist = IntArray(n) { Int.MAX_VALUE }
    dist[source] = 0
    val pq = java.util.PriorityQueue<Pair<Int, Int>>(compareBy { it.second }) // (node, dist)
    pq.add(source to 0)
    while (pq.isNotEmpty()) {
        val (node, d) = pq.poll()
        if (d > dist[node]) continue                        // stale entry
        for ((neighbour, weight) in graph[node].orEmpty()) {
            val newDist = d + weight
            if (newDist < dist[neighbour]) {
                dist[neighbour] = newDist
                pq.add(neighbour to newDist)
            }
        }
    }
    return dist
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| With a binary heap priority queue | O((V + E) log V) |
| With a simple array (no heap) | O(V²) — fine only for dense, small graphs |

#### 7. Common Mistakes — Must Know

1. Using Dijkstra on a graph with **negative edge weights** — it can produce a wrong (too-short) answer, since it never revisits a "finalised" node. Use Bellman-Ford instead (topic 4).
2. Not skipping stale priority queue entries (a node can be pushed multiple times with different distances; only the smallest matters).
3. Confusing this with BFS — Dijkstra is needed only when edges have **different, non-negative weights**; plain BFS already solves the unweighted case in O(V + E).

#### 8. Related Topics

1. `3` Choosing the Right Algorithm for the Weights You Have — when to reach for Dijkstra vs the alternatives
2. `4` Bellman-Ford — Handles Negative Weights, Detects Negative Cycles — the fix when weights can be negative
3. `DS Graph` — BFS, the unweighted-graph equivalent
4. `07` Greedy Graph Algorithms (in `04-Greedy Algorithms`) — why this algorithm is classified as greedy

#### 9. Interview Must Remember

1. Dijkstra = **BFS with a priority queue instead of a plain queue**, for weighted graphs.
2. Works **only with non-negative weights** — always mention this limitation.
3. O((V + E) log V) with a heap — know this number cold.
