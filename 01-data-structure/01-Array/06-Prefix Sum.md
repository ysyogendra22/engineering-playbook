# Prefix Sum

> Learn this well. It is the base of many subarray questions and makes range queries `O(1)`.

#### 1. What Is It?

A **prefix sum** array stores the **running total** of the array:

```text
nums   = [3, 1, 4, 2, 5]
prefix = [0, 3, 4, 8, 10, 15]          prefix[i] = sum of the first i numbers
```

(We add a `0` at the front, so `prefix[0] = 0`. This avoids special cases.)

With it, the sum of **any range** is a subtraction:

```text
sum(left .. right) = prefix[right + 1] - prefix[left]
```

Why it is used: if a question asks for **many range sums**, a loop costs `O(n)` per query. With a prefix sum, each query is `O(1)` after one `O(n)` setup.

How to spot it: "sum of a range / subarray", "many queries", "equal left and right sums".

#### 2. How It Works

Sum of `nums[1..3]` (that is `1 + 4 + 2 = 7`):

```text
prefix[4] - prefix[1] = 10 - 3 = 7
```

Why it works: `prefix[4]` is the sum of the first 4 numbers (indexes 0–3). `prefix[1]` is the sum of the first 1 number (index 0). Subtracting leaves indexes 1–3.

Find Pivot Index (LeetCode 724): the index where the sum on the left equals the sum on the right.

```text
nums = [1, 7, 3, 6, 5, 6]     total = 28
at index 3 (value 6): left sum = 1+7+3 = 11, right sum = 28 - 11 - 6 = 11  → pivot is 3
```

You do not even need the whole array: keep a running `leftSum` and compute `rightSum = total - leftSum - nums[i]`.

#### 3. Brute Force vs Optimized

| | Brute force | Prefix sum |
|---|---|---|
| Each range query | loop over the range: `O(n)` | `O(1)` |
| Setup | none | `O(n)` once |
| `q` queries | `O(q · n)` | `O(n + q)` |
| Extra space | `O(1)` | `O(n)` |

```kotlin
fun rangeSumBrute(nums: IntArray, left: Int, right: Int): Int {
    var sum = 0
    for (i in left..right) sum += nums[i]
    return sum
}
```

#### 4. Kotlin Code

```kotlin
// Range Sum Query - Immutable (LeetCode 303)
class NumArray(nums: IntArray) {
    private val prefix = IntArray(nums.size + 1)

    init {
        for (i in nums.indices) prefix[i + 1] = prefix[i] + nums[i]
    }

    fun sumRange(left: Int, right: Int): Int = prefix[right + 1] - prefix[left]
}

// Running Sum of 1d Array (LeetCode 1480)
fun runningSum(nums: IntArray): IntArray {
    val result = nums.copyOf()
    for (i in 1 until result.size) result[i] += result[i - 1]
    return result
}

// Find Pivot Index (LeetCode 724): no extra array needed
fun pivotIndex(nums: IntArray): Int {
    val total = nums.sum()
    var leftSum = 0
    for (i in nums.indices) {
        val rightSum = total - leftSum - nums[i]
        if (leftSum == rightSum) return i
        leftSum += nums[i]
    }
    return -1
}
```

Checks: `NumArray([-2,0,3,-5,2,-1]).sumRange(0, 2)` → `1`, `sumRange(2, 5)` → `-1`. `runningSum([1,2,3,4])` → `[1,3,6,10]`. `pivotIndex([1,7,3,6,5,6])` → `3`.

Use `Long` for the sums if the values are large.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Build the prefix array | `O(n)` | `O(n)` |
| One range query | `O(1)` | `O(1)` |

#### 6. Common Mistakes

1. **Off-by-one:** with a leading `0`, the formula is `prefix[right + 1] - prefix[left]`.
2. **Forgetting the leading `0`.** Then `left = 0` needs a special case.
3. **`Int` overflow** on large sums.
4. **Using it when the array changes often.** Each update would force a rebuild. Use a Fenwick tree (advanced).
5. **Index out of bounds** when the prefix array has `n + 1` items.

#### 7. Say This in the Interview

1. "I will build a prefix sum array once in `O(n)`. Then each range sum is `prefix[r + 1] - prefix[l]`, which is `O(1)`."
2. "I use `Long` if the sums can overflow."

#### 8. Quick Check

1. For `nums = [2, 4, 6]`, what is the prefix array (with a leading 0)?
2. How do you get `nums[1] + nums[2]` from it?

<details>
<summary>Answers</summary>

1. `[0, 2, 6, 12]`.
2. `prefix[3] - prefix[1] = 12 - 2 = 10`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1480 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) (Easy) | the prefix array itself |
| 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) (Easy) | `O(1)` range sums |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) (Easy) | left sum = right sum |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) | prefix and suffix products (note 18) |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium) | prefix sum + map (note 26) |
| 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) (Medium) | prefix balance + map |
| 304 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) (Medium) | 2D prefix sum (note 25) |
