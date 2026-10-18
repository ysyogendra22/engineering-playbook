# Meeting Rooms / Scheduling with Heap

#### 1. Definition — Must Know

1. **Meeting Rooms II** asks: given meeting time intervals `[start, end]`, what is the **minimum number of rooms** needed so no two meetings overlap in the same room?
2. The heap keeps the **end times of meetings that are still running**.
3. This note is about *Meeting Rooms II* (LeetCode 253, premium). A free, closely related problem is *Car Pooling* (LeetCode 1094). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is the classic "heap + sorted intervals" problem.
2. The same idea answers "how many servers, rooms, or workers do I need at the busiest time?"
3. It builds on the interval ideas in `03-leetcode-patterns` (topic 9, Merge Intervals).

#### 3. How It Works — Must Know

Meetings: `[0, 30]`, `[5, 10]`, `[15, 20]`.

```text
Sort by start time:  [0,30]  [5,10]  [15,20]
Min-heap of end times of rooms in use:

[0, 30]  → heap empty, need a room.                      add 30      heap: [30]       rooms = 1
[5, 10]  → earliest end is 30; 30 <= 5? No → new room.  add 10      heap: [10, 30]   rooms = 2
[15, 20] → earliest end is 10; 10 <= 15? Yes → reuse.   remove 10, add 20   heap: [20, 30]   rooms = 2

Answer: 2   (the heap size is the number of rooms in use)
```

The heap root is the room that becomes free first. If that meeting has already ended when the next one starts, reuse the room.

#### 4. Core Concepts — Must Know

1. **Sort meetings by start time.**
2. **Min-heap of end times.** The root is the earliest end.
3. For each meeting:
   - if `heap.peek() <= start` → the room is free: **remove** that end time,
   - then **add** this meeting's end time.
4. **Answer = final heap size** (or the largest size reached; for this method they are the same).
5. A meeting that ends exactly when another starts (`end == start`) does **not** overlap. Use `<=`.

#### 5. Algorithm — Must Know

```text
sort intervals by start
heap = min-heap of end times

for each interval in sorted order:
    if heap is not empty and heap.peek() <= interval.start:
        heap.poll()                       // reuse that room
    heap.add(interval.end)

return heap.size
```

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

fun minMeetingRooms(intervals: Array<IntArray>): Int {
    if (intervals.isEmpty()) return 0
    val sorted = intervals.sortedBy { it[0] }
    val ends = PriorityQueue<Int>()          // end times of meetings in progress

    for (meeting in sorted) {
        if (ends.isNotEmpty() && ends.peek() <= meeting[0]) {
            ends.poll()                      // a room became free
        }
        ends.add(meeting[1])
    }
    return ends.size
}
```

**Two pointers over sorted starts and ends (no heap, same time)**

```kotlin
fun minMeetingRoomsSweep(intervals: Array<IntArray>): Int {
    val starts = intervals.map { it[0] }.sorted()
    val ends = intervals.map { it[1] }.sorted()
    var rooms = 0
    var endIndex = 0
    for (start in starts) {
        if (start < ends[endIndex]) rooms++      // everything still running: need another room
        else endIndex++                           // one meeting ended: reuse its room
    }
    return rooms
}
```

**Meeting Rooms I** (can one person attend all meetings?) needs no heap. Sort by start and check that each meeting starts at or after the previous one ends:

```kotlin
fun canAttendAll(intervals: Array<IntArray>): Boolean {
    val sorted = intervals.sortedBy { it[0] }
    for (i in 1 until sorted.size) {
        if (sorted[i][0] < sorted[i - 1][1]) return false
    }
    return true
}
```

#### 7. Time & Space Complexity — Must Know

| Step | Time |
|---|---:|
| Sort by start | `O(n log n)` |
| Heap work (`n` adds, up to `n` polls) | `O(n log n)` |
| **Total** | **`O(n log n)`** |
| Space | `O(n)` |

#### 8. Common Scheduling Patterns — Must Know

1. **Meeting Rooms II** (LeetCode 253, premium) — this note.
2. **Car Pooling** (LeetCode 1094) — a free alternative. Use the same sweep or a heap of drop-off times.
3. **Minimum number of platforms** for trains, or servers for requests, at the busiest moment.
4. **Task Scheduler** (LeetCode 621) — a max-heap of remaining task counts with a cooldown.
5. **Employee Free Time** and **Merge Intervals** — sorting plus merging (`03-leetcode-patterns`, topic 9).

#### 9. Edge Cases / Common Mistakes

1. Not sorting by start time first.
2. Using `<` instead of `<=`, so meetings that touch at one time are wrongly counted as overlapping.
3. Using a max-heap of end times.
4. Storing start times in the heap instead of end times.
5. Removing the earliest end only sometimes. Do it when the room is free, and always add the new end.
6. Empty input.
7. Worrying about "maximum size" versus "final size". They are equal here because each step either keeps the heap size or grows it by one, so it never shrinks. Be able to explain why.

#### 10. When to Use / When Not to Use

**Use the heap when:**

1. You also need to know *which* room is reused, or process intervals as they come.

**Use the two-pointer sweep when:**

1. You only need the count. It is shorter and uses simple arrays.

**Avoid both when:**

1. The times are small integers in a known range. A difference array over time is `O(n + range)`.

#### 11. Related Topics

1. Heap for Scheduling / Processing by Priority
2. Merge Intervals (`03-leetcode-patterns`, topic 9)
3. Greedy Algorithms (`02-algorithm/04-Greedy Algorithms`)
4. Sorting (`02-algorithm/01-sorting`)

#### 12. Interview Must Remember

1. **Sort by start. Min-heap of end times.**
2. If the earliest end `<=` the new start, **reuse** (remove it). Always **add** the new end.
3. **Heap size = rooms needed.**
4. `O(n log n)`. Say the free alternative: Car Pooling.
