# Sorting-Based Array Problems

#### 1. What Is It?

Some problems become **easy after sorting**. Sorting puts related items next to each other, so one pass, two pointers, or a greedy choice can finish the job.

The price is `O(n log n)` time for the sort. The rest is usually `O(n)`.

Use it when the question is about **order, closeness, overlap, pairing or comparing neighbours**, and the **original positions do not matter**.

| Problem type | After sorting... |
|---|---|
| duplicates | equal items are neighbours |
| closest pair / smallest difference | the answer is between neighbours |
| intervals / meetings | overlaps are neighbours (note 15) |
| pairs for a target | two pointers (note 04) |
| greedy matching | match smallest with smallest |
| "arrange to form the biggest number" | sort with a custom comparison |

#### 2. How It Works

*Assign Cookies* (LeetCode 455): each child has a greed `g[i]`, each cookie has a size `s[j]`. A child is happy if `s[j] >= g[i]`. Maximise happy children.

```text
g = [1, 2, 3]   s = [1, 1]
sort both (already sorted)
cookie 1 → child 1 (1 ≥ 1) ✓
cookie 1 → child 2 (1 < 2) ✗ → try the next cookie (none)
answer 1
```

Greedy idea: give the **smallest cookie that satisfies** the least greedy child. Sorting makes this a two-pointer scan.

*Array Partition* (LeetCode 561): pair up numbers to maximise the sum of the minimums of the pairs. Sort, then pair neighbours. The answer is the sum of every second number.

*Largest Number* (LeetCode 179): arrange numbers to form the largest number. Sort with the rule "`a` before `b` if `ab > ba`" (as text).

```text
[3, 30, 34, 5, 9]  →  compare "330" vs "303": 330 is bigger, so 3 comes before 30.
sorted: 9, 5, 34, 3, 30  →  "9534330"
```

#### 3. Brute Force vs Optimized

| | Brute force | After sorting |
|---|---|---|
| Idea | compare every pair / try every arrangement | sort, then one pass |
| Time | `O(n²)` or worse | `O(n log n)` |
| Space | `O(1)` | `O(1)` to `O(n)` (depends on the sort) |

```kotlin
fun containsDuplicateBrute(nums: IntArray): Boolean {
    for (i in nums.indices) for (j in i + 1 until nums.size) if (nums[i] == nums[j]) return true
    return false
}

fun containsDuplicateSorted(nums: IntArray): Boolean {
    val sorted = nums.sortedArray()
    for (i in 1 until sorted.size) if (sorted[i] == sorted[i - 1]) return true
    return false
}
```

#### 4. Kotlin Code

```kotlin
// Assign Cookies (LeetCode 455)
fun findContentChildren(g: IntArray, s: IntArray): Int {
    g.sort(); s.sort()
    var child = 0
    for (cookie in s) {
        if (child < g.size && cookie >= g[child]) child++     // this cookie satisfies this child
    }
    return child
}

// Array Partition (LeetCode 561)
fun arrayPairSum(nums: IntArray): Int {
    nums.sort()
    var sum = 0
    for (i in nums.indices step 2) sum += nums[i]             // the smaller of each neighbour pair
    return sum
}

// Largest Number (LeetCode 179)
fun largestNumber(nums: IntArray): String {
    val strs = nums.map { it.toString() }
        .sortedWith { a, b -> (b + a).compareTo(a + b) }      // "ba" vs "ab": bigger first
    return if (strs[0] == "0") "0" else strs.joinToString("")
}

// Largest Perimeter Triangle (LeetCode 976): sort, check the biggest sides first
fun largestPerimeter(nums: IntArray): Int {
    nums.sort()
    for (i in nums.size - 1 downTo 2) {
        if (nums[i - 2] + nums[i - 1] > nums[i]) return nums[i - 2] + nums[i - 1] + nums[i]
    }
    return 0
}

// Sort by a rule: array of pairs sorted by the second value
val pairs = arrayOf(intArrayOf(1, 5), intArrayOf(2, 3), intArrayOf(3, 4))
pairs.sortBy { it[1] }                                         // [[2,3],[3,4],[1,5]]
```

Checks: `findContentChildren([1,2,3], [1,1])` → `1`. `arrayPairSum([1,4,3,2])` → `4`. `largestNumber([3,30,34,5,9])` → `"9534330"`. `largestPerimeter([2,1,2])` → `5`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Sort + one pass | `O(n log n)` | `O(1)`–`O(n)` |
| Counting sort (small value range) | `O(n + range)` | `O(range)` |

#### 6. Common Mistakes

1. **Sorting when positions matter** (Two Sum returns indexes). You lose the indexes.
2. **Sorting `IntArray` in place** when the caller needs the original order. Use `sortedArray()` or copy first.
3. **Comparator overflow:** `a - b` can overflow for big numbers. Use `compareTo`.
4. **Largest Number:** comparing the numbers instead of the joined strings, and the all-zeros case (`"000"` → `"0"`).
5. **Forgetting duplicates.**

#### 7. Say This in the Interview

1. "Order does not matter here, so I will sort first. That costs `O(n log n)` and makes the rest a single pass."
2. "Sorting loses the original indexes, so I would not use it for Two Sum with indexes."

#### 8. Quick Check

1. What is the total time of sort + one linear scan?
2. Why is `a - b` risky in a comparator?

<details>
<summary>Answers</summary>

1. `O(n log n)` (the sort dominates).
2. It can overflow for very large or very small `Int` values, giving a wrong order. Use `compareTo`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) (Easy) | greedy + sort |
| 561 | [Array Partition](https://leetcode.com/problems/array-partition/) (Easy) | pair neighbours |
| 976 | [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/) (Easy) | sort, check the largest |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) | sort by start |
| 179 | [Largest Number](https://leetcode.com/problems/largest-number/) (Medium) | custom comparator |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) (Medium) | sort + two pointers |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) (Medium) | avoid a full sort (note 20) |
