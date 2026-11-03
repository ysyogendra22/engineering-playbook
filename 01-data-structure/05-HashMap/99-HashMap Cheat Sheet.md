# HashMap Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–26.

#### 1. Key Takeaways

1. A `HashMap` gives **`O(1)` average** `put`, `get`, `containsKey` and `remove` (worst `O(n)` with many collisions).
2. Its superpower: turn a **search** into a **lookup**. "Have I seen this? How many times? At which index?" → map.
3. **Counting:** `map[x] = (map[x] ?: 0) + 1`. **Grouping:** `getOrPut(key) { mutableListOf() }.add(item)`.
4. **Two Sum family:** store what you have seen, look up the **complement**. **Check first, then store.**
5. **Prefix sum + map** solves "subarray with sum / balance / remainder" in `O(n)`, even with negatives. Seed it with `{0: 1}` (or `{0: -1}` for indexes).
6. Keys need correct `equals` / `hashCode`. Use a **data class**, `Pair`, `List`, or an encoded `Int`. **Never an array.**
7. `HashMap` has no order: `LinkedHashMap` keeps insertion order, `TreeMap` sorts the keys (`O(log n)`).
8. **HashMap + doubly linked list = LRU cache** with `O(1)` `get` and `put`.

#### 2. Kotlin Operations and Complexity

| Action | Kotlin | Time |
|---|---|---|
| put / update | `map[k] = v`, `put(k, v)` | `O(1)` avg |
| get | `map[k]` (nullable), `getOrDefault(k, d)` | `O(1)` avg |
| contains key | `k in map`, `containsKey(k)` | `O(1)` avg |
| remove | `map.remove(k)` | `O(1)` avg |
| count | `map[k] = (map[k] ?: 0) + 1`, `merge(k, 1, Int::plus)` | `O(1)` avg |
| group | `map.getOrPut(k) { mutableListOf() }.add(v)` | `O(1)` avg |
| size / empty | `size`, `isEmpty()` | `O(1)` |
| iterate | `for ((k, v) in map)` | `O(n)` |
| counts of a collection | `list.groupingBy { it }.eachCount()` | `O(n)` |

Which map: `HashMap` (fastest), `LinkedHashMap` (insertion order, also LRU with `accessOrder = true`), `TreeMap` (sorted, `floorKey`/`ceilingKey`, `O(log n)`).

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Note |
|---|---|---|
| "how many times", "most frequent", "anagram" | frequency map | 06, 19 |
| "does it exist", "is it in" | lookup (set or map) | 07, 16 |
| "two numbers that add up to" | complement lookup, value to index | 08 |
| "group by", "anagrams together" | key → list | 09, 20 |
| "index of", "within `k` positions" | value to index | 10 |
| "subarray sum equals `k`" (negatives allowed) | prefix sum + count map | 11 |
| "longest subarray with sum / equal 0s and 1s" | prefix → first index | 12 |
| "longest substring with at most `k` distinct" | sliding window + count map | 13 |
| "key is a pair or a state" | data class or encoded key | 14 |
| "any duplicate" | seen set | 18 |
| "count pairs that ..." | map of earlier counts | 21 |
| "first non-repeating" | count, then first with 1 | 22 |
| "copy a structure with pointers" | old → new map | 23 |
| "XOR / parity / remainder subarrays" | prefix state + map | 24 |
| "LRU cache", "O(1) get and put with eviction" | HashMap + doubly linked list | 25 |
| "implement HashMap" | buckets + chaining | 26 |

#### 4. Templates to Memorise

**Frequency**

```kotlin
val count = HashMap<Int, Int>()
for (x in nums) count[x] = (count[x] ?: 0) + 1
```

**Two Sum (value to index)**

```kotlin
val indexOf = HashMap<Int, Int>()
for ((i, x) in nums.withIndex()) {
    val j = indexOf[target - x]
    if (j != null) return intArrayOf(j, i)
    indexOf[x] = i
}
```

**Group**

```kotlin
val groups = HashMap<String, MutableList<String>>()
for (w in words) groups.getOrPut(String(w.toCharArray().also { it.sort() })) { mutableListOf() }.add(w)
```

**Subarray sum equals `k`**

```kotlin
val seen = HashMap<Int, Int>(); seen[0] = 1
var sum = 0; var count = 0
for (x in nums) { sum += x; count += seen[sum - k] ?: 0; seen[sum] = (seen[sum] ?: 0) + 1 }
```

