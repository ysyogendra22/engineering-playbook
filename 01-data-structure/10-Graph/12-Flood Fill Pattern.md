# Flood Fill Pattern

#### 1. What Is It?

**Flood fill** starts from one cell and **spreads to all connected cells** that satisfy a rule. It is DFS or BFS on a grid (note 11).

It is the idea behind the "paint bucket" tool in a drawing app.

Many interview questions are flood fill with a different goal:

| Goal | Question |
|---|---|
| change the colour of a region | Flood Fill |
| count regions | Number of Islands |
| measure a region | Max Area of Island |
| find regions **not** touching the border | Surrounded Regions, Number of Enclaves |
| find cells that **can reach** the border | Pacific Atlantic Water Flow |

#### 2. How It Works

*Flood Fill* (LeetCode 733): change the colour of the region that contains `(sr, sc)`.

```text
image                      sr=1, sc=1, color=2        result
1 1 1                      start at (1,1), colour 1   2 2 2
1 1 0          →           spread to all connected    2 2 0
1 0 1                      cells with colour 1        2 0 1
```

Notice the bottom-right `1` is **not** connected (it only touches `0` cells), so it stays `1`.

**A very useful trick: start from the border.** *Surrounded Regions* asks to flip every `'O'` region that is **completely surrounded** by `'X'`. It is easier to find the opposite: the `'O'` cells connected to the **border** are safe.

```text
1. Flood fill from every 'O' on the border, marking them 'T' (temporary).
2. Now every remaining 'O' is surrounded → turn it into 'X'.
3. Turn every 'T' back into 'O'.
```

#### 3. Kotlin Code

```kotlin
private val DIRS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

// Flood Fill (LeetCode 733)
fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, color: Int): Array<IntArray> {
    val original = image[sr][sc]
    if (original == color) return image                    // already the new colour: avoids an endless loop
    val rows = image.size
    val cols = image[0].size

    fun dfs(r: Int, c: Int) {
        if (r !in 0 until rows || c !in 0 until cols || image[r][c] != original) return
        image[r][c] = color                                 // the new colour also marks "visited"
        for (d in DIRS) dfs(r + d[0], c + d[1])
    }

    dfs(sr, sc)
    return image
}

// Surrounded Regions (LeetCode 130): start from the border
fun solve(board: Array<CharArray>) {
    if (board.isEmpty()) return
    val rows = board.size
    val cols = board[0].size

    fun dfs(r: Int, c: Int) {
        if (r !in 0 until rows || c !in 0 until cols || board[r][c] != 'O') return
        board[r][c] = 'T'                                   // safe: connected to the border
        for (d in DIRS) dfs(r + d[0], c + d[1])
    }

    for (r in 0 until rows) { dfs(r, 0); dfs(r, cols - 1) }       // left and right borders
    for (c in 0 until cols) { dfs(0, c); dfs(rows - 1, c) }       // top and bottom borders

    for (r in 0 until rows) for (c in 0 until cols) {
        when (board[r][c]) {
            'O' -> board[r][c] = 'X'                        // surrounded
            'T' -> board[r][c] = 'O'                        // restore the safe ones
        }
    }
}

// Number of Enclaves (LeetCode 1020): land cells that cannot reach the border
fun numEnclaves(grid: Array<IntArray>): Int {
    val rows = grid.size
    val cols = grid[0].size

    fun dfs(r: Int, c: Int) {
        if (r !in 0 until rows || c !in 0 until cols || grid[r][c] != 1) return
        grid[r][c] = 0
        for (d in DIRS) dfs(r + d[0], c + d[1])
    }

    for (r in 0 until rows) { dfs(r, 0); dfs(r, cols - 1) }
    for (c in 0 until cols) { dfs(0, c); dfs(rows - 1, c) }
    return grid.sumOf { row -> row.count { it == 1 } }
}
```

Check: `floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)` → `[[2,2,2],[2,2,0],[2,0,1]]`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Flood fill, one region | `O(R · C)` | `O(R · C)` (recursion) |
| Whole-grid versions (Surrounded Regions) | `O(R · C)` | `O(R · C)` |

#### 5. Common Mistakes

1. **Flood fill with the same colour.** If the new colour equals the old one, the DFS never stops marking. Return early.
2. **Checking bounds after the cell.** Check bounds first.
3. **Forgetting a temporary marker** (like `'T'`) in Surrounded Regions, so you cannot tell safe cells from surrounded ones.
4. **Not restoring** the safe cells at the end.
5. **Starting from every cell** instead of from the border, which is slower and harder.
6. **Deep recursion** on a big grid. Use BFS or a stack.

#### 6. Say This in the Interview

1. "I flood fill with DFS: change the cell, then spread to the four neighbours that match."
2. "For 'surrounded' questions I start from the border and mark everything safe. What is left is the answer."
3. "Time and space are `O(R · C)`."

#### 7. Quick Check

1. Why return early when the new colour equals the old colour?
2. In Surrounded Regions, why start from the border?

<details>
<summary>Answers</summary>

1. The cells would never look "different" after being painted, so the DFS would keep going forever.
2. A region is safe only if it touches the border. It is simpler to mark the border-connected cells and treat the rest as surrounded.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 733 | Flood Fill (Easy) | this note |
| 200 | Number of Islands (Medium) | count regions |
| 695 | Max Area of Island (Medium) | size of a region |
| 130 | Surrounded Regions (Medium) | start from the border |
| 1020 | Number of Enclaves (Medium) | start from the border |
| 417 | Pacific Atlantic Water Flow (Medium) | search from each ocean |
