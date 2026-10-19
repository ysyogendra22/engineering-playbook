# HashMap vs HashSet

#### 1. Definition — Must Know

1. A **HashMap** stores **key → value** pairs. It answers "what goes with this key?".
2. A **HashSet** stores **keys only**. It answers "is this key present?".
3. Both are hash-based and both give `O(1)` average `add/put`, `get/contains` and `remove`.
4. The longer version of this comparison is in `01-data-structure/06-HashSet/03-HashSet vs HashMap.md`.

#### 2. Why It Is Used — Must Know

1. Choosing between them is the first decision in many problems.
2. The wrong choice wastes memory (map instead of set) or cannot solve the problem (set instead of map).
3. Interviewers ask: "Why did you use a map here, not a set?".

#### 3. How It Works — Must Know

```text
HashSet<String>             HashMap<String, Int>

apple                       apple  → 3
pear                        pear   → 1

"is apple here?"            "how many apples?"  /  "where is apple?"
```

Quick decision:

```text
What do I need back from the lookup?
   just yes / no                  → HashSet
   a count                        → HashMap<K, Int>
   an index or position           → HashMap<K, Int>
   a list of related items        → HashMap<K, MutableList<V>>
   an object / extra data         → HashMap<K, V>
```

#### 4. Core Concepts — Must Know

| | HashSet | HashMap |
|---|---|---|
| Stores | keys | key + value |
| Main question | exists? | what value? |
| Add | `add(x)` → `Boolean` | `put(k, v)` → old value or `null` |
| Lookup | `x in set` | `map[k]` → `V?` |
| Repeat key | ignored | value replaced |
| Memory | lower | higher |
| Typical use | seen, visited, unique | count, index, group, cache |

1. A Java `HashSet` is a `HashMap` with dummy values.
2. A map's `keys` is a set. A set can be turned into a map with `associateWith`.
3. Same rules for keys: `equals`/`hashCode`, no arrays, no mutation.

#### 5. Algorithm — Must Know

```text
1. Write what you look up (the key).
2. Write what you need back.
3. "Just yes or no" → set.  "A number, index, list or object" → map.
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Set is enough: Contains Duplicate
fun containsDuplicate(nums: IntArray): Boolean {
    val seen = HashSet<Int>()
    return nums.any { !seen.add(it) }
}

// Map is needed: Two Sum returns INDICES
fun twoSum(nums: IntArray, target: Int): IntArray {
    val indexOf = HashMap<Int, Int>()
    for ((i, x) in nums.withIndex()) {
        indexOf[target - x]?.let { return intArrayOf(it, i) }
        indexOf[x] = i
    }
    return intArrayOf()
}

// Map is needed: counts
fun isAnagram(a: String, b: String): Boolean =
    a.groupingBy { it }.eachCount() == b.groupingBy { it }.eachCount()

// Set is enough: Longest Consecutive Sequence
fun longestConsecutive(nums: IntArray): Int {
    val set = nums.toHashSet()
    var best = 0
    for (n in set) {
        if (n - 1 !in set) {
            var len = 1
            while (n + len in set) len++
            best = maxOf(best, len)
        }
    }
    return best
}
```

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
| Contains Duplicate | Set | seen or not |
| Longest Consecutive Sequence | Set | only "is `x+1` present?" |
| Visited in BFS | Set | seen or not |
| Two Sum (indices) | Map | needs the index |
| Valid Anagram | Map / array | needs counts |
| Group Anagrams | Map | list per key |
| Subarray Sum Equals K | Map | counts of prefix sums |
| BFS distance | Map | distance per node |
| Intersection of Two Arrays | Set | unique common values |
| Intersection of Two Arrays II | Map | counts |

#### 9. Edge Cases / Common Mistakes

1. `HashMap<Int, Boolean>` where `HashSet<Int>` would do.
2. A set where a count is needed.
3. A set for Two Sum when indices are required.
4. `map.put` treated as "ignore if present" (it overwrites).
5. Forgetting that `map[k]` is nullable.
6. Using a map for 26 letters when an `IntArray(26)` is faster.

#### 10. When to Use / When Not to Use

**Use a set when:**

1. Only existence or uniqueness matters.

**Use a map when:**

1. You need counts, positions, groups, or stored data.

**Use neither when:**

1. Keys are small integers in a known range. An array is faster.

#### 11. Related Topics

1. HashSet
2. Duplicate Detection
3. HashMap Fundamentals
4. HashSet vs HashMap (`01-data-structure/06-HashSet/03-HashSet vs HashMap.md`)

#### 12. Interview Must Remember

1. **Set: "is it there?" Map: "what goes with it?"**
2. Count, index, list, or object → map. Yes/no → set.
3. Say the choice and the reason out loud.
4. Small integer keys → array.
