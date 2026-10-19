# Intersection / Common Elements

#### 1. Definition — Must Know

1. The **intersection** of two collections is the set of values that appear in **both**.
2. With a HashSet: put one collection in a set, then keep the values from the other that are in that set.
3. The main problem is *Intersection of Two Arrays* (LeetCode 349). The version with repeats is *Intersection of Two Arrays II* (LeetCode 350). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is a common easy-level question that tests whether you reach for a set.
2. The brute force check (`O(n × m)`) becomes `O(n + m)`.
3. In apps: shared friends, common tags, overlapping permissions.

#### 3. How It Works — Must Know

`a = [1, 2, 2, 1]`, `b = [2, 2]`

```text
Step 1: setA = {1, 2}
Step 2: go through b:
        2 → in setA → add to result
        2 → in setA → already in result (result is a set) → no change
Step 3: result = {2}
```

With repeats (LeetCode 350) the answer is `[2, 2]` because `2` appears twice in **both** arrays. A set cannot count, so use a map of counts:

```text
count of a:  {1: 2, 2: 2}
go through b:
   2 → count 2 > 0 → add 2, count becomes 1
   2 → count 1 > 0 → add 2, count becomes 0
result = [2, 2]
```

#### 4. Core Concepts — Must Know

1. **Unique common values → HashSet.**
2. **Common values with repeats → HashMap of counts** (or sorted arrays and two pointers).
3. **Build the set from the smaller array** to save memory.
4. **Result as a set** removes repeated matches for free.
5. Kotlin already has `intersect`, which does the same work in one call.

| Version | Best approach | Time |
|---|---|---:|
| Unique common values | Two sets | `O(n + m)` |
| With repeats | Count map | `O(n + m)` |
| Both arrays sorted | Two pointers | `O(n + m)`, `O(1)` space |
| One array is huge, one is small | Set of the small one | `O(n + m)` |

#### 5. Algorithm — Must Know

```text
setA = set of array A
result = empty set
for each x in B:
    if x in setA → add x to result
return result
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Intersection of Two Arrays (unique values)
fun intersection(a: IntArray, b: IntArray): IntArray {
    val setA = a.toHashSet()
    val result = HashSet<Int>()
    for (x in b) if (x in setA) result.add(x)
    return result.toIntArray()
}

// Built-in
fun intersectionShort(a: IntArray, b: IntArray): IntArray =
    a.toSet().intersect(b.toSet()).toIntArray()
```

**Intersection II (repeats count)**

```kotlin
fun intersect(a: IntArray, b: IntArray): IntArray {
    val count = HashMap<Int, Int>()
    for (x in a) count[x] = (count[x] ?: 0) + 1

    val result = mutableListOf<Int>()
    for (x in b) {
        val c = count[x] ?: 0
        if (c > 0) {
            result.add(x)
            count[x] = c - 1
        }
    }
    return result.toIntArray()
}
```

**Both arrays sorted (two pointers, no extra map)**

```kotlin
fun intersectSorted(a: IntArray, b: IntArray): IntArray {
    var i = 0
    var j = 0
    val result = mutableListOf<Int>()
    while (i < a.size && j < b.size) {
        when {
            a[i] == b[j] -> { result.add(a[i]); i++; j++ }
            a[i] < b[j] -> i++
            else -> j++
        }
    }
    return result.toIntArray()
}
```

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Set | `O(n + m)` | `O(min(n, m))` if the smaller side is stored |
| Count map | `O(n + m)` | `O(n)` |
| Sorted + two pointers | `O(n + m)` | `O(1)` extra |
| Sort both first | `O(n log n + m log m)` | `O(1)` extra |
| Brute force | `O(n × m)` | `O(1)` |

#### 8. Common Intersection Patterns — Must Know

1. **Intersection of Two Arrays** (LeetCode 349) — sets.
2. **Intersection of Two Arrays II** (LeetCode 350) — counts, or sorted + two pointers.
3. **Common characters** across words (LeetCode 1002) — minimum counts per letter.
4. **Intersection of three arrays** — three sets, or count how many arrays contain each value.
5. **Find the difference of two arrays** (LeetCode 2215) — set minus set.
6. **Follow-ups:** "arrays are sorted" → two pointers. "One array is huge or on disk" → put the small one in memory.

#### 9. Edge Cases / Common Mistakes

1. Using a set when the answer needs repeats (LeetCode 350).
2. Forgetting to decrease the count in the map version, so extra repeats are added.
3. Returning duplicates in the unique version because the result was a list.
4. Empty arrays. The answer is empty.
5. Result order: a `HashSet` has no order. The problem usually allows any order.
6. Storing the larger array in the set when memory is a concern.

#### 10. When to Use / When Not to Use

**Use sets when:**

1. Only distinct common values are needed.

**Use a count map when:**

1. Repeats matter.

**Use two pointers when:**

1. Inputs are already sorted, or you want `O(1)` extra space.

#### 11. Related Topics

1. Set Union / Intersection / Difference
2. Unique Elements Pattern
3. HashSet + Two Pointers
4. HashSet vs HashMap

#### 12. Interview Must Remember

1. **Set of A, scan B, keep what is in the set.**
2. Repeats matter → count map. Sorted → two pointers.
3. `O(n + m)` time. Put the smaller array in the set.
4. `a.toSet().intersect(b.toSet())` is the Kotlin shortcut.
