# Mapping / Index Tracking

#### 1. What Is It?

**Index tracking** stores **where** each value was seen: `value → index`.

You can keep:

- the **first** index of a value (store only if the value is new → `putIfAbsent`),
- the **last** index of a value (always overwrite → `map[x] = i`).

It lets you jump from a value to its position in `O(1)` instead of searching the array.

It is used when the question is about **distance** or **position**: "within `k` positions", "longest gap", "next greater".

| You want... | Keep |
|---|---|
| the closest earlier equal value | the **last** index |
| the longest range between equal states | the **first** index |
| the position of a value | its index |

#### 2. How It Works

*Contains Duplicate II* (LeetCode 219): are there two equal numbers at most `k` positions apart?

`nums = [1, 2, 3, 1]`, `k = 3`

```text
last = {}                                    (value → last index)
i=0  x=1   not in last          → last[1] = 0
i=1  x=2   not in last          → last[2] = 1
i=2  x=3   not in last          → last[3] = 2
i=3  x=1   last[1] = 0, distance 3 - 0 = 3 <= 3 → TRUE
```

If the distance is too big, store the **new** index (`last[x] = i`) and go on. The latest index is always the closest one for the next match.

*Next Greater Element I* (LeetCode 496) uses the map the other way: after a stack finds each number's next greater value, the map `number → next greater` answers the queries.

#### 3. Kotlin Code

```kotlin
// Contains Duplicate II: keep the LAST index of each value
fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
    val last = HashMap<Int, Int>()
    for ((i, x) in nums.withIndex()) {
        val j = last[x]
        if (j != null && i - j <= k) return true
        last[x] = i
    }
    return false
}

// Next Greater Element I: map each value to its next greater value
fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
    val nextGreater = HashMap<Int, Int>()
    val stack = ArrayDeque<Int>()
    for (n in nums2) {
        while (stack.isNotEmpty() && stack.last() < n) {
            nextGreater[stack.removeLast()] = n
        }
        stack.addLast(n)
    }
    return IntArray(nums1.size) { nextGreater[nums1[it]] ?: -1 }
}

// First index of each value (keep the earliest)
fun firstIndexMap(nums: IntArray): Map<Int, Int> {
    val first = HashMap<Int, Int>()
    for ((i, x) in nums.withIndex()) first.putIfAbsent(x, i)
    return first
}

// Index of every value in one line (the last index wins for repeats)
fun indexMap(nums: IntArray): Map<Int, Int> =
    nums.withIndex().associate { (i, x) -> x to i }
```

Check: `nextGreaterElement([4,1,2], [1,3,4,2])` → `[-1, 3, -1]`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| One pass with an index map | `O(n)` | `O(u)`, `u` = different values |

#### 5. Common Mistakes

1. **Using `put` when you want the first index.** It overwrites. Use `putIfAbsent`.
2. **Using `putIfAbsent` when you want the last index.**
3. **Not checking `null`** before using the stored index.
4. **Off-by-one in the distance** (`i - j` vs `i - j - 1`).
5. **`associate` over repeated values** silently keeps the last index.
6. **Using indexes from one array on another array.**

#### 6. Say This in the Interview

1. "I keep a map from value to its last index. If the same value comes again within `k`, I return true."
2. "For the longest range I keep the **first** index; for the closest repeat I keep the **last** index."
3. "One pass: `O(n)` time, `O(n)` space."

#### 7. Quick Check

1. For `[1, 0, 1, 1]` and `k = 1`, is there a nearby duplicate?
2. When do you use `putIfAbsent` for indexes?

<details>
<summary>Answers</summary>

1. Yes. The two `1`s at indexes 2 and 3 are `1` apart.
2. When you want to keep the **first** index of a value (for longest ranges).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1 | Two Sum (Easy) | value → index |
| 219 | Contains Duplicate II (Easy) | last index |
| 496 | Next Greater Element I (Easy) | value → next greater |
| 3 | Longest Substring Without Repeating Characters (Medium) | last index of each letter (note 13) |
| 243 | Shortest Word Distance (Easy, premium) | latest index of each word |
