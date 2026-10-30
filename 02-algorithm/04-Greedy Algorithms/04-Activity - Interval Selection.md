# Activity / Interval Selection

> The most asked greedy family in FAANG interviews. Learn one rule: **sort by end time**.

#### 1. What Is It?

You get a list of intervals `[start, end]` (meetings, balloons, tasks). Common goals:

| Goal | Question |
|---|---|
| keep the most non-overlapping intervals | Activity Selection, Non-overlapping Intervals (435) |
| remove the fewest intervals so none overlap | Non-overlapping Intervals (435) |
| fewest arrows to burst all balloons | Minimum Arrows (452) |
| fewest rooms for all meetings | Meeting Rooms II (253) |
| merge overlapping intervals | Merge Intervals (56) |

#### 2. How It Works

**Rule: sort by end time. Keep an interval if it starts at or after the end of the last kept one.**

```text
[[1,2],[2,3],[3,4],[1,3]]  sorted by end:  [1,2] [2,3] [1,3] [3,4]

keep [1,2]  (lastEnd = 2)
keep [2,3]  (2 >= 2, lastEnd = 3)
skip [1,3]  (1 < 3, overlaps)
keep [3,4]  (3 >= 3)

kept = 3, so we remove 4 − 3 = 1 interval
```

Why end time: the interval that ends first leaves the most room for the rest (note 03).

**Minimum arrows (452).** Balloons are intervals on a line. One arrow at `x` bursts every balloon with `start <= x <= end`. Sort by end. Shoot at the end of the first balloon. All balloons that start at or before that point burst. When a balloon starts after it, shoot a new arrow at its end.

**Meeting Rooms II (253).** Count the most meetings happening at the same time. Sort all starts and all ends separately. Walk through the starts: if the next meeting starts before the earliest end, a new room is needed; otherwise a room is freed.

```text
[[0,30],[5,10],[15,20]]   starts: 0 5 15    ends: 10 20 30
0  < 10 → rooms = 1
5  < 10 → rooms = 2
15 >= 10 → reuse a room (move to the next end)
answer: 2
```

**Merge Intervals (56)** sorts by **start** instead. It is in the Array folder (`Interval Problems`). Do not mix up the two: *merging* sorts by start, *choosing the most* sorts by end.

#### 3. Brute Force vs Optimized

| Problem | Brute force | Optimized |
|---|---|---|
| Most non-overlapping | try every subset, `O(2^n)` | sort by end, `O(n log n)` |
| Meeting Rooms II | for each start, count meetings that cover it, `O(n²)` | sorted starts and ends, `O(n log n)` |

```kotlin
fun minMeetingRoomsBrute(intervals: Array<IntArray>): Int {
    var best = 0
    for (a in intervals) {
        var overlap = 0
        for (b in intervals) if (b[0] <= a[0] && a[0] < b[1]) overlap++   // b is running when a starts
        best = maxOf(best, overlap)
    }
    return best
}
```

The most overlap always happens at some meeting's start time, so checking each start is enough.

#### 4. Kotlin Code

```kotlin
// Non-overlapping Intervals (LeetCode 435): minimum number to remove
fun eraseOverlapIntervals(intervals: Array<IntArray>): Int {
    val sorted = intervals.sortedBy { it[1] }
    var kept = 0
    var lastEnd = Int.MIN_VALUE
    for (iv in sorted) {
        if (iv[0] >= lastEnd) { kept++; lastEnd = iv[1] }
    }
    return intervals.size - kept
}

// Minimum Number of Arrows to Burst Balloons (LeetCode 452)
fun findMinArrowShots(points: Array<IntArray>): Int {
    if (points.isEmpty()) return 0
    val sorted = points.sortedBy { it[1] }
    var arrows = 1
    var arrowAt = sorted[0][1]
    for (p in sorted) {
        if (p[0] > arrowAt) {                         // this balloon is missed: new arrow
            arrows++
            arrowAt = p[1]
        }
    }
    return arrows
}

// Meeting Rooms II (LeetCode 253)
fun minMeetingRooms(intervals: Array<IntArray>): Int {
    val starts = intervals.map { it[0] }.sorted()
    val ends = intervals.map { it[1] }.sorted()
    var rooms = 0
    var endPtr = 0
    for (s in starts) {
        if (s < ends[endPtr]) rooms++                 // no room is free yet
        else endPtr++                                 // reuse the room that just freed
    }
    return rooms
}
```

Checks: `eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])` → `1`. `eraseOverlapIntervals([[1,2],[1,2],[1,2]])` → `2`. `findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])` → `2`. `minMeetingRooms([[0,30],[5,10],[15,20]])` → `2`. `minMeetingRooms([[7,10],[2,4]])` → `1`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Sort by end + scan | `O(n log n)` | `O(n)` for the sorted copy |
| Meeting Rooms II | `O(n log n)` | `O(n)` |

#### 6. Common Mistakes

1. **Sorting by start** for "most intervals". Sort by **end**.
2. **Touching intervals** (`[1,2]`, `[2,3]`). In 435 and 253 they do **not** overlap (`>=`). In 452, balloons that touch **share** an arrow (`>` is the new-arrow test).
3. **Subtracting to compare** (`a[1] - b[1]`) which can overflow. Use `sortedBy`.
4. **Empty input** for arrows or rooms.
5. **Mixing up "kept" and "removed"** (answer is `n − kept`).
6. **Heap vs two arrays for rooms.** Both work. Say the one you can write without bugs.

#### 7. Say This in the Interview

1. "I sort by end time and keep an interval when it starts after the last kept end. The earliest end leaves the most room. `O(n log n)`."
2. "For rooms I need the maximum overlap, so I sort starts and ends separately and sweep."
3. "Do touching intervals count as overlapping?" (ask first)

#### 8. Quick Check

1. Answer for `[[1,2],[2,3]]` in problem 435?
2. Which sort key do you use for Merge Intervals?

<details>
<summary>Answers</summary>

1. `0` (touching intervals do not overlap).
2. Start time.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 252 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (Easy, premium) | sort, check neighbours |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (Medium) | sort by end |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium) | sort by end |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Medium, premium) | sweep or heap |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) | sort by start |
