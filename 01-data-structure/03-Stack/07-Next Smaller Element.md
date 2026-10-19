# Next Smaller Element

#### 1. Definition — Must Know

1. For each item, the **next smaller element** is the **first smaller value to its right**. If there is none, the answer is `-1`.
2. Example: `[4, 5, 2, 10, 8]` → `[2, 2, -1, 8, -1]`.
3. The method: an **increasing monotonic stack** of indexes (bottom to top: small → big).
4. It is the mirror of Next Greater Element: flip the comparison.

#### 2. Why It Is Used — Must Know

1. It gives boundaries for areas and spans (Largest Rectangle in Histogram).
2. It solves "find the discount / the next cheaper item" style questions.
3. It is `O(n)` instead of `O(n²)`.

#### 3. How It Works — Must Know

`nums = [4, 5, 2, 10, 8]`

```text
i=0 (4):  push 0                                  stack values: [4]
i=1 (5):  5 > 4 → push                            stack: [4, 5]
i=2 (2):  top 5 > 2 → pop idx1: answer 2
          top 4 > 2 → pop idx0: answer 2          stack: []   then push idx2: [2]
i=3 (10): 10 > 2 → push                           stack: [2, 10]
i=4 (8):  top 10 > 8 → pop idx3: answer 8         stack: [2]  then push idx4: [2, 8]

Left: idx2 (2) and idx4 (8) → -1

result: [2, 2, -1, 8, -1]
```

Rule: **while the top is bigger than the new item, pop it; the new item is its next smaller element.**

#### 4. Core Concepts — Must Know

1. **Increasing stack of indexes.**
2. **Pop while `nums[top] > nums[i]`** (strictly smaller). Use `>=` for "smaller or equal".
3. **Same cost and structure** as Next Greater: only the comparison changes.
4. **Real use — "final price after a discount":** the discount for item `i` is the first later price that is smaller or equal. So use `>=` when popping.
5. **Previous smaller** is found in the same loop: after popping, the top (if any) is the previous smaller item.
6. **Both sides at once:** when an index is popped, the new item is its **next smaller**, and the item just below it in the stack is its **previous smaller**. This is how histogram widths are found.

| Task | Pop while | Answer |
|---|---|---|
| Next smaller (strict) | `nums[top] > nums[i]` | `nums[i]` |
| Next smaller or equal | `nums[top] >= nums[i]` | `nums[i]` |
| Previous smaller (strict) | `nums[top] >= nums[i]` | `nums[top]` after popping |

#### 5. Algorithm — Must Know

```text
result = all -1; stack = empty
for i in 0 until n:
    while stack not empty and nums[stack.top] > nums[i]:
        result[stack.pop()] = nums[i]
    stack.push(i)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Next Smaller Element (value), -1 if none
fun nextSmallerElements(nums: IntArray): IntArray {
    val result = IntArray(nums.size) { -1 }
    val stack = ArrayDeque<Int>()                         // indexes, values increasing
    for (i in nums.indices) {
        while (stack.isNotEmpty() && nums[stack.last()] > nums[i]) {
            result[stack.removeLast()] = nums[i]
        }
        stack.addLast(i)
    }
    return result
}

// Next Smaller index (n if none) — useful for widths
fun nextSmallerIndex(nums: IntArray): IntArray {
    val n = nums.size
    val result = IntArray(n) { n }
    val stack = ArrayDeque<Int>()
    for (i in 0 until n) {
        while (stack.isNotEmpty() && nums[stack.last()] > nums[i]) {
            result[stack.removeLast()] = i
        }
        stack.addLast(i)
    }
    return result
}

// Final Prices With a Special Discount in a Shop (LeetCode 1475)
fun finalPrices(prices: IntArray): IntArray {
    val result = prices.copyOf()
    val stack = ArrayDeque<Int>()
    for (i in prices.indices) {
        while (stack.isNotEmpty() && prices[stack.last()] >= prices[i]) {
            result[stack.removeLast()] -= prices[i]       // discount = first later price <= this price
        }
        stack.addLast(i)
    }
    return result
}
```

Checks: `nextSmallerElements([4,5,2,10,8])` → `[2,2,-1,8,-1]`. `finalPrices([8,4,6,2,3])` → `[4,2,4,2,3]`.

#### 7. Time & Space Complexity — Must Know

| Version | Time | Space |
|---|---:|---:|
| Brute force | `O(n²)` | `O(1)` |
| **Monotonic stack** | **`O(n)`** | `O(n)` |

#### 8. Common Next-Smaller Patterns — Must Know

1. **Final Prices With a Special Discount** (LeetCode 1475).
2. **Largest Rectangle in Histogram** (LeetCode 84) — next and previous smaller bars.
3. **Sum of Subarray Minimums** (LeetCode 907) — spans from previous/next smaller.
4. **Remove K Digits** (LeetCode 402) — a stack that removes bigger digits before a smaller one.
5. **Online Stock Span** — previous greater (mirror problem).
6. **Smallest subsequence problems** (LeetCode 316, 1081) — increasing stack with extra rules.
7. **Android example:** for each price in a list, find the next cheaper price.

#### 9. Edge Cases / Common Mistakes

1. Using `<` when the problem needs "smaller or equal" (or the other way round).
2. Mixing up with Next Greater (flipped sign).
3. Forgetting the default (`-1` for values, `n` for indexes).
4. `stack.last()` on an empty stack inside the `while`.
5. Modifying `prices` in place while still reading it (use a copy, as above).
6. Ties creating wrong widths in area problems. Be consistent: strict on one side, non-strict on the other.
7. Assuming left-to-right gives the *previous* smaller directly. Read the top **after** popping.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the nearest smaller value on one side, for every item.

**Avoid when:**

1. You need the minimum of a sliding window (monotonic queue).
2. You need the smallest value in the whole array (just `min()`).

#### 11. Related Topics

1. Monotonic Stack
2. Next Greater Element
3. Previous Greater / Smaller Element
4. Largest Rectangle in Histogram

#### 12. Interview Must Remember

1. **Increasing stack of indexes. Pop while `top > current`.**
2. Same code as Next Greater with the comparison flipped.
3. Final-prices style questions use `>=` when popping.
4. `O(n)` time and space.
