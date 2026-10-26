# Largest Rectangle in Histogram

> A famous Hard question. It is also the base of "Maximal Rectangle". Take your time with the trace.

#### 1. What Is It?

You get the heights of bars in a histogram. Every bar is 1 wide. Find the **area of the biggest rectangle** that fits inside the bars.

```text
heights = [2, 1, 5, 6, 2, 3]

        6
      5 █
      █ █     3
      █ █ 2   █
  2   █ █ █   █
  █ 1 █ █ █   █
  █ █ █ █ █ █

Biggest rectangle: the bars 5 and 6, height 5, width 2 → area 10
```

A rectangle is limited by its **shortest bar**. So for each bar, ask: **how far can this bar stretch to the left and to the right before it meets a shorter bar?** Then `area = height × width`.

A monotonic stack finds both limits in one pass.

#### 2. How It Works

Keep a stack of indexes with **increasing heights**. When a bar is **shorter than the top**, the top bar cannot stretch any further right. Pop it and compute its area:

- **height** = height of the popped bar
- **right limit** = the current index `i` (the shorter bar that stopped it)
- **left limit** = the new top of the stack after popping (or `-1` if the stack is empty)
- **width** = `i - left - 1`

At the end, add an extra bar of height `0` so all remaining bars get popped and counted.

```text
heights = [2, 1, 5, 6, 2, 3]

i=0 (2): push 0                                          stack: [0]
i=1 (1): 2 > 1 → pop 0: height 2, left = -1, width 1-(-1)-1 = 1, area 2
         push 1                                          stack: [1]
i=2 (5): push                                            stack: [1, 2]
i=3 (6): push                                            stack: [1, 2, 3]
i=4 (2): pop 3: height 6, left = 2, width 4-2-1 = 1, area 6
         pop 2: height 5, left = 1, width 4-1-1 = 2, area 10   ← best
         top is bar 1 (height 1) <= 2 → stop.  push 4    stack: [1, 4]
i=5 (3): push                                            stack: [1, 4, 5]
i=6 (end, height 0):
         pop 5: height 3, left = 4, width 6-4-1 = 1, area 3
         pop 4: height 2, left = 1, width 6-1-1 = 4, area 8
         pop 1: height 1, left = -1, width 6-(-1)-1 = 6, area 6

answer = 10
```

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea | for each bar, stretch left and right while bars are not shorter | increasing stack |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` | `O(n)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
fun largestRectangleBrute(heights: IntArray): Int {
    var best = 0
    for (i in heights.indices) {
        var left = i
        var right = i
        while (left > 0 && heights[left - 1] >= heights[i]) left--
        while (right < heights.size - 1 && heights[right + 1] >= heights[i]) right++
        best = maxOf(best, heights[i] * (right - left + 1))
    }
    return best
}
```

The stack finds the nearest shorter bar on both sides for every bar in a single pass.

#### 4. Kotlin Code

```kotlin
fun largestRectangleArea(heights: IntArray): Int {
    val stack = ArrayDeque<Int>()                            // indexes, heights increasing
    var best = 0
    for (i in 0..heights.size) {                             // note: goes one step past the end
        val h = if (i == heights.size) 0 else heights[i]     // extra bar of height 0
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
```

Checks: `[2,1,5,6,2,3]` → `10`. `[2,4]` → `4`. `[2,2]` → `4`. `[]` → `0`.

**Related problem — Trapping Rain Water (LeetCode 42).** Given bar heights, how much rain water is trapped between the bars? A stack solution: keep a stack of indexes with **decreasing** heights. When a taller bar arrives, the popped bar is the "bottom" of a pool. The new top is the left wall, the new bar is the right wall.

```kotlin
fun trap(height: IntArray): Int {
    val stack = ArrayDeque<Int>()
    var water = 0
    for (i in height.indices) {
        while (stack.isNotEmpty() && height[stack.last()] < height[i]) {
            val bottom = stack.removeLast()
            if (stack.isEmpty()) break                      // no left wall
            val left = stack.last()
            val depth = minOf(height[left], height[i]) - height[bottom]
            water += depth * (i - left - 1)
        }
        stack.addLast(i)
    }
    return water
}
// trap([0,1,0,2,1,0,1,3,2,1,2,1]) → 6
```

(Two pointers also solve this in `O(1)` space. Know both.)

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Monotonic stack | `O(n)` | `O(n)` |
| Brute force (expand from every bar) | `O(n²)` | `O(1)` |

#### 6. Common Mistakes

1. **Forgetting the extra bar of height 0** at the end. The bars left in the stack are never counted.
2. **Wrong width.** It is `i - left - 1`, not `i - left`.
3. **Using the popped index as the left limit.** Use the **new top** after popping.
4. **Forgetting `left = -1`** when the stack becomes empty.
5. **Computing the area before popping.**
6. **Overflow.** `height × width` can exceed `Int` for very large inputs. Use `Long` if the limits are big.

#### 7. Say This in the Interview

1. "A rectangle is limited by its shortest bar, so for each bar I need the nearest shorter bar on the left and on the right."
2. "I use an increasing stack. A shorter bar pops the taller ones and tells me their right limit. The new top is the left limit."
3. "I add a bar of height 0 at the end to flush the stack."
4. "Time `O(n)`, space `O(n)`."

#### 8. Quick Check

1. What is the answer for `[4]`?
2. In `[2, 4]`, what is the biggest rectangle?

<details>
<summary>Answers</summary>

1. `4` (height 4, width 1).
2. `4`. Either the bar of height 4 alone (area 4), or both bars at height 2 (area 4).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (Hard) | this note |
| 85 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) (Hard) | one histogram per row |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) | decreasing stack or two pointers |
| 907 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) (Medium) | same left and right limits |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (Medium) | easier warm-up for the same stack |
