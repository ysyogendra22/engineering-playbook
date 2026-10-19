# HashMap + Prefix Sum Advanced Patterns

#### 1. Definition — Must Know

1. The basic pattern stores **prefix sums** in a map (`Prefix Sum + HashMap`).
2. The **advanced** version stores any **prefix state** that can be updated one element at a time: an XOR value, a bitmask of parities, a balance, a count of odd numbers.
3. Rule: **two equal prefix states mean the part between them is "neutral"** (XOR 0, all parities even, balance 0).

#### 2. Why It Is Used — Must Know

1. It turns hard-looking questions ("longest substring with every vowel an even number of times") into a short loop.
2. It shows you understand the idea, not only the Subarray Sum Equals K template.
3. These are medium and hard interview problems.

#### 3. How It Works — Must Know

**XOR prefix.** XOR undoes itself: `a xor a = 0`. So the XOR of a subarray `[j+1 .. i]` is `prefix[i] xor prefix[j]`.

```text
Want subarray XOR = k:     prefix[i] xor prefix[j] = k   →   prefix[j] = prefix[i] xor k
```

**Bitmask parity.** For "each vowel appears an even number of times", keep 5 bits, one per vowel. Each vowel flips its bit. Equal masks at `j` and `i` mean every vowel appeared an even number of times between them.

```text
s = "eleetminicoworoep"           a=bit0  e=bit1  i=bit2  o=bit3  u=bit4

mask after each character (flip the bit when you see a vowel):
e → 00010      l → 00010      e → 00000      e → 00010 ...
mask 00000 first seen at index -1 (before the string); seen again at index 2
→ the part from index 0 to 2 ("ele") has e twice (even), so length 3 is possible
```

The answer for this input is `13` (the substring `"leetminicowor"`).

#### 4. Core Concepts — Must Know

| Problem | Prefix state | Map stores | Lookup |
|---|---|---|---|
| Subarrays with XOR = k (count) | running XOR | state → count | `state xor k` |
| Longest substring, vowels all even (LeetCode 1371) | 5-bit parity mask | mask → first index | same mask |
| Count Number of Nice Subarrays (LeetCode 1248) | number of odd numbers so far | count → how many | `odd - k` |
| Binary Subarrays With Sum (LeetCode 930) | running sum of 0/1 | sum → count | `sum - goal` |
| Contiguous Array (LeetCode 525) | balance (+1 / −1) | balance → first index | same balance |
| Number of Substrings with equal counts | difference of counts | difference → count | same difference |

1. **Pick the state** so the question becomes "find two equal states" or "find a state at a fixed offset".
2. **Bitmask state** has at most `2^m` values for `m` flags, so an array of size `2^m` can replace the map.
3. **Count → map of counts. Longest → map of first indices.**
4. **Start with the empty prefix:** state `0` with count `1`, or first index `-1`.
5. **Look up before storing** the current state.

#### 5. Algorithm — Must Know

```text
state = start state (0)
map = { state : 1 }  or  { state : -1 }
for i, x in input:
    state = update(state, x)
    look up the needed partner state in the map
    store the state (count it, or keep the first index only)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Count subarrays whose XOR equals k
fun countSubarraysXor(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1
    var xor = 0
    var answer = 0
    for (x in nums) {
        xor = xor xor x
        answer += count[xor xor k] ?: 0
        count[xor] = (count[xor] ?: 0) + 1
    }
    return answer
}

// Longest substring where each vowel appears an even number of times (LeetCode 1371)
fun findTheLongestSubstring(s: String): Int {
    val firstIndex = IntArray(32) { -2 }           // -2 = not seen yet
    firstIndex[0] = -1
    var mask = 0
    var best = 0
    for ((i, c) in s.withIndex()) {
        when (c) {
            'a' -> mask = mask xor 1
            'e' -> mask = mask xor 2
            'i' -> mask = mask xor 4
            'o' -> mask = mask xor 8
            'u' -> mask = mask xor 16
        }
        if (firstIndex[mask] == -2) firstIndex[mask] = i
        else best = maxOf(best, i - firstIndex[mask])
    }
    return best
}

// Count Number of Nice Subarrays — exactly k odd numbers
fun numberOfSubarrays(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1
    var odd = 0
    var answer = 0
    for (x in nums) {
        if (x % 2 != 0) odd++
        answer += count[odd - k] ?: 0
        count[odd] = (count[odd] ?: 0) + 1
    }
    return answer
}

// Binary Subarrays With Sum (0/1 array): the same shape as Subarray Sum Equals K
fun numSubarraysWithSum(nums: IntArray, goal: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1
    var sum = 0
    var answer = 0
    for (x in nums) {
        sum += x
        answer += count[sum - goal] ?: 0
        count[sum] = (count[sum] ?: 0) + 1
    }
    return answer
}
```

Checks: `countSubarraysXor([4, 2, 2, 6, 4], 6)` → `4`. `numberOfSubarrays([1,1,2,1,1], 3)` → `2`. `findTheLongestSubstring("eleetminicoworoep")` → `13`.

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| XOR subarrays | `O(n)` | `O(n)` |
| Vowel mask | `O(n)` | `O(1)` (32 slots) |
| Nice subarrays | `O(n)` | `O(n)` |
| Brute force | `O(n²)` | — |

#### 8. Common Advanced Prefix Patterns — Must Know

1. **Count subarrays with XOR k** (also LeetCode 1442 style XOR triplets).
2. **Find the Longest Substring Containing Vowels in Even Counts** (LeetCode 1371).
3. **Count Number of Nice Subarrays** (LeetCode 1248).
4. **Binary Subarrays With Sum** (LeetCode 930).
5. **Contiguous Array** (LeetCode 525).
6. **Make Sum Divisible by P** (LeetCode 1590).
7. **Subarray Sums Divisible by K** (LeetCode 974).
8. **2D prefix sums + map:** Number of Submatrices That Sum to Target (LeetCode 1074) — fix two rows, then run the 1D pattern over columns.
9. **Sliding window alternative:** `atMost(k) - atMost(k - 1)` counts "exactly k" for non-negative arrays.

#### 9. Edge Cases / Common Mistakes

1. Choosing a state that loses information the question needs.
2. Forgetting the empty prefix (`0` with count `1` / index `-1`).
3. Overwriting the first index when you want the longest range.
4. Using `-1` as "not seen" and also as the empty-prefix index. Use a different marker, as in the vowel code (`-2`).
5. Bit positions wrong or reused for two characters.
6. Looking up after storing, which can count empty ranges.
7. `Int` overflow in sums.
8. Using it for subsequences. It only works for contiguous parts.

#### 10. When to Use / When Not to Use

**Use when:**

1. The rule can be expressed as "two equal states" or "states at a fixed offset".
2. The parts must be contiguous.

**Avoid when:**

1. A sliding window already works (non-negative numbers, `O(1)` space).
2. The rule depends on order in ways a single state cannot capture.

#### 11. Related Topics

1. Prefix Sum + HashMap
2. Subarray Sum Patterns
3. Bit Manipulation (`02-algorithm/09-Bit Manipulation`)
4. Prefix Sum (`03-leetcode-patterns`, topic 7)

#### 12. Interview Must Remember

1. **Choose a prefix state; equal states ⇒ the middle part is neutral.**
2. XOR: look for `state xor k`. Parity: use a bitmask. Balance: use `+1 / −1`.
3. Count → counts; longest → first index; start with the empty prefix.
4. Contiguous only. `O(n)` time.
