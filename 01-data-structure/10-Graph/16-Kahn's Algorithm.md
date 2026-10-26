# Kahn's Algorithm

> The BFS way to do a topological sort. Easy to write and easy to explain. Many interviewers prefer it.

#### 1. What Is It?

**Kahn's algorithm** finds a topological order with a **queue** and the **in-degree** of each node.

- **In-degree** = the number of edges coming **into** a node = the number of tasks that must be done **before** it.
- A node with in-degree `0` has nothing to wait for, so it can go **first**.

The idea: repeat "take a node with in-degree 0, put it in the order, and remove it from the graph."

It also **detects cycles**: if you cannot take all the nodes, the rest are stuck in a cycle.

#### 2. How It Works

```text
Edges: 0 → 1, 0 → 2, 1 → 3, 2 → 3

in-degree:  0:0   1:1   2:1   3:2

queue = [0]                       (only 0 has in-degree 0)
take 0 → order [0]
         lower in-degree of 1 → 0 → add 1;  of 2 → 0 → add 2      queue = [1, 2]
take 1 → order [0, 1]
         lower in-degree of 3 → 1 (still waiting for 2)
take 2 → order [0, 1, 2]
         lower in-degree of 3 → 0 → add 3                           queue = [3]
take 3 → order [0, 1, 2, 3]

processed 4 nodes = all nodes → no cycle
```

If the number of processed nodes is **less than `n`**, there is a cycle.

```text
Edges: 0 → 1, 1 → 0       in-degree: 0:1  1:1   → no node with in-degree 0 → queue is empty → 0 processed < 2 → cycle
```

#### 3. Kotlin Code

```kotlin
// Returns a valid order, or an empty list if there is a cycle
fun kahn(n: Int, graph: List<List<Int>>): List<Int> {
    val indegree = IntArray(n)
    for (node in 0 until n) for (next in graph[node]) indegree[next]++

    val queue = ArrayDeque<Int>()
    for (node in 0 until n) if (indegree[node] == 0) queue.addLast(node)

    val order = mutableListOf<Int>()
    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        order.add(node)
        for (next in graph[node]) {
            indegree[next]--
            if (indegree[next] == 0) queue.addLast(next)      // all its prerequisites are done
        }
    }
    return if (order.size == n) order else emptyList()        // fewer than n → a cycle
}

// Course Schedule II (LeetCode 210)
fun findOrder(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
    val graph = List(numCourses) { mutableListOf<Int>() }
    for ((course, pre) in prerequisites) graph[pre].add(course)
    return kahn(numCourses, graph).toIntArray()
}

// Course Schedule (LeetCode 207)
fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean =
    findOrder(numCourses, prerequisites).size == numCourses

// Minimum number of semesters if you can take any number of courses per semester (BFS by levels)
fun minimumSemesters(n: Int, relations: Array<IntArray>): Int {      // courses are numbered 1..n
    val graph = List(n + 1) { mutableListOf<Int>() }
    val indegree = IntArray(n + 1)
    for ((a, b) in relations) { graph[a].add(b); indegree[b]++ }
    val queue = ArrayDeque<Int>()
    for (i in 1..n) if (indegree[i] == 0) queue.addLast(i)
    var semesters = 0
    var taken = 0
    while (queue.isNotEmpty()) {
        semesters++
        repeat(queue.size) {                                          // one semester = one level
            val course = queue.removeFirst()
            taken++
            for (next in graph[course]) if (--indegree[next] == 0) queue.addLast(next)
        }
    }
    return if (taken == n) semesters else -1
}
```

Checks: `kahn(4, [[1,2],[3],[3],[]])` → `[0, 1, 2, 3]`. `findOrder(2, [[1,0]])` → `[0, 1]`. `canFinish(2, [[1,0],[0,1]])` → `false`. `minimumSemesters(3, [[1,3],[2,3]])` → `2`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Kahn's algorithm | `O(V + E)` | `O(V)` |

Each node and each edge is handled once.

#### 5. Common Mistakes

1. **Wrong edge direction.** For `[course, prerequisite]` the edge is `prerequisite → course`.
2. **Forgetting the cycle check** (`order.size == n`).
3. **Adding a node when its in-degree is decreased**, not when it reaches `0`.
4. **Not counting every edge** when computing in-degrees.
5. **Parallel edges** (the same pair twice) count twice in the in-degree and must be decreased twice. The code does that.
6. **Assuming a unique answer.** Several orders can be valid.

#### 6. Say This in the Interview

1. "I count the in-degree of every node. Nodes with in-degree 0 go into a queue."
2. "I take a node, add it to the order, and lower the in-degree of its neighbours. A neighbour with in-degree 0 joins the queue."
3. "If I process fewer than `n` nodes, there is a cycle. Time `O(V + E)`."

#### 7. Quick Check

1. What is the in-degree of a node?
2. How does Kahn's algorithm tell you there is a cycle?

<details>
<summary>Answers</summary>

1. The number of edges pointing into it (how many things must come before it).
2. The order ends up with fewer than `n` nodes. The nodes in a cycle never reach in-degree 0.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 207 | Course Schedule (Medium) | cycle check with Kahn |
| 210 | Course Schedule II (Medium) | the order |
| 1136 | Parallel Courses (premium) | levels = semesters |
| 310 | Minimum Height Trees (Medium) | peel leaves, a Kahn-style idea (note 32) |
| 2115 | Find All Possible Recipes from Given Supplies (Medium) | dependencies |
| 2050 | Parallel Courses III (Hard) | longest path in a DAG (note 34) |
