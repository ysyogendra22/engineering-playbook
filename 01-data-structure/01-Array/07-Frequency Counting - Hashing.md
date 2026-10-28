# Frequency Counting / Hashing

> The array-side view. The full HashMap notes are in `01-data-structure/05-HashMap`.

#### 1. What Is It?

**Frequency counting** means counting how many times each value appears. **Hashing** (a `HashMap` or `HashSet`) lets you check "have I seen this?" in `O(1)` instead of scanning the array.

Use it when the brute force has **two nested loops** and the inner loop only asks "does this value exist?" or "how many of this value?".

| Tool | Use when |
|---|---|
| `HashSet` | only "seen / not seen" (duplicates) |
| `HashMap<Int, Int>` | counts, or value → index |
| `IntArray(26)` | lowercase letters (fast, `O(1)` space) |
| `BooleanArray(n + 1)` | values are in `1..n` |

#### 2. How It Works

*Two Sum*: for each number `x`, you need `target - x`. Keep a map of numbers you have seen.

```text
nums = [2, 7, 11, 15], target = 9
x=2  need 7  not seen → store 2→0
x=7  need 2  seen at index 0 → answer [0, 1]
```

*Contains Duplicate*: `set.add(x)` returns `false` if `x` was already there.

*Valid Anagram*: count each letter of the first word up, and of the second word down. If all counts end at 0, they match.

#### 3. Brute Force vs Optimized

| | Brute force | Hashing |
|---|---|---|
| Idea | for each item, scan the rest | remember what you have seen |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` | `O(n)` |

```kotlin
fun containsDuplicateBrute(nums: IntArray): Boolean {
    for (i in nums.indices) for (j in i + 1 until nums.size) {
        if (nums[i] == nums[j]) return true
    }
    return false
}
```

Other option when memory is tight: **sort** first (`O(n log n)`, `O(1)` extra) and compare neighbours.

#### 4. Kotlin Code

```kotlin
// Two Sum (LeetCode 1)
fun twoSum(nums: IntArray, target: Int): IntArray {
    val seen = HashMap<Int, Int>()                         // value → index
    for ((i, x) in nums.withIndex()) {
        val j = seen[target - x]
        if (j != null) return intArrayOf(j, i)
        seen[x] = i                                        // store AFTER checking
    }
    return intArrayOf()
}

// Contains Duplicate (LeetCode 217)
fun containsDuplicate(nums: IntArray): Boolean {
    val seen = HashSet<Int>()
    for (n in nums) if (!seen.add(n)) return true
    return false
}

// Valid Anagram (LeetCode 242)
fun isAnagram(s: String, t: String): Boolean {
    if (s.length != t.length) return false
    val count = IntArray(26)
    for (i in s.indices) { count[s[i] - 'a']++; count[t[i] - 'a']-- }
    return count.all { it == 0 }
}

// Intersection of Two Arrays II (LeetCode 350): each value as often as it appears in both
fun intersect(a: IntArray, b: IntArray): IntArray {
    val count = HashMap<Int, Int>()
    for (x in a) count[x] = (count[x] ?: 0) + 1
    val result = mutableListOf<Int>()
    for (x in b) {
        val c = count[x] ?: 0
        if (c > 0) { result.add(x); count[x] = c - 1 }
    }
    return result.toIntArray()
}

// First Unique Character (LeetCode 387)
fun firstUniqChar(s: String): Int {
    val count = IntArray(26)
    for (c in s) count[c - 'a']++
    for ((i, c) in s.withIndex()) if (count[c - 'a'] == 1) return i
    return -1
}
```

Checks: `twoSum([2,7,11,15], 9)` → `[0, 1]`. `intersect([1,2,2,1], [2,2])` → `[2, 2]`. `firstUniqChar("leetcode")` → `0`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| One pass with a map or set | `O(n)` | `O(n)` |
| Counting letters with `IntArray(26)` | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Storing before checking** in Two Sum: a number pairs with itself.
2. **`count[x]++` on a `HashMap`.** It does not compile. Use `(count[x] ?: 0) + 1`.
3. **`IntArray(26)` with capital letters or digits.**
4. **Arrays as map keys.** They compare by reference. Use a `List` or a `String`.
5. **Forgetting duplicates in the input.**

#### 7. Say This in the Interview

1. "Brute force is `O(n²)`. With a HashMap I can check each item in `O(1)`, so it is `O(n)` time and `O(n)` space."
2. "For lowercase letters I use an `IntArray(26)`, so space is `O(1)`."
3. "If memory is limited I can sort first and compare neighbours."

#### 8. Quick Check

1. Which structure for "have I seen this number before?"
2. Which structure when you need the index of a seen number?

<details>
<summary>Answers</summary>

1. A `HashSet`.
2. A `HashMap<Int, Int>` from value to index.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) (Easy) | value → index |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy) | set |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy) | letter counts |
| 350 | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) (Easy) | counts |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (Easy) | count, then scan |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium) | sorted letters as a key |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium) | counts + heap |
