# Two Pointers

> One of the most asked array patterns. It often turns `O(n²)` into `O(n)`.

#### 1. What Is It?

**Two pointers** means using **two indexes** that move through the array, instead of one. Because both move in a smart way, you avoid checking every pair.

Three common shapes:

| Shape | Pointers | Used for |
|---|---|---|
| **Opposite ends** | `left` starts at 0, `right` starts at `n - 1`, they move toward each other | sorted array pair sum, palindrome, container with most water |
| **Same direction** (read / write) | a fast pointer reads, a slow pointer writes | remove duplicates, move zeroes (in-place, note 12) |
| **Two arrays** | one pointer in each | merge sorted arrays, intersection |

How to spot it: the array is **sorted** (or can be sorted), you need a **pair/triple** with a property, or you must rewrite the array **in place**.

#### 2. How It Works

*Two Sum II* (LeetCode 167): a **sorted** array, find two numbers that add to `target`.

`nums = [1, 3, 4, 6, 9]`, `target = 10`

```text
l=0 (1), r=4 (9): sum 10 → found!

Another try, target = 7:
l=0 (1), r=4 (9): sum 10 > 7 → too big → move r left
l=0 (1), r=3 (6): sum 7  → found (1 + 6)
```

The rule: **if the sum is too small, move `left` right (a bigger number). If it is too big, move `right` left (a smaller number).** Each step removes one candidate for good, so the total is `O(n)`.

#### 3. Brute Force vs Optimized

| | Brute force | Two pointers |
|---|---|---|
| Idea | check every pair | move the ends toward each other |
| Time | `O(n²)` | `O(n)` (after sorting if needed) |
| Space | `O(1)` | `O(1)` |

```kotlin
fun twoSumSortedBrute(nums: IntArray, target: Int): IntArray {
    for (i in nums.indices) for (j in i + 1 until nums.size) {
        if (nums[i] + nums[j] == target) return intArrayOf(i, j)
    }
    return intArrayOf()
}
```

#### 4. Kotlin Code

```kotlin
// Two Sum II (sorted array), returns the indexes
fun twoSumSorted(nums: IntArray, target: Int): IntArray {
    var l = 0
    var r = nums.size - 1
    while (l < r) {
        val sum = nums[l] + nums[r]
        when {
            sum == target -> return intArrayOf(l, r)
            sum < target -> l++
            else -> r--
        }
    }
    return intArrayOf()
}

// Valid Palindrome (LeetCode 125): compare from both ends, ignore non-letters
fun isPalindrome(s: String): Boolean {
    var l = 0
    var r = s.length - 1
    while (l < r) {
        if (!s[l].isLetterOrDigit()) { l++; continue }
        if (!s[r].isLetterOrDigit()) { r--; continue }
        if (s[l].lowercaseChar() != s[r].lowercaseChar()) return false
        l++; r--
    }
    return true
}

// Container With Most Water (LeetCode 11): always move the shorter wall
fun maxArea(height: IntArray): Int {
    var l = 0
    var r = height.size - 1
    var best = 0
    while (l < r) {
        best = maxOf(best, minOf(height[l], height[r]) * (r - l))
        if (height[l] < height[r]) l++ else r--       // a taller wall is the only way to get more area
    }
    return best
}

// 3Sum (LeetCode 15): sort, fix one number, two pointers for the other two
fun threeSum(nums: IntArray): List<List<Int>> {
    nums.sort()
    val result = mutableListOf<List<Int>>()
    for (i in 0 until nums.size - 2) {
        if (i > 0 && nums[i] == nums[i - 1]) continue             // skip repeated first numbers
        var l = i + 1
        var r = nums.size - 1
        while (l < r) {
            val sum = nums[i] + nums[l] + nums[r]
            when {
                sum < 0 -> l++
                sum > 0 -> r--
                else -> {
                    result.add(listOf(nums[i], nums[l], nums[r]))
                    l++; r--
                    while (l < r && nums[l] == nums[l - 1]) l++   // skip repeats
                    while (l < r && nums[r] == nums[r + 1]) r--
                }
            }
        }
    }
    return result
}
```

Checks: `twoSumSorted([1,3,4,6,9], 10)` → `[0, 4]`. `maxArea([1,8,6,2,5,4,8,3,7])` → `49`. `threeSum([-1,0,1,2,-1,-4])` → `[[-1,-1,2],[-1,0,1]]`.

#### 5. Complexity

| Problem | Time | Space |
|---|---|---|
| Pair in a sorted array | `O(n)` | `O(1)` |
| Container With Most Water | `O(n)` | `O(1)` |
| 3Sum | `O(n²)` (sort `O(n log n)` + a loop of two pointers) | `O(1)` extra |

#### 6. Common Mistakes

1. **Using it on an unsorted array** (for pair sums) without sorting. Sorting also loses the original indexes.
2. **Moving the wrong pointer.** Think: which move can improve the result?
3. **`while (l <= r)` instead of `l < r`** when you need two different items.
4. **3Sum: not skipping duplicates**, which gives repeated triples.
5. **Infinite loop** because a pointer never moves.
6. **Overflow** when adding large numbers. Use `Long` if needed.

#### 7. Say This in the Interview

1. "The array is sorted, so I use two pointers from both ends. If the sum is too small I move left forward, otherwise I move right back."
2. "Each pointer only moves one way, so it is `O(n)` time and `O(1)` space."
3. "For an unsorted array I would use a HashMap, or sort first if indexes are not needed."

#### 8. Quick Check

1. In Two Sum II, the sum is too big. Which pointer moves?
2. Why is the container's shorter wall the one to move?

<details>
<summary>Answers</summary>

1. The right pointer moves left (to a smaller number).
2. The area is limited by the shorter wall. Moving the taller wall can only make the width smaller without a better height.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Easy) | both ends |
| 977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) (Easy) | fill from the biggest |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) (Easy) | read / write pointers |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (Medium) | opposite ends |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Medium) | move the shorter wall |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) (Medium) | sort + two pointers |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) (Medium) | three pointers (note 20) |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) | two pointers with max heights |
