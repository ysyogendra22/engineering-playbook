# Common HashMap Edge Cases

#### 1. Definition — Must Know

1. These are the situations where HashMap code most often **breaks or gives wrong answers**.
2. Most come from five places: **missing keys (null)**, **key equality**, **mutation**, **order**, and **empty or extreme input**.
3. Run this list before you say "done" in an interview.

#### 2. Why It Is Used — Must Know

1. Interviewers watch whether you think about edge cases before they point them out.
2. Many real app bugs (crashes, lost cache entries) come from these same mistakes.
3. A short checklist is faster than debugging.

#### 3. How It Works — Must Know

The most common crash:

```text
val count = HashMap<Char, Int>()
count['a']++            ← does not compile: count['a'] is Int?, not Int
count['a']!! + 1        ← compiles, but crashes with NullPointerException when 'a' is missing
(count['a'] ?: 0) + 1   ← correct
```

The most common silent bug:

```text
map.getOrDefault(key, mutableListOf()).add(item)
   ↑ the new list is NOT stored in the map, so the item is lost
map.getOrPut(key) { mutableListOf() }.add(item)    ← correct
```

#### 4. Core Concepts — Must Know

| # | Edge case | What happens | Fix |
|---|---|---|---|
| 1 | Missing key | `map[k]` returns `null` | `?: default`, `getOrDefault`, `getOrPut` |
| 2 | `map[k]!!` on a missing key | `NullPointerException` | check `null` first |
| 3 | `map[k]++` | compile error | `map[k] = (map[k] ?: 0) + 1` |
| 4 | `getOrDefault` with a mutable default | default is not stored | use `getOrPut` |
| 5 | Arrays as keys | duplicates and lookups fail | use `List`, `String`, or a `data class` |
| 6 | Mutating a key | entry becomes unfindable | immutable keys (`val`) |
| 7 | Class without `equals`/`hashCode` | equal-looking keys differ | use a `data class` |
| 8 | Expecting order | `HashMap` order is not defined | `LinkedHashMap` or `TreeMap` |
| 9 | Removing in a `for` loop | `ConcurrentModificationException` | `entries.removeIf { }` or an `Iterator` |
| 10 | Putting during iteration | same exception | collect changes, apply after the loop |
| 11 | `containsValue` in a loop | `O(n)` each, so `O(n²)` | keep a reverse map or a set of values |
| 12 | Count of `0` left in the map | `map.size` is wrong as "distinct count" | remove the key when the count hits `0` |
| 13 | Comparing maps with `==` | equal only if all keys and values match | remove zero-count keys first |
| 14 | `null` key or value | allowed in `HashMap`, confusing | avoid; use a sentinel or `Optional`-style |
| 15 | `Int` overflow in counts or sums | wrong results | use `Long` when needed |
| 16 | `HashMap` shared across threads | corrupted state | `ConcurrentHashMap` or locking |
| 17 | `mapOf()` is read-only | `put` does not compile | use `mutableMapOf()` / `HashMap` |
| 18 | `associateBy` / `associate` with repeated keys | the last one wins silently | use `groupBy` |
| 19 | Large `HashMap<Int, Int>` | boxed numbers use much memory | arrays, `IntArray`, or specialised maps |
| 20 | Empty input | loops do nothing; `maxBy` throws | use `maxByOrNull` |

#### 5. Algorithm — Must Know

Checklist before you finish:

