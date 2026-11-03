# Kotlin PriorityQueue

> The Kotlin/Java `PriorityQueue` is a min-heap. Learn the four ways to build one, and the traps that cost points in interviews.

#### 1. What Is It?

Kotlin uses Java's `java.util.PriorityQueue` (there is no separate Kotlin class). It is a **min-heap** by default, backed by an array.

| Method | Meaning | Cost |
|---|---|---|
| `add(x)` / `offer(x)` | insert | `O(log n)` |
| `peek()` | smallest item, or `null` if empty | `O(1)` |
| `poll()` | remove and return the smallest, or `null` if empty | `O(log n)` |
| `remove()` | remove the smallest, **throws** if empty | `O(log n)` |
| `remove(x)` | remove one value `x` | **`O(n)`** |
| `contains(x)` | check a value | **`O(n)`** |
| `size`, `isEmpty()`, `isNotEmpty()` | | `O(1)` |

#### 2. How It Works

**Four ways to create one**

| Need | Code |
|---|---|
| Min-heap of `Int` | `PriorityQueue<Int>()` |
| Max-heap of `Int` | `PriorityQueue<Int>(compareByDescending<Int> { it })` |
| Heap ordered by a field | `PriorityQueue<Task>(compareBy<Task> { it.priority })` |
| Heap of arrays / pairs | `PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })` |

**Tie-breakers (several keys):** `compareBy<T>({ it.a }, { it.b })`. Mix directions: `compareBy<T> { it.a }.thenByDescending { it.b }`.

```text
(distance, node) in Dijkstra:  PriorityQueue<IntArray>(compareBy { it[0] })
(count, word) in top-K words:  PriorityQueue<String>(compareBy<String>({ count[it] }).thenByDescending { it })
```

**The traps**

1. **Iteration and `println(pq)` are not sorted.** The internal array is heap order only.
2. **`remove(x)` and `contains(x)` are `O(n)`.**
3. **No decrease-key.** To change a priority, add a new entry and ignore the old one when it comes out (lazy deletion, note 23).
4. **Do not change an object's priority after adding it.** The heap will not move it.
5. **Comparator overflow:** `{ a, b -> a - b }` can overflow. Use `compareBy` or `Integer.compare`.
6. **`peek()` and `poll()` return `null`** on an empty queue. In Kotlin, a `!!` or a check is needed.
7. **`PriorityQueue<Int>` boxes** every value. Fine for interviews.

#### 3. Brute Force vs Optimized

| Habit | Better |
|---|---|
| sort the whole list to get the max again and again | max-heap |
| `pq.remove(x)` in a loop, `O(n)` each | lazy deletion with a map |
| `pq.toList()` to see the order | `poll()` repeatedly (iteration is unordered) |
| `(a, b) -> a - b` comparator | `compareBy` |

```kotlin
// Wrong way to read a heap in order: iteration order is NOT sorted
val pq = PriorityQueue<Int>(listOf(5, 3, 8, 1, 9))
println(pq.toList())             // heap order, e.g. [1, 3, 8, 5, 9]  (NOT [1, 3, 5, 8, 9])
```

#### 4. Kotlin Code

```kotlin
import java.util.PriorityQueue

fun demo() {
    // min-heap
    val min = PriorityQueue<Int>()
    min.addAll(listOf(5, 3, 8, 1, 9))
    println(min.peek())                                    // 1

    // max-heap
    val max = PriorityQueue<Int>(compareByDescending<Int> { it })
    max.addAll(listOf(5, 3, 8, 1, 9))
    println(max.peek())                                    // 9

    // custom object
    data class Task(val priority: Int, val name: String)
    val tasks = PriorityQueue<Task>(compareBy<Task> { it.priority })
    tasks.add(Task(3, "email")); tasks.add(Task(1, "bug"))
    println(tasks.poll().name)                             // bug

    // array entries: [distance, node]
    val dijkstra = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })
    dijkstra.add(intArrayOf(5, 1)); dijkstra.add(intArrayOf(2, 8))
    println(dijkstra.poll().toList())                      // [2, 8]

    // several keys: count ascending, then word descending
    val counts = mapOf("a" to 2, "b" to 2, "c" to 1)
    val words = PriorityQueue<String>(compareBy<String>({ counts[it]!! }).thenByDescending { it })
    words.addAll(counts.keys)
    println(words.poll())                                  // c  (lowest count)
    println(words.poll())                                  // b  (same count as a, but b is later in the alphabet)

    // empty queue
    val empty = PriorityQueue<Int>()
    println(empty.peek())                                  // null
    println(empty.poll())                                  // null
    // empty.remove() throws NoSuchElementException
}
```

Checks (printed values are in the comments above): `min.peek()` → `1`, `max.peek()` → `9`, `tasks.poll().name` → `"bug"`, `dijkstra.poll().toList()` → `[2, 8]`, the word heap polls `"c"` then `"b"`, and `empty.peek()` → `null`.

Build a heap from a collection in one step (this is the `O(n)` heapify): `PriorityQueue<Int>(listOf(5, 3, 8, 1, 9))`.

#### 5. Complexity

| | Time |
|---|---|
| `add`, `poll`, `remove()` | `O(log n)` |
| `peek`, `size` | `O(1)` |
| `remove(x)`, `contains(x)` | `O(n)` |
| Build from a collection | `O(n)` |

#### 6. Common Mistakes

1. **Printing the heap** and expecting sorted output.
2. **Calling `remove(x)`** and assuming `O(log n)`.
3. **Subtracting in the comparator** (overflow).
4. **Mutating a stored object's key** without re-inserting.
5. **Forgetting `null` from `peek()`/`poll()`** (Kotlin will make you handle it).
6. **Using the wrong heap direction.** Remember: min-heap by default.
7. **Creating `PriorityQueue<Int>(k)` thinking `k` is a size limit.** It is only the initial capacity (and in some overloads the first argument must be a comparator or collection).

#### 7. Say This in the Interview

1. "Kotlin's `PriorityQueue` is a min-heap. For a max-heap I pass `compareByDescending`."
2. "`add` and `poll` are `O(log n)`, `peek` is `O(1)`. `remove(x)` is `O(n)`, so I'll avoid it and use lazy deletion if I must."
3. "I'll use `compareBy` instead of subtracting, so there's no overflow."

#### 8. Quick Check

1. What does `PriorityQueue<Int>().poll()` return when the queue is empty?
2. How do you make a heap ordered by `it[1]` of `IntArray`s?
3. Does `println(pq)` show items in sorted order?

<details>
<summary>Answers</summary>

1. `null`.
2. `PriorityQueue<IntArray>(compareBy<IntArray> { it[1] })`.
3. No, only the root is guaranteed to be the smallest.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (Easy) | max-heap |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (Medium) | heap of arrays |
| 692 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) (Medium) | multi-key comparator |
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium) | `(distance, node)` entries |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Medium, premium) | min-heap of end times |
