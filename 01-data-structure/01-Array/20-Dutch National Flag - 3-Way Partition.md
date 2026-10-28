# Dutch National Flag / 3-Way Partition

#### 1. What Is It?

The **Dutch National Flag** problem sorts an array that contains only **three kinds of values** (for example `0`, `1`, `2`) in **one pass** and **in place**.

It uses **three pointers** and splits the array into four zones:

```text
[ 0s | 1s | unknown | 2s ]
  ↑low   ↑mid       ↑high
```

- Everything before `low` is `0`.
- Everything from `low` up to (not including) `mid` is `1`.
- Everything after `high` is `2`.
- `mid` scans the unknown part.

It is also the idea behind a 3-way partition in quicksort, and it is the clean answer to *Sort Colors* (LeetCode 75).

#### 2. How It Works

Look at `nums[mid]`:

| `nums[mid]` | Do | Why |
|---|---|---|
| `0` | swap with `nums[low]`; `low++`, `mid++` | a `0` belongs on the left |
| `1` | `mid++` | already in the middle zone |
| `2` | swap with `nums[high]`; `high--` (**do not** move `mid`) | the swapped-in item is unknown, so look at it again |

`nums = [2, 0, 2, 1, 1, 0]`

```text
low=0 mid=0 high=5   [2,0,2,1,1,0]   nums[mid]=2 → swap with high → [0,0,2,1,1,2]  high=4
low=0 mid=0 high=4   [0,0,2,1,1,2]   nums[mid]=0 → swap with low (itself) → low=1 mid=1
low=1 mid=1 high=4   [0,0,2,1,1,2]   nums[mid]=0 → swap with low (itself) → low=2 mid=2
low=2 mid=2 high=4   [0,0,2,1,1,2]   nums[mid]=2 → swap with high → [0,0,1,1,2,2]  high=3
low=2 mid=2 high=3   [0,0,1,1,2,2]   nums[mid]=1 → mid=3
low=2 mid=3 high=3   nums[mid]=1 → mid=4
mid > high → stop        result [0,0,1,1,2,2]
```

#### 3. Brute Force vs Optimized

| | Sort | Count then fill | Dutch flag |
|---|---|---|---|
| Time | `O(n log n)` | `O(n)`, two passes | `O(n)`, one pass |
| Space | `O(1)` | `O(1)` | `O(1)` |

```kotlin
fun sortColorsCounting(nums: IntArray) {
    val count = IntArray(3)
    for (x in nums) count[x]++                       // pass 1: count
    var i = 0
    for (color in 0..2) repeat(count[color]) { nums[i++] = color }   // pass 2: write
}
```

The interview follow-up is almost always "can you do it in **one pass**?".

#### 4. Kotlin Code

```kotlin
// Sort Colors (LeetCode 75)
fun sortColors(nums: IntArray) {
    var low = 0
    var mid = 0
    var high = nums.size - 1
    while (mid <= high) {
        when (nums[mid]) {
            0 -> { swap(nums, low, mid); low++; mid++ }
            1 -> mid++
            else -> { swap(nums, mid, high); high-- }          // do not move mid
        }
    }
}

private fun swap(a: IntArray, i: Int, j: Int) { val t = a[i]; a[i] = a[j]; a[j] = t }

// 3-way partition around a pivot value: smaller | equal | bigger
fun partitionAround(nums: IntArray, pivot: Int) {
    var low = 0
    var mid = 0
    var high = nums.size - 1
    while (mid <= high) {
        when {
            nums[mid] < pivot -> { swap(nums, low, mid); low++; mid++ }
            nums[mid] == pivot -> mid++
            else -> { swap(nums, mid, high); high-- }
        }
    }
}

// Sort Array By Parity II (LeetCode 922): even indexes get even numbers, odd indexes get odd numbers
fun sortArrayByParityII(nums: IntArray): IntArray {
    var even = 0
    var odd = 1
    while (even < nums.size && odd < nums.size) {
        if (nums[even] % 2 == 0) even += 2
        else if (nums[odd] % 2 == 1) odd += 2
        else { swap(nums, even, odd); even += 2; odd += 2 }
    }
    return nums
}
```

Checks: `sortColors([2,0,2,1,1,0])` → `[0,0,1,1,2,2]`. `partitionAround([5,1,5,3,7,5], 5)` → items smaller than 5 first, then the 5s, then the bigger ones.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Dutch national flag | `O(n)` (one pass) | `O(1)` |

#### 6. Common Mistakes

1. **Moving `mid` after swapping with `high`.** The new item at `mid` is unchecked.
2. **Loop condition `mid < high`** instead of `mid <= high`. The last unknown item is missed.
3. **Moving `low` and `mid` wrongly** when `low == mid` (swap with itself is fine).
4. **Using it with more than three values.** Use counting sort or sort.
5. **Forgetting empty and one-item arrays.**

#### 7. Say This in the Interview

1. "Sorting is `O(n log n)`. Since there are only three values, I use three pointers and finish in one pass: `O(n)` time, `O(1)` space."
2. "When I swap a `2` from the right, I do not move `mid`, because the swapped-in value is not checked yet."

#### 8. Quick Check

1. After swapping `nums[mid]` with `nums[low]` (a `0`), what moves?
2. After swapping with `nums[high]` (a `2`), what moves?

<details>
<summary>Answers</summary>

1. `low++` and `mid++`.
2. Only `high--`. `mid` stays.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) (Easy) | two-way version |
| 905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) (Easy) | two-way partition |
| 922 | [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/) (Easy) | two index pointers |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) (Medium) | three-way partition |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium) | partition idea (note 22) |
| 324 | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) (Medium) | partition around the median |
