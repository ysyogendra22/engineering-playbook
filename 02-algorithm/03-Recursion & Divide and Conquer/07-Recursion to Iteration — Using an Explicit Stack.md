# Recursion to Iteration — Using an Explicit Stack

#### 1. Definition — Must Know

1. Any recursive function can be rewritten as a loop that manages its **own stack** (usually a `Deque` or `MutableList`) instead of relying on the language's call stack.
2. This is called turning recursion into **iteration with an explicit stack**.

#### 2. Why It Is Used — Must Know

1. It avoids a stack overflow on very deep recursion (topic 2), since your own stack lives on the heap, which is much larger.
2. It can be faster in practice, because it skips the overhead of real function calls.
3. Some interviewers specifically ask for the iterative version of a recursive algorithm, to check you understand what's happening underneath.

#### 3. How It Works — Must Know

Recursive DFS on a tree:

```kotlin
fun dfsRecursive(node: TreeNode?) {
    if (node == null) return
    visit(node)
    dfsRecursive(node.left)
    dfsRecursive(node.right)
}
```

The same traversal, using your own stack instead of the call stack:

```text
stack = [root]
while stack is not empty:
    node = stack.pop()
    visit(node)
    push node.right (push right first, so left is processed first — LIFO)
    push node.left
```

1. The call stack normally remembers "what to do next" for you. An explicit stack does the same job, by hand.
2. Push order matters: since a stack is last-in-first-out, push the right child before the left child so the left child is popped and visited first.

#### 4. Algorithm — Must Know

```text
function iterativeVersion(start):
    stack = [start]
    while stack is not empty:
        current = stack.pop()
        process(current)
        for each next step from current, in reverse order:
            stack.push(next step)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun dfsIterative(root: TreeNode?) {
    if (root == null) return
    val stack = ArrayDeque<TreeNode>()
    stack.addLast(root)
    while (stack.isNotEmpty()) {
        val node = stack.removeLast()
        visit(node)
        node.right?.let { stack.addLast(it) }
        node.left?.let { stack.addLast(it) }
    }
}
```

#### 6. Complexity — Must Know

| | Recursive | Iterative with explicit stack |
|---|---|---|
| Time | O(n) | O(n) — the same |
| Space | O(h) call stack, where h is the tree height | O(h) on your own stack — same order, but on the heap, with a much higher limit |

The Big-O stays the same. What changes is *where* that space lives, and how much of it is available before you hit a crash.

#### 7. Common Mistakes — Must Know

1. Pushing children in the wrong order and getting a different traversal order than intended.
2. Forgetting that BFS uses a **queue** (first-in-first-out), while this DFS technique uses a **stack** (last-in-first-out) — mixing them up changes the whole traversal.
3. Assuming the iterative version is always required — usually the recursive version is fine unless depth or performance is a real concern.

#### 8. Related Topics

1. `2` The Call Stack & Space Complexity — what you're replacing
2. `6` Tail Recursion — a narrower fix for a similar problem
3. `DS Graph` and `DS Tree` — DFS and BFS traversal notes

#### 9. Interview Must Remember

1. An explicit stack (`ArrayDeque`, pushed and popped) does the same job as the call stack — just visibly, and on the heap.
2. **Push order controls visit order** for a stack-based traversal — think it through, don't guess.
3. Mention this as the fix when a recursive solution risks a stack overflow on deep input.
