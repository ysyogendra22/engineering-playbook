# Graph Representation

> In an interview you must decide how to store the graph before you write any algorithm. The usual answer is the adjacency list.

#### 1. What Is It?

There are three standard ways to store a graph in code.

| Way | What it is | Memory |
|---|---|---|
| **Adjacency list** | for each vertex, a list of its neighbours | `O(V + E)` |
| **Adjacency matrix** | a `V × V` table; cell `[a][b]` says if an edge exists | `O(V²)` |
| **Edge list** | one list of all edges `[a, b]` (or `[a, b, weight]`) | `O(E)` |

#### 2. How It Works

The graph: edges `0-1`, `0-2`, `1-3`, `2-3`.

```text
Adjacency list:           Adjacency matrix:            Edge list:
0: [1, 2]                     0  1  2  3               [0, 1]
1: [0, 3]                 0   0  1  1  0               [0, 2]
2: [0, 3]                 1   1  0  0  1               [1, 3]
3: [1, 2]                 2   1  0  0  1               [2, 3]
                          3   0  1  1  0
```

How to choose:

| Question | Best choice |
|---|---|
| Walk the graph (BFS / DFS / Dijkstra / topological sort) | **adjacency list** |
| "Is there an edge between `a` and `b`?" many times, small graph | adjacency matrix (`O(1)`) |
| The input already comes as pairs, or you sort edges (Kruskal) | edge list |
| Dense graph (many edges, `E` close to `V²`) | adjacency matrix |
| Sparse graph (few edges) | **adjacency list** |

Most interview graphs are **sparse**, so use the adjacency list. For a grid, you do not build anything: the neighbours are computed from the row and column (note 11).

A weighted adjacency list stores `(neighbour, weight)`.

#### 3. Kotlin Code

```kotlin
// Adjacency list (undirected)
fun adjacencyList(n: Int, edges: Array<IntArray>): List<List<Int>> {
    val graph = List(n) { mutableListOf<Int>() }
    for ((a, b) in edges) {
        graph[a].add(b)
        graph[b].add(a)
    }
    return graph
}

// Weighted adjacency list: edges are [a, b, weight]
fun weightedList(n: Int, edges: Array<IntArray>): List<List<Pair<Int, Int>>> {
    val graph = List(n) { mutableListOf<Pair<Int, Int>>() }
    for ((a, b, w) in edges) {
        graph[a].add(b to w)
        graph[b].add(a to w)
    }
    return graph
}

// Adjacency matrix
fun adjacencyMatrix(n: Int, edges: Array<IntArray>): Array<BooleanArray> {
    val matrix = Array(n) { BooleanArray(n) }
    for ((a, b) in edges) {
        matrix[a][b] = true
        matrix[b][a] = true
    }
    return matrix
}

// Usage
val edges = arrayOf(intArrayOf(0, 1), intArrayOf(0, 2), intArrayOf(1, 3), intArrayOf(2, 3))
println(adjacencyList(4, edges))                  // [[1, 2], [0, 3], [0, 3], [1, 2]]
println(adjacencyMatrix(4, edges)[0][1])          // true: edge 0-1 exists, checked in O(1)
```

Sometimes the input is **already** a matrix or a list (e.g. `isConnected[i][j] == 1` in *Number of Provinces*, or `graph[i]` = neighbours of `i` in *Is Graph Bipartite?*). Use it directly. Do not convert it.

#### 4. Complexity

| | Adjacency list | Adjacency matrix | Edge list |
|---|---|---|---|
| Memory | `O(V + E)` | `O(V²)` | `O(E)` |
| Is there an edge `a-b`? | `O(degree)` | `O(1)` | `O(E)` |
| All neighbours of `a` | `O(degree)` | `O(V)` | `O(E)` |
| Walk the whole graph | `O(V + E)` | `O(V²)` | — |

#### 5. Common Mistakes

1. **Using a matrix for a big sparse graph.** `V = 100,000` needs 10 billion cells.
2. **Forgetting the reverse edge** for an undirected graph.
3. **Building the graph when the input is already usable.**
4. **Using `Array(n) { mutableListOf<Int>() }` incorrectly as `Array(n, mutableListOf())`.** That shares one list between all nodes. Use the lambda form.
5. **Node numbers that start at `1`** while the array starts at `0`. Allocate `n + 1` or subtract 1.

#### 6. Say This in the Interview

1. "I will use an adjacency list, because the graph is sparse. Memory is `O(V + E)` and a full walk is `O(V + E)`."
2. "An adjacency matrix would need `O(V²)` memory, which is too much here."
3. "For Kruskal's algorithm I keep an edge list so I can sort it."

#### 7. Quick Check

1. Which representation gives an `O(1)` check for an edge between `a` and `b`?
2. Why is `Array(n, mutableListOf<Int>())` a bug?

<details>
<summary>Answers</summary>

1. The adjacency matrix.
2. It puts the same list object in every slot, so all nodes share one neighbour list.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1971 | Find if Path Exists in Graph (Easy) | edge list → adjacency list |
| 547 | Number of Provinces (Medium) | the input is already a matrix |
| 997 | Find the Town Judge (Easy) | only degree arrays are needed |
| 133 | Clone Graph (Medium) | the graph is given as node objects |
| 1584 | Min Cost to Connect All Points (Medium) | complete graph, no list needed |
