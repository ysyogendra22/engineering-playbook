# Prefix / Suffix Pattern

#### 1. What Is It?

Sometimes the answer for index `i` depends on **everything to its left** and **everything to its right**. Compute one array from the left (**prefix**) and one from the right (**suffix**), then combine them.

```text
nums   = [1, 2, 3, 4]
prefix = product of everything LEFT of i  → [1, 1, 2, 6]
suffix = product of everything RIGHT of i → [24, 12, 4, 1]
answer[i] = prefix[i] × suffix[i]         → [24, 12, 8, 6]
```

This is *Product of Array Except Self* (LeetCode 238): no division allowed, and zeros are possible, so the prefix/suffix idea is the way.

How to spot it: "for each element, use all the elements before and after it", "except self", "max to the left and right" (trapping rain water).

#### 2. How It Works

Two passes:

```text
1. Left to right: result[i] = product of all items before i        (result[0] = 1)
2. Right to left: multiply result[i] by the product of all items after i
```

You can do this with `O(1)` extra space (not counting the output): keep a running product while scanning.

```text
nums = [1, 2, 3, 4]

pass 1 (left):   result = [1, 1, 2, 6]       running product of the left: 1, 1, 2, 6
pass 2 (right):  right = 1
   i=3: result[3] = 6 × 1 = 6    right = 1 × 4 = 4
   i=2: result[2] = 2 × 4 = 8    right = 4 × 3 = 12
   i=1: result[1] = 1 × 12 = 12  right = 12 × 2 = 24
   i=0: result[0] = 1 × 24 = 24
result = [24, 12, 8, 6]
```

Another example, *Trapping Rain Water* (LeetCode 42): the water above bar `i` is `min(maxLeft[i], maxRight[i]) - height[i]`. `maxLeft` is a prefix maximum and `maxRight` is a suffix maximum.

#### 3. Brute Force vs Optimized

| | Brute force | Prefix + suffix |
|---|---|---|
| Idea | for each `i`, multiply all other items | combine left and right running products |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` extra | `O(1)` extra (output excluded) |
| Note | | no division, so zeros are fine |

```kotlin
fun productExceptSelfBrute(nums: IntArray): IntArray =
    IntArray(nums.size) { i ->
        var product = 1
        for (j in nums.indices) if (j != i) product *= nums[j]
        product
    }
```

#### 4. Kotlin Code

```kotlin
// Product of Array Except Self (LeetCode 238)
fun productExceptSelf(nums: IntArray): IntArray {
    val n = nums.size
    val result = IntArray(n)
    result[0] = 1
    for (i in 1 until n) result[i] = result[i - 1] * nums[i - 1]     // product of everything on the left

    var right = 1
    for (i in n - 1 downTo 0) {
        result[i] *= right                                             // times the product on the right
        right *= nums[i]
    }
    return result
}

// Trapping Rain Water (LeetCode 42) with prefix and suffix maximums
fun trap(height: IntArray): Int {
    val n = height.size
    if (n == 0) return 0
    val maxLeft = IntArray(n)
    val maxRight = IntArray(n)
    maxLeft[0] = height[0]
    for (i in 1 until n) maxLeft[i] = maxOf(maxLeft[i - 1], height[i])
    maxRight[n - 1] = height[n - 1]
    for (i in n - 2 downTo 0) maxRight[i] = maxOf(maxRight[i + 1], height[i])

    var water = 0
    for (i in 0 until n) water += minOf(maxLeft[i], maxRight[i]) - height[i]
    return water
}

// Find Pivot Index with the same idea: left sum vs right sum
fun pivotIndex(nums: IntArray): Int {
    val total = nums.sum()
    var left = 0
    for (i in nums.indices) {
        if (left == total - left - nums[i]) return i
        left += nums[i]
    }
    return -1
}

// Candy (LeetCode 135): two passes, left rule and right rule
fun candy(ratings: IntArray): Int {
    val n = ratings.size
    val candies = IntArray(n) { 1 }
    for (i in 1 until n) if (ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1      // left to right
    for (i in n - 2 downTo 0) if (ratings[i] > ratings[i + 1]) candies[i] = maxOf(candies[i], candies[i + 1] + 1)
    return candies.sum()
}
```

Checks: `productExceptSelf([1,2,3,4])` → `[24,12,8,6]`. `productExceptSelf([-1,1,0,-3,3])` → `[0,0,9,0,0]`. `trap([0,1,0,2,1,0,1,3,2,1,2,1])` → `6`. `candy([1,0,2])` → `5`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Product except self | `O(n)` | `O(1)` extra |
| Trapping Rain Water (arrays) | `O(n)` | `O(n)` |
| Trapping Rain Water (two pointers) | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Using division** (fails when there is a zero).
2. **Off-by-one in the first item** (the left product of index 0 is `1`).
3. **Updating `right` before using it.** Multiply first, then update.
4. **Overflow in products.** Use `Long` if needed.
5. **Candy:** a single pass is not enough. You need both directions.

#### 7. Say This in the Interview

1. "For each index I need everything on its left and its right. I compute left products in one pass and right products in another, so it is `O(n)` and I avoid division."
2. "I reuse the output array for the left products, so extra space is `O(1)`."

#### 8. Quick Check

1. What is the left product of the first item?
2. Why is division a bad idea for Product Except Self?

<details>
<summary>Answers</summary>

1. `1` (the empty product).
2. A zero in the array makes division impossible or wrong.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) (Easy) | left sum vs right sum |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) | prefix × suffix |
| 2256 | [Minimum Average Difference](https://leetcode.com/problems/minimum-average-difference/) (Medium) | prefix sum from both sides |
| 135 | [Candy](https://leetcode.com/problems/candy/) (Hard) | two passes |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) | prefix and suffix maximums |
