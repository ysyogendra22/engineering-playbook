# Common Array Edge Cases

> Read this list before every array interview and run through it at the end of every solution.

#### 1. What Is It?

Edge cases are the inputs where a solution that looks right **crashes** or **gives a wrong answer**. Interviewers watch if you check them yourself. Most array bugs come from five places:

1. **empty or tiny** input,
2. **index bounds** (off-by-one),
3. **duplicates and equal values**,
4. **negative numbers and zero**,
5. **overflow** and **changing the input**.

#### 2. The Checklist

| # | Edge case | What goes wrong | Fix |
|---|---|---|---|
| 1 | Empty array | `nums[0]` crashes | check `isEmpty()` first |
| 2 | One element | loops that compare neighbours do nothing | test it; return early if needed |
| 3 | Two elements | `i + 1`, `i - 1` or `mid` logic breaks | test it |
| 4 | All elements equal | duplicate logic, `<` vs `<=`, windows | test it |
| 5 | Already sorted / reverse sorted | worst case for some algorithms | test both |
| 6 | Off-by-one: `0..n` instead of `0 until n` | index out of bounds | use `until` / `indices` |
| 7 | `nums[i + 1]` at the last index | crash | loop to `n - 2` |
| 8 | Negative numbers | sliding window sums, `Kadane` start value | prefix sum + map; start with `nums[0]` |
| 9 | Zeros | product problems, division | count the zeros; avoid division |
| 10 | Duplicates | `3Sum` repeats, sets lose items | skip equal neighbours |
| 11 | `Int` overflow (sums, products, `mid`) | wrong result | use `Long`; `lo + (hi - lo) / 2` |
| 12 | `Int.MIN_VALUE` as a sentinel | `-x`, `abs`, `x - 1` overflow | use `Long` or a nullable |
| 13 | `k` larger than `n` | rotation, window | `k % n`; check `k <= n` |
| 14 | Changing the array while looping | skipped items | loop backwards or copy |
| 15 | Modifying the input when it should not be changed | caller's data is damaged | copy it |
| 16 | `==` on arrays | compares references | `contentEquals` |
| 17 | Printing an array | prints an address | `contentToString()` |
| 18 | `list.removeAt(0)` / `list.add(0, x)` in a loop | `O(n²)` | use `ArrayDeque` or a pointer |
| 19 | 2D: `rows` vs `cols` mixed | wrong cells | `matrix.size`, `matrix[0].size` |
| 20 | 2D: empty matrix or empty first row | `matrix[0]` crashes | check both |

#### 3. Kotlin Code

```kotlin
// 1 and 2. Guard clauses
fun maxOfArray(nums: IntArray): Int? {
    if (nums.isEmpty()) return null                 // empty: no answer
    var best = nums[0]
    for (i in 1 until nums.size) best = maxOf(best, nums[i])
    return best
}

// 7. Adjacent pairs: stop at n - 2
fun hasAdjacentEqual(nums: IntArray): Boolean {
    for (i in 0 until nums.size - 1) if (nums[i] == nums[i + 1]) return true
    return false
}

// 11. Overflow
val a = Int.MAX_VALUE
println(a + 1)                                      // -2147483648  (wrong)
println(a.toLong() + 1)                             // 2147483648
val mid = lo + (hi - lo) / 2                        // safe middle (instead of (lo + hi) / 2)

// 14. Removing while looping: go backwards
val list = mutableListOf(1, 2, 2, 3)
for (i in list.indices.reversed()) if (list[i] == 2) list.removeAt(i)
list.removeIf { it == 2 }                           // or use removeIf

// 16 and 17. Arrays compare and print
val x = intArrayOf(1, 2); val y = intArrayOf(1, 2)
println(x == y)                                     // false (different objects)
println(x.contentEquals(y))                         // true
println(x.contentToString())                        // [1, 2]

// 15. Copy when the caller must not see changes
val copy = x.copyOf()
```

#### 4. Complexity

Edge cases do not change the complexity. They change **correctness**. Two exceptions: `removeAt(0)` in a loop turns `O(n)` into `O(n²)`, and an unlucky input (sorted, all equal) can push quicksort-style code to `O(n²)`.

#### 5. Common Mistakes

1. **Testing only the example from the question.** Always add: empty, one item, two items, all equal, sorted, reverse sorted, negatives, duplicates, maximum values.
2. **Not asking the interviewer** about the constraints ("Can the array be empty? Can it have negatives or duplicates? How big can `n` be?").
3. **Returning early on an edge case but forgetting what to return** (`0`, `-1`, `null`, empty list).

#### 6. Say This in the Interview

1. "Before I code, let me confirm the constraints: can the array be empty, have duplicates, or negative numbers? How large can `n` be?"
2. "Edge cases I will test: empty, one item, all equal, sorted, and large values for overflow."

#### 7. Quick Check

1. Which loop reads `nums[i + 1]` safely?
2. How do you compare two arrays by content?

<details>
<summary>Answers</summary>

1. `for (i in 0 until nums.size - 1)`.
2. `a.contentEquals(b)`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Edge case to watch |
|---|---|---|
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Medium) | all negative numbers |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) | zeros |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) (Medium) | duplicates, fewer than 3 items |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) (Medium) | `k > n` |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) (Easy) | one item, overflow of `mid` |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (Easy) | empty `nums2` or `nums1` |
