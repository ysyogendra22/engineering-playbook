# Stack Fundamentals — LIFO

#### 1. Definition — Must Know

1. A **stack** is a collection where the **last item added is the first one removed**: **LIFO** (Last In, First Out).
2. You only work at **one end**, called the **top**. You **push** onto the top and **pop** from the top.
3. You normally see only the top item. There is no access to the middle.

#### 2. Why It Is Used — Must Know

1. It remembers things **in reverse order**: the most recent thing comes back first.
2. It is the natural tool for **matching and nesting** (brackets, tags, function calls) and for **undo**.
3. It powers a family of interview patterns: parentheses, monotonic stack (next greater element, histogram), expression evaluation, iterative DFS.
4. In Android: the **back stack** of screens, the **call stack** of functions, and undo/redo.

#### 3. How It Works — Must Know

```text
        push(40)            pop() → 40
          ↓                   ↑
        ┌────┐              ┌────┐
        │ 40 │ ← top        │ 30 │ ← top
        │ 30 │              │ 20 │
        │ 20 │              │ 10 │
        │ 10 │              └────┘
        └────┘
```

Real examples:

```text
A pile of plates:       you take the top plate first.
Browser back button:    pages are stacked as you visit them; "back" pops the latest one.
Undo (Ctrl+Z):          the last action is undone first.
Function calls:         the function called last finishes first (the call stack).
```

Compare with a **queue** (FIFO): the first item in is the first out. A stack is the opposite.

#### 4. Core Concepts — Must Know

1. **LIFO order** — newest out first.
2. **Main operations** (all `O(1)`): `push`, `pop`, `peek` (top), `isEmpty`, `size`.
3. **Overflow / underflow:** pushing onto a full fixed-size stack is **overflow**. Popping an empty stack is **underflow**. Kotlin's dynamic stacks only have underflow.
4. **Kotlin/JVM tools:**

| Tool | Notes |
|---|---|
| `ArrayDeque<T>` | **Recommended.** Use `addLast`, `removeLast`, `last()`. |
| `java.util.Stack<T>` | Old, built on `Vector` (synchronized, slower). Avoid in new code. |
| `java.util.ArrayDeque` as `Deque` | `push`/`pop`/`peek` work at the **front**. |
| `MutableList` | `add`, `removeAt(lastIndex)` works but is easy to misuse. |

5. **The call stack:** each function call pushes a *frame*; each return pops it. Deep recursion can cause `StackOverflowError`.
6. **When you see these signs, think "stack":** matching pairs, "most recent unresolved item", "next greater/smaller", undo, reverse, nested structure, iterative replacement of recursion.

#### 5. Algorithm — Must Know

The basic stack loop:

```text
stack = empty
for each item:
    while the stack top "loses" to the item (or matches it): pop and handle
    push the item
at the end: handle what is left in the stack
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val stack = ArrayDeque<Int>()

stack.addLast(10)                 // push
stack.addLast(20)
stack.addLast(30)

println(stack.last())             // peek → 30
println(stack.removeLast())       // pop  → 30
println(stack.size)               // 2
println(stack.isEmpty())          // false

// Safe versions for empty stacks
println(stack.lastOrNull())       // 20, or null when empty
println(stack.removeLastOrNull()) // 20, or null when empty

// Reverse a string with a stack
fun reverse(s: String): String {
    val st = ArrayDeque<Char>()
    for (c in s) st.addLast(c)
    val sb = StringBuilder()
    while (st.isNotEmpty()) sb.append(st.removeLast())
    return sb.toString()
}
println(reverse("stack"))         // kcats
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `push` | `O(1)` amortized |
| `pop` | `O(1)` |
| `peek` | `O(1)` |
| `isEmpty`, `size` | `O(1)` |
| Search for a value | `O(n)` |
| Space | `O(n)` |

#### 8. Common Stack Patterns — Must Know

1. **Matching pairs:** Valid Parentheses.
2. **Monotonic stack:** next greater/smaller, Daily Temperatures, Largest Rectangle.
3. **Expression handling:** evaluate RPN, basic calculator, decode string.
4. **Undo style:** Min Stack, Simplify Path, Remove Adjacent Duplicates.
5. **Iterative DFS:** replace recursion with an explicit stack.
6. **Collision simulation:** Asteroid Collision.
7. **Android:** back stack, undo/redo of edits.

#### 9. Edge Cases / Common Mistakes

1. `pop` or `peek` on an empty stack (`NoSuchElementException`). Check `isEmpty()` first or use `...OrNull()`.
2. Mixing up the ends of a `Deque`: Java's `push` adds to the **front**; Kotlin's `addLast` adds to the **back**. Be consistent.
3. Using `java.util.Stack` and `ArrayDeque` in the same code.
4. Forgetting what is left in the stack after the loop ends.
5. Using a stack when you need FIFO order.
6. Deep recursion instead of an explicit stack (`StackOverflowError`).
7. Assuming `peek` removes the item.

#### 10. When to Use / When Not to Use

**Use when:**

1. The most recent unresolved item matters most.
2. Things are nested or paired.
3. You need to undo or go back.

**Avoid when:**

1. You need the oldest item first (queue).
2. You need the best item first (priority queue / heap).
3. You need random access (array).

#### 11. Related Topics

1. Stack Operations & Complexity
2. Stack Implementation
3. Queue (`01-data-structure/04-Queue`)
4. Monotonic Stack (`03-leetcode-patterns`, topic 10)

#### 12. Interview Must Remember

1. **LIFO: push and pop at the same end.**
2. In Kotlin use `ArrayDeque` with `addLast` / `removeLast` / `last()`.
3. All main operations are `O(1)`.
4. Think "stack" when you see matching, nesting, undo, or "next greater".
