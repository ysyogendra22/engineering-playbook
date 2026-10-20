# Duplicate Detection

> The set version is in `01-data-structure/06-HashSet/04-Duplicate Detection.md`. This note covers the questions where a **map** is needed.

#### 1. What Is It?

Duplicate detection finds values that appear **more than once**.

| Question | Tool |
|---|---|
| Is there any duplicate? | `HashSet` (`add` returns `false`) |
| Which values repeat? How many times? | count map |
| At which positions? | `value → list of indexes` |
| Are two equal values within `k` positions? | `value → last index` |

#### 2. How It Works

`nums = [4, 3, 2, 7, 8, 2, 3, 1]`

```text
counts: {4:1, 3:2, 2:2, 7:1, 8:1, 1:1}
values with count > 1:  2 and 3        ← the duplicates
```

For "nearby duplicates" keep the **last index** of each value (note 10).

If extra memory is a problem there are two other tools:

- **Sort first**, then equal values sit next to each other (`O(n log n)`, little extra space).
- For *Find the Duplicate Number* (values `1..n`, one repeated), Floyd's cycle detection finds it in `O(1)` space.

#### 3. Kotlin Code

```kotlin
// Duplicate values with their counts
fun duplicateCounts(nums: IntArray): Map<Int, Int> =
    nums.toList().groupingBy { it }.eachCount().filterValues { it > 1 }

// Duplicate values in first-seen order (no count map)
fun findDuplicates(nums: IntArray): List<Int> {
    val seen = HashSet<Int>()
    val dups = LinkedHashSet<Int>()
    for (n in nums) if (!seen.add(n)) dups.add(n)
    return dups.toList()
}

// All positions of every repeated value
fun duplicateIndexes(nums: IntArray): Map<Int, List<Int>> {
    val positions = HashMap<Int, MutableList<Int>>()
    for ((i, x) in nums.withIndex()) positions.getOrPut(x) { mutableListOf() }.add(i)
    return positions.filterValues { it.size > 1 }
}

// Contains Duplicate II: equal values at most k positions apart
fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
    val last = HashMap<Int, Int>()
    for ((i, x) in nums.withIndex()) {
        val j = last[x]
        if (j != null && i - j <= k) return true
        last[x] = i
    }
    return false
}

// Find the Duplicate Number: O(1) space with Floyd's cycle detection
fun findDuplicate(nums: IntArray): Int {
    var slow = nums[0]
    var fast = nums[0]
    do {
        slow = nums[slow]
        fast = nums[nums[fast]]
    } while (slow != fast)
    slow = nums[0]
    while (slow != fast) {
        slow = nums[slow]
        fast = nums[fast]
    }
    return slow
}
```

Check: `findDuplicate([1,3,4,2,2])` → `2`.

#### 4. Complexity

| Way | Time | Space |
|---|---|---|
| Count map | `O(n)` | `O(u)` |
| Index-list map | `O(n)` | `O(n)` |
| Last-index map | `O(n)` | `O(u)` |
| Sort and compare neighbours | `O(n log n)` | `O(1)` extra |
| Floyd's cycle (values `1..n`) | `O(n)` | `O(1)` |

`u` = number of different values.

#### 5. Common Mistakes

1. **Using a count map** when a set is enough (more memory).
2. **Calling something a duplicate at count `1`.** The test is `count > 1`.
3. **Wrong distance** in the nearby version. It is `i - j <= k`.
4. **Forgetting to update the last index** when there is no match.
5. **Not mentioning** the sort or Floyd's alternatives when asked for `O(1)` space.

#### 6. Say This in the Interview

1. "A yes/no question needs only a set. Counts, positions or distances need a map."
2. "For duplicates within `k` positions I keep the last index of each value."
3. "If memory is limited I can sort first, or for values `1..n` use Floyd's cycle detection."

#### 7. Quick Check

1. Which structure tells you **where** duplicates are?
2. Which keeps the closest earlier equal value?

<details>
<summary>Answers</summary>

1. A map from value to a list of indexes.
2. A map from value to its **last** index.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 217 | Contains Duplicate (Easy) | set |
| 219 | Contains Duplicate II (Easy) | last-index map |
| 220 | Contains Duplicate III (Hard) | buckets or `TreeSet` |
| 287 | Find the Duplicate Number (Medium) | Floyd's cycle |
| 442 | Find All Duplicates in an Array (Medium) | mark values inside the array |
