# HashMap Operations & Complexity

#### 1. Definition — Must Know

1. The core operations are **insert / put**, **get / search**, **update** and **delete**.
2. All of them run in **`O(1)` average** time.
3. Kotlin adds helpers for the most common cases: `getOrDefault`, `getOrPut`, `merge`, `compute`, `putIfAbsent`.

#### 2. Why It Is Used — Must Know

1. You must know the cost of each call to state the complexity of a solution.
2. Choosing the right helper (`getOrPut`, `merge`) makes code shorter and safer.
3. Knowing the worst case and the resize cost shows depth.

#### 3. How It Works — Must Know

Every operation follows **hash → bucket → equals check**.

```text
put(k, v)   hash k → bucket → key found?  yes: replace value, return old value
                                          no : add new entry (size + 1), maybe resize
get(k)      hash k → bucket → key found?  yes: return value    no: return null
remove(k)   hash k → bucket → key found?  yes: delete entry, return old value   no: null
```

**Resize.** When the map is more than 75% full (load factor 0.75), the table doubles and every entry is placed again. One resize costs `O(n)`, but it is rare, so `put` is `O(1)` **amortized**.

#### 4. Core Concepts — Must Know

1. **Insert / Put**
   - `map[k] = v` or `map.put(k, v)`.
   - Returns the old value (or `null` if the key was new).
2. **Get / Search**
   - `map[k]` returns `V?`. `k in map` checks the key only.
3. **Update**
   - Same as `put` — it replaces the value. Or compute from the old value: `merge`, `compute`.
4. **Delete**
   - `map.remove(k)` returns the removed value or `null`.
5. **Helpers:**

| Need | Call | Stores the default? |
|---|---|---|
| Value or a default | `map.getOrDefault(k, 0)` | No |
| Value, or create and store | `map.getOrPut(k) { mutableListOf() }` | **Yes** |
| Add only if missing | `map.putIfAbsent(k, v)` | Yes |
| Add to a count | `map.merge(k, 1) { old, new -> old + new }` | Yes |
| Change from the old value | `map.compute(k) { _, old -> (old ?: 0) + 1 }` | Yes |

#### 5. Algorithm — Must Know

```text
count[x] += 1   written safely:
    count[x] = (count[x] ?: 0) + 1
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val map = HashMap<String, Int>()

// Insert / put
map["a"] = 1
val old = map.put("a", 5)             // returns 1 (the old value)
map.putIfAbsent("b", 2)               // only if "b" is missing

// Get / search
val v = map["a"]                      // Int?  (5)
val d = map.getOrDefault("z", 0)      // 0, nothing stored
println("a" in map)                   // true
println(map.containsValue(2))         // true, but O(n)

// Update
map["a"] = (map["a"] ?: 0) + 1        // safe increment
map.merge("a", 1) { old, one -> old + one }          // increment, short form
map.compute("a") { _, cur -> (cur ?: 0) * 2 }         // change using the old value

// Delete
map.remove("b")                       // returns 2
map.remove("zzz")                     // null, no error
map.entries.removeIf { it.value > 10 }                // remove by condition (safe in a loop)
map.clear()

// getOrPut: group items
val groups = HashMap<Int, MutableList<String>>()
for (w in listOf("hi", "yo", "hello")) groups.getOrPut(w.length) { mutableListOf() }.add(w)
println(groups)                       // {2=[hi, yo], 5=[hello]}
```

Remove while looping — the safe way:

```kotlin
val m = hashMapOf(1 to "a", 2 to "b", 3 to "c")
m.entries.removeIf { it.key % 2 == 1 }          // safe
// for (k in m.keys) if (k % 2 == 1) m.remove(k)   // ConcurrentModificationException
```

#### 7. Time & Space Complexity — Must Know

| Operation | Average | Worst |
|---|---:|---:|
| `put` / `set` | `O(1)` amortized | `O(n)` (resize or very bad hash) |
| `get` | `O(1)` | `O(n)` |
| `containsKey` | `O(1)` | `O(n)` |
| `remove` | `O(1)` | `O(n)` |
| `containsValue` | `O(n)` | `O(n)` |
| `size`, `isEmpty` | `O(1)` | `O(1)` |
| Iterate | `O(n + capacity)` | — |
| Space | `O(n)` | — |

1. Java 8+ turns very long chains into balanced trees, so the real worst case is close to `O(log n)`.
2. `HashMap<Int, Int>` boxes every key and value. It uses much more memory than an `IntArray`.
3. `TreeMap` operations are `O(log n)`.

#### 8. Common Operation Patterns — Must Know

1. **Count:** `map[x] = (map[x] ?: 0) + 1`.
2. **Group:** `map.getOrPut(key) { mutableListOf() }.add(item)`.
3. **Check then read:** `val v = map[k]; if (v != null) …` (one lookup).
4. **Store first index:** `map.putIfAbsent(x, i)`.
5. **Store last index:** `map[x] = i`.
6. **Pre-size** for huge inputs: `HashMap<Int, Int>(expectedSize * 2)`.

#### 9. Edge Cases / Common Mistakes

1. `map[k]++` does not compile for `HashMap<K, Int>`. Use `(map[k] ?: 0) + 1`.
2. `map[k]!!` crashes when the key is missing.
3. `getOrDefault` does not store the default. `getOrPut` does.
4. `getOrDefault(k, mutableListOf())` then `.add()` loses the list, because it was never stored. Use `getOrPut`.
5. Calling `containsKey` and then `get` (two lookups) when one `get` is enough.
6. Removing during a `for` loop over `keys`/`entries`.
7. Saying every operation is always `O(1)`. Say "average".
8. `put` returns the **old** value, not the new one.

#### 10. When to Use / When Not to Use

**Use when:**

1. Most work is put / get / remove by key.

**Avoid when:**

1. You need the smallest/largest key or ranges. Use a `TreeMap`.
2. Keys are tiny integers. Use an array.

#### 11. Related Topics

1. HashMap Fundamentals
2. Frequency Counting
3. Grouping Pattern
4. Common HashMap Edge Cases

#### 12. Interview Must Remember

1. `put`, `get`, `remove`, `containsKey` are **`O(1)` average**. `containsValue` is `O(n)`.
2. Increment with `(map[k] ?: 0) + 1`, `merge`, or `getOrDefault`.
3. **`getOrPut` stores the default. `getOrDefault` does not.**
4. Never remove from a map inside a `for` loop over it. Use `removeIf`.
