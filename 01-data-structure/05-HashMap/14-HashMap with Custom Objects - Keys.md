# HashMap with Custom Objects / Keys

#### 1. Definition — Must Know

1. A HashMap can use **your own classes** as **keys** (`Point`, `Pair`, `State`) or as **values** (`User`, `Task`).
2. A **key** class must have correct `equals()` and `hashCode()`. A **value** class needs nothing special.
3. In Kotlin a **`data class`** with `val` fields is the safe default key.

#### 2. Why It Is Used — Must Know

1. Many keys are naturally several values: `(row, col)`, `(index, remaining)`, `(x, y, direction)`.
2. Memoization in dynamic programming uses such keys.
3. Broken keys cause silent bugs: lookups that "randomly" fail.

#### 3. How It Works — Must Know

```text
map[key]:
   1. key.hashCode()  → picks the bucket
   2. in the bucket, compare stored keys with key.equals()
   3. equal key found → use it; else → missing
```

**The contract:** if `a.equals(b)` then `a.hashCode() == b.hashCode()`.

```kotlin
data class Point(val x: Int, val y: Int)

val dist = HashMap<Point, Int>()
dist[Point(1, 2)] = 5
println(dist[Point(1, 2)])      // 5 — a new, equal object finds the entry
```

A normal class without `equals`/`hashCode` would return `null` here, because two different objects are never equal by default.

#### 4. Core Concepts — Must Know

| Key choice | Equality is based on | Good for |
|---|---|---|
| `Int`, `Long`, `String`, `Char` | value | simple keys |
| `Pair`, `Triple` | contents | quick two/three-part keys |
| `List<Int>` | contents | variable-size keys (immutable use only) |
| `data class` | primary-constructor properties | named, readable keys |
| Normal class | reference (identity) | when identity is truly what you want |
| `IntArray`, `Array` | reference | **never use as a key** |

1. **Keys must be immutable.** Do not change fields after the key is in the map.
2. **Pack into a single `Long`** for speed: `row.toLong() * cols + col`, or `(r.toLong() shl 32) or c.toLong()`.
3. **Joined `String` keys** (`"$r,$c"`) work but allocate more. Always use a separator.
4. **Values can be anything**, including lists, other maps, or objects. A mutable value is fine, since only the key's hash matters.
5. **Big keys are slow** because hashing reads the whole key.

#### 5. Algorithm — Must Know

```text
1. Decide what identifies an item (the key fields).
2. Make a data class (val fields) or pack the fields into one Int/Long/String.
3. Use it as the map key.
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// 1. Pair as a key: distance of visited cells
val visited = HashMap<Pair<Int, Int>, Int>()
visited[2 to 3] = 7
println(visited[2 to 3])                                // 7

// 2. data class state: memoization (Unique Paths)
fun uniquePaths(m: Int, n: Int): Long {
    val memo = HashMap<Pair<Int, Int>, Long>()
    fun go(r: Int, c: Int): Long {
        if (r == m - 1 || c == n - 1) return 1
        return memo.getOrPut(r to c) { go(r + 1, c) + go(r, c + 1) }
    }
    return go(0, 0)
}

// 3. Packed Long key — lighter and faster
fun key(r: Int, c: Int): Long = (r.toLong() shl 32) or (c.toLong() and 0xffffffffL)
val cells = HashMap<Long, Int>()
cells[key(2, 3)] = 7

// 4. A class with your own equals/hashCode — identity by id only
class User(val id: Int, var name: String) {
    override fun equals(other: Any?) = this === other || (other is User && id == other.id)
    override fun hashCode(): Int = id.hashCode()
}
val scores = HashMap<User, Int>()
scores[User(1, "Asha")] = 90
println(scores[User(1, "Someone else")])                // 90 — same id

// 5. Objects as VALUES: no special rule
data class Profile(val name: String, val email: String)
val profiles = HashMap<Int, Profile>()
profiles[1] = Profile("Asha", "a@x.com")

// 6. Bad keys
println(hashMapOf(intArrayOf(1, 2) to "x")[intArrayOf(1, 2)])     // null (arrays compare by reference)
println(hashMapOf(listOf(1, 2) to "x")[listOf(1, 2)])             // x
```

Mutable key bug:

```kotlin
data class Box(var v: Int)
val m = HashMap<Box, String>()
val b = Box(1)
m[b] = "one"
b.v = 2
println(m[b])                    // null — the entry is lost (usually)
```

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---|
| `get` / `put` | `O(1)` average, plus `hashCode()` and `equals()` cost |
| `data class` hash | `O(number of fields)` |
| `List` key hash | `O(list size)` |
| `Pair<Int, Int>` | two boxed `Int`s plus the pair — more memory than a packed `Long` |

#### 8. Common Custom-Key Patterns — Must Know

1. **Coordinates:** `Pair(r, c)` or a packed `Long`.
2. **DP memo:** `(i, j)`, `(index, remaining)`, `(left, right, turn)`.
3. **BFS state:** `(row, col, keys)` as a data class.
4. **Edge key:** `(from, to)` for visited edges.
5. **Signature keys:** sorted letters, 26-count string, shape string (Group Anagrams).
6. **Composite lookup:** `(userId, itemId)` in app caches.
7. **Android example:** a `data class CacheKey(val url: String, val width: Int)` for an image cache.

#### 9. Edge Cases / Common Mistakes

1. Using a normal class as a key and expecting content equality.
2. Overriding `equals` without `hashCode`, or the opposite.
3. Using `var` fields in a key and changing them.
4. Using `IntArray` / `Array` as a key.
5. Joined `String` keys without a separator.
6. Packing fields into a `Long` without checking ranges (fields overlap).
7. Using `hashCode()` itself as the key. Different objects can share one.
8. Using floating-point fields. Equality is exact.
9. Recursion inside `getOrPut`: this is fine with Kotlin's `getOrPut` (it does not hold the map during the call), but `computeIfAbsent` with a recursive call can throw a `ConcurrentModificationException`.

#### 10. When to Use / When Not to Use

**Use a data class key when:**

1. Readability matters and the number of keys is moderate.

**Use a packed `Int`/`Long` key when:**

1. Speed and memory matter (large grids, millions of states).

**Avoid when:**

1. You can use a 2D array for DP or visited. It is faster.

#### 11. Related Topics

1. Hashing / Hash Function — Basic Concept
2. Common HashMap Edge Cases
3. HashSet with Custom Objects (`01-data-structure/06-HashSet/16-HashSet with Custom Objects.md`)
4. Dynamic Programming memoization (`02-algorithm/05-Dynamic Programming`)

#### 12. Interview Must Remember

1. **Keys need `equals()` and `hashCode()` that agree.** `data class` + `val` is the safe default.
2. **Never use arrays as keys. Never mutate a key.**
3. Pack small fields into a `Long` for speed.
4. Values can be anything; only keys have rules.
