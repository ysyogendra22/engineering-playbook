# Grouping Pattern

#### 1. Definition — Must Know

1. The **grouping pattern** puts items that share a property under the **same key**.
2. The map is `key → list of items`.
3. The key is a value you compute from each item (its length, first letter, sorted letters, date, category).

#### 2. Why It Is Used — Must Know

1. It organizes data in one pass (`O(n)`) instead of repeated filtering.
2. It is the base of Group Anagrams, bucket problems, and "section headers" in lists.
3. In apps: group chat messages by date, contacts by first letter, products by category.

#### 3. How It Works — Must Know

Group words by length: `["hi", "yo", "hello", "world", "ok"]`

```text
key = word.length

"hi"    → key 2   {2: [hi]}
"yo"    → key 2   {2: [hi, yo]}
"hello" → key 5   {2: [hi, yo], 5: [hello]}
"world" → key 5   {2: [hi, yo], 5: [hello, world]}
"ok"    → key 2   {2: [hi, yo, ok], 5: [hello, world]}
```

The important step: **if the key is new, create an empty list first**, then add the item. `getOrPut` does both.

#### 4. Core Concepts — Must Know

1. **Choose the key.** The key is the "same group" rule.
2. **`getOrPut(key) { mutableListOf() }.add(item)`** is the standard line.
3. **`groupBy { key }`** does the whole job for a collection.
4. **Group count only?** Use `groupingBy { key }.eachCount()` or a count map.
5. **Group, then use:** sort inside groups, take the largest group, count groups (`map.size`).
6. **Related Kotlin helpers:**

| Helper | Result |
|---|---|
| `groupBy { key }` | `Map<K, List<T>>` (lists of all items) |
| `associateBy { key }` | `Map<K, T>` (one item per key, the **last** wins) |
| `groupingBy { key }.eachCount()` | `Map<K, Int>` |
| `partition { condition }` | two lists (true / false) |

#### 5. Algorithm — Must Know

```text
groups = empty map
for each item:
    key = computeKey(item)
    groups[key] (create an empty list if missing).add(item)
return groups
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Manual grouping by length
fun groupByLength(words: List<String>): Map<Int, List<String>> {
    val groups = HashMap<Int, MutableList<String>>()
    for (w in words) {
        groups.getOrPut(w.length) { mutableListOf() }.add(w)
    }
    return groups
}

// Built-in
val byLength = listOf("hi", "yo", "hello", "world", "ok").groupBy { it.length }
// {2=[hi, yo, ok], 5=[hello, world]}

// Group objects
data class Message(val date: String, val text: String)
val messages = listOf(Message("Mon", "Hi"), Message("Tue", "Yo"), Message("Mon", "Bye"))
val byDate = messages.groupBy { it.date }          // {Mon=[Hi, Bye], Tue=[Yo]}

// Group and transform the values
val textsByDate = messages.groupBy({ it.date }, { it.text })   // {Mon=[Hi, Bye], Tue=[Yo]}

// Group indices (Group the People Given the Group Size They Belong To — idea)
fun groupIndicesByValue(nums: IntArray): Map<Int, List<Int>> {
    val groups = HashMap<Int, MutableList<Int>>()
    for ((i, n) in nums.withIndex()) groups.getOrPut(n) { mutableListOf() }.add(i)
    return groups
}

// Largest group
val biggest = byLength.maxByOrNull { it.value.size }?.key
```

#### 7. Time & Space Complexity — Must Know

| Part | Time | Space |
|---|---:|---:|
| Group `n` items with an `O(1)` key | `O(n)` | `O(n)` |
| Group `n` strings of length `k`, key = sorted letters | `O(n · k log k)` | `O(n · k)` |
| Group with a count key (26 counts) | `O(n · k)` | `O(n · k)` |

The cost of the **key** is the main variable. A simple key is `O(1)`; a key built from a string costs `O(k)` or more.

#### 8. Common Grouping Patterns — Must Know

1. **Group Anagrams** (LeetCode 49) — key = sorted letters (next topic).
2. **Group by property** — length, first letter, parity, remainder.
3. **Group Shifted Strings** (LeetCode 249, premium) — key = pattern of differences.
4. **Group the People Given the Group Size** (LeetCode 1282) — key = group size.
5. **Group indices of equal values** — `value → list of indices`.
6. **Sections in a list (Android)** — group messages by date, then show headers.
7. **Bucket sort idea** — group numbers by range or digit.

#### 9. Edge Cases / Common Mistakes

1. Using `getOrDefault(key, mutableListOf())` then `.add()`. The new list is never stored, so the item is lost.
2. Using `associateBy` when you need all items. It keeps only the last one.
3. A key that is too coarse (groups different things) or too fine (splits equal things).
4. Using `IntArray` as a key.
5. Expecting ordered groups from a `HashMap`. Use `LinkedHashMap` (what `groupBy` returns) or sort the keys.
6. Changing a list inside the map while looping over the map.
7. Forgetting that `groupBy` returns **read-only lists**. Use `toMutableList()` if you need to edit.
8. Empty input returns an empty map.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need to see or process items by category.
2. You need the group sizes or the largest group.

**Avoid when:**

1. You only need counts. A count map is lighter.
2. You only need to split into two parts. Use `partition`.

#### 11. Related Topics

1. Group Anagrams Pattern
2. Frequency Counting
3. Key-Value Pair Concept
4. Sorting (`02-algorithm/01-sorting`)

#### 12. Interview Must Remember

1. **`getOrPut(key) { mutableListOf() }.add(item)`.**
2. `getOrDefault` does not store the new list.
3. `groupBy` is the one-line version. `associateBy` keeps one item per key.
4. The key design decides everything.
