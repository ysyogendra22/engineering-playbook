# Graph Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–34.

#### 1. Key Takeaways

1. A graph is **vertices + edges**. In code, store it as an **adjacency list**: `V + E` memory.
2. **BFS** (queue) = fewest steps when every step costs the same. **DFS** (recursion or stack) = components, cycles, all paths.
3. Always use a **`visited`** set, and mark a node visited when you **add it to the queue** (BFS).
4. A single search covers **one component**. Loop over **all** nodes to cover a disconnected graph.
5. Ask first: is the graph **directed**? **weighted**? Can it have **cycles**, **self-loops**, **duplicate edges**?
6. A **grid** is a graph you do not build: use a direction array, check bounds first.
7. Different edge costs → **Dijkstra**. Order with prerequisites → **topological sort**. "Are these connected?" as edges arrive → **Union-Find**.

#### 2. Representations

| Way | Memory | Edge `a-b`? | Use when |
|---|---|---|---|
| **Adjacency list** | `O(V + E)` | `O(degree)` | almost always (sparse graphs) |
| Adjacency matrix | `O(V²)` | `O(1)` | small or dense graph, input already a matrix |
| Edge list | `O(E)` | `O(E)` | Kruskal (needs sorting), input as pairs |

```kotlin
val graph = List(n) { mutableListOf<Int>() }
for ((a, b) in edges) { graph[a].add(b); graph[b].add(a) }     // undirected: add both ways
```

#### 3. Algorithms and Complexity

| Algorithm | Use for | Time | Space |
|---|---|---|---|
| BFS | fewest steps, levels | `O(V + E)` | `O(V)` |
| DFS | components, cycles, all paths | `O(V + E)` | `O(V)` |
| Connected components | count groups | `O(V + E)` | `O(V)` |
| Cycle check, undirected | DFS with parent / Union-Find | `O(V + E)` | `O(V)` |
| Cycle check, directed | 3-state DFS / Kahn | `O(V + E)` | `O(V)` |
| Topological sort (DFS or Kahn) | order with prerequisites | `O(V + E)` | `O(V)` |
| Bipartite check | 2-colouring | `O(V + E)` | `O(V)` |
| 0-1 BFS | edge costs 0 or 1 | `O(V + E)` | `O(V)` |
| **Dijkstra** | different costs, no negatives | `O((V + E) log V)` | `O(V)` |
| Bellman-Ford | negative costs, stop limits | `O(V · E)` | `O(V)` |
| Floyd-Warshall | all pairs | `O(V³)` | `O(V²)` |
| Union-Find | merge / same group? | `O(α(V))` per op | `O(V)` |
| Kruskal (MST) | sort edges + Union-Find | `O(E log E)` | `O(V)` |
| Prim (MST) | grow one tree with a heap | `O(E log V)` | `O(V)` |
| Grid with `R × C` cells | any of the above | `O(R · C)` | `O(R · C)` |

#### 4. Patterns and How to Identify Them

| Signal in the question | Pattern | Note | Example |
|---|---|---|---|
| "connections", "friends", "provinces", "islands" | connected components | 10, 11 | Number of Provinces |
| grid of cells, up/down/left/right | grid as graph (BFS/DFS) | 11, 12 | Number of Islands |
| "fewest moves/steps", equal costs | BFS shortest path | 9, 17 | Shortest Path in Binary Matrix |
| rot / fire / water spreading | multi-source BFS | 21 | Rotting Oranges |
| words, lock codes, boards you change step by step | implicit graph + BFS | 30 | Word Ladder |
| "cheapest", "minimum time", different costs | Dijkstra | 18 | Network Delay Time |
| prerequisites, dependencies, build order | topological sort / Kahn | 15, 16, 31 | Course Schedule II |
| "is there a cycle?" (directed) | 3-state DFS or Kahn | 14 | Course Schedule |
| "does this edge make a cycle?" / "same group?" | Union-Find | 23 | Redundant Connection |
| "split into two groups" | bipartite 2-colouring | 22 | Is Graph Bipartite? |
| "connect everything at the lowest cost" | MST (Kruskal / Prim) | 26–28 | Min Cost to Connect All Points |
| "copy the graph" | map original → clone | 29 | Clone Graph |
| ratios / weighted relations | weighted DFS | 33 | Evaluate Division |
| longest path / earliest time with prerequisites | DP in topological order | 34 | Parallel Courses III |
| in-degree / out-degree counts | degree counting | 32 | Find the Town Judge |

#### 5. Templates to Memorise

**BFS (shortest steps)**

```kotlin
val dist = IntArray(n) { -1 }
val queue = ArrayDeque<Int>()
dist[start] = 0
queue.addLast(start)
while (queue.isNotEmpty()) {
    val node = queue.removeFirst()
    for (next in graph[node]) {
        if (dist[next] == -1) {                  // dist doubles as visited
            dist[next] = dist[node] + 1
            queue.addLast(next)
        }
    }
}
```

**DFS (components)**

