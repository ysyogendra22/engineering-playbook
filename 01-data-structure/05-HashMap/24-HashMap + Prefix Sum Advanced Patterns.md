# HashMap + Prefix Sum Advanced Patterns

> Read notes 11 and 12 first. Here the "prefix" is not always a sum.

#### 1. What Is It?

The basic pattern stores **prefix sums** in a map. The advanced version stores **any state that you can update one element at a time**: an XOR value, a bitmask of odd/even counts, a count of odd numbers.

The rule is the same:

> **Two equal prefix states mean the part between them is "neutral"** (XOR 0, every count even, balance 0).

So the question becomes "find two equal states" or "find a state at a fixed offset".

#### 2. How It Works

**XOR prefix.** `a xor a = 0`, so the XOR of a subarray is `prefix[i] xor prefix[j]`. To get a subarray with XOR `k`, look for `prefix[i] xor k` in the map.

**Bitmask of parities** (*Find the Longest Substring Containing Vowels in Even Counts*, LeetCode 1371). Keep 5 bits, one per vowel. Each time you see a vowel, **flip its bit**. If the same mask appeared before, every vowel appeared an even number of times in between.

```text
bit0=a  bit1=e  bit2=i  bit3=o  bit4=u

s = "eleetminicoworoep"
the mask starts as 00000.  'e' flips bit1, 'l' does nothing, 'e' flips bit1 back...
mask 00000 is seen at index -1 (before the string) and again at index 2
→ "ele" has "e" twice (even) → a valid substring of length 3
The best answer for this input is 13.
```

Which state for which question:

| Question | State | Map stores | Look up |
|---|---|---|---|
| Subarrays with XOR `k` (count) | running XOR | state → count | `state xor k` |
| Vowels all even (longest) | 5-bit mask | mask → first index | the same mask |
| Nice Subarrays: exactly `k` odd numbers | how many odd numbers so far | count → how many times | `odd - k` |
| Binary Subarrays With Sum | running sum | sum → count | `sum - goal` |
| Equal 0s and 1s | balance | balance → first index | the same balance |

#### 3. Kotlin Code

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
    val firstIndex = IntArray(32) { -2 }             // -2 means "not seen yet"
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

// Count Number of Nice Subarrays (LeetCode 1248): exactly k odd numbers
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

// Binary Subarrays With Sum (LeetCode 930)
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

Checks: `countSubarraysXor([4,2,2,6,4], 6)` → `4`. `numberOfSubarrays([1,1,2,1,1], 3)` → `2`. `findTheLongestSubstring("eleetminicoworoep")` → `13`.

#### 4. Complexity

| Problem | Time | Space |
|---|---|---|
| XOR subarrays | `O(n)` | `O(n)` |
| Vowel mask | `O(n)` | `O(1)` (32 slots) |
| Nice subarrays | `O(n)` | `O(n)` |
| Brute force | `O(n²)` | — |

#### 5. Common Mistakes

1. **Choosing a state that loses information** the question needs.
2. **Forgetting the empty prefix** (`0` with count `1`, or index `-1`).
3. **Overwriting the first index** when you want the longest range.
4. **Using `-1` as "not seen"** when `-1` is also the empty-prefix index. The vowel code uses `-2` for "not seen".
5. **Wrong bit for a vowel**, or one bit used for two letters.
6. **Looking up after storing.**
7. **Using it for subsequences.** It only works for **contiguous** parts.

#### 6. Say This in the Interview

1. "The answer needs two equal prefix states, so I keep a map from state to first index (or count)."
2. "For 'every count even' the state is a bitmask of parities. For XOR questions I look up `state xor k`."
3. "One pass: `O(n)` time."

#### 7. Quick Check

1. What is the XOR of `a` with itself?
2. In the vowel problem, what does a repeated mask tell you?

<details>
<summary>Answers</summary>

1. `0`.
2. In the part between the two positions, every vowel appeared an even number of times.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1371 | Find the Longest Substring Containing Vowels in Even Counts (Medium) | bitmask of parities |
| 1248 | Count Number of Nice Subarrays (Medium) | count of odd numbers |
| 930 | Binary Subarrays With Sum (Medium) | same shape as 560 |
| 525 | Contiguous Array (Medium) | balance (note 12) |
| 974 | Subarray Sums Divisible by K (Medium) | remainders (note 12) |
| 1074 | Number of Submatrices That Sum to Target (Hard) | fix two rows, then 1D prefix sums |
