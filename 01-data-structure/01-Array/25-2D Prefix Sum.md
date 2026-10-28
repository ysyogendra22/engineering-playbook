# 2D Prefix Sum

#### 1. What Is It?

A **2D prefix sum** is the prefix sum idea for a matrix. `prefix[r][c]` stores the sum of **all cells in the rectangle from the top-left corner to just before `(r, c)`**.

With it, the sum of **any rectangle** is found in `O(1)` using four values.

How to spot it: "sum of a sub-rectangle", "many rectangle queries", "block sums", "count rectangles with a sum".

#### 2. How It Works

Use a prefix matrix with one extra row and column of zeros: `prefix[r + 1][c + 1]` = sum of `matrix[0..r][0..c]`.

**Build it:**

```text
prefix[r+1][c+1] = matrix[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]
                   this cell    + the block above + the block left - the block counted twice
```

**Query the rectangle from `(r1, c1)` to `(r2, c2)`:**

```text
sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
      big rectangle      - the strip above  - the strip left  + the corner removed twice
```

Example: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`

```text
prefix (with the extra row/column of zeros):
0  0   0   0
0  1   3   6
0  5  12  21
0 12  27  45

sum of the 2x2 block rows 1..2, columns 1..2 (5+6+8+9 = 28):
prefix[3][3] - prefix[1][3] - prefix[3][1] + prefix[1][1]
= 45 - 6 - 12 + 1 = 28 ✓
```

Think of it as inclusion-exclusion: take the big rectangle, subtract the two strips, and add back the corner you subtracted twice.

#### 3. Brute Force vs Optimized

| | Brute force | 2D prefix sum |
|---|---|---|
| Each query | loop over the rectangle: `O(R · C)` | `O(1)` |
| Setup | none | `O(R · C)` once |
| `q` queries | `O(q · R · C)` | `O(R · C + q)` |
| Space | `O(1)` extra | `O(R · C)` |

```kotlin
fun regionSumBrute(m: Array<IntArray>, r1: Int, c1: Int, r2: Int, c2: Int): Int {
    var sum = 0
    for (r in r1..r2) for (c in c1..c2) sum += m[r][c]
    return sum
}
```

#### 4. Kotlin Code

```kotlin
// Range Sum Query 2D - Immutable (LeetCode 304)
class NumMatrix(matrix: Array<IntArray>) {
    private val prefix = Array(matrix.size + 1) { IntArray(matrix[0].size + 1) }

    init {
        for (r in matrix.indices) for (c in matrix[0].indices) {
            prefix[r + 1][c + 1] = matrix[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
        }
    }

    fun sumRegion(r1: Int, c1: Int, r2: Int, c2: Int): Int =
        prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]
}

// Matrix Block Sum (LeetCode 1314): for each cell, the sum of the cells within distance k
fun matrixBlockSum(mat: Array<IntArray>, k: Int): Array<IntArray> {
    val rows = mat.size
    val cols = mat[0].size
    val prefix = Array(rows + 1) { IntArray(cols + 1) }
    for (r in 0 until rows) for (c in 0 until cols) {
        prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
    }
    return Array(rows) { r ->
        IntArray(cols) { c ->
            val r1 = maxOf(0, r - k); val c1 = maxOf(0, c - k)
            val r2 = minOf(rows - 1, r + k); val c2 = minOf(cols - 1, c + k)
            prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]
        }
    }
}
```

Checks: `NumMatrix([[1,2,3],[4,5,6],[7,8,9]]).sumRegion(1, 1, 2, 2)` → `28`. `sumRegion(0, 0, 2, 2)` → `45`. `matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1)` → `[[12,21,16],[27,45,33],[24,39,28]]`.

*Number of Submatrices That Sum to Target* (LeetCode 1074, Hard): fix two rows, collapse the columns into a 1D array, then use the 1D "subarray sum equals k" HashMap idea (notes 26).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Build | `O(R · C)` | `O(R · C)` |
| One rectangle query | `O(1)` | `O(1)` |

#### 6. Common Mistakes

1. **Forgetting the `+ prefix[r1][c1]` term** (the corner subtracted twice).
2. **Off-by-one with the extra row and column.** Use `+ 1` consistently.
3. **Mixing up `(row, column)` and `(x, y)`.**
4. **Index out of bounds** at the borders (clamp with `maxOf(0, ...)` and `minOf(size - 1, ...)`).
5. **Overflow.** Use `Long` for big matrices.

#### 7. Say This in the Interview

1. "I build a 2D prefix sum once in `O(R · C)`. Then each rectangle sum is four lookups: the big rectangle minus the strip above, minus the strip on the left, plus the corner."
2. "That is `O(1)` per query instead of `O(R · C)`."

#### 8. Quick Check

1. Why add `prefix[r1][c1]` back in the query?
2. How big is the prefix matrix for a `3 × 4` matrix?

<details>
<summary>Answers</summary>

1. The corner was subtracted twice (once in each strip), so add it once.
2. `4 × 5` (one extra row and one extra column).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 304 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) (Medium) | the base problem |
| 1314 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) (Medium) | a block around each cell |
| 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) (Easy) | the 1D version (note 06) |
| 1074 | [Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) (Hard) | fix rows, then 1D + map |
