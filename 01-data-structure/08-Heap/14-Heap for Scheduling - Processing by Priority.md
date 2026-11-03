# Heap for Scheduling / Processing by Priority

> "Always do the most important thing next" is a heap. This note covers the greedy-with-a-heap questions: schedulers, stones, and "save your best resource for later".

#### 1. What Is It?

In scheduling problems you **repeatedly choose the best available item**, and the set of available items changes. A heap picks the best in `O(log n)` and accepts new items in `O(log n)`.

| Question | Heap | Rule |
|---|---|---|
| **Last Stone Weight** (1046) | max-heap | smash the two heaviest |
| **Task Scheduler** (621) | max-heap of counts | run the most frequent task next |
| **Furthest Building You Can Reach** (1642) | min-heap of climbs | use ladders for the biggest climbs |
| **Single-Threaded CPU** (1834) | min-heap by (processing time, index) | run the shortest available task |
| **Meeting Rooms II** (253) | min-heap of end times | note 20 |

**Signals:** "process in order of priority", "the most / least X first", "simulate a CPU", "greedy but the best item changes".

#### 2. How It Works

**Last Stone Weight.** Take the two largest stones `a ≥ b`. If `a == b` both vanish. Else a stone of weight `a − b` returns. Repeat.

```text
[2, 7, 4, 1, 8, 1]
smash 8 and 7 → 1      [2, 4, 1, 1, 1]
smash 4 and 2 → 2      [2, 1, 1, 1]
smash 2 and 1 → 1      [1, 1, 1]
smash 1 and 1 → 0      [1]
answer 1
```

**Furthest Building You Can Reach.** You have `bricks` and `ladders`. A climb of height `d` costs `d` bricks, or one ladder (any height). A **ladder is best used on the biggest climbs**, bricks on the small ones.

- Keep a **min-heap of climbs that used a ladder**.
- For each climb `d > 0`: push `d`. If the heap holds more than `ladders` items, the **smallest** climb pays with **bricks** instead (`bricks -= poll()`). If `bricks < 0`, stop: you cannot go further.

```text
heights = [4, 2, 7, 6, 9, 14, 12], bricks = 5, ladders = 1
0→1: down, free
1→2: climb 5 → heap {5} (1 ladder). ok
2→3: down, free
3→4: climb 3 → heap {3, 5} too big → pay the smallest (3) with bricks: bricks 5 → 2. ok
4→5: climb 5 → heap {5, 5} → pay 5 with bricks: bricks 2 - 5 < 0 → stop at building 4
answer 4
```

**Task Scheduler** (simulation). Max-heap of counts. Each slot, run the task with the largest count, then park it for `n` slots (a queue). Time is counted per slot (full code in `ALG Greedy Algorithms` note 13).

#### 3. Brute Force vs Optimized

| Problem | Brute force | Heap |
|---|---|---|
| Last Stone Weight | re-sort the list each round: `O(n² log n)` | max-heap: `O(n log n)` |
| Furthest Building | try every assignment of ladders: exponential | min-heap of climbs: `O(n log L)` |

```kotlin
// Brute force: re-sort every round
fun lastStoneWeightBrute(stones: IntArray): Int {
    val list = stones.toMutableList()
    while (list.size > 1) {
        list.sortDescending()
        val a = list.removeAt(0)
        val b = list.removeAt(0)
        if (a != b) list.add(a - b)
    }
    return if (list.isEmpty()) 0 else list[0]
}
```

#### 4. Kotlin Code

