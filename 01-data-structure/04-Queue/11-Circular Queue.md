# Circular Queue

#### 1. Definition — Must Know

1. A **circular queue** (ring buffer) is a queue built on a **fixed-size array** whose end connects back to its start.
2. When an index reaches the end of the array, it **wraps around** to index 0 using the modulo operator `%`.
3. This reuses the free space at the front, so both `enqueue` and `dequeue` stay `O(1)` and no items are shifted.

#### 2. Why It Is Used — Must Know

1. A plain array queue wastes the space at the front after dequeues. A circular queue reuses it.
2. It has a **fixed, predictable memory size**, which is important for buffers (audio, sensor data, logs, network packets).
3. *Design Circular Queue* (LeetCode 622) is a common design question.
4. Kotlin's own `ArrayDeque` is a growing circular array inside.

#### 3. How It Works — Must Know

Capacity 4. Keep `head` (index of the front item) and `size` (how many items).

Trace with the formula `slot = (head + size) % capacity`:

```text
start: head=0, size=0
enqueue 1 → slot (0+0)%4 = 0   [1 _ _ _]  size 1
enqueue 2 → slot (0+1)%4 = 1   [1 2 _ _]  size 2
enqueue 3 → slot (0+2)%4 = 2   [1 2 3 _]  size 3
dequeue   → head = (0+1)%4 = 1             size 2    front is now 2
enqueue 4 → slot (1+2)%4 = 3   [1 2 3 4]  size 3
enqueue 5 → slot (1+3)%4 = 0   [5 2 3 4]  size 4     wrapped to index 0!
enqueue 6 → full → rejected
```

Front item = `data[head]`. Rear item = `data[(head + size - 1) % capacity]`.

#### 4. Core Concepts — Must Know

1. **Fixed capacity.** Enqueue on a full queue fails (or overwrites the oldest item, in some buffers).
2. **Wrap with modulo:** `(index + 1) % capacity`.
3. **Track `size` (or a count)** to tell *empty* from *full*. If you only use `head` and `tail`, both cases look like `head == tail`.
4. **Two ways to avoid the empty/full confusion:**

| Method | How |
|---|---|
| Keep a `size` counter | simple, uses all slots |
| Leave one slot empty | `tail + 1 == head` means full; uses `capacity - 1` slots |

5. **Overwriting ring buffer:** when full, the new item replaces the oldest one. Used for "keep the last N" logs.
6. **No shifting.** Only indices change.
7. **Circular deque** (LeetCode 641) is the same idea with both ends.

#### 5. Algorithm — Must Know

```text
enqueue(x):  if size == capacity: return false
             data[(head + size) % capacity] = x;  size++;  return true
dequeue():   if size == 0: return false
             head = (head + 1) % capacity;  size--;  return true
front():     if size == 0: -1 else data[head]
rear():      if size == 0: -1 else data[(head + size - 1) % capacity]
```

#### 6. Kotlin Implementation — Must Know

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

// Overwriting ring buffer: keeps the last `capacity` items (like a rolling log)
class RingBuffer<T>(private val capacity: Int) {
    private val data = arrayOfNulls<Any?>(capacity)
    private var head = 0
    private var size = 0

    fun add(item: T) {
        if (size == capacity) {
            data[head] = item                       // overwrite the oldest
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
println(q.enQueue(4))   // false — full
println(q.rear())       // 3
println(q.deQueue())    // true
println(q.enQueue(4))   // true — reuses the freed slot
println(q.rear())       // 4

val log = RingBuffer<String>(3)
listOf("a", "b", "c", "d", "e").forEach { log.add(it) }
println(log.toList())   // [c, d, e]
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `enQueue` | `O(1)` |
| `deQueue` | `O(1)` |
| `front` / `rear` | `O(1)` |
| `isEmpty` / `isFull` | `O(1)` |
| Space | `O(capacity)`, fixed |

#### 8. Common Circular Patterns — Must Know

1. **Design Circular Queue** (LeetCode 622).
2. **Design Circular Deque** (LeetCode 641).
3. **Overwriting log / "last N events" buffer.**
4. **Audio / video / sensor buffers** between a fast producer and a consumer.
5. **Bounded buffer** in producer-consumer code.
6. **Android example:** a ring buffer of the last 100 log lines or the last 50 location samples.
7. **Circular array problems:** Next Greater Element II (LeetCode 503) uses `i % n`.

#### 9. Edge Cases / Common Mistakes

1. Using only `head` and `tail`, so *empty* and *full* look the same.
2. Forgetting `% capacity` when moving an index.
3. Wrong rear index: it is `(head + size - 1) % capacity`, not `head + size`.
4. Negative index when moving backwards (for deques). Use `(i - 1 + capacity) % capacity`.
5. Capacity `0` (division by zero in `%`).
6. Enqueue on a full queue silently overwriting when the problem expects `false`.
7. Dequeue not changing `size`.
8. Returning stale data after a dequeue (the slot is not cleared; that is fine for `Int`, but clear object slots to free memory).

#### 10. When to Use / When Not to Use

**Use when:**

1. You need a fixed-size buffer with `O(1)` operations.
2. You want "keep the last N" behaviour.

**Avoid when:**

1. The size is unknown and growth is fine. Use `ArrayDeque`.
2. You need a thread-safe queue. Use `ArrayBlockingQueue`.

#### 11. Related Topics

1. Queue Implementation
2. Deque
3. Producer-Consumer Queue — Concept
4. Array (`01-data-structure/01-Array`)

#### 12. Interview Must Remember

1. **Wrap indices with `% capacity`. Track `size` to tell empty from full.**
2. Next free slot = `(head + size) % capacity`. Rear = `(head + size - 1) % capacity`.
3. All operations `O(1)`, memory fixed.
4. Kotlin's `ArrayDeque` is a growing circular array.
