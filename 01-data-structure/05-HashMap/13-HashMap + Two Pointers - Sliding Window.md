# HashMap + Two Pointers / Sliding Window

#### 1. Definition — Must Know

1. A **sliding window** is a range `[left, right]` that grows on the right and shrinks on the left.
2. A **HashMap** keeps **counts of the items inside the window**.
3. Use it when the rule needs counts: "at most `k` distinct", "contains all of these characters", "the same letters as another word".
4. If the rule only needs "no repeats", a `HashSet` is enough (`01-data-structure/06-HashSet/14`).

#### 2. Why It Is Used — Must Know

1. It turns "check every substring" (`O(n²)` or worse) into `O(n)`.
2. It is behind many hard string problems, such as *Minimum Window Substring*.
3. It is a frequent interview topic for medium and hard questions.

#### 3. How It Works — Must Know

*Fruit Into Baskets* (LeetCode 904): the longest subarray with at most **2 distinct values**.

`fruits = [1, 2, 1, 2, 3]`

```text
left=0
right=0 fruit 1 → counts {1:1}                 distinct 1   length 1
right=1 fruit 2 → counts {1:1, 2:1}            distinct 2   length 2
right=2 fruit 1 → counts {1:2, 2:1}            distinct 2   length 3
right=3 fruit 2 → counts {1:2, 2:2}            distinct 2   length 4   ← best
right=4 fruit 3 → counts {1:2, 2:2, 3:1}       distinct 3 > 2 → shrink
        remove fruits[0]=1 → {1:1, 2:2, 3:1}   still 3 distinct, left=1
        remove fruits[1]=2 → {1:1, 2:1, 3:1}   still 3 distinct, left=2
        remove fruits[2]=1 → {2:1, 3:1}        2 distinct, left=3     length 2

Answer: 4
```

When a count drops to `0`, **remove the key** so `map.size` is the number of distinct values.

#### 4. Core Concepts — Must Know

1. **Two pointers:** `right` moves every step. `left` moves only when the window breaks the rule.
2. **Map = counts inside the window.** Add `s[right]` on the right, remove `s[left]` on the left.
3. **Remove keys with count 0.** Otherwise `map.size` is wrong.
4. **Variable window:** shrink with a `while` until the rule is valid again.
5. **Fixed window** (anagram search): slide one step at a time — add the new item, remove the old one.
6. **"Missing" counter:** for "contains all needed characters", track how many distinct needed characters are still short. It avoids comparing whole maps on every step.

| Problem | Rule |
|---|---|
| Fruit Into Baskets / at most `k` distinct | `map.size <= k` |
| Minimum Window Substring | window has every needed letter with enough count |
| Permutation in String / Find All Anagrams | window counts equal the target counts |
| Longest Repeating Character Replacement | `windowSize - maxCount <= k` |

#### 5. Algorithm — Must Know

```text
left = 0; counts = empty map
for right in 0 until n:
    add s[right] to counts
    while the window is invalid:
        remove s[left] from counts (delete the key if the count reaches 0)
        left++
    update the answer using (right - left + 1)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Longest subarray with at most 2 distinct values (Fruit Into Baskets)
fun totalFruit(fruits: IntArray): Int {
    val count = HashMap<Int, Int>()
    var left = 0
    var best = 0
    for (right in fruits.indices) {
        count[fruits[right]] = (count[fruits[right]] ?: 0) + 1
        while (count.size > 2) {
            val f = fruits[left]
            val c = count.getValue(f) - 1
            if (c == 0) count.remove(f) else count[f] = c
            left++
        }
        best = maxOf(best, right - left + 1)
    }
    return best
}

// Minimum Window Substring
fun minWindow(s: String, t: String): String {
    if (t.isEmpty() || s.length < t.length) return ""
    val need = HashMap<Char, Int>()
    for (c in t) need[c] = (need[c] ?: 0) + 1

    val have = HashMap<Char, Int>()
    var missing = need.size                 // distinct letters not yet satisfied
    var left = 0
    var bestLen = Int.MAX_VALUE
    var bestStart = 0

    for (right in s.indices) {
        val c = s[right]
        if (c in need) {
            have[c] = (have[c] ?: 0) + 1
            if (have[c] == need[c]) missing--
        }
        while (missing == 0) {                         // the window is valid: try to shrink it
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

// Permutation in String — fixed window with letter counts
fun checkInclusion(s1: String, s2: String): Boolean {
    if (s1.length > s2.length) return false
    val need = IntArray(26)
    val window = IntArray(26)
    for (c in s1) need[c - 'a']++
    for (i in s2.indices) {
        window[s2[i] - 'a']++
        if (i >= s1.length) window[s2[i - s1.length] - 'a']--
        if (window.contentEquals(need)) return true
    }
    return false
}
```

Checks: `totalFruit([1,2,1,2,3])` → `4`. `minWindow("ADOBECODEBANC", "ABC")` → `"BANC"`.

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| At most `k` distinct | `O(n)` | `O(k)` |
| Minimum Window Substring | `O(n + m)` | `O(m)` (letters in `t`) |
| Permutation in String (26 letters) | `O(26 · n)` ≈ `O(n)` | `O(1)` |
| Brute force substrings | `O(n²)`–`O(n³)` | — |

Each item is added once and removed once, so the `while` loop does not make it `O(n²)`.

#### 8. Common HashMap + Window Patterns — Must Know

1. **Fruit Into Baskets** (LeetCode 904), **Longest Substring with At Most K Distinct Characters** (LeetCode 340, premium).
2. **Minimum Window Substring** (LeetCode 76).
3. **Permutation in String** (LeetCode 567), **Find All Anagrams in a String** (LeetCode 438).
4. **Longest Repeating Character Replacement** (LeetCode 424).
5. **Longest Substring Without Repeating Characters** (LeetCode 3) — map of last index.
6. **Subarrays with K Different Integers** (LeetCode 992) — `atMost(k) - atMost(k-1)`.
7. **Substring with Concatenation of All Words** (LeetCode 30) — word counts in a window.

#### 9. Edge Cases / Common Mistakes

1. Not removing keys whose count reaches `0`, so `map.size` is wrong.
2. Using `if` instead of `while` when shrinking.
3. Comparing whole maps on every step. Use a `missing` counter or a fixed `IntArray` compare.
4. Updating the answer before the window is valid (or after it was broken).
5. Boxed `Int` compare: `have[c] == need[c]` is fine in Kotlin (value equality), but `===` is not.
6. `t` longer than `s` — return `""` at once.
7. Duplicate letters in `t`. Use counts, not a set.
8. Off-by-one in the window length.

#### 10. When to Use / When Not to Use

**Use when:**

1. The window rule depends on counts or on the number of distinct items.

**Use a set when:**

1. The rule is only "no repeats".

**Avoid when:**

1. The parts are not contiguous.
2. Numbers can be negative and the rule is about sums. Use prefix sum + map.

#### 11. Related Topics

1. Sliding Window (`03-leetcode-patterns`, topic 5)
2. Two Pointers (`03-leetcode-patterns`, topic 4)
3. HashSet + Sliding Window (`01-data-structure/06-HashSet/14-HashSet + Sliding Window.md`)
4. Character / String Frequency Problems

#### 12. Interview Must Remember

1. **Map = counts inside the window.** Add on the right, remove on the left.
2. **Delete a key when its count reaches `0`.**
3. Shrink with `while`. Each item enters and leaves once, so `O(n)`.
4. Use a `missing` counter or `IntArray` instead of comparing maps.
