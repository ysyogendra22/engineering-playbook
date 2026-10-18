# Multiple Heap / Advanced Two-Heaps Patterns

#### 1. Definition — Must Know

1. Some problems need **more than one heap**, each with a different job.
2. Two common shapes:
   - **Balanced two heaps** — one for the lower half and one for the upper half (the median pattern), extended with deletion.
   - **Pipeline of two heaps** — one heap holds items that are **not ready yet**, the other holds items that are **ready**, ordered by profit or priority.
3. The main examples: **Sliding Window Median** (LeetCode 480) and **IPO** (LeetCode 502). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. One order is not enough. IPO needs "cheapest first" to unlock items and "most profitable first" to pick items.
2. Sliding Window Median needs the two-heaps median trick plus items that **leave** the window.
3. Both are common "hard" interview problems. Knowing the structure matters more than remembering every line.

#### 3. How It Works — Must Know

**Pipeline pattern — IPO.** You start with capital `w`, can finish at most `k` projects, and each project needs a minimum capital and gives a profit. Maximise final capital.

```text
profits = [1, 2, 3]     capital = [0, 1, 1]     k = 2     w = 0

Heap A: all projects, min-heap by REQUIRED CAPITAL     (not affordable yet)
Heap B: affordable projects, max-heap by PROFIT        (ready to pick)

Round 1: w = 0 → move every project with capital <= 0 from A to B  → B has project 0 (profit 1)
         pick the best from B → profit 1 → w = 1
Round 2: w = 1 → move projects with capital <= 1 from A to B       → B has projects 1, 2
         pick the best from B → profit 3 → w = 4

Answer: 4
```

**Balanced pattern — Sliding Window Median.** Keep the window split into a lower half (max-heap) and an upper half (min-heap) with sizes differing by at most one. When the window slides:

```text
add the new number      → push to the right heap, rebalance
remove the old number   → mark it deleted (lazy), fix the "valid size" of its heap, rebalance
median                  → top of the lower heap (odd size) or the average of both tops (even size)
```

#### 4. Core Concepts — Must Know

1. **Each heap has one clear job.** Write it down before coding.
2. **Move items between heaps** as conditions change (affordable, ready, balanced).
3. **Two sizes must be tracked** when you use lazy deletion. `heap.size` includes stale items, so keep `lowSize` and `highSize` of valid items.
4. **Rebalance after every change.** Valid sizes must satisfy `lowSize == highSize` or `lowSize == highSize + 1`.
5. **Prune tops** after removing or moving an item, so each heap top is always a live item.
6. Patterns at a glance:

| Problem | Heap 1 | Heap 2 |
|---|---|---|
| Find Median from Data Stream | max-heap, lower half | min-heap, upper half |
| Sliding Window Median | same, plus lazy deletion | same |
| IPO | min-heap by capital (locked) | max-heap by profit (unlocked) |
| Maximum Performance of a Team (LC 1383) | sort by efficiency, then one min-heap of speeds | — |
| Process tasks by time (LC 1834) | tasks sorted by start | min-heap of ready tasks by duration |

#### 5. Algorithm — Must Know

**IPO**

```text
locked   = min-heap of project indexes by capital
unlocked = max-heap of project indexes by profit
repeat k times:
    while locked is not empty and capital[locked.peek()] <= wealth:
        unlocked.add(locked.poll())
    if unlocked is empty: stop
    wealth += profit[unlocked.poll()]
return wealth
```

**Sliding Window Median:** see the code below.

#### 6. Kotlin Implementation — Must Know

**IPO**

```kotlin
import java.util.PriorityQueue

fun findMaximizedCapital(k: Int, w: Int, profits: IntArray, capital: IntArray): Int {
    val locked = PriorityQueue<Int>(compareBy<Int> { capital[it] })              // by required capital
    val unlocked = PriorityQueue<Int>(compareByDescending<Int> { profits[it] })  // by profit
    for (i in profits.indices) locked.add(i)

    var wealth = w
    repeat(k) {
        while (locked.isNotEmpty() && capital[locked.peek()] <= wealth) {
            unlocked.add(locked.poll())
        }
        if (unlocked.isEmpty()) return wealth        // nothing affordable: stop early
        wealth += profits[unlocked.poll()]
    }
    return wealth
}
```

The `Int` sum is fine for the usual problem limits. Use `Long` if your limits are bigger.

