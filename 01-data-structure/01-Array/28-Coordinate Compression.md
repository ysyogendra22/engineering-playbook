# Coordinate Compression

> A helper technique. It is rare as a question by itself, but it unlocks arrays with huge values.

#### 1. What Is It?

**Coordinate compression** replaces big values with small **ranks** `0, 1, 2, ...`, keeping the **order** the same.

```text
values: [100, 5, 1000000, 5, 42]
sorted distinct: [5, 42, 100, 1000000]
ranks:  [2, 0, 3, 0, 1]
```

Why it is used: some tools (a counting array, a Fenwick tree / BIT, a segment tree) need small indexes like `0 .. m-1`. If the values go up to `10⁹`, you cannot make an array that big. Compress first, then use the small ranks.

How to spot it: huge values but only the **relative order** matters, "rank of each element", "count smaller elements after self" (with a BIT), offline range queries.

#### 2. How It Works

Steps:

1. Copy the values and **sort** them.
2. **Remove duplicates**.
3. The rank of a value is its position in the sorted distinct list. Find it with a **map** (`value → rank`) or **binary search**.

Same equal values get the same rank. Different values keep their order: if `a < b` then `rank(a) < rank(b)`.

```text
Rank Transform of an Array (LeetCode 1331): [40, 10, 20, 30]
sorted distinct: [10, 20, 30, 40]  →  ranks start at 1: 10→1, 20→2, 30→3, 40→4
answer [4, 1, 2, 3]
```

#### 3. Brute Force vs Optimized

| | Brute force | Coordinate compression |
|---|---|---|
| Idea | use the values directly (array of size `max`) | map to ranks, array of size `m` |
| Memory | `O(max value)` (can be 10⁹) | `O(n)` |
| Time | — | `O(n log n)` for the sort |

```kotlin
// Brute force idea: a count array indexed by the value. It fails when values are up to 10^9.
fun countsByValue(nums: IntArray): IntArray {
    val counts = IntArray(nums.max() + 1)          // huge if the values are huge (Kotlin 1.7+)
    for (x in nums) counts[x]++
    return counts
}
```

#### 4. Kotlin Code

```kotlin
// Ranks with a map (starting from 0)
fun compress(nums: IntArray): IntArray {
    val sortedDistinct = nums.distinct().sorted()
    val rank = HashMap<Int, Int>()
    for ((i, v) in sortedDistinct.withIndex()) rank[v] = i
    return IntArray(nums.size) { rank.getValue(nums[it]) }
}

// Ranks with binary search (no map)
fun compressBinary(nums: IntArray): IntArray {
    val sortedDistinct = nums.distinct().sorted().toIntArray()
    return IntArray(nums.size) { java.util.Arrays.binarySearch(sortedDistinct, nums[it]) }
}

// Rank Transform of an Array (LeetCode 1331): ranks start from 1
fun arrayRankTransform(arr: IntArray): IntArray {
    val sortedDistinct = arr.distinct().sorted()
    val rank = HashMap<Int, Int>()
    for ((i, v) in sortedDistinct.withIndex()) rank[v] = i + 1
    return IntArray(arr.size) { rank.getValue(arr[it]) }
}

// Relative Ranks (LeetCode 506): "Gold Medal", "Silver Medal", "Bronze Medal", then the place number
fun findRelativeRanks(score: IntArray): Array<String> {
    val order = score.indices.sortedByDescending { score[it] }       // indexes, best score first
    val result = Array(score.size) { "" }
    for ((place, index) in order.withIndex()) {
        result[index] = when (place) {
            0 -> "Gold Medal"
            1 -> "Silver Medal"
            2 -> "Bronze Medal"
            else -> (place + 1).toString()
        }
    }
    return result
}

// Idea only: after compression, a Fenwick tree (BIT) over ranks can count "how many smaller values appeared before".
```

Checks: `compress([100, 5, 1000000, 5, 42])` → `[2, 0, 3, 0, 1]`. `arrayRankTransform([40,10,20,30])` → `[4,1,2,3]`. `findRelativeRanks([10,3,8,9,4])` → `["Gold Medal","5","Bronze Medal","Silver Medal","4"]`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Sort + dedupe | `O(n log n)` | `O(n)` |
| Ranks via a map | `O(n)` | `O(n)` |
| Ranks via binary search | `O(n log n)` | `O(n)` |

#### 6. Common Mistakes

1. **Not removing duplicates** before ranking (equal values get different ranks).
2. **Ranks starting at 0 vs 1.** Read the question.
3. **Using it when the actual values matter** (sums), not just their order.
4. **Sorting the original array in place** and losing the original order. Sort a copy.
5. **Using `Int` subtraction** to compare big numbers (overflow). Use `compareTo`.

#### 7. Say This in the Interview

1. "The values are huge but only their order matters, so I compress them to ranks `0..m−1`. Then I can use an array or a Fenwick tree."
2. "Sorting the distinct values costs `O(n log n)`."

#### 8. Quick Check

1. What are the ranks of `[7, 3, 7, 10]` (starting at 0)?
2. Does compression keep equal values equal?

<details>
<summary>Answers</summary>

1. `[1, 0, 1, 2]`.
2. Yes. Equal values get the same rank.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 506 | [Relative Ranks](https://leetcode.com/problems/relative-ranks/) (Easy) | rank by sorted order |
| 1331 | [Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) (Easy) | the base problem |
| 315 | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) (Hard) | compress + Fenwick tree |
| 327 | [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) (Hard) | compress prefix sums |
