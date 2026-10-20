# Level-by-Level Processing

#### 1. What Is It?

Normal BFS handles **one node at a time**. **Level-by-level** BFS handles **one whole level at a time**.

The trick: at the start of each round, read **`queue.size`**. That is exactly the number of nodes in the current level. Process that many nodes. The children you add belong to the next level.

Use it when the answer depends on levels:

- list the nodes of each level,
- the last (or first) node of each level,
- the depth of a tree, or the number of steps.

#### 2. How It Works

```text
        3
       / \
      9  20
        /  \
       15   7

queue [3]         size 1 → level 0:  take 3, add 9 and 20        level = [3]
queue [9, 20]     size 2 → level 1:  take 9, 20, add 15 and 7    level = [9, 20]
queue [15, 7]     size 2 → level 2:  take 15, 7                  level = [15, 7]
queue []          stop

result: [[3], [9, 20], [15, 7]]
```

At the start of a round the queue holds **only** that level. The children you add go behind them and wait for the next round.

Which value you keep from each level decides the question:

| Question | Keep from each level |
|---|---|
| Level Order Traversal (102) | all nodes |
| Right Side View (199) | the **last** node |
| Average of Levels (637) | sum ÷ count |
| Zigzag (103) | all nodes, reversed on every second level |
| Minimum Depth (111) | stop at the first leaf |
| Maximum Depth (104) | the number of rounds |

#### 3. Kotlin Code

```kotlin
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

// Level order traversal
fun levelOrder(root: TreeNode?): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    if (root == null) return result
    val queue = ArrayDeque<TreeNode>()
    queue.addLast(root)

    while (queue.isNotEmpty()) {
        val level = mutableListOf<Int>()
        repeat(queue.size) {                         // the size is read ONCE, before the body runs
            val node = queue.removeFirst()
            level.add(node.`val`)
            node.left?.let { queue.addLast(it) }
            node.right?.let { queue.addLast(it) }
        }
        result.add(level)
    }
    return result
}

// Right side view: the last node of each level
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

// Minimum depth: stop at the first leaf
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

On the tree above: `levelOrder` → `[[3], [9, 20], [15, 7]]`, `rightSideView` → `[3, 20, 7]`, `minDepth` → `2`.

For zigzag, build each level the same way and call `level.reversed()` on every second level.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Level-order BFS | `O(n)` | `O(w)`, where `w` is the widest level |

Every node is added and removed once.

#### 5. Common Mistakes

1. **Reading the size inside the loop condition** (`while (i < queue.size)`). New children make it grow, so levels mix. `repeat(queue.size)` and `for (i in 0 until size)` read it once, which is correct.
2. **Not creating a new list for each level.**
3. **Forgetting the empty tree** (`root == null`).
4. **Off-by-one in depth.** Decide if the root is depth 0 or 1.
5. **Zigzag:** reversing the wrong levels.

#### 6. Say This in the Interview

1. "I use BFS. At the start of each round I read the queue size, which is the size of the current level."
2. "Outer loop is the levels, inner loop is the nodes of one level."
3. "Time `O(n)`, space `O(width of the tree)`."

#### 7. Quick Check

1. How do you get the number of nodes in the current level?
2. For the right side view, which node of each level do you keep?

<details>
<summary>Answers</summary>

1. Read `queue.size` at the start of the round.
2. The last one (index `size - 1`).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 102 | Binary Tree Level Order Traversal (Medium) | this note |
| 107 | Binary Tree Level Order Traversal II (Medium) | reverse the result |
| 103 | Binary Tree Zigzag Level Order Traversal (Medium) | reverse every second level |
| 199 | Binary Tree Right Side View (Medium) | last node of each level |
| 637 | Average of Levels in Binary Tree (Easy) | sum ÷ count |
| 111 | Minimum Depth of Binary Tree (Easy) | stop at the first leaf |
| 116 | Populating Next Right Pointers in Each Node (Medium) | link nodes inside a level |
