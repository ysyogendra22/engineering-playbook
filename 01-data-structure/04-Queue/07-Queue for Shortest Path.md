# Queue for Shortest Path

#### 1. What Is It?

In a graph where **every step costs the same** (an "unweighted" graph), **BFS finds the shortest path**.

The first time BFS reaches a node is the **shortest** way to it. So you store:

- `dist[node]` — the number of steps to reach it (this also marks it visited),
- `parent[node]` — which node you came from (only needed to rebuild the path).

"Minimum number of moves / steps / changes" in a question is very often a shortest-path question. The "node" can be a city, a grid cell, a word, a lock code, or a number.

#### 2. How It Works

```text
Graph:   0 — 1 — 2 — 5
         |        |
         3 ———————4

edges: 0-1, 1-2, 2-5, 0-3, 3-4, 4-2          Shortest path from 0 to 5?

queue [0]                   dist: 0→0
take 0: reach 1, 3          dist: 1→1, 3→1       parent: 1←0, 3←0
take 1: reach 2             dist: 2→2            parent: 2←1
take 3: reach 4             dist: 4→2            parent: 4←3
take 2: reach 5             dist: 5→3            parent: 5←2

Follow parents from 5: 5 ← 2 ← 1 ← 0     path: 0 → 1 → 2 → 5   (3 steps)
```

Why it is correct: the queue handles all nodes at distance `d` before any node at distance `d + 1`. So when a node is first discovered, no shorter way exists.

Which algorithm for which edges:

| Edge costs | Use |
|---|---|
| all equal | **BFS** |
| only 0 or 1 | 0-1 BFS (note 17) |
| different, not negative | Dijkstra (heap) |
| negative possible | Bellman-Ford |

#### 3. Kotlin Code

```kotlin
// Shortest path (list of nodes). Empty list if the target cannot be reached.
fun shortestPath(graph: List<List<Int>>, src: Int, dst: Int): List<Int> {
    val dist = IntArray(graph.size) { -1 }          // -1 means "not reached yet"
    val parent = IntArray(graph.size) { -1 }
    val queue = ArrayDeque<Int>()

    dist[src] = 0
    queue.addLast(src)

    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        if (node == dst) break
        for (next in graph[node]) {
            if (dist[next] == -1) {
                dist[next] = dist[node] + 1
                parent[next] = node
                queue.addLast(next)
            }
        }
    }

    if (dist[dst] == -1) return emptyList()
    val path = mutableListOf<Int>()
    var cur = dst
    while (cur != -1) {
        path.add(cur)
        cur = parent[cur]
    }
    return path.reversed()
}

// When the "nodes" are numbers: fewest operations to turn start into target
// allowed moves: +1, -1, ×2  (a small example of an implicit graph)
fun minOperations(start: Int, target: Int, limit: Int = 10_000): Int {
    val dist = HashMap<Int, Int>()
    val queue = ArrayDeque<Int>()
    dist[start] = 0
    queue.addLast(start)
    while (queue.isNotEmpty()) {
        val x = queue.removeFirst()
        if (x == target) return dist.getValue(x)
        for (next in intArrayOf(x + 1, x - 1, x * 2)) {
            if (next in 0..limit && next !in dist) {
                dist[next] = dist.getValue(x) + 1
                queue.addLast(next)
            }
        }
    }
    return -1
}
```

Checks: on the graph above, `shortestPath(graph, 0, 5)` → `[0, 1, 2, 5]`. `minOperations(2, 7)` → `3` (for example `2 → 3 → 6 → 7`).

#### 4. Complexity

| | Time | Space |
|---|---|---|
| BFS shortest path | `O(V + E)` | `O(V)` |
| Grid with `R × C` cells | `O(R · C)` | `O(R · C)` |

#### 5. Common Mistakes

1. **Using BFS on a weighted graph.** It gives wrong answers. Use Dijkstra.
2. **Marking visited when you take the node out** instead of when you add it.
3. **Forgetting `dist[start] = 0`.**
4. **Start equals target.** The answer is `0` steps.
5. **Target unreachable.** Return `-1` or an empty path. Do not follow `parent` from `-1`.
6. **Forgetting to reverse the path** after following the parents.
7. **Counting nodes instead of edges** (or the reverse). Read the question: "number of steps" vs "number of cells".

#### 6. Say This in the Interview

1. "All moves cost 1, so BFS gives the shortest path. The first time I reach a node is the shortest way."
2. "I keep a `dist` array that is also my visited marker, and a `parent` array to rebuild the path."
3. "Time `O(V + E)`. If the edges had different costs I would use Dijkstra."

#### 7. Quick Check

1. Why is DFS not used to find the shortest path?
2. What is the shortest distance from a node to itself?

<details>
<summary>Answers</summary>

1. DFS follows one long path first. The first path it finds is not necessarily the shortest.
2. `0`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1091 | Shortest Path in Binary Matrix (Medium) | grid BFS (note 09) |
| 127 | Word Ladder (Hard) | words are nodes |
| 752 | Open the Lock (Medium) | lock codes are nodes |
| 433 | Minimum Genetic Mutation (Medium) | like Word Ladder |
| 279 | Perfect Squares (Medium) | numbers are nodes |
| 909 | Snakes and Ladders (Medium) | board squares are nodes |
