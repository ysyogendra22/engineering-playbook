# Dijkstra's Algorithm

> The standard answer for the shortest path with different edge costs. Know the code by heart.

#### 1. What Is It?

**Dijkstra's algorithm** finds the **cheapest path** from one start node to every other node in a graph with **non-negative** edge weights.

How it works in one sentence: always take the unfinished node with the **smallest known distance**, then try to improve its neighbours' distances through it. This improvement step is called **relaxation**.

You need a **priority queue** (min-heap) to get "the smallest distance" quickly.

It does **not** work with negative weights (use Bellman-Ford then).

#### 2. How It Works

```text
Graph (weights on edges):
    0 —4— 1
    |     |
    1     2
    |     |
    2 —3— 3        edges: 0-1:4, 0-2:1, 1-3:2, 2-3:3, 1-2:2

Start at 0.  dist = [0, ∞, ∞, ∞]    heap = [(0, node 0)]

pop (0, 0):  try 1: 0+4 = 4 → dist[1] = 4;   try 2: 0+1 = 1 → dist[2] = 1
pop (1, 2):  try 3: 1+3 = 4 → dist[3] = 4;   try 1: 1+2 = 3 < 4 → dist[1] = 3
pop (3, 1):  try 3: 3+2 = 5 > 4 → no change
pop (4, 3):  nothing to improve
pop (4, 1):  stale (4 > dist[1] = 3) → skip

final dist = [0, 3, 1, 4]
```

**Relaxation:** `if (dist[u] + w < dist[v]) { dist[v] = dist[u] + w; push (dist[v], v) }`.

**Stale entries:** a node can be pushed several times with different distances. When you pop an entry whose distance is **bigger than the best known** (`d > dist[u]`), skip it.

Why it fails with negative edges: Dijkstra assumes that once a node is finished, no cheaper path to it can appear. A negative edge can break that.

BFS or Dijkstra? BFS is Dijkstra when all weights are equal.

#### 3. Kotlin Code

```kotlin
import java.util.PriorityQueue

// graph[u] = list of (v, weight). Returns the shortest distance from src to every node.
fun dijkstra(n: Int, graph: List<List<Pair<Int, Int>>>, src: Int): IntArray {
    val INF = Int.MAX_VALUE
    val dist = IntArray(n) { INF }
    dist[src] = 0
    val pq = PriorityQueue<IntArray>(compareBy { it[0] })       // [distance, node]
    pq.add(intArrayOf(0, src))

    while (pq.isNotEmpty()) {
        val (d, u) = pq.poll()
        if (d > dist[u]) continue                                // stale entry → skip
        for ((v, w) in graph[u]) {
            if (d + w < dist[v]) {
                dist[v] = d + w
                pq.add(intArrayOf(dist[v], v))
            }
        }
    }
    return dist                                                  // INF means "unreachable"
}

// Network Delay Time (LeetCode 743): times[i] = [from, to, time], nodes are 1..n
fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
    val graph = List(n + 1) { mutableListOf<Pair<Int, Int>>() }
    for ((from, to, time) in times) graph[from].add(to to time)
    val dist = dijkstra(n + 1, graph, k)
    var longest = 0
    for (node in 1..n) {
        if (dist[node] == Int.MAX_VALUE) return -1               // some node is never reached
        longest = maxOf(longest, dist[node])
    }
    return longest
}

// Path With Minimum Effort (LeetCode 1631): the cost of a path is its biggest height difference
fun minimumEffortPath(heights: Array<IntArray>): Int {
    val rows = heights.size
    val cols = heights[0].size
    val dist = Array(rows) { IntArray(cols) { Int.MAX_VALUE } }
    dist[0][0] = 0
    val pq = PriorityQueue<IntArray>(compareBy { it[0] })        // [effort, row, col]
    pq.add(intArrayOf(0, 0, 0))
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    while (pq.isNotEmpty()) {
        val (effort, r, c) = pq.poll()
        if (effort > dist[r][c]) continue
        if (r == rows - 1 && c == cols - 1) return effort
        for (d in dirs) {
            val nr = r + d[0]
            val nc = c + d[1]
            if (nr !in 0 until rows || nc !in 0 until cols) continue
            val newEffort = maxOf(effort, Math.abs(heights[nr][nc] - heights[r][c]))   // max, not sum
            if (newEffort < dist[nr][nc]) {
                dist[nr][nc] = newEffort
                pq.add(intArrayOf(newEffort, nr, nc))
            }
        }
    }
    return 0
}
```

Checks: the graph in the trace gives `dijkstra` → `[0, 3, 1, 4]`. `networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)` → `2`. `minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])` → `2`.

To rebuild the path, also keep a `parent` array and set `parent[v] = u` when you relax an edge.

#### 4. Complexity

For `V` nodes and `E` edges (binary heap):

| | Time | Space |
|---|---|---|
| Dijkstra | `O((V + E) log V)` | `O(V + E)` |

#### 5. Common Mistakes

1. **Negative edge weights.** Dijkstra may give wrong answers.
2. **No stale-entry check** (`if (d > dist[u]) continue`). It still works but does extra work.
3. **`Int.MAX_VALUE + w`** overflows and becomes negative. The code avoids it by only relaxing from a finished node whose distance is finite.
4. **Using a normal queue** instead of a priority queue. That is not Dijkstra.
5. **Marking visited when you push.** A node can later get a better distance. Update by distance instead.
6. **Summing when the question wants the maximum** along the path (as in Minimum Effort). Use `maxOf`.
7. **Forgetting the unreachable case.**
8. **Node numbering from 1** with arrays that start at 0. Allocate `n + 1`.

#### 6. Say This in the Interview

1. "The edges have different non-negative costs, so BFS is wrong. I use Dijkstra."
2. "I keep a min-heap of (distance, node). I pop the smallest, skip stale entries, and relax the neighbours."
3. "Time `O((V + E) log V)`. If there were negative weights I would use Bellman-Ford."

#### 7. Quick Check

1. What data structure picks the next node?
2. Why skip a popped entry with `d > dist[u]`?

<details>
<summary>Answers</summary>

1. A priority queue (min-heap) ordered by distance.
2. A shorter route to `u` was found after this entry was pushed. This entry is out of date.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 743 | Network Delay Time (Medium) | Dijkstra from `k` |
| 1631 | Path With Minimum Effort (Medium) | Dijkstra with `max` as the path cost |
| 1514 | Path with Maximum Probability (Medium) | Dijkstra on probabilities (maximise) |
| 787 | Cheapest Flights Within K Stops (Medium) | Bellman-Ford or BFS with a stop limit |
| 778 | Swim in Rising Water (Hard) | Dijkstra with `max` |
| 1976 | Number of Ways to Arrive at Destination (Medium) | Dijkstra + count paths |
