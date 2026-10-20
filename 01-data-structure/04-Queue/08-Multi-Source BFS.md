# Multi-Source BFS

#### 1. What Is It?

Normal BFS starts from **one** node. **Multi-source BFS** starts from **many nodes at the same time**.

Before the loop, put **all the sources in the queue at distance 0**. BFS then spreads out from all of them together. The first time a cell is reached, it gets the distance to its **nearest source**.

Why it matters: "distance to the nearest X for every cell" would be slow if you ran a BFS from every cell. One multi-source BFS does it in `O(cells)`.

It fits things that **spread at the same time**: rot, fire, water, a virus, a signal.

#### 2. How It Works

**01 Matrix** (LeetCode 542): for each cell, the distance to the nearest `0`.

```text
input            answer
0 0 0            0 0 0
0 1 0     →      0 1 0
1 1 1            1 2 1

Start: the queue holds every cell that is 0, with distance 0.
Round 1: unknown neighbours of the 0s get distance 1.
Round 2: their unknown neighbours get distance 2.
```

**Rotting Oranges** (LeetCode 994): every minute, fresh oranges next to a rotten one become rotten. The queue starts with **all** rotten oranges. One round of BFS = one minute.

```text
2 1 1         minute 0: rotten at (0,0)
1 1 0         minute 1: (0,1) and (1,0) rot
0 1 1         minute 2: (0,2) and (1,1) rot
              minute 3: (2,1) rots
              minute 4: (2,2) rots        → answer 4
```

#### 3. Kotlin Code

```kotlin
private val DIRS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

// 01 Matrix: distance to the nearest 0
fun updateMatrix(mat: Array<IntArray>): Array<IntArray> {
    val rows = mat.size
    val cols = mat[0].size
    val dist = Array(rows) { IntArray(cols) { -1 } }          // -1 = not reached yet
    val queue = ArrayDeque<Int>()                              // cell id = row * cols + col

    for (r in 0 until rows) for (c in 0 until cols) {
        if (mat[r][c] == 0) {                                  // every source goes in first
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

// Rotting Oranges: minutes until no fresh orange is left, or -1
fun orangesRotting(grid: Array<IntArray>): Int {
    val rows = grid.size
    val cols = grid[0].size
    val queue = ArrayDeque<Int>()
    var fresh = 0

    for (r in 0 until rows) for (c in 0 until cols) {
        when (grid[r][c]) {
            2 -> queue.addLast(r * cols + c)                   // rotten: a source
            1 -> fresh++
        }
    }

    var minutes = 0
    while (queue.isNotEmpty() && fresh > 0) {
        repeat(queue.size) {                                   // one round = one minute
            val id = queue.removeFirst()
            val r = id / cols
            val c = id % cols
            for (d in DIRS) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr in 0 until rows && nc in 0 until cols && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2                           // rotten now, and visited
                    fresh--
                    queue.addLast(nr * cols + nc)
                }
            }
        }
        minutes++
    }
    return if (fresh == 0) minutes else -1                     // -1: some orange can never rot
}
```

Checks: `orangesRotting([[2,1,1],[1,1,0],[0,1,1]])` → `4`. `updateMatrix([[0,0,0],[0,1,0],[1,1,1]])` → `[[0,0,0],[0,1,0],[1,2,1]]`.

`orangesRotting` changes the input grid. Copy it first if the caller needs it unchanged.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Multi-source BFS on `R × C` cells | `O(R · C)` | `O(R · C)` |
| A separate BFS from every cell | `O((R · C)²)` | — |

#### 5. Common Mistakes

1. **Running a separate BFS from each source.** Far too slow.
2. **Not marking the sources as visited** when you put them in the queue.
3. **Off-by-one in minutes.** The loop must stop when nothing fresh is left. Do not add an extra minute.
4. **Forgetting the unreachable case.** If fresh oranges remain, return `-1`.
5. **No sources at all.** No rotten oranges and some fresh ones: `-1`. No fresh oranges: `0`.
6. **Changing the input** when the caller still needs it.

#### 6. Say This in the Interview

1. "Instead of one BFS per cell, I put all sources in the queue at distance 0 and run one BFS."
2. "Each cell is reached first by its nearest source, so that is its distance."
3. "Time and space are `O(R · C)`."

#### 7. Quick Check

1. In Rotting Oranges, what goes in the queue before the loop starts?
2. When do you return `-1`?

<details>
<summary>Answers</summary>

1. All the rotten oranges.
2. When some fresh orange was never reached (it is blocked off by empty cells).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 994 | Rotting Oranges (Medium) | this note |
| 542 | 01 Matrix (Medium) | this note |
| 286 | Walls and Gates (Medium, premium) | sources are the gates |
| 1162 | As Far from Land as Possible (Medium) | sources are the land cells |
| 1765 | Map of Highest Peak (Medium) | sources are the water cells |
| 934 | Shortest Bridge (Medium) | find one island, then BFS from it |
| 417 | Pacific Atlantic Water Flow (Medium) | BFS from each ocean's border |
