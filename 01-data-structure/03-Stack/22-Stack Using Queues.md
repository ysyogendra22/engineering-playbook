# Stack Using Queues

#### 1. Definition — Must Know

1. Build a **LIFO stack** using only **queue** operations (`addLast` to enqueue, `removeFirst` to dequeue, `first` to peek).
2. A queue gives the *oldest* item first, so we must arrange the queue so that the *newest* item is at the front.
3. It is *Implement Stack using Queues* (LeetCode 225). The full version of this note, with both designs and more cases, is in `01-data-structure/04-Queue/15-Stack Using Queues.md`.

#### 2. Why It Is Used — Must Know

1. It is the mirror of "Queue using two stacks". Interviewers often ask both together.
2. It tests whether you really understand LIFO vs FIFO.
3. It trains the **rotate** operation: `queue.addLast(queue.removeFirst())`.

#### 3. How It Works — Must Know

**One-queue method.** After every `push`, rotate the queue so the newest item reaches the front.

```text
push(1):  [1]                          nothing to rotate
push(2):  add 2 → [1, 2]    rotate 1 time (1 goes to the back)  → [2, 1]
push(3):  add 3 → [2, 1, 3] rotate 2 times                       → [3, 2, 1]

top() → 3  (front)
pop() → 3  → queue [2, 1]
```

Now `pop` and `top` are plain queue operations on the front.

```text
Stack view (top on the left):   3 2 1
Queue view (front on the left): 3 2 1      ← the same order after rotation
```

#### 4. Core Concepts — Must Know

1. **Costly push, cheap pop** (the usual choice): `push` rotates `size - 1` times, `pop`/`top` are `O(1)`.
2. **Costly pop, cheap push** (the other choice): `push` is `O(1)`; `pop` rotates `size - 1` items so the last one reaches the front, then removes it.
3. **One queue is enough.** The second queue in textbook solutions only does what rotation does.
4. **Rotate exactly `size - 1` times.** Rotating `size` times returns to the start.
5. **`empty()`** is just `queue.isEmpty()`.
6. **Compared with a real stack**, this is slower. It exists to test understanding.

| Design | `push` | `pop` | `top` |
|---|---:|---:|---:|
| Rotate on push | `O(n)` | `O(1)` | `O(1)` |
| Rotate on pop | `O(1)` | `O(n)` | `O(n)` |
| Real stack (`ArrayDeque`) | `O(1)` | `O(1)` | `O(1)` |

#### 5. Algorithm — Must Know

```text
push(x):   queue.addLast(x);  repeat(queue.size - 1) { queue.addLast(queue.removeFirst()) }
pop():     return queue.removeFirst()
top():     return queue.first()
empty():   return queue.isEmpty()
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class MyStack {
    private val queue = ArrayDeque<Int>()          // used ONLY as a queue: addLast / removeFirst / first

    fun push(x: Int) {
        queue.addLast(x)
        repeat(queue.size - 1) {                   // older items go behind the new one
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
println(s.empty())   // false
```

Rotate-on-pop variant (cheap push):

```kotlin
class MyStackCheapPush {
    private val queue = ArrayDeque<Int>()

    fun push(x: Int) { queue.addLast(x) }

    fun pop(): Int {
        repeat(queue.size - 1) { queue.addLast(queue.removeFirst()) }
        return queue.removeFirst()
    }

    fun top(): Int {
        repeat(queue.size - 1) { queue.addLast(queue.removeFirst()) }
        val value = queue.first()
        queue.addLast(queue.removeFirst())        // rotate the last one back
        return value
    }

    fun empty() = queue.isEmpty()
}
```

#### 7. Time & Space Complexity — Must Know

| Operation | Rotate on push |
|---|---:|
| `push` | `O(n)` |
| `pop` | `O(1)` |
| `top` | `O(1)` |
| `empty` | `O(1)` |
| Space | `O(n)` |

`n` pushes cost `O(n²)` in total with this design.

#### 8. Common Related Patterns — Must Know

1. **Implement Stack using Queues** (LeetCode 225).
2. **Implement Queue using Stacks** (LeetCode 232) (`01-data-structure/04-Queue/14-Queue Using Two Stacks.md`).
3. **Min Stack** — extra info per item.
4. **Reverse a queue** with a stack, or reverse a stack with a queue.
5. **Rotation in simulations:** hot potato, round-robin.

#### 9. Edge Cases / Common Mistakes

1. Rotating `size` times instead of `size - 1`.
2. Rotating before adding the new item.
3. Using `removeLast()` and thereby using stack operations, defeating the exercise.
4. Pop or top on an empty stack (`NoSuchElementException`). State how you handle it.
5. Claiming `push` is `O(1)` in the rotate-on-push design.
6. Rotate-on-pop `top()`: forgetting to put the last item back at the end of the queue.

#### 10. When to Use / When Not to Use

**Use when:**

1. The problem limits you to queue operations.

**Avoid when:**

1. You can use a real stack. It is simpler and `O(1)` for everything.

#### 11. Related Topics

1. Stack Implementation
2. Queue Using Two Stacks (`01-data-structure/04-Queue/14-Queue Using Two Stacks.md`)
3. Stack Using Queues — full version in the Queue folder (`01-data-structure/04-Queue/15-Stack Using Queues.md`)
4. Min Stack

#### 12. Interview Must Remember

1. **After each push, rotate `size − 1` times so the newest item is at the front.**
2. Then `pop` and `top` are plain queue operations.
3. One queue is enough. Push is `O(n)`.
4. Know both directions: stack from queues, queue from stacks.
