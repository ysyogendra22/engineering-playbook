# Largest Rectangle in Histogram

#### 1. Definition — Must Know

1. You are given bar heights of a histogram (each bar has width 1). Find the **area of the largest rectangle** that fits inside the bars.
2. A rectangle is limited by the **shortest bar** it covers.
3. It is *Largest Rectangle in Histogram* (LeetCode 84). If a number and a title ever disagree, trust the title.
4. The method: for each bar, find how far it can extend **left and right** before meeting a shorter bar. A monotonic stack finds both limits in `O(n)`.

#### 2. Why It Is Used — Must Know

1. It is the hardest "classic" monotonic stack question and a frequent hard-level interview problem.
2. It is the building block for *Maximal Rectangle* (LeetCode 85).
3. It teaches the idea of treating **each element as the minimum** of a range.

#### 3. How It Works — Must Know

`heights = [2, 1, 5, 6, 2, 3]`

```text
        6
      5 █
      █ █     3
      █ █ 2   █
  2   █ █ █   █
  █ 1 █ █ █   █
  █ █ █ █ █ █
```

For bar `5` (index 2): it can extend right through `6` (height ≥ 5) and stops at `2`; it can extend left until `1`. So its range is indexes 2–3 (width 2). Area = `5 × 2 = 10`. This is the answer.

Keep a stack of indexes with **increasing heights**. When a bar is **shorter than the top**, the top bar cannot extend further right, so pop it and compute its area:

```text
height = heights[popped]
right boundary = i (the shorter bar that stopped it)
left boundary  = the new top of the stack (the previous shorter bar), or -1 if the stack is empty
width = i - left - 1
area = height × width
```

Walk through:

```text
i=0 (2): push 0                                     stack: [0]
i=1 (1): 2 > 1 → pop 0: h=2, left=-1 (empty), width=1-(-1)-1=1, area 2
         push 1                                     stack: [1]
i=2 (5): push 2                                     [1, 2]
i=3 (6): push 3                                     [1, 2, 3]
i=4 (2): pop 3: h=6, left=2, width=4-2-1=1, area 6
         pop 2: h=5, left=1, width=4-1-1=2, area 10  ← best
         top is 1 (height 1 <= 2) → stop, push 4    [1, 4]
i=5 (3): push 5                                     [1, 4, 5]
i=6 (end, height 0 sentinel):
         pop 5: h=3, left=4, width=6-4-1=1, area 3
         pop 4: h=2, left=1, width=6-1-1=4, area 8
         pop 1: h=1, left=-1, width=6-(-1)-1=6, area 6

best = 10
```

The trailing **height 0 sentinel** forces everything left in the stack to be popped and counted.

#### 4. Core Concepts — Must Know

1. **Each bar is the shortest bar of some rectangle.** The best rectangle for it extends left and right until a shorter bar.
2. **Increasing stack of indexes.** A shorter incoming bar pops the taller ones, because they can no longer extend to the right.
3. **Right boundary** = the index `i` that caused the pop (next shorter).
4. **Left boundary** = the new stack top after the pop (previous shorter), or `-1` if the stack is empty.
5. **Width = `i - left - 1`.**
6. **Sentinel:** process one extra step with height `0` at `i = n`, so the stack empties.
7. **Equal heights:** popping on `>=` is safe. The last equal bar computes the widest rectangle.
8. **Area can be large:** `height × width` may exceed `Int` for very large inputs. Use `Long` if limits are big.

#### 5. Algorithm — Must Know

```text
best = 0; stack = empty
for i in 0..n:                         // include i = n with height 0
    h = (i == n) ? 0 : heights[i]
    while stack not empty and heights[stack.top] >= h:
        height = heights[stack.pop()]
        left = stack empty ? -1 : stack.top
        width = i - left - 1
        best = max(best, height * width)
    stack.push(i)
return best
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun largestRectangleArea(heights: IntArray): Int {
    val stack = ArrayDeque<Int>()                         // indexes, heights increasing
    var best = 0
    for (i in 0..heights.size) {
        val h = if (i == heights.size) 0 else heights[i]   // sentinel at the end
        while (stack.isNotEmpty() && heights[stack.last()] >= h) {
            val height = heights[stack.removeLast()]
            val left = if (stack.isEmpty()) -1 else stack.last()
            val width = i - left - 1
            best = maxOf(best, height * width)
        }
        stack.addLast(i)
    }
    return best
}

// Same idea, two passes with precomputed boundaries (easier to reason about)
fun largestRectangleTwoPass(heights: IntArray): Int {
    val n = heights.size
    val left = IntArray(n) { -1 }        // previous smaller index
    val right = IntArray(n) { n }        // next smaller index
    val stack = ArrayDeque<Int>()
    for (i in 0 until n) {
        while (stack.isNotEmpty() && heights[stack.last()] >= heights[i]) {
            right[stack.removeLast()] = i
        }
        left[i] = if (stack.isEmpty()) -1 else stack.last()
        stack.addLast(i)
    }
    var best = 0
    for (i in 0 until n) best = maxOf(best, heights[i] * (right[i] - left[i] - 1))
    return best
}
```

Checks: `largestRectangleArea([2,1,5,6,2,3])` → `10`. `largestRectangleArea([2,4])` → `4`. `largestRectangleArea([2,2])` → `4`. `largestRectangleArea([])` → `0`.

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Brute force (expand from every bar) | `O(n²)` | `O(1)` |
| Divide and conquer (split at the minimum) | `O(n log n)` average | `O(log n)` |
| **Monotonic stack** | **`O(n)`** | `O(n)` |

#### 8. Common Histogram Patterns — Must Know

1. **Largest Rectangle in Histogram** (LeetCode 84).
2. **Maximal Rectangle** (LeetCode 85) — run this per row of a binary matrix.
3. **Maximal Square** (LeetCode 221) — usually DP.
4. **Trapping Rain Water** (LeetCode 42) — related shape, different goal.
5. **Sum of Subarray Minimums** (LeetCode 907) — same boundaries, different formula.
6. **Largest rectangle in a skyline** or UI layout problems.
7. **Android example:** the largest free horizontal block in a bar-chart style layout.

#### 9. Edge Cases / Common Mistakes

1. Forgetting the **sentinel** (the final height `0` step), so the bars left in the stack are never counted.
2. Wrong width: it is `i - left - 1`, not `i - left`.
3. Using the popped index itself as the left boundary. Use the **new top** after popping.
4. Forgetting `left = -1` when the stack becomes empty.
5. Popping on `>` vs `>=` inconsistently. Both give correct answers when widths are computed as above.
6. Empty array → `0`.
7. `Int` overflow for huge heights × widths (use `Long`).
8. Computing the area before popping (using the wrong stack top).

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the largest area bounded by the shortest bar in a range.

**Avoid when:**

1. The shape is not a histogram. Convert it to one first (row heights in Maximal Rectangle).

#### 11. Related Topics

1. Monotonic Stack
2. Next Smaller Element
3. Previous Greater / Smaller Element
4. Maximal Rectangle

#### 12. Interview Must Remember

1. **Increasing stack of indexes. On a shorter bar, pop and compute `height × (i − newTop − 1)`.**
2. **Add a sentinel `0` height at the end.**
3. Left bound = new top (or `-1`); right bound = the current index.
4. `O(n)` time and space.