```kotlin
import java.util.PriorityQueue

// Last Stone Weight (LeetCode 1046)
fun lastStoneWeight(stones: IntArray): Int {
    val heap = PriorityQueue<Int>(compareByDescending<Int> { it })
    for (s in stones) heap.add(s)
    while (heap.size > 1) {
        val a = heap.poll()
        val b = heap.poll()
        if (a != b) heap.add(a - b)
    }
    return if (heap.isEmpty()) 0 else heap.peek()
}

// Furthest Building You Can Reach (LeetCode 1642)
fun furthestBuilding(heights: IntArray, bricks: Int, ladders: Int): Int {
    val ladderClimbs = PriorityQueue<Int>()                  // min-heap: climbs that currently use a ladder
    var bricksLeft = bricks
    for (i in 0 until heights.size - 1) {
        val climb = heights[i + 1] - heights[i]
        if (climb <= 0) continue                             // going down or flat is free
        ladderClimbs.add(climb)
        if (ladderClimbs.size > ladders) {
            bricksLeft -= ladderClimbs.poll()                // the smallest climb pays with bricks
            if (bricksLeft < 0) return i                     // cannot reach building i + 1
        }
    }
    return heights.size - 1
}

// Single-Threaded CPU (LeetCode 1834): tasks[i] = [enqueueTime, processingTime]
fun getOrder(tasks: Array<IntArray>): IntArray {
    val order = tasks.indices.sortedBy { tasks[it][0] }      // by enqueue time
    val heap = PriorityQueue<Int>(compareBy<Int>({ tasks[it][1] }, { it }))   // shortest first, then index
    val result = IntArray(tasks.size)
    var time = 0L
    var next = 0
    var done = 0
    while (done < tasks.size) {
        if (heap.isEmpty() && time < tasks[order[next]][0]) time = tasks[order[next]][0].toLong()   // jump ahead when idle
        while (next < order.size && tasks[order[next]][0] <= time) heap.add(order[next++])
        val t = heap.poll()
        result[done++] = t
        time += tasks[t][1]
    }
    return result
}
```

Checks: `lastStoneWeight(intArrayOf(2, 7, 4, 1, 8, 1))` → `1`. `lastStoneWeight(intArrayOf(1))` → `1`. `lastStoneWeight(intArrayOf(2, 2))` → `0`. `lastStoneWeightBrute(intArrayOf(2, 7, 4, 1, 8, 1))` → `1`. `furthestBuilding(intArrayOf(4, 2, 7, 6, 9, 14, 12), 5, 1)` → `4`. `furthestBuilding(intArrayOf(4, 12, 2, 7, 3, 18, 20, 3, 19), 10, 2)` → `7`. `furthestBuilding(intArrayOf(14, 3, 19, 3), 17, 0)` → `3`. `getOrder(arrayOf(intArrayOf(1, 2), intArrayOf(2, 4), intArrayOf(3, 2), intArrayOf(4, 1)))` → `[0, 2, 3, 1]`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Last Stone Weight | `O(n log n)` | `O(n)` |
| Furthest Building | `O(n log L)` for `L` ladders | `O(L)` |
| Single-Threaded CPU | `O(n log n)` | `O(n)` |

#### 6. Common Mistakes

1. **Re-sorting** every round instead of using a heap.
2. **Furthest Building:** spending bricks first on the biggest climbs. Ladders are for the **biggest** climbs.
3. **Treating downhill climbs** as costs. Only positive differences count.
4. **CPU:** forgetting to jump `time` forward when the heap is empty.
5. **CPU:** forgetting the tie-break by index.
6. **Returning the wrong index** in Furthest Building (the loop index `i` is the last reachable building when the next one fails).

#### 7. Say This in the Interview

1. "I always need the best available item next, and the available set changes, so I'll use a heap."
2. "In Furthest Building, ladders are best spent on the biggest climbs. I keep a min-heap of the climbs that currently use ladders. When it exceeds the ladder count, the smallest one pays with bricks."
3. "Each operation is `O(log n)`, so the whole simulation is `O(n log n)`."

#### 8. Quick Check

1. `lastStoneWeight` of `[3, 3, 3]`?
2. Why does Furthest Building use a **min**-heap?
3. In the CPU problem, what if no task is available at the current time?

<details>
<summary>Answers</summary>

1. `3`. Smash two `3`s to nothing, one `3` is left.
2. The root is the **smallest** ladder climb. When there are too many, that one is the best to replace with bricks.
3. Jump the clock to the next task's enqueue time.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (Easy) | max-heap |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium) | max-heap of counts |
| 1642 | [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/) (Medium) | min-heap of ladder climbs |
| 1834 | [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) (Medium) | shortest available task |
| 767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) (Medium) | max-heap, two letters |
| 1353 | [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) (Medium) | min-heap of end days |
