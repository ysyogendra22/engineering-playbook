# Queue Implementation

#### 1. What Is It?

"Implement a queue" means you build `enqueue`, `dequeue`, `peek` and `isEmpty` yourself, using something simpler underneath.

| Way | Idea | Good or bad |
|---|---|---|
| **Linked list** (`head` + `tail`) | add at the tail, remove at the head | both `O(1)`. This is the standard answer. |
| **Circular array** | an array whose end wraps to its start | both `O(1)`, fixed size (note 11) |
| **Plain array, shift on dequeue** | remove index 0 and shift everything | `O(n)` dequeue. **Bad.** |
| **Two stacks** | see note 14 | amortized `O(1)` |

In real code you use `ArrayDeque`. You write your own only when asked.

#### 2. How It Works

Keep two pointers: `head` (the front) and `tail` (the back).

```text
head → [A] → [B] → [C] ← tail

enqueue(D):   tail.next = new node D, then tail = D
              head → [A] → [B] → [C] → [D] ← tail

dequeue():    value = head.value, then head = head.next
              returns A.   head → [B] → [C] → [D]
```

One special case: when the **last** item is removed, `head` becomes `null`. You must also set `tail = null`. Otherwise `tail` still points to a removed node, and the next `enqueue` links to it by mistake.

Why not just a `head` pointer? Then `enqueue` would walk the whole list to find the end (`O(n)`). The `tail` pointer makes it `O(1)`.

#### 3. Kotlin Code

```kotlin
class LinkedQueue<T> {
    private class Node<T>(val value: T) {
        var next: Node<T>? = null
    }

    private var head: Node<T>? = null
    private var tail: Node<T>? = null
    var size = 0
        private set

    fun isEmpty() = size == 0

    fun enqueue(value: T) {
        val node = Node(value)
        val last = tail
        if (last == null) {
            head = node                          // the queue was empty
        } else {
            last.next = node
        }
        tail = node
        size++
    }

    fun dequeue(): T {
        val first = head ?: throw NoSuchElementException("Queue is empty")
        head = first.next
        if (head == null) tail = null            // the queue became empty
        size--
        return first.value
    }

    fun peek(): T = (head ?: throw NoSuchElementException("Queue is empty")).value
}

// Usage
val q = LinkedQueue<Int>()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
println(q.dequeue())   // 1
println(q.peek())      // 2
println(q.size)        // 2
```

What you would really write in an Android project:

```kotlin
class SimpleQueue<T> {
    private val items = ArrayDeque<T>()
    fun enqueue(value: T) = items.addLast(value)
    fun dequeue(): T = items.removeFirst()
    fun peek(): T = items.first()
    fun isEmpty() = items.isEmpty()
}
```

#### 4. Complexity

| Action | Linked list | `ArrayDeque` |
|---|---|---|
| `enqueue` | `O(1)` | `O(1)` on average |
| `dequeue` | `O(1)` | `O(1)` |
| `peek` | `O(1)` | `O(1)` |
| Memory | one node per item | compact |

#### 5. Common Mistakes

1. **Forgetting `tail = null`** when the queue becomes empty.
2. **Only keeping `head`.** Then `enqueue` is `O(n)`.
3. **Array version that shifts items** on every dequeue.
4. **Not updating `size`.**
5. **Not handling dequeue on an empty queue** (throw a clear error or return `null`).

#### 6. Say This in the Interview

1. "I will use a linked list with a `head` and a `tail` pointer. Enqueue adds at the tail and dequeue removes at the head, so both are `O(1)`."
2. "When the last item is removed, I also reset the tail."
3. "In production I would use `ArrayDeque`."

#### 7. Quick Check

1. Why do we need a `tail` pointer?
2. After you dequeue the only item, what must `head` and `tail` be?

<details>
<summary>Answers</summary>

1. So `enqueue` can add at the back in `O(1)` without walking the list.
2. Both `null`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 232 | Implement Queue using Stacks (Easy) | queue from two stacks |
| 622 | Design Circular Queue (Medium) | fixed array that wraps |
| 641 | Design Circular Deque (Medium) | ring buffer with two ends |
| 225 | Implement Stack using Queues (Easy) | the mirror |
