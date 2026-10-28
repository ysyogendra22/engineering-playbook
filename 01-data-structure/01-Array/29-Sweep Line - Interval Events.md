# Sweep Line / Interval Events

> The clean way to answer "how many things overlap at once?" and "when is the busiest time?".

#### 1. What Is It?

The **sweep line** idea: turn every interval into **two events** and walk through them in time order.

- At `start` → something begins: **+1**.
- At `end` → something finishes: **−1**.

Imagine a vertical line moving from left to right. At each event you update a running count. The **maximum of the running count** is the most overlap at the same time.

```text
meetings: [0,30] [5,10] [15,20]
events:   (0,+1) (5,+1) (10,-1) (15,+1) (20,-1) (30,-1)
running:     1      2       1       2       1       0       → maximum 2 → 2 rooms needed
```

How to spot it: "minimum meeting rooms", "maximum overlap", "busiest time", "is any pair double-booked", "car pooling", "skyline".

#### 2. How It Works

Steps:

1. Create events `(time, change)`: `+1` at the start, `-1` at the end.
2. **Sort by time.** If two events have the **same time**, process the **end (−1) first**, so an interval that ends at 10 does not overlap one that starts at 10.
3. Walk through the events, keep the running count, and track the maximum.

For *My Calendar* (LeetCode 729): you add bookings one by one, and a booking is refused if it overlaps an existing one. Two intervals `[s1, e1)` and `[s2, e2)` overlap when `s1 < e2 && s2 < e1`.

The same idea with a **difference array** (note 19) works when times are small integers. Events + sorting works for any times.

#### 3. Brute Force vs Optimized

| | Brute force | Sweep line |
|---|---|---|
| Idea | for every interval, count how many others overlap it | sort events, one pass |
| Time | `O(n²)` | `O(n log n)` |
| Space | `O(1)` | `O(n)` |

```kotlin
fun maxOverlapBrute(intervals: Array<IntArray>): Int {
    var best = 0
    for (a in intervals) {
        var count = 0
        for (b in intervals) if (b[0] <= a[0] && a[0] < b[1]) count++     // how many are running when a starts
        best = maxOf(best, count)
    }
    return best
}
```

#### 4. Kotlin Code

```kotlin
// Meeting Rooms II (LeetCode 253): the minimum number of rooms
fun minMeetingRooms(intervals: Array<IntArray>): Int {
    val events = ArrayList<IntArray>()
    for ((start, end) in intervals) {
        events.add(intArrayOf(start, 1))                   // a meeting starts
        events.add(intArrayOf(end, -1))                    // a meeting ends
    }
    events.sortWith(compareBy({ it[0] }, { it[1] }))       // by time; at the same time, -1 comes before +1
    var running = 0
    var best = 0
    for (event in events) {
        running += event[1]
        best = maxOf(best, running)
    }
    return best
}

// My Calendar I (LeetCode 729): refuse a booking if it overlaps an old one
class MyCalendar {
    private val bookings = mutableListOf<IntArray>()

    fun book(start: Int, end: Int): Boolean {
        for (b in bookings) if (start < b[1] && b[0] < end) return false      // overlap
        bookings.add(intArrayOf(start, end))
        return true
    }
}

// Car Pooling (LeetCode 1094) with events: trips are [passengers, from, to]
fun carPooling(trips: Array<IntArray>, capacity: Int): Boolean {
    val events = ArrayList<IntArray>()
    for ((passengers, from, to) in trips) {
        events.add(intArrayOf(from, passengers))
        events.add(intArrayOf(to, -passengers))
    }
    events.sortWith(compareBy({ it[0] }, { it[1] }))       // at the same time, drop-offs (negative) come first
    var onBoard = 0
    for (event in events) {
        onBoard += event[1]
        if (onBoard > capacity) return false
    }
    return true
}
```

Checks: `minMeetingRooms([[0,30],[5,10],[15,20]])` → `2`. `minMeetingRooms([[7,10],[2,4]])` → `1`. `carPooling([[2,1,5],[3,3,7]], 4)` → `false`. `carPooling([[2,1,5],[3,5,7]], 3)` → `true`.

The `MyCalendar` version above is `O(n)` per booking. A `TreeMap` makes it `O(log n)`.

The Skyline Problem (LeetCode 218, Hard) is a sweep line with a max-heap of building heights.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Sort events + one pass | `O(n log n)` | `O(n)` |
| Same with small integer times (difference array) | `O(n + range)` | `O(range)` |

#### 6. Common Mistakes

1. **Wrong order for equal times.** Process **ends before starts**, or touching intervals look like an overlap.
2. **Forgetting to sort the events.**
3. **Mixing half-open and closed intervals.** `[1, 5]` and `[5, 8]` overlap if closed, not if half-open. Read the question.
4. **Only counting starts** and not subtracting ends.
5. **Sorting only by time** with an unstable approach and getting a random order for ties.
6. **Overlap check typo** (`<` vs `<=`).

#### 7. Say This in the Interview

1. "I turn each interval into two events: +1 at the start and −1 at the end. I sort them and keep a running count. The maximum is the answer. Time `O(n log n)`."
2. "At the same time, ends come before starts, so touching meetings do not count as overlapping."

#### 8. Quick Check

1. How many events does `n` intervals create?
2. For `[1, 5]` and `[5, 8]` as meetings, do they need two rooms?

<details>
<summary>Answers</summary>

1. `2n` (a start and an end for each).
2. No. The first ends at 5 when the second starts. One room is enough.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 252 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (Easy, premium) | any overlap? |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Medium, premium) | maximum overlap |
| 729 | [My Calendar I](https://leetcode.com/problems/my-calendar-i/) (Medium) | overlap check |
| 731 | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) (Medium) | refuse a triple booking |
| 1094 | [Car Pooling](https://leetcode.com/problems/car-pooling/) (Medium) | passengers on board |
| 218 | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) (Hard) | sweep + max-heap |
