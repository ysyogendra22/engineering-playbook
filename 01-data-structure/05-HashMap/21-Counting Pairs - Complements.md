# Counting Pairs / Complements

#### 1. Definition — Must Know

1. These problems ask **how many pairs** `(i, j)` with `i < j` satisfy a rule, such as "equal", "sum is `target`", or "sum is divisible by `k`".
2. The method: go left to right and keep a map of **counts of earlier values**. For each new item, **add the count of its complement** to the answer, then record the item.
3. It is Two Sum, but **counting** instead of returning indices.

#### 2. Why It Is Used — Must Know

1. Brute force checks every pair (`O(n²)`). Counting uses one pass (`O(n)`).
2. It handles duplicates correctly because the map holds counts, not just yes/no.
3. It appears with sums, differences, remainders, and equal values.

#### 3. How It Works — Must Know

*Number of Good Pairs* (LeetCode 1512): count pairs `i < j` with `nums[i] == nums[j]`.

`nums = [1, 2, 3, 1, 1, 3]`

```text
count = {}                    answer = 0
x=1  seen before 0 times → answer += 0     count {1:1}
x=2  0 times             → answer += 0     count {1:1, 2:1}
x=3  0 times             → answer += 0     count {1:1, 2:1, 3:1}
x=1  1 time              → answer += 1     count {1:2, ...}       pair (0,3)
x=1  2 times             → answer += 2     count {1:3, ...}       pairs (0,4) (3,4)
x=3  1 time              → answer += 1     count {..., 3:2}       pair (2,5)

Answer: 4
```

Each new item forms a pair with **every earlier item that matches its complement**. The count of earlier matches is exactly the number of new pairs.

#### 4. Core Concepts — Must Know

1. **Complement** depends on the rule:

| Rule | Complement of `x` |
|---|---|
| `a[i] == a[j]` | `x` |
| `a[i] + a[j] == target` | `target - x` |
| `a[i] - a[j] == k` | `x - k` (and/or `x + k`) |
| `(a[i] + a[j]) % m == 0` | remainder `(m - x % m) % m` |

2. **Look up first, then add `x`.** This keeps `i < j` and stops an item from pairing with itself.
3. **Counts, not just presence.** If the complement appeared 3 times, add 3.
4. **Remainders:** count remainders in an `IntArray(m)` when `m` is small and fixed.
5. **Equal values** (`x == complement`) are handled automatically by lookup-before-add.
6. **Result size:** the count can reach `n²/2`. Use `Long` for big inputs.

#### 5. Algorithm — Must Know

```text
count = empty map; answer = 0
for x in nums:
    answer += count[complement(x)] (or 0)
    count[x] += 1
return answer
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Number of Good Pairs — equal values
fun numIdenticalPairs(nums: IntArray): Int {
    val count = HashMap<Int, Int>()
    var answer = 0
    for (x in nums) {
        val c = count[x] ?: 0
        answer += c
        count[x] = c + 1
    }
    return answer
}

// Count pairs with sum == target
fun countPairsWithSum(nums: IntArray, target: Int): Long {
    val count = HashMap<Int, Int>()
    var answer = 0L
    for (x in nums) {
        answer += count[target - x] ?: 0
        count[x] = (count[x] ?: 0) + 1
    }
    return answer
}

// Pairs of Songs With Total Durations Divisible by 60 — remainders in an array
fun numPairsDivisibleBy60(time: IntArray): Int {
    val remainder = IntArray(60)
    var answer = 0
    for (t in time) {
        val r = t % 60
        answer += remainder[(60 - r) % 60]      // partner remainder
        remainder[r]++
    }
    return answer
}

// K-diff Pairs in an Array — count UNIQUE pairs with |a - b| == k
fun findPairs(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    for (x in nums) count[x] = (count[x] ?: 0) + 1
    var pairs = 0
    for ((value, c) in count) {
        if (k == 0) { if (c > 1) pairs++ }
        else if ((value + k) in count) pairs++
    }
    return pairs
}
```

Checks: `numIdenticalPairs([1,2,3,1,1,3])` → `4`. `numPairsDivisibleBy60([30,20,150,100,40])` → `3`. `findPairs([3,1,4,1,5], 2)` → `2`.

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Brute force | `O(n²)` | `O(1)` |
| **Count map, one pass** | **`O(n)`** | `O(u)` |
| Remainder array of size `m` | `O(n + m)` | `O(m)` |

#### 8. Common Pair-Counting Patterns — Must Know

1. **Number of Good Pairs** (LeetCode 1512).
2. **Pairs of Songs Divisible by 60** (LeetCode 1010).
3. **K-diff Pairs in an Array** (LeetCode 532).
4. **Count Number of Bad Pairs** (LeetCode 2364) — rewrite the rule as `nums[i] - i`, then count equal values.
5. **Max Number of K-Sum Pairs** (LeetCode 1679) — use up pairs as you match them.
6. **Number of Pairs of Interchangeable Rectangles** (LeetCode 2001) — ratio as the key.
7. **4Sum II** (LeetCode 454) — counts of pair sums.
8. **Subarray version:** counts of prefix values (`Prefix Sum + HashMap`).

#### 9. Edge Cases / Common Mistakes

1. Adding the current value before the lookup, so each item pairs with itself.
2. Counting each pair twice (once as `(i, j)` and once as `(j, i)`).
3. Using a set, which loses duplicates, when counts are needed.
4. Negative remainders: use `((x % m) + m) % m` for negative numbers.
5. Remainder `0` partner: it is `0`, not `m`. Use `(m - r) % m`.
6. `Int` overflow in the answer. Use `Long` for large inputs.
7. In K-diff pairs: counting a pair once per value. Check `k == 0` separately.
8. Max K-Sum Pairs: not decreasing the complement's count after using it.

#### 10. When to Use / When Not to Use

**Use when:**

1. You count pairs by a rule that can be turned into "find the complement".

**Avoid when:**

1. You must list the pairs themselves. Use two pointers or store indices.
2. The array is sorted and `O(1)` space is required. Use two pointers.

#### 11. Related Topics

1. Two Sum Pattern
2. Frequency Counting
3. Prefix Sum + HashMap
4. Subarray Sum Patterns

#### 12. Interview Must Remember

1. **Look up the complement's count first, then add the current item.**
2. Counts handle duplicates; a set does not.
3. Remainder partner: `(m - r) % m`.
4. `O(n)` time. Use `Long` if the count can be large.
