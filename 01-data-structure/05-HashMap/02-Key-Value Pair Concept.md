# Key-Value Pair Concept

#### 1. Definition — Must Know

1. A **key-value pair** (also called an **entry**) links one **key** to one **value**.
2. The **key** is the label you search with. The **value** is the data stored under that label.
3. Keys are **unique** in a map. Values can repeat.

#### 2. Why It Is Used — Must Know

1. Most real data is "something → information about it": user id → user, word → meaning, product → price.
2. Choosing the right key and value is the main design decision in a HashMap problem.
3. Good key/value choices make the solution short and fast.

#### 3. How It Works — Must Know

```text
Key (unique)     Value (can repeat)
"Asha"       →   30
"Ben"        →   25
"Chitra"     →   30          ← two keys can share a value
"Asha"       →   31          ← same key: the old value 30 is replaced
```

A map entry is one row: `("Ben", 25)`. In Kotlin, a pair is written `"Ben" to 25`.

**Choosing key and value — ask two questions:**

```text
1. What do I search with?   → that is the KEY
2. What do I need back?     → that is the VALUE
```

| Problem | Key | Value |
|---|---|---|
| Count letters | letter | count |
| Two Sum | number | index |
| Group Anagrams | sorted letters | list of words |
| Prefix sum | prefix sum | how many times / first index |
| Phone book | name | number |

#### 4. Core Concepts — Must Know

1. **Unique keys.** `put` on an existing key replaces the value.
2. **Values are free.** They can be numbers, lists, objects, even other maps.
3. **A key must be immutable** (or never changed while in the map).
4. **Entry** (`Map.Entry<K, V>`) gives `.key` and `.value`.
5. **Destructuring:** `for ((k, v) in map)` reads each pair.
6. **Views of a map:** `map.keys` (a set), `map.values` (a collection), `map.entries` (a set of entries).
7. **`Pair<A, B>`** is a plain two-value holder. `a to b` creates one. A `Pair` is *not* a map entry, but `mapOf(a to b)` builds a map from pairs.

#### 5. Algorithm — Must Know

```text
Designing a map for a problem:
1. Decide the key (what I look up by).
2. Decide the value (what I need to know about it).
3. Decide when to add, update, and read.
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val scores = hashMapOf("Asha" to 90, "Ben" to 75)

// Read all entries
for ((name, score) in scores) println("$name has $score")
for (entry in scores.entries) println("${entry.key} -> ${entry.value}")

// Views
println(scores.keys)        // [Asha, Ben]  (a Set)
println(scores.values)      // [90, 75]     (a Collection — values can repeat)

// Values can be lists: key → many values
val tags = HashMap<String, MutableList<String>>()
tags.getOrPut("kotlin") { mutableListOf() }.add("android")
tags.getOrPut("kotlin") { mutableListOf() }.add("coroutines")
println(tags)               // {kotlin=[android, coroutines]}

// Build a map from a list
data class User(val id: Int, val name: String)
val users = listOf(User(1, "Asha"), User(2, "Ben"))
val byId = users.associateBy { it.id }              // id → User
val nameById = users.associate { it.id to it.name } // id → name

// Swap keys and values (values must be unique, or later ones win)
val reversed = scores.entries.associate { (k, v) -> v to k }
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| Read one pair by key | `O(1)` average |
| Add / update / remove one pair | `O(1)` average |
| Iterate all pairs | `O(n)` |
| Find a key by value (reverse lookup) | `O(n)` |
| Space | `O(n)` pairs |

#### 8. Common Key-Value Designs — Must Know

1. **item → count** (frequency).
2. **item → index** (position tracking, Two Sum).
3. **category → list of items** (grouping).
4. **state → result** (memoization in DP).
5. **old node → new node** (copying structures).
6. **prefix → count** (subarray sums).
7. **Android example:** `viewId → listener`, `userId → cached profile`, `route → screen`.

#### 9. Edge Cases / Common Mistakes

1. Picking the wrong key, so you cannot find what you need quickly.
2. Overwriting by accident when two items share a key.
3. Needing to search by value. That is `O(n)`. Keep a second map the other way.
4. Using a mutable object as a key and changing it.
5. Forgetting that `associateBy` and `associate` keep the **last** item for a repeated key.
6. Treating `map.values` as a set. It can contain repeats.
7. Building a `String` key by joining fields without a separator (`"1" + "23"` equals `"12" + "3"`).

#### 10. When to Use / When Not to Use

**Use when:**

1. Every item has a natural label to look it up by.

**Avoid when:**

1. There is no useful key. Use a list.
2. Keys repeat and you need all of them. Use `key → list` (grouping).

#### 11. Related Topics

1. HashMap Fundamentals
2. Grouping Pattern
3. Mapping / Index Tracking
4. HashMap with Custom Objects / Keys

#### 12. Interview Must Remember

1. **Key = what you search with. Value = what you need back.**
2. Keys are unique; values can repeat.
3. Value = list gives grouping. Value = count gives frequency.
4. Say your key and value out loud before you code.
