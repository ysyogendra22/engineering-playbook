# Interval Problems

> A FAANG favourite: Merge Intervals, Insert Interval, Meeting Rooms. Almost all of them start with the same step: **sort by start time**.

#### 1. What Is It?

An **interval** is a range `[start, end]`, for example a meeting from 9 to 11. Interval problems ask you to **merge**, **insert**, **count overlaps** or **remove overlaps**.

Two intervals `a` and `b` **overlap** when each one starts before the other ends:

```text
a.start <= b.end  and  b.start <= a.end        (touching at one point, like [1,3] and [3,5], counts as overlap in "merge")
```

The main idea: **sort by start**. Then overlapping intervals sit next to each other, and one pass finishes the job.

| Problem | Method |
|---|---|
| Merge Intervals | sort by start, merge neighbours |
| Insert Interval | already sorted: copy, merge, copy |
| Non-overlapping Intervals (remove the fewest) | sort by **end**, keep the earliest-ending |
| Meeting Rooms II (rooms needed) | sort starts and ends / events (note 29), or a min-heap of end times |
| Burst Balloons (fewest arrows) | sort by end, shoot at the end |

#### 2. How It Works

*Merge Intervals* (LeetCode 56): `[[1,3],[2,6],[8,10],[15,18]]`

```text
sorted by start: [1,3] [2,6] [8,10] [15,18]
result = [[1,3]]
[2,6]:   2 <= 3 (overlaps the last) → merge: end = max(3, 6) = 6    result [[1,6]]
[8,10]:  8 > 6  (no overlap)        → add                           result [[1,6],[8,10]]
[15,18]: 15 > 10                    → add                           result [[1,6],[8,10],[15,18]]
```

*Non-overlapping Intervals* (LeetCode 435): remove the fewest intervals so none overlap. **Greedy:** sort by **end**. Keep an interval if it starts at or after the end of the last kept one. Otherwise remove it. The earliest-ending interval leaves the most room for the rest.

#### 3. Brute Force vs Optimized

| | Brute force | Sort + one pass |
|---|---|---|
| Idea | compare every pair, merge repeatedly | sort, then compare only with the last result |
| Time | `O(n²)` or worse | `O(n log n)` |
| Space | `O(n)` | `O(n)` for the output |

The brute force repeats "find two overlapping intervals, merge them" until none are left. Sorting removes the need to search.

#### 4. Kotlin Code

```kotlin
// Merge Intervals (LeetCode 56)
fun merge(intervals: Array<IntArray>): Array<IntArray> {
    if (intervals.isEmpty()) return arrayOf()
    val sorted = intervals.sortedBy { it[0] }
    val result = mutableListOf(sorted[0].copyOf())
    for (i in 1 until sorted.size) {
        val last = result.last()
        if (sorted[i][0] <= last[1]) last[1] = maxOf(last[1], sorted[i][1])    // overlap: extend the end
        else result.add(sorted[i].copyOf())
    }
    return result.toTypedArray()
}

// Insert Interval (LeetCode 57): the list is already sorted
fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
    val result = mutableListOf<IntArray>()
    var i = 0
    val n = intervals.size
    while (i < n && intervals[i][1] < newInterval[0]) result.add(intervals[i++])   // 1. before the new one
    var start = newInterval[0]
    var end = newInterval[1]
    while (i < n && intervals[i][0] <= end) {                                      // 2. overlapping: merge
        start = minOf(start, intervals[i][0])
        end = maxOf(end, intervals[i][1])
        i++
    }
    result.add(intArrayOf(start, end))
    while (i < n) result.add(intervals[i++])                                       // 3. after the new one
    return result.toTypedArray()
}

// Non-overlapping Intervals (LeetCode 435): the fewest to remove
fun eraseOverlapIntervals(intervals: Array<IntArray>): Int {
    val sorted = intervals.sortedBy { it[1] }               // sort by END
    var end = Int.MIN_VALUE
    var removed = 0
    for (interval in sorted) {
        if (interval[0] >= end) end = interval[1]            // keep it
        else removed++                                       // overlaps the last kept one: remove it
    }
    return removed
}

// Meeting Rooms (LeetCode 252): can one person attend all meetings?
fun canAttendMeetings(intervals: Array<IntArray>): Boolean {
    val sorted = intervals.sortedBy { it[0] }
    for (i in 1 until sorted.size) if (sorted[i][0] < sorted[i - 1][1]) return false
    return true
}

// Minimum Number of Arrows to Burst Balloons (LeetCode 452)
fun findMinArrowShots(points: Array<IntArray>): Int {
    val sorted = points.sortedBy { it[1] }                  // sort by END
    var arrows = 0
    var lastShot = Long.MIN_VALUE
    for (p in sorted) {
        if (p[0] > lastShot) { arrows++; lastShot = p[1].toLong() }   // a new arrow at this balloon's end
    }
    return arrows
}
```

Checks: `merge([[1,3],[2,6],[8,10],[15,18]])` → `[[1,6],[8,10],[15,18]]`. `insert([[1,3],[6,9]], [2,5])` → `[[1,5],[6,9]]`. `eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])` → `1`. `findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])` → `2`.

For **Meeting Rooms II** (the most rooms needed at once) see the sweep line note (29).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Merge Intervals | `O(n log n)` | `O(n)` |
| Insert Interval (already sorted) | `O(n)` | `O(n)` |
| Non-overlapping, Meeting Rooms I, Arrows | `O(n log n)` | `O(1)` extra |

#### 6. Common Mistakes

1. **Not sorting first.**
2. **Merging with `<` instead of `<=`** when touching intervals count as overlapping (`[1,3]` and `[3,5]` merge in LeetCode 56).
3. **Forgetting `maxOf` for the end.** An interval can be inside another one: `[1,10]` and `[2,3]`.
4. **Changing the input intervals** when copies are better (`copyOf()`).
5. **Sorting by start** when the greedy needs **end** (Non-overlapping Intervals, Arrows).
6. **Empty input.**

#### 7. Say This in the Interview

1. "I sort by start time so overlapping intervals are neighbours. Then I merge in one pass. Time `O(n log n)`."
2. "Two intervals overlap when `next.start <= last.end`. When they do, the new end is the `max` of the two ends."
3. "For 'remove the fewest', I sort by end and keep the interval that ends first."

#### 8. Quick Check

1. Do `[1, 3]` and `[3, 5]` merge in Merge Intervals?
2. For `[1, 10]` and `[2, 3]`, what is the merged interval?

<details>
<summary>Answers</summary>

1. Yes, they touch at 3, giving `[1, 5]`.
2. `[1, 10]`. Use `max(10, 3)` for the end.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 252 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (Easy, premium) | sort, check neighbours |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) | sort by start, merge |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) (Medium) | before, merge, after |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (Medium) | sort by end, greedy |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium) | sort by end, greedy |
| 986 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) (Medium) | two pointers over two lists |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Medium, premium) | sweep line or heap (note 29) |