**Sliding Window Median (read it for the structure, don't memorise it)**

```kotlin
fun medianSlidingWindow(nums: IntArray, k: Int): DoubleArray {
    val low = PriorityQueue<Int>(Comparator.reverseOrder())   // max-heap: lower half
    val high = PriorityQueue<Int>()                           // min-heap: upper half
    val delayed = HashMap<Int, Int>()                         // value → pending deletions
    var lowSize = 0                                           // valid items only
    var highSize = 0

    fun prune(heap: PriorityQueue<Int>) {
        while (heap.isNotEmpty()) {
            val top = heap.peek()
            val pending = delayed[top] ?: break
            if (pending == 1) delayed.remove(top) else delayed[top] = pending - 1
            heap.poll()
        }
    }

    fun balance() {
        if (lowSize > highSize + 1) {
            high.add(low.poll()); lowSize--; highSize++
            prune(low)
        } else if (lowSize < highSize) {
            low.add(high.poll()); highSize--; lowSize++
            prune(high)
        }
    }

    fun add(x: Int) {
        if (low.isEmpty() || x <= low.peek()) { low.add(x); lowSize++ } else { high.add(x); highSize++ }
        balance()
    }

    fun remove(x: Int) {
        delayed[x] = (delayed[x] ?: 0) + 1
        if (x <= low.peek()) {
            lowSize--
            if (x == low.peek()) prune(low)
        } else {
            highSize--
            if (x == high.peek()) prune(high)
        }
        balance()
    }

    fun median(): Double =
        if (k % 2 == 1) low.peek().toDouble()
        else (low.peek().toLong() + high.peek()) / 2.0

    val result = DoubleArray(nums.size - k + 1)
    for (i in 0 until k) add(nums[i])
    result[0] = median()
    for (i in k until nums.size) {
        add(nums[i])
        remove(nums[i - k])
        result[i - k + 1] = median()
    }
    return result
}
```

Why it works: the tops of both heaps are always live (we prune after every change), `lowSize`/`highSize` count only live items, and the removal goes to the side where the value belongs.

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| IPO | `O((n + k) log n)` | `O(n)` |
| Sliding Window Median | `O(n log k)` amortized | `O(n)` with stale items |
| Find Median from Data Stream (for comparison) | `O(log n)` per add | `O(n)` |

#### 8. Common Multi-Heap Patterns — Must Know

1. **Locked / unlocked** (IPO, task scheduling by start time, meetings by arrival).
2. **Lower half / upper half** (running median, sliding window median).
3. **Sort once + one heap** (Maximum Performance of a Team, Course Schedule III): when sorting handles one rule, a single heap handles the second.
4. **Two heaps for window min and max** (longest subarray with a limited difference).
5. **Alternative:** a `TreeMap` of counts (or a sorted structure) can replace two heaps in the sliding median, and gives easy exact deletion.

#### 9. Edge Cases / Common Mistakes

1. Writing code before deciding what each heap means.
2. Using `heap.size` instead of the valid size when stale items exist.
3. Forgetting to prune the top after moving or removing an item, so a stale top is read as the median.
4. Removing from the wrong side when values equal the boundary (`<=` versus `<`). Follow one rule everywhere.
5. IPO: not stopping when no project is affordable.
6. IPO: using one heap and re-sorting each round, which is slow.
7. Overflow when adding two values to find the average. Convert to `Long` first.
8. Even-size windows: forgetting to take both tops.
9. Treating the `delayed` map as a set when duplicate values exist.

#### 10. When to Use / When Not to Use

**Use when:**

1. One ordering unlocks items and another picks the best (IPO-style).
2. You need a median or a split point that changes as items arrive and leave.

**Avoid when:**

1. One sort plus one heap already solves it.
2. An order-statistic structure (such as a `TreeMap`) is simpler and speed is not critical.

#### 11. Related Topics

1. Two Heaps Pattern
2. Find Median from Data Stream
3. Lazy Deletion with Heap
4. Heap + Sliding Window
5. Heap for Scheduling / Processing by Priority

#### 12. Interview Must Remember

1. **Give each heap one job** and say it out loud.
2. IPO: min-heap by capital to unlock, max-heap by profit to choose.
3. Sliding Window Median: two heaps + lazy deletion + **valid sizes** + prune the tops.
4. If it gets too heavy, say that a `TreeMap` of counts is a valid alternative.
