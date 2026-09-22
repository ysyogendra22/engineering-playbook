# Backtracking vs Dynamic Programming

#### 1. Definition — Must Know

1. **Backtracking** explores every valid path through a decision tree, undoing choices as it goes — it does not remember or reuse work from other branches.
2. **Dynamic Programming** solves a problem by combining answers to smaller, **repeated** subproblems, caching each one so it's never solved twice.
3. Both are recursive, and both explore choices — the difference is whether the same smaller subproblem comes up more than once.

#### 2. Why It Is Used — Must Know

Recognising which one a problem needs (or if it needs both) is a common point of confusion — a problem that looks like backtracking sometimes has hidden overlapping subproblems, in which case DP (or a DP layer added on top of backtracking) is the faster fix.

#### 3. How It Works — Must Know

```text
Backtracking example: generate all subsets of [1, 2, 3]
  Each subset is a DIFFERENT answer — there's no smaller "subproblem" that
  repeats across branches. Nothing to cache.

DP example: Fibonacci
  fib(3) is needed by BOTH fib(5)'s and fib(4)'s call trees — it's the SAME
  subproblem, computed the same way, reused. Caching it helps enormously.

Backtracking + DP together: counting the number of DISTINCT paths through a
  grid with obstacles, where many different partial paths reach the SAME cell.
  Reaching cell (i, j) is a repeated subproblem — worth caching (this becomes
  Grid Paths DP, see `05-Dynamic Programming/05`), even though the underlying
  exploration is the same shape as backtracking.
```

#### 4. Algorithm — Must Know

```text
Ask: "if I solve this recursively, does the exact same smaller call
      (same inputs) happen more than once?"

NO  → this is pure backtracking (topic 1) — no caching helps, since every
      call explores genuinely different territory
YES → this has overlapping subproblems (see `05-Dynamic Programming/01`) —
      add memoization, and it becomes (or gains) a DP solution
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// Pure backtracking — every path is a distinct answer, nothing to cache
fun subsets(nums: IntArray): List<List<Int>> { /* see `01-The Template` */ TODO() }

// Backtracking WITH overlapping subproblems — worth memoizing
// (counting paths to the end of a grid; many paths pass through the same cell)
fun countPaths(row: Int, col: Int, rows: Int, cols: Int,
               cache: MutableMap<Pair<Int, Int>, Int> = mutableMapOf()): Int {
    if (row == rows - 1 || col == cols - 1) return 1
    val key = row to col
    cache[key]?.let { return it }
    val result = countPaths(row + 1, col, rows, cols, cache) +
                 countPaths(row, col + 1, rows, cols, cache)
    cache[key] = result
    return result
}
```

#### 6. Complexity — Must Know

| | Backtracking (no repeats) | DP (with repeats, cached) |
|---|---|---|
| Time | Exponential/factorial — proportional to the number of leaves | Polynomial — proportional to the number of *distinct* states |

#### 7. Common Mistakes — Must Know

1. Trying to memoize pure backtracking problems (like generating all subsets) — there's nothing to cache, since each result is genuinely distinct; memoization adds overhead for no benefit.
2. Missing that a backtracking-shaped problem actually has repeated subproblems, and leaving a slow exponential solution when a DP fix was available (this is one of the most common "why is my solution too slow" interview moments).
3. Confusing "explores many paths" (true of both) with "repeats the same subproblem" (true of only one) — these are different things.

#### 8. Related Topics

1. `1` Optimal Substructure & Overlapping Subproblems (in `05-Dynamic Programming`) — the exact check to run
2. `1` The Template — Choose, Explore, Un-choose — the shared recursive shape
3. `5` 2D DP — Grid Paths, Edit Distance, Longest Common Subsequence (in `05-Dynamic Programming`) — the grid-paths example used here

#### 9. Interview Must Remember

1. **"Does the same subproblem repeat?"** is the one question that tells them apart.
2. If a "generate all ___" problem is timing out, check whether it's secretly counting/optimising over repeated states — that's your cue to add memoization.
3. Pure enumeration (list every subset/permutation) never benefits from caching — every answer is unique by definition.
