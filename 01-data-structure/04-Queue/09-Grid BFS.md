# Grid BFS

#### 1. What Is It?

**Grid BFS** is BFS on a 2D grid (a matrix). Each cell is a node. Its neighbours are the cells **up, down, left and right** (sometimes also the 4 diagonals).

Typical goals:

- the **shortest path** from one cell to another,
- exploring a **connected region** (islands, flood fill).

Grid problems are everywhere in interviews. They all use the same template.

#### 2. How It Works

For every cell you take out of the queue, look at its neighbours. A neighbour is added only if:

1. it is **inside the grid**,
2. it is **walkable** (not a wall or water),
3. it is **not visited**.

Then mark it visited and add it.

```text
Directions (row change, column change):
  down (1, 0)   up (-1, 0)   right (0, 1)   left (0, -1)
8 directions: every (dr, dc) with dr and dc in -1..1, except (0, 0)
```

*Shortest Path in Binary Matrix* (LeetCode 1091): from the top-left to the bottom-right through `0` cells, moving in 8 directions. Return the number of **cells** on the shortest path.

```text
0 0 0         (0,0) is step 1
1 1 0         (0,1) is step 2
1 1 0         (1,2) is step 3  (diagonal from (0,1))
              (2,2) is step 4  → answer 4
```

Handy tricks:

- **Cell id:** `row * cols + col` is one `Int`. Decode with `/ cols` and `% cols`.
- **Level by level:** increase `steps` after each round of `repeat(queue.size)`.
- **Visited:** a `BooleanArray(rows * cols)`.

#### 3. Kotlin Code

```kotlin
// Shortest Path in Binary Matrix (8 directions, counts cells)
fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
    val n = grid.size
    if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1
    if (n == 1) return 1

    val visited = BooleanArray(n * n)
    val queue = ArrayDeque<Int>()
    queue.addLast(0)
    visited[0] = true
    var steps = 1

    while (queue.isNotEmpty()) {
        repeat(queue.size) {
            val id = queue.removeFirst()
            val r = id / n
            val c = id % n
            for (dr in -1..1) for (dc in -1..1) {
                if (dr == 0 && dc == 0) continue
                val nr = r + dr
                val nc = c + dc
                if (nr in 0 until n && nc in 0 until n && grid[nr][nc] == 0 && !visited[nr * n + nc]) {
                    if (nr == n - 1 && nc == n - 1) return steps + 1
                    visited[nr * n + nc] = true
                    queue.addLast(nr * n + nc)
                }
            }
        }
        steps++
    }
    return -1
}

// A general maze: '#' is a wall. Returns the number of moves, or -1.
fun shortestMaze(maze: Array<CharArray>, sr: Int, sc: Int, tr: Int, tc: Int): Int {
    val rows = maze.size
    val cols = maze[0].size
    if (maze[sr][sc] == '#' || maze[tr][tc] == '#') return -1
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    val dist = Array(rows) { IntArray(cols) { -1 } }           // also the visited marker
    val queue = ArrayDeque<Int>()
    dist[sr][sc] = 0
    queue.addLast(sr * cols + sc)

    while (queue.isNotEmpty()) {
        val id = queue.removeFirst()
        val r = id / cols
        val c = id % cols
        if (r == tr && c == tc) return dist[r][c]
        for (d in dirs) {
            val nr = r + d[0]
            val nc = c + d[1]
            if (nr in 0 until rows && nc in 0 until cols && maze[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1
                queue.addLast(nr * cols + nc)
            }
        }
    }
    return -1
}

// Flood Fill: change the colour of the connected region
fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, color: Int): Array<IntArray> {
    val original = image[sr][sc]
    if (original == color) return image
    val rows = image.size
    val cols = image[0].size
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    val queue = ArrayDeque<Int>()
    image[sr][sc] = color
    queue.addLast(sr * cols + sc)
    while (queue.isNotEmpty()) {
        val id = queue.removeFirst()
        for (d in dirs) {
            val nr = id / cols + d[0]
            val nc = id % cols + d[1]
            if (nr in 0 until rows && nc in 0 until cols && image[nr][nc] == original) {
                image[nr][nc] = color                           // the new colour also marks "visited"
                queue.addLast(nr * cols + nc)
            }
        }
    }
    return image
}
```

Checks: `shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])` → `4`. `[[0,1],[1,0]]` → `2`.

#### 4. Complexity

For `R` rows and `C` columns:

| | Time | Space |
|---|---|---|
| Grid BFS | `O(R · C)` | `O(R · C)` |

#### 5. Common Mistakes

1. **Checking the bounds after reading the cell.** Always check bounds first.
2. **Marking visited when you take the cell out**, not when you add it.
3. **4 versus 8 directions.** Read the question.
4. **Mixing `rows` and `cols`** in the cell id on a non-square grid.
5. **Blocked start or target**, or start equal to target. Handle them before the loop.
6. **Counting cells instead of moves** (or the reverse). A path of 4 cells has 3 moves.
7. **Using DFS for the shortest path.**

#### 6. Say This in the Interview

1. "A grid is a graph. Each cell connects to its 4 (or 8) neighbours, so BFS gives the shortest path."
2. "I use a direction array, check bounds first, and mark cells visited when I add them."
3. "Time and space are `O(R · C)`."

#### 7. Quick Check

1. A path has 5 cells. How many moves is that?
2. What are the 4 direction pairs?

<details>
<summary>Answers</summary>

1. `4` moves.
2. `(1,0)`, `(-1,0)`, `(0,1)`, `(0,-1)`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1091 | Shortest Path in Binary Matrix (Medium) | 8 directions |
| 1926 | Nearest Exit from Entrance in Maze (Medium) | 4 directions |
| 733 | Flood Fill (Easy) | change a region |
| 200 | Number of Islands (Medium) | count regions |
| 695 | Max Area of Island (Medium) | size of a region |
| 130 | Surrounded Regions (Medium) | BFS from the border |
| 994 | Rotting Oranges (Medium) | multi-source BFS (note 08) |
