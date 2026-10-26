# Shortest Path in Unweighted Graph — BFS

> "Minimum number of steps" almost always means BFS. The queue details are also in `01-data-structure/04-Queue/07-Queue for Shortest Path.md`.

#### 1. What Is It?

In a graph where **every edge costs the same** (an unweighted graph), **BFS finds the shortest path**.

The first time BFS reaches a node is the shortest way to it. So you store:

- `dist[node]`: the number of edges from the start. It also marks the node as visited.
- `parent[node]`: where you came from. It lets you rebuild the path.

The "node" can be a city, a grid cell, a word, a lock code or a number. Questions say "minimum number of moves / steps / changes".

#### 2. How It Works

```text
Graph:   0 — 1 — 2 — 5          edges: 0-1, 1-2, 2-5, 0-3, 3-4, 4-2
         |        |
         3 ———————4

Shortest path from 0 to 5?

queue [0]                dist 0→0
take 0: reach 1, 3       dist 1→1, 3→1       parent 1←0, 3←0
take 1: reach 2          dist 2→2            parent 2←1
take 3: reach 4          dist 4→2            parent 4←3
take 2: reach 5          dist 5→3            parent 5←2

Follow the parents back from 5:  5 ← 2 ← 1 ← 0     path 0 → 1 → 2 → 5   (3 edges)
```

Why BFS is correct: the queue finishes all nodes at distance `d` before any node at distance `d + 1`. So the first arrival is the shortest.

If the edges have **different costs**, BFS is wrong. Use Dijkstra (note 18).

#### 3. Kotlin Code

```kotlin
// Shortest path as a list of nodes. Empty list if the target cannot be reached.
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

// Shortest Path with Alternating Colors (LeetCode 1129): the state is (node, colour of the last edge)
fun shortestAlternatingPaths(n: Int, redEdges: Array<IntArray>, blueEdges: Array<IntArray>): IntArray {
    val graph = Array(2) { List(n) { mutableListOf<Int>() } }       // 0 = red, 1 = blue
    for ((a, b) in redEdges) graph[0][a].add(b)
    for ((a, b) in blueEdges) graph[1][a].add(b)

    val answer = IntArray(n) { -1 }
    val visited = Array(2) { BooleanArray(n) }
    val queue = ArrayDeque<IntArray>()                               // [node, colour of the last edge]
    queue.addLast(intArrayOf(0, 0)); queue.addLast(intArrayOf(0, 1))
    visited[0][0] = true; visited[1][0] = true
    var steps = 0
    while (queue.isNotEmpty()) {
        repeat(queue.size) {
            val (node, colour) = queue.removeFirst()
            if (answer[node] == -1) answer[node] = steps
            val nextColour = 1 - colour                              // the next edge must have the other colour
            for (next in graph[nextColour][node]) {
                if (!visited[nextColour][next]) {
                    visited[nextColour][next] = true
                    queue.addLast(intArrayOf(next, nextColour))
                }
            }
        }
        steps++
    }
    return answer
}
```

Check: on the graph above, `shortestPath(graph, 0, 5)` → `[0, 1, 2, 5]`.

The grid version (Shortest Path in Binary Matrix) is in `01-data-structure/04-Queue/09-Grid BFS.md`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| BFS shortest path | `O(V + E)` | `O(V)` |
| Grid `R × C` | `O(R · C)` | `O(R · C)` |

#### 5. Common Mistakes

1. **Using BFS on a weighted graph.**
2. **Marking visited when taking the node out** instead of when adding it.
3. **Forgetting `dist[start] = 0`.**
4. **Unreachable target.** Return `-1` or an empty path. Do not follow `parent` from `-1`.
5. **Forgetting to reverse** the path.
6. **Counting nodes instead of edges** (or the reverse).
7. **Forgetting extra state.** If a rule depends on more than the node (like the last colour), put it in the BFS state.

#### 6. Say This in the Interview

1. "Every move costs 1, so BFS gives the shortest path. The first time I reach a node is the shortest way."
2. "I keep a `dist` array as my visited marker and a `parent` array to rebuild the path."
3. "Time `O(V + E)`. With different costs I would use Dijkstra."

#### 7. Quick Check

1. What is the BFS distance of the start node?
2. Why is the first arrival the shortest?

<details>
<summary>Answers</summary>

1. `0`.
2. BFS handles all nodes at distance `d` before any at `d + 1`, so no shorter way can appear later.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1091 | Shortest Path in Binary Matrix (Medium) | grid BFS |
| 127 | Word Ladder (Hard) | words are nodes |
| 752 | Open the Lock (Medium) | lock codes are nodes |
| 433 | Minimum Genetic Mutation (Medium) | like Word Ladder |
| 1129 | Shortest Path with Alternating Colors (Medium) | state = node + last colour |
| 909 | Snakes and Ladders (Medium) | board squares are nodes |
| 279 | Perfect Squares (Medium) | numbers are nodes |
