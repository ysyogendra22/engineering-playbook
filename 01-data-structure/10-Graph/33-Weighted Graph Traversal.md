# Weighted Graph Traversal

> How to walk a graph when the edges carry numbers. Some interview problems hide a weighted graph in a simple story.

#### 1. What Is It?

In a **weighted graph** each edge has a **weight**. When you walk the graph (BFS or DFS) you carry along a **running value** built from those weights: a total cost, a product, a maximum.

Two kinds of questions:

| Question | Method |
|---|---|
| **Cheapest** / shortest path | Dijkstra (note 18) |
| **Is there a path, and what is its value?** (not the cheapest) | plain DFS / BFS that carries the value |

The second kind often looks like a maths puzzle. *Evaluate Division* (LeetCode 399) is the classic:

> Given `a / b = 2.0` and `b / c = 3.0`, what is `a / c`? And `c / a`? And `a / x` if `x` is unknown?

Each variable is a **node**. The equation `a / b = 2.0` is an edge `a → b` with weight `2.0`, and the reverse edge `b → a` with weight `1 / 2.0`. The answer to a query is the **product of the weights** along any path.

#### 2. How It Works

```text
a / b = 2.0   →  a → b (2.0),  b → a (0.5)
b / c = 3.0   →  b → c (3.0),  c → b (0.333...)

Query a / c:  path a → b → c:  2.0 × 3.0 = 6.0
Query c / a:  path c → b → a:  0.333 × 0.5 = 0.1666...
Query a / x:  x is not in the graph → -1.0
Query a / a:  1.0
```

DFS from the start node, carrying the product `acc`:

```text
dfs(cur, target, acc):
    if cur == target: return acc
    mark cur visited
    for each (next, weight) of cur:
        if next not visited:
            result = dfs(next, target, acc × weight)
            if result is found: return it
    return not found
```

Any path gives the same answer here (the equations are consistent), so DFS is enough. For a **cheapest** path you would need Dijkstra.

#### 3. Kotlin Code

```kotlin
// Evaluate Division (LeetCode 399)
fun calcEquation(
    equations: List<List<String>>,
    values: DoubleArray,
    queries: List<List<String>>
): DoubleArray {
    val graph = HashMap<String, MutableList<Pair<String, Double>>>()
    for ((i, eq) in equations.withIndex()) {
        val (a, b) = eq
        graph.getOrPut(a) { mutableListOf() }.add(b to values[i])            // a → b with weight a / b
        graph.getOrPut(b) { mutableListOf() }.add(a to 1.0 / values[i])      // b → a with weight b / a
    }

    fun dfs(cur: String, target: String, acc: Double, visited: HashSet<String>): Double {
        if (cur == target) return acc
        visited.add(cur)
        for ((next, weight) in graph[cur] ?: emptyList()) {
            if (next !in visited) {
                val result = dfs(next, target, acc * weight, visited)
                if (result >= 0) return result                                // found
            }
        }
        return -1.0
    }

    return DoubleArray(queries.size) { i ->
        val (a, b) = queries[i]
        if (a !in graph || b !in graph) -1.0 else dfs(a, b, 1.0, HashSet())
    }
}

// Weighted adjacency list: the total weight of a path
fun pathWeight(graph: List<List<Pair<Int, Int>>>, path: List<Int>): Int {
    var total = 0
    for (i in 0 until path.size - 1) {
        total += graph[path[i]].first { it.first == path[i + 1] }.second
    }
    return total
}
```

Check: `calcEquation([["a","b"],["b","c"]], [2.0, 3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])` → `[6.0, 0.5, -1.0, 1.0, -1.0]`.

Other weighted-walk problems you already know:

| Question | Walk |
|---|---|
| Network Delay Time (743) | Dijkstra |
| Path with Maximum Probability (1514) | Dijkstra, multiply and maximise |
| Cheapest Flights Within K Stops (787) | BFS by levels with a cost array, or Bellman-Ford |
| Path With Minimum Effort (1631) | Dijkstra with `max` as the cost |

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Evaluate Division, per query | `O(V + E)` | `O(V)` |
| Dijkstra | `O((V + E) log V)` | `O(V)` |

#### 5. Common Mistakes

1. **Forgetting the reverse edge** with weight `1 / value`.
2. **Using BFS or DFS** when the question asks for the cheapest path. Use Dijkstra.
3. **Not checking that both variables exist** (`x / x` with unknown `x` is `-1.0`, not `1.0`).
4. **Not marking nodes visited**, so cycles loop forever.
5. **Using `0` as "not found"**, which is a possible answer. Use `-1.0` as the question says.
6. **Floating-point equality.** Avoid `==` on doubles except for sentinel values like `-1.0`.

#### 6. Say This in the Interview

1. "Each variable is a node and each equation is a weighted edge in both directions: `value` and `1 / value`."
2. "A query is a path, and the answer is the product of the weights along it. I use DFS with a visited set."
3. "If I needed the cheapest path I would use Dijkstra instead."

#### 7. Quick Check

1. If `a / b = 4`, what is the weight of the edge `b → a`?
2. Which algorithm is used for the cheapest weighted path?

<details>
<summary>Answers</summary>

1. `1 / 4 = 0.25`.
2. Dijkstra (for non-negative weights).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 399 | Evaluate Division (Medium) | multiply weights along a path |
| 743 | Network Delay Time (Medium) | Dijkstra |
| 1514 | Path with Maximum Probability (Medium) | Dijkstra, maximise a product |
| 787 | Cheapest Flights Within K Stops (Medium) | cost with a stop limit |
| 1631 | Path With Minimum Effort (Medium) | Dijkstra with `max` |
