# Min Heap vs Max Heap

#### 1. Definition — Must Know

1. A **min-heap** keeps the **smallest** element at the root. Every parent is `≤` its children.
2. A **max-heap** keeps the **largest** element at the root. Every parent is `≥` its children.
3. They are the same structure with the comparison reversed.

#### 2. Why It Is Used — Must Know

1. Choosing the right one is the first decision in almost every heap problem.
2. Many problems want a heap that is **opposite to what the words suggest**. For example, finding the `k` **largest** items uses a **min-heap** (see below).

#### 3. How It Works — Must Know

The same values `5, 3, 8, 1, 9`, stored both ways:

```text
Min-heap                 Max-heap
     1                        9
   /   \                    /   \
  3     8                  8     5
 / \                      / \
5   9                    1   3
```

1. Min-heap: `peek()` gives `1`.
2. Max-heap: `peek()` gives `9`.
3. The shape may differ, because insertion order and comparison decide where each value lands.

#### 4. Core Concepts — Must Know

1. **Min-heap** → quick access to the minimum.
2. **Max-heap** → quick access to the maximum.
3. **Rule for Top K:** keep a heap of size `k`. The root is the item you would drop first.

| Goal | Heap to use | Why |
|---|---|---|
| `k` **largest** items | **Min**-heap of size `k` | The root is the smallest of the `k` kept, so it is the one to throw away |
| `k` **smallest** items | **Max**-heap of size `k` | The root is the largest of the `k` kept |
| Always process the earliest deadline | Min-heap | Smallest deadline first |
| Always process the highest score | Max-heap | Largest score first |

4. Libraries usually give one type (Kotlin: a min-heap) and ask you to reverse it for the other.

#### 5. Algorithm — Must Know

Nothing new is implemented. The only change is the comparison:

```text
min-heap: a goes above b when a < b
max-heap: a goes above b when a > b
```

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

// Min-heap (default)
val minHeap = PriorityQueue<Int>()

// Max-heap
val maxHeap = PriorityQueue<Int>(compareByDescending<Int> { it })
// also works: PriorityQueue<Int>(Comparator.reverseOrder())

minHeap.addAll(listOf(5, 3, 8, 1, 9))
maxHeap.addAll(listOf(5, 3, 8, 1, 9))

println(minHeap.peek())   // 1
println(maxHeap.peek())   // 9
```

Do not write the max-heap comparator as `{ a, b -> b - a }`. The subtraction can overflow for large or negative values. Use `compareByDescending`, `Comparator.reverseOrder()`, or `b.compareTo(a)`.

#### 7. Time & Space Complexity — Must Know

| Operation | Min-heap | Max-heap |
|---|---:|---:|
| Peek | `O(1)` | `O(1)` |
| Insert | `O(log n)` | `O(log n)` |
| Extract | `O(log n)` | `O(log n)` |
| Space | `O(n)` | `O(n)` |

Both have identical cost. Only the comparison differs.

#### 8. Common Choices — Must Know

1. Kth **largest** element → min-heap of size `k`.
2. Kth **smallest** element → max-heap of size `k`.
3. Running median → one max-heap (lower half) **and** one min-heap (upper half).
4. Dijkstra's shortest path → min-heap by distance.
5. Task with highest priority first → max-heap (or a min-heap with the priority negated).

#### 9. Edge Cases / Common Mistakes

1. Using a max-heap to keep the `k` largest. You would throw away the wrong item.
2. Negating values to fake a max-heap, then overflowing on `Int.MIN_VALUE` (`-Int.MIN_VALUE` is still `Int.MIN_VALUE`).
3. Comparator written as `b - a`, which can overflow.
4. Forgetting that Kotlin's default is a **min-heap**. Java's `PriorityQueue` behaves the same way.
5. Mixing the two heaps in the Two Heaps pattern and putting a value in the wrong half.

#### 10. When to Use / When Not to Use

**Use a min-heap when:** the next thing you need is the smallest item, or you keep the `k` largest.

**Use a max-heap when:** the next thing you need is the largest item, or you keep the `k` smallest.

**Use both together when:** you split data into a lower half and an upper half (running median).

#### 11. Related Topics

1. Heap Fundamentals
2. Kotlin `PriorityQueue`
3. Top K Elements Pattern
4. Two Heaps Pattern

#### 12. Interview Must Remember

1. Min-heap → minimum at the root. Max-heap → maximum at the root.
2. **`k` largest → min-heap of size `k`. `k` smallest → max-heap of size `k`.**
3. Kotlin's `PriorityQueue` is a **min-heap** by default.
4. Build a max-heap with `compareByDescending` or `Comparator.reverseOrder()`, not `b - a`.
