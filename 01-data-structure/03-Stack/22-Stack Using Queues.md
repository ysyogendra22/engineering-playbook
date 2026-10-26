# Stack Using Queues

> The full version, with more cases, is in `01-data-structure/04-Queue/15-Stack Using Queues.md`. This note has what you need for the interview.

#### 1. What Is It?

Build a **stack** (LIFO) using only **queue** operations: add at the back, remove from the front, look at the front.

A queue gives the **oldest** item first. A stack must give the **newest** item first. So we must arrange the queue so that the **newest item is at the front**.

This is *Implement Stack using Queues* (LeetCode 225). It is the mirror of *Implement Queue using Stacks* (LeetCode 232).

#### 2. How It Works

**One queue.** After every `push`, **rotate** the queue: move the older items from the front to the back, so the new item ends up at the front.

```text
push(1):  add 1 → [1]                           nothing to rotate
push(2):  add 2 → [1, 2]    rotate 1 time:  1 goes to the back   → [2, 1]
push(3):  add 3 → [2, 1, 3] rotate 2 times: 2 then 1 go to the back → [3, 2, 1]

top() → 3     (the front)
pop() → 3     queue is now [2, 1]
```

Now `pop` and `top` are plain queue operations on the front.

Rotate exactly `size - 1` times. (Rotating `size` times brings the order back to where it started.)

#### 3. Kotlin Code

```kotlin
class MyStack {
    private val queue = ArrayDeque<Int>()          // use ONLY addLast / removeFirst / first

    fun push(x: Int) {
        queue.addLast(x)
        repeat(queue.size - 1) {                   // move the older items behind the new one
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

You may also be asked for the other choice: `push` is `O(1)` and `pop` rotates `size - 1` items. Say that you picked rotate-on-push because `pop` and `top` are then the most common, cheapest calls.

#### 4. Complexity

| Operation | Time |
|---|---|
| `push` | `O(n)` (the rotation) |
| `pop`, `top`, `empty` | `O(1)` |
| Space | `O(n)` |

#### 5. Common Mistakes

1. **Rotating `size` times** instead of `size - 1`.
2. **Rotating before adding** the new item.
3. **Using `removeLast()`.** That is a stack operation. The point is to use queue operations only.
4. **Popping an empty stack.** Say how you handle it.
5. **Saying `push` is `O(1)`** in the rotate-on-push design.

#### 6. Say This in the Interview

1. "A queue gives the oldest item first, so after each push I rotate the queue to put the newest item at the front."
2. "Push is `O(n)`. Pop and top are `O(1)`."
3. "In practice I would use a real stack, which is `O(1)` for everything."

#### 7. Quick Check

1. Queue is `[2, 1]`. You push `3`. What is the queue after the rotation?
2. How many rotations after pushing into a queue that now has 5 items?

<details>
<summary>Answers</summary>

1. `[3, 2, 1]`. Add 3 → `[2, 1, 3]`. Rotate 2 times.
2. `4` (`size - 1`).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) (Easy) | this note |
| 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) (Easy) | the mirror |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) (Medium) | store extra data with each item |
| 1381 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) (Medium) | stack design |
