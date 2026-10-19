# Maximal Rectangle

#### 1. Definition — Must Know

1. Given a binary matrix of `0`s and `1`s, find the **largest rectangle containing only `1`s** and return its **area**.
2. It is *Maximal Rectangle* (LeetCode 85). If a number and a title ever disagree, trust the title.
3. The method: turn **each row into a histogram** (heights of consecutive `1`s going up) and solve *Largest Rectangle in Histogram* for that row.

#### 2. Why It Is Used — Must Know

1. It is a classic hard problem that becomes simple once you see the reduction to the histogram problem.
2. It shows how to build a new problem from a solved one.
3. It is a frequent follow-up after Largest Rectangle in Histogram.

#### 3. How It Works — Must Know

```text
matrix:               heights after each row (consecutive 1s above, including this row):
1 0 1 0 0             row 0: [1, 0, 1, 0, 0]
1 0 1 1 1             row 1: [2, 0, 2, 1, 1]
1 1 1 1 1             row 2: [3, 1, 3, 2, 2]
1 0 0 1 0             row 3: [4, 0, 0, 3, 0]
```

Height update rule: `heights[c] = if (cell == 1) heights[c] + 1 else 0`.

Largest rectangle in each histogram:

```text
row 0: [1,0,1,0,0]   → 1
row 1: [2,0,2,1,1]   → 3  (the three columns 2..4 with height 1)
row 2: [3,1,3,2,2]   → 6  (columns 2..4 with height 2 → 2 × 3 = 6)  ← best
row 3: [4,0,0,3,0]   → 4

answer = 6
```

Each histogram row is solved with the monotonic stack from the previous note in `O(columns)`.

#### 4. Core Concepts — Must Know

1. **Heights array** of size `cols`, updated row by row.
2. **A `0` cell resets the height to `0`.** A `1` cell adds 1.
3. **After each row,** compute the largest rectangle in that histogram.
4. **The answer is the maximum over all rows.**
5. **Reuse the histogram function** (monotonic stack with a trailing `0` sentinel).
6. **The matrix may be `Array<CharArray>`** (`'0'`/`'1'`), as on LeetCode. Compare with `'1'`.
7. **Other approaches:** DP with left/right/height arrays (also `O(rows × cols)`); brute force over all rectangles is too slow.

| Approach | Time | Space |
|---|---:|---:|
| Brute force | `O(R² · C²)` or worse | `O(1)` |
| **Histogram + stack per row** | **`O(R · C)`** | `O(C)` |
| DP with `left`, `right`, `height` arrays | `O(R · C)` | `O(C)` |

#### 5. Algorithm — Must Know

```text
heights = zeros(cols); best = 0
for each row:
    for each column c:
        heights[c] = (matrix[row][c] == '1') ? heights[c] + 1 : 0
    best = max(best, largestRectangleInHistogram(heights))
return best
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun maximalRectangle(matrix: Array<CharArray>): Int {
    if (matrix.isEmpty()) return 0
    val cols = matrix[0].size
    val heights = IntArray(cols)
    var best = 0

    for (row in matrix) {
        for (c in 0 until cols) {
            heights[c] = if (row[c] == '1') heights[c] + 1 else 0
        }
        best = maxOf(best, largestRectangleArea(heights))
    }
    return best
}

// From "Largest Rectangle in Histogram"
fun largestRectangleArea(heights: IntArray): Int {
    val stack = ArrayDeque<Int>()                           // indexes, heights increasing
    var best = 0
    for (i in 0..heights.size) {
        val h = if (i == heights.size) 0 else heights[i]    // sentinel
        while (stack.isNotEmpty() && heights[stack.last()] >= h) {
            val height = heights[stack.removeLast()]
            val left = if (stack.isEmpty()) -1 else stack.last()
            best = maxOf(best, height * (i - left - 1))
        }
        stack.addLast(i)
    }
    return best
}

// Usage
val matrix = arrayOf(
    charArrayOf('1', '0', '1', '0', '0'),
    charArrayOf('1', '0', '1', '1', '1'),
    charArrayOf('1', '1', '1', '1', '1'),
    charArrayOf('1', '0', '0', '1', '0'),
)
println(maximalRectangle(matrix))     // 6
```

Checks: the matrix above → `6`. `[["0"]]` → `0`. `[["1"]]` → `1`. `[]` → `0`.

#### 7. Time & Space Complexity — Must Know

For `R` rows and `C` columns:

| Part | Cost |
|---|---:|
| Update heights per row | `O(C)` |
| Histogram per row (stack) | `O(C)` |
| **Total time** | **`O(R · C)`** |
| **Space** | `O(C)` for `heights` and the stack |

#### 8. Common Related Patterns — Must Know

1. **Maximal Rectangle** (LeetCode 85).
2. **Largest Rectangle in Histogram** (LeetCode 84) — the building block.
3. **Maximal Square** (LeetCode 221) — DP.
4. **Count Submatrices With All Ones** (LeetCode 1504) — heights + stack counting.
5. **Largest Submatrix With Rearrangements** (LeetCode 1727) — heights + sorting.
6. **Max Area of Island** (LeetCode 695) — connected region, not a rectangle.
7. **Android example:** the largest empty rectangular space on a grid-based layout.

#### 9. Edge Cases / Common Mistakes

1. Not resetting the height to `0` for a `0` cell.
2. Computing the histogram only once at the end instead of after each row.
3. Comparing a `Char` cell with the number `1` (use `'1'`).
4. Forgetting the sentinel in the histogram function.
5. Empty matrix, or an empty first row.
6. Creating a new `heights` array for each row (the heights must carry over).
7. Treating a rectangle that has `0`s inside as valid (the histogram only uses consecutive `1`s).
8. `Int` overflow for huge matrices (use `Long` for the area if needed).

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the largest all-ones rectangle in a binary grid.

**Avoid when:**

1. You need a square (DP is simpler).
2. You need a region of any shape (flood fill / BFS / DFS).

#### 11. Related Topics

1. Largest Rectangle in Histogram
2. Monotonic Stack
3. Dynamic Programming (`02-algorithm/05-Dynamic Programming`)
4. Grid BFS (`01-data-structure/04-Queue/09-Grid BFS.md`)

#### 12. Interview Must Remember

1. **Build heights row by row (`0` resets, `1` adds). Run the histogram solution on every row.**
2. Answer = best over all rows.
3. `O(R · C)` time, `O(C)` space.
4. It is Largest Rectangle in Histogram applied `R` times.
