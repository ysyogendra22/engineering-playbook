# Level-by-Level Processing

#### 1. Definition — Must Know

1. **Level-by-level processing** is BFS that handles **one whole level at a time** instead of one node at a time.
2. The trick: at the start of each round, read **`queue.size`**. That is exactly the number of nodes in the current level. Process that many, and the new nodes you add form the next level.
3. It answers questions that depend on levels: "list each level", "last node of each level", "depth", "number of steps".

#### 2. Why It Is Used — Must Know

1. Many tree and graph questions are really about levels (LeetCode 102, 107, 103, 199, 637, 111, 515).
2. It gives the **distance** (level number) for free.
3. It is a standard pattern for shortest path in unweighted graphs and grids.

#### 3. How It Works — Must Know

```text
        3
       / \
      9  20
        /  \
       15   7

queue [3]              size 1 → level 0:  take 3   add 9, 20      level = [3]
queue [9, 20]          size 2 → level 1:  take 9, 20   add 15, 7  level = [9, 20]
queue [15, 7]          size 2 → level 2:  take 15, 7              level = [15, 7]
queue []               stop

result: [[3], [9, 20], [15, 7]]
```

Why it works: when a level starts, the queue holds **only** that level. Nodes added while you process it go behind them and wait for the next round.

#### 4. Core Concepts — Must Know

1. **Capture the size first:** `repeat(queue.size) { … }` reads the size once, before the body changes the queue.
2. **Outer `while`** loops over levels. **Inner `repeat`** loops over the nodes in one level.
3. **Level counter:** increase by 1 after each outer round (`depth++`, `steps++`).
4. **Per-level result:** make a new list at the start of each round and add it to the answer at the end.
5. **Pick what to keep per level:**

| Question | Keep from each level |
|---|---|
| Level Order Traversal (LeetCode 102) | all nodes |
| Right Side View (LeetCode 199) | the last node |
| Left Side View | the first node |
| Average of Levels (LeetCode 637) | the sum / count |
| Largest Value in Each Row (LeetCode 515) | the maximum |
| Zigzag (LeetCode 103) | all nodes, reversed on odd levels |
| Minimum Depth (LeetCode 111) | stop at the first leaf |
| Maximum Depth (LeetCode 104) | the number of rounds |

6. **For graphs and grids**, the level number is the distance from the start.

#### 5. Algorithm — Must Know

```text
queue = [root]
while queue is not empty:
    levelSize = queue.size
    repeat levelSize times:
        node = removeFirst()
        process node
        add node's children to the back
    finish the level (store result, depth++)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

// Level Order Traversal
fun levelOrder(root: TreeNode?): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    if (root == null) return result
    val queue = ArrayDeque<TreeNode>()
    queue.addLast(root)

    while (queue.isNotEmpty()) {
        val level = mutableListOf<Int>()
        repeat(queue.size) {                       // size is read once
            val node = queue.removeFirst()
            level.add(node.`val`)
            node.left?.let { queue.addLast(it) }
            node.right?.let { queue.addLast(it) }
        }
        result.add(level)
    }
    return result
}

// Right Side View — the last node of each level
fun rightSideView(root: TreeNode?): List<Int> {
    val result = mutableListOf<Int>()
    if (root == null) return result
    val queue = ArrayDeque<TreeNode>()
    queue.addLast(root)
    while (queue.isNotEmpty()) {
        val size = queue.size
        for (i in 0 until size) {
            val node = queue.removeFirst()
            if (i == size - 1) result.add(node.`val`)
            node.left?.let { queue.addLast(it) }
            node.right?.let { queue.addLast(it) }
        }
    }
    return result
}

// Zigzag Level Order
fun zigzagLevelOrder(root: TreeNode?): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    if (root == null) return result
    val queue = ArrayDeque<TreeNode>()
    queue.addLast(root)
    var leftToRight = true
    while (queue.isNotEmpty()) {
        val level = mutableListOf<Int>()
        repeat(queue.size) {
            val node = queue.removeFirst()
            level.add(node.`val`)
            node.left?.let { queue.addLast(it) }
            node.right?.let { queue.addLast(it) }
        }
        result.add(if (leftToRight) level else level.reversed())
        leftToRight = !leftToRight
    }
    return result
}

// Minimum Depth — stop at the first leaf
fun minDepth(root: TreeNode?): Int {
    if (root == null) return 0
    val queue = ArrayDeque<TreeNode>()
    queue.addLast(root)
    var depth = 1
    while (queue.isNotEmpty()) {
        repeat(queue.size) {
            val node = queue.removeFirst()
            if (node.left == null && node.right == null) return depth
            node.left?.let { queue.addLast(it) }
            node.right?.let { queue.addLast(it) }
        }
        depth++
    }
    return depth
}
```

Check on the tree above: `levelOrder` → `[[3], [9, 20], [15, 7]]`, `rightSideView` → `[3, 20, 7]`, `minDepth` → `2`.

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---:|
| Time | `O(n)` — every node is added and removed once |
| Space | `O(w)` where `w` is the widest level (up to `n/2` for a complete tree) |

#### 8. Common Level Patterns — Must Know

1. **Binary Tree Level Order Traversal** (LeetCode 102) and **II** (bottom-up, 107).
2. **Zigzag Level Order** (LeetCode 103).
3. **Right Side View** (LeetCode 199).
4. **Average of Levels** (LeetCode 637), **Largest Value in Each Row** (LeetCode 515).
5. **Minimum Depth** (LeetCode 111), **Maximum Depth** (LeetCode 104).
6. **Populating Next Right Pointers** (LeetCode 116/117).
7. **Graph / grid BFS with step count** (next notes).
8. **Word Ladder** — the level is the chain length.

#### 9. Edge Cases / Common Mistakes

1. Reading `queue.size` **inside** the loop condition of a `while`, so new children are counted as part of the current level. `repeat(queue.size)` and `for (i in 0 until size)` read it once, which is safe.
2. Forgetting to reset the per-level list for each round.
3. Empty tree (`root == null`).
4. Off-by-one in depth (starting at 0 vs 1).
5. Returning from inside `repeat`/`for` without the right value (`minDepth`).
6. Reversing the wrong levels in zigzag.
7. Using recursion (DFS with a depth parameter) when the problem is simply level-based. It also works, but BFS is more natural.
8. Large trees: the queue can hold a whole level, so memory is `O(w)`.

#### 10. When to Use / When Not to Use

**Use when:**

1. The answer depends on levels, depth, or distance in steps.

**Use plain BFS (no level loop) when:**

1. You only need the visit order and not the level boundaries.

**Use DFS when:**

1. You need path-based answers (path sum, diameter).

#### 11. Related Topics

1. BFS
2. Tree level-order (`01-data-structure/07-Tree/05-BFS - Level Order Traversal.md`)
3. Queue for Shortest Path
4. Grid BFS

#### 12. Interview Must Remember

1. **`repeat(queue.size) { … }` processes exactly one level.**
2. Outer loop = levels; inner loop = nodes of one level.
3. Level count = depth = distance in steps.
4. `O(n)` time, `O(width)` space.
