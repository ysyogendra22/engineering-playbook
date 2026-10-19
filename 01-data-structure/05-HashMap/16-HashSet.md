# HashSet

#### 1. Definition — Must Know

1. A **HashSet** is a collection of **unique values** with `O(1)` average `add`, `contains` and `remove`.
2. It is the **keys-only** cousin of a HashMap. Java's `HashSet` is built on a `HashMap`, where each value is a dummy object.
3. This note is the short view from the HashMap side. The full HashSet notes are in `01-data-structure/06-HashSet`.

#### 2. Why It Is Used — Must Know

1. When you only need "have I seen this?", a set is simpler and lighter than a map.
2. It removes duplicates and gives fast membership checks.
3. Many map solutions can be simplified to a set when counts or indices are not needed.

#### 3. How It Works — Must Know

```text
HashSet<String> = HashMap<String, DUMMY>

add("apple")      →  map.put("apple", DUMMY)       returns true if the key was new
contains("apple") →  map.containsKey("apple")
remove("apple")   →  map.remove("apple")
```

```text
set:  {apple, pear}           same as map keys  {apple → ·, pear → ·}
```

#### 4. Core Concepts — Must Know

1. **Unique values only.** Adding an existing value does nothing and returns `false`.
2. **Same rules as map keys:** correct `equals()` / `hashCode()`, no arrays, no mutation.
3. **Same speed:** `O(1)` average.
4. **Same order rules:** `HashSet` none, `LinkedHashSet` insertion order, `TreeSet` sorted.
5. **Convert both ways:**

| From | To | Code |
|---|---|---|
| list | set | `list.toHashSet()` |
| map | its keys as a set | `map.keys` |
| set | map with a default | `set.associateWith { 0 }` |

6. **Set operations:** `union`, `intersect`, `subtract` (`01-data-structure/06-HashSet/12`).

#### 5. Algorithm — Must Know

```text
seen = empty set
for each item:
    if seen.add(item) is false → duplicate
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val set = HashSet<Int>()
println(set.add(5))          // true  (new)
println(set.add(5))          // false (already there)
println(5 in set)            // true
set.remove(5)

val unique = listOf(3, 1, 3, 2).toHashSet()      // {1, 2, 3}
val keysOnly: Set<String> = hashMapOf("a" to 1, "b" to 2).keys

// Contains Duplicate
fun containsDuplicate(nums: IntArray): Boolean {
    val seen = HashSet<Int>()
    for (n in nums) if (!seen.add(n)) return true
    return false
}
```

#### 7. Time & Space Complexity — Must Know

| Operation | Average |
|---|---:|
| `add` | `O(1)` |
| `contains` | `O(1)` |
| `remove` | `O(1)` |
| Space | `O(n)` (less than a map, because there are no values) |

#### 8. Common HashSet Patterns — Must Know

1. **Duplicate detection.**
2. **Fast membership / lookup.**
3. **Unique elements and distinct counts.**
4. **Longest Consecutive Sequence.**
5. **Visited / seen in BFS and DFS.**
6. **Sliding window with unique items.**

All are explained in `01-data-structure/06-HashSet`.

#### 9. Edge Cases / Common Mistakes

1. Using a `HashMap<K, Boolean>` when a `HashSet<K>` is enough.
2. Using a set when counts are needed.
3. Expecting insertion order from `HashSet`.
4. Putting arrays or mutable objects in a set.
5. Removing from a set while looping over it.
6. Forgetting that `mutableSetOf()` is a `LinkedHashSet`.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need only existence or uniqueness.

**Use a map when:**

1. You need counts, indices, or other data per key.

#### 11. Related Topics

1. HashMap vs HashSet
2. Duplicate Detection
3. HashSet Fundamentals (`01-data-structure/06-HashSet/01-HashSet Fundamentals.md`)
4. HashMap Fundamentals

#### 12. Interview Must Remember

1. **A set is a map without values.** Existence only.
2. `add` returns `false` for a duplicate.
3. Same key rules as a map: `equals`, `hashCode`, immutability.
4. Need counts or indices → use a `HashMap`.
