# Connected Components

#### 1. What Is It?

A **connected component** is a group of vertices where every vertex can reach every other vertex in the group, and no vertex outside the group is connected to it.

"Count the groups" is one of the most common graph questions. It hides behind many stories:

| Story | Component means |
|---|---|
| provinces, friend circles | a group of connected people |
| islands | a group of connected land cells |
| network connectivity | computers that can reach each other |
| accounts that share an email | accounts of one person |

Two ways to count them:

| Way | Idea | Use when |
|---|---|---|
| **DFS / BFS** | start a search from each unvisited node | the whole graph is given |
| **Union-Find** | merge nodes edge by edge, count the groups | edges arrive one by one, or you also need "same group?" queries |

#### 2. How It Works

```text
Graph:  0-1, 1-2, 3-4,  5 (alone)

DFS from 0 → visits {0, 1, 2}       components = 1
DFS from 3 → visits {3, 4}          components = 2
DFS from 5 → visits {5}             components = 3
```

With union-find: start with `n` groups. Every time `union(a, b)` joins two **different** groups, the group count goes down by one.

```text
n = 6 → 6 groups
union(0,1): different groups → 5
union(1,2): different        → 4
union(3,4): different        → 3
groups = 3
```

**Number of Provinces** (LeetCode 547) gives an `n × n` matrix where `isConnected[i][j] == 1` means `i` and `j` are connected. Run the same loop; the neighbours of `i` are the `j` with `isConnected[i][j] == 1`.

#### 3. Kotlin Code

```kotlin
// Number of Provinces (LeetCode 547): DFS on an adjacency matrix
fun findCircleNum(isConnected: Array<IntArray>): Int {
    val n = isConnected.size
    val visited = BooleanArray(n)

    fun dfs(city: Int) {
        visited[city] = true
        for (other in 0 until n) {
            if (isConnected[city][other] == 1 && !visited[other]) dfs(other)
        }
    }

    var provinces = 0
    for (city in 0 until n) {
        if (!visited[city]) {
            provinces++
            dfs(city)
        }
    }
    return provinces
}

// Max Area of Island (LeetCode 695): the size of the biggest component on a grid
fun maxAreaOfIsland(grid: Array<IntArray>): Int {
    val rows = grid.size
    val cols = grid[0].size

    fun dfs(r: Int, c: Int): Int {
        if (r !in 0 until rows || c !in 0 until cols || grid[r][c] != 1) return 0
        grid[r][c] = 0                                      // mark visited
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
    }

    var best = 0
    for (r in 0 until rows) for (c in 0 until cols) best = maxOf(best, dfs(r, c))
    return best
}

// Number of Operations to Make Network Connected (LeetCode 1319)
// You need (components - 1) cables to join all components, and n - 1 cables in total.
fun makeConnected(n: Int, connections: Array<IntArray>): Int {
    if (connections.size < n - 1) return -1                 // not enough cables
    val graph = List(n) { mutableListOf<Int>() }
    for ((a, b) in connections) { graph[a].add(b); graph[b].add(a) }
    val visited = BooleanArray(n)
    fun dfs(node: Int) {
        visited[node] = true
        for (next in graph[node]) if (!visited[next]) dfs(next)
    }
    var components = 0
    for (i in 0 until n) if (!visited[i]) { components++; dfs(i) }
    return components - 1
}
```

Checks: `findCircleNum([[1,1,0],[1,1,0],[0,0,1]])` → `2`. `maxAreaOfIsland([[1,1,0],[0,1,0],[0,0,1]])` → `3`. `makeConnected(4, [[0,1],[0,2],[1,2]])` → `1`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| DFS / BFS | `O(V + E)` | `O(V)` |
| Matrix input (`n × n`) | `O(V²)` | `O(V)` |
| Grid `R × C` | `O(R · C)` | `O(R · C)` worst case (recursion) |
| Union-find | `O(E · α(V))` | `O(V)` |

#### 5. Common Mistakes

1. **Counting after the search instead of before it.** Increase the counter when you *start* a new search.
2. **Forgetting isolated nodes.** Each is its own component.
3. **Not marking the cell/node visited at once**, so DFS comes back to it.
4. **Recursion depth** on a huge grid. Use BFS or an explicit stack.
5. **Modifying the input grid** when the caller still needs it.

#### 6. Say This in the Interview

1. "Each connected component is one group, so I loop over all nodes and start a DFS from every unvisited one. The number of starts is the answer."
2. "If edges arrive one by one, I use union-find and decrease the group count on each successful union."
3. "Time `O(V + E)`."

#### 7. Quick Check

1. A graph of 5 nodes has 3 edges and no cycle. How many components?
2. When do you prefer union-find over DFS?

<details>
<summary>Answers</summary>

1. `5 - 3 = 2`. Every edge of a forest joins two components.
2. When edges are added over time, or you must answer "are these two connected?" many times.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 547 | Number of Provinces (Medium) | count components (matrix) |
| 323 | Number of Connected Components in an Undirected Graph (Medium, premium) | count components |
| 200 | Number of Islands (Medium) | components on a grid |
| 695 | Max Area of Island (Medium) | size of the biggest component |
| 1319 | Number of Operations to Make Network Connected (Medium) | components − 1 |
| 721 | Accounts Merge (Medium) | union-find on emails |
