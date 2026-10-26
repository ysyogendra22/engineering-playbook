# Multi-Source BFS

> The queue details and full grid examples are in `01-data-structure/04-Queue/08-Multi-Source BFS.md`. This note is the graph view.

#### 1. What Is It?

Normal BFS starts from **one** node. **Multi-source BFS** starts from **many nodes at the same time**.

Before the loop, put **all the sources in the queue at distance 0**. Then run the usual BFS. Each node is reached first by its **nearest source**, so its distance is the distance to the nearest source.

Why it matters: "distance to the nearest X for every node" would need one BFS per node. Multi-source BFS does it in a single pass: `O(V + E)`.

It fits things that **spread together**: rot, fire, water, infection, a signal.

#### 2. How It Works

```text
Graph (a line):  0 — 1 — 2 — 3 — 4 — 5
Sources: 0 and 5

queue = [0, 5], dist[0] = 0, dist[5] = 0
round 1: from 0 reach 1 (dist 1);  from 5 reach 4 (dist 1)
round 2: from 1 reach 2 (dist 2);  from 4 reach 3 (dist 2)
round 3: 2 and 3 are already reached

dist = [0, 1, 2, 2, 1, 0]       each node knows its distance to the nearest source
```

The code is the normal BFS. Only the **starting queue** is different.

Common questions and what the sources are:

| Question | Sources | Spreads into |
|---|---|---|
| Rotting Oranges | rotten oranges | fresh oranges |
| 01 Matrix | all `0` cells | `1` cells |
| Walls and Gates | all gates | empty rooms |
| As Far from Land as Possible | land cells | water cells |
| Pacific Atlantic Water Flow | each ocean's border cells | higher cells |

Trick: **reverse the thinking**. Instead of "from each cell, find the nearest target", start from the **targets**.

#### 3. Kotlin Code

```kotlin
// Distance from every node to the nearest source
fun nearestSource(graph: List<List<Int>>, sources: List<Int>): IntArray {
    val dist = IntArray(graph.size) { -1 }
    val queue = ArrayDeque<Int>()
    for (s in sources) {                      // every source goes in first, at distance 0
        dist[s] = 0
        queue.addLast(s)
    }
    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        for (next in graph[node]) {
            if (dist[next] == -1) {
                dist[next] = dist[node] + 1
                queue.addLast(next)
            }
        }
    }
    return dist
}

// 01 Matrix (LeetCode 542): distance from each cell to the nearest 0
fun updateMatrix(mat: Array<IntArray>): Array<IntArray> {
    val rows = mat.size
    val cols = mat[0].size
    val dist = Array(rows) { IntArray(cols) { -1 } }
    val queue = ArrayDeque<Int>()
    for (r in 0 until rows) for (c in 0 until cols) {
        if (mat[r][c] == 0) {
            dist[r][c] = 0
            queue.addLast(r * cols + c)
        }
    }
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    while (queue.isNotEmpty()) {
        val id = queue.removeFirst()
        val r = id / cols
        val c = id % cols
        for (d in dirs) {
            val nr = r + d[0]
            val nc = c + d[1]
            if (nr in 0 until rows && nc in 0 until cols && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1
                queue.addLast(nr * cols + nc)
            }
        }
    }
    return dist
}
```

Checks: `nearestSource` on the line graph with sources `[0, 5]` → `[0, 1, 2, 2, 1, 0]`. `updateMatrix([[0,0,0],[0,1,0],[1,1,1]])` → `[[0,0,0],[0,1,0],[1,2,1]]`.

For Rotting Oranges (counting minutes with `repeat(queue.size)`) see the Queue folder, note 08.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Multi-source BFS | `O(V + E)` | `O(V)` |
| Grid `R × C` | `O(R · C)` | `O(R · C)` |
| One BFS from every node | `O(V · (V + E))` | — |

#### 5. Common Mistakes

1. **Running a separate BFS from each source.** Far too slow.
2. **Not marking the sources as visited** when you put them in the queue.
3. **Forgetting unreachable nodes** (they stay `-1`).
4. **Off-by-one in time/minutes.** Count rounds with `repeat(queue.size)` and stop when nothing is left to reach.
5. **No sources at all.** Check this case.

#### 6. Say This in the Interview

1. "Instead of a BFS per node, I put all sources in the queue at distance 0 and run one BFS."
2. "Every node is reached first by its nearest source."
3. "Time `O(V + E)`, space `O(V)`."

#### 7. Quick Check

1. What goes into the queue before the loop starts?
2. What is the distance of a source?

<details>
<summary>Answers</summary>

1. All the sources.
2. `0`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 994 | Rotting Oranges (Medium) | sources = rotten oranges |
| 542 | 01 Matrix (Medium) | sources = zeros |
| 286 | Walls and Gates (Medium, premium) | sources = gates |
| 1162 | As Far from Land as Possible (Medium) | sources = land |
| 1765 | Map of Highest Peak (Medium) | sources = water |
| 934 | Shortest Bridge (Medium) | find one island, then BFS from it |
| 417 | Pacific Atlantic Water Flow (Medium) | search from the borders |
