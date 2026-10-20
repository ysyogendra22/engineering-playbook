# HashMap with Custom Objects / Keys

#### 1. What Is It?

A HashMap can use **your own classes** as **keys** (like a `Point` or a `State`) or as **values** (like a `User`).

- A **key** class needs correct `equals()` and `hashCode()`.
- A **value** class needs nothing special.

In Kotlin, a **`data class`** with `val` fields writes both functions for you. It is the safe default for keys.

Why it matters: many keys are really **several values together**: `(row, col)`, `(index, remaining)`, `(x, y, direction)`. Memoization (dynamic programming) and BFS on grids use such keys all the time.

#### 2. How It Works

```text
map[key]:
   1. key.hashCode() picks the bucket
   2. inside the bucket, compare stored keys with key.equals()
   3. an equal key found → use it.  Otherwise → missing.
```

```kotlin
data class Point(val x: Int, val y: Int)

val dist = HashMap<Point, Int>()
dist[Point(1, 2)] = 5
println(dist[Point(1, 2)])      // 5: a NEW but equal object finds the entry
```

A normal class (no `equals`) would return `null` here, because two different objects are never equal by default.

Which key types work:

| Key type | Equal when... | Use for |
|---|---|---|
| `Int`, `Long`, `String`, `Char` | same value | simple keys |
| `Pair`, `Triple` | same contents | quick 2- or 3-part keys |
| `List<Int>` | same contents | keys of any length (do not change them later) |
| `data class` | same constructor fields | named, readable keys |
| normal class | same object | only if identity is what you want |
| `IntArray`, `Array` | same object | **never use as a key** |

#### 3. Kotlin Code

```kotlin
// Pair as a key
val visited = HashMap<Pair<Int, Int>, Int>()
visited[2 to 3] = 7
println(visited[2 to 3])                              // 7

// A data class key for memoization: Unique Paths
fun uniquePaths(m: Int, n: Int): Long {
    val memo = HashMap<Pair<Int, Int>, Long>()
    fun go(r: Int, c: Int): Long {
        if (r == m - 1 || c == n - 1) return 1
        return memo.getOrPut(r to c) { go(r + 1, c) + go(r, c + 1) }
    }
    return go(0, 0)
}

// Pack two Ints into one Long: lighter and faster than a Pair
fun key(r: Int, c: Int): Long = (r.toLong() shl 32) or (c.toLong() and 0xffffffffL)
val cells = HashMap<Long, Int>()
cells[key(2, 3)] = 7

// Your own equals/hashCode: two users are equal if they have the same id
class User(val id: Int, var name: String) {
    override fun equals(other: Any?) = this === other || (other is User && id == other.id)
    override fun hashCode(): Int = id.hashCode()
}

// Objects as VALUES need no special rule
data class Profile(val name: String, val email: String)
val profiles = HashMap<Int, Profile>()
profiles[1] = Profile("Asha", "a@x.com")

// Bad key: arrays
println(hashMapOf(intArrayOf(1, 2) to "x")[intArrayOf(1, 2)])    // null
println(hashMapOf(listOf(1, 2) to "x")[listOf(1, 2)])            // x
```

The mutable key bug:

```kotlin
data class Box(var v: Int)
val m = HashMap<Box, String>()
val b = Box(1)
m[b] = "one"
b.v = 2
println(m[b])                    // null: the entry is lost (its hash code changed)
```

#### 4. Complexity

| | Time |
|---|---|
| `get` / `put` | `O(1)` average, plus the cost of `hashCode()` and `equals()` |
| Hash of a `data class` | `O(number of fields)` |
| Hash of a `List` key | `O(size of the list)` |

A long key makes every operation slower. A packed `Long` is the lightest.

#### 5. Common Mistakes

1. **A normal class as a key** and expecting content equality.
2. **`equals` without `hashCode`** (or the opposite).
3. **`var` fields in a key**, changed later.
4. **`IntArray` or `Array` as a key.**
5. **A joined `String` key without a separator.** Use `"$r,$c"`.
6. **Packing fields into a `Long` without checking ranges.** The fields overlap.
7. **A floating-point field in a key.** Equality is exact, so `0.1 + 0.2` is not `0.3`.

#### 6. Say This in the Interview

1. "My key has two parts, so I use a `data class` (or a `Pair`) with `val` fields."
2. "For speed I can pack two numbers into one `Long`."
3. "I never use arrays as keys and never change a key after inserting it."

#### 7. Quick Check

1. Why does `HashMap<IntArray, String>` fail to find a key?
2. What makes a `data class` a good key?

<details>
<summary>Answers</summary>

1. An `IntArray` compares by reference. A new array with the same numbers is not equal and has another hash code.
2. Kotlin generates `equals` and `hashCode` from its constructor fields, so equal contents mean equal keys.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 62 | Unique Paths (Medium) | memo with a `(row, col)` key |
| 70 | Climbing Stairs (Easy) | memo with an `Int` key |
| 49 | Group Anagrams (Medium) | key = sorted letters or a `List` of counts |
| 864 | Shortest Path to Get All Keys (Hard) | BFS state `(row, col, keys)` |
| 1 | Two Sum (Easy) | simple key, for comparison |
