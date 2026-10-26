# Cycle Detection — Directed Graph

> Asked all the time: *Course Schedule* is a directed cycle detection.

#### 1. What Is It?

In a **directed** graph, a cycle means you can follow the arrows and come back to a node you started from.

Example: `A → B → C → A`. In a course schedule, "A needs B, B needs C, C needs A" is impossible.

The undirected "parent" check does **not** work here. In a directed graph, two different paths can reach the same node without any cycle:

```text
A → B → D        D is reached by two paths, but there is no cycle.
A → C → D
```

Two standard ways:

| Way | Idea |
|---|---|
| **DFS with 3 states** | a cycle exists if DFS reaches a node that is **still on the current path** |
| **Kahn's algorithm** (note 16) | if topological sort cannot process all nodes, there is a cycle |

#### 2. How It Works

Give every node one of three states:

| State | Meaning |
|---|---|
| `0` unvisited | not seen yet |
| `1` visiting | on the **current DFS path** |
| `2` done | fully explored, **no cycle through it** |

Rule: if DFS reaches a node whose state is `1` (visiting), we came back to the current path → **cycle**.

```text
Graph: 0 → 1, 1 → 2, 2 → 0

dfs(0): state[0] = visiting
   dfs(1): state[1] = visiting
      dfs(2): state[2] = visiting
         neighbour 0: state is visiting → CYCLE
```

```text
Graph: 0 → 1, 0 → 2, 1 → 3, 2 → 3          (no cycle)

dfs(0) visiting
   dfs(1) visiting → dfs(3) visiting → done (state 2) → 1 done
   dfs(2) visiting → neighbour 3 is DONE (not visiting) → fine → 2 done
0 done
```

Reaching a **done** node is fine. Only reaching a **visiting** node is a cycle.

#### 3. Kotlin Code

```kotlin
// Is there a cycle in a directed graph?
fun hasCycle(n: Int, graph: List<List<Int>>): Boolean {
    val state = IntArray(n)                       // 0 = unvisited, 1 = visiting, 2 = done

    fun dfs(node: Int): Boolean {
        state[node] = 1
        for (next in graph[node]) {
            if (state[next] == 1) return true     // back to the current path → cycle
            if (state[next] == 0 && dfs(next)) return true
        }
        state[node] = 2
        return false
    }

    for (s in 0 until n) {
        if (state[s] == 0 && dfs(s)) return true
    }
    return false
}

// Course Schedule (LeetCode 207): can you finish all courses?
fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
    val graph = List(numCourses) { mutableListOf<Int>() }
    for ((course, pre) in prerequisites) graph[pre].add(course)     // pre → course
    return !hasCycle(numCourses, graph)
}

// Find Eventual Safe States (LeetCode 802): nodes that cannot reach a cycle
fun eventualSafeNodes(graph: Array<IntArray>): List<Int> {
    val n = graph.size
    val state = IntArray(n)                       // 0 = unvisited, 1 = visiting, 2 = safe

    fun isSafe(node: Int): Boolean {
        if (state[node] == 1) return false        // on the current path → part of a cycle
        if (state[node] == 2) return true
        state[node] = 1
        for (next in graph[node]) if (!isSafe(next)) return false
        state[node] = 2
        return true
    }

    return (0 until n).filter { isSafe(it) }
}
```

Checks: `canFinish(2, [[1,0]])` → `true`. `canFinish(2, [[1,0],[0,1]])` → `false`. `eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])` → `[2, 4, 5, 6]`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| DFS with 3 states | `O(V + E)` | `O(V)` |
| Kahn's algorithm | `O(V + E)` | `O(V)` |

#### 5. Common Mistakes

1. **Using only a `visited` flag** (2 states). A node reached by two different paths looks like a cycle. You need the third state.
2. **Forgetting to set the state to "done"** after exploring a node.
3. **Using the parent check** from the undirected version.
4. **Checking only one start node.** Loop over all nodes.
5. **Wrong edge direction** in Course Schedule. The edge is `prerequisite → course`.

#### 6. Say This in the Interview

1. "In a directed graph I use DFS with three states: unvisited, on the current path, and done. Reaching a node that is on the current path means a cycle."
2. "Alternatively Kahn's algorithm: if I cannot process every node, there is a cycle."
3. "Time `O(V + E)`."

#### 7. Quick Check

1. Why is reaching a "done" node not a cycle?
2. For `[[1, 0]]` in Course Schedule, which way does the edge point?

<details>
<summary>Answers</summary>

1. A done node was fully explored and does not lead back to the current path. We just found another way to reach it.
2. `0 → 1` (course `0` is the prerequisite of course `1`).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 207 | Course Schedule (Medium) | is there a cycle? |
| 210 | Course Schedule II (Medium) | give the order (note 15) |
| 802 | Find Eventual Safe States (Medium) | nodes that cannot reach a cycle |
| 685 | Redundant Connection II (Hard) | directed cycle + in-degree |
| 329 | Longest Increasing Path in a Matrix (Hard) | DFS on a DAG with memo |
