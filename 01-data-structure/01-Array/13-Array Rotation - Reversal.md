# Array Rotation / Reversal

#### 1. What Is It?

**Reversal** flips an array: the first item swaps with the last, the second with the second last, and so on.

**Rotation** moves every item `k` places to the right (or left), and items that fall off one end come back at the other end.

```text
rotate right by 2:   [1, 2, 3, 4, 5]  →  [4, 5, 1, 2, 3]
```

The famous trick: **rotation = three reversals.** It works in place with `O(1)` extra space.

#### 2. How It Works

Rotate right by `k` (use `k = k % n` first, because rotating by `n` changes nothing):

```text
nums = [1, 2, 3, 4, 5], k = 2

1. reverse the whole array:        [5, 4, 3, 2, 1]
2. reverse the first k items:      [4, 5, 3, 2, 1]
3. reverse the rest (n - k items): [4, 5, 1, 2, 3]   ✓
```

Why it works: reversing the whole array brings the last `k` items to the front (but backwards). The two small reversals fix the order inside each part.

Rotate **left** by `k`: reverse the first `k`, reverse the rest, then reverse the whole array. (Or rotate right by `n - k`.)

Other facts:

- A **rotated sorted array** (like `[4, 5, 1, 2, 3]`) has exactly one place where the order drops. Binary search uses this (note 09).
- A string `s` is a rotation of `t` if `s` appears inside `t + t` and the lengths are equal.

#### 3. Brute Force vs Optimized

| | Brute force | Three reversals |
|---|---|---|
| Idea | shift the whole array by one place, `k` times | reverse the array in three parts |
| Time | `O(n · k)` | `O(n)` |
| Space | `O(1)` | `O(1)` |
| Another way | copy into a new array at `(i + k) % n` | — |

```kotlin
fun rotateBrute(nums: IntArray, k: Int) {
    repeat(k % nums.size) {
        val last = nums[nums.size - 1]
        for (i in nums.size - 1 downTo 1) nums[i] = nums[i - 1]     // shift right by one
        nums[0] = last
    }
}

fun rotateWithCopy(nums: IntArray, k: Int) {                       // O(n) time, O(n) space
    val copy = nums.copyOf()
    for (i in nums.indices) nums[(i + k) % nums.size] = copy[i]
}
```

#### 4. Kotlin Code

```kotlin
private fun reverse(nums: IntArray, from: Int, to: Int) {
    var l = from
    var r = to
    while (l < r) {
        val t = nums[l]; nums[l] = nums[r]; nums[r] = t
        l++; r--
    }
}

// Rotate Array (LeetCode 189): rotate right by k
fun rotate(nums: IntArray, k: Int) {
    val n = nums.size
    if (n == 0) return
    val shift = k % n
    reverse(nums, 0, n - 1)           // 1. the whole array
    reverse(nums, 0, shift - 1)       // 2. the first `shift` items
    reverse(nums, shift, n - 1)       // 3. the rest
}

// Reverse String (LeetCode 344)
fun reverseString(s: CharArray) {
    var l = 0
    var r = s.size - 1
    while (l < r) { val t = s[l]; s[l] = s[r]; s[r] = t; l++; r-- }
}

// Rotate String (LeetCode 796): is goal a rotation of s?
fun rotateString(s: String, goal: String): Boolean =
    s.length == goal.length && (s + s).contains(goal)

// Check if Array Is Sorted and Rotated (LeetCode 1752): at most one drop (circular)
fun check(nums: IntArray): Boolean {
    var drops = 0
    for (i in nums.indices) {
        if (nums[i] > nums[(i + 1) % nums.size]) drops++
    }
    return drops <= 1
}
```

Checks: `rotate([1,2,3,4,5,6,7], 3)` → `[5,6,7,1,2,3,4]`. `rotateString("abcde", "cdeab")` → `true`. `check([3,4,5,1,2])` → `true`. `check([2,1,3,4])` → `false`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Three reversals | `O(n)` | `O(1)` |
| Copy method | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Forgetting `k % n`.** `k` can be larger than `n`.
2. **`k % n == 0`** and then reversing `0 .. -1`. The reverse function must handle an empty range (the `l < r` check does).
3. **Wrong order of the three reversals.**
4. **Rotating left vs right** mixed up.
5. **Empty array** (`k % 0` crashes).
6. **Returning a new array** when the question says modify `nums` in place.

#### 7. Say This in the Interview

1. "Rotation by `k` is three reversals: the whole array, then the first `k`, then the rest. That is `O(n)` time and `O(1)` space."
2. "I take `k % n` first."

#### 8. Quick Check

1. `[1, 2, 3, 4]` rotated right by 1?
2. What is `k` after `k % n` for `k = 9`, `n = 4`?

<details>
<summary>Answers</summary>

1. `[4, 1, 2, 3]`.
2. `1`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) (Easy) | two pointers swap |
| 796 | [Rotate String](https://leetcode.com/problems/rotate-string/) (Easy) | `s + s` contains `goal` |
| 1752 | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) (Easy) | at most one drop |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) (Medium) | three reversals |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Medium) | binary search |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium) | binary search |
