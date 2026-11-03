# Heap Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–25.

#### 1. Key Takeaways

1. A heap gives the **min (or max) in `O(1)`**, and `add` / `poll` in `O(log n)`. It is **not sorted**, only the root is guaranteed.
2. **K largest → min-heap of size K. K smallest → max-heap of size K.** The root is the weakest candidate, the first to be evicted.
3. Kotlin's `PriorityQueue` is a **min-heap**. For a max-heap: `PriorityQueue<Int>(compareByDescending { it })`. Never write `a - b` in a comparator.
4. Most heap questions are one of: **Top K**, **K-way merge**, **two heaps (median)**, **schedule by priority**, **Dijkstra**.
5. A heap cannot update or remove an arbitrary item quickly. Use **lazy deletion**: push a new entry, skip stale ones.
6. Build a heap from an array in **`O(n)`** (bottom-up heapify), not `O(n log n)`.
7. Always check: empty heap, `K > n`, `K = 0`, duplicates, ties, overflow.

#### 2. Complexity Table

| Operation | Time | Space |
|---|---|---|
| `peek` | `O(1)` | |
| `add` / `offer` | `O(log n)` | |
| `poll` / `remove()` | `O(log n)` | |
| `remove(x)` / `contains(x)` | `O(n)` | |
| Build heap from `n` items | `O(n)` | in place |
| `n` adds | `O(n log n)` | |
| Heap sort | `O(n log n)` | `O(1)` |
| Top K of `n` (heap size K) | `O(n log K)` | `O(K)` |
| Merge `K` sorted lists, `N` items | `O(N log K)` | `O(K)` |
| Running median, `add` / `findMedian` | `O(log n)` / `O(1)` | `O(n)` |
| Dijkstra with a heap | `O((V + E) log V)` | `O(V + E)` |

Array layout (0-based): left child `2i + 1`, right child `2i + 2`, parent `(i − 1) / 2`, last parent `n / 2 − 1`.

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Note |
|---|---|---|
| "kth largest / smallest" | min-heap size K (or quickselect) | 09 |
| "top K frequent / closest / best" | size-K heap on a score | 08, 18, 19 |
| "merge K sorted lists / arrays / matrix rows" | heap with one item per list | 10, 11 |
| "median of a stream" | max-heap (low) + min-heap (high) | 12, 13 |
| "unlock then pick the best" (IPO) | min-heap by cost + max-heap by profit | 12 |
| "always process the largest / smallest next" | heap simulation (stones, tasks, CPU) | 14 |
| "minimum number of rooms / machines" | sort by start + min-heap of end times | 20 |
| "smallest range covering K lists" | K-way heap + track the current max | 21 |
| "top K of changing scores" | HashMap + heap | 22 |
| "update or cancel an item in a heap" | lazy deletion / stale entries | 23 |
| "max / min of a sliding window" | `(value, index)` heap, drop old indexes (or a deque) | 24 |
| "choose K to maximise sum × min / ratio" | sort by one key + heap of size K on the other | 25 |
| "shortest path with weights" | Dijkstra with `(distance, node)` | 23 |
| "sort in place with O(1) extra space" | heap sort | 17 |

#### 4. Templates to Memorise

**Top K largest**

```kotlin
val heap = PriorityQueue<Int>()
for (x in nums) { heap.add(x); if (heap.size > k) heap.poll() }
// heap.peek() is the Kth largest
```

**Top K by a score**

```kotlin
val heap = PriorityQueue<Int>(compareBy<Int> { score[it] })     // weakest on top
for (x in items) { heap.add(x); if (heap.size > k) heap.poll() }
```

**K-way merge**

```kotlin
val heap = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })   // [value, list, pos]
for ((i, l) in lists.withIndex()) if (l.isNotEmpty()) heap.add(intArrayOf(l[0], i, 0))
while (heap.isNotEmpty()) {
    val (v, i, p) = heap.poll()
    out.add(v)
    if (p + 1 < lists[i].size) heap.add(intArrayOf(lists[i][p + 1], i, p + 1))
}
```

**Two heaps (median)**

```kotlin
low.add(num); high.add(low.poll())
if (high.size > low.size) low.add(high.poll())
val median = if (low.size > high.size) low.peek().toDouble() else (low.peek() + high.peek()) / 2.0
```

