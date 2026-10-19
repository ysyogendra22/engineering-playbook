# HashSet vs HashMap

#### 1. Definition — Must Know

1. A **HashSet** stores **keys only**. It answers "is this key present?".
2. A **HashMap** stores **key → value pairs**. It answers "what is the value for this key?".
3. Both use hashing and both give `O(1)` average operations.
4. In Java, a `HashSet` is actually built on top of a `HashMap`. The set's values are the map's keys.

#### 2. Why It Is Used — Must Know

1. Choosing the right one is the first decision in many interview problems.
2. The wrong choice either wastes memory (a map when a set is enough) or cannot solve the problem (a set when a value is needed).
3. Interviewers often ask: "Why a set here and not a map?".

#### 3. How It Works — Must Know

```text
HashSet<String>           HashMap<String, Int>

"apple"                   "apple"  → 3
"banana"                  "banana" → 1
"cherry"                  "cherry" → 7

question: "is apple here?"     question: "how many apples?"  /  "where is apple?"
```

Inside the JVM:

```text
HashSet<E>  ≈  HashMap<E, PRESENT>     (every key has the same dummy value)
```

#### 4. Core Concepts — Must Know

| | HashSet | HashMap |
|---|---|---|
| Stores | keys | key + value |
| Main question | exists? | what value? |
| Add | `add(x)` → Boolean | `put(k, v)` → old value or null |
| Lookup | `x in set` | `map[k]` → value or null |
| Duplicates | ignored | overwrites the old value |
| Memory | lower | higher (stores values too) |
| Typical use | seen, visited, unique | count, index, group, cache |

**How to choose:**

```text
Do I only need to know "seen it or not"?          → HashSet
Do I need a count?                                → HashMap<K, Int>
Do I need the index or position of a value?       → HashMap<K, Int>
Do I need to group items under a key?             → HashMap<K, MutableList<V>>
Do I need to store extra data for each key?       → HashMap
```

#### 5. Algorithm — Must Know

Decision rule used in interviews:

```text
1. Write what you look up (the key).
2. Write what you need back.
3. If the answer to step 2 is "just yes or no" → HashSet.
4. If it is a number, index, list or object → HashMap.
```

#### 6. Kotlin Implementation — Must Know

Same problem family, different tool:

```kotlin
// Contains Duplicate → a set is enough
fun containsDuplicate(nums: IntArray): Boolean {
    val seen = HashSet<Int>()
    for (n in nums) if (!seen.add(n)) return true
    return false
}

// Two Sum (return INDICES) → needs a map, because we must give back the index
fun twoSum(nums: IntArray, target: Int): IntArray {
    val indexOf = HashMap<Int, Int>()          // value → index
    for ((i, n) in nums.withIndex()) {
        val j = indexOf[target - n]
        if (j != null) return intArrayOf(j, i)
        indexOf[n] = i
    }
    return intArrayOf()
}

// Intersection II (each value as many times as it appears in BOTH) → needs counts → map
fun intersect(a: IntArray, b: IntArray): IntArray {
    val count = HashMap<Int, Int>()
    for (n in a) count[n] = (count[n] ?: 0) + 1
    val result = mutableListOf<Int>()
    for (n in b) {
        val c = count[n] ?: 0
        if (c > 0) { result.add(n); count[n] = c - 1 }
    }
    return result.toIntArray()
}
```

You can turn a map into a set of its keys: `map.keys`. You can turn a set into a map with a default: `set.associateWith { 0 }`.

#### 7. Time & Space Complexity — Must Know

| | HashSet | HashMap |
|---|---:|---:|
| Add / put | `O(1)` avg | `O(1)` avg |
| Contains / get | `O(1)` avg | `O(1)` avg |
| Remove | `O(1)` avg | `O(1)` avg |
| Space | `O(n)` | `O(n)`, larger constant |

#### 8. Common Choice Patterns — Must Know

| Problem | Choice | Why |
|---|---|---|
| Contains Duplicate | Set | Only need seen / not seen |
| Longest Consecutive Sequence | Set | Only need "is `x+1` present?" |
| Intersection of Two Arrays (unique) | Set | Only need membership |
| Two Sum (indices) | Map | Need the index |
| Intersection of Two Arrays II | Map | Need counts |
| Valid Anagram | Map / array | Need counts |
| Group Anagrams | Map | Need a list per key |
| Visited in BFS | Set | Only need seen / not seen |
| Distance in BFS | Map | Need the distance per node |

#### 9. Edge Cases / Common Mistakes

1. Using `HashMap<Int, Boolean>` when `HashSet<Int>` is enough.
2. Using a set when duplicates need counting.
3. Using a set for Two Sum when indices are required.
4. Forgetting that `map[k]` returns `null` for a missing key (`Int?`).
5. Treating `map.put` as "ignore if present". It overwrites. Use `putIfAbsent` or `getOrPut`.
6. Using a `HashMap` when a `BooleanArray`/`IntArray` would do for small ranges (such as 26 letters).

#### 10. When to Use / When Not to Use

**Use a HashSet when:**

1. Only existence or uniqueness matters.

**Use a HashMap when:**

1. You need counts, positions, groups, or stored data.

**Use neither when:**

1. Keys are small integers in a known range. A plain array is faster and lighter.

#### 11. Related Topics

1. HashSet Fundamentals
2. Fast Membership / Lookup Pattern
3. HashMap (`01-data-structure/05-HashMap`)
4. Two Sum / Complement Lookup with HashSet

#### 12. Interview Must Remember

1. **Set: "is it there?" Map: "what goes with it?"**
2. A Java `HashSet` is a `HashMap` with dummy values.
3. If you need a count, an index, or a list per key → `HashMap`.
4. Say your choice and the reason: "I only need existence, so a set."