```text
1. What if the key is missing?        (null handling)
2. What if the input is empty / one element / all the same?
3. Are my keys immutable, with correct equals/hashCode? Any arrays?
4. Do I change the map while looping over it?
5. Does the answer depend on order?
6. Could counts or sums overflow Int?
7. Is a map really needed (an array or a set may be enough)?
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val count = HashMap<Char, Int>()

// 1. Safe increment
for (c in "hello") count[c] = (count[c] ?: 0) + 1

// 2. getOrDefault vs getOrPut
val groups = HashMap<Int, MutableList<String>>()
groups.getOrDefault(1, mutableListOf()).add("lost")         // not stored!
println(groups)                                             // {}
groups.getOrPut(1) { mutableListOf() }.add("kept")
println(groups)                                             // {1=[kept]}

// 3. Remove while looping — safe
val m = hashMapOf(1 to 10, 2 to 20, 3 to 30)
m.entries.removeIf { it.value >= 20 }
println(m)                                                  // {1=10}

// 4. Remove zero counts so size means "distinct"
fun decrement(map: HashMap<Char, Int>, c: Char) {
    val v = map.getValue(c) - 1
    if (v == 0) map.remove(c) else map[c] = v
}

// 5. Arrays as keys
println(hashMapOf(intArrayOf(1) to "a")[intArrayOf(1)])     // null
println(hashMapOf(listOf(1) to "a")[listOf(1)])             // a

// 6. Map equality ignores order, but needs the same keys
println(mapOf(1 to 1, 2 to 2) == mapOf(2 to 2, 1 to 1))     // true
println(mapOf(1 to 1) == mapOf(1 to 1, 2 to 0))             // false (extra key with 0)

// 7. Empty input
val empty = emptyMap<String, Int>()
println(empty.maxByOrNull { it.value })                     // null  (maxBy would throw)

// 8. Overflow
val big = Int.MAX_VALUE
println(big + 1)                                            // -2147483648
println(big.toLong() + 1)                                   // 2147483648
```

#### 7. Time & Space Complexity — Must Know

| Concern | Impact |
|---|---|
| Bad `hashCode` (all keys collide) | operations drop toward `O(n)` (about `O(log n)` with tree buckets) |
| `containsValue` | `O(n)` each call |
| Boxed `Integer` keys and values | roughly 16–40 bytes per object, versus 4 bytes in an `IntArray` |
| Many resizes | pre-size with `HashMap(capacity)` when the size is known |

#### 8. Common Bug Families — Must Know

1. **Null bugs:** missing keys, `!!`, nullable values.
2. **Equality bugs:** arrays, classes without `equals`.
3. **Mutation bugs:** changing keys; changing the map while looping.
4. **Order bugs:** assuming sorted or insertion order.
5. **Default bugs:** `getOrDefault` with a mutable default.
6. **Size bugs:** zero-count entries; `containsValue` loops.
7. **Number bugs:** overflow, `Int` vs `Long` keys.

#### 9. Edge Cases / Common Mistakes

1. Testing only the example from the problem.
2. Using `map.keys.first()` on an empty map. It throws `NoSuchElementException`.
3. Mixing key types (`Int` and `Long`), so lookups silently fail.
4. Using the wrong type for a character key (`'1'` is not `1`).
5. Treating `map.values` as a set. It has repeats.
6. Keeping a reference to `map.entries` items and changing the map after.
7. Using `toString()` of a map as a key. It depends on order and is slow.
8. Returning a `Map` you later modify, so the caller sees changes.
9. Thinking `HashMap` is synchronized. It is not.

#### 10. When to Use / When Not to Use

**Use this checklist when:**

1. You finish writing any HashMap solution.
2. You review code that uses maps as caches.

**Remember:**

1. A map is only as correct as the `equals()` and `hashCode()` of its keys.

#### 11. Related Topics

1. HashMap Operations & Complexity
2. HashMap with Custom Objects / Keys
3. Frequency Counting
4. Common HashSet Edge Cases (`01-data-structure/06-HashSet/11-Common HashSet Edge Cases.md`)

#### 12. Interview Must Remember

1. **`map[k]` can be `null`.** Use `?: 0`, `getOrDefault`, `getOrPut`.
2. **`getOrDefault` does not store. `getOrPut` does.**
3. **No arrays as keys, no mutating keys, no removing inside a `for` loop.**
4. Delete keys whose count hits `0`, and think about overflow.
