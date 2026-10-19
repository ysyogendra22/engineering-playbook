# Visited / Seen Pattern

#### 1. Definition — Must Know

1. The **visited / seen pattern** uses a set to remember what you have **already processed**, so you never process it twice.
2. Typical uses: graph and grid search, cycle detection, "first repeated value", loops that may never end.
3. The key line: `if (!visited.add(x)) skip`.

#### 2. Why It Is Used — Must Know

1. Without it, a graph search can loop forever on a cycle.
2. It also avoids repeating work on the same state, which keeps the time linear.
3. It is the base of BFS, DFS, and many "detect a loop" questions.

#### 3. How It Works — Must Know

Example: *Happy Number* (LeetCode 202). Replace the number by the sum of the squares of its digits, again and again. If it reaches `1`, it is happy. If it loops, it is not.

```text
n = 19
19 → 1² + 9² = 82
82 → 8² + 2² = 68
68 → 6² + 8² = 100
100 → 1² + 0² + 0² = 1     → reached 1 → happy

n = 2
2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4   ← 4 was seen before → loop → not happy
```

The set of seen numbers is how we notice that we came back to a place we already visited.

#### 4. Core Concepts — Must Know

1. **Mark when you add to the queue/stack**, not later, in BFS. Otherwise the same item may be queued many times.
2. **`add()` returns `false` if already seen.** Use it as the check and the mark in one step.
3. **What you store is the state's key.** For a grid cell use `row * cols + col`, a `Pair`, or a `data class`.
4. **Cycle detection:** if a walk reaches a value it has seen before, there is a loop.
5. **Two common shapes:**

| Shape | Question |
|---|---|
| Detect a repeat | Did I see this before? (first repeated value, cycles) |
| Avoid revisits | Skip anything already processed (BFS / DFS, grids) |

6. **Alternatives:** a `BooleanArray` for small integer ids is faster. Floyd's cycle detection finds a loop with `O(1)` extra space.

#### 5. Algorithm — Must Know

```text
visited = empty set
start: visited.add(start); queue.add(start)
while queue is not empty:
    node = queue.removeFirst()
    for each neighbour of node:
        if visited.add(neighbour):        // true only the first time
            queue.add(neighbour)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Happy Number
fun isHappy(n: Int): Boolean {
    val seen = HashSet<Int>()
    var x = n
    while (x != 1 && seen.add(x)) {
        x = digitSquareSum(x)
    }
    return x == 1
}

private fun digitSquareSum(value: Int): Int {
    var sum = 0
    var y = value
    while (y > 0) {
        val d = y % 10
        sum += d * d
        y /= 10
    }
    return sum
}
```

**Number of Islands with a visited set** (grid of `'0'` and `'1'`)

```kotlin
fun numIslands(grid: Array<CharArray>): Int {
    if (grid.isEmpty()) return 0
    val rows = grid.size
    val cols = grid[0].size
    val visited = HashSet<Int>()                 // cell id = row * cols + col
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    var count = 0

    for (r in 0 until rows) {
        for (c in 0 until cols) {
            if (grid[r][c] == '1' && visited.add(r * cols + c)) {   // a new island
                count++
                val queue = ArrayDeque<Int>()
                queue.add(r * cols + c)
                while (queue.isNotEmpty()) {
                    val id = queue.removeFirst()
                    val row = id / cols
                    val col = id % cols
                    for (d in dirs) {
                        val nr = row + d[0]
                        val nc = col + d[1]
                        if (nr in 0 until rows && nc in 0 until cols &&
                            grid[nr][nc] == '1' && visited.add(nr * cols + nc)
                        ) {
                            queue.add(nr * cols + nc)
                        }
                    }
                }
            }
        }
    }
    return count
}
```

**Linked list cycle with a set** (the `O(1)` space answer is Floyd's two pointers)

```kotlin
class ListNode(var `val`: Int) { var next: ListNode? = null }

fun hasCycle(head: ListNode?): Boolean {
    val seen = HashSet<ListNode>()           // ListNode has no equals(), so this compares identity
    var node = head
    while (node != null) {
        if (!seen.add(node)) return true
        node = node.next
    }
    return false
}
```

#### 7. Time & Space Complexity — Must Know

| Case | Time | Space |
|---|---:|---:|
| Graph with `V` nodes, `E` edges | `O(V + E)` | `O(V)` |
| Grid `R × C` | `O(R × C)` | `O(R × C)` |
| Happy Number | about `O(log n)` steps | small |
| Linked list cycle with a set | `O(n)` | `O(n)` |

#### 8. Common Visited / Seen Patterns — Must Know

1. **BFS / DFS on graphs and grids** — visited set of nodes or cells.
2. **Cycle detection** — linked list (LeetCode 141), Happy Number (LeetCode 202).
3. **First repeated element** — the first `add` that returns `false`.
4. **Avoid repeated states** — puzzles, word ladder, lock problems.
5. **Memory of seen coordinates** — robot paths, "path crossing" problems.
6. **Android example:** remember which item ids were already shown, so a refresh does not add them again.

#### 9. Edge Cases / Common Mistakes

1. Marking visited **when removing** from the queue, not when adding. The queue then holds many copies.
2. Not marking the start node.
3. Using a set of arrays/lists that you mutate later.
4. Using `Pair<Int, Int>` in a huge grid (extra objects). An `Int` id is lighter.
5. Forgetting to check bounds before the visited check.
6. Using a set of mutable objects. Their hash can change.
7. Using recursion on a very big graph. Deep DFS can cause a `StackOverflowError`. Use an explicit stack.

#### 10. When to Use / When Not to Use

**Use when:**

1. The structure can loop back, or has many paths to the same place.

**Avoid when:**

1. The structure is a tree with no shared children. No visited set is needed.
2. Ids are small integers. A `BooleanArray` is faster.
3. You can mark the data itself (such as changing a grid cell), if the input may be modified.

#### 11. Related Topics

1. HashSet in Graph / State-Space Problems
2. Duplicate Detection
3. Graph BFS / DFS (`02-algorithm/07-Graph Algorithms`)
4. Linked List (`01-data-structure/02-LinkedList`)

#### 12. Interview Must Remember

1. **`if (!visited.add(x)) skip`.**
2. Mark when you **enqueue**, not when you dequeue.
3. Visited prevents infinite loops and repeated work.
4. Floyd's cycle detection and `BooleanArray` are the lighter alternatives.
