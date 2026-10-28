# Flatten Multilevel Linked List

#### 1. What Is It?

A doubly linked list where a node can also have a **`child`** pointer to another doubly linked list (which can have its own children). **Flatten** it into one single-level list, where the child list comes **right after its parent**.

```text
1 ⇄ 2 ⇄ 3 ⇄ 4
        ↓
        7 ⇄ 8
        
→ 1 ⇄ 2 ⇄ 3 ⇄ 7 ⇄ 8 ⇄ 4
```

This is *Flatten a Multilevel Doubly Linked List* (LeetCode 430). It looks like a tree walk (go down first, then continue): a **depth-first** order.

#### 2. How It Works

**Method 1 — Stack.** Walk the list. When a node has a child:

1. Push the node's `next` on a stack (it must come back later).
2. Link the node to the child (`node.next = child`, `child.prev = node`) and set `node.child = null`.
3. Continue with the child list.

When you reach the end of a list (`next == null`) and the stack is not empty, pop a node and link the current node to it.

```text
1 ⇄ 2 ⇄ 3 ⇄ 4,  3.child = 7 ⇄ 8

at 3: push 4.  3 → 7.   continue: 7, 8
at 8: next is null, pop 4:  8 → 4
result: 1 ⇄ 2 ⇄ 3 ⇄ 7 ⇄ 8 ⇄ 4
```

**Method 2 — Recursion.** Flatten the child list first. Return its tail. Connect `node → child ... childTail → node.next`. Same idea, but the stack is the call stack.

#### 3. Brute Force vs Optimized

| | Brute force | Stack |
|---|---|---|
| Idea | DFS to collect all nodes in order, then re-link them | re-link while walking |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(depth)` |

```kotlin
fun flattenBrute(head: MNode?): MNode? {
    val order = mutableListOf<MNode>()
    fun dfs(node: MNode?) {
        var cur = node
        while (cur != null) {
            order.add(cur)
            dfs(cur.child)
            cur = cur.next
        }
    }
    dfs(head)
    for (i in order.indices) {
        val n = order[i]
        n.child = null
        n.prev = if (i > 0) order[i - 1] else null
        n.next = if (i < order.size - 1) order[i + 1] else null
    }
    return head
}
```

Collect first, re-link after. If you re-link while collecting, the `next` pointers you are following change.

#### 4. Kotlin Code

```kotlin
class MNode(var `val`: Int) {
    var prev: MNode? = null
    var next: MNode? = null
    var child: MNode? = null
}

// Flatten a Multilevel Doubly Linked List (LeetCode 430): stack
fun flatten(head: MNode?): MNode? {
    val stack = ArrayDeque<MNode>()
    var cur = head
    while (cur != null) {
        val child = cur.child
        if (child != null) {
            cur.next?.let { stack.addLast(it) }       // come back to this later
            cur.next = child
            child.prev = cur
            cur.child = null                           // the child pointer must be cleared
        }
        if (cur.next == null && stack.isNotEmpty()) {  // end of a list: resume the saved one
            val saved = stack.removeLast()
            cur.next = saved
            saved.prev = cur
        }
        cur = cur.next
    }
    return head
}

// Flatten Binary Tree to Linked List (LeetCode 114): a similar "re-link in DFS order" idea
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

fun flattenTree(root: TreeNode?) {
    var cur = root
    while (cur != null) {
        val left = cur.left
        if (left != null) {
            var rightmost: TreeNode = left
            while (rightmost.right != null) rightmost = rightmost.right!!
            rightmost.right = cur.right                // attach the right subtree after the left one
            cur.right = left
            cur.left = null
        }
        cur = cur.right
    }
}
```

Check (stack version): list `1⇄2⇄3⇄4` with `3.child = 7⇄8`:
`flatten` gives `1⇄2⇄3⇄7⇄8⇄4`, and `4.prev` is `8`.
Check (tree version): tree `1(2(3,4),5(null,6))` flattens to the right-leaning chain `1→2→3→4→5→6`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Stack | `O(n)` | `O(d)`, `d` = nesting depth |
| Recursion | `O(n)` | `O(d)` call stack |
| Tree version (rightmost) | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Not setting `child = null`.** The result must have no child pointers.
2. **Not updating `prev`** on the nodes you connect (it is a doubly linked list).
3. **Losing the old `next`** of the parent. Save it on the stack before you overwrite it.
4. **Forgetting to resume the saved list** when a child list ends.
5. **Pushing `null`** on the stack (a parent with no `next`). Push only non-null nodes.
6. **Empty list:** return `null`.

#### 7. Say This in the Interview

1. "It is a depth-first order: go into the child list first, then come back to the parent's `next`. I save the parent's `next` on a stack."
2. "When a child list ends, I pop the saved node and connect it. I also fix `prev` and clear `child`."

#### 8. Quick Check

1. What goes on the stack?
2. What must be done with each `child` pointer after the flatten?

<details>
<summary>Answers</summary>

1. The parent's `next` node, so you can return to it after the child list.
2. Set it to `null`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 430 | [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) (Medium) | this note |
| 114 | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) (Medium) | DFS order re-link |
| 341 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) (Medium) | stack of iterators |
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) (Medium) | another list with extra pointers (note 22) |
| 426 | [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) (Medium, premium) | in-order + prev / next |
