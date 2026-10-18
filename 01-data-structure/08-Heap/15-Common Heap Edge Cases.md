# Common Heap Edge Cases

#### 1. Definition — Must Know

1. These are the inputs and situations that most often break a heap solution.
2. Most bugs come from **empty heaps**, **comparator mistakes**, and **changing items after they are inside the heap**.
3. Check this list before you submit any heap code.

#### 2. Why It Is Used — Must Know

1. Heap code looks short, so small mistakes hide easily.
2. Interviewers use `k = 0`, empty input, and duplicates to see whether you think about boundaries.
3. Many of these problems appear as silent wrong answers, not crashes.

#### 3. How It Works — Must Know

A bug that looks correct:

```kotlin
val heap = PriorityQueue<Int>(compareBy<Int> { -it })   // "max-heap"
heap.add(Int.MIN_VALUE)
heap.add(5)
println(heap.peek())   // prints Int.MIN_VALUE, not 5
```

`-Int.MIN_VALUE` is still `Int.MIN_VALUE` (overflow), so that value compares wrongly. Use `compareByDescending { it }`.

Another one:

```kotlin
val heap = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })
val item = intArrayOf(5, 0)
heap.add(item)
item[0] = 1          // changed after adding: the heap is not re-ordered
```

The heap still believes `item` has key `5`.

#### 4. Core Concepts — Must Know

1. **The heap only checks order when you add or remove.** It never re-checks an item you changed.
2. **The comparator decides everything.** A wrong comparator gives wrong answers with no error.
3. **Empty is a normal state** that your code must handle.
4. **Only the root is guaranteed best.** Iteration order is not sorted.

#### 5. Edge Case Checklist — Must Know

| Case | What should happen |
|---|---|
| Empty heap, `peek()` / `poll()` | Return `null` (`PriorityQueue`). `remove()` / `element()` throw. Check `isNotEmpty()` first |
| Single element | Works. The element is both root and last item |
| `k = 0` | Return an empty result. Do not call `peek()` on an empty heap |
| `k > n` | The heap simply keeps everything. The "Kth" element may not exist |
| `k = n` | Heap-based Top K equals a full sort. Sorting is simpler |
| Duplicates | Kept as separate items, unless the problem says "distinct" |
| Equal priorities | Order among them is unspecified. Add a sequence number if it matters |
| Negative numbers | Fine for heaps. Negating values to fake a max-heap is dangerous (`Int.MIN_VALUE`) |
| Comparator `b - a` | May overflow. Use `compareByDescending` or `compareTo` |
| Very large values | Use `Long` for computed keys, such as squared distances or sums |
| Changing an item after adding it | The heap breaks. Remove and re-add it, or add a new entry and mark the old one stale |
| `remove(x)` | `O(n)`, not `O(log n)` |
| `contains(x)` | `O(n)` |
| Iterating a `PriorityQueue` | Not sorted. Poll to get sorted order |
| Modifying while iterating | `ConcurrentModificationException` |
| `null` element | `NullPointerException` |
| Elements not comparable and no comparator | `ClassCastException` |
| Multiple threads | Not thread-safe. Use `PriorityBlockingQueue` or a lock |
| Heap size grows without limit | Memory problem. Cap it (Top K) or drain it regularly |

#### 6. Kotlin Implementation — Must Know

Defensive patterns:

```kotlin
import java.util.PriorityQueue

fun kLargest(nums: IntArray, k: Int): List<Int> {
    if (k <= 0 || nums.isEmpty()) return emptyList()      // k = 0 or empty input
    val heap = PriorityQueue<Int>()
    for (n in nums) {
        heap.add(n)
        if (heap.size > k) heap.poll()
    }
    return heap.sortedDescending()                         // k > n returns all n items
}

// Safe peek
val best: Int? = if (heap.isNotEmpty()) heap.peek() else null

// Safe comparator for large values
val byDistance = compareBy<IntArray> {
    it[0].toLong() * it[0] + it[1].toLong() * it[1]       // Long, no overflow
}
```

#### 7. Time & Space Complexity — Must Know

Edge cases do not change the main costs (`add` / `poll` `O(log n)`, `peek` `O(1)`).

The ones that **do** change the cost:

| Situation | Cost |
|---|---:|
| `remove(x)` or `contains(x)` | `O(n)` |
| Checking `size` | `O(1)` |
| Building from a collection | `O(n)`, while `addAll` is `O(n log n)` |

#### 8. Common Edge-Case Patterns — Must Know

1. **Boundary values of `k`:** `0`, `1`, `n`, and more than `n`.
2. **Empty and one-element input.**
3. **Ties:** decide the rule and say it aloud.
4. **Stale entries:** an item removed or replaced elsewhere but still in the heap (see "Lazy Deletion with Heap").
5. **Overflow:** in comparators and in computed keys.

#### 9. Edge Cases / Common Mistakes

1. Calling `peek()` on an empty heap and treating `null` as a value.
2. Building a max-heap with negation or `b - a`.
3. Updating a field of an object that is already in the heap.
4. Assuming the heap prints sorted.
5. Using `remove(x)` in a hot loop.
6. Not stating assumptions about duplicates and ties before coding.

#### 10. When to Use / When Not to Use

**Use this checklist:**

1. Before coding, to state your assumptions.
2. After coding, to dry-run `k = 0`, an empty input, and a duplicate-heavy input.

#### 11. Related Topics

1. Kotlin `PriorityQueue`
2. Min Heap vs Max Heap
3. Top K Elements Pattern
4. Lazy Deletion with Heap

#### 12. Interview Must Remember

1. **Empty heap**: `peek` / `poll` give `null`. Check first.
2. **Never mutate an item inside the heap.**
3. **Max-heap by `compareByDescending`**, not negation and not `b - a`.
4. Test `k = 0`, `k > n`, and duplicates on every solution.
