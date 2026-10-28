# Array Traversal

#### 1. What Is It?

**Traversal** means visiting the items of an array in some order. Almost every solution starts with a traversal. Knowing the common ways saves time and avoids off-by-one bugs.

| Way | Use for |
|---|---|
| **Forward** | most problems |
| **Backward** | deleting while looping, building from the end (merge sorted arrays) |
| **From both ends** | palindromes, two pointers |
| **With a step** | every second item, skipping |
| **Circular** (`% n`) | circular arrays, rotation |
| **Neighbours** (`i`, `i + 1`) | comparing adjacent items, sortedness |
| **Nested** | all pairs (brute force), 2D arrays |

#### 2. How It Works

```text
nums = [4, 7, 1, 9]

forward:     4 → 7 → 1 → 9
backward:    9 → 1 → 7 → 4
both ends:   (4,9) → (7,1)
circular:    start at index 3: 9 → 4 → 7 → 1      index = (start + step) % n
adjacent:    (4,7) (7,1) (1,9)
```

Rules that prevent bugs:

- Valid indexes are `0 .. n - 1`. Use `nums.indices` or `until nums.size`.
- When you look at `nums[i + 1]`, loop only to `n - 2`.
- When you look at `nums[i - 1]`, start from `1`.
- Check `nums.isEmpty()` first.

#### 3. Kotlin Code

```kotlin
val nums = intArrayOf(4, 7, 1, 9)

for (x in nums) print("$x ")                           // forward, values only
for (i in nums.indices) print("${nums[i]} ")           // forward, with the index
for (i in nums.indices.reversed()) print("${nums[i]} ") // backward (same as n - 1 downTo 0)

var l = 0
var r = nums.size - 1
while (l < r) {                                        // from both ends
    println("${nums[l]} and ${nums[r]}")
    l++; r--
}

for (i in 0 until nums.size - 1) println(nums[i] + nums[i + 1])   // adjacent pairs
nums.toList().zipWithNext().forEach { (a, b) -> println(a + b) } // the same, shorter

val start = 3
for (step in 0 until nums.size) print("${nums[(start + step) % nums.size]} ")   // circular

for (i in nums.indices step 2) print("${nums[i]} ")    // every second item

// Check if an array is sorted (adjacent traversal)
fun isSorted(a: IntArray): Boolean {
    for (i in 1 until a.size) if (a[i] < a[i - 1]) return false
    return true
}

// Max Consecutive Ones (LeetCode 485)
fun findMaxConsecutiveOnes(nums: IntArray): Int {
    var best = 0
    var run = 0
    for (x in nums) {
        run = if (x == 1) run + 1 else 0
        best = maxOf(best, run)
    }
    return best
}
```

Checks: `isSorted([1,2,2,5])` → `true`. `findMaxConsecutiveOnes([1,1,0,1,1,1])` → `3`.

#### 4. Complexity

| Traversal | Time | Space |
|---|---|---|
| One pass | `O(n)` | `O(1)` |
| Nested (all pairs) | `O(n²)` | `O(1)` |
| 2D grid `R × C` | `O(R · C)` | `O(1)` |

#### 5. Common Mistakes

1. **Off-by-one:** `for (i in 0..nums.size)` goes one step too far. Use `until`.
2. **Reading `nums[i + 1]` at the last index.**
3. **Removing items while looping forward.** Loop backwards or build a new list.
4. **Not handling an empty array** (`nums[0]` crashes).
5. **Using `for (x in nums)` when you need the index.**

#### 6. Say This in the Interview

1. "I traverse once, so time is `O(n)` and space is `O(1)`."
2. "I handle the empty array first, and I stop at `n - 2` because I compare with the next item."

#### 7. Quick Check

1. Which loop visits all valid indexes: `0..n` or `0 until n`?
2. How do you move around a circular array of size `n`?

<details>
<summary>Answers</summary>

1. `0 until n` (`0..n` includes `n`, which is out of range).
2. Use `(index + 1) % n`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) (Easy) | track a run |
| 896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) (Easy) | compare neighbours |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) (Easy) | left sum vs right sum |
| 1752 | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) (Easy) | count drops, circular |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) (Medium) | index with `% n` |
