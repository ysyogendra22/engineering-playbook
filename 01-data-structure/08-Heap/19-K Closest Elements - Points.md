# K Closest Elements / Points

#### 1. Definition — Must Know

1. **K Closest Points to Origin** (LeetCode 973): given points `(x, y)`, return the `k` points closest to `(0, 0)`.
2. **Find K Closest Elements** (LeetCode 658): given a sorted array, return the `k` numbers closest to a target `x`.
3. Both are Top K problems where the key is a **distance**. If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is a direct use of the "keep the best `k`" heap.
2. It teaches an important trick: compare **squared** distance, so no square root is needed.
3. It matches real features such as "nearest stores" or "closest friends".

#### 3. How It Works — Must Know

Points `(1, 3)`, `(-2, 2)`, `(5, 8)`, `(0, 1)`, `k = 2`. Squared distance from the origin: `x² + y²`.

```text
(1, 3)   → 10
(-2, 2)  → 8
(5, 8)   → 89
(0, 1)   → 1

Max-heap of size 2, ordered by distance (the root is the FARTHEST of the kept points):
add (1, 3)  d=10     heap: (1,3)
add (-2, 2) d=8      heap: (1,3) (-2,2)
add (5, 8)  d=89     size 3 > 2 → remove the farthest (5,8)   → (1,3) (-2,2)
add (0, 1)  d=1      size 3 > 2 → remove the farthest (1,3)   → (-2,2) (0,1)

Answer: (-2, 2) and (0, 1)
```

#### 4. Core Concepts — Must Know

1. **Closest `k` → max-heap of size `k`**, ordered by distance. The root is the farthest of the kept points, so it is the one to remove.
2. **Use squared distance.** `√` is monotonic, so the order is the same and floating point is avoided.
3. **Use `Long`** for the squared distance if coordinates can be large.
4. For a **sorted array**, a heap works, but binary search plus two pointers is faster (`O(log n + k)`).

| Problem | Best approach | Time |
|---|---|---:|
| Closest points (unsorted) | Max-heap of size `k` | `O(n log k)` |
| Closest points (unsorted) | Quickselect on distance | `O(n)` average |
| Closest elements in a **sorted** array | Binary search + two pointers | `O(log n + k)` |

#### 5. Algorithm — Must Know

```text
heap = max-heap ordered by squared distance
for each point:
    heap.add(point)
    if heap.size > k: heap.poll()      // drop the farthest
return all points in the heap
```

#### 6. Kotlin Implementation — Must Know

**Closest points to the origin**

```kotlin
import java.util.PriorityQueue

fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
    fun dist(p: IntArray): Long = p[0].toLong() * p[0] + p[1].toLong() * p[1]

    val heap = PriorityQueue<IntArray>(compareByDescending<IntArray> { dist(it) })   // max-heap
    for (p in points) {
        heap.add(p)
        if (heap.size > k) heap.poll()
    }
    return heap.toTypedArray()
}
```

**Closest elements to a value `x` (heap version)**

```kotlin
import kotlin.math.abs

fun findClosestElements(arr: IntArray, k: Int, x: Int): List<Int> {
    // The root is the "worst" kept number: the farthest from x, and on a tie the larger value
    val heap = PriorityQueue<Int>(
        compareByDescending<Int> { abs(it.toLong() - x) }.thenByDescending { it }
    )
    for (n in arr) {
        heap.add(n)
        if (heap.size > k) heap.poll()
    }
    return heap.sorted()
}
```

Binary search plus two pointers for the sorted array is shown in `03-leetcode-patterns` (topics 4 and 8).

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Heap of size `k` | `O(n log k)` | `O(k)` |
| Sort by distance | `O(n log n)` | `O(n)` |
| Quickselect | `O(n)` average | `O(1)` extra |

#### 8. Common Variations — Must Know

1. **Closest points to any given point.** Replace the origin with `(qx, qy)`.
2. **K nearest places on a phone map.** For GPS, use a proper geographic distance, and a spatial index such as geohash or a quadtree for large data (`SD 33`).
3. **Find K Closest Elements** (LeetCode 658) — ties favour the smaller number.
4. **K Closest Points with Manhattan distance** — change the key to `abs(x) + abs(y)`.

#### 9. Edge Cases / Common Mistakes

1. Using a **min**-heap for the closest points. It keeps the farthest ones.
2. Computing `√(x² + y²)`. It is slower and may introduce floating-point errors.
3. `Int` overflow in `x * x + y * y` for large coordinates. Convert to `Long` first.
4. `k` larger than the number of points.
5. Points at the same distance. Any order is usually allowed, but read the problem.
6. For LeetCode 658: forgetting the tie rule (smaller number wins) and returning an unsorted list.
7. Using the heap on a sorted array when a binary search is expected for the better complexity.

#### 10. When to Use / When Not to Use

**Use the heap when:**

1. The data is unsorted and `k` is small.
2. Points arrive over time.

**Avoid it when:**

1. The array is sorted. Use binary search and two pointers.
2. The data is large and fixed, and you query many times. Use a spatial index (k-d tree, geohash).

#### 11. Related Topics

1. Top K Elements Pattern
2. Kth Largest / Kth Smallest Element
3. Quickselect (`02-algorithm/02-searching/13-Quickselect.md`)
4. Binary Search (`02-algorithm/02-searching/03-Binary Search.md`)

#### 12. Interview Must Remember

1. **Closest `k` → max-heap of size `k`** by distance.
2. **Compare squared distance** (use `Long`). No square root.
3. `O(n log k)` time, `O(k)` space.
4. For a **sorted** array, say binary search plus two pointers.
