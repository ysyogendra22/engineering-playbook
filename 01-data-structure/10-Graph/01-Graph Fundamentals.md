# Graph Fundamentals

> Start here. Graphs appear in many FAANG interview questions, often hidden inside a grid, a list of courses, or a word puzzle. Read this note slowly once.

#### 1. What Is a Graph?

A **graph** is a set of **things** and the **connections** between them.

- The things are called **vertices** (or **nodes**).
- The connections are called **edges**.

Real-life examples: people and friendships, cities and roads, web pages and links, courses and prerequisites.

```text
A ----- B            Vertices: A, B, C, D
|       |            Edges:    A-B, A-C, B-D, C-D
C ----- D
```

Unlike a tree, a graph can have **cycles** (a way back to the start), **many paths** between two nodes, and **separate pieces**.

#### 2. Words You Must Know

| Word | Meaning |
|---|---|
| **Vertex / node** | one item (a person, a city, a course) |
| **Edge** | a connection between two vertices |
| **Neighbour** | a vertex directly connected to another |
| **Path** | a list of vertices where each is connected to the next |
| **Cycle** | a path that comes back to where it started |
| **Directed** | edges have a direction (`A → B` is not `B → A`) |
| **Weighted** | edges have a cost (distance, time, price) |
| **Connected** | you can reach every vertex from every other vertex |
| **`V`, `E`** | the number of vertices, the number of edges |

#### 3. How It Works

In an interview you almost never draw the graph. You store it in code. The standard way is an **adjacency list**: for each vertex, a list of its neighbours.

```text
Edges: 0-1, 0-2, 1-3, 2-3

0: [1, 2]
1: [0, 3]
2: [0, 3]
3: [1, 2]
```

Then you **walk** the graph:

| Walk | Uses | Good for |
|---|---|---|
| **DFS** (go deep first) | stack or recursion | cycles, components, paths, all possibilities |
| **BFS** (go level by level) | queue | shortest path with equal steps, nearest target |

Both need a **visited** set, because a graph can have cycles. Without it, you walk in circles forever.

Graph vs tree: a tree is a graph that is **connected** and has **no cycles**. A tree with `n` nodes always has `n - 1` edges.

#### 4. Kotlin Code

```kotlin
// Build an undirected graph from an edge list
fun buildGraph(n: Int, edges: Array<IntArray>): List<List<Int>> {
    val graph = List(n) { mutableListOf<Int>() }
    for ((a, b) in edges) {
        graph[a].add(b)
        graph[b].add(a)              // undirected: add both directions
    }
    return graph
}

// Walk the graph with BFS and return the nodes you can reach from start
fun reachable(graph: List<List<Int>>, start: Int): List<Int> {
    val visited = BooleanArray(graph.size)
    val order = mutableListOf<Int>()
    val queue = ArrayDeque<Int>()
    visited[start] = true
    queue.addLast(start)
    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        order.add(node)
        for (next in graph[node]) {
            if (!visited[next]) {
                visited[next] = true
                queue.addLast(next)
            }
        }
    }
    return order
}

// Usage
val graph = buildGraph(4, arrayOf(intArrayOf(0, 1), intArrayOf(0, 2), intArrayOf(1, 3), intArrayOf(2, 3)))
println(graph)                       // [[1, 2], [0, 3], [0, 3], [1, 2]]
println(reachable(graph, 0))         // [0, 1, 2, 3]
```

#### 5. How to Spot a Graph Problem

| If the question has... | Think... | Note |
|---|---|---|
| "connections", "friends", "network", "islands" | connected components | 10, 23 |
| a grid of cells (up, down, left, right) | grid as a graph | 11, 12 |
| "prerequisites", "dependencies", "order of tasks" | topological sort | 15, 16 |
| "minimum number of steps/moves" | BFS | 9, 17 |
| "cheapest route", "minimum cost/time" with different costs | Dijkstra | 18 |
| "does this create a cycle?" | cycle detection or DSU | 13, 14, 23 |
| "split into two groups" | bipartite check | 22 |
| "connect everything at the lowest cost" | minimum spanning tree | 26 – 28 |
| "words/states you can change one step at a time" | implicit graph + BFS | 30 |

#### 6. Complexity

| Action | Time |
|---|---|
| DFS or BFS over the whole graph | `O(V + E)` |
| Memory for an adjacency list | `O(V + E)` |
| Check if an edge `a-b` exists (adjacency list) | `O(degree of a)` |

#### 7. Common Mistakes

1. **No `visited` check.** The program loops forever on a cycle.
2. **Marking visited too late in BFS.** Mark when you add to the queue.
3. **Forgetting the reverse edge** in an undirected graph.
4. **Missing disconnected parts.** Start a search from every unvisited node.
5. **Mixing `0`-based and `1`-based node numbers.**

#### 8. Say This in the Interview

1. "I will model this as a graph. The nodes are ... and the edges are ..."
2. "I store it as an adjacency list, so a full walk is `O(V + E)`."
3. "I use BFS (or DFS) with a visited set."
4. "I will check disconnected parts, cycles and an empty input."

#### 9. Quick Check

1. How many edges does a tree with 7 nodes have?
2. Why do we need a `visited` set?

<details>
<summary>Answers</summary>

1. `6` (`n - 1`).
2. A graph can have cycles. Without `visited` you would go around a cycle forever.

</details>

#### 10. Related LeetCode Questions (Often Asked)

Solve them in this order. Search by title if a number looks wrong.

**Start here — Easy**

| # | Question | Main idea | Note |
|---|---|---|---|
| 1971 | Find if Path Exists in Graph | BFS or DFS | 8, 9 |
| 997 | Find the Town Judge | in-degree and out-degree | 32 |
| 733 | Flood Fill | DFS on a grid | 12 |
| 463 | Island Perimeter | count borders of cells | 11 |

**Most often asked — Medium**

| # | Question | Main idea | Note |
|---|---|---|---|
| 200 | Number of Islands | grid DFS/BFS | 11 |
| 133 | Clone Graph | map old → clone | 29 |
| 207 | Course Schedule | cycle in a directed graph | 14, 16 |
| 210 | Course Schedule II | topological order | 15, 16 |
| 547 | Number of Provinces | connected components | 10, 23 |
| 994 | Rotting Oranges | multi-source BFS | 21 |
| 785 | Is Graph Bipartite? | 2-colouring | 22 |
| 743 | Network Delay Time | Dijkstra | 18 |
| 684 | Redundant Connection | union-find | 23 |
| 399 | Evaluate Division | weighted graph DFS | 33 |

**Hard — these separate strong candidates**

| # | Question | Main idea | Note |
|---|---|---|---|
| 127 | Word Ladder | BFS on words | 30 |
| 269 | Alien Dictionary | topological sort | 31 |
| 778 | Swim in Rising Water | Dijkstra or union-find | 18 |

**If you have little time, do these 8 first:** 200, 133, 207, 210, 547, 994, 743, 127.
