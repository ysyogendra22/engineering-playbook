# Stack-Based DFS

#### 1. Definition — Must Know

1. **DFS** (Depth-First Search) goes as **deep as possible** along one path before backtracking.
2. Normally DFS is written with **recursion**, which uses the **call stack**.
3. **Stack-based (iterative) DFS** uses your own `ArrayDeque` as the stack instead of recursion.
4. Both give a valid DFS. The explicit stack avoids `StackOverflowError` on very deep inputs.

#### 2. Why It Is Used — Must Know

1. Deep recursion (100,000 levels in a long chain or a large grid) can crash the app. An explicit stack lives on the heap and can be as large as memory allows.
2. Interviewers often ask: "can you do this without recursion?".
3. It makes inorder/preorder/postorder tree traversal, graph DFS, and flood fill easy to control.

#### 3. How It Works — Must Know

**Graph DFS.** Push the start. Repeat: pop a node; if it is new, visit it and push its neighbours.

```text
graph: 0:[1,2]  1:[3]  2:[3]  3:[]

stack [0]
pop 0 → visit 0, push neighbours (in reverse so 1 is on top):  stack [2, 1]
pop 1 → visit 1, push 3:                                       stack [2, 3]
pop 3 → visit 3:                                               stack [2]
pop 2 → visit 2, 3 is already visited:                         stack []

visit order: 0, 1, 3, 2   (same as recursive DFS)
```

**Tree preorder (root, left, right).** Push the root. Pop a node, visit it, push **right first, then left**, so left is processed first.

```text
      1
     / \
    2   3

stack [1] → pop 1, visit; push 3, push 2 → pop 2, visit → pop 3, visit
order: 1, 2, 3
```

**Tree inorder (left, root, right).** Go left as far as possible, pushing nodes. Pop one, visit it, then move to its right child.

#### 4. Core Concepts — Must Know

1. **The stack replaces the call stack.** Each item is "a node still to explore".
2. **Order trick:** to explore neighbours in the same order as recursion, push them in **reverse**.
3. **Visited timing:** for graphs, mark a node visited when you **pop** it (and skip it if it was already visited) or when you **push** it. Marking on pop keeps the exact recursive order; marking on push uses less stack space but can change the order.
4. **Trees need no visited set** (no cycles).
5. **Preorder:** pop → visit → push right, push left.
6. **Inorder:** loop `cur`: push while going left; pop → visit → `cur = node.right`.
7. **Postorder:** harder. Common trick: do preorder with "root, right, left", then reverse the result.
8. **Stack of frames:** if you need state (which child is next), push small objects like `(node, nextChildIndex)`.

| | Recursive DFS | Stack-based DFS |
|---|---|---|
| Code | shortest | a bit longer |
| Depth limit | JVM stack (about thousands to tens of thousands of frames) | heap memory |
| Control over order | by code order | by push order |
| Easy to pause/resume | no | yes |

#### 5. Algorithm — Must Know

```text
dfs(start):
    stack = [start]
    while stack is not empty:
        node = stack.pop()
        if node is visited: continue
        mark node visited;  process node
        for each neighbour in reverse order:
            if neighbour is not visited: stack.push(neighbour)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

// Graph DFS (adjacency list)
fun dfs(graph: List<List<Int>>, start: Int): List<Int> {
    val visited = BooleanArray(graph.size)
    val order = mutableListOf<Int>()
    val stack = ArrayDeque<Int>()
    stack.addLast(start)
    while (stack.isNotEmpty()) {
        val node = stack.removeLast()
        if (visited[node]) continue
        visited[node] = true
        order.add(node)
        for (next in graph[node].asReversed()) {          // reverse to match recursive order
            if (!visited[next]) stack.addLast(next)
        }
    }
    return order
}

// Tree preorder
fun preorder(root: TreeNode?): List<Int> {
    val result = mutableListOf<Int>()
    if (root == null) return result
    val stack = ArrayDeque<TreeNode>()
    stack.addLast(root)
    while (stack.isNotEmpty()) {
        val node = stack.removeLast()
        result.add(node.`val`)
        node.right?.let { stack.addLast(it) }              // right first
        node.left?.let { stack.addLast(it) }               // so left is on top
    }
    return result
}

// Tree inorder
fun inorder(root: TreeNode?): List<Int> {
    val result = mutableListOf<Int>()
    val stack = ArrayDeque<TreeNode>()
    var cur = root
    while (cur != null || stack.isNotEmpty()) {
        while (cur != null) {                              // go as far left as possible
            stack.addLast(cur)
            cur = cur.left
        }
        val node = stack.removeLast()
        result.add(node.`val`)
        cur = node.right
    }
    return result
}

// Tree postorder: root-right-left, then reverse
fun postorder(root: TreeNode?): List<Int> {
    val result = mutableListOf<Int>()
    if (root == null) return result
    val stack = ArrayDeque<TreeNode>()
    stack.addLast(root)
    while (stack.isNotEmpty()) {
        val node = stack.removeLast()
        result.add(node.`val`)
        node.left?.let { stack.addLast(it) }
        node.right?.let { stack.addLast(it) }
    }
    result.reverse()
    return result
}

// Number of Islands with an explicit stack (no recursion, safe for big grids)
fun numIslands(grid: Array<CharArray>): Int {
    val rows = grid.size
    val cols = grid[0].size
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    var count = 0
    for (r in 0 until rows) for (c in 0 until cols) {
        if (grid[r][c] != '1') continue
        count++
        val stack = ArrayDeque<Int>()
        grid[r][c] = '0'                                   // mark visited (changes the input)
        stack.addLast(r * cols + c)
        while (stack.isNotEmpty()) {
            val id = stack.removeLast()
            for (d in dirs) {
                val nr = id / cols + d[0]
                val nc = id % cols + d[1]
                if (nr in 0 until rows && nc in 0 until cols && grid[nr][nc] == '1') {
                    grid[nr][nc] = '0'
                    stack.addLast(nr * cols + nc)
                }
            }
        }
    }
    return count
}
```

