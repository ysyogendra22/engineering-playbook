# Array Fundamentals

> Start here. Arrays are the most common input in FAANG coding rounds. Most array questions use one of about 12 patterns, and this folder teaches them in order.

#### 1. What Is an Array?

An **array** stores items **one after another in memory**. Each item has a position called an **index**, and the first index is `0`.

```text
index:   0    1    2    3    4
value: [ 7 ][ 3 ][ 9 ][ 1 ][ 5 ]
```

Why it is used: because the items sit next to each other, you can jump to **any index in `O(1)`**. Arrays are the base of strings, matrices, stacks, queues, heaps and hash tables.

The size of a plain array is **fixed**. If you need a list that grows, use an `ArrayList` (`MutableList` in Kotlin).

#### 2. Words You Must Know

| Word | Meaning |
|---|---|
| **Index** | the position of an item, starting at 0 |
| **Length / size** | the number of items |
| **Subarray** | a **continuous** part of the array, for example `[3, 9, 1]` |
| **Subsequence** | items in order, but **not necessarily next to each other**, for example `[7, 9, 5]` |
| **In-place** | changing the array itself, using `O(1)` extra memory |
| **`O(1)`, `O(n)`** | the work stays the same / grows with the length |

A subarray is continuous. A subsequence can skip items. Interview questions use these words carefully.

#### 3. How It Works

Why access is fast: the address of index `i` is `start + i × itemSize`. The computer does one multiplication, so it does not matter how long the array is.

Why insert and delete in the middle are slow: the items after the position must **shift**.

```text
insert 8 at index 2 in [7, 3, 9, 1, 5]:
shift 9, 1, 5 one place to the right  →  [7, 3, _, 9, 1, 5]  →  put 8  →  [7, 3, 8, 9, 1, 5]
```

#### 4. Kotlin Code

```kotlin
val nums = intArrayOf(7, 3, 9, 1, 5)          // fixed size, primitives (fast, no boxing)
val zeros = IntArray(5)                        // [0, 0, 0, 0, 0]
val filled = IntArray(5) { it * 2 }            // [0, 2, 4, 6, 8]

println(nums[2])                               // 9   (access, O(1))
nums[2] = 10                                   // update, O(1)
println(nums.size)                             // 5

for (x in nums) println(x)                     // each value
for (i in nums.indices) println("$i: ${nums[i]}")
for ((i, x) in nums.withIndex()) println("$i: $x")

println(nums.contentToString())                // [7, 3, 10, 1, 5]   (println(nums) would print an address)
val copy = nums.copyOf()                       // a real copy
nums.sort()                                    // sorts in place, O(n log n)

val list = mutableListOf(7, 3, 9)              // a growing list (ArrayList)
list.add(1)

val grid = Array(3) { IntArray(4) }            // 3 rows, 4 columns, all zeros
grid[1][2] = 5
```

#### 5. How to Spot an Array Pattern

| If the question says... | Think... | Note |
|---|---|---|
| sorted array, pair that adds to a target, palindrome | two pointers | 04 |
| longest/shortest subarray with a rule, fixed size `k` | sliding window | 05 |
| sum of a range, many queries | prefix sum | 06, 25 |
| "subarray with sum `k`" (negatives allowed) | prefix sum + HashMap | 26 |
| maximum subarray sum | Kadane | 10 |
| count / find duplicates, anagrams | frequency count, hashing | 07 |
| sorted, "find in `O(log n)`" | binary search | 09, 24 |
| intervals, meetings, overlap | sort + merge | 15, 29 |
| "do it in place", "`O(1)` space" | pointers, swapping | 12, 20, 21 |
| rotate, reverse | three reversals | 13 |
| matrix, grid, spiral | 2D traversal | 16 |
| 1 to n numbers, find missing/duplicate | cyclic sort | 21 |
| kth largest | quickselect or heap | 22 |

#### 6. Complexity

| Action | Time |
|---|---|
| Access / update by index | `O(1)` |
| Search (unsorted) | `O(n)` |
| Search (sorted, binary search) | `O(log n)` |
| Insert / delete in the middle | `O(n)` |
| Insert / delete at the end (`ArrayList`) | `O(1)` on average |
| Memory for `n` items | `O(n)` |

#### 7. Common Mistakes

1. **Index out of bounds.** The last index is `size - 1`.
2. **Printing an `IntArray` directly.** It prints an address. Use `contentToString()`.
3. **`==` on two arrays.** It compares references. Use `contentEquals`.
4. **Changing an array while looping over it** without thinking about the indexes.
5. **Forgetting empty and one-item arrays.**
6. **Copying with `val b = a`.** That is the same array. Use `a.copyOf()`.

#### 8. Say This in the Interview

1. "Let me confirm: is the array sorted? Can it have duplicates or negative numbers? Can it be empty?"
2. "Brute force is `O(n²)` with two loops. I can do better with ..."
3. "I will state the time and space at the end."

#### 9. Quick Check

1. What is the time to read `nums[100000]`?
2. What is the difference between a subarray and a subsequence?

<details>
<summary>Answers</summary>

1. `O(1)`.
2. A subarray is continuous. A subsequence keeps the order but can skip items.

</details>

#### 10. Related LeetCode Questions (Easy → Medium)

Solve them in this order. Search by title if a link looks wrong.

**Start here — Easy**

| # | Question | Main idea | Note |
|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | hash map of seen values | 07 |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | set or sort | 07 |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | read/write pointers | 12 |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | track the minimum so far | 10 |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | merge from the back | 14 |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | prefix sum | 06 |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | halve the range | 09 |

**Most often asked — Medium**

| # | Question | Main idea | Note |
|---|---|---|---|
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane | 10 |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | prefix × suffix | 18 |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | sort + two pointers | 04 |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | two pointers | 04 |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | sort + merge | 15 |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | prefix sum + map | 26 |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Dutch national flag | 20 |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | binary search | 09 |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | transpose + reverse | 16 |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | sliding window | 05 |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | quickselect or heap | 22 |
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | cyclic sort (Hard) | 21 |

**If you have little time, do these 8 first:** 1, 53, 238, 15, 56, 560, 3, 33.

For one-page revision, read the **Array Cheat Sheet** (note 99).
