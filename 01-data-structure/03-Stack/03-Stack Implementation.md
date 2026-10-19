# Stack Implementation

#### 1. Definition — Must Know

1. Implementing a stack means building `push`, `pop`, `peek` and `isEmpty` yourself on top of a simpler structure.
2. The two classic designs are **array based** (including Kotlin's `ArrayDeque`) and **linked-list based**.
3. In real code you use `ArrayDeque`. Interviewers ask for a manual version to see if you understand the details.

#### 2. Why It Is Used — Must Know

1. "Implement a stack" is a common warm-up question.
2. It tests array resizing, pointers, and handling empty/full cases.
3. It leads to related designs: Min Stack, queue from two stacks.

#### 3. How It Works — Must Know

**Array-based.** Keep an array and an index `size` that points to the next free slot. The top is at `size - 1`.

```text
array:  [ 10 | 20 | 30 |    |    ]      size = 3
                    ↑ top (index size-1)

push(40): array[size] = 40; size++      → [10, 20, 30, 40, _]
pop():    size--; return array[size]    → returns 40, size = 3
When size == array.size on push → make a new array twice as big and copy (amortized O(1)).
```

**Linked-list-based.** Keep only a `top` pointer. A push makes a new node that points to the old top. A pop moves `top` to the next node.

```text
top → [30] → [20] → [10] → null

push(40): new node 40 whose next = old top;  top = new node
pop():    value = top.value;  top = top.next
```

#### 4. Core Concepts — Must Know

| Design | Push | Pop | Memory | Notes |
|---|---:|---:|---|---|
| Dynamic array (`ArrayDeque`, `ArrayList`) | `O(1)` amortized | `O(1)` | compact | best in practice |
| Fixed array | `O(1)` | `O(1)` | fixed | can overflow |
| Linked list | `O(1)` | `O(1)` | one node per item, pointers | no resize, more memory |

1. **Array:** the top is the **last used index**, so pushing and popping never shift items.
2. **Doubling** the array when full makes push `O(1)` *amortized*.
3. **Linked list:** the top is the **head**. All work is at the head, so no tail pointer is needed.
4. **Empty check:** array → `size == 0`. Linked list → `top == null`.
5. **Generic type:** use `Stack<T>` so the class works for any item.
6. **Clear popped slots** in an object array (`data[size] = null`) so the garbage collector can free memory.
7. **Kotlin's `ArrayDeque`** already gives you everything.

#### 5. Algorithm — Must Know

```text
Array stack:
  push(x): if size == capacity: grow ×2;  data[size++] = x
  pop():   if size == 0: error;  return data[--size]
  peek():  if size == 0: error;  return data[size - 1]

Linked stack:
  push(x): top = Node(x, next = top)
  pop():   if top == null: error;  value = top.value;  top = top.next;  return value
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// 1. Array-based stack of Ints with growth
class ArrayStack(initialCapacity: Int = 4) {
    private var data = IntArray(initialCapacity)
    var size = 0
        private set

    fun isEmpty() = size == 0

    fun push(x: Int) {
        if (size == data.size) data = data.copyOf(data.size * 2)   // double
        data[size++] = x
    }

    fun pop(): Int {
        if (isEmpty()) throw NoSuchElementException("Stack is empty")
        return data[--size]
    }

    fun peek(): Int {
        if (isEmpty()) throw NoSuchElementException("Stack is empty")
        return data[size - 1]
    }
}

// 2. Linked-list-based generic stack
class LinkedStack<T> {
    private class Node<T>(val value: T, val next: Node<T>?)

    private var top: Node<T>? = null
    var size = 0
        private set

    fun isEmpty() = top == null

    fun push(x: T) {
        top = Node(x, top)
        size++
    }

    fun pop(): T {
        val node = top ?: throw NoSuchElementException("Stack is empty")
        top = node.next
        size--
        return node.value
    }

    fun peek(): T = (top ?: throw NoSuchElementException("Stack is empty")).value
}

// 3. What you would really write: wrap ArrayDeque
class SimpleStack<T> {
    private val items = ArrayDeque<T>()
    fun push(x: T) = items.addLast(x)
    fun pop(): T = items.removeLast()
    fun peek(): T = items.last()
    fun isEmpty() = items.isEmpty()
    val size get() = items.size
}

// Usage
val s = LinkedStack<String>()
s.push("a"); s.push("b")
println(s.peek())   // b
println(s.pop())    // b
println(s.size)     // 1
```

A fixed-capacity stack (rejects pushes when full):

```kotlin
class BoundedStack(private val capacity: Int) {
    private val data = IntArray(capacity)
    private var size = 0
    fun push(x: Int): Boolean { if (size == capacity) return false; data[size++] = x; return true }
    fun pop(): Int? = if (size == 0) null else data[--size]
}
```

#### 7. Time & Space Complexity — Must Know

| Operation | Array (dynamic) | Linked list |
|---|---:|---:|
| `push` | `O(1)` amortized | `O(1)` |
| `pop` | `O(1)` | `O(1)` |
| `peek` | `O(1)` | `O(1)` |
| Space | `O(n)`, compact | `O(n)`, extra pointer per node |

Array doubling copies items sometimes (`O(n)`), but spread over many pushes it averages `O(1)`.

#### 8. Common Implementation Variations — Must Know

1. **Dynamic array stack** (Kotlin `ArrayDeque`).
2. **Linked-list stack** (head = top).
3. **Fixed-size stack** with overflow.
4. **Min Stack** — stack plus running minimum.
5. **Two stacks in one array** (low priority).
6. **Stack from two queues** (see "Stack Using Queues").
7. **Thread-safe stack** — synchronized wrapper or `ConcurrentLinkedDeque`.

#### 9. Edge Cases / Common Mistakes

1. Off-by-one: top is `size - 1`, next free slot is `size`.
2. Pop from an empty stack without a clear error.
3. Forgetting to resize, or resizing by a fixed amount (not doubling), making push `O(n)`.
4. Linked list: keeping a `tail` and pushing there, which makes pop `O(n)`.
5. Not clearing popped object slots (memory kept alive).
6. Returning `size` before decrementing in `pop`.
7. Using `java.util.Stack` in modern code.

#### 10. When to Use / When Not to Use

**Write it yourself when:**

1. The interviewer asks for it, or you need special behaviour (bounded, min tracking).

**Use `ArrayDeque` when:**

1. You just need a stack in your solution.

#### 11. Related Topics

1. Stack Operations & Complexity
2. Min Stack
3. Linked List (`01-data-structure/02-LinkedList`)
4. Queue Implementation (`01-data-structure/04-Queue/03-Queue Implementation.md`)

#### 12. Interview Must Remember

1. **Array stack: top = `size - 1`. Linked stack: top = head.**
2. Double the array when full → amortized `O(1)` push.
3. Handle underflow clearly.
4. In real code use `ArrayDeque`.
