# Find Median from Data Stream

#### 1. Definition — Must Know

1. Numbers arrive one at a time. After each one you may be asked for the **median** of all numbers so far.
2. Median:
   - odd count → the middle value,
   - even count → the average of the two middle values.
3. This is *Find Median from Data Stream* (LeetCode 295). If a number and a title ever disagree, trust the title.
4. The answer is the Two Heaps pattern.

#### 2. Why It Is Used — Must Know

1. It is the classic heap question, and a favourite at top companies.
2. It shows why keeping data sorted is too slow, and why two heaps are enough.
3. Medians are used in real monitoring: response times, scores, prices.

#### 3. How It Works — Must Know

Stream: `5, 2, 8, 1`. The lower half is a max-heap (`low`), the upper half is a min-heap (`high`).

```text
add 5:  low=[5]        high=[]       median = 5
add 2:  low=[2]        high=[5]      median = (2 + 5) / 2 = 3.5
add 8:  low=[5, 2]     high=[8]      median = 5
add 1:  low=[2, 1]     high=[5, 8]   median = (2 + 5) / 2 = 3.5

Check: sorted data is 1, 2, 5, 8 → median (2 + 5) / 2 = 3.5 ✓
```

Inside `add`, each number goes into `low`, its largest value moves to `high`, and `low` takes one back if `high` becomes larger.

#### 4. Core Concepts — Must Know

1. **Lower half** → max-heap. **Upper half** → min-heap.
2. **Invariants:** everything in `low` ≤ everything in `high`; `low.size` is equal to or one more than `high.size`.
3. **Median:** odd count → `low.peek()`. Even count → average of both tops.
4. **No sorting** of the whole stream is ever done.

Comparison:

| Method | Add | Median |
|---|---:|---:|
| Keep a list and sort for each query | `O(1)` | `O(n log n)` |
| Insert into a sorted list | `O(n)` | `O(1)` |
| **Two heaps** | **`O(log n)`** | **`O(1)`** |

#### 5. Algorithm — Must Know

```text
addNum(x):
    low.add(x)
    high.add(low.poll())
    if high.size > low.size: low.add(high.poll())

findMedian():
    if low.size > high.size: return low.peek()
    return (low.peek() + high.peek()) / 2
```

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

class MedianFinder {

    private val low = PriorityQueue<Int>(compareByDescending<Int> { it })   // max-heap
    private val high = PriorityQueue<Int>()                                  // min-heap

    fun addNum(num: Int) {
        low.add(num)
        high.add(low.poll())
        if (high.size > low.size) low.add(high.poll())
    }

    fun findMedian(): Double =
        if (low.size > high.size) low.peek().toDouble()
        else (low.peek().toDouble() + high.peek().toDouble()) / 2.0
}

// Usage
val finder = MedianFinder()
finder.addNum(5); finder.addNum(2)
println(finder.findMedian())   // 3.5
finder.addNum(8)
println(finder.findMedian())   // 5.0
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `addNum` | `O(log n)` |
| `findMedian` | `O(1)` |
| Space | `O(n)` |

#### 8. Common Follow-Ups — Must Know

1. **All numbers are between 0 and 100.** Keep a count for each value in an `IntArray(101)`. The median is found by walking the counts: `O(100)`, which is a constant.
2. **99% of numbers are between 0 and 100.** Use the counts for that range, plus a small separate structure for the rare outliers.
3. **Sliding Window Median** (LeetCode 480) — needs deletions (see "Multiple Heap / Advanced Two-Heaps Patterns").
4. **Median of two sorted arrays** (LeetCode 4) — a different problem, solved with binary search (`02-algorithm/02-searching`).

#### 9. Edge Cases / Common Mistakes

1. Calling `findMedian()` before any number is added (both heaps are empty).
2. Reading the wrong top when the counts are odd.
3. Averaging two `Int` values without converting to `Double`, which can overflow.
4. Forgetting to rebalance after the move.
5. Making the min-heap the lower half by mistake.
6. Returning an `Int` median for an even count, losing the `.5`.

#### 10. When to Use / When Not to Use

**Use when:**

1. The median is asked for repeatedly while data arrives.

**Avoid when:**

1. The data is fixed. Sort once.
2. Values are in a tiny range. Use counts.
3. You need removal of arbitrary old values. Use lazy deletion (see the advanced topic).

#### 11. Related Topics

1. Two Heaps Pattern
2. Min Heap vs Max Heap
3. Multiple Heap / Advanced Two-Heaps Patterns
4. Sorting (`02-algorithm/01-sorting`)

#### 12. Interview Must Remember

1. **Two heaps: max-heap (lower half), min-heap (upper half).**
2. Add in `O(log n)`, median in `O(1)`.
3. Odd count → top of the lower heap. Even count → average of the tops.
4. Know the follow-up: **small value range → counting array.**
