# Queue Implementation

#### 1. Definition — Must Know

1. Implementing a queue means building `enqueue`, `dequeue`, `peek` and `isEmpty` yourself on top of a simpler structure.
2. The two main designs are **linked-list based** and **array based**.
3. In real code you use `ArrayDeque`. Interviewers ask for a manual version to see if you understand the pointers or indices.

#### 2. Why It Is Used — Must Know

1. It is a common design question ("implement a queue").
2. It shows if you can keep `O(1)` for both ends.
3. It leads to related designs: circular queue, queue with two stacks.

#### 3. How It Works — Must Know

**Linked-list queue.** Keep a `head` (front) and a `tail` (back).

```text
head → [A] → [B] → [C] ← tail

enqueue(D):  tail.next = new node D;  tail = D
dequeue():   value = head.value;      head = head.next   (if head becomes null, tail = null)
```

**Array queue (naive, wrong).** Dequeue by removing index 0 shifts every item: `O(n)`.

**Array queue (better).** Keep a `head` index. Dequeue just moves `head` forward. The array may grow, and the unused front space is wasted, so a real design wraps around (a **circular queue**, a separate note) or compacts occasionally.

```text
array: [A][B][C][D][ ][ ]
        ↑head    ↑tail (next free slot)
dequeue: head moves to 1  → A is "gone" (slot kept, not reused until the array is compacted or wraps)
```

#### 4. Core Concepts — Must Know

| Design | Enqueue | Dequeue | Notes |
|---|---:|---:|---|
| Linked list (`head` + `tail`) | `O(1)` | `O(1)` | one object per item; no resize |
| Dynamic array + `head` index | `O(1)` amortized | `O(1)` | needs compaction or wrap-around |
| Circular array | `O(1)` | `O(1)` | fixed capacity (or resize) |
| Dynamic array + `removeAt(0)` | `O(1)` | **`O(n)`** | avoid |
| Two stacks | `O(1)` | amortized `O(1)` | see "Queue Using Two Stacks" |

1. **Keep both ends.** A singly linked list with only `head` makes enqueue `O(n)`. A `tail` pointer fixes it.
2. **Empty case:** when the last item is removed, set `tail = null` too.
3. **Generic type:** use `Queue<T>` so the class works for any item.
4. **Kotlin's `ArrayDeque`** is a circular, growing array under the hood.

#### 5. Algorithm — Must Know

```text
enqueue(x):
    node = Node(x)
    if tail == null: head = node; tail = node
    else: tail.next = node; tail = node
    size++

dequeue():
    if head == null: error (empty)
    value = head.value
    head = head.next
    if head == null: tail = null
    size--
    return value
```

#### 6. Kotlin Implementation — Must Know

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
            head = node
        } else {
            last.next = node
        }
        tail = node
        size++
    }

    fun dequeue(): T {
        val first = head ?: throw NoSuchElementException("Queue is empty")
        head = first.next
        if (head == null) tail = null           // the queue became empty
        size--
        return first.value
    }

    fun peek(): T = (head ?: throw NoSuchElementException("Queue is empty")).value
}

// Usage
val q = LinkedQueue<Int>()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
println(q.dequeue())     // 1
println(q.peek())        // 2
println(q.size)          // 2
```

A simple wrapper over `ArrayDeque` (what you would really write):

```kotlin
class SimpleQueue<T> {
    private val items = ArrayDeque<T>()
    fun enqueue(value: T) = items.addLast(value)
    fun dequeue(): T = items.removeFirst()
    fun peek(): T = items.first()
    fun isEmpty() = items.isEmpty()
    val size get() = items.size
}
```

#### 7. Time & Space Complexity — Must Know

| Operation | Linked list | `ArrayDeque` wrapper |
|---|---:|---:|
| `enqueue` | `O(1)` | `O(1)` amortized |
| `dequeue` | `O(1)` | `O(1)` |
| `peek` | `O(1)` | `O(1)` |
| Space | `O(n)` (a node per item) | `O(n)` (compact) |

#### 8. Common Implementation Variations — Must Know

1. **Linked list with `head` and `tail`.**
2. **Circular array** with a fixed size (LeetCode 622).
3. **Dynamic array that doubles** when full.
4. **Two stacks** (LeetCode 232).
5. **Bounded queue** that rejects or blocks on full.
6. **Generic queue** with `T`.
7. **Thread-safe queue** (`ConcurrentLinkedQueue`, `LinkedBlockingQueue`).

#### 9. Edge Cases / Common Mistakes

1. Forgetting to set `tail = null` when the queue becomes empty. The next `enqueue` then links to a dead node.
2. Only keeping `head`, making `enqueue` `O(n)`.
3. Dequeue on an empty queue without a clear error or `null`.
4. Not updating `size`.
5. Array version: shifting all items on every dequeue.
6. Peeking after `dequeue` of the last item.
7. Returning the node instead of the value.

#### 10. When to Use / When Not to Use

**Write it yourself when:**

1. The interviewer asks for it, or you need special behaviour (bounded, blocking).

**Use `ArrayDeque` when:**

1. You just need a queue. It is faster and well tested.

#### 11. Related Topics

1. Circular Queue
2. Queue Using Two Stacks
3. Linked List (`01-data-structure/02-LinkedList`)
4. Queue Operations

#### 12. Interview Must Remember

1. **Linked list + `head` + `tail` = `O(1)` enqueue and dequeue.**
2. Reset `tail` to `null` when the last item leaves.
3. Never use `removeAt(0)` on an array-backed list.
4. In real code, use `ArrayDeque`.
