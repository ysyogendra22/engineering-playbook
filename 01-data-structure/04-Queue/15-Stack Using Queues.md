# Stack Using Queues

#### 1. What Is It?

Build a **stack** (LIFO) using only **queue** operations: add at the back, remove from the front, look at the front.

A queue gives the **oldest** item first. A stack must give the **newest** item first. So we must arrange the queue so that the **newest item is at the front**.

The tool is **rotation**: move the front item to the back (`addLast(removeFirst())`).

This is *Implement Stack using Queues* (LeetCode 225). It is the mirror of *Implement Queue using Stacks* (note 14).

#### 2. How It Works

**One queue, rotate on push.** After adding the new item, rotate the queue so the new item reaches the front.

```text
push(1):  [1]
push(2):  add 2 → [1, 2]      rotate 1 time: 1 moves to the back   → [2, 1]
push(3):  add 3 → [2, 1, 3]   rotate 2 times: 2 then 1 move back   → [3, 2, 1]

top() → 3      (the front)
pop() → 3      queue is now [2, 1]
```

Rotate exactly **`size - 1`** times. Rotating `size` times brings you back to where you started.

The other choice is **cheap push, costly pop**: `push` just adds at the back. `pop` first rotates `size - 1` items, so the newest reaches the front, and then removes it. Both are valid. Rotate-on-push is the usual answer because `pop` and `top` become `O(1)`.

#### 3. Kotlin Code

```kotlin
class MyStack {
    private val queue = ArrayDeque<Int>()      // use ONLY addLast / removeFirst / first

    fun push(x: Int) {
        queue.addLast(x)
        repeat(queue.size - 1) {               // older items go behind the new one
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

#### 4. Complexity

| Action | Time |
|---|---|
| `push` | `O(n)` (the rotation) |
| `pop`, `top`, `empty` | `O(1)` |
| Memory | `O(n)` |

#### 5. Common Mistakes

1. **Rotating `size` times** instead of `size - 1`.
2. **Rotating before adding** the new item.
3. **Using `removeLast()`.** That is a stack operation. Use queue operations only.
4. **Pop or top on an empty stack.** Say how you handle it.
5. **Saying `push` is `O(1)`** in the rotate-on-push design.

#### 6. Say This in the Interview

1. "A queue gives the oldest item first, so after each push I rotate the queue to put the newest item at the front."
2. "Push is `O(n)`. Pop and top are `O(1)`."
3. "In real code I would use a real stack, which is `O(1)` for everything."

#### 7. Quick Check

1. The queue is `[2, 1]` and you push `3`. What is the queue after the rotation?
2. How many rotations after pushing into a queue that now holds 5 items?

<details>
<summary>Answers</summary>

1. `[3, 2, 1]`. Add 3 → `[2, 1, 3]`, then rotate 2 times.
2. `4` (`size - 1`).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 225 | Implement Stack using Queues (Easy) | this note |
| 232 | Implement Queue using Stacks (Easy) | the mirror (note 14) |
| 155 | Min Stack (Medium) | stack with extra data |
| 1381 | Design a Stack With Increment Operation (Medium) | stack design |
