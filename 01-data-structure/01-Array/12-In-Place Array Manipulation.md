# In-Place Array Manipulation

> Interview phrase: "do it in place" or "with `O(1)` extra space". The answer is almost always two pointers.

#### 1. What Is It?

**In-place** means changing the **input array itself**, using only a few extra variables (`O(1)` extra memory). You do not create a second array.

Three main techniques:

| Technique | Idea | Example |
|---|---|---|
| **Read / write pointers** | a fast pointer reads every item, a slow pointer writes the items you keep | remove duplicates, move zeroes, remove an element |
| **Swapping** | swap items into the right place | reverse, partition, Dutch flag |
| **Overwrite from the back** | fill from the end so you do not destroy unread data | merge sorted arrays (note 14) |

#### 2. How It Works

*Move Zeroes* (LeetCode 283): move all `0`s to the end, keep the order of the others.

`nums = [0, 1, 0, 3, 12]`

```text
write = 0 (the next place for a non-zero)
read 0 (value 0)  → skip
read 1 (value 1)  → nums[write=0] = 1, write = 1        [1, 1, 0, 3, 12]
read 2 (value 0)  → skip
read 3 (value 3)  → nums[write=1] = 3, write = 2        [1, 3, 0, 3, 12]
read 4 (value 12) → nums[write=2] = 12, write = 3       [1, 3, 12, 3, 12]
fill the rest with 0 from write to the end              [1, 3, 12, 0, 0]
```

The same read/write idea removes an element, removes duplicates from a sorted array, and keeps "at most two of each".

#### 3. Brute Force vs Optimized

| | Brute force | In place |
|---|---|---|
| Idea | build a new array of the items you keep | overwrite with a write pointer |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` |

```kotlin
fun moveZeroesBrute(nums: IntArray) {
    val kept = nums.filter { it != 0 }                  // extra O(n) array
    for (i in nums.indices) nums[i] = if (i < kept.size) kept[i] else 0
}
```

The extra array is the only thing the interviewer wants you to remove.

#### 4. Kotlin Code

```kotlin
// Move Zeroes (LeetCode 283)
fun moveZeroes(nums: IntArray) {
    var write = 0
    for (read in nums.indices) {
        if (nums[read] != 0) nums[write++] = nums[read]
    }
    while (write < nums.size) nums[write++] = 0
}

// Remove Element (LeetCode 27): returns the new length
fun removeElement(nums: IntArray, value: Int): Int {
    var write = 0
    for (x in nums) if (x != value) nums[write++] = x
    return write
}

// Remove Duplicates from Sorted Array (LeetCode 26)
fun removeDuplicates(nums: IntArray): Int {
    if (nums.isEmpty()) return 0
    var write = 1
    for (read in 1 until nums.size) {
        if (nums[read] != nums[read - 1]) nums[write++] = nums[read]
    }
    return write
}

// Remove Duplicates from Sorted Array II (LeetCode 80): keep at most two of each
fun removeDuplicatesII(nums: IntArray): Int {
    var write = 0
    for (x in nums) {
        if (write < 2 || x != nums[write - 2]) nums[write++] = x
    }
    return write
}

// Squares in place idea: swap helper
fun swap(a: IntArray, i: Int, j: Int) { val t = a[i]; a[i] = a[j]; a[j] = t }

// Sort Array By Parity (LeetCode 905): evens first, one pass with two ends
fun sortArrayByParity(nums: IntArray): IntArray {
    var l = 0
    var r = nums.size - 1
    while (l < r) {
        if (nums[l] % 2 == 0) l++
        else if (nums[r] % 2 == 1) r--
        else swap(nums, l, r)
    }
    return nums
}
```

Checks: `moveZeroes([0,1,0,3,12])` → `[1,3,12,0,0]`. `removeElement([3,2,2,3], 3)` → `2`. `removeDuplicates([0,0,1,1,1,2,2,3,3,4])` → `5`. `removeDuplicatesII([1,1,1,2,2,3])` → `5`.

For results the questions ask for the new length `k`: only the first `k` items matter.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Read / write pointers | `O(n)` | `O(1)` |
| Swapping partitions | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Overwriting an item you still need to read.** The write pointer must never pass the read pointer.
2. **Forgetting to fill the tail** (for example the zeros).
3. **Returning the wrong length** (the write pointer is the new length).
4. **Deleting with `removeAt` inside a loop** (`O(n²)`).
5. **Empty array** (`nums[0]` crashes).
6. **Assuming the array is sorted** (Remove Duplicates needs a sorted array).

#### 7. Say This in the Interview

1. "I will use a read pointer and a write pointer. The read pointer scans every item. The write pointer marks where the next kept item goes."
2. "That is `O(n)` time and `O(1)` extra space, and I never overwrite an unread item."

#### 8. Quick Check

1. After moving zeroes in `[0, 1, 0, 2]`, what is `write` before the final fill?
2. In Remove Duplicates, when is an item kept?

<details>
<summary>Answers</summary>

1. `2` (two non-zero items: 1 and 2).
2. When it is different from the item before it (the array is sorted).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) (Easy) | read / write pointers |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) (Easy) | keep what is not the value |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) (Easy) | compare with the previous |
| 905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) (Easy) | two ends, swap |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (Easy) | write from the back (note 14) |
| 80 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) (Medium) | keep at most two |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) (Medium) | three-way partition (note 20) |
