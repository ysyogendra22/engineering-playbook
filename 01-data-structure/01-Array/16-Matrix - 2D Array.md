# Matrix / 2D Array

> Matrix questions test careful indexing. The patterns are few: traverse, rotate, spiral, and set/search.

#### 1. What Is It?

A **matrix** (2D array) is an array of rows. `matrix[r][c]` is the item in row `r` and column `c`. A matrix with `R` rows and `C` columns has `R × C` items.

```text
        c=0 c=1 c=2
r=0   [  1   2   3 ]
r=1   [  4   5   6 ]
r=2   [  7   8   9 ]
```

Three common tasks:

| Task | Idea |
|---|---|
| **Traversal** | nested loops; or walk diagonals / in a spiral |
| **Rotation** (90° clockwise) | **transpose**, then **reverse each row** |
| **Spiral order** | four moving borders: top, bottom, left, right |

Many matrix questions are really graph questions (islands, shortest path). Those are in the Graph folder.

#### 2. How It Works

**Rotate 90° clockwise in place** (`n × n`):

```text
1 2 3        transpose (swap [i][j] with [j][i])       reverse each row
4 5 6   →    1 4 7                               →     7 4 1
7 8 9        2 5 8                                     8 5 2
             3 6 9                                     9 6 3
```

(To rotate counter-clockwise, reverse each row first, then transpose, or transpose and reverse the columns.)

**Spiral order** with four borders:

```text
go right along the top row, then top++
go down along the right column, then right--
go left along the bottom row, then bottom--      (only if top <= bottom)
go up along the left column, then left++         (only if left <= right)
repeat while top <= bottom and left <= right

[[1,2,3],[4,5,6],[7,8,9]]  →  1 2 3 6 9 8 7 4 5
```

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Rotate | build a new matrix: `new[c][n - 1 - r] = old[r][c]` | transpose + reverse rows, in place |
| Time | `O(n²)` | `O(n²)` |
| Space | `O(n²)` | `O(1)` |

```kotlin
fun rotateWithCopy(matrix: Array<IntArray>) {
    val n = matrix.size
    val copy = Array(n) { matrix[it].copyOf() }
    for (r in 0 until n) for (c in 0 until n) matrix[c][n - 1 - r] = copy[r][c]
}
```

#### 4. Kotlin Code

```kotlin
// Rotate Image (LeetCode 48): in place
fun rotate(matrix: Array<IntArray>) {
    val n = matrix.size
    for (i in 0 until n) for (j in i + 1 until n) {              // 1. transpose
        val t = matrix[i][j]; matrix[i][j] = matrix[j][i]; matrix[j][i] = t
    }
    for (row in matrix) row.reverse()                             // 2. reverse every row
}

// Spiral Matrix (LeetCode 54)
fun spiralOrder(matrix: Array<IntArray>): List<Int> {
    val result = mutableListOf<Int>()
    var top = 0
    var bottom = matrix.size - 1
    var left = 0
    var right = matrix[0].size - 1
    while (top <= bottom && left <= right) {
        for (c in left..right) result.add(matrix[top][c]); top++
        for (r in top..bottom) result.add(matrix[r][right]); right--
        if (top <= bottom) { for (c in right downTo left) result.add(matrix[bottom][c]); bottom-- }
        if (left <= right) { for (r in bottom downTo top) result.add(matrix[r][left]); left++ }
    }
    return result
}

// Set Matrix Zeroes (LeetCode 73): if an item is 0, set its whole row and column to 0
fun setZeroes(matrix: Array<IntArray>) {
    val rows = BooleanArray(matrix.size)
    val cols = BooleanArray(matrix[0].size)
    for (r in matrix.indices) for (c in matrix[0].indices) {
        if (matrix[r][c] == 0) { rows[r] = true; cols[c] = true }          // 1. remember
    }
    for (r in matrix.indices) for (c in matrix[0].indices) {
        if (rows[r] || cols[c]) matrix[r][c] = 0                            // 2. then change
    }
}

// Search a 2D Matrix II (LeetCode 240): rows and columns sorted. Start at the top-right.
fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
    var r = 0
    var c = matrix[0].size - 1
    while (r < matrix.size && c >= 0) {
        when {
            matrix[r][c] == target -> return true
            matrix[r][c] > target -> c--          // too big: move left
            else -> r++                           // too small: move down
        }
    }
    return false
}

// Transpose Matrix (LeetCode 867): any R x C shape
fun transpose(matrix: Array<IntArray>): Array<IntArray> {
    val rows = matrix.size
    val cols = matrix[0].size
    return Array(cols) { c -> IntArray(rows) { r -> matrix[r][c] } }
}
```

Checks: `rotate([[1,2,3],[4,5,6],[7,8,9]])` → `[[7,4,1],[8,5,2],[9,6,3]]`. `spiralOrder([[1,2,3],[4,5,6],[7,8,9]])` → `[1,2,3,6,9,8,7,4,5]`. `searchMatrix([[1,4,7],[2,5,8],[3,6,9]], 5)` → `true`.

`setZeroes` above uses `O(R + C)` extra space. An `O(1)` version uses the first row and column as markers.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Traverse / rotate / spiral / transpose | `O(R · C)` | `O(1)` extra (the output list excluded) |
| Set Matrix Zeroes | `O(R · C)` | `O(R + C)` |
| Search II (staircase) | `O(R + C)` | `O(1)` |

#### 6. Common Mistakes

1. **Mixing up rows and columns** (`matrix.size` is rows, `matrix[0].size` is columns).
2. **Spiral:** not checking `top <= bottom` and `left <= right` before the last two loops. A single row or column repeats items.
3. **Transpose swapping the whole matrix** (both `[i][j]` and `[j][i]` twice). Swap only for `j > i`.
4. **Setting zeroes while scanning**, which creates new zeroes you then wrongly spread.
5. **Empty matrix** (`matrix[0]` crashes).
6. **Copying a row reference** (`val b = a`). Use `copyOf()`.

#### 7. Say This in the Interview

1. "To rotate in place I transpose, then reverse each row. That is `O(n²)` time and `O(1)` space."
2. "For spiral order I keep four borders and shrink them after each side."
3. "I will check an empty matrix, a single row and a single column."

#### 8. Quick Check

1. How many items does a `3 × 4` matrix have?
2. How do you get `matrix[r][c]` into the new place after rotating clockwise?

<details>
<summary>Answers</summary>

1. `12`.
2. It goes to `new[c][n - 1 - r]`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 867 | [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) (Easy) | swap rows and columns |
| 566 | [Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/) (Easy) | index = `r * cols + c` |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) (Medium) | transpose + reverse |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) (Medium) | four borders |
| 59 | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) (Medium) | fill in a spiral |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) (Medium) | remember, then change |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (Medium) | binary search on a flat index |
| 240 | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) (Medium) | staircase from the top-right |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) (Medium) | sets for rows, columns, boxes |
