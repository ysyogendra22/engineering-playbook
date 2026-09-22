# Floyd-Warshall — All-Pairs Shortest Path

#### 1. Definition — Must Know

**Floyd-Warshall** computes the shortest path between **every pair** of nodes in a graph, all at once, in a single algorithm — instead of running a single-source algorithm (like Dijkstra's) once per node.

#### 2. Why It Is Used — Must Know

1. When the question is "what's the shortest distance between *any two* nodes", running Dijkstra's from every single node (V times) is more complex to reason about than one clean Floyd-Warshall pass.
2. It's short to write — three nested loops — which makes it a fast, low-risk choice for small graphs in an interview.

#### 3. How It Works — Must Know

```text
The core idea: for every pair (i, j), check if going THROUGH some
intermediate node k gives a shorter path than the current best.

dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

Try this for every possible k, one at a time, updating dist as you go.
After considering all nodes as possible "waypoints", dist[i][j] holds
the true shortest path from i to j.
```

```text
Initial distances (direct edges only, infinity if no direct edge):
      A    B    C
A  [  0,   4,   ∞ ]
B  [  ∞,   0,   2 ]
C  [  1,   ∞,   0 ]

Consider A as a waypoint: does A→...→A→...→ help anyone? (usually not, skip trivial cases)
Consider B as a waypoint: dist[A][C] = min(∞, dist[A][B] + dist[B][C]) = min(∞, 4+2) = 6
Consider C as a waypoint: dist[B][A] = min(∞, dist[B][C] + dist[C][A]) = min(∞, 2+1) = 3
                          dist[A][A] stays 0, but now check A→C→A type improvements, etc.

Final: dist[A][C] = 6 (via B), and other pairs updated similarly.
```

#### 4. Algorithm — Must Know

```text
dist = the direct-edge distance matrix (infinity where there's no direct edge, 0 on the diagonal)

for k in all nodes:               # try every node as a possible waypoint
    for i in all nodes:
        for j in all nodes:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

The order of the loops matters: `k` **must** be the outermost loop — it represents "having now considered node k as a possible waypoint for every pair".

#### 5. Kotlin Implementation — Must Know

```kotlin
fun floydWarshall(n: Int, dist: Array<IntArray>): Array<IntArray> {
    val INF = Int.MAX_VALUE / 2   // avoid overflow when adding two "infinities"
    for (k in 0 until n) {
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j]
                }
            }
        }
    }
    return dist
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Time | O(V³) |
| Space | O(V²) — the full distance matrix |

O(V³) sounds worse than running Dijkstra V times (O(V × (V+E) log V)), and for sparse graphs it usually is — Floyd-Warshall is best suited to **small or dense** graphs where its simplicity outweighs the raw complexity.

#### 7. Common Mistakes — Must Know

1. Putting `k` in the innermost loop instead of the outermost — this silently gives a wrong (or incomplete) answer, since it changes what "already considered" means at each step.
2. Using `Int.MAX_VALUE` directly for "infinity" and then adding two of them together — this overflows. Use a large-but-safe placeholder like `Int.MAX_VALUE / 2` instead.
3. Reaching for Floyd-Warshall for a **single-source** shortest path question — that's Dijkstra's or Bellman-Ford's job, and Floyd-Warshall does far more work than needed.

#### 8. Related Topics

1. `1` Dijkstra's Algorithm — Shortest Path, Non-Negative Weights — the single-source equivalent
2. `4` Bellman-Ford — Handles Negative Weights, Detects Negative Cycles — also handles negative weights, single-source
3. `3` Choosing the Right Algorithm for the Weights You Have

#### 9. Interview Must Remember

1. Floyd-Warshall = **for every possible waypoint k, try improving every pair (i, j) by routing through k.**
2. **`k` must be the outermost loop** — this is the one detail people get wrong from memory.
3. O(V³) time, O(V²) space — best for small or dense graphs needing all-pairs distances, not for single-source questions.
