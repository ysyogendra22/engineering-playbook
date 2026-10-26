# Grid as Graph

> A very common FAANG pattern. A 2D grid is a graph that you do not have to build.

#### 1. What Is It?

A 2D grid (matrix) is a graph:

- each **cell** is a **vertex**,
- two cells are connected if they are **neighbours**: up, down, left, right (sometimes also the 4 diagonals).

You do not build an adjacency list. You **compute the neighbours** from the row and the column.

So all graph tools work on a grid: DFS, BFS, shortest path, connected components, multi-source BFS, Dijkstra.

#### 2. How It Works

For the cell `(r, c)`, the neighbours are:

```text
          (r-1, c)
(r, c-1)   (r, c)   (r, c+1)
          (r+1, c)
```

In code, use a **direction array**:

```kotlin
val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
```

Every neighbour check has the same three parts:

1. **Is it inside the grid?** `nr in 0 until rows && nc in 0 until cols` (check this **first**).
2. **Is it allowed?** (land, not a wall, same colour...)
3. **Is it unvisited?**

Handy tricks:

- **Cell id:** `r * cols + c` is a single `Int`. Decode with `id / cols` and `id % cols`.
- **Mark visited** with a `BooleanArray`, or by **changing the cell** (e.g. `'1'` → `'0'`) if you may modify the input.

Which walk:

| Question | Use |
|---|---|
| count / mark regions, flood fill | DFS or BFS |
| shortest path (each move costs 1) | BFS |
| spread from many cells at once | multi-source BFS |
| cells have different costs | Dijkstra |

#### 3. Kotlin Code

```kotlin
private val DIRS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

// Number of Islands (LeetCode 200): count connected groups of '1'
fun numIslands(grid: Array<CharArray>): Int {
    if (grid.isEmpty()) return 0
    val rows = grid.size
    val cols = grid[0].size

    fun dfs(r: Int, c: Int) {
        if (r !in 0 until rows || c !in 0 until cols || grid[r][c] != '1') return
        grid[r][c] = '0'                                    // mark visited
        for (d in DIRS) dfs(r + d[0], c + d[1])
    }

    var islands = 0
    for (r in 0 until rows) for (c in 0 until cols) {
        if (grid[r][c] == '1') {
            islands++
            dfs(r, c)
        }
    }
    return islands
}

// The same with BFS and a visited array (does not change the input, no deep recursion)
fun numIslandsBfs(grid: Array<CharArray>): Int {
    if (grid.isEmpty()) return 0
    val rows = grid.size
    val cols = grid[0].size
    val visited = BooleanArray(rows * cols)
    var islands = 0
    for (r in 0 until rows) for (c in 0 until cols) {
        if (grid[r][c] == '1' && !visited[r * cols + c]) {
            islands++
            val queue = ArrayDeque<Int>()
            visited[r * cols + c] = true
            queue.addLast(r * cols + c)
            while (queue.isNotEmpty()) {
                val id = queue.removeFirst()
                for (d in DIRS) {
                    val nr = id / cols + d[0]
                    val nc = id % cols + d[1]
                    if (nr in 0 until rows && nc in 0 until cols &&
                        grid[nr][nc] == '1' && !visited[nr * cols + nc]
                    ) {
                        visited[nr * cols + nc] = true
                        queue.addLast(nr * cols + nc)
                    }
                }
            }
        }
    }
    return islands
}

// Island Perimeter (LeetCode 463): count the sides of land cells that touch water or the edge
fun islandPerimeter(grid: Array<IntArray>): Int {
    val rows = grid.size
    val cols = grid[0].size
    var perimeter = 0
    for (r in 0 until rows) for (c in 0 until cols) {
        if (grid[r][c] == 1) {
            for (d in DIRS) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr !in 0 until rows || nc !in 0 until cols || grid[nr][nc] == 0) perimeter++
            }
        }
    }
    return perimeter
}
```

Checks: `numIslands` on `["11000","11000","00100","00011"]` → `3`. `islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])` → `16`.

#### 4. Complexity

For `R` rows and `C` columns:

| | Time | Space |
|---|---|---|
| DFS or BFS over the grid | `O(R · C)` | `O(R · C)` worst case |

#### 5. Common Mistakes

1. **Checking the bounds after reading the cell.** You get an index error. Check bounds first.
2. **Not marking visited** before going deeper. DFS goes back and forth forever.
3. **Mixing `rows` and `cols`** in the cell id on a non-square grid.
4. **4 versus 8 directions.** Read the question.
5. **Comparing a `Char` cell with a number** (`grid[r][c] == 1` when it is `'1'`).
6. **Deep recursion** on a big grid (`StackOverflowError`). Use BFS or an explicit stack.
7. **Changing the input** when the caller still needs it.

#### 6. Say This in the Interview

1. "I treat the grid as a graph. Each cell connects to its 4 neighbours, which I compute with a direction array."
2. "I check bounds first, then the cell value, then visited."
3. "Time and space are `O(R · C)`. For fewest steps I use BFS; for regions DFS or BFS."

#### 7. Quick Check

1. What are the four direction pairs?
2. Why do you check the bounds before reading `grid[nr][nc]`?

<details>
<summary>Answers</summary>

1. `(1,0)`, `(-1,0)`, `(0,1)`, `(0,-1)`.
2. If `nr` or `nc` is outside the grid, reading the cell throws an index error.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 200 | Number of Islands (Medium) | count regions |
| 695 | Max Area of Island (Medium) | size of a region |
| 463 | Island Perimeter (Easy) | count borders |
| 733 | Flood Fill (Easy) | change a region (note 12) |
| 1091 | Shortest Path in Binary Matrix (Medium) | BFS shortest path |
| 994 | Rotting Oranges (Medium) | multi-source BFS |
| 417 | Pacific Atlantic Water Flow (Medium) | search from the borders |
| 79 | Word Search (Medium) | grid DFS + backtracking |