**Meeting rooms**

```kotlin
val ends = PriorityQueue<Int>()
for (m in intervals.sortedBy { it[0] }) {
    if (ends.isNotEmpty() && ends.peek() <= m[0]) ends.poll()
    ends.add(m[1])
}
// ends.size = rooms
```

**Dijkstra (stale entries)**

```kotlin
val heap = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] }); heap.add(intArrayOf(0, src))
while (heap.isNotEmpty()) {
    val (d, u) = heap.poll()
    if (d > dist[u]) continue
    for ((v, w) in graph[u]) if (d + w < dist[v]) { dist[v] = d + w; heap.add(intArrayOf(dist[v], v)) }
}
```

**Sift down (min-heap)**

```kotlin
fun siftDown(a: IntArray, size: Int, start: Int) {
    var i = start
    while (true) {
        val l = 2 * i + 1; val r = l + 1; var s = i
        if (l < size && a[l] < a[s]) s = l
        if (r < size && a[r] < a[s]) s = r
        if (s == i) return
        val t = a[i]; a[i] = a[s]; a[s] = t; i = s
    }
}
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Heap |
|---|---|---|
| Kth largest | sort `O(n log n)` | size-K min-heap `O(n log K)` |
| Top K frequent | sort the counts `O(n log n)` | heap `O(n log K)`, buckets `O(n)` |
| Merge K sorted | concatenate + sort `O(N log N)` | heap `O(N log K)` |
| Running median | sorted list insert `O(n)` | two heaps `O(log n)` |
| Meeting rooms | overlap count `O(n²)` | sort + heap `O(n log n)` |
| Sliding window max | scan each window `O(n·k)` | heap `O(n log n)`, deque `O(n)` |
| Build a heap | `n` adds `O(n log n)` | heapify `O(n)` |
| Update a priority | `remove` + `add` `O(n)` | push a new entry, skip stale `O(log n)` |
| Smallest range for K lists | combos `O(L^K)` | heap `O(N log K)` |

#### 6. Common Mistakes and Edge Cases

1. **Wrong heap type** for Top K (max-heap for the K largest).
2. **Comparator with subtraction** (overflow). Use `compareBy`.
3. **Printing the heap** and expecting sorted order.
4. **`peek()` / `poll()` return `null`** on an empty heap.
5. **Heap not capped at `K`.**
6. **`pq.remove(x)`** is `O(n)`. Use lazy deletion.
7. **Mutating an item's key** after adding it.
8. **No tie-break** for equal keys (words, counts, indexes).
9. **Forgetting the `K > n` and `K = 0`** cases.
10. **Meeting rooms:** `<` vs `<=` when one meeting ends as another starts.
11. **Median:** integer division, or `Int` overflow when adding two tops.
12. **Edge cases:** empty input, one element, all equal, duplicates, negatives, very large values.

#### 7. What to Say Out Loud

1. "I need the best item again and again while the set changes, so a heap gives me `O(log n)` per operation."
2. "For the K largest I use a **min**-heap of size K: the root is the weakest candidate, so it's evicted first. That's `O(n log K)` instead of sorting in `O(n log n)`."
3. "Kotlin's `PriorityQueue` is a min-heap, so I reverse the comparator for a max-heap, using `compareBy` so it can't overflow."
4. "A heap can't update an item, so I push a new entry and ignore stale ones when they come out."
5. "Before finishing, I'll check: empty, `K > n`, duplicates and ties."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | max-heap |
| Easy | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | min-heap size K |
| Easy | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | heap with a tie |
| Medium | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | size-K heap, quickselect |
| Medium | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | counts + heap |
| Medium | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | max-heap on distance |
| Medium | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | tie-break |
| Medium | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | distance + tie |
| Medium | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | max-heap of counts |
| Medium | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | max-heap |
| Medium | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | K-way merge |
| Medium | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | heap of pairs |
| Medium | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | end-time heap (premium) |
| Medium | [Car Pooling](https://leetcode.com/problems/car-pooling/) | free alternative |
| Medium | [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/) | min-heap of climbs |
| Medium | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Dijkstra |
| Hard | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | K-way merge |
| Hard | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | two heaps |
| Hard | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | heap or deque |
| Hard | [IPO](https://leetcode.com/problems/ipo/) | two heaps |