```kotlin
fun dfs(node: Int) {
    visited[node] = true
    for (next in graph[node]) if (!visited[next]) dfs(next)
}
for (s in 0 until n) if (!visited[s]) { components++; dfs(s) }
```

**Grid neighbours**

```kotlin
val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
for (d in dirs) {
    val nr = r + d[0]; val nc = c + d[1]
    if (nr !in 0 until rows || nc !in 0 until cols) continue      // bounds FIRST
    // check the cell, then visited
}
```

**Kahn (topological order / cycle)**

```kotlin
val indegree = IntArray(n)
for (u in 0 until n) for (v in graph[u]) indegree[v]++
val queue = ArrayDeque<Int>()
for (u in 0 until n) if (indegree[u] == 0) queue.addLast(u)
val order = mutableListOf<Int>()
while (queue.isNotEmpty()) {
    val u = queue.removeFirst(); order.add(u)
    for (v in graph[u]) if (--indegree[v] == 0) queue.addLast(v)
}
// order.size < n → there is a cycle
```

**Dijkstra**

```kotlin
val dist = IntArray(n) { Int.MAX_VALUE }
dist[src] = 0
val pq = PriorityQueue<IntArray>(compareBy { it[0] })          // [distance, node]
pq.add(intArrayOf(0, src))
while (pq.isNotEmpty()) {
    val (d, u) = pq.poll()
    if (d > dist[u]) continue                                   // stale entry
    for ((v, w) in graph[u]) if (d + w < dist[v]) { dist[v] = d + w; pq.add(intArrayOf(dist[v], v)) }
}
```

**Union-Find**

```kotlin
val parent = IntArray(n) { it }
fun find(x: Int): Int { if (parent[x] != x) parent[x] = find(parent[x]); return parent[x] }
fun union(a: Int, b: Int): Boolean { val ra = find(a); val rb = find(b); if (ra == rb) return false; parent[ra] = rb; return true }
```

#### 6. Brute Force to Optimized

| Problem | Brute force | Optimized |
|---|---|---|
| Shortest path (equal steps) | try every path (exponential) | BFS: `O(V + E)` |
| Cheapest path | try every path | Dijkstra: `O((V + E) log V)` |
| Course order | try every ordering (`V!`) | Kahn: `O(V + E)` |
| Distance to the nearest source for every cell | BFS from each cell: `O((R·C)²)` | one multi-source BFS: `O(R·C)` |
| Are two nodes connected, many queries | DFS each time: `O(V + E)` per query | Union-Find: almost `O(1)` |
| Minimum spanning tree | try every spanning tree | Kruskal / Prim |
| Word Ladder | one-sided BFS: `O(b^d)` | bidirectional BFS: `O(b^(d/2))` |

#### 7. Common Mistakes and Edge Cases

1. No `visited` set → infinite loop on a cycle.
2. Marking visited when **taking** a node out of the BFS queue → duplicates, slow.
3. Forgetting the reverse edge (undirected) or adding it (directed).
4. Wrong direction from `[course, prerequisite]` → the edge is `prerequisite → course`.
5. Using BFS on a weighted graph, or Dijkstra with negative weights.
6. Checking only one component of a disconnected graph.
7. Undirected cycle check: treating the **parent** as a cycle. Directed cycle check: using the parent trick (use 3 states).
8. Grid: bounds read after the cell; `rows` and `cols` mixed in `r * cols + c`.
9. `Int.MAX_VALUE + w` overflow. Nodes numbered from 1.
10. Test: empty graph, one node, no edges, start equals target, unreachable target, cycle, disconnected graph.

#### 8. What to Say Out Loud

1. "I model this as a graph: the nodes are ... and the edges are ... Is it directed or weighted?"
2. "I need the fewest steps with equal costs, so BFS with a visited set. Time `O(V + E)`."
3. "Edge cases: empty input, disconnected graph, cycles, and an unreachable target."

#### 9. Practice Order

| Level | Question | Idea |
|---|---|---|
| Easy | [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | BFS / DFS |
| Easy | [Flood Fill](https://leetcode.com/problems/flood-fill/) | grid DFS |
| Easy | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | in-degree and out-degree |
| Medium | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | grid components |
| Medium | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | component size |
| Medium | [Clone Graph](https://leetcode.com/problems/clone-graph/) | map original → clone |
| Medium | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | components / Union-Find |
| Medium | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | multi-source BFS |
| Medium | [01 Matrix](https://leetcode.com/problems/01-matrix/) | multi-source BFS |
| Medium | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | grid BFS |
| Medium | [Course Schedule](https://leetcode.com/problems/course-schedule/) | directed cycle |
| Medium | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | topological order |
| Medium | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | 2-colouring |
| Medium | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Union-Find |
| Medium | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Dijkstra |
| Medium | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | weighted DFS |
| Medium | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | search from the borders |
| Medium | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | MST |
| Hard | [Word Ladder](https://leetcode.com/problems/word-ladder/) | BFS on words |
| Hard | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | topological sort (premium) |
