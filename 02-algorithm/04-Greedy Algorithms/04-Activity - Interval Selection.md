# Activity / Interval Selection

#### 1. Definition — Must Know

1. **Activity selection** asks: given a set of activities, each with a start and end time, pick the **maximum number** of them that don't overlap.
2. It is the clearest, most classic example of greedy + sorting (topic 2) in action.

#### 2. Why It Is Used — Must Know

1. It's the "hello world" of greedy algorithms — nearly every scheduling or interval problem in interviews is a variation of it.
2. It shows the full pattern cleanly: sort by end time, then scan once with one running variable.

#### 3. How It Works — Must Know

```text
Meetings (start, end): (1,4) (3,5) (0,6) (5,7) (8,9) (5,9)

Sort by end time: (1,4) (3,5) (0,6) (5,7) (5,9) (8,9)

lastEnd = -infinity
(1,4): 1 >= lastEnd → pick it, lastEnd = 4
(3,5): 3 <  lastEnd → skip
(0,6): 0 <  lastEnd → skip
(5,7): 5 >= lastEnd → pick it, lastEnd = 7
(5,9): 5 <  lastEnd → skip
(8,9): 8 >= lastEnd → pick it, lastEnd = 9

Picked: (1,4), (5,7), (8,9)  →  3 activities
```

#### 4. Algorithm — Must Know

```text
sort activities by end time
lastEnd = -infinity
count = 0
for each activity in sorted order:
    if activity.start >= lastEnd:
        count += 1
        lastEnd = activity.end
return count
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun maxActivities(activities: List<Pair<Int, Int>>): Int {
    val sorted = activities.sortedBy { it.second }
    var lastEnd = Int.MIN_VALUE
    var count = 0
    for ((start, end) in sorted) {
        if (start >= lastEnd) {
            count++
            lastEnd = end
        }
    }
    return count
}
```

#### 6. Complexity — Must Know

| Step | Cost |
|---|---|
| Sort by end time | O(n log n) |
| Single scan | O(n) |
| Total | O(n log n) |

#### 7. Common Mistakes — Must Know

1. Sorting by **start** time or by **duration** instead of end time — both give wrong answers.
2. Using `>` instead of `>=` (or the reverse) when comparing `start` to `lastEnd` — get the boundary condition right based on whether activities that touch exactly at a shared point count as overlapping.
3. Trying to solve this with Dynamic Programming out of caution — it's unnecessary here, since the greedy choice is provably correct (topic 3).

#### 8. Related Topics

1. `2` Greedy + Sorting — the Usual Pairing
2. `3` Proving Correctness with an Exchange Argument — the proof for this exact problem
3. `SD 9` Merge Intervals (in `03-leetcode-patterns`) — overlapping-interval problems that build on this idea

#### 9. Interview Must Remember

1. **Sort by end time**, not start time — this is the detail people get wrong under pressure.
2. One running variable (`lastEnd`) is all the state this greedy scan needs.
3. This is the reference example to reach for whenever a new problem "smells like" scheduling or interval selection.
