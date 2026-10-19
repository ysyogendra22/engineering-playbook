# Frequency Counting

#### 1. Definition — Must Know

1. **Frequency counting** means counting **how many times each value appears**.
2. The map is `value → count`.
3. It is the most common HashMap pattern. Many problems begin with "count everything first".

#### 2. Why It Is Used — Must Know

1. It replaces sorting or nested loops (`O(n²)`) with one pass (`O(n)`).
2. It solves anagrams, majority elements, most frequent items, unique counts, and more.
3. It is the first step of Top K Frequent (heap), Group Anagrams, and many window problems.

#### 3. How It Works — Must Know

`nums = [1, 2, 2, 3, 3, 3]`

```text
start:      {}
see 1  →    {1: 1}
see 2  →    {1: 1, 2: 1}
see 2  →    {1: 1, 2: 2}
see 3  →    {1: 1, 2: 2, 3: 1}
see 3  →    {1: 1, 2: 2, 3: 2}
see 3  →    {1: 1, 2: 2, 3: 3}
```

Use the counts: most frequent is `3` (3 times). Values that appear once: `1`.

#### 4. Core Concepts — Must Know

1. **Count in one pass.** `count[x] = (count[x] ?: 0) + 1`.
2. **Read counts in a second pass** (or while counting) to answer the question.
3. **Fixed small alphabet?** Use `IntArray(26)` (or 128 / 256). It is faster and lighter than a map.
4. **Increase while scanning, decrease while checking.** Used in "Ransom Note" and anagram checks.
5. **Kotlin shortcuts:** `groupingBy { it }.eachCount()` builds the map in one line.

| Situation | Best tool |
|---|---|
| Lowercase letters | `IntArray(26)` |
| Any characters | `HashMap<Char, Int>` |
| Numbers (any range) | `HashMap<Int, Int>` |
| Words | `HashMap<String, Int>` |

#### 5. Algorithm — Must Know

```text
count = empty map
for each item: count[item] += 1
then read the counts to answer the question
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Count with a loop
fun countFrequencies(nums: IntArray): HashMap<Int, Int> {
    val count = HashMap<Int, Int>()
    for (n in nums) count[n] = (count[n] ?: 0) + 1
    return count
}

// One-liner
val freq = listOf(1, 2, 2, 3, 3, 3).groupingBy { it }.eachCount()   // {1=1, 2=2, 3=3}

// Most frequent value
fun mostFrequent(nums: IntArray): Int? =
    countFrequencies(nums).maxByOrNull { it.value }?.key

// Valid Anagram
fun isAnagram(s: String, t: String): Boolean {
    if (s.length != t.length) return false
    val count = IntArray(26)
    for (i in s.indices) {
        count[s[i] - 'a']++
        count[t[i] - 'a']--
    }
    return count.all { it == 0 }
}

// Ransom Note — can the note be built from the magazine letters?
fun canConstruct(ransomNote: String, magazine: String): Boolean {
    val count = IntArray(26)
    for (c in magazine) count[c - 'a']++
    for (c in ransomNote) {
        if (--count[c - 'a'] < 0) return false
    }
    return true
}

// Majority Element (appears more than n/2 times)
fun majorityElement(nums: IntArray): Int {
    val count = HashMap<Int, Int>()
    for (n in nums) {
        val c = (count[n] ?: 0) + 1
        count[n] = c
        if (c > nums.size / 2) return n
    }
    return -1
}
```

The `O(1)` space answer for majority element is the Boyer–Moore voting algorithm.

#### 7. Time & Space Complexity — Must Know

| Case | Time | Space |
|---|---:|---:|
| Count `n` items with `u` unique values | `O(n)` | `O(u)` |
| Letters in `IntArray(26)` | `O(n)` | `O(1)` |
| Find the most frequent | `O(u)` extra | — |
| Sort by frequency | `O(u log u)` | — |

#### 8. Common Frequency Patterns — Must Know

1. **Valid Anagram** (LeetCode 242) — equal counts.
2. **Ransom Note** (LeetCode 383) — enough letters.
3. **Majority Element** (LeetCode 169) — count above `n/2`.
4. **First Unique Character** (LeetCode 387) — count, then find the first with count 1.
5. **Top K Frequent Elements** (LeetCode 347) — count, then heap or buckets (`01-data-structure/08-Heap`).
6. **Sort Characters By Frequency** (LeetCode 451).
7. **Unique Number of Occurrences** (LeetCode 1207) — a set of the counts.
8. **Find All Anagrams / Permutation in String** — counts in a sliding window.

#### 9. Edge Cases / Common Mistakes

1. Writing `count[x]++` on a `HashMap`. Use `(count[x] ?: 0) + 1`.
2. Using a map when a 26-slot array would do.
3. Index errors with uppercase letters or digits in `IntArray(26)`.
4. Forgetting different lengths in anagram checks.
5. Comparing counts of two maps with `==`. This works for maps with the same content, but not if one has a key with count `0` and the other does not have the key.
6. Ties for "most frequent". The problem says which to return.
7. Counting characters of a `String` with Unicode or emoji.
8. Empty input.

#### 10. When to Use / When Not to Use

**Use when:**

1. The answer depends on how many times something appears.

**Avoid when:**

1. You only need to know if something appeared. Use a `HashSet`.
2. You need the order of appearance. Use a `LinkedHashMap` or store indices.

#### 11. Related Topics

1. Character / String Frequency Problems
2. Top K Frequent Elements (`01-data-structure/08-Heap/18-Top K Frequent Elements.md`)
3. Group Anagrams Pattern
4. First Unique / Repeated Element

#### 12. Interview Must Remember

1. **`count[x] = (count[x] ?: 0) + 1`** — or `groupingBy { it }.eachCount()`.
2. Lowercase letters → `IntArray(26)`.
3. Count first, then answer. `O(n)` time, `O(u)` space.
4. Frequency + heap = Top K.
