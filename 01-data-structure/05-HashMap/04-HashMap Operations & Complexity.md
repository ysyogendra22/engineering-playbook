# HashMap Operations & Complexity

#### 1. What Is It?

The four basic operations of a HashMap:

| Operation | Kotlin | Returns |
|---|---|---|
| **Insert / Put** | `map[k] = v` or `map.put(k, v)` | the old value, or `null` for a new key |
| **Get / Search** | `map[k]` | the value, or `null` if missing |
| **Update** | `map[k] = newValue` | (same as put) |
| **Delete** | `map.remove(k)` | the removed value, or `null` |

All four are `O(1)` on average. Kotlin also has helpers for the most common cases:

| Need | Call | Stores the default? |
|---|---|---|
| The value, or a default | `map.getOrDefault(k, 0)` | **No** |
| The value, or create and **store** one | `map.getOrPut(k) { mutableListOf() }` | **Yes** |
| Add only if the key is missing | `map.putIfAbsent(k, v)` | Yes |
| Add to a count | `map.merge(k, 1) { old, new -> old + new }` | Yes |
| Change using the old value | `map.compute(k) { _, old -> (old ?: 0) + 1 }` | Yes |

#### 2. How It Works

Every operation does the same three steps: **hash the key → go to the bucket → compare with `equals()`**.

```text
put(k, v)    key found?  yes → replace the value     no → add a new pair
get(k)       key found?  yes → return the value      no → return null
remove(k)    key found?  yes → delete the pair        no → return null
```

**Resizing:** when the map is 75% full, it doubles its buckets and places every pair again. One resize costs `O(n)`, but it is rare, so `put` stays `O(1)` on average ("amortized").

#### 3. Kotlin Code

```kotlin
val map = HashMap<String, Int>()

// Put
map["a"] = 1
val old = map.put("a", 5)                     // returns 1 (the old value)
map.putIfAbsent("b", 2)                       // only if "b" is missing

// Get
val v = map["a"]                              // Int? → 5
val d = map.getOrDefault("z", 0)              // 0, and "z" is NOT added
println("a" in map)                           // true

// Update using the old value (increment)
map["a"] = (map["a"] ?: 0) + 1                // the safe increment
map.merge("a", 1) { old, one -> old + one }   // same, shorter

// Delete
map.remove("b")                               // returns 2
map.remove("zzz")                             // returns null, no error

// getOrPut: group items by length
val groups = HashMap<Int, MutableList<String>>()
for (w in listOf("hi", "yo", "hello")) groups.getOrPut(w.length) { mutableListOf() }.add(w)
println(groups)                               // {2=[hi, yo], 5=[hello]}
```

Remove while looping — the safe way:

```kotlin
val m = hashMapOf(1 to "a", 2 to "b", 3 to "c")
m.entries.removeIf { it.key % 2 == 1 }        // safe
// for (k in m.keys) if (k % 2 == 1) m.remove(k)   // crashes: ConcurrentModificationException
```

#### 4. Complexity

| Operation | Average | Notes |
|---|---|---|
| `put`, `get`, `remove`, `containsKey` | `O(1)` | |
| `containsValue` | `O(n)` | scans every pair |
| `size`, `isEmpty` | `O(1)` | |
| Visit all pairs | `O(n)` | |
| Memory | `O(n)` | `HashMap<Int, Int>` boxes numbers, so it uses more memory than an `IntArray` |

#### 5. Common Mistakes

1. **`map[k]++`** does not compile. Use `(map[k] ?: 0) + 1`.
2. **`map[k]!!`** crashes when the key is missing.
3. **`getOrDefault(k, mutableListOf()).add(x)`**. The new list is never stored, so `x` is lost. Use `getOrPut`.
4. **Calling `containsKey` and then `get`.** One `get` is enough: `val v = map[k]; if (v != null) ...`.
5. **Removing inside `for (k in map.keys)`.** It crashes. Use `removeIf`.
6. **Calling `containsValue` in a loop.** It is `O(n)` each time.
7. **Forgetting that `put` returns the old value**, not the new one.

#### 6. Say This in the Interview

1. "`put`, `get` and `remove` are `O(1)` on average."
2. "I use `getOrPut` to create the list the first time a key appears."
3. "`containsValue` is `O(n)`, so I keep a reverse map if I need fast value lookups."

#### 7. Quick Check

1. What is the difference between `getOrDefault` and `getOrPut`?
2. What does `map.remove("x")` return if `"x"` is not there?

<details>
<summary>Answers</summary>

1. `getOrDefault` only returns a default. `getOrPut` also **stores** the new value in the map.
2. `null`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Operation used |
|---|---|---|
| 1 | Two Sum (Easy) | `get`, then `put` |
| 242 | Valid Anagram (Easy) | increment counts |
| 49 | Group Anagrams (Medium) | `getOrPut` |
| 347 | Top K Frequent Elements (Medium) | counts with `merge` |
| 560 | Subarray Sum Equals K (Medium) | `get` and `put` on prefix sums |
