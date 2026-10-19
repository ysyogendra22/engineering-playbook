# Set Union / Intersection / Difference

#### 1. Definition — Must Know

1. **Union** — all values that are in `A` **or** `B` (or both).
2. **Intersection** — values that are in `A` **and** `B`.
3. **Difference** — values that are in `A` **but not** in `B`.
4. **Symmetric difference** — values that are in one set **but not both**.
5. Kotlin gives you these as ready-made functions: `union`, `intersect`, `subtract`.

#### 2. Why It Is Used — Must Know

1. They turn "compare two groups" tasks into one line of code.
2. They answer common questions: what is new, what was removed, what is shared.
3. In apps: sync local and remote items, find added or removed permissions, compare two lists of ids.

#### 3. How It Works — Must Know

```text
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

Union (A ∪ B)               {1, 2, 3, 4, 5, 6}
Intersection (A ∩ B)        {3, 4}
Difference (A − B)          {1, 2}          in A, not in B
Difference (B − A)          {5, 6}
Symmetric difference        {1, 2, 5, 6}    (A − B) ∪ (B − A)
```

```text
   A only      both      B only
  {1, 2}      {3, 4}     {5, 6}
```

#### 4. Core Concepts — Must Know

| Operation | Kotlin | Result type | Changes the original? |
|---|---|---|---|
| Union | `a union b` or `a + b` | `Set` | No |
| Intersection | `a intersect b` | `Set` | No |
| Difference | `a subtract b` or `a - b` | `Set` | No |
| Symmetric difference | `(a - b) + (b - a)` | `Set` | No |
| Subset check | `b.containsAll(a)` | `Boolean` | No |
| Disjoint check | `a.none { it in b }` | `Boolean` | No |
| In-place union | `a.addAll(b)` | `Boolean` | **Yes** |
| In-place intersection | `a.retainAll(b)` | `Boolean` | **Yes** |
| In-place difference | `a.removeAll(b)` | `Boolean` | **Yes** |

1. The first group builds a **new** collection. The last three **change** the set.
2. For `O(1)` lookups inside these operations, the argument should also be a set. Passing a `List` makes some operations `O(n × m)`.
3. The result of `intersect` keeps the order of `a`.

#### 5. Algorithm — Must Know

```text
union:        result = copy of A;  add every item of B
intersection: result = items of A that are in B
difference:   result = items of A that are not in B
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val a = setOf(1, 2, 3, 4)
val b = setOf(3, 4, 5, 6)

println(a union b)               // [1, 2, 3, 4, 5, 6]
println(a intersect b)           // [3, 4]
println(a subtract b)            // [1, 2]
println((a - b) + (b - a))       // [1, 2, 5, 6]  symmetric difference
println(setOf(3, 4).let { b.containsAll(it) })   // true — {3, 4} is a subset of b

// In place (needs a MutableSet)
val x = hashSetOf(1, 2, 3)
x.addAll(listOf(3, 4))           // x = {1, 2, 3, 4}
x.retainAll(setOf(2, 3, 4))      // x = {2, 3, 4}
x.removeAll(setOf(4))            // x = {2, 3}
```

**Find the Difference of Two Arrays** (LeetCode 2215)

```kotlin
fun findDifference(nums1: IntArray, nums2: IntArray): List<List<Int>> {
    val a = nums1.toSet()
    val b = nums2.toSet()
    return listOf((a - b).toList(), (b - a).toList())
}
```

**What changed between two lists of ids? (typical app code)**

```kotlin
fun diff(oldIds: List<Int>, newIds: List<Int>): Triple<Set<Int>, Set<Int>, Set<Int>> {
    val old = oldIds.toSet()
    val new = newIds.toSet()
    val added = new - old
    val removed = old - new
    val kept = old intersect new
    return Triple(added, removed, kept)
}
```

#### 7. Time & Space Complexity — Must Know

For sets of size `n` and `m`:

| Operation | Time | Extra space |
|---|---:|---:|
| Union | `O(n + m)` | `O(n + m)` |
| Intersection | `O(n + m)` (about `O(min(n, m))` if you loop over the smaller set) | `O(min(n, m))` |
| Difference | `O(n + m)` | `O(n)` |
| Subset check | `O(n)` | `O(1)` |
| In-place `addAll` | `O(m)` | `O(1)` extra |

Converting a list to a set first costs `O(n)`.

#### 8. Common Set-Operation Patterns — Must Know

1. **Added / removed / unchanged** between two snapshots.
2. **Common elements** (Intersection of Two Arrays).
3. **Find the Difference of Two Arrays** (LeetCode 2215).
4. **Permissions needed minus permissions granted** — what to request.
5. **Is the second a subset of the first?** — `containsAll`.
6. **Disjoint check** — do two groups share nothing?
7. **Android example:** `DiffUtil` style logic for lists, or syncing selected item ids with new data.

#### 9. Edge Cases / Common Mistakes

1. Using these on lists with duplicates and expecting multiset results. Sets drop repeats.
2. Mixing up `a - b` and `b - a`.
3. Using in-place functions on a read-only `Set`. It will not compile.
4. Changing a set while another variable still expects the old content.
5. Expecting `a + b` on a `List` to work like union. For lists, `+` just joins them.
6. Forgetting that `retainAll` removes everything if the argument is empty.
7. Passing a `List` as the argument for big data. Convert it to a set first.

#### 10. When to Use / When Not to Use

**Use when:**

1. You compare two groups of unique items.
2. You need added / removed / shared items.

**Avoid when:**

1. Duplicates matter (use counts in a map).
2. Order of the result must follow another list. Filter that list instead.

#### 11. Related Topics

1. Intersection / Common Elements
2. Unique Elements Pattern
3. HashSet Operations & Complexity
4. Collections in Kotlin (`03-leetcode-patterns`, topic 3)

#### 12. Interview Must Remember

1. **`union`, `intersect`, `subtract`** make new sets. `addAll`, `retainAll`, `removeAll` change the set.
2. `a - b` is not `b - a`. Symmetric difference = `(a - b) + (b - a)`.
3. Convert lists to sets first. Cost `O(n + m)`.
4. Sets lose duplicates. Use a map for counts.
