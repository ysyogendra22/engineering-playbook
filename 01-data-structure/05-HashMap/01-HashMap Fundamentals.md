# HashMap Fundamentals

#### 1. Definition — Must Know

1. A **HashMap** stores **key → value** pairs and finds a value by its key in **`O(1)` on average**.
2. Each **key is unique**. Putting a value under an existing key **replaces** the old value.
3. It has **no index** and **no guaranteed order**. You ask "what goes with this key?", not "what is at position 3?".
4. In Kotlin/JVM, `HashMap<K, V>` (and `hashMapOf(...)`) is `java.util.HashMap`.

#### 2. Why It Is Used — Must Know

1. **Fast lookup by key:** id → user, word → count, value → index.
2. **Counting:** how many times does each item appear?
3. **Grouping:** put related items under one key.
4. It turns many `O(n²)` solutions (nested loops) into `O(n)`. It is the most used data structure in coding interviews.

#### 3. How It Works — Must Know

```text
key  →  hashCode()  →  bucket index  →  look inside that bucket, compare keys with equals()

put("apple", 3):   hash("apple") → bucket 5 → empty → store ("apple" → 3)
put("pear", 7):    hash("pear")  → bucket 9 → empty → store ("pear" → 7)
get("apple"):      hash("apple") → bucket 5 → key matches → return 3
put("apple", 9):   hash("apple") → bucket 5 → key matches → replace value 3 with 9
```

```text
bucket 5: ("apple" → 9)
bucket 9: ("pear"  → 7)
```

If two keys land in the same bucket (a **collision**), the bucket holds a small chain of entries. Java's `HashMap` starts with 16 buckets and doubles them when 75% full.

#### 4. Core Concepts — Must Know

1. **Key + value.** The key is used to find. The value is the data you want.
2. **Keys need `equals()` and `hashCode()`** that agree. Strings, numbers, `Pair`, `List` and data classes are safe keys.
3. **`get` returns `V?`** (null when the key is missing). Handle it.
4. **Kotlin map types:**

| Type | Order | Speed | Use when |
|---|---|---|---|
| `HashMap` / `hashMapOf()` | none | `O(1)` avg | Most interview problems |
| `LinkedHashMap` / `mutableMapOf()` | insertion order | `O(1)` avg | You need the original order |
| `TreeMap` / `sortedMapOf()` | sorted by key | `O(log n)` | Sorted keys, floor/ceiling |
| `mapOf()` | insertion order | `O(1)` avg | Read-only map |

5. **`mutableMapOf()` is a `LinkedHashMap`**, not a plain `HashMap`.
6. A `HashMap` allows **one `null` key** and null values. Avoid them.

#### 5. Algorithm — Must Know

The usual shape of a HashMap solution:

```text
map = empty
for each item:
    look up something about it in the map   (a count, an index, a group)
    use or update that information
    store the item's own information in the map
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val map = HashMap<String, Int>()            // empty
val ages = hashMapOf("Asha" to 30, "Ben" to 25)

map["apple"] = 3                            // put
map["apple"] = 9                            // update (replaces)
println(map["apple"])                       // 9
println(map["kiwi"])                        // null (missing key)
println(map.getOrDefault("kiwi", 0))        // 0
println("apple" in map)                     // true  — same as containsKey
map.remove("apple")
println(map.size)                           // 0

for ((key, value) in ages) println("$key -> $value")    // order not guaranteed
```

Count with a map (the most common use):

```kotlin
val counts = HashMap<Char, Int>()
for (c in "banana") counts[c] = (counts[c] ?: 0) + 1
println(counts)                             // {a=3, b=1, n=2}
```

#### 7. Time & Space Complexity — Must Know

| Operation | Average | Worst |
|---|---:|---:|
| `put` | `O(1)` | `O(n)`* |
| `get` | `O(1)` | `O(n)`* |
| `remove` | `O(1)` | `O(n)`* |
| `containsKey` | `O(1)` | `O(n)`* |
| `containsValue` | `O(n)` | `O(n)` |
| Iterate all | `O(n + capacity)` | — |
| Space | `O(n)` | — |

\*Worst case happens only with very bad hashing. Modern Java turns long chains into trees, so it is rare. Say "`O(1)` average" in interviews.

#### 8. Common HashMap Patterns — Must Know

1. **Frequency counting** — `value → count`.
2. **Lookup / existence** — `id → object`.
3. **Two Sum** — `value → index`.
4. **Grouping** — `key → list of items`.
5. **Prefix sum + map** — `prefix → count or first index`.
6. **Cache** — `key → cached value` (LRU with a linked list).

#### 9. Edge Cases / Common Mistakes

1. Forgetting that `map[key]` can be `null`. Use `?: 0`, `getOrDefault`, or `getOrPut`.
2. Writing `map[key]++` on a `HashMap<K, Int>`. It does not compile because `get` returns a nullable.
3. Expecting insertion order from a `HashMap`.
4. Using arrays as keys. They compare by reference.
5. Changing a key object after it is in the map.
6. Using `containsValue` in a loop (`O(n)` each time).
7. Using a map when a plain array would be faster (small integer keys or 26 letters).

#### 10. When to Use / When Not to Use

**Use when:**

1. You need to find, count, or group by a key quickly.

**Avoid when:**

1. You only need existence. A `HashSet` is lighter.
2. Keys are small integers in a known range. Use an array.
3. You need sorted keys. Use a `TreeMap`.

#### 11. Related Topics

1. Key-Value Pair Concept
2. Hashing / Hash Function — Basic Concept
3. HashMap Operations & Complexity
4. HashSet (`01-data-structure/06-HashSet`)

#### 12. Interview Must Remember

1. **HashMap = key → value with `O(1)` average put/get/remove.**
2. `get` returns a nullable. Use `?: 0` or `getOrDefault`.
3. No order. `mutableMapOf()` is a `LinkedHashMap`.
4. Keys need correct `equals()` and `hashCode()`.
