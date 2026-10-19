# Smallest / Largest Range Problems

#### 1. Definition — Must Know

1. These problems ask for a **range `[a, b]`** that satisfies a rule across several lists or items.
2. The main example is **Smallest Range Covering Elements from K Lists** (LeetCode 632): find the smallest range `[a, b]` that contains **at least one number from each of `k` sorted lists**. If a number and a title ever disagree, trust the title.
3. The heap tracks the **current minimum** of one element per list. A separate variable tracks the **current maximum**.

#### 2. Why It Is Used — Must Know

1. It extends K-way merge. The same heap of "one element per list" now answers a range question.
2. It shows a useful pattern: **heap for the minimum, a variable for the maximum.**
3. It is a common "hard" heap question, so it is worth knowing the idea.

#### 3. How It Works — Must Know

Lists: `A = [4, 10, 15]`, `B = [0, 9, 12]`, `C = [5, 18, 22]`.

```text
Take the first element of each list:  4, 0, 5      min = 0, max = 5     range [0, 5]  (size 5)

The range must include one number from every list.
To make it smaller we must raise the minimum, so move the list that owns the minimum.

Remove 0 (list B), take B's next → 9:   4, 9, 5    min = 4, max = 9     range [4, 9]   (size 5)
Remove 4 (list A), take A's next → 10:  10, 9, 5   min = 5, max = 10    range [5, 10]  (size 5)
Remove 5 (list C), take C's next → 18:  10, 9, 18  min = 9, max = 18    range [9, 18]  (size 9)
...keep going, remember the smallest range seen...
Stop when the list that owns the minimum has no next element.
```

The range is always `[current min, current max]`. A smaller range can only come from moving the minimum up.

#### 4. Core Concepts — Must Know

1. **Min-heap** holds one element from each list: `[value, listIndex, elementIndex]`.
2. **`currentMax`** is the largest value among the elements in the heap. It only increases (lists are sorted).
3. **Range now = `[heap.peek().value, currentMax]`.** Compare its size to the best so far.
4. **Move forward only the list that owns the minimum.** Any other move cannot shrink the range.
5. **Stop** when that list has no more elements, because the range could no longer include every list.

#### 5. Algorithm — Must Know

```text
heap = min-heap by value
currentMax = -infinity
for each list i:
    push (list[i][0], i, 0)
    currentMax = max(currentMax, list[i][0])
best = [heap.peek().value, currentMax]

loop:
    (value, i, j) = heap.poll()
    if currentMax - value < best size: best = [value, currentMax]
    if j + 1 == list[i].size: stop
    push (list[i][j+1], i, j+1)
    currentMax = max(currentMax, list[i][j+1])
return best
```

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

fun smallestRange(nums: List<List<Int>>): IntArray {
    // Each entry: [value, listIndex, elementIndex]
    val heap = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })
    var currentMax = Int.MIN_VALUE

    for ((i, list) in nums.withIndex()) {
        heap.add(intArrayOf(list[0], i, 0))
        currentMax = maxOf(currentMax, list[0])
    }

    var bestLow = heap.peek()[0]
    var bestHigh = currentMax

    while (true) {
        val (value, listIndex, elementIndex) = heap.poll()

        // Long avoids overflow when values are near Int limits
        if (currentMax.toLong() - value < bestHigh.toLong() - bestLow) {
            bestLow = value
            bestHigh = currentMax
        }

        val next = elementIndex + 1
        if (next == nums[listIndex].size) break        // this list is used up

        val nextValue = nums[listIndex][next]
        heap.add(intArrayOf(nextValue, listIndex, next))
        currentMax = maxOf(currentMax, nextValue)
    }
    return intArrayOf(bestLow, bestHigh)
}
```

Example: `[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]` → `[20, 24]`.

The strict `<` keeps the **first** range found on a tie. The minimum only rises, so that is the one with the smaller start, as the problem asks.

#### 7. Time & Space Complexity — Must Know

Let `N` = total number of elements in all lists, `k` = number of lists.

| Part | Cost |
|---|---:|
| Each element is pushed and popped once | `O(N log k)` |
| Heap size | `O(k)` |
| **Total** | **Time `O(N log k)`, Space `O(k)`** |

#### 8. Common Range Variations — Must Know

1. **Smallest range covering `k` lists** (LeetCode 632) — this note.
2. **Smallest window in one array that contains all needed values** — sliding window with a `HashMap` (`03-leetcode-patterns`, topic 5).
3. **Largest range / longest consecutive run** (LeetCode 128, Longest Consecutive Sequence) — a `HashSet` solves it in `O(n)`. No heap is needed.
4. **Minimum difference between any two values from different lists** — the same heap idea, or sort and use two pointers.
5. **Smallest range after changes** — usually sorting and greedy. Do not force a heap.

#### 9. Edge Cases / Common Mistakes

1. Moving the wrong list. Only the list with the **minimum** moves.
2. Forgetting to update `currentMax` after pushing the next element.
3. Not stopping when a list is exhausted, and reading past the end.
4. Overflow in `max - min` when values are near `Int` limits. Use `Long`.
5. An empty list in the input. The problem usually promises none; check.
6. Using a max-heap. The minimum is the item that must be replaced.
7. Replacing the best range on ties with `<=`, which gives a larger start.

#### 10. When to Use / When Not to Use

**Use when:**

1. You have `k` sorted sources and need a range that touches all of them.

**Avoid when:**

1. There is a single array. A sliding window is simpler.
2. The task is about consecutive numbers. A `HashSet` is enough.

#### 11. Related Topics

1. K-Way Merge Pattern
2. Merge K Sorted Lists / Arrays
3. Sliding Window (`03-leetcode-patterns`)
4. Heap + HashMap Pattern

#### 12. Interview Must Remember

1. **Min-heap of one element per list, plus a `currentMax` variable.**
2. **Advance the list that owns the minimum.** Stop when it runs out.
3. `O(N log k)` time, `O(k)` space.
4. "Largest range" style problems (consecutive numbers) use a `HashSet`, not a heap.
