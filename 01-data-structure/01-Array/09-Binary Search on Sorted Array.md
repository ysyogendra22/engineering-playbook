# Binary Search on Sorted Array

> Asked everywhere. The idea is simple. The details (boundaries) are where people fail. The longer notes are in `02-algorithm/02-searching`.

#### 1. What Is It?

**Binary search** finds a value in a **sorted** array by **halving** the search range each step.

```text
Look at the middle item.
  equal to the target → found
  target is smaller   → search the left half
  target is bigger    → search the right half
```

Why it is fast: after `k` steps only `n / 2^k` items are left. So it needs about `log₂ n` steps (a million items: 20 steps).

How to spot it: the array is **sorted** (or rotated sorted, or monotonic in some way), and the question says "find", "first", "last", "insert position", or asks for `O(log n)`.

#### 2. How It Works

`nums = [1, 3, 5, 7, 9, 11]`, `target = 7`

```text
lo=0, hi=5   mid=2 (5)   5 < 7 → search right  → lo=3
lo=3, hi=5   mid=4 (9)   9 > 7 → search left   → hi=3
lo=3, hi=3   mid=3 (7)   found at index 3
```

Always compute the middle as `lo + (hi - lo) / 2`. The form `(lo + hi) / 2` can overflow for huge arrays.

Two common versions:

| Version | Loop | When |
|---|---|---|
| Find an exact value | `while (lo <= hi)` | classic search |
| Find a boundary (first item `>= target`) | `while (lo < hi)` with `hi = mid` | lower bound, insert position, first/last occurrence |

**Lower bound** = the first index whose value is `>= target`. With it you get insert position, first occurrence (`lowerBound(target)`) and last occurrence (`lowerBound(target + 1) - 1`).

#### 3. Brute Force vs Optimized

| | Linear scan | Binary search |
|---|---|---|
| Time | `O(n)` | `O(log n)` |
| Needs sorted data | no | **yes** |

```kotlin
fun searchBrute(nums: IntArray, target: Int): Int {
    for (i in nums.indices) if (nums[i] == target) return i
    return -1
}
```

#### 4. Kotlin Code

```kotlin
// Binary Search (LeetCode 704)
fun search(nums: IntArray, target: Int): Int {
    var lo = 0
    var hi = nums.size - 1
    while (lo <= hi) {
        val mid = lo + (hi - lo) / 2
        when {
            nums[mid] == target -> return mid
            nums[mid] < target -> lo = mid + 1
            else -> hi = mid - 1
        }
    }
    return -1
}

// Lower bound: the first index with nums[i] >= target (nums.size if there is none)
fun lowerBound(nums: IntArray, target: Int): Int {
    var lo = 0
    var hi = nums.size
    while (lo < hi) {
        val mid = lo + (hi - lo) / 2
        if (nums[mid] < target) lo = mid + 1 else hi = mid
    }
    return lo
}

// Search Insert Position (LeetCode 35)
fun searchInsert(nums: IntArray, target: Int): Int = lowerBound(nums, target)

// First and Last Position of a value (LeetCode 34)
fun searchRange(nums: IntArray, target: Int): IntArray {
    val first = lowerBound(nums, target)
    if (first == nums.size || nums[first] != target) return intArrayOf(-1, -1)
    val last = lowerBound(nums, target + 1) - 1
    return intArrayOf(first, last)
}

// Search in Rotated Sorted Array (LeetCode 33): one half is always sorted
fun searchRotated(nums: IntArray, target: Int): Int {
    var lo = 0
    var hi = nums.size - 1
    while (lo <= hi) {
        val mid = lo + (hi - lo) / 2
        if (nums[mid] == target) return mid
        if (nums[lo] <= nums[mid]) {                                   // the left half is sorted
            if (target >= nums[lo] && target < nums[mid]) hi = mid - 1 else lo = mid + 1
        } else {                                                       // the right half is sorted
            if (target > nums[mid] && target <= nums[hi]) lo = mid + 1 else hi = mid - 1
        }
    }
    return -1
}

// Find Minimum in Rotated Sorted Array (LeetCode 153)
fun findMin(nums: IntArray): Int {
    var lo = 0
    var hi = nums.size - 1
    while (lo < hi) {
        val mid = lo + (hi - lo) / 2
        if (nums[mid] > nums[hi]) lo = mid + 1 else hi = mid           // the minimum is on the unsorted side
    }
    return nums[lo]
}
```

Checks: `search([1,3,5,7,9,11], 7)` → `3`. `searchRange([5,7,7,8,8,10], 8)` → `[3, 4]`. `searchRotated([4,5,6,7,0,1,2], 0)` → `4`. `findMin([3,4,5,1,2])` → `1`.

Kotlin also has `nums.binarySearch(target)` (returns the index, or a negative number if missing).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Binary search | `O(log n)` | `O(1)` |
| Sorting first, then searching | `O(n log n)` | — |

#### 6. Common Mistakes

1. **Using it on an unsorted array.**
2. **Infinite loop** from wrong updates. With `lo <= hi` use `mid + 1` / `mid - 1`. With `lo < hi` use `hi = mid`.
3. **`(lo + hi) / 2` overflow.** Use `lo + (hi - lo) / 2`.
4. **Off-by-one on the boundaries** (`hi = n` vs `n - 1`).
5. **Forgetting duplicates** (use lower bound for the first one).
6. **Rotated array:** deciding which half is sorted with `<` instead of `<=`.

#### 7. Say This in the Interview

1. "The array is sorted, so I use binary search. Each step halves the range, so time is `O(log n)`."
2. "I compute the middle as `lo + (hi - lo) / 2` to avoid overflow."
3. "For first/last occurrence I use a lower bound."

#### 8. Quick Check

1. About how many steps does binary search need for 1,000,000 items?
2. Which loop condition do you use when you search for an exact value?

<details>
<summary>Answers</summary>

1. About 20 (`log₂ 1,000,000`).
2. `while (lo <= hi)`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) (Easy) | the classic |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) (Easy) | lower bound |
| 278 | [First Bad Version](https://leetcode.com/problems/first-bad-version/) (Easy) | find the boundary |
| 34 | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium) | two lower bounds |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium) | find the sorted half |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Medium) | compare with the last item |
| 162 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) (Medium) | move toward the bigger neighbour |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (Medium) | treat it as one sorted list |
