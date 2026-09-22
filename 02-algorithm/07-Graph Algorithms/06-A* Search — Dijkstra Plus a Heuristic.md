# A* Search — Dijkstra Plus a Heuristic

#### 1. Definition — Must Know

**A\* (A-star) search** finds the shortest path to one specific target node, like Dijkstra's, but uses an extra piece of information — a **heuristic**, a guess at how far the remaining distance to the target is — to explore more promising nodes first.

#### 2. Why It Is Used — Must Know

1. When you have a genuinely useful heuristic (like straight-line distance on a map, which is always ≤ the real road distance), A* reaches the target much faster than Dijkstra's in practice, by not wasting time exploring nodes that are clearly heading the wrong way.
2. It's the algorithm behind most real pathfinding — game AI, GPS navigation, robotics.

#### 3. How It Works — Must Know

```text
Dijkstra's picks the next node to explore by:
    priority = distance so far (g)

A* picks the next node to explore by:
    priority = distance so far (g) + estimated remaining distance (h)
             = f(node) = g(node) + h(node)

The heuristic h(node) must never OVERESTIMATE the true remaining distance
(this property is called "admissible") — otherwise A* can give a wrong,
non-shortest answer.

Example: on a 2D grid map, h(node) = straight-line distance from node to
the target. This is always ≤ the real path distance (you can't walk in a
straighter line than straight), so it's a safe, admissible heuristic.
```

1. A* explores nodes that *look* closer to the target first, instead of exploring purely by distance-from-start like Dijkstra's.
2. If `h(node) = 0` for every node, A* becomes exactly Dijkstra's — Dijkstra's is really A* with no heuristic information at all.

#### 4. Algorithm — Must Know

```text
g = {source: 0, all others: infinity}     # real distance so far
priorityQueue = [(g[source] + h(source), source)]

while priorityQueue is not empty:
    (_, node) = priorityQueue.popMin()   # smallest f = g + h
    if node == target: return g[node]
    for (neighbour, weight) in node's edges:
        newG = g[node] + weight
        if newG < g[neighbour]:
            g[neighbour] = newG
            priorityQueue.push((newG + h(neighbour), neighbour))
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun aStar(
    graph: Map<Int, List<Pair<Int, Int>>>, source: Int, target: Int, n: Int,
    heuristic: (Int) -> Int   // estimated remaining distance to target
): Int {
    val g = IntArray(n) { Int.MAX_VALUE }
    g[source] = 0
    val pq = java.util.PriorityQueue<Pair<Int, Int>>(compareBy { it.second }) // (node, f = g + h)
    pq.add(source to heuristic(source))
    while (pq.isNotEmpty()) {
        val (node, _) = pq.poll()
        if (node == target) return g[node]
        for ((neighbour, weight) in graph[node].orEmpty()) {
            val newG = g[node] + weight
            if (newG < g[neighbour]) {
                g[neighbour] = newG
                pq.add(neighbour to newG + heuristic(neighbour))
            }
        }
    }
    return -1   // target unreachable
}
```

#### 6. Complexity — Must Know

| | Worst case | Typical case with a good heuristic |
|---|---|---|
| A* | Same as Dijkstra's, O((V + E) log V) | Often visits far fewer nodes in practice |

The worst-case Big-O doesn't improve over Dijkstra's — the real-world speed-up comes from exploring fewer nodes, which isn't captured by Big-O alone.

#### 7. Common Mistakes — Must Know

1. Using a heuristic that can **overestimate** the true remaining distance — this breaks correctness and can give a path that isn't actually shortest.
2. Reaching for A* when there's no useful heuristic available, or when you need distances to *every* node, not just one target — Dijkstra's is the simpler, equally correct choice there.
3. Forgetting that A* is only worth the extra complexity when the heuristic is genuinely informative — a poor heuristic gives little to no speed-up over plain Dijkstra's.

#### 8. Related Topics

1. `1` Dijkstra's Algorithm — Shortest Path, Non-Negative Weights — A* generalises this directly
2. `3` Choosing the Right Algorithm for the Weights You Have

#### 9. Interview Must Remember

1. A* = **Dijkstra's, but the priority queue orders by `distance so far + estimated remaining distance`.**
2. The heuristic must **never overestimate** the true remaining distance, or the result can be wrong.
3. Use it when you have one specific target and a genuinely useful heuristic (like straight-line distance) — otherwise, plain Dijkstra's is simpler and just as correct.
