# Stack Implementation

#### 1. What Is It?

"Implement a stack" means you build `push`, `pop`, `peek` and `isEmpty` yourself, using a simpler structure underneath.

There are two standard ways. Interviewers expect you to know both.

| Way | Idea |
|---|---|
| **Array** | keep an array and a number `size`. The top is at index `size - 1`. |
| **Linked list** | keep a pointer `top` to the newest node. Each node points to the one below it. |

In real code you just use `ArrayDeque`. You write your own only when asked.

#### 2. How It Works

**Array stack.** `size` is also the next free slot.

```text
data = [10, 20, 30, _, _]     size = 3     top item = data[size - 1] = 30

push(40):  data[3] = 40, size = 4        → [10, 20, 30, 40, _]
pop():     size = 3, return data[3]      → returns 40
```

When the array is full, make a new array **twice as big**, copy the items, and continue. This keeps `push` fast on average.

**Linked-list stack.** Always add and remove at the head, so no tail pointer is needed.

```text
top → [30] → [20] → [10] → null

push(40):  new node 40 points to the old top, then top = new node
           top → [40] → [30] → [20] → [10]
pop():     value = top.value, then top = top.next
```

#### 3. Kotlin Code

**Array version (with growth)**

```kotlin
class ArrayStack(capacity: Int = 4) {
    private var data = IntArray(capacity)
    private var size = 0

    fun isEmpty() = size == 0

    fun push(x: Int) {
        if (size == data.size) data = data.copyOf(data.size * 2)   // double when full
        data[size] = x
        size++
    }

    fun pop(): Int {
        if (isEmpty()) throw NoSuchElementException("Stack is empty")
        size--
        return data[size]
    }

    fun peek(): Int {
        if (isEmpty()) throw NoSuchElementException("Stack is empty")
        return data[size - 1]
    }
}
```

**Linked-list version**

```kotlin
class LinkedStack<T> {
    private class Node<T>(val value: T, val next: Node<T>?)

    private var top: Node<T>? = null

    fun isEmpty() = top == null

    fun push(x: T) {
        top = Node(x, top)               // new node points to the old top
    }

    fun pop(): T {
        val node = top ?: throw NoSuchElementException("Stack is empty")
        top = node.next
        return node.value
    }

    fun peek(): T = (top ?: throw NoSuchElementException("Stack is empty")).value
}
```

**Usage**

```kotlin
val s = LinkedStack<String>()
s.push("a"); s.push("b")
println(s.peek())   // b
println(s.pop())    // b
println(s.pop())    // a
println(s.isEmpty())// true
```

#### 4. Complexity

| Operation | Array stack | Linked-list stack |
|---|---|---|
| `push` | `O(1)` on average (an occasional resize costs `O(n)`) | `O(1)` |
| `pop`, `peek` | `O(1)` | `O(1)` |
| Memory | compact | one extra pointer per item |

#### 5. Common Mistakes

1. **Off-by-one.** The top is at `size - 1`. The next free slot is `size`.
2. **Not growing the array.** Pushing into a full array throws `ArrayIndexOutOfBoundsException`.
3. **Growing by a fixed amount** (for example +1). Then every push copies the array. **Double** it.
4. **Linked list: pushing at the tail.** Then `pop` needs to walk the whole list (`O(n)`).
5. **Not handling an empty stack** in `pop` and `peek`.

#### 6. Say This in the Interview

1. "I will use an array and a `size` counter. The top is at `size - 1`."
2. "When the array is full I double it, so push is `O(1)` on average."
3. "With a linked list, push and pop both happen at the head, so both are `O(1)`."
4. "In real code I would just use `ArrayDeque`."

#### 7. Quick Check

1. In an array stack with `size = 3`, where is the top item?
2. Why double the array instead of adding one slot?

<details>
<summary>Answers</summary>

1. At index `2` (`size - 1`).
2. Adding one slot means copying the whole array on every push (`O(n)` each time). Doubling copies rarely, so push averages `O(1)`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) (Medium) | stack that also returns the minimum in `O(1)` |
| 1381 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) (Medium) | array stack with a `size` counter |
| 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) (Easy) | build one structure from another |
| 225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) (Easy) | rotate the queue |
