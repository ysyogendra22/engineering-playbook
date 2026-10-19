# Subarray Sum Patterns

#### 1. Definition — Must Know

1. **Subarray sum patterns** are problems about contiguous parts of an array whose sum (or a property of the sum) matches a rule.
2. They all use the same engine: **running prefix value + a map of earlier prefix values**.
3. What changes is **what you store as the prefix** (the sum, the remainder, a balance) and **what you store in the map** (a count or a first index).

#### 2. Why It Is Used — Must Know

1. Once you know the engine, many "hard-looking" problems become the same short solution.
2. They are very common in interviews.
3. Choosing the right prefix value is the real skill.

#### 3. How It Works — Must Know

Same engine, different prefix:

```text
Sum equals k                → prefix = running sum,        look for sum - k
Sum divisible by k          → prefix = running sum % k,    look for the SAME remainder
Equal numbers of 0 and 1    → prefix = balance (+1 / -1),  look for the SAME balance
```

*Contiguous Array* (LeetCode 525): longest subarray with equal 0s and 1s. Treat `0` as `-1`.

```text
nums = [0, 1, 0]         balance after each element: -1, 0, -1

first = {0: -1}          ← before the array, balance is 0, at index -1
i=0  balance -1   not seen → first[-1]=0
i=1  balance  0   seen at -1 → length 1-(-1) = 2         ([0,1])
i=2  balance -1   seen at 0  → length 2-0 = 2            ([1,0])

Answer: 2
```

Two equal prefix values at `j` and `i` mean the part between them adds to zero (balance), or to a multiple of `k` (remainder).

#### 4. Core Concepts — Must Know

| Problem | Prefix value | Map stores | Lookup |
|---|---|---|---|
| Subarray Sum = k (count) | `sum` | prefix → count | `sum - k` |
| Longest subarray, sum = k | `sum` | prefix → first index | `sum - k` |
| Divisible by k (count) | `sum mod k` | remainder → count | same remainder |
| Continuous Subarray Sum | `sum mod k` | remainder → first index | same remainder |
| Equal 0s and 1s | balance | balance → first index | same balance |

1. **Equal prefixes mean the middle part is "zero".** The sum between them is `0` (or a multiple of `k`).
2. **Fix negative remainders:** in Kotlin `-1 % 5 == -1`. Use `((sum % k) + k) % k`.
3. **Longest → first index; count → count.**
4. **Length at least 2** (Continuous Subarray Sum): compare `i - firstIndex >= 2`.

#### 5. Algorithm — Must Know

```text
map = { startState : startValue }          // {0: 1} for counting, {0: -1} for first index
state = 0
for i, x in nums:
    state = update(state, x)               // add, mod, or +1/-1
    look up the needed state in the map
    store the state (count it, or keep the first index)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Subarray Sums Divisible by K — count
fun subarraysDivByK(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    count[0] = 1
    var sum = 0
    var answer = 0
    for (x in nums) {
        sum = ((sum + x) % k + k) % k          // keep the remainder non-negative
        answer += count[sum] ?: 0
        count[sum] = (count[sum] ?: 0) + 1
    }
    return answer
}

// Continuous Subarray Sum — is there a subarray of length >= 2 whose sum is a multiple of k?
fun checkSubarraySum(nums: IntArray, k: Int): Boolean {
    val firstIndex = HashMap<Int, Int>()
    firstIndex[0] = -1
    var sum = 0
    for ((i, x) in nums.withIndex()) {
        sum = (sum + x) % k                    // k > 0 and numbers >= 0 in this problem
        val j = firstIndex[sum]
        if (j != null) {
            if (i - j >= 2) return true
        } else {
            firstIndex[sum] = i                // keep the earliest index only
        }
    }
    return false
}

// Contiguous Array — longest subarray with equal 0s and 1s
fun findMaxLength(nums: IntArray): Int {
    val firstIndex = HashMap<Int, Int>()
    firstIndex[0] = -1
    var balance = 0
    var best = 0
    for ((i, x) in nums.withIndex()) {
        balance += if (x == 1) 1 else -1
        val j = firstIndex[balance]
        if (j != null) best = maxOf(best, i - j) else firstIndex[balance] = i
    }
    return best
}
```

Checks: `subarraysDivByK([4,5,0,-2,-3,1], 5)` → `7`. `checkSubarraySum([23,2,4,6,7], 6)` → `true`. `findMaxLength([0,1,0])` → `2`.

The plain "sum equals k" versions are in "Prefix Sum + HashMap".

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| All of the above | `O(n)` | `O(n)` (remainders: `O(min(n, k))`) |
| Brute force | `O(n²)` | `O(1)` |

#### 8. Common Subarray-Sum Patterns — Must Know

1. **Subarray Sum Equals K** (LeetCode 560).
2. **Subarray Sums Divisible by K** (LeetCode 974).
3. **Continuous Subarray Sum** (LeetCode 523).
4. **Contiguous Array** (LeetCode 525).
5. **Binary Subarrays With Sum** (LeetCode 930).
6. **Maximum Size Subarray Sum Equals k** (LeetCode 325, premium).
7. **Count Number of Nice Subarrays** (LeetCode 1248) — treat odd as `1`, even as `0`, then count sum `k`.
8. **Make Sum Divisible by P** (LeetCode 1590) — remainder and shortest subarray.

#### 9. Edge Cases / Common Mistakes

1. Negative remainders: `-3 % 5 == -3` in Kotlin. Fix with `+ k` and `% k` again.
2. Forgetting the starting entry (`{0: 1}` or `{0: -1}`).
3. Overwriting the first index. Only store it if it is missing.
4. Checking length `>= 2` wrongly (`i - j > 2`).
5. `k = 0` in the divisibility problems (division by zero). Handle it separately if allowed.
6. Mixing up count maps and first-index maps.
7. `Int` overflow of the sum.
8. Using sliding window for these (it breaks with negatives).

#### 10. When to Use / When Not to Use

**Use when:**

1. The question is about contiguous parts, sums, remainders, or balances.

**Avoid when:**

1. The parts do not need to be contiguous (subsequences). Use DP or sorting.
2. Numbers are positive and a window works with `O(1)` space.

#### 11. Related Topics

1. Prefix Sum + HashMap
2. HashMap + Prefix Sum Advanced Patterns
3. Counting Pairs / Complements
4. Prefix Sum (`03-leetcode-patterns`, topic 7)

#### 12. Interview Must Remember

1. **Same engine, different prefix:** sum, remainder, or balance.
2. **Equal prefixes ⇒ the part between them is zero / a multiple of `k`.**
3. Count → count map. Longest → first-index map.
4. Fix negative remainders. Start with `{0: 1}` or `{0: -1}`.
