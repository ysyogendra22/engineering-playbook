# HashSet + Sliding Window

#### 1. Definition — Must Know

1. A **sliding window** is a range of consecutive items that grows on the right and shrinks on the left.
2. A **HashSet** holds the items **inside the current window**, so you can check duplicates in `O(1)`.
3. Use it when the rule is "all items in the window must be unique" or "no duplicate within distance `k`".

#### 2. Why It Is Used — Must Know

1. It turns an `O(n²)` "check every substring" idea into `O(n)`.
2. It is behind famous problems: *Longest Substring Without Repeating Characters* (LeetCode 3) and *Contains Duplicate II* (LeetCode 219).
3. It shows two techniques working together, which interviewers like.

#### 3. How It Works — Must Know

Longest substring without repeating characters, `s = "abcabcbb"`.

```text
left = 0, window = {}

right=0 'a' not in window → add          window {a}        length 1
right=1 'b' not in window → add          window {a,b}      length 2
right=2 'c' not in window → add          window {a,b,c}    length 3   ← best
right=3 'a' IS in window  → remove s[left]='a', left=1      window {b,c}
                            then add 'a'                    window {b,c,a}  length 3
right=4 'b' IS in window  → remove 'b', left=2, add 'b'     window {c,a,b}  length 3
right=5 'c' IS in window  → remove 'c', left=3, add 'c'     window {a,b,c}  length 3
right=6 'b' IS in window  → remove 'a' (left=4), 'b' (left=5), add 'b'
                                                            window {c,b}    length 2
right=7 'b' IS in window  → remove 'c' (left=6), 'b' (left=7), add 'b'
                                                            window {b}      length 1

Answer: 3   (the best length seen)
```

The idea: when the new item breaks the rule, **remove items from the left until the rule is true again**, then add the new item.

#### 4. Core Concepts — Must Know

1. **Two pointers:** `left` and `right`. `right` moves every step. `left` moves only when needed.
2. **The set is the window.** It always holds exactly the items from `left` to `right`.
3. **Shrink with a `while`:** keep removing from the left while the new item is still a duplicate.
4. **Each item enters and leaves the set at most once**, so the total is `O(n)`.
5. **Fixed-size window** (like "within `k` positions"): after adding, if the set is larger than `k`, remove the item that fell out.
6. **Map instead of set** when you want to jump `left` directly: store the last index of each character.

| Problem | Window | Rule |
|---|---|---|
| Longest substring without repeats | Variable | All characters unique |
| Contains Duplicate II | Fixed size `k` | No duplicate within `k` positions |
| Max sum of distinct subarray of size `k` (LeetCode 2461) | Fixed size `k` | All `k` items distinct |

#### 5. Algorithm — Must Know

```text
Variable window:
left = 0; window = empty set; best = 0
for right in 0 until n:
    while s[right] is in window:
        window.remove(s[left]); left++
    window.add(s[right])
    best = max(best, right - left + 1)

Fixed window of size k (duplicate within k):
for i in 0 until n:
    if window.add(nums[i]) is false: return true
    if window.size > k: window.remove(nums[i - k])
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Longest Substring Without Repeating Characters
fun lengthOfLongestSubstring(s: String): Int {
    val window = HashSet<Char>()
    var left = 0
    var best = 0
    for (right in s.indices) {
        while (s[right] in window) {
            window.remove(s[left])
            left++
        }
        window.add(s[right])
        best = maxOf(best, right - left + 1)
    }
    return best
}

// Contains Duplicate II — two equal values at most k positions apart
fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
    val window = HashSet<Int>()
    for (i in nums.indices) {
        if (!window.add(nums[i])) return true
        if (window.size > k) window.remove(nums[i - k])
    }
    return false
}

// Faster jump with a map (last index of each character)
fun lengthOfLongestSubstringMap(s: String): Int {
    val lastSeen = HashMap<Char, Int>()
    var left = 0
    var best = 0
    for (right in s.indices) {
        val prev = lastSeen[s[right]]
        if (prev != null && prev >= left) left = prev + 1
        lastSeen[s[right]] = right
        best = maxOf(best, right - left + 1)
    }
    return best
}
```

Checks: `"abcabcbb"` → `3`. `"bbbbb"` → `1`. `"pwwkew"` → `3`. `containsNearbyDuplicate([1,2,3,1], 3)` → `true`.

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| Longest unique substring | `O(n)` | `O(min(n, alphabet))` |
| Contains Duplicate II | `O(n)` | `O(k)` |
| Brute force substrings | `O(n²)` or `O(n³)` | — |

Each character is added once and removed once, so the `while` loop does not make it `O(n²)`.

#### 8. Common HashSet + Window Patterns — Must Know

1. **Longest Substring Without Repeating Characters** (LeetCode 3).
2. **Contains Duplicate II** (LeetCode 219) — fixed window.
3. **Maximum Sum of Distinct Subarrays With Length K** (LeetCode 2461) — set plus running sum (a map of counts also works).
4. **Longest subarray with unique items** — the same idea with numbers.
5. **Substring problems with a limited number of distinct characters** — a map of counts is needed, not just a set.
6. **Longest Nice Subarray, repeating elements** — set variants.

#### 9. Edge Cases / Common Mistakes

1. Using `if` instead of `while` when shrinking. Several items may need to be removed.
2. Adding the new item before the shrink loop finishes.
3. Wrong length: `right - left + 1`.
4. In the fixed window: removing `nums[i - k]` too early or too late. The set should hold at most the last `k` items.
5. Empty string. The answer is `0`.
6. Using a set when counts are needed ("at most 2 distinct characters" needs a map).
7. In the map version: forgetting `prev >= left`, so `left` jumps backward.

#### 10. When to Use / When Not to Use

**Use when:**

1. The rule is about **uniqueness** inside a contiguous range.

**Use a map instead when:**

1. You need counts, or the exact last index of an item.

**Avoid when:**

1. The range is not contiguous (subsequences). Use another technique.

#### 11. Related Topics

1. Sliding Window (`03-leetcode-patterns`, topic 5)
2. HashSet with Strings / Characters
3. Duplicate Detection
4. HashSet + Two Pointers

#### 12. Interview Must Remember

1. **The set holds exactly the current window.**
2. **Shrink from the left with a `while` until the rule is valid again.**
3. `O(n)`: each item enters and leaves the set once.
4. Counts needed → `HashMap`, not `HashSet`.
