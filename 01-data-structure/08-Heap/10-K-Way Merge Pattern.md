# K-Way Merge Pattern

#### 1. Definition — Must Know

1. The **K-Way Merge** pattern combines **`k` sorted sources** into one sorted result (or finds something in that merged order).
2. The heap holds **one current item from each source**.
3. Repeatedly remove the smallest item from the heap, then add the **next item from the same source**.

#### 2. Why It Is Used — Must Know

1. The smallest item overall must be the smallest of the `k` front items. A heap finds it in `O(log k)`.
2. It avoids merging everything and re-sorting. Total cost is `O(N log k)`, where `N` is the total number of items.
3. It works on any sorted source, including files, streams, and database result pages.

#### 3. How It Works — Must Know

Merge three sorted lists: `A = [1, 4, 7]`, `B = [2, 5, 8]`, `C = [3, 6, 9]`.

```text
Start: put the first item of each list in the heap
heap: (1, A), (2, B), (3, C)

poll (1, A) → output 1 → add next of A: (4, A)      heap: (2,B) (3,C) (4,A)
poll (2, B) → output 2 → add next of B: (5, B)      heap: (3,C) (4,A) (5,B)
poll (3, C) → output 3 → add next of C: (6, C)      heap: (4,A) (5,B) (6,C)
poll (4, A) → output 4 → add next of A: (7, A)
... and so on

Output: 1 2 3 4 5 6 7 8 9
```

The heap never holds more than `k` items.

#### 4. Core Concepts — Must Know

1. **Heap entry** = the value plus **where it came from** (source index, and position or iterator).
2. **Initialisation:** push the first item of every non-empty source.
3. **Loop:** poll the smallest, output it, push the next item of that source (if any).
4. **Heap size is at most `k`**, so each step costs `O(log k)`.
5. **Signal words:** "k sorted lists", "k sorted arrays", "merge", "smallest range", "kth smallest in a sorted matrix", "smallest sums of pairs".

#### 5. Algorithm — Must Know

```text
heap = min-heap ordered by value
for each source i that is not empty:
    heap.add((first value of source i, i))

while heap is not empty:
    (value, i) = heap.poll()
    output value
    if source i has another item:
        heap.add((next value of source i, i))
```

#### 6. Kotlin Implementation — Must Know

A generic version that works with any sorted sources:

```kotlin
import java.util.PriorityQueue

fun <T : Comparable<T>> kWayMerge(sources: List<Iterator<T>>): List<T> {
    val heap = PriorityQueue<Pair<T, Int>>(compareBy<Pair<T, Int>> { it.first })
    sources.forEachIndexed { index, source ->
        if (source.hasNext()) heap.add(source.next() to index)
    }

    val result = mutableListOf<T>()
    while (heap.isNotEmpty()) {
        val (value, index) = heap.poll()
        result.add(value)
        if (sources[index].hasNext()) heap.add(sources[index].next() to index)
    }
    return result
}

// Usage
val merged = kWayMerge(
    listOf(
        listOf(1, 4, 7).iterator(),
        listOf(2, 5, 8).iterator(),
        listOf(3, 6, 9).iterator()
    )
)
println(merged)   // [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Concrete versions for arrays and linked lists are in "Merge K Sorted Lists / Arrays".

#### 7. Time & Space Complexity — Must Know

`N` = total number of items across all sources, `k` = number of sources.

| Case | Time | Space |
|---|---:|---:|
| Full merge | `O(N log k)` | `O(k)` for the heap, plus the output |
| Find only the R-th smallest overall (stop after `R` polls) | `O((k + R) log k)` | `O(k)` |

Compare:

| Method | Time |
|---|---:|
| Put everything in one list, then sort | `O(N log N)` |
| Merge two lists at a time, left to right | `O(N · k)` |
| **Heap K-way merge** | **`O(N log k)`** |

#### 8. Common K-Way Merge Patterns — Must Know

1. **Merge K Sorted Lists / Arrays** (LeetCode 23).
2. **Kth Smallest Element in a Sorted Matrix** (LeetCode 378) — each row is a sorted source. Stop after `k` polls.
3. **Find K Pairs with Smallest Sums** (LeetCode 373) — each row of the pair table is sorted.
4. **Smallest Range Covering Elements from K Lists** (LeetCode 632) — see "Smallest / Largest Range Problems".
5. **External sorting** — merge sorted chunks that do not fit in memory (`02-algorithm/01-sorting`, "External Sort" is awareness only).

#### 9. Edge Cases / Common Mistakes

1. Forgetting to push the **next** item from the same source after polling.
2. Not remembering the source. Without it you cannot find the next item.
3. Empty sources. Skip them at the start.
4. `k = 0` (no sources) or `k = 1` (just return the single source).
5. Comparing only the value in a `Pair` with a default comparator. Use a comparator on the value field.
6. Duplicates across sources. They are all kept, in any order among equal values.
7. Putting **all** items in the heap at the start. That turns it into a normal heap sort.

#### 10. When to Use / When Not to Use

**Use when:**

1. The sources are already sorted.
2. `k` is large, or the sources are streams or files.

**Avoid when:**

1. `k = 2`. A simple two-pointer merge is enough.
2. The sources are not sorted. Sort them first, or use another approach.

#### 11. Related Topics

1. Merge K Sorted Lists / Arrays
2. Smallest / Largest Range Problems
3. Heap Fundamentals
4. Merge Sort (`02-algorithm/01-sorting/04-Merge Sort.md`)
5. Divide and Conquer (`02-algorithm/03-Recursion & Divide and Conquer`)

#### 12. Interview Must Remember

1. Heap of **one item per source**: poll the smallest, push the next from the same source.
2. Heap size ≤ `k`, so total time is **`O(N log k)`**.
3. Each heap entry must remember **which source** it came from.
4. Recognise it from "`k` sorted ...".
