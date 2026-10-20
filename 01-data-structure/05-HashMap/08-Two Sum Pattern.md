# Two Sum Pattern

> The most famous interview question. The idea "look for the partner" appears in many other problems.

#### 1. What Is It?

**Two Sum** (LeetCode 1): given an array and a `target`, return the **indexes** of two numbers that add up to the target.

Slow way: check every pair (`O(n²)`).

Fast way with a HashMap:

- For each number `x`, the number you need is its **complement**: `target - x`.
- Keep a map `value → index` of the numbers you have already seen.
- If the complement is in the map, you found the pair.

If you only need a **yes/no** answer, a `HashSet` is enough. You need a **map** when you must return **indexes** or **counts**.

#### 2. How It Works

`nums = [3, 2, 4]`, `target = 6`

```text
seen = {}                              (value → index)
i=0  x=3  need 6-3 = 3  in seen? no  → store 3→0     seen = {3:0}
i=1  x=2  need 6-2 = 4  in seen? no  → store 2→1     seen = {3:0, 2:1}
i=2  x=4  need 6-4 = 2  in seen? YES (index 1)       → answer [1, 2]
```

**Check first, then store.** If you store first, `3` could pair with itself when `target = 6` and the array is `[3]`.

Duplicates still work: `nums = [3, 3]`, `target = 6`.

```text
i=0  x=3  need 3  not seen → store 3→0
i=1  x=3  need 3  seen at index 0 → answer [0, 1]
```

The same idea in other problems:

| Problem | Complement / idea |
|---|---|
| Sorted array | two pointers, no map (`O(1)` space) |
| 4Sum II | map of all sums of two arrays |
| Difference `k` | look for `x - k` and `x + k` |
| Two Sum design | `add(x)` and `find(sum)` with a count map |

#### 3. Kotlin Code

```kotlin
fun twoSum(nums: IntArray, target: Int): IntArray {
    val seen = HashMap<Int, Int>()                 // value → index
    for ((i, x) in nums.withIndex()) {
        val j = seen[target - x]
        if (j != null) return intArrayOf(j, i)     // the partner was seen earlier
        seen[x] = i                                // store AFTER checking
    }
    return intArrayOf()
}

// 4Sum II (LeetCode 454): count tuples with a[i] + b[j] + c[k] + d[l] == 0
fun fourSumCount(a: IntArray, b: IntArray, c: IntArray, d: IntArray): Int {
    val sums = HashMap<Int, Int>()                 // sum of one a and one b → how many ways
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

// Two Sum design: add numbers, then ask "is there a pair with this sum?"
class TwoSum {
    private val count = HashMap<Int, Int>()

    fun add(number: Int) {
        count[number] = (count[number] ?: 0) + 1
    }

    fun find(value: Int): Boolean {
        for ((num, c) in count) {
            val other = value - num
            if (other == num) { if (c > 1) return true }       // needs two copies of the same number
            else if (other in count) return true
        }
        return false
    }
}

// Sorted array: two pointers, O(1) space
fun hasPairSorted(nums: IntArray, target: Int): Boolean {
    var l = 0
    var r = nums.size - 1
    while (l < r) {
        val sum = nums[l] + nums[r]
        when {
            sum == target -> return true
            sum < target -> l++
            else -> r--
        }
    }
    return false
}
```

#### 4. Complexity

| Way | Time | Space |
|---|---|---|
| Brute force | `O(n²)` | `O(1)` |
| **HashMap, one pass** | **`O(n)`** | `O(n)` |
| Sorted array, two pointers | `O(n)` | `O(1)` |
| 4Sum II with a map | `O(n²)` | `O(n²)` |

#### 5. Common Mistakes

1. **Storing before checking.** A number can pair with itself.
2. **Using a set when you need indexes.**
3. **Sorting first and losing the original indexes.**
4. **Overflow** in `x + y` or `target - x` for huge values. Use `Long`.
5. **Returning the same index twice.**
6. **Not handling "no answer".** Return an empty array or `null` (or the question guarantees one answer).
7. **Two Sum design:** forgetting that `x + x == target` needs **two** copies of `x`.

#### 6. Say This in the Interview

1. "Brute force is `O(n²)`. For each number I need `target - x`, so I keep a map of value to index for numbers I have seen."
2. "I check the complement first, then store the current number."
3. "That is one pass: `O(n)` time and `O(n)` space. If the array were sorted I would use two pointers with `O(1)` space."

#### 7. Quick Check

1. For `nums = [2, 7, 11, 15]` and `target = 9`, what is returned?
2. Why check before storing?

<details>
<summary>Answers</summary>

1. `[0, 1]` (the numbers `2` and `7`).
2. So a number cannot be paired with itself.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1 | Two Sum (Easy) | this note |
| 167 | Two Sum II, Input Array Is Sorted (Medium) | two pointers |
| 15 | 3Sum (Medium) | sort + two pointers |
| 454 | 4Sum II (Medium) | map of pair sums |
| 653 | Two Sum IV, Input Is a BST (Easy) | a set while walking the tree |
| 170 | Two Sum III, Data Structure Design (Easy, premium) | count map |
