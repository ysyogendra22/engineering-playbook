# Counting Pairs / Complements

#### 1. What Is It?

These questions ask **how many pairs** `(i, j)` with `i < j` follow a rule: "equal", "sum to `target`", "divisible by `k`".

It is **Two Sum, but counting** instead of returning indexes:

- Go left to right.
- Keep a map of **how many times each earlier value appeared**.
- For each new item, **add the count of its complement** to the answer. Then record the item.

Brute force checks every pair (`O(n²)`). Counting uses one pass (`O(n)`).

#### 2. How It Works

*Number of Good Pairs* (LeetCode 1512): count pairs `i < j` with `nums[i] == nums[j]`.

`nums = [1, 2, 3, 1, 1, 3]`

```text
count = {}                    answer = 0
x=1   seen 0 times  → add 0         count {1:1}
x=2   seen 0 times  → add 0         count {1:1, 2:1}
x=3   seen 0 times  → add 0         count {1:1, 2:1, 3:1}
x=1   seen 1 time   → add 1         count {1:2, ...}      pair (0,3)
x=1   seen 2 times  → add 2         count {1:3, ...}      pairs (0,4) and (3,4)
x=3   seen 1 time   → add 1         count {..., 3:2}      pair (2,5)

answer = 4
```

Each new item forms a pair with **every earlier item** that matches its complement. The stored count is exactly the number of new pairs.

The complement depends on the rule:

| Rule | Complement of `x` |
|---|---|
| `a == b` | `x` |
| `a + b == target` | `target - x` |
| `a - b == k` | `x - k` (and/or `x + k`) |
| `(a + b) % m == 0` | the remainder `(m - x % m) % m` |

**Look up first, then add `x`.** That keeps `i < j` and stops an item from pairing with itself.

#### 3. Kotlin Code

```kotlin
// Number of Good Pairs: equal values
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

// Pairs of Songs With Total Durations Divisible by 60 (LeetCode 1010)
fun numPairsDivisibleBy60(time: IntArray): Int {
    val remainder = IntArray(60)
    var answer = 0
    for (t in time) {
        val r = t % 60
        answer += remainder[(60 - r) % 60]          // the partner remainder
        remainder[r]++
    }
    return answer
}

// K-diff Pairs in an Array (LeetCode 532): count UNIQUE pairs with |a - b| == k
fun findPairs(nums: IntArray, k: Int): Int {
    val count = HashMap<Int, Int>()
    for (x in nums) count[x] = (count[x] ?: 0) + 1
    var pairs = 0
    for ((value, c) in count) {
        if (k == 0) { if (c > 1) pairs++ }          // a pair of equal numbers
        else if ((value + k) in count) pairs++
    }
    return pairs
}
```

Checks: `numIdenticalPairs([1,2,3,1,1,3])` → `4`. `numPairsDivisibleBy60([30,20,150,100,40])` → `3`. `findPairs([3,1,4,1,5], 2)` → `2`.

#### 4. Complexity

| Way | Time | Space |
|---|---|---|
| Brute force | `O(n²)` | `O(1)` |
| **Count map, one pass** | **`O(n)`** | `O(u)` |
| Remainder array of size `m` | `O(n + m)` | `O(m)` |

#### 5. Common Mistakes

1. **Adding the current value before the lookup.** An item pairs with itself.
2. **Counting each pair twice** (as `(i, j)` and as `(j, i)`).
3. **Using a set** when counts are needed.
4. **Negative remainders.** Use `((x % m) + m) % m`.
5. **Wrong partner remainder.** It is `(m - r) % m`, not `m - r` (when `r` is `0`).
6. **Overflow** of the answer. It can reach `n²/2`, so use `Long` for big inputs.
7. **K-diff pairs:** forgetting the special case `k == 0`.

#### 6. Say This in the Interview

1. "For each item I add how many earlier items complete a pair, then I record the item. That keeps `i < j`."
2. "A count map handles duplicates, which a set cannot."
3. "One pass: `O(n)` time. I use `Long` if the count can be large."

#### 7. Quick Check

1. For `[1, 1, 1]`, how many good pairs are there?
2. Why record the current item **after** the lookup?

<details>
<summary>Answers</summary>

1. `3`: pairs (0,1), (0,2), (1,2). The code adds 0, then 1, then 2.
2. Otherwise the item would be counted as a partner of itself.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1512 | Number of Good Pairs (Easy) | equal values |
| 1010 | Pairs of Songs With Total Durations Divisible by 60 (Medium) | remainder counts |
| 532 | K-diff Pairs in an Array (Medium) | unique pairs |
| 2364 | Count Number of Bad Pairs (Medium) | rewrite the rule as `nums[i] - i`, count equal values |
| 1679 | Max Number of K-Sum Pairs (Medium) | use up pairs as you match them |
| 454 | 4Sum II (Medium) | counts of pair sums (note 08) |
