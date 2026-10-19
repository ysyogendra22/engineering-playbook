# Unique Elements Pattern

#### 1. Definition — Must Know

1. The **unique elements pattern** uses a set to **keep only one copy of each value**, or to **count how many different values** there are.
2. A set removes duplicates automatically.
3. Use `LinkedHashSet` (or `distinct()`) if you want to keep the **original order**.

#### 2. Why It Is Used — Must Know

1. "How many distinct values?" is a very common question.
2. It is the building block for many checks: "are all counts different?", "is every value unique?".
3. In app code it removes repeated items from a list before showing it.

#### 3. How It Works — Must Know

`[3, 1, 3, 2, 1]`

```text
HashSet:        {1, 2, 3}     (order not guaranteed)  → size 3
LinkedHashSet:  [3, 1, 2]     (first-seen order)      → size 3
```

Example: *Unique Number of Occurrences* (LeetCode 1207). Are the occurrence counts of all values different?

```text
arr = [1, 2, 2, 1, 1, 3]

count of each value:   1 → 3,  2 → 2,  3 → 1
set of counts:         {3, 2, 1}     size 3 == number of values 3  → all different → true
```

#### 4. Core Concepts — Must Know

1. **Distinct count = `set.size`.**
2. **Keep order:** `list.distinct()` or `toCollection(LinkedHashSet())`. `distinct()` keeps the first occurrence.
3. **Distinct by a field:** `list.distinctBy { it.id }`.
4. **Compare sizes:** `set.size == list.size` means every item was already unique.
5. **Set of a derived value:** put counts, lengths, sums or keys into the set, not only the items.

| Need | Kotlin |
|---|---|
| Unique values (any order) | `toHashSet()` |
| Unique values, keep order | `distinct()` or `toSet()` |
| Unique by property | `distinctBy { it.prop }` |
| Count unique | `toSet().size` |

#### 5. Algorithm — Must Know

```text
set = empty
for each item: set.add(derive(item))
answer = set.size   (or the set itself)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Distinct values, original order kept
val unique = listOf(3, 1, 3, 2, 1).distinct()          // [3, 1, 2]

// Count distinct
fun countDistinct(nums: IntArray): Int = nums.toHashSet().size

// Unique Number of Occurrences
fun uniqueOccurrences(arr: IntArray): Boolean {
    val count = HashMap<Int, Int>()
    for (n in arr) count[n] = (count[n] ?: 0) + 1
    return count.values.toHashSet().size == count.size
}

// Distinct by a field
data class User(val id: Int, val name: String)
val users = listOf(User(1, "Asha"), User(2, "Ben"), User(1, "Asha K"))
val uniqueUsers = users.distinctBy { it.id }            // keeps the first user with each id

// Missing Number (0..n) with a set
fun missingNumber(nums: IntArray): Int {
    val set = nums.toHashSet()
    for (i in 0..nums.size) if (i !in set) return i
    return -1
}

// Single Number (one value appears once, the others twice) — set toggle
fun singleNumber(nums: IntArray): Int {
    val set = HashSet<Int>()
    for (n in nums) if (!set.add(n)) set.remove(n)
    return set.first()
}
```

`singleNumber` has a better `O(1)` space answer using XOR: `nums.reduce { a, b -> a xor b }`.

#### 7. Time & Space Complexity — Must Know

| Task | Time | Space |
|---|---:|---:|
| Build the set | `O(n)` | `O(u)` |
| `distinct()` | `O(n)` | `O(u)` |
| `distinctBy` | `O(n)` | `O(u)` |

`u` = number of unique values (at most `n`).

#### 8. Common Unique Patterns — Must Know

1. **Count distinct values.**
2. **Remove duplicates but keep order** — `distinct()`.
3. **Check all values are different** — `set.size == list.size`.
4. **Unique Number of Occurrences** (LeetCode 1207) — a set of counts.
5. **Intersection of Two Arrays** (LeetCode 349) — unique common values.
6. **Missing Number**, **Single Number** — sets (with a better XOR or math answer).
7. **Number of distinct results** — distinct sums, distinct substrings, distinct states.

#### 9. Edge Cases / Common Mistakes

1. Expecting `HashSet` to keep input order.
2. `distinctBy` keeps the **first** item for each key, so the rest are lost. Check this is what you want.
3. Using `distinct()` on arrays of arrays. Inner arrays compare by reference.
4. Using floating-point numbers as set items. `0.1 + 0.2` is not `0.3`. `NaN` equals itself in a set, and `0.0` and `-0.0` are different.
5. Converting to a set when you needed the counts. Use a map.
6. Not handling an empty input (the size is `0`).

#### 10. When to Use / When Not to Use

**Use when:**

1. You need uniqueness or the number of different values.

**Avoid when:**

1. You need how many times each appeared. Use a `HashMap`.
2. You need the values sorted. Use `sorted().distinct()` or a `TreeSet`.

#### 11. Related Topics

1. Duplicate Detection
2. HashSet vs HashMap
3. Intersection / Common Elements
4. HashSet with Custom Objects

#### 12. Interview Must Remember

1. **Distinct count = `set.size`.**
2. `distinct()` and `LinkedHashSet` keep first-seen order. `HashSet` does not.
3. `distinctBy { it.id }` for objects.
4. Need counts → map, not a set.
