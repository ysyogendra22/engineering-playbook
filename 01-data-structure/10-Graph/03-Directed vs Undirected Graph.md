# Directed vs Undirected Graph

#### 1. What Is It?

| | Undirected | Directed |
|---|---|---|
| Edge | works **both ways**: `A — B` | works **one way**: `A → B` |
| Example | friendship on Facebook | following on Twitter, course prerequisites, web links |
| Picture | `A ----- B` | `A -----> B` |
| Stored as | add `B` to `A`'s list **and** `A` to `B`'s list | add `B` to `A`'s list only |
| Degree | one number | in-degree and out-degree |

Always find out which kind it is. It changes the code and the algorithms:

| Task | Undirected | Directed |
|---|---|---|
| Cycle detection | DFS with a parent, or union-find | DFS with 3 states, or Kahn's algorithm |
| Connected parts | components | strongly connected components (advanced) |
| Ordering tasks | not possible | topological sort |

#### 2. How It Works

Edges `[[0,1],[1,2]]`:

```text
Undirected:                    Directed:
0: [1]                         0: [1]
1: [0, 2]                      1: [2]
2: [1]                         2: []

You can go 0→1, 1→0, 1→2, 2→1.     You can go only 0→1 and 1→2.
```

**An undirected edge is the same as two directed edges** (`A → B` and `B → A`). That is how you store it.

Example of why it matters: *Course Schedule* gives pairs `[course, prerequisite]`. The edge is **one-way** (prerequisite → course). Treating it as undirected hides the real order.

#### 3. Kotlin Code

```kotlin
// One function for both kinds
fun buildGraph(n: Int, edges: Array<IntArray>, directed: Boolean): List<List<Int>> {
    val graph = List(n) { mutableListOf<Int>() }
    for ((a, b) in edges) {
        graph[a].add(b)
        if (!directed) graph[b].add(a)       // the reverse edge only for undirected graphs
    }
    return graph
}

val edges = arrayOf(intArrayOf(0, 1), intArrayOf(1, 2))
println(buildGraph(3, edges, directed = false))   // [[1], [0, 2], [1]]
println(buildGraph(3, edges, directed = true))    // [[1], [2], []]

// Course Schedule input: [course, prerequisite] → edge prerequisite → course
fun buildCourseGraph(n: Int, prerequisites: Array<IntArray>): List<List<Int>> {
    val graph = List(n) { mutableListOf<Int>() }
    for ((course, pre) in prerequisites) graph[pre].add(course)
    return graph
}
```

#### 4. Complexity

| | Undirected | Directed |
|---|---|---|
| Memory (adjacency list) | `O(V + 2E)` | `O(V + E)` |
| Walk the whole graph | `O(V + E)` | `O(V + E)` |

#### 5. Common Mistakes

1. **Forgetting the reverse edge** in an undirected graph. Half of the graph becomes unreachable.
2. **Adding the reverse edge** in a directed graph. You create wrong paths.
3. **Getting the edge direction wrong** when the input is `[a, b]`. Read the statement: is it `a → b` or `b → a`?
4. **Using the undirected cycle check** (parent check) on a directed graph. It gives wrong answers.

#### 6. Say This in the Interview

1. "Is the graph directed? It decides how I store the edges and which cycle check I use."
2. "For an undirected edge I add it in both directions."
3. "In Course Schedule the edge goes from the prerequisite to the course."

#### 7. Quick Check

1. How many entries does an undirected edge add to an adjacency list?
2. For `[course, prerequisite] = [1, 0]`, which way does the edge point?

<details>
<summary>Answers</summary>

1. `2` (one for each end).
2. `0 → 1` (from the prerequisite to the course).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1971 | Find if Path Exists in Graph (Easy) | undirected |
| 997 | Find the Town Judge (Easy) | directed, in and out degrees |
| 207 | Course Schedule (Medium) | directed, cycle detection |
| 785 | Is Graph Bipartite? (Medium) | undirected |
| 802 | Find Eventual Safe States (Medium) | directed |
