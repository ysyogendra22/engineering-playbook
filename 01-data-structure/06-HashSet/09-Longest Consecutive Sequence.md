# Longest Consecutive Sequence

#### 1. Definition — Must Know

1. Given an unsorted array, find the **length of the longest run of consecutive numbers** (like `1, 2, 3, 4`), in any order in the input.
2. It is *Longest Consecutive Sequence* (LeetCode 128). If a number and a title ever disagree, trust the title.
3. It must run in **`O(n)`**, so sorting (`O(n log n)`) is not the target answer.

#### 2. Why It Is Used — Must Know

1. It is a very common HashSet interview question.
2. It teaches a clever trick: **only start counting from the beginning of a sequence**.
3. That trick keeps the total work linear.

#### 3. How It Works — Must Know

`nums = [100, 4, 200, 1, 3, 2]`

```text
set = {100, 4, 200, 1, 3, 2}

For each number, ask: "is there a number just BEFORE me (n - 1)?"

100 → 99 is not in the set  → 100 is a START. Count: 100 → 101? no.            length 1
4   → 3 is in the set       → NOT a start. Skip.
200 → 199 is not in the set → START. 201? no.                                  length 1
1   → 0 is not in the set   → START. 2 yes, 3 yes, 4 yes, 5 no.               length 4
3   → 2 is in the set       → skip
2   → 1 is in the set       → skip

Answer: 4   (1, 2, 3, 4)
```

#### 4. Core Concepts — Must Know

1. **Put all numbers in a set** for `O(1)` lookups.
2. **A number starts a sequence only if `n - 1` is not in the set.**
3. **From a start, walk up** while `cur + 1` is in the set.
4. **Why it is `O(n)`:** each number is walked over at most once, because only starts begin a walk.
5. **Duplicates** do not matter, because the set removes them.
6. Iterate over the **set** (not the array) so repeated numbers do not repeat the work.

#### 5. Algorithm — Must Know

```text
set = all numbers
best = 0
for each n in set:
    if (n - 1) is not in set:          // n is the start of a sequence
        cur = n
        length = 1
        while (cur + 1) is in set:
            cur += 1
            length += 1
        best = max(best, length)
return best
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun longestConsecutive(nums: IntArray): Int {
    val set = nums.toHashSet()
    var best = 0

    for (n in set) {
        if ((n - 1) !in set) {          // start of a sequence
            var cur = n
            var length = 1
            while ((cur + 1) in set) {
                cur++
                length++
            }
            best = maxOf(best, length)
        }
    }
    return best
}
```

**Sorting version (simpler, `O(n log n)`)**

```kotlin
fun longestConsecutiveSort(nums: IntArray): Int {
    if (nums.isEmpty()) return 0
    val sorted = nums.distinct().sorted()
    var best = 1
    var run = 1
    for (i in 1 until sorted.size) {
        run = if (sorted[i] == sorted[i - 1] + 1) run + 1 else 1
        best = maxOf(best, run)
    }
    return best
}
```

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| **HashSet, start-only walk** | **`O(n)`** | `O(n)` |
| Sort + scan | `O(n log n)` | `O(n)` |
| Walk from every number (no start check) | `O(n²)` worst case | `O(n)` |

#### 8. Common Variations — Must Know

1. **Longest Consecutive Sequence** (LeetCode 128).
2. **Binary Tree Longest Consecutive Sequence** (LeetCode 298, premium) — DFS, not a set.
3. **Missing ranges / summary ranges** — usually a sorted array scan.
4. **Union-Find alternative** — merge `n` with `n + 1`. Same `O(n)` idea with a different tool.
5. **Return the sequence itself** — remember the best start and length.

#### 9. Edge Cases / Common Mistakes

1. Skipping the `n - 1` start check. The solution then becomes `O(n²)` on inputs like `1..n`.
2. Looping over the array (with duplicates) instead of the set.
3. Empty array. The answer is `0`.
4. Integer overflow at the extremes: `Int.MIN_VALUE - 1` wraps around. LeetCode's limits avoid it; mention it.
5. Duplicates counted twice in the sorting version. Remove them first.
6. Assuming the order of the input matters. It does not.
7. Treating "consecutive" as "adjacent in the array". It means adjacent in value.

#### 10. When to Use / When Not to Use

**Use when:**

1. The input is unsorted and `O(n)` is required.

**Use sorting when:**

1. The input is small, or you prefer simpler code and `O(n log n)` is accepted.

**Avoid a set when:**

1. Values are in a small dense range. A `BooleanArray` works too.

#### 11. Related Topics

1. Fast Membership / Lookup Pattern
2. Unique Elements Pattern
3. Union-Find (`02-algorithm/07-Graph Algorithms`)
4. Sorting (`02-algorithm/01-sorting`)

#### 12. Interview Must Remember

1. **Only start counting when `n - 1` is not in the set.**
2. Walk up with `cur + 1` while it is in the set.
3. `O(n)` time, `O(n)` space. Each number is walked once.
4. Iterate the set, not the array.
