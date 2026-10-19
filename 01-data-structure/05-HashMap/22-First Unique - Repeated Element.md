# First Unique / Repeated Element

#### 1. Definition — Must Know

1. **First unique element:** the first value (by position) that appears **exactly once**.
2. **First repeated element:** the first value that shows up **a second time** while scanning left to right.
3. They are different questions and need different approaches:
   - first unique → **count everything first**, then scan in order,
   - first repeated → **one pass** with a set.

#### 2. Why It Is Used — Must Know

1. They test the difference between "count first" and "check as you go".
2. *First Unique Character in a String* (LeetCode 387) is a very common easy question.
3. The streaming version (first unique in a stream) shows how to keep order with a queue.

#### 3. How It Works — Must Know

`s = "loveleetcode"`

**First unique character**

```text
Pass 1: count      l:2  o:2  v:1  e:4  t:1  c:1  d:1
Pass 2: scan in order and stop at the first letter with count 1
        l(2) no, o(2) no, v(1) YES → index 2
```

**First repeated character**

```text
s = "abcdbe"
a → add (new)  b → add  c → add  d → add  b → add returns false → 'b' is the first repeated
```

Why two passes for "unique"? You cannot know a letter is unique until you have seen the whole string.

#### 4. Core Concepts — Must Know

1. **First unique = count, then scan the original order.** The map has no order; the original string/array gives the order.
2. **First repeated = set.** `add` returns `false` at the first repeat.
3. **`LinkedHashMap` keeps insertion order**, so you can find the first entry with count 1 without a second pass over the input (but scanning the entries costs `O(u)`).
4. **Store the index** (`value → first index`, or `-1` after a repeat) to find the unique one with the smallest index.
5. **Streams:** keep a queue of candidates and discard from the front while the front is no longer unique (lazy deletion).
6. **Small alphabet:** use `IntArray(26)` for counts.

| Question | Approach |
|---|---|
| First unique (array/string known up front) | count, then scan in order |
| First repeated | set, one pass |
| First unique in a stream | counts map + queue |
| First non-repeating by index with one pass | `value → index`, mark repeats as `-1`, take the minimum index at the end |

#### 5. Algorithm — Must Know

```text
First unique:
  count each item
  for each item in the original order: if count == 1 → return it

First repeated:
  seen = empty set
  for each item: if seen.add(item) is false → return it
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// First Unique Character in a String — returns the index, or -1
fun firstUniqChar(s: String): Int {
    val count = IntArray(26)
    for (c in s) count[c - 'a']++
    for ((i, c) in s.withIndex()) {
        if (count[c - 'a'] == 1) return i
    }
    return -1
}

// First unique value in an array, any integers
fun firstUnique(nums: IntArray): Int? {
    val count = HashMap<Int, Int>()
    for (n in nums) count[n] = (count[n] ?: 0) + 1
    return nums.firstOrNull { count[it] == 1 }
}

// First repeated element
fun firstRepeated(nums: IntArray): Int? {
    val seen = HashSet<Int>()
    for (n in nums) if (!seen.add(n)) return n
    return null
}

// First unique in a stream (like LeetCode 1429, premium)
class FirstUnique {
    private val count = HashMap<Int, Int>()
    private val queue = ArrayDeque<Int>()

    fun add(value: Int) {
        count[value] = (count[value] ?: 0) + 1
        if (count[value] == 1) queue.addLast(value)
    }

    fun showFirstUnique(): Int {
        // lazy deletion: drop front values that became non-unique
        while (queue.isNotEmpty() && count.getValue(queue.first()) > 1) queue.removeFirst()
        return if (queue.isEmpty()) -1 else queue.first()
    }
}
```

Checks: `firstUniqChar("leetcode")` → `0`. `firstUniqChar("loveleetcode")` → `2`. `firstUniqChar("aabb")` → `-1`.

#### 7. Time & Space Complexity — Must Know

| Task | Time | Space |
|---|---:|---:|
| First unique, two passes | `O(n)` | `O(u)` (`O(1)` for 26 letters) |
| First repeated, set | `O(n)` | `O(u)` |
| Stream `add` | `O(1)` | `O(u)` |
| Stream `showFirstUnique` | `O(1)` amortized | — |

#### 8. Common Patterns — Must Know

1. **First Unique Character in a String** (LeetCode 387).
2. **First Unique Number in a stream** (LeetCode 1429, premium).
3. **First Letter to Appear Twice** (LeetCode 2351) — first repeated, set.
4. **Find the first duplicate** in an array — set.
5. **Single Number** (LeetCode 136) — XOR is the `O(1)` space answer.
6. **Remove all adjacent duplicates** — stack, not a map.
7. **Android example:** show the first notification type that has only one unread message.

#### 9. Edge Cases / Common Mistakes

1. Trying to find the first unique in one pass without counts.
2. Looping over the **map** to find the first unique and expecting the input order. Loop over the input instead (or use `LinkedHashMap`).
3. Confusing "first repeated" (second occurrence appears first) with "first element that has a duplicate". Example: `[2, 1, 1, 2]` — the first repeated by second occurrence is `1`; the first element that has a duplicate is `2`.
4. Returning the value when the index is wanted, or the reverse.
5. No unique value: return `-1` / `null`.
6. Stream version: leaving non-unique values at the front of the queue.
7. Counting in a `HashMap` when a 26-slot array is enough.

#### 10. When to Use / When Not to Use

**Use the count + scan when:**

1. All data is available and you need the first unique.

**Use the set when:**

1. You need the first repeated element.

**Use the queue + map when:**

1. Data arrives as a stream and you must answer at any moment.

#### 11. Related Topics

1. Frequency Counting
2. Duplicate Detection
3. Character / String Frequency Problems
4. Queue (`01-data-structure/04-Queue`)

#### 12. Interview Must Remember

1. **First unique → count first, then scan in the original order.**
2. **First repeated → set, one pass.**
3. Stream: map of counts + queue, drop non-unique fronts lazily.
4. A map has no input order; use the input (or a `LinkedHashMap`) for order.
