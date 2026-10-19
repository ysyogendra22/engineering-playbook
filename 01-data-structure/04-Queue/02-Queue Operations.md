# Queue Operations

#### 1. Definition — Must Know

1. The core queue operations are **enqueue**, **dequeue**, **peek**, **size**, and **isEmpty**.
2. They all run in **`O(1)`** (amortized for `ArrayDeque`).
3. Kotlin and Java use different names for the same actions. You must know both sets.

#### 2. Why It Is Used — Must Know

1. Interview code uses these calls constantly (BFS, simulations, design questions).
2. Choosing the "safe" or "throwing" version matters when the queue may be empty.
3. Mixing the names (`add` vs `addLast`, `poll` vs `removeFirst`) is a common source of bugs.

#### 3. How It Works — Must Know

```text
enqueue(x)   put x at the back
dequeue()    remove and return the front item
peek()       return the front item, do not remove
size         number of items
isEmpty      true when there are no items

Start:          []
enqueue(1):     [1]
enqueue(2):     [1, 2]
peek():         → 1       queue stays [1, 2]
dequeue():      → 1       queue is [2]
dequeue():      → 2       queue is []
dequeue():      → error or null (the queue is empty)
```

#### 4. Core Concepts — Must Know

**Kotlin `ArrayDeque`**

| Action | Call | When empty |
|---|---|---|
| Enqueue | `addLast(x)` or `add(x)` | — |
| Dequeue | `removeFirst()` | throws `NoSuchElementException` |
| Dequeue (safe) | `removeFirstOrNull()` | returns `null` |
| Peek | `first()` | throws |
| Peek (safe) | `firstOrNull()` | returns `null` |
| Size / empty | `size`, `isEmpty()`, `isNotEmpty()` | — |

**Java `Queue` interface** (`LinkedList`, `java.util.ArrayDeque`, `PriorityQueue`)

| Action | Throws on failure | Returns special value |
|---|---|---|
| Enqueue | `add(x)` | `offer(x)` → `false` if a bounded queue is full |
| Dequeue | `remove()` | `poll()` → `null` if empty |
| Peek | `element()` | `peek()` → `null` if empty |

1. **Prefer `offer` / `poll` / `peek`** with Java queues. They do not throw.
2. **`add` on a normal queue never fails.** It matters for bounded queues (full → exception).
3. **Order of removal for each type:**
   - `ArrayDeque`, `LinkedList`: oldest first.
   - `PriorityQueue`: smallest (or highest priority) first.
4. **Clear / contains / iterate:** `clear()`, `contains(x)` (`O(n)`), `for (x in queue)` (front to back, does not remove).

#### 5. Algorithm — Must Know

Safe processing loop:

```text
while queue is not empty:
    item = dequeue()
    ...
```

Safe peek:

```text
if queue is not empty: look at front
else: handle "no item"
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val q = ArrayDeque<String>()

q.addLast("A")                  // enqueue
q.addLast("B")
q.add("C")                      // same as addLast

println(q.first())              // A  (peek)
println(q.removeFirst())        // A  (dequeue)
println(q.size)                 // 2
println("B" in q)               // true, O(n)

for (item in q) println(item)   // B, C  — front to back

q.clear()
println(q.firstOrNull())        // null
// q.removeFirst()              // would throw NoSuchElementException
println(q.removeFirstOrNull())  // null
```

Java-style:

```kotlin
import java.util.LinkedList
import java.util.Queue

val jq: Queue<Int> = LinkedList()
jq.offer(1)
jq.offer(2)
println(jq.peek())    // 1
println(jq.poll())    // 1
println(jq.poll())    // 2
println(jq.poll())    // null — empty, no exception
```

A queue that returns a default when empty:

```kotlin
fun <T> ArrayDeque<T>.dequeueOrDefault(default: T): T = removeFirstOrNull() ?: default
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `addLast` / `offer` | `O(1)` amortized |
| `removeFirst` / `poll` | `O(1)` |
| `first` / `peek` | `O(1)` |
| `size`, `isEmpty` | `O(1)` |
| `contains` | `O(n)` |
| `clear` | `O(n)` |
| Iteration | `O(n)` |

Space is `O(n)` for `n` stored items.

#### 8. Common Operation Patterns — Must Know

1. **Drain loop:** `while (queue.isNotEmpty()) { removeFirst() … }`.
2. **Snapshot size for a level:** `repeat(queue.size) { … }`.
3. **Rotate:** `queue.addLast(queue.removeFirst())` (hot potato, round robin).
4. **Peek before deciding:** `if (queue.first() < x) …`.
5. **Enqueue many:** `queue.addAll(list)`.
6. **Bounded queue:** check `offer` result, or check `size == capacity` before adding.

#### 9. Edge Cases / Common Mistakes

1. `removeFirst()` or `first()` on an empty queue throws. Check `isEmpty()` or use `...OrNull()`.
2. Mixing `push`/`pop` (stack words) with queue calls on a `Deque`. On `java.util.Deque`, `push` adds to the **front**.
3. Using `add` when you wanted `addFirst` (front) on a deque.
4. Using `contains` in a loop (`O(n)` each).
5. Confusing `remove()` (dequeue) with `remove(x)` (delete a specific item).
6. Modifying the queue inside `for (x in queue)`. This throws `ConcurrentModificationException`.
7. Assuming `PriorityQueue` iterates in priority order. It does not.

#### 10. When to Use / When Not to Use

**Use the throwing version when:**

1. An empty queue is a bug and you want it to crash loudly.

**Use the safe version when:**

1. An empty queue is normal (polling a task queue).

#### 11. Related Topics

1. Queue Fundamentals
2. Queue Implementation
3. Deque
4. Queue Edge Cases

#### 12. Interview Must Remember

1. **Enqueue = `addLast` / `offer`. Dequeue = `removeFirst` / `poll`. Peek = `first` / `peek`.**
2. Safe versions return `null` instead of throwing.
3. Everything is `O(1)` except `contains` and `clear`.
4. `repeat(queue.size)` captures the size once, for level-by-level loops.
