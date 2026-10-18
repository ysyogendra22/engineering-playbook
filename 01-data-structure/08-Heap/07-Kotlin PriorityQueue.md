# Kotlin `PriorityQueue`

#### 1. Definition — Must Know

1. Kotlin on the JVM and on Android uses Java's `java.util.PriorityQueue`.
2. It is a **min-heap** by default. You change the order with a **comparator**.
3. This is the class you use in interviews and in real code, instead of writing your own heap.

#### 2. Why It Is Used — Must Know

1. It gives `O(log n)` insert and extract, and `O(1)` peek, with no code to write.
2. Almost every heap interview problem is solved with it.
3. Knowing its methods, its default order, and its traps saves time and bugs.

#### 3. How It Works — Must Know

```text
PriorityQueue<Int>()                      → min-heap   (smallest first)
PriorityQueue<Int>(comparator)            → order given by the comparator
PriorityQueue<Int>(listOf(5, 1, 3))       → heap built from a collection in O(n)
```

Internally it stores a binary heap in an array and sifts up and down on each change.

#### 4. Core Concepts — Must Know

| Method | What it does | Empty queue | Cost |
|---|---|---|---:|
| `add(x)` / `offer(x)` | Insert | n/a | `O(log n)` |
| `peek()` | Best item, not removed | returns `null` | `O(1)` |
| `poll()` | Remove and return the best item | returns `null` | `O(log n)` |
| `remove()` | Remove and return the best item | **throws** | `O(log n)` |
| `element()` | Best item, not removed | **throws** | `O(1)` |
| `remove(x)` | Remove one occurrence of `x` | returns `false` | **`O(n)`** |
| `contains(x)` | Search | `false` | **`O(n)`** |
| `size`, `isEmpty()` | Count | | `O(1)` |

Rules to remember:

1. `peek()` and `poll()` return `null` when empty. In Kotlin that is a platform type, so check `isNotEmpty()` first.
2. **Iteration order is not sorted.** Only `poll()` gives sorted order.
3. `null` elements are not allowed.
4. Elements must be comparable, or you must give a comparator. Otherwise `ClassCastException`.
5. The queue is **not thread-safe**. Use `PriorityBlockingQueue` for concurrent access.

#### 5. Algorithm — Must Know

The three setups you need to know:

```text
Min-heap:   PriorityQueue<T>()
Max-heap:   PriorityQueue<T>(reverse order comparator)
Custom:     PriorityQueue<T>(comparator on the field(s) you care about)
```

#### 6. Kotlin Implementation — Must Know

**Min-heap**

```kotlin
import java.util.PriorityQueue

val minHeap = PriorityQueue<Int>()
```

**Max-heap**

```kotlin
val maxHeap1 = PriorityQueue<Int>(compareByDescending<Int> { it })
val maxHeap2 = PriorityQueue<Int>(Comparator.reverseOrder())
```

**Custom comparator**

```kotlin
// By a field of a data class
data class Task(val name: String, val priority: Int, val order: Long)

val tasks = PriorityQueue<Task>(
    compareByDescending<Task> { it.priority }   // highest priority first
        .thenBy { it.order }                    // then oldest first
)

// By the first value of an IntArray
val byFirst = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })

// By two values of an IntArray
val byTwo = PriorityQueue<IntArray>(compareBy<IntArray>({ it[0] }, { it[1] }))

// By the value of a Pair
val byValue = PriorityQueue<Pair<String, Int>>(compareBy<Pair<String, Int>> { it.second })
```

**Build from a collection in `O(n)`**

```kotlin
val nums = listOf(9, 4, 7, 1)
val heap = PriorityQueue<Int>(nums)    // heapifies once
// heap.addAll(nums) would cost O(n log n)
```

**Drain in order**

```kotlin
while (heap.isNotEmpty()) {
    println(heap.poll())   // 1, 4, 7, 9
}
```

Add `import java.util.PriorityQueue` at the top. Kotlin's common standard library has no `PriorityQueue`. If you share code through Kotlin Multiplatform, check what your targets provide, or write a small heap (see "Heap Operations & Complexity").

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `add`, `offer` | `O(log n)` |
| `poll`, `remove()` | `O(log n)` |
| `peek` | `O(1)` |
| `remove(x)`, `contains(x)` | `O(n)` |
| Build from a collection | `O(n)` |
| Space | `O(n)` |

#### 8. Common Usage Patterns — Must Know

1. Fixed-size heap for Top K (add, then `poll()` when `size > k`).
2. Heap of `IntArray` or `Pair` for "value plus where it came from" (K-way merge, Dijkstra).
3. Two heaps for a running median.
4. Heap with a sequence number for stable scheduling.

#### 9. Edge Cases / Common Mistakes

1. Comparator `{ a, b -> b - a }`. It can overflow. Use `compareByDescending` or `b.compareTo(a)`.
2. Relying on `println(heap)` or a `for` loop to show sorted order.
3. Mutating an object's priority field after adding it. The heap does not notice.
4. Using `remove(x)` in a loop and assuming `O(log n)`.
5. Forgetting that `peek()` and `poll()` can be `null`.
6. A comparator that returns `0` for different objects when you want a total order (for example, in a set). Fine for a heap, but ties come out in any order.
7. Sharing one `PriorityQueue` between threads without protection.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the best item repeatedly, on the JVM or Android.
2. You want to avoid writing a heap by hand.

**Avoid when:**

1. You need priority updates or deletes by key. Use a map as well, or a sorted structure such as `TreeSet`.
2. You are in shared Kotlin Multiplatform code with no JVM target.

#### 11. Related Topics

1. Min Heap vs Max Heap
2. Priority Queue
3. Heap for Scheduling / Processing by Priority
4. Lazy Deletion with Heap
5. Kotlin for Coding Interviews (`03-leetcode-patterns`, topic 3)

#### 12. Interview Must Remember

1. Default is a **min-heap**. Max-heap = `compareByDescending` or `Comparator.reverseOrder()`.
2. `peek` / `poll` return `null` when empty. `remove()` throws.
3. `remove(x)` and `contains(x)` are **`O(n)`**. Iteration is **not sorted**.
4. Build from a collection for `O(n)`. Never mutate an item's priority in place.
