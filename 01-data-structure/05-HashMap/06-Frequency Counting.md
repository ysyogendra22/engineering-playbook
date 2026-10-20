# Frequency Counting

> The most common HashMap pattern. Many problems start with "count everything first".

#### 1. What Is It?

**Frequency counting** means counting **how many times each value appears**.

The map is `value → count`. You build it in one pass, then read the counts to answer the question.

It replaces sorting or nested loops (`O(n²)`) with one pass (`O(n)`).

#### 2. How It Works

`nums = [1, 2, 2, 3, 3, 3]`

```text
start:   {}
see 1 →  {1: 1}
see 2 →  {1: 1, 2: 1}
see 2 →  {1: 1, 2: 2}
see 3 →  {1: 1, 2: 2, 3: 1}
see 3 →  {1: 1, 2: 2, 3: 2}
see 3 →  {1: 1, 2: 2, 3: 3}
```

Now the counts answer many questions: the most frequent value is `3`. The values that appear once: `1`.

Choose the counter:

| Input | Counter |
|---|---|
| lowercase letters `a`–`z` | `IntArray(26)` (index `c - 'a'`) — faster, no boxing |
| any characters | `HashMap<Char, Int>` |
| any numbers | `HashMap<Int, Int>` |
| words | `HashMap<String, Int>` |

Two useful tricks:

- **Add for one string, subtract for the other.** If everything ends at 0, they match (anagram check).
- **Count first, then read.** For "first unique" or "top k", build the counts, then scan or sort.

#### 3. Kotlin Code

```kotlin
// Count with a loop
fun countFrequencies(nums: IntArray): HashMap<Int, Int> {
    val count = HashMap<Int, Int>()
    for (n in nums) count[n] = (count[n] ?: 0) + 1
    return count
}

// One-liner
val freq = listOf(1, 2, 2, 3, 3, 3).groupingBy { it }.eachCount()    // {1=1, 2=2, 3=3}

// Most frequent value
fun mostFrequent(nums: IntArray): Int? =
    countFrequencies(nums).maxByOrNull { it.value }?.key

// Valid Anagram (LeetCode 242)
fun isAnagram(s: String, t: String): Boolean {
    if (s.length != t.length) return false
    val count = IntArray(26)
    for (i in s.indices) {
        count[s[i] - 'a']++
        count[t[i] - 'a']--
    }
    return count.all { it == 0 }
}

// Ransom Note (LeetCode 383): can the note be built from the magazine letters?
fun canConstruct(ransomNote: String, magazine: String): Boolean {
    val count = IntArray(26)
    for (c in magazine) count[c - 'a']++
    for (c in ransomNote) {
        if (--count[c - 'a'] < 0) return false         // not enough of this letter
    }
    return true
}

// Majority Element (LeetCode 169): appears more than n / 2 times
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

The `O(1)`-space answer for majority element is the Boyer–Moore voting algorithm. Mention it if asked to improve space.

**Top K Frequent Elements (LeetCode 347)** is "count, then keep the `k` biggest counts with a heap". The full solution is in `01-data-structure/08-Heap/18-Top K Frequent Elements.md`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Count `n` items with `u` different values | `O(n)` | `O(u)` |
| Letters in `IntArray(26)` | `O(n)` | `O(1)` |
| Sort the counts afterwards | `O(u log u)` | — |

#### 5. Common Mistakes

1. **Writing `count[x]++`.** It does not compile. Use `(count[x] ?: 0) + 1`.
2. **Using a map when `IntArray(26)` is enough.**
3. **Index errors** with capital letters or digits in `IntArray(26)`.
4. **Different lengths** in an anagram check (return `false` at once).
5. **Comparing two maps** where one has a key with count `0`. Remove zero-count keys first.
6. **Ties** for "most frequent". The question says which to return.

#### 6. Say This in the Interview

1. "I will count with a HashMap in one pass, then answer from the counts. That is `O(n)` time and `O(u)` space."
2. "For lowercase letters I use an `IntArray(26)`, so space is `O(1)`."
3. "For the top `k` I would add a heap on top of the counts."

#### 7. Quick Check

1. What are the counts for `"hello"`?
2. How can you check an anagram with only one array?

<details>
<summary>Answers</summary>

1. `h:1, e:1, l:2, o:1`.
2. Add `1` for each letter of the first word and subtract `1` for each letter of the second. If all slots are `0`, they are anagrams.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 242 | Valid Anagram (Easy) | equal counts |
| 383 | Ransom Note (Easy) | enough letters |
| 169 | Majority Element (Easy) | count above `n / 2` |
| 1207 | Unique Number of Occurrences (Easy) | a set of the counts |
| 347 | Top K Frequent Elements (Medium) | counts + heap |
| 451 | Sort Characters By Frequency (Medium) | counts, then sort |
| 692 | Top K Frequent Words (Medium) | counts + heap, ties alphabetical |
