# Two Sum Pattern

#### 1. Definition — Must Know

1. **Two Sum** (LeetCode 1): given an array and a `target`, return the **indices** of two numbers that add up to the target.
2. The HashMap solution stores `value → index` for numbers already seen, and for each number looks for its **complement** `target - x`.
3. If you only need *whether* a pair exists, a `HashSet` is enough (see `01-data-structure/06-HashSet/07`). A map is needed when you need **indices or counts**.

#### 2. Why It Is Used — Must Know

1. It beats brute force `O(n²)` with a one-pass `O(n)` solution.
2. It is the most asked interview question, and the idea repeats in many problems.
3. It teaches the habit: "for this item, which partner am I looking for?".

#### 3. How It Works — Must Know

`nums = [3, 2, 4]`, `target = 6`

```text
seen = {}                                   value → index
i=0  x=3   need 6-3=3   in seen? no    → store 3→0      seen = {3:0}
i=1  x=2   need 6-2=4   in seen? no    → store 2→1      seen = {3:0, 2:1}
i=2  x=4   need 6-4=2   in seen? YES (index 1)  → answer [1, 2]
```

**Check first, then store.** Otherwise `3` could pair with itself in `[3]` with `target = 6`.

Duplicates still work: `nums = [3, 3]`, `target = 6`:

```text
i=0  x=3  need 3  not in seen → store 3→0
i=1  x=3  need 3  in seen (index 0) → answer [0, 1]
```

#### 4. Core Concepts — Must Know

1. **Complement = `target - x`.**
2. **Map `value → index`.** Later duplicates may overwrite earlier indices; that is fine because we check before storing.
3. **One pass.** Each item is checked once and stored once.
4. **Variations change the complement:**

| Variation | Complement / idea |
|---|---|
| Difference `k` | look for `x - k` and `x + k` |
| Count pairs | store counts; add `count[target - x]` |
| Sorted array | two pointers, no map (`O(1)` space) |
| Three numbers | fix one, then solve Two Sum on the rest (3Sum) |
| Four lists (4Sum II) | map of pair sums from two lists |
| Data structure design | `add(x)` and `find(sum)` with a count map |

5. **Two Sum design (LeetCode 170, premium):** `add(x)` stores `count[x]++`; `find(sum)` checks each key `k`: if `sum - k == k` it needs count ≥ 2, otherwise `sum - k` must exist.

#### 5. Algorithm — Must Know

```text
seen = empty map (value → index)
for i, x in nums:
    j = seen[target - x]
    if j exists: return [j, i]
    seen[x] = i
return no answer
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun twoSum(nums: IntArray, target: Int): IntArray {
    val seen = HashMap<Int, Int>()            // value → index
    for ((i, x) in nums.withIndex()) {
        val j = seen[target - x]
        if (j != null) return intArrayOf(j, i)
        seen[x] = i
    }
    return intArrayOf()
}
```

**4Sum II** (LeetCode 454): count tuples `(i, j, k, l)` with `a[i] + b[j] + c[k] + d[l] == 0`.

```kotlin
fun fourSumCount(a: IntArray, b: IntArray, c: IntArray, d: IntArray): Int {
    val sums = HashMap<Int, Int>()              // sum of a+b → how many ways
    for (x in a) for (y in b) {
        val s = x + y
        sums[s] = (sums[s] ?: 0) + 1
    }
    var count = 0
    for (x in c) for (y in d) {
        count += sums[-(x + y)] ?: 0
    }
    return count
}
```

**Two Sum design with counts**

```kotlin
class TwoSum {
    private val count = HashMap<Int, Int>()

    fun add(number: Int) {
        count[number] = (count[number] ?: 0) + 1
    }

    fun find(value: Int): Boolean {
        for ((num, c) in count) {
            val other = value - num
            if (other == num) { if (c > 1) return true }
            else if (other in count) return true
        }
        return false
    }
}
```

**Sorted input, two pointers** (see `01-data-structure/06-HashSet/15`): `O(n)` time and `O(1)` space.

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Brute force | `O(n²)` | `O(1)` |
| **HashMap, one pass** | **`O(n)`** | `O(n)` |
| Sort + two pointers | `O(n log n)` | `O(1)` extra (indices lost) |
| 4Sum II with a map | `O(n²)` | `O(n²)` |
| Two Sum design: `add` / `find` | `O(1)` / `O(u)` | `O(u)` |

#### 8. Common Two Sum Patterns — Must Know

1. **Two Sum** (LeetCode 1).
2. **Two Sum II, sorted** (LeetCode 167) — two pointers.
3. **3Sum** (LeetCode 15) — sort + two pointers.
4. **4Sum II** (LeetCode 454) — map of pair sums.
5. **K-diff Pairs in an Array** (LeetCode 532) — map of counts.
6. **Pairs of Songs With Total Durations Divisible by 60** (LeetCode 1010) — remainder counts (see "Counting Pairs / Complements").
7. **Subarray Sum Equals K** (LeetCode 560) — the same idea over prefix sums.

#### 9. Edge Cases / Common Mistakes

1. Storing before checking, so one number pairs with itself.
2. Using a set when indices are needed.
3. Sorting first and then losing the original indices.
4. Overflow in `target - x` or `x + y`. Use `Long` if values are extreme.
5. Returning `[i, i]`.
6. Not handling "no answer" (return an empty array or `null`).
7. In the design version, forgetting that `x + x == target` needs two copies.
8. Assuming exactly one answer when the problem does not promise it.

#### 10. When to Use / When Not to Use

**Use the map when:**

1. The array is unsorted and you need indices.

**Use two pointers when:**

1. The array is sorted (or indices do not matter) and memory is tight.

**Use a set when:**

1. You only need a yes/no answer.

#### 11. Related Topics

1. Counting Pairs / Complements
2. Prefix Sum + HashMap
3. HashSet — Two Sum / Complement Lookup (`01-data-structure/06-HashSet/07-Two Sum - Complement Lookup with HashSet.md`)
4. Two Pointers (`03-leetcode-patterns`, topic 4)

#### 12. Interview Must Remember

1. **Map `value → index`. Look for `target - x` before storing `x`.**
2. `O(n)` time, `O(n)` space.
3. Sorted input → two pointers. Only yes/no → set.
4. The same complement idea works for prefix sums, differences, and remainders.
