# Maximal Rectangle

#### 1. What Is It?

You get a grid of `0`s and `1`s. Find the **largest rectangle that contains only `1`s** and return its area.

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1       ← the rectangle of 1s in rows 1–2 and columns 2–4 has area 2 × 3 = 6
1 0 0 1 0
```

This is *Maximal Rectangle* (LeetCode 85), a Hard question. The trick is simple once you know *Largest Rectangle in Histogram* (note 11):

> **Turn every row into a histogram, then solve the histogram problem for that row.**

#### 2. How It Works

For each row, make an array `heights`. `heights[c]` is the number of `1`s in a row going **up** from this cell (including this cell). A `0` resets the height to `0`.

```text
matrix:               heights after each row:
1 0 1 0 0             row 0: [1, 0, 1, 0, 0]
1 0 1 1 1             row 1: [2, 0, 2, 1, 1]
1 1 1 1 1             row 2: [3, 1, 3, 2, 2]
1 0 0 1 0             row 3: [4, 0, 0, 3, 0]
```

Update rule: `heights[c] = if (cell == '1') heights[c] + 1 else 0`.

Biggest rectangle in each histogram:

```text
row 0: [1,0,1,0,0] → 1
row 1: [2,0,2,1,1] → 3   (three columns at height 1)
row 2: [3,1,3,2,2] → 6   (columns 2–4 at height 2 → 2 × 3)   ← best
row 3: [4,0,0,3,0] → 4

answer = 6
```

#### 3. Kotlin Code

```kotlin
fun maximalRectangle(matrix: Array<CharArray>): Int {
    if (matrix.isEmpty()) return 0
    val cols = matrix[0].size
    val heights = IntArray(cols)                      // carries over from row to row
    var best = 0

    for (row in matrix) {
        for (c in 0 until cols) {
            heights[c] = if (row[c] == '1') heights[c] + 1 else 0
        }
        best = maxOf(best, largestRectangleArea(heights))
    }
    return best
}

// From note 11: Largest Rectangle in Histogram
fun largestRectangleArea(heights: IntArray): Int {
    val stack = ArrayDeque<Int>()                     // indexes, heights increasing
    var best = 0
    for (i in 0..heights.size) {
        val h = if (i == heights.size) 0 else heights[i]
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

Checks: the matrix above → `6`. `[['0']]` → `0`. `[['1']]` → `1`. `[]` → `0`.

#### 4. Complexity

For `R` rows and `C` columns:

| | Time | Space |
|---|---|---|
| Heights + stack per row | `O(R · C)` | `O(C)` |
| Brute force | far too slow | — |

#### 5. Common Mistakes

1. **Not resetting the height to `0`** when the cell is `0`.
2. **Creating a new `heights` array for every row.** The heights must carry over.
3. **Solving the histogram only once at the end.** Do it after **every** row.
4. **Comparing the cell with the number `1`** when it is a character. Use `'1'`.
5. **Missing the extra height-`0` bar** inside the histogram function.
6. **Empty matrix.**

#### 6. Say This in the Interview

1. "I treat each row as the base of a histogram. `heights[c]` counts consecutive 1s going up."
2. "For every row I run the stack solution for Largest Rectangle in Histogram and keep the best."
3. "Time `O(R · C)`, space `O(C)`."

#### 7. Quick Check

1. What is `heights` after row 1 if row 0 is `[1, 1]` and row 1 is `[1, 0]`?
2. Why do we reset a height to `0` for a `0` cell?

<details>
<summary>Answers</summary>

1. `[2, 0]`.
2. A `0` breaks the column of `1`s. A rectangle cannot go through it.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 84 | Largest Rectangle in Histogram (Hard) | the building block |
| 85 | Maximal Rectangle (Hard) | this note |
| 221 | Maximal Square (Medium) | dynamic programming |
| 1504 | Count Submatrices With All Ones (Medium) | heights + counting |
| 1727 | Largest Submatrix With Rearrangements (Medium) | heights + sorting |
