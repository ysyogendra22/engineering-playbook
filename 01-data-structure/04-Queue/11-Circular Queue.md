# Circular Queue

#### 1. What Is It?

A **circular queue** (also called a **ring buffer**) is a queue built on a **fixed-size array** whose end connects back to its start.

When an index reaches the end of the array, it **wraps around** to index 0. This is done with the `%` (remainder) operator: `(index + 1) % capacity`.

Why it exists:

- A plain array queue wastes the free space at the front after items are removed. A circular queue **reuses** it.
- Memory is **fixed**, which is what buffers need (audio, sensor data, logs).
- Both `enqueue` and `dequeue` stay `O(1)` and **no items are shifted**.

*Design Circular Queue* (LeetCode 622) is a common design question. Kotlin's own `ArrayDeque` is a growing circular array inside.

#### 2. How It Works

Keep an array `data`, an index `head` (where the front item is), and `size` (how many items).

```text
Next free slot = (head + size) % capacity
Front item     = data[head]
Rear item      = data[(head + size - 1) % capacity]
```

Capacity 4:

```text
start: head=0, size=0
enqueue 1 → slot (0+0)%4 = 0   [1 _ _ _]  size 1
enqueue 2 → slot (0+1)%4 = 1   [1 2 _ _]  size 2
enqueue 3 → slot (0+2)%4 = 2   [1 2 3 _]  size 3
dequeue   → head = (0+1)%4 = 1             size 2     front is 2
enqueue 4 → slot (1+2)%4 = 3   [1 2 3 4]  size 3
enqueue 5 → slot (1+3)%4 = 0   [5 2 3 4]  size 4     wrapped to index 0
enqueue 6 → full → rejected
```

**Why keep `size`?** If you only keep `head` and `tail`, an *empty* queue and a *full* queue both look like `head == tail`. A `size` counter removes the doubt.

#### 3. Kotlin Code

```kotlin
// Design Circular Queue (LeetCode 622)
class MyCircularQueue(private val capacity: Int) {
    private val data = IntArray(capacity)
    private var head = 0
    private var size = 0

    fun enQueue(value: Int): Boolean {
        if (isFull()) return false
        data[(head + size) % capacity] = value
        size++
        return true
    }

    fun deQueue(): Boolean {
        if (isEmpty()) return false
        head = (head + 1) % capacity
        size--
        return true
    }

    fun front(): Int = if (isEmpty()) -1 else data[head]

    fun rear(): Int = if (isEmpty()) -1 else data[(head + size - 1) % capacity]

    fun isEmpty(): Boolean = size == 0

    fun isFull(): Boolean = size == capacity
}

// A ring buffer that keeps the LAST `capacity` items (new items overwrite the oldest)
class RingBuffer<T>(private val capacity: Int) {
    private val data = arrayOfNulls<Any?>(capacity)
    private var head = 0
    private var size = 0

    fun add(item: T) {
        if (size == capacity) {
            data[head] = item                          // overwrite the oldest
            head = (head + 1) % capacity
        } else {
            data[(head + size) % capacity] = item
            size++
        }
    }

    @Suppress("UNCHECKED_CAST")
    fun toList(): List<T> = List(size) { data[(head + it) % capacity] as T }
}

// Usage
val q = MyCircularQueue(3)
println(q.enQueue(1))   // true
println(q.enQueue(2))   // true
println(q.enQueue(3))   // true
println(q.enQueue(4))   // false: full
println(q.rear())       // 3
println(q.deQueue())    // true
println(q.enQueue(4))   // true: the freed slot is reused
println(q.rear())       // 4

val log = RingBuffer<String>(3)
listOf("a", "b", "c", "d", "e").forEach { log.add(it) }
println(log.toList())   // [c, d, e]
```

#### 4. Complexity

| Action | Time |
|---|---|
| `enQueue`, `deQueue`, `front`, `rear`, `isEmpty`, `isFull` | `O(1)` |
| Memory | `O(capacity)`, fixed |

#### 5. Common Mistakes

1. **Using only `head` and `tail`**, so empty and full look the same. Keep `size`.
2. **Forgetting `% capacity`** when moving an index.
3. **Wrong rear index.** It is `(head + size - 1) % capacity`.
4. **Capacity `0`** (remainder by zero).
5. **Overwriting when full** when the question expects `false`.
6. **Not changing `size`** after enqueue or dequeue.

#### 6. Say This in the Interview

1. "I use a fixed array with a `head` index and a `size` counter."
2. "Indexes wrap with `% capacity`. The next free slot is `(head + size) % capacity`."
3. "All operations are `O(1)` and no item is ever shifted."
4. "A `size` counter tells me empty from full."

#### 7. Quick Check

1. Capacity 5, `head = 3`, `size = 4`. Where is the next free slot?
2. Why do we use `%`?

<details>
<summary>Answers</summary>

1. `(3 + 4) % 5 = 2`.
2. To wrap an index back to 0 when it goes past the end of the array.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 622 | Design Circular Queue (Medium) | this note |
| 641 | Design Circular Deque (Medium) | ring buffer with two ends |
| 503 | Next Greater Element II (Medium) | circular array with `i % n` |
| 346 | Moving Average from Data Stream (Easy, premium) | fixed window of the last N |
