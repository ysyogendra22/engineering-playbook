# Tree Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–21.

#### 1. Key Takeaways

1. A tree is **recursive**: every subtree is a tree. Most solutions are `if (node == null) return base` then combine `left` and `right`.
2. Decide first: do I pass data **down** (parameters: depth, remaining sum, bounds) or **return it up** (height, balanced, diameter)?
3. **BFS (queue)** for levels, sides and minimum depth. **DFS (recursion)** for paths, heights and subtree values.
4. **Inorder of a BST is sorted.** Use it for validate, kth smallest, successor.
5. Many "hard" problems are one pattern: **return one value, record another in a variable** (diameter, max path sum).
6. Say the `O(h)` space: `O(log n)` if balanced, `O(n)` if the tree is a chain.
7. Always test: empty tree, single node, chain (left and right), balanced.

#### 2. Complexity Table

| Operation | Time | Space |
|---|---|---|
| Any traversal (DFS or BFS) | `O(n)` | DFS `O(h)`, BFS `O(w)` |
| BST search / insert / delete | `O(h)` (`O(log n)` balanced, `O(n)` chain) | `O(h)` recursive, `O(1)` iterative |
| Height, diameter, balanced, path sum | `O(n)` | `O(h)` |
| LCA (binary tree) / (BST) | `O(n)` / `O(h)` | `O(h)` / `O(1)` |
| Build from preorder + inorder | `O(n)` with a map | `O(n)` |
| Serialize / deserialize | `O(n)` | `O(n)` |
| Kth smallest (BST) | `O(h + k)` | `O(h)` |
| AVL / Red-Black operations | `O(log n)` | `O(n)` |
| Fenwick / segment tree | `O(log n)` per operation | `O(n)` |

`h` = height. `w` = widest level.

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Note |
|---|---|---|
| "depth", "height", "longest root-to-leaf" | bottom-up DFS: `1 + max(left, right)` | 06 |
| "minimum depth" | BFS, first leaf (or DFS with the one-child rule) | 05, 06 |
| "level by level", "each row", "average of levels" | BFS with `queue.size` per level | 05 |
| "right / left side view" | BFS last / first of each level | 14 |
| "top / bottom view", "vertical" | BFS with horizontal distance | 14 |
| "zigzag", "spiral" | level order + reverse alternate levels | 19 |
| "validate BST" | pass `(low, high)` bounds, or inorder strictly increasing | 09 |
| "kth smallest", "sorted", "successor" in a BST | inorder, stop early | 20 |
| "balanced" | bottom-up height with a `-1` failure signal | 10 |
| "diameter", "longest path between nodes" | height + global best (`left + right`) | 11 |
| "maximum path sum" | gain with `max(0, ...)` + global best | 17 |
| "root-to-leaf sum", "all paths" | pass the remaining sum down, backtrack | 12 |
| "path sum, any start and end" | prefix sums + map (undo on exit) | 12 |
| "lowest common ancestor" | postorder split-point / BST ordering | 13 |
| "same", "symmetric", "mirror", "subtree" | recurse on **two** nodes together | 18 |
| "construct from traversals" | root from pre/post, split with inorder (map) | 15 |
| "serialize / deserialize" | preorder with `#` markers | 16 |
| "build a balanced BST from sorted data" | middle element as the root | 20 |
| "any number of children" | N-ary node + loop over children | 21 |
| "range sum with updates" | Fenwick or segment tree | 21 |

#### 4. Templates to Memorise

**Basic recursion (bottom-up)**

```kotlin
fun solve(node: TreeNode?): Int {
    if (node == null) return 0
    val left = solve(node.left)
    val right = solve(node.right)
    return 1 + maxOf(left, right)
}
```

**Top-down with a parameter**

```kotlin
fun dfs(node: TreeNode?, remaining: Int): Boolean {
    if (node == null) return false
    if (node.left == null && node.right == null) return node.value == remaining
    return dfs(node.left, remaining - node.value) || dfs(node.right, remaining - node.value)
}
```

**Level order**

```kotlin
val queue = ArrayDeque<TreeNode>(); queue.addLast(root)
while (queue.isNotEmpty()) {
    repeat(queue.size) {                         // one level
        val node = queue.removeFirst()
        node.left?.let { queue.addLast(it) }
        node.right?.let { queue.addLast(it) }
    }
}
```

**Return one thing, record another (diameter / max path sum)**

