# Branch and Bound — Tracking a Best-So-Far Bound

#### 1. Definition — Must Know

**Branch and bound** is backtracking used for **optimisation** problems (find the minimum or maximum), with one addition: it keeps track of the best answer found so far (the "bound"), and prunes any branch that provably cannot beat it.

#### 2. Why It Is Used — Must Know

1. Plain backtracking (topic 1) is for "find all valid answers" or "does any valid answer exist". Branch and bound is for "find the *best* answer" — a small but important difference in what you're searching for.
2. It can prune far more aggressively than validity-only pruning (topic 3), because it can reject a branch just for being *worse* than what's already found, not only for being *invalid*.

#### 3. How It Works — Must Know

Example: minimising total cost while exploring a tree of choices.

```text
bestSoFar = infinity

At each node in the search:
  currentCost = cost accumulated so far on this path
  if currentCost >= bestSoFar:
      PRUNE — even if we finish this path perfectly, it can't beat what we
      already have, so there's no point continuing down this branch
  if this is a complete answer:
      bestSoFar = min(bestSoFar, currentCost)
      return
  otherwise, try each next choice and recurse
```

The key extra idea beyond plain pruning: even a path that is still **valid** can be cut off, if it's already too expensive to possibly win.

#### 4. Algorithm — Must Know

```text
bestSoFar = infinity (or -infinity, for maximisation)

function branchAndBound(path, currentCost):
    if currentCost is already worse than bestSoFar:
        return                                  # bound-based prune
    if path is complete:
        bestSoFar = better of (bestSoFar, currentCost)
        return
    for each option:
        path.add(option)
        branchAndBound(path, currentCost + cost of option)
        path.removeLast()
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// Minimise total cost picking one option per step from a small set of choices
fun branchAndBoundMinCost(choicesPerStep: List<List<Int>>): Int {
    var bestSoFar = Int.MAX_VALUE

    fun search(step: Int, currentCost: Int) {
        if (currentCost >= bestSoFar) return          // bound-based prune
        if (step == choicesPerStep.size) {
            bestSoFar = minOf(bestSoFar, currentCost)
            return
        }
        for (cost in choicesPerStep[step]) {
            search(step + 1, currentCost + cost)
        }
    }

    search(0, 0)
    return bestSoFar
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Worst case | Same exponential bound as plain backtracking |
| Typical case | Often far fewer nodes visited, since bad branches are cut off early once a decent `bestSoFar` is found |

The earlier you find a good `bestSoFar`, the more branches you can prune — the order you explore choices in can matter a lot in practice.

#### 7. Common Mistakes — Must Know

1. Forgetting to check the bound **before** recursing further — the whole point is to cut off work early, not after it's already been done.
2. Using `>` instead of `>=` (or vice versa) when comparing against `bestSoFar` — get the boundary condition right for your specific problem (equal-cost paths may or may not need replacing).
3. Not exploring "promising" branches first — a good ordering (try likely-cheap options first) finds a strong `bestSoFar` sooner, which prunes more overall.

#### 8. Related Topics

1. `3` Pruning — Stopping a Branch Early — the validity-only version of this idea
2. `5` Backtracking vs Dynamic Programming — the other tool for optimisation problems
3. `07-Graph Algorithms` (its own folder) — some shortest-path-style problems use a related bounding idea

#### 9. Interview Must Remember

1. Branch and bound = backtracking **plus a running best-so-far value**, used to cut off branches that can't win, not just branches that are invalid.
2. Say the check out loud: **"if this partial path is already worse than my best complete answer, stop exploring it."**
3. It's for optimisation ("find the best"), while plain backtracking (topic 1) is for enumeration or existence ("find all" or "does one exist").
