# Queue Operations

#### 1. What Is It?

A queue has a few basic operations. Know them by heart, and know **which Kotlin call does each one**. Java uses different names for the same actions, and interviewers may use either.

| Action | Kotlin `ArrayDeque` | If the queue is empty |
|---|---|---|
| **Enqueue** (add at the back) | `addLast(x)` | — |
| **Dequeue** (remove the front) | `removeFirst()` | crashes (`NoSuchElementException`) |
| **Dequeue (safe)** | `removeFirstOrNull()` | returns `null` |
| **Peek** (look at the front) | `first()` | crashes |
| **Peek (safe)** | `firstOrNull()` | returns `null` |
| **Size / empty** | `size`, `isEmpty()`, `isNotEmpty()` | — |

The Java `Queue` interface (`LinkedList`, `java.util.ArrayDeque`) has two sets of names:

| Action | Crashes when it fails | Returns a special value |
|---|---|---|
| Enqueue | `add(x)` | `offer(x)` (`false` if a bounded queue is full) |
| Dequeue | `remove()` | `poll()` (`null` if empty) |
| Peek | `element()` | `peek()` (`null` if empty) |

#### 2. How It Works

```text
Start:        []
enqueue(1):   [1]
enqueue(2):   [1, 2]
peek():       1                 queue stays [1, 2]
dequeue():    1                 queue is [2]
dequeue():    2                 queue is []
dequeue():    error or null     the queue is empty
```

Three small patterns appear in many solutions:

| Pattern | Code idea | Used for |
|---|---|---|
| **Drain loop** | `while (queue.isNotEmpty()) { removeFirst() ... }` | BFS, task processing |
| **Rotate** | `queue.addLast(queue.removeFirst())` | hot potato, round robin, stack from queue |
| **One level at a time** | `repeat(queue.size) { ... }` | level-order traversal |

#### 3. Kotlin Code

```kotlin
val q = ArrayDeque<String>()

q.addLast("A")                  // enqueue
q.addLast("B")
q.addLast("C")

println(q.first())              // A   (peek)
println(q.removeFirst())        // A   (dequeue)
println(q.size)                 // 2
println("B" in q)               // true, but this is O(n)

for (item in q) println(item)   // B, C  (front to back, nothing is removed)

q.clear()
println(q.removeFirstOrNull())  // null, no crash
```

Rotate (move the front to the back):

```kotlin
val people = ArrayDeque(listOf("A", "B", "C", "D"))
repeat(2) { people.addLast(people.removeFirst()) }
println(people)                 // [C, D, A, B]
```

Java style:

```kotlin
import java.util.LinkedList
import java.util.Queue

val jq: Queue<Int> = LinkedList()
jq.offer(1)
jq.offer(2)
println(jq.peek())    // 1
println(jq.poll())    // 1
println(jq.poll())    // 2
println(jq.poll())    // null: empty, no crash
```

#### 4. Complexity

| Action | Time |
|---|---|
| `addLast`, `removeFirst`, `first`, `size`, `isEmpty` | `O(1)` |
| `contains` | `O(n)` |
| `clear`, iterate all | `O(n)` |

#### 5. Common Mistakes

1. **Dequeue or peek on an empty queue.** Check `isNotEmpty()` or use the `...OrNull()` versions.
2. **Using `remove(x)`** thinking it is "dequeue". It removes a specific value (`O(n)`).
3. **On a Java `Deque`, mixing `push` and `addLast`.** `push` adds to the **front**.
4. **Changing the queue inside `for (x in queue)`.** It crashes.
5. **Assuming a `PriorityQueue` prints in priority order.** It does not. Only `poll()` gives the right order.

#### 6. Say This in the Interview

1. "I use `ArrayDeque`: `addLast` to enqueue and `removeFirst` to dequeue, both `O(1)`."
2. "`removeFirstOrNull` is safe when the queue may be empty."
3. "I capture the size with `repeat(queue.size)` so new items do not extend the current level."

#### 7. Quick Check

1. Which Java method returns `null` instead of crashing when the queue is empty: `remove()` or `poll()`?
2. How do you move the front item to the back?

<details>
<summary>Answers</summary>

1. `poll()`.
2. `queue.addLast(queue.removeFirst())`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Operation used |
|---|---|---|
| 933 | Number of Recent Calls (Easy) | drain from the front |
| 1823 | Find the Winner of the Circular Game (Medium) | rotate |
| 2073 | Time Needed to Buy Tickets (Easy) | rotate |
| 102 | Binary Tree Level Order Traversal (Medium) | `repeat(queue.size)` |
