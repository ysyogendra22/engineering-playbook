# Duplicate Detection

#### 1. Definition — Must Know

1. **Duplicate detection** means finding out whether a value appears **more than once**.
2. With a HashSet: go through the items, and if `add` returns `false`, you found a duplicate.
3. The classic problem is *Contains Duplicate* (LeetCode 217). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is the most common HashSet interview question.
2. It shows the jump from `O(n²)` to `O(n)` clearly.
3. It appears in real code: duplicate user IDs, repeated requests, repeated list items.

#### 3. How It Works — Must Know

`nums = [1, 2, 3, 1]`

```text
seen = {}
see 1 → add → true  (new)       seen = {1}
see 2 → add → true              seen = {1, 2}
see 3 → add → true              seen = {1, 2, 3}
see 1 → add → false (already!)  → duplicate found → return true
```

Three ways to solve it:

| Approach | Idea | Time | Space |
|---|---|---:|---:|
| Brute force | Compare every pair | `O(n²)` | `O(1)` |
| Sort | Sort, then check neighbours | `O(n log n)` | `O(1)`–`O(n)` |
| **HashSet** | Remember what you have seen | **`O(n)`** | `O(n)` |

#### 4. Core Concepts — Must Know

1. **`add()` returning `false` is the duplicate signal.** No need for `contains` first.
2. **Stop early.** Return as soon as you find the first duplicate.
3. **Sorting is a good alternative** when memory is limited: after sorting, equal values sit next to each other.
4. **Size trick:** `set.size < list.size` means at least one duplicate exists. It is short but always processes everything.
5. Choose the data to remember: the whole value, a key (like an id), or a hash of a big object.

#### 5. Algorithm — Must Know

```text
seen = empty set
for each item in the input:
    if seen.add(item) is false:
        return true          // duplicate
return false
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Contains Duplicate — early exit
fun containsDuplicate(nums: IntArray): Boolean {
    val seen = HashSet<Int>()
    for (n in nums) {
        if (!seen.add(n)) return true
    }
    return false
}

// One-liner (processes the whole array)
fun containsDuplicateShort(nums: IntArray): Boolean =
    nums.toHashSet().size != nums.size
```

**Sort version (no extra set)**

```kotlin
fun containsDuplicateSorted(nums: IntArray): Boolean {
    val sorted = nums.sortedArray()
    for (i in 1 until sorted.size) {
        if (sorted[i] == sorted[i - 1]) return true
    }
    return false
}
```

**Find the first duplicate value**

```kotlin
fun firstDuplicate(nums: IntArray): Int? {
    val seen = HashSet<Int>()
    for (n in nums) if (!seen.add(n)) return n
    return null
}
```

**Find all duplicates**

```kotlin
fun allDuplicates(nums: IntArray): Set<Int> {
    val seen = HashSet<Int>()
    val dups = LinkedHashSet<Int>()
    for (n in nums) if (!seen.add(n)) dups.add(n)
    return dups
}
```

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| HashSet | `O(n)` | `O(n)` |
| Sort + scan | `O(n log n)` | `O(1)` if sorted in place |
| Brute force | `O(n²)` | `O(1)` |

#### 8. Common Duplicate-Detection Patterns — Must Know

1. **Contains Duplicate** (LeetCode 217) — any duplicate anywhere.
2. **Contains Duplicate II** (LeetCode 219) — duplicates within distance `k`. Use a window set (see "HashSet + Sliding Window").
3. **Find the Duplicate Number** (LeetCode 287) — a set works in `O(n)` space. The `O(1)` space answer uses Floyd's cycle detection.
4. **Find All Duplicates in an Array** (LeetCode 442) — a set works. The `O(1)` space answer marks values using the array itself.
5. **First Repeating Character** — a set of `Char`.
6. **Detect duplicate objects** — use an id or a `data class` as the key.

#### 9. Edge Cases / Common Mistakes

1. Empty or single-element input. The answer is `false`.
2. Using `contains` and then `add`. It is two lookups for no reason.
3. Not stopping early on the first duplicate.
4. Putting `IntArray`/`Array` items in the set. Duplicates are missed because arrays compare by reference.
5. Large input and memory limits. Mention the sort alternative.
6. Confusing "all values distinct" with "no value repeats within `k` positions".

#### 10. When to Use / When Not to Use

**Use a HashSet when:**

1. You need a fast answer and memory is fine.
2. Data comes as a stream and you cannot sort it.

**Use sorting when:**

1. Extra memory is a problem.
2. You are allowed to change or copy the array.

**Use a `BooleanArray`/`BitSet` when:**

1. Values are in a small known range, such as `0..n`.

#### 11. Related Topics

1. HashSet Fundamentals
2. Unique Elements Pattern
3. HashSet + Sliding Window
4. Sorting (`02-algorithm/01-sorting`)

#### 12. Interview Must Remember

1. **`if (!seen.add(x)) return true`.**
2. Hash set is `O(n)` time and space. Sort is `O(n log n)` with little space.
3. Say both options and the trade-off.
4. Windowed duplicates need a window set.
