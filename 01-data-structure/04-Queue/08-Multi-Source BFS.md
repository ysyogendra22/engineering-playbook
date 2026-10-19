# Multi-Source BFS

#### 1. Definition — Must Know

1. **Multi-source BFS** starts the search from **many starting nodes at the same time**.
2. Put **all sources in the queue at distance 0** before the loop begins. BFS then spreads outward from all of them together.
3. The first time a cell is reached, it gets the distance to its **nearest source**.

#### 2. Why It Is Used — Must Know

1. "Distance to the nearest X" for every cell would take `O(cells × sources)` if you ran BFS from each cell. One multi-source BFS does it in `O(cells)`.
2. It models things that spread at the same time: rot, fire, water, signal, infection.
3. Classic problems: Rotting Oranges, 01 Matrix, Walls and Gates, As Far from Land as Possible.

#### 3. How It Works — Must Know

*01 Matrix* (LeetCode 542): for each cell, the distance to the nearest `0`.

```text
input            distance
0 0 0            0 0 0
0 1 0     →      0 1 0
1 1 1            1 2 1

Start: queue = every cell that is 0, with distance 0.
Round 1: neighbours of the 0s that are still unknown get distance 1.
Round 2: their neighbours get distance 2.
```

*Rotting Oranges* (LeetCode 994): each minute, fresh oranges next to a rotten one become rotten. The queue starts with **all** rotten oranges; each round is one minute.

```text
2 1 1          minute 0: rotten at (0,0)
1 1 0
0 1 1

minute 1: (0,1) and (1,0) rot
minute 2: (0,2) and (1,1) rot
minute 3: (2,1) rots
minute 4: (2,2) rots          → answer 4
```

#### 4. Core Concepts — Must Know

1. **Seed the queue with all sources** (distance 0).
2. **Distance array filled with `-1`** (unknown). It doubles as the visited marker.
3. **Process level by level** if you need the number of rounds (minutes). Otherwise store the distance per cell.
4. **Count what is left** (fresh oranges). If any remain at the end, some cells are unreachable.
5. **Same code as normal BFS.** Only the starting queue changes.
6. **Sources of different kinds** (several colours of spread) can be done by running the BFS once with extra data, or once per kind.
7. **Reverse thinking:** instead of "from each cell to the nearest target", start from the targets.

| Problem | Sources | Spreads into |
|---|---|---|
| Rotting Oranges | rotten oranges | fresh oranges |
| 01 Matrix | all `0` cells | `1` cells |
| Walls and Gates | all gates | empty rooms |
| Map of Highest Peak (LeetCode 1765) | water cells | land cells |
| As Far from Land as Possible (LeetCode 1162) | land cells | water cells |
| Pacific Atlantic Water Flow | ocean border cells | uphill cells |

#### 5. Algorithm — Must Know

```text
queue = all source cells; mark them visited (distance 0)
while queue is not empty:
    repeat(queue.size):        // one round = one unit of time / distance
        cell = removeFirst()
        for each neighbour that is valid and not visited:
            mark visited; set distance = distance(cell) + 1; addLast(neighbour)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
private val DIRS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

// 01 Matrix — distance to the nearest 0
fun updateMatrix(mat: Array<IntArray>): Array<IntArray> {
    val rows = mat.size
    val cols = mat[0].size
    val dist = Array(rows) { IntArray(cols) { -1 } }
    val queue = ArrayDeque<Int>()                          // cell id = row * cols + col

    for (r in 0 until rows) for (c in 0 until cols) {
        if (mat[r][c] == 0) {
            dist[r][c] = 0
            queue.addLast(r * cols + c)
        }
    }

    while (queue.isNotEmpty()) {
        val id = queue.removeFirst()
        val r = id / cols
        val c = id % cols
        for (d in DIRS) {
            val nr = r + d[0]
            val nc = c + d[1]
            if (nr in 0 until rows && nc in 0 until cols && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1
                queue.addLast(nr * cols + nc)
            }
        }
    }
    return dist
}

// Rotting Oranges — minutes until no fresh orange remains, or -1
fun orangesRotting(grid: Array<IntArray>): Int {
    val rows = grid.size
    val cols = grid[0].size
    val queue = ArrayDeque<Int>()
    var fresh = 0

    for (r in 0 until rows) for (c in 0 until cols) {
        when (grid[r][c]) {
            2 -> queue.addLast(r * cols + c)
            1 -> fresh++
        }
    }

    var minutes = 0
    while (queue.isNotEmpty() && fresh > 0) {
        repeat(queue.size) {
            val id = queue.removeFirst()
            val r = id / cols
            val c = id % cols
            for (d in DIRS) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr in 0 until rows && nc in 0 until cols && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2                       // marks it rotten and visited
                    fresh--
                    queue.addLast(nr * cols + nc)
                }
            }
        }
        minutes++
    }
    return if (fresh == 0) minutes else -1
}
```

Checks: `orangesRotting([[2,1,1],[1,1,0],[0,1,1]])` → `4`. `updateMatrix([[0,0,0],[0,1,0],[1,1,1]])` → `[[0,0,0],[0,1,0],[1,2,1]]`.

`orangesRotting` changes the input grid. Copy it first if the caller needs it unchanged.

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---:|
| Time | `O(R · C)` — each cell enters the queue once |
| Space | `O(R · C)` |
| Running BFS from every cell separately | `O((R · C)²)` |

#### 8. Common Multi-Source Patterns — Must Know

1. **Rotting Oranges** (LeetCode 994).
2. **01 Matrix** (LeetCode 542).
3. **Walls and Gates** (LeetCode 286, premium).
4. **As Far from Land as Possible** (LeetCode 1162).
5. **Map of Highest Peak** (LeetCode 1765).
6. **Shortest Bridge** (LeetCode 934) — DFS to find one island, then multi-source BFS from it.
7. **Pacific Atlantic Water Flow** (LeetCode 417) — BFS from each ocean's border.
8. **Time for a message/virus to reach everyone.**

#### 9. Edge Cases / Common Mistakes

1. Running a separate BFS from every source. It is too slow.
2. Pushing sources into the queue but forgetting to mark them visited.
3. Starting at minute `1` instead of `0`, or adding an extra minute after the last spread (the loop stops when `fresh == 0`).
4. No sources at all. For Rotting Oranges with no fresh oranges the answer is `0`; with fresh but no rotten, `-1`.
5. Unreachable cells (blocked by walls). Check for leftovers.
6. Not checking grid bounds.
7. Changing the input grid when the caller needs it.
8. Counting rounds when the problem asks for distance per cell (or the reverse).

#### 10. When to Use / When Not to Use

**Use when:**

1. Many sources spread at the same speed, or you need the nearest source for every cell.

**Avoid when:**

1. You have one source (normal BFS).
2. Move costs differ (Dijkstra with several sources in the heap).

#### 11. Related Topics

1. BFS
2. Grid BFS
3. Level-by-Level Processing
4. Grid as graph (`01-data-structure/10-Graph/11-Grid as Graph.md`)

#### 12. Interview Must Remember

1. **Put all sources in the queue first, at distance 0.**
2. One BFS gives the nearest-source distance for every cell: `O(cells)`.
3. Levels = time rounds. Track the count of fresh/unreached cells.
4. Same BFS code, different starting queue.
