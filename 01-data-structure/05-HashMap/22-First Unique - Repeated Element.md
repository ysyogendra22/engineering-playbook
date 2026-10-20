# First Unique / Repeated Element

#### 1. What Is It?

Two questions that sound alike but need different methods:

| Question | Meaning | Method |
|---|---|---|
| **First unique** | the first item (by position) that appears **exactly once** | **count everything first**, then scan in the original order |
| **First repeated** | the first item that shows up **a second time** while you scan | **one pass** with a set |

Why "unique" needs two passes: you cannot know that an item is unique until you have seen the whole input.

*First Unique Character in a String* (LeetCode 387) is a very common easy question.

#### 2. How It Works

**First unique** in `"loveleetcode"`:

```text
Pass 1: count        l:2  o:2  v:1  e:4  t:1  c:1  d:1
Pass 2: scan in the original order, stop at the first letter with count 1
        l(2) no,  o(2) no,  v(1) YES → index 2
```

**First repeated** in `"abcdbe"`:

```text
a → add (new)    b → add    c → add    d → add
b → add returns false → b is the first repeated character
```

Important: a map has **no input order**. Scan the **input** (not the map) to find the first unique. Or use a `LinkedHashMap`, which keeps insertion order.

**First unique in a stream** (items arrive one at a time): keep a count map **and** a queue of candidates. When asked, remove from the front of the queue while the front is no longer unique.

#### 3. Kotlin Code

```kotlin
// First Unique Character in a String: returns the index, or -1
fun firstUniqChar(s: String): Int {
    val count = IntArray(26)
    for (c in s) count[c - 'a']++
    for ((i, c) in s.withIndex()) {
        if (count[c - 'a'] == 1) return i
    }
    return -1
}

// First unique number in an array (any integers)
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

// First unique in a stream (LeetCode 1429, premium)
class FirstUnique {
    private val count = HashMap<Int, Int>()
    private val queue = ArrayDeque<Int>()

    fun add(value: Int) {
        count[value] = (count[value] ?: 0) + 1
        if (count[value] == 1) queue.addLast(value)
    }

    fun showFirstUnique(): Int {
        // drop front values that are no longer unique
        while (queue.isNotEmpty() && count.getValue(queue.first()) > 1) queue.removeFirst()
        return if (queue.isEmpty()) -1 else queue.first()
    }
}
```

Checks: `firstUniqChar("leetcode")` → `0`. `firstUniqChar("loveleetcode")` → `2`. `firstUniqChar("aabb")` → `-1`.

#### 4. Complexity

| Task | Time | Space |
|---|---|---|
| First unique (two passes) | `O(n)` | `O(u)` (`O(1)` for 26 letters) |
| First repeated | `O(n)` | `O(u)` |
| Stream: `add` / `showFirstUnique` | `O(1)` / `O(1)` on average | `O(u)` |

#### 5. Common Mistakes

1. **Trying to find the first unique in one pass** without counts.
2. **Looping over the map** and expecting the input order. Loop over the input.
3. **Mixing up** "first repeated" (second occurrence comes first) with "first element that has a duplicate". In `[2, 1, 1, 2]` the first repeated is `1`, but the first element with a duplicate is `2`.
4. **Returning the value when the index is asked** (or the reverse).
5. **No unique item.** Return `-1` or `null`.
6. **Stream version:** leaving non-unique values at the front of the queue.

#### 6. Say This in the Interview

1. "To find the first unique I count every item, then scan the input in order and return the first with count 1. That is `O(n)`."
2. "For the first repeated item, a set and one pass is enough."
3. "For a stream I keep counts plus a queue of candidates and remove non-unique ones from the front when asked."

#### 7. Quick Check

1. What is the first unique character of `"aabbcd"`?
2. What is the first repeated character of `"abcba"`?

<details>
<summary>Answers</summary>

1. `c` (index 4).
2. `b`. The second `b` appears before the second `a`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 387 | First Unique Character in a String (Easy) | count, then scan |
| 2351 | First Letter to Appear Twice (Easy) | first repeated, set |
| 1429 | First Unique Number (Medium, premium) | counts + queue |
| 136 | Single Number (Easy) | XOR gives `O(1)` space |
| 217 | Contains Duplicate (Easy) | any repeat |
