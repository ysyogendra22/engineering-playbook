# Merge Sorted Arrays

#### 1. What Is It?

Combine two **sorted** arrays into one sorted array. It is the "merge" step of merge sort.

The trick is **two pointers**, one in each array. At every step take the smaller of the two current items.

In *Merge Sorted Array* (LeetCode 88), `nums1` has extra empty space at the end, and you must merge **into `nums1` in place**. The trick there: **fill from the back**, so you never overwrite an item you still need.

#### 2. How It Works

`nums1 = [1, 2, 3, 0, 0, 0]` (m = 3), `nums2 = [2, 5, 6]` (n = 3)

Fill from the **back**, taking the **bigger** of the two last items:

```text
i = 2 (nums1 last real item), j = 2 (nums2 last), k = 5 (write position)

compare 3 and 6 → 6 is bigger → nums1[5] = 6, j=1, k=4
compare 3 and 5 → 5            → nums1[4] = 5, j=0, k=3
compare 3 and 2 → 3            → nums1[3] = 3, i=1, k=2
compare 2 and 2 → take nums2   → nums1[2] = 2, j=-1, k=1
nums2 is used up → the rest of nums1 is already in place

result [1, 2, 2, 3, 5, 6]
```

Why from the back? The empty space is at the end of `nums1`. Writing at the front would overwrite real data. Writing from the back uses the empty space first.

#### 3. Brute Force vs Optimized

| | Brute force | Two pointers |
|---|---|---|
| Idea | copy both into one array and sort | merge by comparing the front (or back) items |
| Time | `O((m + n) log(m + n))` | `O(m + n)` |
| Space | `O(1)` to `O(m + n)` | `O(1)` in place |

```kotlin
fun mergeBrute(nums1: IntArray, m: Int, nums2: IntArray, n: Int) {
    for (j in 0 until n) nums1[m + j] = nums2[j]
    nums1.sort()
}
```

#### 4. Kotlin Code

```kotlin
// Merge Sorted Array (LeetCode 88): in place, from the back
fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int) {
    var i = m - 1              // last real item of nums1
    var j = n - 1              // last item of nums2
    var k = m + n - 1          // where to write
    while (j >= 0) {           // when nums2 is used up, nums1 is already in place
        if (i >= 0 && nums1[i] > nums2[j]) nums1[k--] = nums1[i--]
        else nums1[k--] = nums2[j--]
    }
}

// Merge two sorted arrays into a new one (simple version)
fun mergeNew(a: IntArray, b: IntArray): IntArray {
    val result = IntArray(a.size + b.size)
    var i = 0; var j = 0; var k = 0
    while (i < a.size && j < b.size) {
        result[k++] = if (a[i] <= b[j]) a[i++] else b[j++]
    }
    while (i < a.size) result[k++] = a[i++]
    while (j < b.size) result[k++] = b[j++]
    return result
}

// Squares of a Sorted Array (LeetCode 977): the biggest square is at one of the two ends
fun sortedSquares(nums: IntArray): IntArray {
    val result = IntArray(nums.size)
    var l = 0
    var r = nums.size - 1
    for (k in nums.size - 1 downTo 0) {
        if (Math.abs(nums[l]) > Math.abs(nums[r])) { result[k] = nums[l] * nums[l]; l++ }
        else { result[k] = nums[r] * nums[r]; r-- }
    }
    return result
}

// Intersection of two sorted arrays (like merge)
fun intersectSorted(a: IntArray, b: IntArray): List<Int> {
    var i = 0; var j = 0
    val result = mutableListOf<Int>()
    while (i < a.size && j < b.size) {
        when {
            a[i] == b[j] -> { result.add(a[i]); i++; j++ }
            a[i] < b[j] -> i++
            else -> j++
        }
    }
    return result
}
```

Checks: `merge([1,2,3,0,0,0], 3, [2,5,6], 3)` gives `[1,2,2,3,5,6]`. `sortedSquares([-4,-1,0,3,10])` → `[0,1,9,16,100]`. `intersectSorted([1,2,2,3],[2,2,4])` → `[2, 2]`.

To merge **k** sorted arrays use a min-heap (`01-data-structure/08-Heap`).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Merge two arrays | `O(m + n)` | `O(1)` in place, `O(m + n)` for a new array |
| Merge `k` arrays with a heap | `O(N log k)` | `O(k)` |

#### 6. Common Mistakes

1. **Filling from the front in place.** You overwrite unread items.
2. **Stopping the loop at the wrong time.** Loop while `j >= 0` (the second array still has items).
3. **Forgetting leftovers** in the "new array" version.
4. **Using `m` and `n` as lengths** instead of indexes `m - 1`, `n - 1`.
5. **`<` vs `<=`** for equal values (only matters if stability is required).

#### 7. Say This in the Interview

1. "Both arrays are sorted, so I use two pointers and compare the front items. That is `O(m + n)`, better than concatenating and sorting."
2. "In place, I start from the back so I never overwrite an item I still need."

#### 8. Quick Check

1. Why does Merge Sorted Array fill `nums1` from the back?
2. After `nums2` is used up, what about the rest of `nums1`?

<details>
<summary>Answers</summary>

1. The free space is at the back, and writing at the front would destroy items not yet merged.
2. It is already in the right place, so nothing more is needed.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (Easy) | fill from the back |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy) | the same on linked lists |
| 977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) (Easy) | two ends |
| 350 | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) (Easy) | two pointers on sorted arrays |
| 986 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) (Medium) | merge-like scan of intervals |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) | min-heap |