Checks: `dfs([[1,2],[3],[3],[]], 0)` → `[0, 1, 3, 2]`. Tree `1(2,3)`: preorder `[1,2,3]`, inorder `[2,1,3]`, postorder `[2,3,1]`.

#### 7. Time & Space Complexity — Must Know

| Case | Time | Space |
|---|---:|---:|
| Graph DFS | `O(V + E)` | `O(V)` (stack + visited; the stack can hold up to `E` entries when marking on pop) |
| Tree traversal | `O(n)` | `O(h)`, `h` = height (up to `O(n)` for a skewed tree) |
| Grid DFS | `O(R · C)` | `O(R · C)` worst case |

#### 8. Common Stack-DFS Patterns — Must Know

1. **Iterative preorder / inorder / postorder** (LeetCode 144, 94, 145).
2. **Number of Islands** (LeetCode 200), **Max Area of Island** (LeetCode 695).
3. **Flood Fill** (LeetCode 733), **Surrounded Regions** (LeetCode 130).
4. **Clone Graph** (LeetCode 133), **Course Schedule** cycle detection (needs state per node).
5. **Validate BST (iterative inorder)** (LeetCode 98), **Kth Smallest in a BST** (LeetCode 230).
6. **Path problems** that need the path itself — push `(node, path)` or use parent links.
7. **Android example:** walking a deeply nested `View` or file-system tree without recursion.

#### 9. Edge Cases / Common Mistakes

1. Pushing left before right in preorder, which visits the right subtree first.
2. Marking visited only when pushing **and** also visiting on pop for graphs with cycles (duplicates in the stack). Use the "skip if visited" check on pop.
3. Forgetting the `visited` set for graphs (infinite loop on cycles).
4. Inorder: forgetting the `cur != null || stack.isNotEmpty()` condition.
5. Postorder: forgetting to reverse the result.
6. Assuming the order equals recursive DFS without pushing neighbours in reverse.
7. Empty tree or graph.
8. Changing the input grid when the caller needs it.

#### 10. When to Use / When Not to Use

**Use when:**

1. Input can be very deep and recursion might overflow.
2. You need to control or pause the traversal.

**Use recursion when:**

1. Depth is small and clarity matters (DFS on a balanced tree).

**Use BFS (a queue) when:**

1. You need the shortest path or level order.

#### 11. Related Topics

1. Tree DFS traversal (`01-data-structure/07-Tree/04-DFS Traversal.md`)
2. Graph DFS (`01-data-structure/10-Graph/08-DFS — Depth First Search.md`)
3. Recursion (`02-algorithm/03-Recursion & Divide and Conquer`)
4. DFS pattern (`03-leetcode-patterns`, topic 13)

#### 12. Interview Must Remember

1. **Explicit stack = iterative DFS. Pop, visit, push children.**
2. Push right then left for preorder; reverse neighbours to match recursion.
3. Inorder: go left pushing, pop, visit, go right.
4. Avoids `StackOverflowError` on deep inputs.
