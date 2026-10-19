# Queue Using Two Stacks

#### 1. Definition — Must Know

1. Build a **FIFO queue** using only **two LIFO stacks**.
2. The stacks are called `inStack` (for new items) and `outStack` (for items ready to leave).
3. When `outStack` is empty, **move everything** from `inStack` to `outStack`. This **reverses** the order, so the oldest item is now on top.
4. It is *Implement Queue using Stacks* (LeetCode 232).

#### 2. Why It Is Used — Must Know

1. It is a classic design question that tests if you understand LIFO vs FIFO.
2. It shows **amortized analysis**: each item moves between the stacks at most once.
3. The idea appears in real systems (functional queues, undo structures).

#### 3. How It Works — Must Know

A stack reverses order. Two reversals give back the original order.

```text
push(1), push(2), push(3)      → inStack: [1, 2, 3]  (top = 3)      outStack: []

pop():
    outStack is empty → move all from inStack:
        pop 3 → push to outStack
        pop 2 → push to outStack
        pop 1 → push to outStack
    inStack: []        outStack: [3, 2, 1]   (top = 1)
    pop from outStack → 1                    ✓ the first item added comes out first

push(4)                        → inStack: [4]                    outStack: [3, 2]

pop():  outStack not empty → pop → 2
pop():  outStack not empty → pop → 3
pop():  outStack empty → move [4] over → pop → 4
```

Rule: **only move when `outStack` is empty.** If you move while it still has items, the order breaks.

#### 4. Core Concepts — Must Know

1. **`push(x)`:** push onto `inStack`. `O(1)`.
2. **`pop()` / `peek()`:** if `outStack` is empty, move all items from `inStack`; then take from `outStack`.
3. **Amortized `O(1)`:** each item is pushed and popped at most twice in total (once per stack). So `n` operations cost `O(n)`.
4. **One `pop` can cost `O(n)`** (when it triggers the move). That is the worst case for a single call.
5. **`empty()`:** both stacks are empty.
6. **Alternative design:** make `push` expensive and `pop` cheap by moving items on every push. It is simpler but always `O(n)` per push.

| Design | `push` | `pop` / `peek` |
|---|---:|---:|
| Two stacks, lazy move | `O(1)` | amortized `O(1)` |
| Two stacks, move on every push | `O(n)` | `O(1)` |

#### 5. Algorithm — Must Know

```text
push(x):   inStack.push(x)
pop():     peek(); return outStack.pop()
peek():    if outStack is empty: while inStack is not empty: outStack.push(inStack.pop())
           return outStack.top()
empty():   inStack.isEmpty() and outStack.isEmpty()
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class MyQueue {
    private val inStack = ArrayDeque<Int>()      // use addLast / removeLast as push / pop
    private val outStack = ArrayDeque<Int>()

    fun push(x: Int) {
        inStack.addLast(x)
    }

    fun pop(): Int {
        moveIfNeeded()
        return outStack.removeLast()
    }

    fun peek(): Int {
        moveIfNeeded()
        return outStack.last()
    }

    fun empty(): Boolean = inStack.isEmpty() && outStack.isEmpty()

    private fun moveIfNeeded() {
        if (outStack.isEmpty()) {
            while (inStack.isNotEmpty()) {
                outStack.addLast(inStack.removeLast())
            }
        }
    }
}

// Usage
val q = MyQueue()
q.push(1); q.push(2); q.push(3)
println(q.pop())     // 1
q.push(4)
println(q.pop())     // 2
println(q.peek())    // 3
println(q.pop())     // 3
println(q.pop())     // 4
println(q.empty())   // true
```

Using the standard stack class:

```kotlin
import java.util.Stack
// Stack<Int>() works too, with push / pop / peek / isEmpty, but ArrayDeque is the modern choice.
```

#### 7. Time & Space Complexity — Must Know

| Operation | Worst single call | Amortized |
|---|---:|---:|
| `push` | `O(1)` | `O(1)` |
| `pop` | `O(n)` | `O(1)` |
| `peek` | `O(n)` | `O(1)` |
| `empty` | `O(1)` | `O(1)` |
| Space | `O(n)` | — |

**Why amortized `O(1)`:** an item is moved from `inStack` to `outStack` once, and removed once. So over `n` operations, total moves ≤ `n`.

#### 8. Common Related Patterns — Must Know

1. **Implement Queue using Stacks** (LeetCode 232).
2. **Implement Stack using Queues** (LeetCode 225) — the next note.
3. **Min Stack / Max Stack** — a stack that also tracks the min or max.
4. **Queue with Min/Max in `O(1)`** — two stacks, each storing the running min/max (a classic follow-up).
5. **Undo / redo** with two stacks.
6. **Persistent / functional queues** in functional languages use two lists the same way.

#### 9. Edge Cases / Common Mistakes

1. Moving items **every time** `pop` is called, even when `outStack` still has items. This breaks the order.
2. Moving items back to `inStack` after the pop. Not needed and not allowed in the lazy design.
3. Checking `empty()` using only one stack.
4. Pop or peek on an empty queue. State what you do (throw, or return a default).
5. Claiming `pop` is always `O(1)`. Say **amortized**.
6. Using the same `ArrayDeque` end for both roles by mistake.
7. Forgetting that `peek` also needs the move step.

#### 10. When to Use / When Not to Use

**Use when:**

1. The interviewer limits you to stack operations.
2. Reads happen in batches (the move cost spreads out).

**Avoid when:**

1. You can use a real queue (`ArrayDeque`). It is simpler and has worst-case `O(1)`.

#### 11. Related Topics

1. Stack Using Queues
2. Queue Implementation
3. Stack (`01-data-structure/03-Stack`)
4. Queue Fundamentals

#### 12. Interview Must Remember

1. **`inStack` for push. `outStack` for pop/peek. Move only when `outStack` is empty.**
2. Moving reverses the order, which turns LIFO into FIFO.
3. Amortized `O(1)`, worst single `pop` is `O(n)`.
4. `empty()` checks both stacks.
