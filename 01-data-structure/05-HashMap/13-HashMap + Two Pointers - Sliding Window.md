# HashMap + Two Pointers / Sliding Window

> Very common in FAANG interviews, especially with strings.

#### 1. What Is It?

A **sliding window** is a range `[left, right]` that grows on the right and shrinks on the left.

A **HashMap** keeps the **counts of the items inside the window**. Use it when the rule needs counts:

- "at most `k` different items",
- "the window contains all the needed letters",
- "the window has the same letters as another word".

If the rule is only "no repeats", a `HashSet` is enough.

Why it matters: it turns "check every substring" (`O(n²)` or worse) into `O(n)`.

#### 2. How It Works

*Fruit Into Baskets* (LeetCode 904): the longest subarray with **at most 2 different values**.

`fruits = [1, 2, 1, 2, 3]`

```text
right=0 fruit 1 → counts {1:1}                 different: 1   length 1
right=1 fruit 2 → counts {1:1, 2:1}            different: 2   length 2
right=2 fruit 1 → counts {1:2, 2:1}            different: 2   length 3
right=3 fruit 2 → counts {1:2, 2:2}            different: 2   length 4   ← best
right=4 fruit 3 → counts {1:2, 2:2, 3:1}       different: 3 > 2 → shrink
        remove fruits[0]=1 → {1:1, 2:2, 3:1}   still 3 different, left = 1
        remove fruits[1]=2 → {1:1, 2:1, 3:1}   still 3 different, left = 2
        remove fruits[2]=1 → {2:1, 3:1}        2 different, left = 3      length 2

answer = 4
```

The steps every time:

1. Add `s[right]` to the counts.
2. While the window breaks the rule: remove `s[left]` and move `left`.
3. When a count reaches `0`, **remove the key**, so `map.size` is the number of different items.
4. Update the answer with `right - left + 1`.

#### 3. Kotlin Code

```kotlin
// Fruit Into Baskets: longest subarray with at most 2 different values
fun totalFruit(fruits: IntArray): Int {
    val count = HashMap<Int, Int>()
    var left = 0
    var best = 0
    for (right in fruits.indices) {
        count[fruits[right]] = (count[fruits[right]] ?: 0) + 1
        while (count.size > 2) {
            val f = fruits[left]
            val c = count.getValue(f) - 1
            if (c == 0) count.remove(f) else count[f] = c       // remove the key at 0
            left++
        }
        best = maxOf(best, right - left + 1)
    }
    return best
}

// Minimum Window Substring (LeetCode 76)
fun minWindow(s: String, t: String): String {
    if (t.isEmpty() || s.length < t.length) return ""
    val need = HashMap<Char, Int>()
    for (c in t) need[c] = (need[c] ?: 0) + 1

    val have = HashMap<Char, Int>()
    var missing = need.size                       // letters of t not yet satisfied
    var left = 0
    var bestLen = Int.MAX_VALUE
    var bestStart = 0

    for (right in s.indices) {
        val c = s[right]
        if (c in need) {
            have[c] = (have[c] ?: 0) + 1
            if (have[c] == need[c]) missing--
        }
        while (missing == 0) {                     // the window is valid: try to shrink it
            if (right - left + 1 < bestLen) {
                bestLen = right - left + 1
                bestStart = left
            }
            val lc = s[left]
            if (lc in need) {
                have[lc] = have.getValue(lc) - 1
                if (have.getValue(lc) < need.getValue(lc)) missing++
            }
            left++
        }
    }
    return if (bestLen == Int.MAX_VALUE) "" else s.substring(bestStart, bestStart + bestLen)
}

// Permutation in String (LeetCode 567): a fixed window with letter counts
fun checkInclusion(s1: String, s2: String): Boolean {
    if (s1.length > s2.length) return false
    val need = IntArray(26)
    val window = IntArray(26)
    for (c in s1) need[c - 'a']++
    for (i in s2.indices) {
        window[s2[i] - 'a']++
        if (i >= s1.length) window[s2[i - s1.length] - 'a']--   // the letter that left the window
        if (window.contentEquals(need)) return true
    }
    return false
}
```

Checks: `totalFruit([1,2,1,2,3])` → `4`. `minWindow("ADOBECODEBANC", "ABC")` → `"BANC"`. `checkInclusion("ab", "eidbaooo")` → `true`.

#### 4. Complexity

| Problem | Time | Space |
|---|---|---|
| At most `k` different | `O(n)` | `O(k)` |
| Minimum Window Substring | `O(n + m)` | `O(m)` (letters in `t`) |
| Permutation in String | `O(26 · n)` ≈ `O(n)` | `O(1)` |
| Brute force substrings | `O(n²)` or worse | — |

Each item is added once and removed once, so the inner `while` does not make it `O(n²)`.

#### 5. Common Mistakes

1. **Not removing keys whose count reaches `0`.** Then `map.size` is wrong.
2. **Using `if` instead of `while`** to shrink the window.
3. **Comparing whole maps on every step.** Use a `missing` counter or compare two `IntArray(26)`.
4. **Updating the answer at the wrong time.** Update only when the window is valid.
5. **Duplicate letters in `t`.** Use counts, not a set.
6. **Off-by-one** in the window length (`right - left + 1`).

#### 6. Say This in the Interview

1. "I slide a window and keep counts of its contents in a map. When the rule breaks, I move `left` until it is valid again."
2. "Each item enters and leaves once, so it is `O(n)`."
3. "I delete a key when its count hits zero, so `map.size` is the number of different items."

#### 7. Quick Check

1. Why must you remove a key when its count becomes `0`?
2. Why is the nested `while` still `O(n)` overall?

<details>
<summary>Answers</summary>

1. Otherwise `map.size` still counts items that are no longer in the window.
2. `left` only moves forward and never goes back. Over the whole run it moves at most `n` times.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 3 | Longest Substring Without Repeating Characters (Medium) | map of last index, or a set |
| 904 | Fruit Into Baskets (Medium) | at most 2 different |
| 340 | Longest Substring with At Most K Distinct Characters (Medium, premium) | at most `k` different |
| 424 | Longest Repeating Character Replacement (Medium) | window size minus max count |
| 567 | Permutation in String (Medium) | fixed window |
| 438 | Find All Anagrams in a String (Medium) | fixed window |
| 76 | Minimum Window Substring (Hard) | needs all letters of `t` |
| 992 | Subarrays with K Different Integers (Hard) | `atMost(k) - atMost(k - 1)` |
