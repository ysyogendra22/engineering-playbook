# Classic Problems — N-Queens, Sudoku, Subset Sum

#### 1. Definition — Must Know

Three of the most commonly referenced backtracking problems, each showing a slightly different shape of "choose, explore, un-choose, with pruning".

#### 2. Why It Is Used — Must Know

Knowing these three by name, and their general shape, lets you quickly map a new, unfamiliar problem onto a pattern you already understand: N-Queens (placement with constraints), Sudoku (fill-in with constraints), Subset Sum (include/exclude choices).

#### 3. How It Works — Must Know

```text
N-Queens:    place one queen per row. At each row, try every column;
             skip (prune) any column attacked by an earlier queen.
             (Full pruning logic in topic 3.)

Sudoku:      find the first empty cell. Try digits 1-9 in it; skip any
             digit that already appears in the same row, column, or 3x3
             box. Recurse into the next empty cell; if a later cell has
             no valid digit, backtrack and try the next digit here.

Subset Sum:  at each number, choose to INCLUDE it or EXCLUDE it from the
             running subset. If the running sum ever exceeds the target,
             prune — no need to keep adding more numbers.
```

#### 4. Algorithm — Must Know

```text
Sudoku (shape):
  function solve():
      cell = findFirstEmptyCell()
      if no empty cell: return true         # solved
      for digit in 1..9:
          if isValid(cell, digit):
              place digit at cell
              if solve(): return true       # keep going
              remove digit from cell         # un-choose, try next digit
      return false                           # no digit worked — backtrack further

Subset Sum (shape):
  function backtrack(index, currentSum):
      if currentSum == target: found a solution; return true
      if currentSum > target or index == n: return false   # prune
      if backtrack(index + 1, currentSum + nums[index]): return true   # include
      if backtrack(index + 1, currentSum): return true                 # exclude
      return false
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun subsetSumExists(nums: IntArray, target: Int): Boolean {
    fun backtrack(index: Int, currentSum: Int): Boolean {
        if (currentSum == target) return true
        if (currentSum > target || index == nums.size) return false   // pruned
        return backtrack(index + 1, currentSum + nums[index]) ||       // include
               backtrack(index + 1, currentSum)                       // exclude
    }
    return backtrack(0, 0)
}
```

#### 6. Complexity — Must Know

| Problem | Complexity (worst case) |
|---|---|
| N-Queens | Much less than O(n^n) with pruning, but still exponential |
| Sudoku | Exponential in the number of empty cells, heavily reduced by constraint checks |
| Subset Sum (backtracking) | O(2ⁿ) — every number is included or excluded |

Note: Subset Sum has a **DP solution** too (`06-Knapsack-Style DP` in `05-Dynamic Programming`), which is faster when the target is small — backtracking here is the straightforward-but-slower version, worth knowing both.

#### 7. Common Mistakes — Must Know

1. Sudoku: forgetting to check the 3×3 box constraint, only checking row and column.
2. N-Queens: recomputing the "is this square attacked" check from scratch each time, instead of tracking attacked columns/diagonals with simple boolean arrays (see the implementation in topic 3).
3. Subset Sum: not pruning when `currentSum > target` (assuming all numbers are positive) — this single check saves a huge amount of unnecessary exploration.

#### 8. Related Topics

1. `1` The Template — Choose, Explore, Un-choose — the shared structure across all three
2. `3` Pruning — Stopping a Branch Early — the N-Queens attack-check logic
3. `06` Knapsack-Style DP (in `05-Dynamic Programming`) — the faster DP version of Subset Sum

#### 9. Interview Must Remember

1. **N-Queens = placement with pruning. Sudoku = fill-in with pruning. Subset Sum = include/exclude with a sum bound.**
2. All three reduce to the same choose/explore/un-choose template — the "valid" check is what differs.
3. Mention when a DP alternative exists and is faster (as with Subset Sum) — it shows you know more than one tool for the same problem.
