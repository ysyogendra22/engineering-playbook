# Grid BFS

#### 1. Definition — Must Know

1. **Grid BFS** is BFS on a 2D grid. Each cell is a node. Its neighbours are the cells **up, down, left and right** (and sometimes the 4 diagonals).
2. The queue holds cells. A `visited` array (or the grid itself) stops repeats.
3. Typical goal: the **shortest path** from a start cell to a target cell, or exploring a connected region.

#### 2. Why It Is Used — Must Know

1. Many interview problems are grids: mazes, islands, flood fill, board games.
2. BFS gives the shortest number of steps when each move costs 1.
3. The same template solves a whole family of problems.

#### 3. How It Works — Must Know

*Shortest Path in Binary Matrix* (LeetCode 1091): from the top-left to the bottom-right through cells that are `0`, moving in 8 directions. Return the number of cells on the shortest path.

```text
0 0 0         steps (cells counted):
1 1 0         (0,0) = 1
1 1 0         (0,1) = 2
              (1,2) = 3   (diagonal from (0,1))
              (2,2) = 4   → answer 4
```

```text
Neighbours of (r, c) in 4 directions:   (r+1,c) (r-1,c) (r,c+1) (r,c-1)
Neighbours in 8 directions: all (r+dr, c+dc) with dr, dc in -1..1, not both 0
```

For each neighbour: **inside the grid? walkable? not visited?** If yes, mark it and enqueue it.

#### 4. Core Concepts — Must Know

1. **Direction array:** `val dirs = arrayOf(intArrayOf(1,0), intArrayOf(-1,0), intArrayOf(0,1), intArrayOf(0,-1))`.
2. **Bounds check first:** `nr in 0 until rows && nc in 0 until cols`.
3. **Cell id:** `r * cols + c` fits in one `Int`, so the queue stores plain numbers. Decode with `/ cols` and `% cols`.
4. **Visited:** a `BooleanArray(rows * cols)` or a 2D array. Or change the grid cell (only if allowed).
5. **Mark visited when you enqueue.**
6. **Level-by-level** gives the step count: `steps++` after each round.
7. **Check the start and the target** cells before the loop (blocked, same cell).
8. **Count cells or moves?** "Number of cells in the path" = moves + 1.

| Problem | Variation |
|---|---|
| Shortest Path in Binary Matrix | 8 directions, walkable `0` |
| Maze / Nearest Exit (LeetCode 1926) | 4 directions, start on the grid |
| Number of Islands (BFS version) | explore a region, no distance |
| Flood Fill (LeetCode 733) | replace colours in a region |
| Rotting Oranges, 01 Matrix | multi-source (previous note) |
| Minimum Knight Moves, Snakes and Ladders | special moves, same BFS |

#### 5. Algorithm — Must Know

```text
if start or target is blocked: no path
queue = [start]; visited[start] = true; steps = 1
while queue is not empty:
    repeat(queue.size):
        cell = removeFirst()
        if cell is the target: return steps
        for each direction:
            nr, nc = neighbour
            if in bounds, walkable, not visited:
                visited = true; addLast
    steps++
return -1
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Shortest Path in Binary Matrix — 8 directions, counts cells
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

// Generic 4-direction shortest path from (sr, sc) to (tr, tc); '#' is a wall
fun shortestMaze(maze: Array<CharArray>, sr: Int, sc: Int, tr: Int, tc: Int): Int {
    val rows = maze.size
    val cols = maze[0].size
    if (maze[sr][sc] == '#' || maze[tr][tc] == '#') return -1
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    val dist = Array(rows) { IntArray(cols) { -1 } }
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

// Flood Fill — change the colour of the connected region
fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, color: Int): Array<IntArray> {
    val original = image[sr][sc]
    if (original == color) return image
    val rows = image.size
    val cols = image[0].size
    val queue = ArrayDeque<Int>()
    image[sr][sc] = color
    queue.addLast(sr * cols + sc)
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    while (queue.isNotEmpty()) {
        val id = queue.removeFirst()
        for (d in dirs) {
            val nr = id / cols + d[0]
            val nc = id % cols + d[1]
            if (nr in 0 until rows && nc in 0 until cols && image[nr][nc] == original) {
                image[nr][nc] = color                         // the new colour also marks "visited"
                queue.addLast(nr * cols + nc)
            }
        }
    }
    return image
}
```

Check: `shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])` → `4`. `[[0,1],[1,0]]` → `2`.

#### 7. Time & Space Complexity — Must Know

For a grid of `R` rows and `C` columns:

| Part | Cost |
|---|---:|
| Time | `O(R · C)` (each cell once, times 4 or 8 directions) |
| Space | `O(R · C)` for visited and the queue |

The queue holds at most about one "frontier" of cells, which can be as large as `O(R + C)` to `O(R · C)`.

#### 8. Common Grid BFS Patterns — Must Know

1. **Shortest Path in Binary Matrix** (LeetCode 1091).
2. **Nearest Exit from Entrance in Maze** (LeetCode 1926).
3. **Number of Islands** (LeetCode 200) — BFS or DFS; see `01-data-structure/06-HashSet/10-Visited - Seen Pattern.md`.
4. **Flood Fill** (LeetCode 733), **Max Area of Island** (LeetCode 695).
5. **Surrounded Regions** (LeetCode 130) — BFS from the border.
6. **Rotting Oranges / 01 Matrix** — multi-source BFS.
7. **Minimum steps with keys or obstacles** — add extra state to the cell.
8. **Android example:** pathfinding on a tile map in a game.

#### 9. Edge Cases / Common Mistakes

1. Bounds check after reading the grid (index error). Check bounds first.
2. Marking visited when taking from the queue, not when adding.
3. Forgetting the 4 vs 8 direction rule.
4. Mixing up `rows` and `cols` in the id (`r * cols + c`). On a non-square grid this gives wrong cells.
5. Blocked start or target; start equals target.
6. Returning steps in the wrong unit (cells vs moves).
7. Using DFS for the shortest path.
8. Changing the input grid when the caller needs it.
9. Recursion depth: a DFS flood fill on a large grid can overflow the stack. BFS with a queue does not.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the fewest moves on a grid with equal-cost moves.
2. You explore connected regions without recursion.

**Avoid when:**

1. Cells have different costs (Dijkstra) or costs 0/1 (0-1 BFS).
2. You need all paths (backtracking).

#### 11. Related Topics

1. BFS
2. Multi-Source BFS
3. Queue for Shortest Path
4. Grid as graph (`01-data-structure/10-Graph/11-Grid as Graph.md`)
5. Flood fill (`01-data-structure/10-Graph/12-Flood Fill Pattern.md`)

#### 12. Interview Must Remember

1. **Direction array + bounds check + visited + queue.**
2. Cell id `r * cols + c`. Mark visited when you enqueue.
3. `steps++` per level; count cells vs moves carefully.
4. `O(R · C)` time and space. Use BFS, not DFS, for shortest paths.
