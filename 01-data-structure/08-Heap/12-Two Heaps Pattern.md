# Two Heaps Pattern

#### 1. Definition — Must Know

1. The **Two Heaps** pattern splits data into two halves and keeps each half in its own heap:
   - a **max-heap** for the **lower half** (smaller values),
   - a **min-heap** for the **upper half** (larger values).
2. The tops of the two heaps are the two **middle** values.
3. It gives the median, or any "middle of the data" value, in `O(1)`, even while data keeps arriving.

#### 2. Why It Is Used — Must Know

1. Finding the median of changing data by sorting each time costs `O(n log n)` per query. Two heaps cost `O(log n)` per insert and `O(1)` per query.
2. A single heap only exposes one end of the data. Two heaps expose both sides of the middle.
3. It is the standard answer to *Find Median from Data Stream*.

#### 3. How It Works — Must Know

Data `1, 2, 3, 4, 5, 6`:

```text
 lower half (max-heap)        upper half (min-heap)
      [ 1, 2, 3 ]                  [ 4, 5, 6 ]
   top = 3 (largest of low)     top = 4 (smallest of high)

 median = (3 + 4) / 2 = 3.5
```

With an odd count, let the lower heap hold one extra item. Its top is the median:

```text
 low  = [ 1, 2, 3 ]     high = [ 4, 5 ]
 median = 3
```

#### 4. Core Concepts — Must Know

Two rules (**invariants**) must hold after every insert:

1. **Order rule:** every value in the lower half is `≤` every value in the upper half.
2. **Size rule:** the sizes differ by at most one. By convention `low.size == high.size` or `low.size == high.size + 1`.

Reading the answer:

| Count | Median |
|---|---|
| Odd | top of the larger heap (the lower heap) |
| Even | average of the two tops |

#### 5. Algorithm — Must Know

```text
addNum(x):
    low.add(x)                       // 1. put in the lower half
    high.add(low.poll())             // 2. move the largest of the lower half to the upper half
    if high.size > low.size:         // 3. keep sizes balanced
        low.add(high.poll())
```

Why this works:

```text
Step 1+2 pass every new value through low, so the value that moves to high is the largest of low.
That keeps "everything in low ≤ everything in high".
Step 3 restores the size rule.
```

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

class TwoHeaps {

    private val low = PriorityQueue<Int>(compareByDescending<Int> { it })   // max-heap
    private val high = PriorityQueue<Int>()                                  // min-heap

    fun add(x: Int) {
        low.add(x)
        high.add(low.poll())
        if (high.size > low.size) low.add(high.poll())
    }

    fun median(): Double {
        require(low.isNotEmpty()) { "no data" }
        return if (low.size > high.size) low.peek().toDouble()
        else (low.peek().toDouble() + high.peek().toDouble()) / 2.0
    }
}
```

`toDouble()` first, so two large `Int` values do not overflow when added.

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| Add a number | `O(log n)` |
| Read the median | `O(1)` |
| Space | `O(n)` |

#### 8. Common Two Heaps Patterns — Must Know

1. **Find Median from Data Stream** (LeetCode 295) — see the next topic.
2. **Sliding Window Median** (LeetCode 480) — two heaps with lazy deletion (see "Multiple Heap / Advanced Two-Heaps Patterns").
3. **IPO** (LeetCode 502) — two heaps with different orders, one to unlock projects and one to choose the best (see the same topic).
4. A "balance" pattern: split into the smaller half and the larger half to look at the middle.

#### 9. Edge Cases / Common Mistakes

1. Putting the max-heap and min-heap the wrong way round.
2. Breaking the size rule so the median reads the wrong top.
3. Reading `peek()` on an empty heap when only one number exists.
4. Integer overflow when averaging two large `Int` values. Convert to `Double` first.
5. Inserting directly into the "right" heap by comparing with the tops, and mishandling the balance. The three-step rule above avoids this.
6. Even count: forgetting to average the two tops.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the median or a middle value while data changes.
2. You need the "smaller half" and "larger half" separately.

**Avoid when:**

1. The data is fixed. Sort once and index the middle.
2. The values are in a small, known range. A counting array is simpler.

#### 11. Related Topics

1. Min Heap vs Max Heap
2. Find Median from Data Stream
3. Multiple Heap / Advanced Two-Heaps Patterns
4. Sliding Window (`03-leetcode-patterns`, topic 5)

#### 12. Interview Must Remember

1. **Max-heap for the lower half, min-heap for the upper half.**
2. Keep sizes equal, or the lower half one larger.
3. Add: `low → high → rebalance`. Median is read from the tops in `O(1)`.
4. Insert is `O(log n)`.
