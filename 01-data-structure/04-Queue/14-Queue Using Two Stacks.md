# Queue Using Two Stacks

#### 1. What Is It?

Build a **queue** (FIFO) using only **two stacks** (LIFO).

- `inStack` receives the new items (`push`).
- `outStack` gives the items out (`pop` / `peek`).

When `outStack` is empty, move **all** items from `inStack` to `outStack`. Moving **reverses** the order, so the oldest item ends up on top.

A stack reverses order. Two reversals give the original order back. That is the whole trick.

This is *Implement Queue using Stacks* (LeetCode 232). It is the mirror of *Implement Stack using Queues* (note 15).

#### 2. How It Works

```text
push 1, push 2, push 3     inStack: [1, 2, 3]  (3 on top)      outStack: []

pop():
    outStack is empty → move everything from inStack:
        take 3 → outStack,  take 2 → outStack,  take 1 → outStack
    inStack: []           outStack: [3, 2, 1]  (1 on top)
    pop from outStack → 1       ✓ the first item added comes out first

push 4                     inStack: [4]                         outStack: [3, 2]
pop() → 2                  (outStack is not empty, so no move)
pop() → 3
pop() → outStack is empty → move [4] over → pop → 4
```

**The key rule: move only when `outStack` is empty.** If you move while it still has items, the order breaks.

#### 3. Kotlin Code

```kotlin
class MyQueue {
    private val inStack = ArrayDeque<Int>()       // used as a stack: addLast / removeLast
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

#### 4. Complexity

| Action | One call (worst) | Average over many calls |
|---|---|---|
| `push` | `O(1)` | `O(1)` |
| `pop`, `peek` | `O(n)` (when it moves everything) | `O(1)` |
| `empty` | `O(1)` | `O(1)` |

**Why the average is `O(1)`:** each item is moved from `inStack` to `outStack` **at most once** and popped once. So `n` operations cost `O(n)` in total. This is called **amortized** `O(1)`.

#### 5. Common Mistakes

1. **Moving items on every `pop`**, even when `outStack` still has items. This breaks the order.
2. **Moving the items back** to `inStack` after the pop. Not needed.
3. **`empty()` checking only one stack.** Check both.
4. **Forgetting that `peek` also needs the move step.**
5. **Saying `pop` is always `O(1)`.** Say "amortized `O(1)`".

#### 6. Say This in the Interview

1. "A stack reverses order, so two stacks give FIFO."
2. "I push to `inStack`. For pop and peek, if `outStack` is empty I move everything over from `inStack`."
3. "Each item moves at most once, so every operation is amortized `O(1)`, even though one pop can take `O(n)`."

#### 7. Quick Check

1. When do you move items from `inStack` to `outStack`?
2. After `push 1, push 2, pop`, which item is left and where is it?

<details>
<summary>Answers</summary>

1. Only when `outStack` is empty and you need to pop or peek.
2. `2`, in `outStack` (the move put both items there, `1` came out).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 232 | Implement Queue using Stacks (Easy) | this note |
| 225 | Implement Stack using Queues (Easy) | the mirror |
| 155 | Min Stack (Medium) | stack with extra data |
| 622 | Design Circular Queue (Medium) | another queue design |
