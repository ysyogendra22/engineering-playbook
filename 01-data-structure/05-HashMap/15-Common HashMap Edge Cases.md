# Common HashMap Edge Cases

> Read this list before a HashMap interview. Run through it at the end of every solution.

#### 1. What Is It?

These are the situations where HashMap solutions most often **crash** or **give a wrong answer**. Interviewers watch if you check them yourself. Most bugs come from five places:

1. a **missing key** (`null`),
2. **key equality** (arrays, classes without `equals`),
3. **changing** keys or the map while looping,
4. **assuming an order**,
5. **empty or extreme input**.

#### 2. The Checklist

| # | Edge case | What goes wrong | Fix |
|---|---|---|---|
| 1 | Missing key | `map[k]` returns `null` | `?: 0`, `getOrDefault`, `getOrPut` |
| 2 | `map[k]!!` on a missing key | `NullPointerException` | check `null` first |
| 3 | `map[k]++` | does not compile | `map[k] = (map[k] ?: 0) + 1` |
| 4 | `getOrDefault` with a mutable default | the default is not stored, items lost | `getOrPut` |
| 5 | Array as a key | lookups fail | `List`, `String` or `data class` |
| 6 | Changing a key | the entry becomes unfindable | immutable keys (`val`) |
| 7 | Class without `equals`/`hashCode` | equal-looking keys differ | `data class` |
| 8 | Expecting order | `HashMap` order is not defined | `LinkedHashMap` or `TreeMap` |
| 9 | Removing inside `for (k in map.keys)` | `ConcurrentModificationException` | `entries.removeIf { }` |
| 10 | `containsValue` in a loop | `O(n)` each, so `O(n²)` | keep a reverse map |
| 11 | A count left at `0` in the map | `map.size` is wrong | remove the key at 0 |
| 12 | Comparing maps with `==` | `0`-count keys make equal data unequal | remove zero-count keys first |
| 13 | `Int` overflow in sums or counts | wrong value | `Long` |
| 14 | Mixed key types (`Int` vs `Long`, `Char` vs `String`) | lookups silently fail | keep one type |
| 15 | Empty input | `maxBy` and `first()` throw | `maxByOrNull`, `firstOrNull` |
| 16 | `mapOf()` is read-only | cannot `put` | `mutableMapOf()` / `HashMap` |
| 17 | `associateBy` with repeated keys | the last item wins | `groupBy` |
| 18 | Shared by threads | corrupted data | `ConcurrentHashMap` |

#### 3. Kotlin Code

```kotlin
val count = HashMap<Char, Int>()

// 1 and 3. Safe increment
for (c in "hello") count[c] = (count[c] ?: 0) + 1

// 4. getOrDefault does not store; getOrPut does
val groups = HashMap<Int, MutableList<String>>()
groups.getOrDefault(1, mutableListOf()).add("lost")
println(groups)                                       // {}   the item is lost
groups.getOrPut(1) { mutableListOf() }.add("kept")
println(groups)                                       // {1=[kept]}

// 9. Remove while looping: the safe way
val m = hashMapOf(1 to 10, 2 to 20, 3 to 30)
m.entries.removeIf { it.value >= 20 }
println(m)                                            // {1=10}

// 11. Remove a key when its count reaches 0
fun decrement(map: HashMap<Char, Int>, c: Char) {
    val v = map.getValue(c) - 1
    if (v == 0) map.remove(c) else map[c] = v
}

// 5. Arrays as keys
println(hashMapOf(intArrayOf(1) to "a")[intArrayOf(1)])    // null
println(hashMapOf(listOf(1) to "a")[listOf(1)])            // a

// 12. Maps with a zero-count key are not equal
println(mapOf(1 to 1) == mapOf(1 to 1, 2 to 0))            // false

// 15. Empty input
println(emptyMap<String, Int>().maxByOrNull { it.value })  // null (maxBy would throw)

// 13. Overflow
println(Int.MAX_VALUE + 1)                                 // -2147483648
println(Int.MAX_VALUE.toLong() + 1)                        // 2147483648
```

#### 4. Complexity

Edge cases do not change the complexity. They change **correctness**. Two exceptions: a bad `hashCode` can make every operation `O(n)`, and `containsValue` in a loop makes the solution `O(n²)`.

#### 5. Common Mistakes

1. **Testing only the example from the question.** Also test: empty input, one item, all items equal, all different.
2. **Using `map.keys.first()` on an empty map.** It throws.
3. **Mixing key types**, so lookups silently return `null`.
4. **Treating `'1'` (a character) as `1` (a number).**
5. **Returning a map and then changing it**, so the caller sees the changes.

#### 6. Say This in the Interview

1. "Edge cases I will check: empty input, a single item, and a missing key."
2. "I handle a missing key with `getOrDefault` or `getOrPut`."
3. "My keys are immutable `data class` or `String` values, never arrays."

#### 7. Quick Check

1. What does `map.getOrDefault(k, mutableListOf()).add(1)` do to the map?
2. Why remove a key when its count hits `0`?

<details>
<summary>Answers</summary>

1. Nothing. The new list is not stored in the map, so the `1` is lost.
2. So `map.size` means "number of different items", and map comparisons work.

</details>

#### 8. Related LeetCode Questions

| # | Question | Edge case to watch |
|---|---|---|
| 1 | Two Sum (Easy) | store after checking, duplicates |
| 49 | Group Anagrams (Medium) | `getOrPut`, array keys |
| 560 | Subarray Sum Equals K (Medium) | start with `{0: 1}` |
| 76 | Minimum Window Substring (Hard) | zero counts, duplicate letters |
| 146 | LRU Cache (Medium) | update vs insert |
