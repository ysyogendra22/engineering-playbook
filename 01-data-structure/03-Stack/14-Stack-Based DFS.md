# Stack-Based DFS

#### 1. What Is It?

**DFS** (Depth-First Search) goes **as deep as it can** along one path, then comes back and tries the next path.

Usually DFS is written with **recursion**. Recursion uses the **call stack** (see note 01). **Stack-based DFS** does the same job with **your own stack** (`ArrayDeque`) and a loop, with no recursion.

Why interviewers ask for it:

- Very deep recursion crashes with `StackOverflowError`. Your own stack lives in normal memory and can be much bigger.
- "Do it iteratively" is a common follow-up question.
- Iterative tree traversals (inorder, preorder, postorder) are standard questions.

#### 2. How It Works

**Graph DFS.** Push the start. Then repeat: pop a node. If it is new, visit it and push its neighbours.

```text
graph:  0 → [1, 2]    1 → [3]    2 → [3]    3 → []

stack [0]
pop 0 → visit 0, push neighbours in reverse (so 1 is on top):   stack [2, 1]
pop 1 → visit 1, push 3:                                        stack [2, 3]
pop 3 → visit 3:                                                stack [2]
pop 2 → visit 2 (3 is already visited):                         stack []

visit order: 0, 1, 3, 2   (the same as recursive DFS)
```

**Tree preorder (root, left, right).** Pop a node, visit it, push the **right** child first and the **left** child second, so left is on top and is handled first.

```text
      1
     / \
    2   3

stack [1] → pop 1 (visit), push 3, push 2 → pop 2 (visit) → pop 3 (visit)
order: 1, 2, 3
```

**Tree inorder (left, root, right).** Go left as far as you can, pushing each node. Pop one, visit it, then move to its right child.

#### 3. Kotlin Code

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
        if (visited[node]) continue                        // may be pushed twice, visit once
        visited[node] = true
        order.add(node)
        for (next in graph[node].asReversed()) {           // reverse → same order as recursion
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

// Tree postorder: do "root, right, left", then reverse the result
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
```

Checks: graph above → `[0, 1, 3, 2]`. Tree `1` with children `2` and `3`: preorder `[1,2,3]`, inorder `[2,1,3]`, postorder `[2,3,1]`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Graph DFS (`V` nodes, `E` edges) | `O(V + E)` | `O(V)` |
| Tree traversal (`n` nodes) | `O(n)` | `O(h)`, `h` = height of the tree (up to `O(n)`) |

#### 5. Common Mistakes

1. **Pushing left before right in preorder.** Then the right side is visited first.
2. **No `visited` check in a graph.** A cycle makes the loop run forever.
3. **Inorder:** a wrong loop condition. It must be `cur != null || stack.isNotEmpty()`.
4. **Postorder:** forgetting to reverse the result.
5. **Expecting the same order as recursion** without pushing neighbours in reverse.
6. **Empty tree** (`root == null`).

#### 6. Say This in the Interview

1. "Recursion uses the call stack. For very deep input I use my own stack to avoid `StackOverflowError`."
2. "Pop a node, visit it, push its children. For preorder I push right first so left is processed first."
3. "Time `O(V + E)` for a graph, `O(n)` for a tree. Space is the stack size."
4. "For a graph I keep a `visited` set to avoid cycles."

#### 7. Quick Check

1. In iterative preorder, which child do you push first: left or right?
2. Why does a graph DFS need a `visited` set but a tree DFS does not?

<details>
<summary>Answers</summary>

1. Right. The stack is last-in first-out, so left (pushed last) comes out first.
2. A graph can have cycles, so you could come back to a node forever. A tree has no cycles.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 144 | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) (Easy) | stack, push right then left |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (Easy) | go left pushing, pop, go right |
| 145 | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) (Easy) | root-right-left, then reverse |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (Medium) | iterative inorder must be increasing |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (Medium) | iterative inorder, stop at `k` |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium) | DFS with a stack on a grid |
