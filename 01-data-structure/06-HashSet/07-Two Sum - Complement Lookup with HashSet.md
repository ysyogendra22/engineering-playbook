# Two Sum / Complement Lookup with HashSet

#### 1. Definition — Must Know

1. **Complement lookup** means: for each number `x`, look for the partner `target - x` in the values you have already seen.
2. With a HashSet, the check is `O(1)`, so the whole search is `O(n)`.
3. A set tells you **whether** a pair exists. If you must return the **indices**, use a `HashMap` (value → index).

#### 2. Why It Is Used — Must Know

1. It beats the brute force `O(n²)` pair check.
2. It is the most famous interview question (*Two Sum*, LeetCode 1), and the idea repeats in many problems.
3. It trains the habit "what partner am I looking for?".

#### 3. How It Works — Must Know

`nums = [2, 7, 11, 15]`, `target = 9`

```text
seen = {}
x = 2   complement = 9 - 2 = 7   is 7 in seen? no    → add 2    seen = {2}
x = 7   complement = 9 - 7 = 2   is 2 in seen? YES   → pair (2, 7) found
```

The order matters:

```text
1. check the complement in seen
2. then add the current number

Why: with target = 6 and nums = [3], adding 3 first would let 3 pair with itself.
```

#### 4. Core Concepts — Must Know

1. **Complement = `target - x`.**
2. **Check first, then add.** The current element must not pair with itself.
3. **One pass.** Each number is looked up once and added once.
4. **Set vs map:**

| Question | Structure |
|---|---|
| Does a pair with this sum exist? | `HashSet` |
| Return the indices of the pair | `HashMap<Value, Index>` |
| Count pairs with duplicates | `HashMap<Value, Count>` |
| Sorted array, `O(1)` space | Two pointers |

5. **Variations** use another complement: difference `x - k` / `x + k`, product `target / x`, XOR `target xor x`.

#### 5. Algorithm — Must Know

```text
seen = empty set
for each x in nums:
    if (target - x) is in seen → return true
    add x to seen
return false
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Does any pair add up to target?
fun hasPairWithSum(nums: IntArray, target: Int): Boolean {
    val seen = HashSet<Int>()
    for (x in nums) {
        if (target - x in seen) return true
        seen.add(x)
    }
    return false
}
```

**Two Sum with indices (a map is needed)**

```kotlin
fun twoSum(nums: IntArray, target: Int): IntArray {
    val indexOf = HashMap<Int, Int>()          // value → index
    for ((i, x) in nums.withIndex()) {
        val j = indexOf[target - x]
        if (j != null) return intArrayOf(j, i)
        indexOf[x] = i
    }
    return intArrayOf()
}
```

**Two Sum IV — Input is a BST** (LeetCode 653): the same idea while walking the tree.

```kotlin
class TreeNode(var `val`: Int) { var left: TreeNode? = null; var right: TreeNode? = null }

fun findTarget(root: TreeNode?, k: Int): Boolean {
    val seen = HashSet<Int>()
    fun dfs(node: TreeNode?): Boolean {
        if (node == null) return false
        if (k - node.`val` in seen) return true
        seen.add(node.`val`)
        return dfs(node.left) || dfs(node.right)
    }
    return dfs(root)
}
```

**Sorted array, `O(1)` space (two pointers)**

```kotlin
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

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Brute force | `O(n²)` | `O(1)` |
| **HashSet / HashMap** | **`O(n)`** | `O(n)` |
| Sort + two pointers | `O(n log n)` | `O(1)` extra |
| Two pointers on sorted input | `O(n)` | `O(1)` |

#### 8. Common Complement Patterns — Must Know

1. **Two Sum** (LeetCode 1) — map with indices.
2. **Two Sum IV, BST** (LeetCode 653) — set while walking the tree.
3. **Pair with difference `k`** — look for `x - k` and `x + k`.
4. **Check If N and Its Double Exist** (LeetCode 1346) — look for `2x` and `x / 2`.
5. **Pairs divisible by `k`** — remainders in a map.
6. **Four Sum II** (LeetCode 454) — map of pair sums.
7. **Subarray sum equals k** — prefix sums in a map (`03-leetcode-patterns`, topic 7).

#### 9. Edge Cases / Common Mistakes

1. Adding the current number before checking, so it pairs with itself.
2. Needing two equal numbers (like `3 + 3 = 6`) and the set is checked in the wrong order. Check-then-add handles this: the second `3` finds the first.
3. Using a set when the problem asks for indices.
4. Sum overflow: `a + b` may exceed `Int`. Use `Long`, or write `target - x` carefully.
5. Negative numbers and zero. They work with the same logic.
6. Returning the same index twice.
7. Forgetting whether the problem guarantees exactly one answer.

#### 10. When to Use / When Not to Use

**Use when:**

1. The array is unsorted and you need `O(n)` time.

**Avoid when:**

1. The array is already sorted and memory is tight. Use two pointers.
2. You need all unique pairs without repeats. Add duplicate handling or sort first.

#### 11. Related Topics

1. HashSet vs HashMap
2. Fast Membership / Lookup Pattern
3. HashSet + Two Pointers
4. HashMap (`01-data-structure/05-HashMap`)
5. Two Pointers (`03-leetcode-patterns`)

#### 12. Interview Must Remember

1. **Look for `target - x` in what you have already seen.**
2. **Check first, then add.**
3. Set = exists. Map = indices.
4. `O(n)` time and space. Sorted input → two pointers with `O(1)` space.
