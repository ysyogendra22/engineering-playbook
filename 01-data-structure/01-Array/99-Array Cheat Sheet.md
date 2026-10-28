# Array Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–30.

#### 1. Key Takeaways

1. An array gives `O(1)` access by index. Insert and delete in the middle cost `O(n)`.
2. Most array questions fit about **12 patterns**. Naming the pattern is half the answer.
3. Say the **brute force first** (usually two loops, `O(n²)`), then improve it.
4. **Sorted input** → two pointers or binary search. **Continuous part** → sliding window, prefix sum or Kadane. **"In place"** → pointers and swaps.
5. Sliding windows for sums need **non-negative** numbers. With negatives use **prefix sum + HashMap**.
6. Always check: empty, one item, duplicates, negatives, overflow (`Long`), and `k > n`.

#### 2. Operations and Complexity

| Action | Time |
|---|---|
| Access / update by index | `O(1)` |
| Search, unsorted / sorted | `O(n)` / `O(log n)` |
| Insert / delete in the middle | `O(n)` |
| Append (`ArrayList`) | `O(1)` on average |
| Sort | `O(n log n)` |
| Memory for `n` items | `O(n)` |

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Complexity | Note |
|---|---|---|---|
| sorted array, pair / triple with a sum | **two pointers** | `O(n)` | 04 |
| longest / shortest continuous part with a rule, size `k` | **sliding window** | `O(n)` | 05 |
| sum of a range, many queries | **prefix sum** | `O(1)` per query | 06 |
| count subarrays with sum `k`, negatives allowed | **prefix sum + HashMap** | `O(n)` | 26 |
| maximum sum subarray | **Kadane** | `O(n)` | 10 |
| seen before? counts? anagram? | **hashing / counting** | `O(n)` | 07 |
| sorted, "find", `O(log n)` | **binary search** | `O(log n)` | 09 |
| "smallest x that works" (speed, capacity, days) | **binary search on answer** | `O(n log range)` | 24 |
| intervals, meetings, overlap | **sort + merge** | `O(n log n)` | 15 |
| most overlap at one time | **sweep line** | `O(n log n)` | 29 |
| many range additions | **difference array** | `O(q + n)` | 19 |
| "in place", `O(1)` space, remove / move | **read / write pointers** | `O(n)` | 12 |
| only 3 values (0 / 1 / 2) | **Dutch national flag** | `O(n)` one pass | 20 |
| numbers `1..n`, missing / duplicate | **cyclic sort** | `O(n)`, `O(1)` space | 21 |
| kth largest / smallest | **quickselect** or heap | `O(n)` avg / `O(n log k)` | 22 |
| element in more than `n/2` | **Boyer-Moore** | `O(n)`, `O(1)` space | 23 |
| rotate by `k` | **three reversals** | `O(n)`, `O(1)` space | 13 |
| left and right of each index (except self) | **prefix × suffix** | `O(n)` | 18 |
| two sorted arrays | **merge from the back** | `O(m + n)` | 14 |
| matrix rotate / spiral / sum of rectangle | **transpose + reverse**, borders, **2D prefix sum** | `O(R·C)` | 16, 25 |
| "exactly k" subarrays | **atMost(k) − atMost(k−1)** | `O(n)` | 27 |
| huge values, only order matters | **coordinate compression** | `O(n log n)` | 28 |
| `n` about 40, subsets | **meet in the middle** | `O(2^(n/2))` | 30 |

#### 4. Templates to Memorise

**Two pointers (sorted pair)**

```kotlin
var l = 0; var r = nums.size - 1
while (l < r) {
    val sum = nums[l] + nums[r]
    when { sum == target -> return true; sum < target -> l++; else -> r-- }
}
```

**Variable sliding window**

```kotlin
var left = 0
for (right in nums.indices) {
    // add nums[right] to the window
    while (/* window is invalid */) { /* remove nums[left] */ left++ }
    best = maxOf(best, right - left + 1)
}
```

**Prefix sum + HashMap (count subarrays with sum k)**

```kotlin
val count = hashMapOf(0 to 1); var sum = 0; var answer = 0
for (x in nums) { sum += x; answer += count[sum - k] ?: 0; count[sum] = (count[sum] ?: 0) + 1 }
```

**Kadane**

