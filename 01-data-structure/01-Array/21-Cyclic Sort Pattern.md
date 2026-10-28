# Cyclic Sort Pattern

#### 1. What Is It?

**Cyclic sort** is for arrays that hold numbers in the range **`1 .. n`** (or `0 .. n`). The idea: **put each number in its own place.** The number `x` belongs at index `x - 1`.

After this, the array is sorted, and the **missing** and **duplicate** numbers sit in the wrong places. You find them with one more scan.

Why it matters: it solves "find the missing / duplicate number" in `O(n)` time and **`O(1)` space**, with no HashSet and no sorting.

How to spot it: "the array contains numbers from `1` to `n`", "find the missing number", "find the duplicate", "first missing positive".

#### 2. How It Works

For each index `i`, while `nums[i]` is not in its right place, **swap it into its place**:

```text
the right place of x is index x - 1
if nums[i] is already at its place, or the place already holds x (a duplicate) → move on
```

`nums = [3, 1, 5, 4, 2]` (values 1..5)

```text
i=0: nums[0]=3 belongs at index 2 → swap with nums[2]  → [5, 1, 3, 4, 2]
i=0: nums[0]=5 belongs at index 4 → swap with nums[4]  → [2, 1, 3, 4, 5]
i=0: nums[0]=2 belongs at index 1 → swap with nums[1]  → [1, 2, 3, 4, 5]
i=0: nums[0]=1 is in place → i=1 ... all in place
sorted [1, 2, 3, 4, 5]
```

Each swap puts at least one number in its final place, so the total swaps are at most `n`. So it is `O(n)`, even with the inner `while`.

*Find All Numbers Disappeared* (LeetCode 448): after the placement, every index `i` where `nums[i] != i + 1` means the number `i + 1` is missing.

*First Missing Positive* (LeetCode 41): ignore numbers outside `1..n`. After placing, the first index with `nums[i] != i + 1` gives the answer `i + 1`. If all are in place, the answer is `n + 1`.

#### 3. Brute Force vs Optimized

| | HashSet | Sort | Cyclic sort |
|---|---|---|---|
| Time | `O(n)` | `O(n log n)` | `O(n)` |
| Space | `O(n)` | `O(1)` | `O(1)` |

```kotlin
fun firstMissingPositiveSet(nums: IntArray): Int {
    val set = nums.toHashSet()                         // O(n) extra space
    var x = 1
    while (x in set) x++
    return x
}
```

#### 4. Kotlin Code

```kotlin
private fun swap(a: IntArray, i: Int, j: Int) { val t = a[i]; a[i] = a[j]; a[j] = t }

// Place every number x (1..n) at index x - 1
fun cyclicSort(nums: IntArray) {
    var i = 0
    while (i < nums.size) {
        val correct = nums[i] - 1
        if (nums[i] != nums[correct]) swap(nums, i, correct) else i++
    }
}

// First Missing Positive (LeetCode 41)
fun firstMissingPositive(nums: IntArray): Int {
    val n = nums.size
    var i = 0
    while (i < n) {
        val v = nums[i]
        if (v in 1..n && nums[v - 1] != v) swap(nums, i, v - 1) else i++      // ignore values outside 1..n
    }
    for (j in 0 until n) if (nums[j] != j + 1) return j + 1
    return n + 1
}

// Find All Numbers Disappeared in an Array (LeetCode 448)
fun findDisappearedNumbers(nums: IntArray): List<Int> {
    var i = 0
    while (i < nums.size) {
        val correct = nums[i] - 1
        if (nums[i] != nums[correct]) swap(nums, i, correct) else i++
    }
    val missing = mutableListOf<Int>()
    for (j in nums.indices) if (nums[j] != j + 1) missing.add(j + 1)
    return missing
}

// Find the Duplicate Number (LeetCode 287): n + 1 numbers in 1..n (this version changes the array)
fun findDuplicate(nums: IntArray): Int {
    var i = 0
    while (i < nums.size) {
        if (nums[i] != i + 1) {
            val correct = nums[i] - 1
            if (nums[i] != nums[correct]) swap(nums, i, correct) else return nums[i]   // already there: duplicate
        } else i++
    }
    return -1
}

// Missing Number (LeetCode 268): numbers 0..n, one missing. No sorting needed: use the sum.
fun missingNumber(nums: IntArray): Int = nums.size * (nums.size + 1) / 2 - nums.sum()
```

Checks: `firstMissingPositive([3,4,-1,1])` → `2`. `firstMissingPositive([7,8,9,11,12])` → `1`. `findDisappearedNumbers([4,3,2,7,8,2,3,1])` → `[5, 6]`. `findDuplicate([1,3,4,2,2])` → `2`. `missingNumber([3,0,1])` → `2`.

If you must not change the array, use the HashSet version, or Floyd's cycle detection for Find the Duplicate Number (HashMap folder, note 18).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Cyclic sort | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Using `nums[i] != i + 1` as the swap check.** It loops forever on duplicates. Check `nums[i] != nums[correct]`.
2. **Moving `i` after a swap.** The new value at `i` still needs checking.
3. **Not ignoring values outside `1..n`** (zero, negatives, huge numbers) in First Missing Positive. This causes index errors.
4. **Using it when values are outside the `1..n` range.** It does not apply.
5. **Changing the input** when the question says not to.

#### 7. Say This in the Interview

1. "The numbers are in `1..n`, so each value has a home index: `value - 1`. I swap each value home. Then the first index with the wrong value shows the missing number."
2. "That is `O(n)` time and `O(1)` space, better than a HashSet."
3. "It changes the array. If that is not allowed, I would use a HashSet."

#### 8. Quick Check

1. Where does the value `4` belong in a `1..n` array?
2. Why is cyclic sort `O(n)` and not `O(n²)`?

<details>
<summary>Answers</summary>

1. At index `3` (`value - 1`).
2. Every swap puts one value in its final place, so there are at most `n` swaps in total.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) (Easy) | sum formula or cyclic sort |
| 448 | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) (Easy) | place, then scan |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium) | place until a duplicate shows |
| 442 | [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) (Medium) | place, then scan |
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) (Hard) | place `1..n`, ignore the rest |