```kotlin
var best = 0
fun height(node: TreeNode?): Int {
    if (node == null) return 0
    val l = height(node.left); val r = height(node.right)
    best = maxOf(best, l + r)
    return 1 + maxOf(l, r)
}
```

**Iterative inorder**

```kotlin
val stack = ArrayDeque<TreeNode>(); var cur = root
while (cur != null || stack.isNotEmpty()) {
    while (cur != null) { stack.addLast(cur); cur = cur.left }
    val node = stack.removeLast()
    // visit node
    cur = node.right
}
```

**Validate BST**

```kotlin
fun check(n: TreeNode?, low: Long, high: Long): Boolean {
    if (n == null) return true
    if (n.value <= low || n.value >= high) return false
    return check(n.left, low, n.value.toLong()) && check(n.right, n.value.toLong(), high)
}
```

**LCA (binary tree)**

```kotlin
fun lca(r: TreeNode?, p: TreeNode, q: TreeNode): TreeNode? {
    if (r == null || r === p || r === q) return r
    val l = lca(r.left, p, q); val rt = lca(r.right, p, q)
    return if (l != null && rt != null) r else l ?: rt
}
```

**BST delete (two children)**

```kotlin
val succ = findMin(root.right!!)
return TreeNode(succ.value, root.left, deleteNode(root.right, succ.value))
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Optimized |
|---|---|---|
| Balanced tree | height at every node `O(n²)` | bottom-up with `-1` `O(n)` |
| Diameter | height at every node `O(n²)` | height + global best `O(n)` |
| Validate BST | check every node against its whole subtrees `O(n²)` | bounds / inorder `O(n)` |
| Path Sum III | DFS from every node `O(n²)` | prefix sum + map `O(n)` |
| Build from traversals | `indexOf` + array copies `O(n²)` | map + pointer `O(n)` |
| Kth smallest | full inorder list `O(n)` space | iterative inorder, stop at k `O(h)` |
| LCA | two root paths + compare | one postorder pass |
| Subtree of another tree | `same()` at every node `O(m·n)` | serialize + substring |
| Count complete tree nodes | visit all `O(n)` | compare left/right depth `O(log² n)` |
| Range sum with updates | sum per query `O(n)` | Fenwick `O(log n)` |

#### 6. Common Mistakes and Edge Cases

1. **Forgetting `root == null`** (the base case).
2. **Leaf vs null:** Path Sum must stop at a **leaf**, not at a null child.
3. **Min depth with one child:** the missing side is not a leaf.
4. **Validate BST with only parent checks**, or `Int` bounds.
5. **Depth vs height, nodes vs edges.** LeetCode depth counts nodes.
6. **Returning the answer (not the height)** in diameter / max path sum.
7. **Not copying the path** when saving a result (backtracking).
8. **`queue.size` read inside the loop** (level order).
9. **BST delete:** forgetting to delete the successor from the right subtree.
10. **Recursion depth** on a chain of 10⁵ nodes: use an explicit stack.
11. Edge cases: empty tree, one node, left chain, right chain, duplicates, negative values, `Int.MIN_VALUE`/`MAX_VALUE`.

#### 7. What to Say Out Loud

1. "A tree is recursive. The base case is a null node, then I combine the left and right answers."
2. "Do I need information from the parent (pass it down) or from the children (return it up)?"
3. "I'll use BFS because the question is about levels." / "I'll use DFS because it's about paths and subtree values."
4. "Time `O(n)`: each node is visited once. Space `O(h)`: `O(log n)` if balanced, `O(n)` if skewed."
5. "The tree might be a chain, so I'll mention recursion depth and the iterative option."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | bottom-up |
| Easy | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | swap |
| Easy | [Same Tree](https://leetcode.com/problems/same-tree/) | two-node recursion |
| Easy | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | mirror |
| Easy | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | traversal |
| Easy | [Path Sum](https://leetcode.com/problems/path-sum/) | top-down |
| Easy | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | bottom-up `-1` |
| Easy | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | height + global |
| Easy | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | same at each node |
| Easy | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | middle root |
| Medium | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS |
| Medium | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | last of level |
| Medium | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | reverse levels |
| Medium | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | bounds |
| Medium | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | inorder |
| Medium | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | postorder |
| Medium | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | backtracking |
| Medium | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | prefix + map |
| Medium | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | map + pointer |
| Medium | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | three cases |
| Medium | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | stack |
| Hard | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | preorder + `#` |
| Hard | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | gain + global |
