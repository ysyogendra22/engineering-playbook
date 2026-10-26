# DFS — Depth First Search

> One of the two core graph walks. Many interview problems (islands, cycles, paths, components) are a DFS.

#### 1. What Is It?

**DFS** goes **as deep as possible** along one path. When it cannot go further, it goes back (**backtracks**) and tries the next path.

It uses **recursion** (the call stack) or your **own stack**. It needs a **visited** set, so it does not walk in circles on a cycle.

Think of exploring a maze: walk down a corridor until you hit a dead end, then go back to the last junction and try another corridor.

#### 2. How It Works

```text
Graph:  0 → [1, 2]    1 → [3]    2 → [3]    3 → []

dfs(0): visit 0
   dfs(1): visit 1
      dfs(3): visit 3          (3 has no neighbours → return)
   back in 0: next neighbour 2
   dfs(2): visit 2
      3 is already visited → skip

visit order: 0, 1, 3, 2
```

The recipe:

```text
dfs(node):
    mark node visited
    process node
    for each neighbour:
        if not visited: dfs(neighbour)
```

Use DFS when you need to: find **any** path, **count/mark components**, detect **cycles**, explore **all possibilities** (backtracking), or process a **grid region**. Use BFS (note 9) when you need the **shortest** path.

#### 3. Kotlin Code

```kotlin
// Recursive DFS: returns the visit order
fun dfs(graph: List<List<Int>>, start: Int): List<Int> {
    val visited = BooleanArray(graph.size)
    val order = mutableListOf<Int>()

    fun visit(node: Int) {
        visited[node] = true
        order.add(node)
        for (next in graph[node]) {
            if (!visited[next]) visit(next)
        }
    }

    visit(start)
    return order
}

// Iterative DFS with your own stack (safe for very deep graphs)
fun dfsIterative(graph: List<List<Int>>, start: Int): List<Int> {
    val visited = BooleanArray(graph.size)
    val order = mutableListOf<Int>()
    val stack = ArrayDeque<Int>()
    stack.addLast(start)
    while (stack.isNotEmpty()) {
        val node = stack.removeLast()
        if (visited[node]) continue
        visited[node] = true
        order.add(node)
        for (next in graph[node].asReversed()) {        // reversed: same order as the recursive version
            if (!visited[next]) stack.addLast(next)
        }
    }
    return order
}

// All Paths From Source to Target in a DAG (LeetCode 797)
fun allPathsSourceTarget(graph: Array<IntArray>): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    val path = mutableListOf(0)

    fun go(node: Int) {
        if (node == graph.size - 1) {
            result.add(path.toList())                    // save a copy
            return
        }
        for (next in graph[node]) {
            path.add(next)
            go(next)
            path.removeAt(path.size - 1)                 // backtrack
        }
    }

    go(0)
    return result
}

// Keys and Rooms (LeetCode 841): can you visit every room?
fun canVisitAllRooms(rooms: List<List<Int>>): Boolean {
    val visited = BooleanArray(rooms.size)
    fun visit(room: Int) {
        visited[room] = true
        for (key in rooms[room]) if (!visited[key]) visit(key)
    }
    visit(0)
    return visited.all { it }
}
```

Checks: `dfs([[1,2],[3],[3],[]], 0)` → `[0, 1, 3, 2]`. `allPathsSourceTarget([[1,2],[3],[3],[]])` → `[[0,1,3],[0,2,3]]`.

For a DAG you do not need `visited` in `allPathsSourceTarget`, because there are no cycles.

#### 4. Complexity

For `V` nodes and `E` edges:

| | Time | Space |
|---|---|---|
| DFS (adjacency list) | `O(V + E)` | `O(V)` (visited + the call stack) |
| All paths in a DAG | exponential in the worst case | `O(V)` for the path + the answer |

#### 5. Common Mistakes

1. **No `visited` set.** Infinite loop on a cycle.
2. **`StackOverflowError`** on very deep graphs. Use the iterative version.
3. **Marking visited after the recursive call** instead of before. A neighbour may visit the node again.
4. **Forgetting to backtrack** (`removeAt`) when collecting paths, or forgetting to **copy** the path (`path.toList()`) before saving it.
5. **Forgetting disconnected parts.** Start a DFS from every unvisited node.

#### 6. Say This in the Interview

1. "I will use DFS with a visited set. Time `O(V + E)`, space `O(V)` for the recursion."
2. "If the graph can be very deep, I would use an explicit stack to avoid a stack overflow."
3. "For all paths I add the node, recurse, then remove it (backtracking)."

#### 7. Quick Check

1. When is DFS a better choice than BFS?
2. What goes wrong if you forget to copy the path before saving it?

<details>
<summary>Answers</summary>

1. For cycles, components, all paths, and backtracking. BFS is better for the shortest path.
2. The saved list is the same object you keep changing, so it ends up empty or wrong. Save `path.toList()`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1971 | Find if Path Exists in Graph (Easy) | DFS from the source |
| 841 | Keys and Rooms (Medium) | can DFS reach every node? |
| 797 | All Paths From Source to Target (Medium) | DFS + backtracking |
| 200 | Number of Islands (Medium) | DFS on a grid |
| 133 | Clone Graph (Medium) | DFS + map |
| 207 | Course Schedule (Medium) | DFS cycle detection |
| 332 | Reconstruct Itinerary (Hard) | DFS on an Euler path |
