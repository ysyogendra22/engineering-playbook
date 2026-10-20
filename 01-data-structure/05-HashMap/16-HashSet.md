# HashSet

> A short note from the HashMap side. The full HashSet notes are in `01-data-structure/06-HashSet`.

#### 1. What Is It?

A **HashSet** is a collection of **unique values**. It answers one question fast: **"is this value in the set?"**

It is a HashMap with **keys only** (no values). In Java, a `HashSet` is built on a `HashMap` where every value is a dummy object.

- `add(x)` returns `true` if `x` was new, and `false` if it was already there.
- `x in set` checks if `x` is inside.
- All are `O(1)` on average.

#### 2. How It Works

```text
HashSet<String>  =  HashMap<String, dummy>

add("apple")       →  put("apple", dummy)         returns true if the key was new
contains("apple")  →  containsKey("apple")
remove("apple")    →  remove("apple")
```

Same rules as map keys: correct `equals()` and `hashCode()`, no arrays, no changing items after adding them.

Types:

| Type | Order |
|---|---|
| `HashSet` / `hashSetOf()` | none |
| `LinkedHashSet` / `mutableSetOf()` | insertion order |
| `TreeSet` / `sortedSetOf()` | sorted, `O(log n)` |

#### 3. Kotlin Code

```kotlin
val set = HashSet<Int>()
println(set.add(5))            // true  (new)
println(set.add(5))            // false (already there)
println(5 in set)              // true
set.remove(5)

val unique = listOf(3, 1, 3, 2).toHashSet()          // {1, 2, 3}
val keysOnly: Set<String> = hashMapOf("a" to 1, "b" to 2).keys

// Contains Duplicate: add() returning false means a repeat
fun containsDuplicate(nums: IntArray): Boolean {
    val seen = HashSet<Int>()
    for (n in nums) if (!seen.add(n)) return true
    return false
}
```

#### 4. Complexity

| Action | Time |
|---|---|
| `add`, `contains`, `remove` | `O(1)` on average |
| Memory | `O(n)` (less than a map) |

#### 5. Common Mistakes

1. **Using `HashMap<K, Boolean>`** when a `HashSet<K>` is enough.
2. **Using a set when you need counts or indexes.** Use a map.
3. **Expecting insertion order** from `HashSet`.
4. **Arrays or mutable objects** inside a set.
5. **Removing from a set inside a `for` loop** over it.

#### 6. Say This in the Interview

1. "I only need to know if I have seen the value, so a `HashSet` is enough. A map would store values I never use."
2. "`add` returns `false` for a duplicate, so one call is both the check and the insert."

#### 7. Quick Check

1. What does `set.add(x)` return when `x` is already in the set?
2. When must you use a map instead of a set?

<details>
<summary>Answers</summary>

1. `false`.
2. When you need to store something with each key: a count, an index, or a list.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 217 | Contains Duplicate (Easy) | seen before? |
| 128 | Longest Consecutive Sequence (Medium) | set + start-of-run check |
| 349 | Intersection of Two Arrays (Easy) | two sets |
| 202 | Happy Number (Easy) | detect a loop with a set |
| 705 | Design HashSet (Easy) | buckets (note 26) |