```kotlin
var cur = nums[0]; var best = nums[0]
for (i in 1 until nums.size) { cur = maxOf(nums[i], cur + nums[i]); best = maxOf(best, cur) }
```

**Binary search (exact value)**

```kotlin
var lo = 0; var hi = nums.size - 1
while (lo <= hi) {
    val mid = lo + (hi - lo) / 2
    when { nums[mid] == target -> return mid; nums[mid] < target -> lo = mid + 1; else -> hi = mid - 1 }
}
```

**In place: read / write pointers**

```kotlin
var write = 0
for (read in nums.indices) if (nums[read] != 0) nums[write++] = nums[read]
```

**Merge intervals**

```kotlin
val sorted = intervals.sortedBy { it[0] }
val result = mutableListOf(sorted[0].copyOf())
for (i in 1 until sorted.size) {
    if (sorted[i][0] <= result.last()[1]) result.last()[1] = maxOf(result.last()[1], sorted[i][1])
    else result.add(sorted[i].copyOf())
}
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Optimized |
|---|---|---|
| Two Sum | two loops `O(n²)` | HashMap `O(n)` |
| Two Sum, sorted | two loops | two pointers `O(n)`, `O(1)` space |
| Max subarray sum | all subarrays `O(n²)` | Kadane `O(n)` |
| Subarray sum equals `k` | all subarrays `O(n²)` | prefix sum + HashMap `O(n)` |
| Range sum queries | loop each time `O(n)` | prefix sum `O(1)` |
| Max sum of size `k` | recompute each window `O(n·k)` | slide the window `O(n)` |
| Rotate by `k` | shift one step `k` times `O(n·k)` | three reversals `O(n)` |
| Merge sorted arrays | concatenate + sort `O((m+n) log)` | merge `O(m + n)` |
| Merge intervals | compare all pairs `O(n²)` | sort + one pass `O(n log n)` |
| Sort colours (0/1/2) | sort `O(n log n)` | Dutch flag `O(n)` |
| Kth largest | sort `O(n log n)` | quickselect `O(n)` avg |
| Missing number (`1..n`) | HashSet `O(n)` space | sum formula / cyclic sort `O(1)` space |
| Product except self | for each `i` multiply others `O(n²)` | prefix × suffix `O(n)` |

#### 6. Common Mistakes and Edge Cases

1. Index out of bounds: use `until`, loop to `n - 2` when reading `i + 1`.
2. Sliding window or two pointers on the wrong input (negatives, unsorted).
3. `best` initialised to `0` when all numbers can be negative.
4. `count[x]++` on a `HashMap` (does not compile): use `(count[x] ?: 0) + 1`.
5. `==` on arrays, printing arrays directly: use `contentEquals`, `contentToString`.
6. `(lo + hi) / 2` overflow: use `lo + (hi - lo) / 2`.
7. Forgetting `k % n` for rotation, `{0: 1}` for prefix maps, the extra `0` bar or sentinel.
8. Merge intervals: use `maxOf` for the end, sort first, `<=` for touching intervals.
9. Overflow in sums and products: use `Long`.
10. Test: empty, one item, two items, all equal, sorted, reverse sorted, negatives, duplicates.

#### 7. What to Say Out Loud

1. "Let me confirm the constraints: sorted? negatives? duplicates? size of `n`? in place?"
2. "Brute force is `O(n²)`. I notice ... so I can use ... to get `O(n)`."
3. "Time `O(...)`, space `O(...)`. Edge cases: empty array, one item, duplicates."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Two Sum](https://leetcode.com/problems/two-sum/) | hashing |
| Easy | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | hashing |
| Easy | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | running minimum |
| Easy | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | in place |
| Easy | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | merge from the back |
| Easy | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | prefix sum |
| Easy | [Binary Search](https://leetcode.com/problems/binary-search/) | binary search |
| Medium | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane |
| Medium | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | prefix × suffix |
| Medium | [3Sum](https://leetcode.com/problems/3sum/) | two pointers |
| Medium | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | two pointers |
| Medium | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | sliding window |
| Medium | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | sort + merge |
| Medium | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | prefix sum + map |
| Medium | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Dutch flag |
| Medium | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | binary search |
| Medium | [Rotate Image](https://leetcode.com/problems/rotate-image/) | matrix |
| Medium | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | quickselect |
| Medium | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | binary search on answer |
