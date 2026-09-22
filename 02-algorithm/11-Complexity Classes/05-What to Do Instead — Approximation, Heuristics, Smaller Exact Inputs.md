# What to Do Instead — Approximation, Heuristics, Smaller Exact Inputs

#### 1. Definition — Must Know

Once a problem is recognised as NP-Complete (topics 3, 4), there are three practical paths forward, instead of continuing to search for a fast exact algorithm that doesn't exist: **exact solutions for small inputs**, **approximation algorithms** (provably close to optimal, fast), and **heuristics** (fast, reasonable, but no guarantee).

#### 2. Why It Is Used — Must Know

This is the actual, practical payoff of recognising NP-Completeness — it's not a dead end, it's a fork toward the right kind of solution for the actual constraints of the problem in front of you.

#### 3. How It Works — Must Know

```text
1. Exact, for small n:
   n ≤ ~20-25?  → bitmask DP (`05-Dynamic Programming/12`) or
                   backtracking with branch and bound
                   (`06-Backtracking & Branch and Bound/06`)
                   Gives the TRUE optimal answer, just only feasible at small scale.

2. Approximation algorithms:
   Provide a solution with a PROVEN bound on how far it can be from
   optimal (for example, "never more than 2x the true minimum"),
   and run in polynomial time.
   Example: for TSP with the triangle inequality, a minimum-spanning-tree
   based approach gives a route at most 2x the optimal length.

3. Heuristics:
   Fast, practical rules that usually give a good answer, with NO
   mathematical guarantee on how close to optimal it is.
   Examples: nearest-neighbour for TSP (always go to the closest
   unvisited city next), greedy graph coloring (color each node with
   the first available color), simulated annealing, genetic algorithms.
```

#### 4. Algorithm — Must Know

```text
Decision guide:
  Do I need the EXACT optimal answer, and is n small?
      → exact algorithm (bitmask DP / branch and bound)

  Do I need a MATHEMATICAL GUARANTEE on how close to optimal, at larger scale?
      → look for a known approximation algorithm for this problem

  Do I just need something reasonable, fast, with no guarantee needed?
      → a heuristic (nearest-neighbour, greedy, etc.)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// A simple heuristic for TSP: nearest-neighbour. Fast, no optimality guarantee.
fun nearestNeighbourTSP(distances: Array<IntArray>, start: Int): List<Int> {
    val n = distances.size
    val visited = BooleanArray(n)
    val route = mutableListOf(start)
    visited[start] = true
    var current = start
    repeat(n - 1) {
        var nearest = -1
        var nearestDist = Int.MAX_VALUE
        for (next in 0 until n) {
            if (!visited[next] && distances[current][next] < nearestDist) {
                nearest = next
                nearestDist = distances[current][next]
            }
        }
        visited[nearest] = true
        route.add(nearest)
        current = nearest
    }
    return route
}
```

#### 6. Complexity — Must Know

| Approach | Time | Guarantee |
|---|---|---|
| Exact (bitmask DP / branch and bound) | Exponential, only feasible for small n | Optimal |
| Approximation algorithm | Polynomial | Provably within a known factor of optimal |
| Heuristic | Usually fast, polynomial | None — "usually good" |

#### 7. Common Mistakes — Must Know

1. Giving up entirely once a problem is identified as NP-Complete, instead of proposing one of these three practical paths — the identification is the start of the answer, not the end of it.
2. Presenting a heuristic as if it were guaranteed optimal — be explicit that heuristics have no such guarantee, while approximation algorithms do (of a specific, stated factor).
3. Not checking the actual `n` in the problem's constraints before deciding which path fits — this is the same check as in topic 4, and it directly decides which of these three options is appropriate.

#### 8. Related Topics

1. `4` Recognising an NP-Complete Shape in an Interview — the step before this one
2. `06-Backtracking & Branch and Bound/06` Branch and Bound — Tracking a Best-So-Far Bound — the exact, small-n approach
3. `12` Interval DP & Bitmask DP — Names Only (in `05-Dynamic Programming`) — the exact, small-n DP approach

#### 9. Interview Must Remember

1. **Three paths after recognising NP-Completeness:** exact for small n, approximation with a guarantee, or a heuristic with none.
2. Always check `n` first — it decides which of the three actually fits the problem in front of you.
3. This is the strongest possible finish to an NP-Complete-shaped question: name the shape, then propose a concrete, practical way forward.
