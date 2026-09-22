# Bellman-Ford — Handles Negative Weights, Detects Negative Cycles

#### 1. Definition — Must Know

**Bellman-Ford** finds the shortest path from one source to every other node, and unlike Dijkstra's, it works correctly even when some edge weights are **negative**. It can also detect if the graph contains a **negative cycle** (a loop whose total weight is negative, which makes "shortest path" undefined — you could loop forever, getting cheaper each time).

#### 2. Why It Is Used — Must Know

1. It's the direct answer whenever a graph problem mentions negative weights or costs (which can represent things like refunds, discounts, or gains, not just costs).
2. The negative-cycle detection is itself a common, separate interview question: "can arbitrage exist in this currency exchange graph?" is a classic dressed-up version of it.

#### 3. How It Works — Must Know

```text
Instead of greedily finalising the closest node first (Dijkstra's approach,
which breaks with negative weights), Bellman-Ford simply relaxes EVERY edge,
repeatedly, V-1 times:

for i in 1 to V-1:
    for each edge (u, v, weight):
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight

Why V-1 times? The shortest path between any two nodes uses at most V-1
edges (it can't revisit a node without that being wasteful), so after
V-1 full passes, every shortest path has definitely been found.

Negative cycle check — do ONE more pass:
    if any edge can still be relaxed after V-1 passes,
    a negative cycle exists (the "shortest path" keeps getting shorter forever).
```

#### 4. Algorithm — Must Know

```text
dist = {source: 0, all others: infinity}
repeat (V - 1) times:
    for each edge (u, v, weight):
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight

# one extra pass to check for negative cycles
for each edge (u, v, weight):
    if dist[u] + weight < dist[v]:
        report "negative cycle detected"
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun bellmanFord(n: Int, edges: List<Triple<Int, Int, Int>>, source: Int): IntArray? {
    val dist = IntArray(n) { Int.MAX_VALUE }
    dist[source] = 0

    repeat(n - 1) {
        for ((u, v, weight) in edges) {
            if (dist[u] != Int.MAX_VALUE && dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight
            }
        }
    }

    for ((u, v, weight) in edges) {   // one more pass — negative cycle check
        if (dist[u] != Int.MAX_VALUE && dist[u] + weight < dist[v]) {
            return null   // negative cycle detected
        }
    }
    return dist
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Time | O(V · E) — V-1 passes, each checking every edge |
| Space | O(V) |

Notably slower than Dijkstra's O((V + E) log V) — this is the cost of correctly handling negative weights.

#### 7. Common Mistakes — Must Know

1. Running only V-1 passes and forgetting the extra pass needed to actually **detect** a negative cycle.
2. Trying to skip straight to Dijkstra "for speed" on a graph that might have negative weights — check first, since Dijkstra silently gives a wrong answer instead of erroring.
3. Not guarding against overflow when `dist[u]` is still infinity — adding `weight` to `Int.MAX_VALUE` can wrap around; always check `dist[u] != infinity` before relaxing.

#### 8. Related Topics

1. `1` Dijkstra's Algorithm — Shortest Path, Non-Negative Weights — the faster algorithm to use when weights are all non-negative
2. `3` Choosing the Right Algorithm for the Weights You Have — the decision table this fits into
3. `5` Floyd-Warshall — All-Pairs Shortest Path — also handles negative weights, for the all-pairs case

#### 9. Interview Must Remember

1. Bellman-Ford = **relax every edge, V-1 times** — simple, and correct even with negative weights.
2. One extra pass after that detects a **negative cycle**.
3. O(V · E) — slower than Dijkstra, and that's the trade-off for handling negative weights correctly.
