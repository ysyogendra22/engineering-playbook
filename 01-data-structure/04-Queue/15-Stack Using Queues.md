# Stack Using Queues

#### 1. Definition — Must Know

1. Build a **LIFO stack** using only **queue** operations (add at the back, remove from the front).
2. A queue gives the *oldest* item first, so the trick is to arrange the queue so that the *newest* item is at the front.
3. It is *Implement Stack using Queues* (LeetCode 225).

#### 2. Why It Is Used — Must Know

1. It is the mirror of "Queue using two stacks". Interviewers often ask both.
2. It tests whether you understand FIFO vs LIFO well enough to convert one into the other.
3. It trains the **rotate** operation: `addLast(removeFirst())`.

#### 3. How It Works — Must Know

**Single-queue method.** After every `push`, rotate the queue so the new item is at the front.

```text
push(1):   add 1 → [1]                 rotate (size-1 = 0 times)           [1]
push(2):   add 2 → [1, 2]              rotate 1 time: move 1 to the back   [2, 1]
push(3):   add 3 → [2, 1, 3]           rotate 2 times: move 2, then 1      [3, 2, 1]

top()  → 3 (front)
pop()  → remove front 3                                                    [2, 1]
```

Now the front is always the newest item, so `pop` and `top` are simple queue operations.

**Two-queue method (the other common answer).** Add to `q2`, move everything from `q1` into `q2`, then swap the two queues' roles. Same cost, more code.

#### 4. Core Concepts — Must Know

1. **Costly push, cheap pop** (usual choice): `push` is `O(n)`, `pop` and `top` are `O(1)`.
2. **Costly pop, cheap push** (alternative): `push` is `O(1)`; `pop` rotates `size - 1` items so the last one reaches the front.
3. **One queue is enough.** Rotation does what the second queue did.
4. **Rotation:** `repeat(size - 1) { queue.addLast(queue.removeFirst()) }`.
5. **`empty()`:** the queue is empty.
6. **Order check:** after each push, the front must be the newest element.

| Design | `push` | `pop` | `top` |
|---|---:|---:|---:|
| Rotate on push | `O(n)` | `O(1)` | `O(1)` |
| Rotate on pop | `O(1)` | `O(n)` | `O(n)` |

#### 5. Algorithm — Must Know

```text
push(x):
    queue.addLast(x)
    repeat(queue.size - 1): queue.addLast(queue.removeFirst())

pop():   return queue.removeFirst()
top():   return queue.first()
empty(): return queue.isEmpty()
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class MyStack {
    private val queue = ArrayDeque<Int>()

    fun push(x: Int) {
        queue.addLast(x)
        repeat(queue.size - 1) {                  // rotate: older items go behind the new one
            queue.addLast(queue.removeFirst())
        }
    }

    fun pop(): Int = queue.removeFirst()

    fun top(): Int = queue.first()

    fun empty(): Boolean = queue.isEmpty()
}

// Usage
val s = MyStack()
s.push(1); s.push(2); s.push(3)
println(s.top())     // 3
println(s.pop())     // 3
println(s.pop())     // 2
s.push(4)
println(s.pop())     // 4
println(s.pop())     // 1
println(s.empty())   // true
```

Two-queue version (for comparison):

```kotlin
class MyStackTwoQueues {
    private var main = ArrayDeque<Int>()
    private var helper = ArrayDeque<Int>()

    fun push(x: Int) {
        helper.addLast(x)                         // new item goes first in the helper
        while (main.isNotEmpty()) helper.addLast(main.removeFirst())
        val temp = main; main = helper; helper = temp     // swap roles
    }

    fun pop(): Int = main.removeFirst()
    fun top(): Int = main.first()
    fun empty(): Boolean = main.isEmpty()
}
```

#### 7. Time & Space Complexity — Must Know

| Operation | One queue (rotate on push) |
|---|---:|
| `push` | `O(n)` |
| `pop` | `O(1)` |
| `top` | `O(1)` |
| `empty` | `O(1)` |
| Space | `O(n)` |

A sequence of `n` pushes costs `O(n²)` in total with this design.

#### 8. Common Related Patterns — Must Know

1. **Implement Stack using Queues** (LeetCode 225).
2. **Implement Queue using Stacks** (LeetCode 232).
3. **Min Stack** (LeetCode 155) and **Max Stack**.
4. **Reverse a queue** using a stack (and the reverse).
5. **Design a stack with increment** or with frequency (Maximum Frequency Stack).
6. **Rotation as a tool:** hot potato, round-robin scheduling.

#### 9. Edge Cases / Common Mistakes

1. Rotating `size` times instead of `size - 1` (the order returns to where it started, so nothing changes).
2. Rotating **before** adding the new item.
3. Using `ArrayDeque.removeLast()` and thereby using stack operations, which defeats the exercise.
4. Pop or top on an empty stack (`NoSuchElementException`). State how you handle it.
5. Claiming `push` is `O(1)` for the rotate-on-push design.
6. In the two-queue version: forgetting to swap the queues after a push.
7. Forgetting that the one-queue version is the cleanest answer to mention.

#### 10. When to Use / When Not to Use

**Use when:**

1. The problem or interviewer limits you to queue operations.

**Avoid when:**

1. You can use a real stack (`ArrayDeque` with `addLast`/`removeLast`). It is `O(1)` for everything.

#### 11. Related Topics

1. Queue Using Two Stacks
2. Queue Operations
3. Stack (`01-data-structure/03-Stack`)
4. Queue Traversal / Processing (rotation)

#### 12. Interview Must Remember

1. **After each push, rotate `size - 1` times so the newest item is at the front.**
2. `pop` and `top` are then plain queue operations (`O(1)`). `push` is `O(n)`.
3. One queue is enough.
4. Know both directions: queue from two stacks, stack from queues.
