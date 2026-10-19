# Duplicate Detection

#### 1. Definition — Must Know

1. **Duplicate detection** finds values that appear **more than once**.
2. A set answers "is there a duplicate?". A **HashMap** answers the richer questions: **how many times**, **where**, and **how far apart**.
3. This note covers the map versions. The set version is in `01-data-structure/06-HashSet/04-Duplicate Detection.md`.

#### 2. Why It Is Used — Must Know

1. Duplicates appear in real data: repeated ids, double taps, repeated requests, repeated list items.
2. Interviewers use it to test whether you pick the right structure for the question.
3. The map adds information a set cannot give.

#### 3. How It Works — Must Know

`nums = [4, 3, 2, 7, 8, 2, 3, 1]`

```text
count: {4:1, 3:2, 2:2, 7:1, 8:1, 1:1}
Values with count > 1:  2 and 3         ← all duplicates
Count of each duplicate: 2 → 2 times, 3 → 2 times
```

Which question needs which tool:

| Question | Tool |
|---|---|
| Is there any duplicate? | `HashSet` (`add` returns `false`) |
| Which values are duplicated? | count map, or two sets |
| How many times does each repeat? | count map |
| At which indices? | `value → list of indices` |
| Are two equal values within `k` positions? | `value → last index` |

#### 4. Core Concepts — Must Know

1. **Count map:** `count[x]++`; a value with count above 1 is a duplicate.
2. **Index map:** `value → last index` for "nearby duplicate" questions.
3. **Index list map:** `value → list of indices` to report all positions.
4. **Stop early** when you only need the first duplicate.
5. **Space-saving options:**
   - sort first and compare neighbours (`O(n log n)`, `O(1)` extra),
   - reuse the array itself as a marker when values are `1..n` (Find All Duplicates, LeetCode 442),
   - Floyd's cycle detection for *Find the Duplicate Number* (LeetCode 287).

#### 5. Algorithm — Must Know

```text
Count version:
count = empty map
for x in nums: count[x] += 1
duplicates = keys whose count > 1

Nearby version:
last = empty map
for i, x in nums:
    if x in last and i - last[x] <= k → true
    last[x] = i
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// All duplicate values with their counts
fun duplicateCounts(nums: IntArray): Map<Int, Int> =
    nums.toList().groupingBy { it }.eachCount().filterValues { it > 1 }

// All duplicate values in first-seen order (no count map)
fun findDuplicates(nums: IntArray): List<Int> {
    val seen = HashSet<Int>()
    val dups = LinkedHashSet<Int>()
    for (n in nums) if (!seen.add(n)) dups.add(n)
    return dups.toList()
}

// All positions of every duplicated value
fun duplicateIndices(nums: IntArray): Map<Int, List<Int>> {
    val positions = HashMap<Int, MutableList<Int>>()
    for ((i, x) in nums.withIndex()) positions.getOrPut(x) { mutableListOf() }.add(i)
    return positions.filterValues { it.size > 1 }
}

// Contains Duplicate II — duplicates within k positions
fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
    val last = HashMap<Int, Int>()
    for ((i, x) in nums.withIndex()) {
        val j = last[x]
        if (j != null && i - j <= k) return true
        last[x] = i
    }
    return false
}

// Find the Duplicate Number (values 1..n, one repeated) — O(1) space, Floyd's cycle
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

// Duplicate objects by key (app code)
data class Order(val id: Int, val total: Int)
val orders = listOf(Order(1, 10), Order(2, 20), Order(1, 10))
val duplicateIds = orders.groupBy { it.id }.filterValues { it.size > 1 }.keys   // {1}
```

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Count map | `O(n)` | `O(u)` |
| Index-list map | `O(n)` | `O(n)` |
| Last-index map (window question) | `O(n)` | `O(u)` |
| Sort + neighbours | `O(n log n)` | `O(1)`–`O(n)` |
| Floyd's cycle (Find the Duplicate Number) | `O(n)` | `O(1)` |

#### 8. Common Duplicate Patterns — Must Know

1. **Contains Duplicate** (LeetCode 217) — set.
2. **Contains Duplicate II** (LeetCode 219) — last-index map.
3. **Contains Duplicate III** (LeetCode 220) — value close within index distance; buckets or a `TreeSet`.
4. **Find All Duplicates in an Array** (LeetCode 442).
5. **Find the Duplicate Number** (LeetCode 287).
6. **Remove Duplicates from Sorted Array** (LeetCode 26) — two pointers.
7. **Duplicate emails / ids in app data** — `groupBy`.

#### 9. Edge Cases / Common Mistakes

1. Using a count map when a set is enough (extra memory).
2. Counting the whole array when the first duplicate is enough.
3. Wrong distance in the nearby version (`i - j <= k`).
4. Forgetting to update the last index after a non-match.
5. Duplicate keys that are arrays or mutable objects.
6. Calling a value a "duplicate" at count `1`. The test is `count > 1`.
7. Not saying the sorting or Floyd's alternatives when asked for `O(1)` space.
8. Floating-point values as keys.

#### 10. When to Use / When Not to Use

**Use a map when:**

1. You need counts, positions, or distances between duplicates.

**Use a set when:**

1. A yes/no answer is enough.

**Use sorting or Floyd's cycle when:**

1. Extra memory is limited.

#### 11. Related Topics

1. HashSet
2. Frequency Counting
3. Mapping / Index Tracking
4. Duplicate Detection — set version (`01-data-structure/06-HashSet/04-Duplicate Detection.md`)

#### 12. Interview Must Remember

1. **Yes/no → set. Counts, positions, distance → map.**
2. Nearby duplicates → `value → last index`.
3. `O(1)` space → sort, or Floyd's cycle for values `1..n`.
4. Stop at the first duplicate when that is all you need.
