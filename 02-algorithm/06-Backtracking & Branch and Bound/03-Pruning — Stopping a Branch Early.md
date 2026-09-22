# Pruning — Stopping a Branch Early

#### 1. Definition — Must Know

**Pruning** means stopping the exploration of a branch in the decision tree (topic 2) as soon as you know it cannot lead to a valid or useful answer — instead of exploring it fully and discarding the result afterward.

#### 2. Why It Is Used — Must Know

1. Without pruning, backtracking explores the entire decision tree — often far too slow to finish.
2. With good pruning, the same backtracking template becomes fast enough to solve real problems like N-Queens or Sudoku in practice, even though the worst-case complexity is still exponential.

#### 3. How It Works — Must Know

N-Queens (placing queens so none attack each other) without vs. with pruning:

```text
Without pruning: place all n queens on the board in every possible arrangement
                  (n² choose n ways), THEN check if any arrangement is valid.

With pruning:    place queens one row at a time. Before placing a queen in a
                  column, check if it's attacked by any already-placed queen.
                  If it is, skip that column immediately — don't even recurse
                  into that branch.
```

```text
Row 0: place queen at column 1
Row 1: try column 0 → attacked diagonally? YES → prune, don't recurse
       try column 1 → attacked directly (same column)? YES → prune
       try column 2 → attacked diagonally? YES → prune
       try column 3 → safe → recurse into row 2 with this placement
```

Pruning here cuts off huge parts of the tree the moment a conflict is detected — no need to place all remaining queens first.

#### 4. Algorithm — Must Know

```text
function backtrack(path, choices):
    if path is complete:
        record path
        return
    for each option in choices:
        if NOT isValid(path, option):   # the pruning check
            continue                     # skip this branch immediately
        path.add(option)
        backtrack(path, updated choices)
        path.removeLast()
```

The only change from the plain template (topic 1) is the `isValid` check **before** recursing, instead of after.

#### 5. Kotlin Implementation — Must Know

```kotlin
fun solveNQueens(n: Int): Int {
    var count = 0
    val cols = BooleanArray(n)
    val diag1 = BooleanArray(2 * n)   // row - col + n
    val diag2 = BooleanArray(2 * n)   // row + col

    fun backtrack(row: Int) {
        if (row == n) { count++; return }
        for (col in 0 until n) {
            val d1 = row - col + n
            val d2 = row + col
            if (cols[col] || diag1[d1] || diag2[d2]) continue   // pruned — skip immediately
            cols[col] = true; diag1[d1] = true; diag2[d2] = true
            backtrack(row + 1)
            cols[col] = false; diag1[d1] = false; diag2[d2] = false
        }
    }

    backtrack(0)
    return count
}
```

#### 6. Complexity — Must Know

| | Without pruning | With pruning |
|---|---|---|
| Worst case | Still explores everything | Same worst-case bound, but far fewer branches visited in practice |

Pruning does not change the theoretical worst-case complexity for most problems — it dramatically reduces the *actual* number of nodes visited, which is what makes previously "too slow" problems solvable in practice.

#### 7. Common Mistakes — Must Know

1. Checking validity **after** fully building a path, instead of before recursing into each new choice — this wastes the exact time pruning is meant to save.
2. A pruning check that's more expensive than the work it saves — keep the check itself fast (constant time, ideally).
3. Pruning too aggressively and accidentally cutting off valid answers — the check must only reject branches that are *truly* impossible.

#### 8. Related Topics

1. `1` The Template — Choose, Explore, Un-choose — where the pruning check gets added
2. `2` Modelling Choices as a Decision Tree — helps you see which branches to prune
3. `6` Branch and Bound — Tracking a Best-So-Far Bound — pruning taken further, for optimisation problems

#### 9. Interview Must Remember

1. Prune **before** recursing, not after — check validity as early as possible.
2. Pruning rarely changes the worst-case Big-O, but it's the difference between a solution that finishes and one that doesn't, in practice.
3. Good pruning checks are cheap (O(1) or close to it) — an expensive check can undo the benefit.