**Longest subarray with sum `k` (first index)**

```kotlin
val first = HashMap<Int, Int>(); first[0] = -1
var sum = 0; var best = 0
for ((i, x) in nums.withIndex()) {
    sum += x
    first[sum - k]?.let { best = maxOf(best, i - it) }
    first.putIfAbsent(sum, i)
}
```

**Sliding window with a count map**

```kotlin
val count = HashMap<Char, Int>(); var left = 0
for (right in s.indices) {
    count[s[right]] = (count[s[right]] ?: 0) + 1
    while (count.size > k) {
        val c = s[left++]
        count[c] = count[c]!! - 1
        if (count[c] == 0) count.remove(c)
    }
    best = maxOf(best, right - left + 1)
}
```

**LRU shortcut**

```kotlin
class LRUCache(private val cap: Int) : LinkedHashMap<Int, Int>(cap, 0.75f, true) {
    override fun removeEldestEntry(e: MutableMap.MutableEntry<Int, Int>?) = size > cap
}
```

**Bucket design**

```kotlin
val index = (key.hashCode() and Int.MAX_VALUE) % buckets.size     // then search the bucket's list
```

#### 5. Brute Force to Optimized

| Problem | Brute force | HashMap |
|---|---|---|
| Count each value | nested loops `O(n²)` | `O(n)` |
| Two Sum | all pairs `O(n²)` | `O(n)` |
| Group anagrams | compare all pairs `O(n² · L)` | sorted-letters key `O(n · L log L)` |
| Subarray sum equals `k` | all subarrays `O(n²)` | prefix + map `O(n)` |
| Longest substring, at most `k` distinct | all substrings `O(n²)` | window + map `O(n)` |
| First unique character | scan the rest `O(n²)` | count then scan `O(n)` |
| Copy a list with random pointers | find positions `O(n²)` | old → new map `O(n)` |
| LRU cache | list of keys `O(n)` per op | map + DLL `O(1)` |
| Membership repeated | `list.contains` `O(n)` | `O(1)` |

#### 6. Common Mistakes and Edge Cases

1. **`map[k]!!`** on a missing key, or `map[k] + 1` on `null`.
2. **Arrays as keys** (identity equality). Use `List`, a data class or a string.
3. **Changing a key** after it is in the map.
4. **Prefix sum map without `{0: 1}`** (misses subarrays starting at 0).
5. **Storing the last index** when the question wants the **first** (longest subarray).
6. **Two Sum:** adding before checking (an element pairs with itself).
7. **Removing from a map while iterating it.**
8. **Expecting order** from `HashMap`.
9. **Removing a zero count** from the window map (`count.size` then counts dead keys).
10. **`Int` overflow** in prefix sums. Use `Long`.
11. **Edge cases:** empty input, one element, all equal, negatives, duplicates, `k = 0`.

#### 7. What to Say Out Loud

1. "I'm repeatedly asking 'have I seen this?', so a `HashMap` turns each search into an `O(1)` average lookup. The whole thing is `O(n)` time and `O(n)` space."
2. "I store each value's index, and for each new number I look up its complement. I check before I store, so a number can't pair with itself."
3. "With negative numbers a sliding window fails, so I use prefix sums with a map of how many times each prefix occurred."
4. "For an LRU cache I combine a hash map with a doubly linked list: the map finds the node and the list moves it in `O(1)`."
5. "Worst case is `O(n)` with many collisions, but the average is `O(1)`."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Two Sum](https://leetcode.com/problems/two-sum/) | complement lookup |
| Easy | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | frequency |
| Easy | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | set |
| Easy | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | count, then scan |
| Easy | [Ransom Note](https://leetcode.com/problems/ransom-note/) | frequency |
| Easy | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | two maps |
| Easy | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | index tracking |
| Easy | [Design HashMap](https://leetcode.com/problems/design-hashmap/) | buckets and chaining |
| Medium | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | grouping |
| Medium | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | counts + heap or buckets |
| Medium | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | prefix + map |
| Medium | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | balance + first index |
| Medium | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | window + map |
| Medium | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | set + run starts |
| Medium | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | remainder map |
| Medium | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | old to new map |
| Medium | [LRU Cache](https://leetcode.com/problems/lru-cache/) | HashMap + DLL |
| Medium | [4Sum II](https://leetcode.com/problems/4sum-ii/) | count of pair sums |
