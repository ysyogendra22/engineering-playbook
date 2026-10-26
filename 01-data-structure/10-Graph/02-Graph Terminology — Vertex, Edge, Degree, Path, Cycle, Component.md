# Graph Terminology — Vertex, Edge, Degree, Path, Cycle, Component

> The words interviewers use. Learn them once, so every graph question is easy to read.

#### 1. What Is It?

These are the basic words used to describe a graph.

| Word | Meaning | Example |
|---|---|---|
| **Vertex** (node) | one item | a person |
| **Edge** | a connection between two vertices | a friendship |
| **Adjacent / neighbour** | two vertices joined by an edge | two friends |
| **Degree** | the number of edges at a vertex | the number of friends |
| **In-degree / out-degree** | (directed graph) edges coming in / going out | followers / following |
| **Path** | vertices where each is connected to the next | `A → B → D` |
| **Cycle** | a path that returns to its start | `A → B → D → C → A` |
| **Connected component** | a group of vertices that can reach each other | one friend circle |
| **Self-loop** | an edge from a vertex to itself | `A → A` |
| **Parallel edges** | two edges between the same two vertices | two roads between two cities |

#### 2. How It Works

```text
Graph:   A --- B       E --- F
         |     |
         C --- D

Vertices:     A, B, C, D, E, F                  (6)
Edges:        A-B, A-C, B-D, C-D, E-F           (5)
Degree of A:  2 (edges A-B and A-C)
Path:         A → B → D
Cycle:        A → B → D → C → A
Components:   {A, B, C, D} and {E, F}           (2 components)
```

Two facts worth remembering:

1. **Handshake rule:** in an undirected graph, the sum of all degrees is `2 × E`. (Every edge adds 1 to the degree of each end.)
2. A graph with `V` vertices that is connected and has no cycle has exactly `V - 1` edges. That is a **tree**.

For a **directed** graph:

```text
A → B       A has out-degree 1;  B has in-degree 1
```

In-degree is the key number in topological sort (Kahn's algorithm, note 16).

#### 3. Kotlin Code

```kotlin
// Degrees of an undirected graph given as an edge list
fun degrees(n: Int, edges: Array<IntArray>): IntArray {
    val degree = IntArray(n)
    for ((a, b) in edges) {
        degree[a]++
        degree[b]++
    }
    return degree
}

// In-degree and out-degree of a directed graph
fun inOutDegrees(n: Int, edges: Array<IntArray>): Pair<IntArray, IntArray> {
    val inDeg = IntArray(n)
    val outDeg = IntArray(n)
    for ((from, to) in edges) {
        outDeg[from]++
        inDeg[to]++
    }
    return inDeg to outDeg
}

// Usage: the graph above (A=0, B=1, C=2, D=3, E=4, F=5)
val edges = arrayOf(intArrayOf(0, 1), intArrayOf(0, 2), intArrayOf(1, 3), intArrayOf(2, 3), intArrayOf(4, 5))
println(degrees(6, edges).toList())      // [2, 2, 2, 2, 1, 1]  → the sum is 10 = 2 × 5 edges
```

#### 4. Complexity

| Action | Time |
|---|---|
| Compute all degrees from an edge list | `O(E)` |
| Degree of one vertex (adjacency list) | `O(1)` (the size of its list) |

#### 5. Common Mistakes

1. **Confusing a path with a cycle.** A cycle must return to the start.
2. **Counting an undirected edge once** when computing degrees. Each end gets +1.
3. **Forgetting self-loops and parallel edges** when the question allows them.
4. **Mixing up in-degree and out-degree** in directed problems.

#### 6. Say This in the Interview

1. "Let me define: nodes are ..., edges are ... and the graph is directed/undirected."
2. "A tree is a connected graph with no cycles, so it has `V - 1` edges."
3. "I will count in-degrees to find the nodes with no prerequisites."

#### 7. Quick Check

1. A connected undirected graph has 5 vertices and 4 edges. Does it have a cycle?
2. In an undirected graph with 6 edges, what is the sum of all degrees?

<details>
<summary>Answers</summary>

1. No. It is a tree (`V - 1 = 4` edges, connected).
2. `12` (`2 × 6`).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 997 | Find the Town Judge (Easy) | in-degree `n - 1`, out-degree `0` |
| 1791 | Find Center of Star Graph (Easy) | the vertex with the highest degree |
| 1557 | Minimum Number of Vertices to Reach All Nodes (Medium) | vertices with in-degree `0` |
| 261 | Graph Valid Tree (Medium, premium) | connected and `V - 1` edges |
