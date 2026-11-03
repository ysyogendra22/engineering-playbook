# Unique Elements Pattern

> "Distinct", "unique" and "how many different" are a `HashSet` (or `LinkedHashSet` for order, `TreeSet` for sorted).

#### 1. What Is It?

The **unique elements pattern** keeps only one copy of each value.

| Need | Tool |
|---|---|
| Unique values, any order | `HashSet` |
| Unique values, **first-seen order** | `LinkedHashSet` / `mutableSetOf()` |
| Unique values, **sorted** | `TreeSet` |
| Number of distinct values | `toHashSet().size` |
| Values that appear **exactly once** | `HashMap` of counts |

**Signals:** "distinct", "unique", "remove duplicates", "how many different", "third maximum distinct", "unique occurrences".

#### 2. How It Works

```text
[3, 1, 3, 2, 1]
HashSet        → {1, 2, 3}  (order not guaranteed)
LinkedHashSet  → [3, 1, 2]  (first-seen order)
TreeSet        → [1, 2, 3]  (sorted)
distinct count → 3
```

**Third Maximum Number (LeetCode 414).** Return the third **distinct** maximum, or the maximum if there are fewer than 3 distinct values. Keep a set of at most **3** values, and drop the smallest when it grows past 3.

```text
[2, 2, 3, 1]
add 2 → {2}    add 2 → {2}    add 3 → {2, 3}    add 1 → {1, 2, 3}
size is 3 → the smallest, 1, is the third maximum
```

**Single Number (LeetCode 136).** Every value appears twice except one. With a set: `2 × (sum of the distinct values) − (sum of all values)` gives the single one. (The XOR trick is `O(1)` space.)

```text
[4, 1, 2, 1, 2]:  distinct {4, 1, 2} sum 7  →  2×7 − 10 = 4
```

**Unique Number of Occurrences (LeetCode 1207).** Count each value's occurrences. Put the counts in a set. If the set has the same size as the number of counts, all counts are distinct.

```text
[1, 2, 2, 1, 1, 3]: counts {1: 3, 2: 2, 3: 1} → counts 3, 2, 1 are all different → true
[1, 2]:             counts {1: 1, 2: 1}       → set {1} is smaller than 2 → false
```

#### 3. Brute Force vs Optimized

| Task | Brute force | Optimized |
|---|---|---|
| Distinct values | nested loops `O(n²)` | set `O(n)` |
| Remove duplicates keeping order | `list.contains` check `O(n²)` | `LinkedHashSet` `O(n)` |
| Single number | count each value `O(n²)` | set formula `O(n)`, XOR `O(n)` and `O(1)` space |
| Third maximum | sort descending, skip duplicates `O(n log n)` | set of 3 `O(n)` |

```kotlin
// Brute force: unique with a list and a scan
fun uniqueBrute(nums: IntArray): List<Int> {
    val out = mutableListOf<Int>()
    for (x in nums) if (!out.contains(x)) out.add(x)       // O(n) scan each time
    return out
}
```

#### 4. Kotlin Code

```kotlin
import java.util.TreeSet

// Remove duplicates, keep the first-seen order
fun removeDuplicatesKeepOrder(nums: IntArray): List<Int> = LinkedHashSet(nums.toList()).toList()

// Third Maximum Number (LeetCode 414)
fun thirdMax(nums: IntArray): Int {
    val top = TreeSet<Int>()
    for (x in nums) {
        top.add(x)
        if (top.size > 3) top.pollFirst()                   // drop the smallest
    }
    return if (top.size == 3) top.first() else top.last()
}

// Single Number (LeetCode 136) with a set (the XOR version is shown in the Bit Manipulation notes)
fun singleNumber(nums: IntArray): Int {
    val distinct = nums.toHashSet()
    return (2 * distinct.sumOf { it.toLong() } - nums.sumOf { it.toLong() }).toInt()
}

// Unique Number of Occurrences (LeetCode 1207)
fun uniqueOccurrences(arr: IntArray): Boolean {
    val count = HashMap<Int, Int>()
    for (x in arr) count[x] = (count[x] ?: 0) + 1
    return count.values.toHashSet().size == count.size
}
```

Checks: `removeDuplicatesKeepOrder(intArrayOf(3, 1, 3, 2, 1))` → `[3, 1, 2]`. `uniqueBrute(intArrayOf(3, 1, 3, 2, 1))` → `[3, 1, 2]`. `thirdMax(intArrayOf(3, 2, 1))` → `1`. `thirdMax(intArrayOf(1, 2))` → `2`. `thirdMax(intArrayOf(2, 2, 3, 1))` → `1`. `singleNumber(intArrayOf(4, 1, 2, 1, 2))` → `4`. `singleNumber(intArrayOf(2, 2, 1))` → `1`. `uniqueOccurrences(intArrayOf(1, 2, 2, 1, 1, 3))` → `true`. `uniqueOccurrences(intArrayOf(1, 2))` → `false`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Distinct / dedupe | `O(n)` | `O(n)` |
| Third maximum (`TreeSet` of size 3) | `O(n)` (each op on 3 items) | `O(1)` |
| Single number (set) | `O(n)` | `O(n)` |
| Unique occurrences | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Third Maximum:** counting duplicates (`[2, 2, 3, 1]` has 3 distinct values, not 4 items).
2. **Third Maximum:** returning the third item of a sorted array (includes duplicates).
3. **Single Number:** overflowing `Int` in the sum formula. Use `Long`.
4. **Using `HashSet` when order matters** (use `LinkedHashSet`).
5. **Comparing the set size to the array size** in Unique Occurrences (compare to the number of **distinct values**).
6. **Forgetting an empty array** or one element.

#### 7. Say This in the Interview

1. "A set keeps one copy of each value, so the number of distinct values is the set's size, in `O(n)`."
2. "If the order of first appearance matters, I use a `LinkedHashSet`. If I need them sorted, a `TreeSet`."
3. "For the third maximum I keep a sorted set of at most three values, so it's `O(n)` time and `O(1)` space."

#### 8. Quick Check

1. Distinct count of `[1, 1, 2, 2, 3]`?
2. Third maximum of `[5, 5]`?
3. `uniqueOccurrences([1, 1, 2, 2])`?

<details>
<summary>Answers</summary>

1. `3`.
2. `5` (fewer than 3 distinct values, so return the maximum).
3. `false` (both values occur twice).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy) | set |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) (Easy) | set formula or XOR |
| 414 | [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) (Easy) | set of at most 3 |
| 1207 | [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) (Easy) | counts, then a set |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) (Easy) | two pointers, in place |
| 349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) (Easy) | unique common values |
