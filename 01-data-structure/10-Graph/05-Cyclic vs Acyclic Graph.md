# Cyclic vs Acyclic Graph

#### 1. What Is It?

- A **cycle** is a path that starts and ends at the same vertex.
- A **cyclic** graph has at least one cycle. An **acyclic** graph has none.

Three names to know:

| Name | Meaning |
|---|---|
| **Tree** | undirected, connected, **no cycle** (`V - 1` edges) |
| **Forest** | several trees (undirected, no cycle) |
| **DAG** | **D**irected **A**cyclic **G**raph: one-way edges, no cycle |

Why it matters:

- A **DAG** can be put in order: **topological sort**. Task dependencies must be a DAG. A cycle means "A needs B, B needs A": impossible.
- Many graph walks need a `visited` set only because of cycles.
- "Is this a valid tree?" and "will this edge create a cycle?" are common interview questions.

#### 2. How It Works

```text
Cyclic (undirected):       Acyclic (undirected, a tree):
A --- B                    A --- B
|     |                    |
C --- D                    C --- D

Cyclic (directed):         DAG (directed, no cycle):
A → B → C                  A → B → C
↑       |                  |       ↑
└───────┘                  └───────┘     (two paths to C, but no way back to A)
```

How to detect a cycle:

| Graph | Method | Note |
|---|---|---|
| Undirected | DFS and watch for a visited neighbour that is not the parent; or union-find | 13, 23 |
| Directed | DFS with 3 states (unvisited, visiting, done); or Kahn's algorithm | 14, 16 |

**Valid tree test (very common):** a graph with `n` nodes is a tree if and only if it has **exactly `n - 1` edges** and is **connected**.

#### 3. Kotlin Code

```kotlin
// Graph Valid Tree (LeetCode 261): n nodes, undirected edges
fun validTree(n: Int, edges: Array<IntArray>): Boolean {
    if (edges.size != n - 1) return false              // a tree has exactly n - 1 edges
    val graph = List(n) { mutableListOf<Int>() }
    for ((a, b) in edges) {
        graph[a].add(b)
        graph[b].add(a)
    }
    val visited = BooleanArray(n)
    val queue = ArrayDeque<Int>()
    visited[0] = true
    queue.addLast(0)
    var count = 1
    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        for (next in graph[node]) {
            if (!visited[next]) {
                visited[next] = true
                count++
                queue.addLast(next)
            }
        }
    }
    return count == n                                  // connected: every node was reached
}
```

Checks: `validTree(5, [[0,1],[0,2],[0,3],[1,4]])` → `true`. `validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])` → `false` (5 edges, not 4).

The full cycle-detection code is in notes 13 and 14.

#### 4. Complexity

| | Time |
|---|---|
| Valid tree check | `O(V + E)` |
| Cycle detection (DFS or union-find) | `O(V + E)` |

#### 5. Common Mistakes

1. **Using the undirected check on a directed graph.** In a directed graph, reaching a visited node does not always mean a cycle.
2. **Forgetting the connected check** in the tree test. `n - 1` edges alone is not enough.
3. **Forgetting the edge count check.** Connected alone is not enough.
4. **Treating a DAG as a tree.** A DAG can have two paths to one node.

#### 6. Say This in the Interview

1. "A tree is connected and has `n - 1` edges. I check both."
2. "For a directed graph I detect cycles with DFS states or Kahn's algorithm. For an undirected one, I use a parent check or union-find."
3. "If there is a cycle in the dependencies, no valid order exists."

#### 7. Quick Check

1. What does DAG stand for?
2. A graph has 6 nodes and 5 edges. Is it always a tree?

<details>
<summary>Answers</summary>

1. Directed Acyclic Graph.
2. No. It must also be connected. With 5 edges it could be a cycle plus a separate piece.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 261 | Graph Valid Tree (Medium, premium) | `n - 1` edges + connected |
| 684 | Redundant Connection (Medium) | the edge that makes a cycle (union-find) |
| 207 | Course Schedule (Medium) | is there a cycle? |
| 210 | Course Schedule II (Medium) | order for a DAG |
| 802 | Find Eventual Safe States (Medium) | nodes that cannot reach a cycle |
