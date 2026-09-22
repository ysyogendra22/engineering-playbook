# Greedy + Sorting — the Usual Pairing

#### 1. Definition — Must Know

1. Most greedy algorithms follow the same shape: **sort the input by some key first, then scan through it once, making the obvious choice at each step.**
2. The sort is what makes the "obvious choice" actually work — without it, the greedy step usually has nothing sensible to compare against.

#### 2. Why It Is Used — Must Know

1. Sorting puts the input in an order where the best local choice is easy to see and cheap to make (usually just "look at the next item").
2. It turns an unclear problem into a simple, predictable pass: sort once, then one linear scan.

#### 3. How It Works — Must Know

Example: Activity Selection — pick the maximum number of non-overlapping meetings.

```text
Meetings (start, end): (1,4) (3,5) (0,6) (5,7) (8,9) (5,9)

Sort by end time:
(1,4) (3,5) (0,6) (5,7) (5,9) (8,9)

Scan, picking a meeting only if it starts after the last picked one ends:
Pick (1,4)              lastEnd = 4
Skip (3,5)  starts at 3, before lastEnd = 4
Skip (0,6)  starts at 0, before lastEnd = 4
Pick (5,7)              lastEnd = 7
Skip (5,9)  starts at 5, before lastEnd = 7
Pick (8,9)              lastEnd = 9

Result: (1,4), (5,7), (8,9) — 3 meetings
```

#### 4. Algorithm — Must Know

```text
function greedySelect(items):
    sort items by the chosen key
    result = []
    for item in sorted items:
        if item is compatible with what's already chosen:
            add item to result
    return result
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun maxNonOverlapping(meetings: List<Pair<Int, Int>>): List<Pair<Int, Int>> {
    val sorted = meetings.sortedBy { it.second }   // sort by end time
    val result = mutableListOf<Pair<Int, Int>>()
    var lastEnd = Int.MIN_VALUE
    for (meeting in sorted) {
        if (meeting.first >= lastEnd) {
            result.add(meeting)
            lastEnd = meeting.second
        }
    }
    return result
}
```

#### 6. Complexity — Must Know

| Step | Cost |
|---|---|
| Sort | O(n log n) |
| Scan | O(n) |
| Total | O(n log n) — the sort dominates |

#### 7. Common Mistakes — Must Know

1. Sorting by the wrong key (for example, sorting activities by *start* time instead of *end* time — that gives a wrong answer for Activity Selection).
2. Skipping the sort step and trying to scan the input in its original order.
3. Forgetting to track the running state (`lastEnd` here) that each new choice needs to be compared against.

#### 8. Related Topics

1. `1` The Greedy Choice Property — why sorting alone isn't proof of correctness
2. `4` Activity / Interval Selection — the fuller version of this example
3. `SD 9` Merge Intervals (in `03-leetcode-patterns`) — the closely related pattern

#### 9. Interview Must Remember

1. When you reach for greedy, ask: **"what should I sort by?"** — that's usually the whole idea.
2. Sort by end time for "pick the maximum number of non-overlapping things" problems.
3. After sorting, the scan is usually a single pass with one running variable tracking the last choice.
