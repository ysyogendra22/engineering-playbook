# HashMap vs HashSet

#### 1. What Is It?

Both are hash-based and give `O(1)` average speed. The difference is **what you get back**.

| | HashSet | HashMap |
|---|---|---|
| Stores | keys only | key + value |
| Answers | "is it there?" | "what goes with it?" |
| Add | `add(x)` → `Boolean` | `put(k, v)` → old value or `null` |
| Look up | `x in set` | `map[k]` → value or `null` |
| Same key twice | ignored | value replaced |
| Memory | lower | higher |

Choosing the right one is the first decision in many interview problems. Interviewers often ask: "why a map and not a set?".

#### 2. How It Works

Ask yourself: **what do I need back from the lookup?**

```text
just yes / no                  → HashSet
a count                        → HashMap<K, Int>
an index / position            → HashMap<K, Int>
a list of related items        → HashMap<K, MutableList<V>>
an object or extra data        → HashMap<K, V>
```

| Problem | Choice | Why |
|---|---|---|
| Contains Duplicate | Set | seen or not |
| Longest Consecutive Sequence | Set | only "is `x + 1` present?" |
| BFS visited | Set | seen or not |
| Two Sum (indexes) | Map | needs the index |
| Valid Anagram | Map / array | needs counts |
| Group Anagrams | Map | a list per key |
| Subarray Sum Equals K | Map | counts of prefix sums |
| BFS distance | Map | a distance per node |

#### 3. Kotlin Code

```kotlin
// A set is enough: Contains Duplicate
fun containsDuplicate(nums: IntArray): Boolean {
    val seen = HashSet<Int>()
    return nums.any { !seen.add(it) }
}

// A map is needed: Two Sum returns INDEXES
fun twoSum(nums: IntArray, target: Int): IntArray {
    val indexOf = HashMap<Int, Int>()
    for ((i, x) in nums.withIndex()) {
        indexOf[target - x]?.let { return intArrayOf(it, i) }
        indexOf[x] = i
    }
    return intArrayOf()
}

// A map is needed: counts
fun isAnagram(a: String, b: String): Boolean =
    a.groupingBy { it }.eachCount() == b.groupingBy { it }.eachCount()

// A set is enough: Longest Consecutive Sequence
fun longestConsecutive(nums: IntArray): Int {
    val set = nums.toHashSet()
    var best = 0
    for (n in set) {
        if (n - 1 !in set) {                    // n starts a run
            var len = 1
            while (n + len in set) len++
            best = maxOf(best, len)
        }
    }
    return best
}
```

You can convert between them: `map.keys` is a set of the keys, and `set.associateWith { 0 }` makes a map from a set.

#### 4. Complexity

| | HashSet | HashMap |
|---|---|---|
| Add / put, contains / get, remove | `O(1)` | `O(1)` |
| Memory | `O(n)` | `O(n)`, bigger per item |

#### 5. Common Mistakes

1. **`HashMap<Int, Boolean>`** where a `HashSet<Int>` is enough.
2. **A set where you need counts.**
3. **A set for Two Sum** when the question asks for indexes.
4. **Treating `map.put` as "ignore if it is there".** It overwrites. Use `putIfAbsent`.
5. **Forgetting that `map[k]` is nullable.**
6. **Using a map for 26 letters** when `IntArray(26)` is faster.

#### 6. Say This in the Interview

1. "I only need to know if a value exists, so a `HashSet`."
2. "I need the index (or the count), so a `HashMap`."
3. "Both are `O(1)` average. The set uses less memory."

#### 7. Quick Check

1. Which do you use for "how many times does each word appear"?
2. Which for "have I seen this number before"?

<details>
<summary>Answers</summary>

1. A `HashMap<String, Int>`.
2. A `HashSet<Int>`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Choice |
|---|---|---|
| 217 | Contains Duplicate (Easy) | set |
| 1 | Two Sum (Easy) | map |
| 349 | Intersection of Two Arrays (Easy) | set |
| 350 | Intersection of Two Arrays II (Easy) | map (counts) |
| 242 | Valid Anagram (Easy) | map or array |
| 128 | Longest Consecutive Sequence (Medium) | set |
