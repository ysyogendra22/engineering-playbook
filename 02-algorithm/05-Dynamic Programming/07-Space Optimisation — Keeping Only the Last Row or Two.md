# Space Optimisation — Keeping Only the Last Row or Two

#### 1. Definition — Must Know

1. When a DP recurrence for state `i` only depends on a **fixed, small number** of previous states (like `i-1` and `i-2`, or just the row above in a 2D table), you don't need to keep the whole table — only the last one or two rows.
2. This turns O(n) or O(n × m) space into O(1) or O(m), without changing the time complexity at all.

#### 2. Why It Is Used — Must Know

1. It's a common, expected follow-up question after any working DP solution: "can you reduce the space?"
2. It's usually a small, mechanical change once the full-table version already works — a good, safe thing to offer even if not asked.

#### 3. How It Works — Must Know

Fibonacci with a full array vs. two variables:

```text
Full table:  dp = [0, 1, 1, 2, 3, 5, 8, ...]     ← O(n) space
                    ↑ but dp[i] only ever needs dp[i-1] and dp[i-2]

Optimised:   keep only `prev` and `prevPrev`      ← O(1) space
```

For 2D DP (like Grid Paths or LCS), the same idea applies one dimension up:

```text
dp[i][j] only depends on dp[i-1][j], dp[i][j-1], and dp[i-1][j-1]
                           ↑ row above              ↑ same row, earlier column

→ you only ever need the PREVIOUS row and the CURRENT row being built,
  not the entire table.
```

#### 4. Algorithm — Must Know

```text
1D:  replace the array with two (or a fixed few) variables, updated each step
2D:  replace the full table with two 1D arrays: "previous row" and "current row",
     swapping them after each row is filled (or update one row in place,
     if the recurrence allows it)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// House Robber, space-optimised from O(n) to O(1)
fun robOptimised(houses: IntArray): Int {
    var prev = 0       // dp[i - 2]
    var curr = 0       // dp[i - 1]
    for (house in houses) {
        val next = maxOf(curr, prev + house)
        prev = curr
        curr = next
    }
    return curr
}
```

```kotlin
// Unique Paths, space-optimised from O(rows * cols) to O(cols)
fun uniquePathsOptimised(rows: Int, cols: Int): Int {
    var previousRow = IntArray(cols) { 1 }
    repeat(rows - 1) {
        val currentRow = IntArray(cols)
        currentRow[0] = 1
        for (j in 1 until cols) {
            currentRow[j] = currentRow[j - 1] + previousRow[j]
        }
        previousRow = currentRow
    }
    return previousRow[cols - 1]
}
```

#### 6. Complexity — Must Know

| | Before | After |
|---|---|---|
| 1D DP (Fibonacci, House Robber) | O(n) space | O(1) space |
| 2D DP (Grid Paths, LCS) | O(n × m) space | O(m) space (one row) |

Time complexity is **unchanged** in both cases — this optimisation is purely about memory.

#### 7. Common Mistakes — Must Know

1. Updating a variable (or a row, in-place) before you've read the old value you still need — order the updates carefully.
2. Trying to space-optimise before the full-table version is correct — get it right first, then shrink it.
3. Space-optimising a problem that also needs to **reconstruct the actual solution** (topic 9) — you usually can't do both at once, since reconstruction needs the full table (or a separate way to trace back).

#### 8. Related Topics

1. `4` 1D DP — Fibonacci, Climbing Stairs, House Robber — the examples optimised here
2. `5` 2D DP — Grid Paths, Edit Distance, Longest Common Subsequence — the 2D version of this trick
3. `9` Reconstructing the Actual Solution, Not Only Its Value — the case where you can't fully space-optimise

#### 9. Interview Must Remember

1. Ask: **"does state `i` only depend on a fixed number of previous states?"** — if yes, space optimisation is possible.
2. Get the full-table solution correct first, then offer the space-optimised version as a follow-up.
3. If the problem needs to reconstruct the actual path or sequence, say that space optimisation and reconstruction usually trade off against each other.
