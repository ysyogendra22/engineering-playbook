# Boyer-Moore Majority Vote

#### 1. What Is It?

The **Boyer-Moore voting algorithm** finds the **majority element** (an element that appears **more than `n / 2` times**) in **one pass** with **`O(1)` space**.

The idea is a vote with cancelling:

- Keep a **candidate** and a **count**.
- If the next item equals the candidate, `count++`. Otherwise `count--`.
- If the count drops to `0`, take the next item as the new candidate.

Why it works: each time a non-majority item cancels a majority item, one of each is removed. The majority element has more than half of all votes, so it cannot be cancelled out completely.

How to spot it: "element that appears more than `n / 2` times" (or more than `n / 3`), and the follow-up says "`O(n)` time and `O(1)` space".

#### 2. How It Works

`nums = [2, 2, 1, 1, 1, 2, 2]`

```text
x=2: count 0 → candidate=2, count=1
x=2: same → count=2
x=1: different → count=1
x=1: different → count=0
x=1: count 0 → candidate=1, count=1
x=2: different → count=0
x=2: count 0 → candidate=2, count=1

candidate = 2  ✓ (it appears 4 times out of 7)
```

If the question does **not** promise that a majority element exists, run a **second pass** to count the candidate and check that it is above `n / 2`.

For **more than `n / 3`** (*Majority Element II*), there can be up to **two** such elements. Keep two candidates and two counts, then verify both.

#### 3. Brute Force vs Optimized

| | Brute force | HashMap | Boyer-Moore |
|---|---|---|---|
| Idea | count each item with a loop | count in a map | cancelling votes |
| Time | `O(n²)` | `O(n)` | `O(n)` |
| Space | `O(1)` | `O(n)` | `O(1)` |

```kotlin
fun majorityElementMap(nums: IntArray): Int {
    val count = HashMap<Int, Int>()
    for (x in nums) {
        val c = (count[x] ?: 0) + 1
        count[x] = c
        if (c > nums.size / 2) return x
    }
    return -1
}
```

#### 4. Kotlin Code

```kotlin
// Majority Element (LeetCode 169): it is guaranteed to exist
fun majorityElement(nums: IntArray): Int {
    var candidate = 0
    var count = 0
    for (x in nums) {
        if (count == 0) candidate = x
        count += if (x == candidate) 1 else -1
    }
    return candidate
}

// If a majority may not exist, verify
fun majorityOrNull(nums: IntArray): Int? {
    val candidate = majorityElement(nums)
    return if (nums.count { it == candidate } > nums.size / 2) candidate else null
}

// Majority Element II (LeetCode 229): all elements that appear more than n / 3 times
fun majorityElementII(nums: IntArray): List<Int> {
    var c1 = 0; var c2 = 1                    // two different candidates at the start
    var n1 = 0; var n2 = 0
    for (x in nums) {
        when {
            x == c1 -> n1++
            x == c2 -> n2++
            n1 == 0 -> { c1 = x; n1 = 1 }
            n2 == 0 -> { c2 = x; n2 = 1 }
            else -> { n1--; n2-- }
        }
    }
    val limit = nums.size / 3
    val result = mutableListOf<Int>()
    if (nums.count { it == c1 } > limit) result.add(c1)
    if (nums.count { it == c2 } > limit) result.add(c2)
    return result
}
```

Checks: `majorityElement([2,2,1,1,1,2,2])` → `2`. `majorityElement([3,2,3])` → `3`. `majorityElementII([3,2,3])` → `[3]`. `majorityElementII([1,1,1,3,3,2,2,2])` → `[2, 1]` (the order does not matter).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Boyer-Moore | `O(n)` | `O(1)` |
| HashMap | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Skipping the verification pass** when a majority is not guaranteed.
2. **Using it for "at least `n / 2`"** (the standard algorithm needs strictly more than half).
3. **Majority II: two candidates starting with the same value.** Start them as different values (`0` and `1`) and always verify.
4. **Updating the count before choosing the candidate** when `count == 0`.
5. **Thinking the candidate is always right.** It is only right if a majority exists.

#### 7. Say This in the Interview

1. "A HashMap gives `O(n)` time but `O(n)` space. Boyer-Moore voting does it in `O(n)` time and `O(1)` space."
2. "Equal items add a vote, different items cancel one. The majority element has more than half the votes, so it survives."
3. "If a majority is not guaranteed, I make a second pass to confirm."

#### 8. Quick Check

1. How many candidates are needed for "more than `n / 3`"?
2. What is the count when a different item arrives?

<details>
<summary>Answers</summary>

1. Two (at most two items can appear more than a third of the time).
2. It goes down by one.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) (Easy) | one candidate |
| 229 | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) (Medium) | two candidates |
| 1150 | [Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy, premium) | binary search |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) (Easy) | XOR for `O(1)` space |
