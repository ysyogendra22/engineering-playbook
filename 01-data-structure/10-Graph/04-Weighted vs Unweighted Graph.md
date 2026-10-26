# Weighted vs Unweighted Graph

#### 1. What Is It?

- **Unweighted graph:** all edges are equal. Every step counts as 1.
- **Weighted graph:** each edge has a **weight** (a cost): distance, time, price, difficulty.

This difference decides **which shortest-path algorithm** you must use. This is asked in almost every graph interview.

| Edge weights | Algorithm | Time |
|---|---|---|
| all equal (or none) | **BFS** | `O(V + E)` |
| only `0` or `1` | 0-1 BFS (Queue folder, note 17) | `O(V + E)` |
| different, **not negative** | **Dijkstra** (note 18) | `O((V + E) log V)` |
| negative possible | Bellman-Ford | `O(V · E)` |
| all pairs of nodes | Floyd-Warshall | `O(V³)` |

#### 2. How It Works

```text
Unweighted:  A --- B --- C            "shortest" = fewest edges
Weighted:    A -5- B -1- C            "shortest" = smallest total weight
             A ---------2--- C        A → C directly costs 2, but A → B → C costs 6
```

BFS thinks `A → B → C` (2 edges) is longer than `A → C` (1 edge). But in the weighted graph, the cheapest route depends on the weights, not on the number of edges.

A weighted edge is stored as **(neighbour, weight)**:

```text
0: [(1, 5), (2, 2)]
1: [(0, 5), (2, 1)]
2: [(0, 2), (1, 1)]
```

#### 3. Kotlin Code

```kotlin
// Weighted undirected graph: each entry is a Pair(neighbour, weight)
fun buildWeightedGraph(n: Int, edges: Array<IntArray>): List<List<Pair<Int, Int>>> {
    val graph = List(n) { mutableListOf<Pair<Int, Int>>() }
    for ((a, b, w) in edges) {
        graph[a].add(b to w)
        graph[b].add(a to w)
    }
    return graph
}

// Total weight of a path
fun pathCost(graph: List<List<Pair<Int, Int>>>, path: List<Int>): Int {
    var total = 0
    for (i in 0 until path.size - 1) {
        val (_, w) = graph[path[i]].first { it.first == path[i + 1] }
        total += w
    }
    return total
}

// Usage
val g = buildWeightedGraph(3, arrayOf(intArrayOf(0, 1, 5), intArrayOf(0, 2, 2), intArrayOf(1, 2, 1)))
println(pathCost(g, listOf(0, 1, 2)))     // 6
println(pathCost(g, listOf(0, 2)))        // 2
```

How to choose in an interview:

```text
Does every move cost the same?        → BFS
Do costs differ and none is negative? → Dijkstra
Are there negative costs?             → Bellman-Ford
```

#### 4. Complexity

| | Unweighted (BFS) | Weighted (Dijkstra) |
|---|---|---|
| Time | `O(V + E)` | `O((V + E) log V)` |
| Memory | `O(V)` | `O(V)` |

#### 5. Common Mistakes

1. **Using BFS on a weighted graph.** It finds the fewest edges, not the lowest cost.
2. **Using Dijkstra with negative weights.** It can give wrong answers.
3. **Forgetting that weights go in both directions** for an undirected weighted edge.
4. **Overflow.** A sum of weights may be bigger than `Int`. Use `Long` when the limits are big.
5. **Using `Int.MAX_VALUE` as infinity and then adding to it.** It overflows. Check before adding.

#### 6. Say This in the Interview

1. "Are the edges weighted? If all moves cost 1, BFS is enough and gives `O(V + E)`."
2. "With different non-negative weights I use Dijkstra with a priority queue."
3. "If there could be negative weights I would use Bellman-Ford."

#### 7. Quick Check

1. Which algorithm for the fewest moves in a maze?
2. Why does BFS fail on a weighted graph?

<details>
<summary>Answers</summary>

1. BFS (all moves cost the same).
2. BFS counts edges, not total weight. The path with fewer edges can have a much higher cost.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1091 | Shortest Path in Binary Matrix (Medium) | unweighted, BFS |
| 743 | Network Delay Time (Medium) | weighted, Dijkstra |
| 1631 | Path With Minimum Effort (Medium) | weighted grid, Dijkstra |
| 787 | Cheapest Flights Within K Stops (Medium) | weighted with a stop limit |
| 1514 | Path with Maximum Probability (Medium) | Dijkstra on probabilities |
