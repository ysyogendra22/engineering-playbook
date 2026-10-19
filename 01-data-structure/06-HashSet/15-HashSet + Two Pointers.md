# HashSet + Two Pointers

#### 1. Definition — Must Know

1. **Two pointers** move through a (usually sorted) array from both ends or at different speeds.
2. A **HashSet** can help them remember or remove duplicates, or can replace them when the input is not sorted.
3. This note compares the two ideas and shows how they work together, especially for removing duplicates in answers (like *3Sum*).

#### 2. Why It Is Used — Must Know

1. Many problems can be solved with a set (`O(n)` memory) **or** two pointers (`O(1)` memory). Interviewers love asking for both.
2. Knowing the trade-off shows maturity: "set when unsorted, two pointers when sorted".
3. 3Sum-style problems need to avoid repeated answers, and the way you avoid them is a key idea.

#### 3. How It Works — Must Know

Same problem, two tools. *Does a pair add up to `target`?*

```text
Unsorted [8, 3, 5, 1], target = 9:
    set  → 8: need 1 (no) | 3: need 6 (no) | 5: need 4 (no) | 1: need 8 (yes!) → true

Sorted [1, 3, 5, 8], target = 9:
    l=0 (1), r=3 (8)  → 1 + 8 = 9 → true
    if the sum is too small, move l right; if too big, move r left.
```

**Avoiding repeated answers in 3Sum:** sort first, then skip equal neighbours.

```text
sorted nums: [-1, -1, 0, 1, 2]

i=0 (-1): two pointers find (-1, 0, 1)   → answer
i=1 (-1): same value as before → SKIP    ← no repeated triple
i=2 ( 0): none
```

#### 4. Core Concepts — Must Know

| | HashSet | Two pointers |
|---|---|---|
| Needs sorted input? | No | Yes (or sort first, `O(n log n)`) |
| Extra memory | `O(n)` | `O(1)` |
| Time | `O(n)` | `O(n)` after sorting |
| Good for | unsorted input, streaming data | sorted input, in-place work |

1. **Remove duplicates from a sorted array in place:** one slow pointer writes, one fast pointer reads. No set is needed.
2. **Remove duplicates from an unsorted array:** a set (and the order may be kept with `LinkedHashSet`).
3. **Avoid duplicate answers:** (a) sort and skip equal neighbours, or (b) store results as sorted lists in a `Set<List<Int>>`.
4. **Option (a) is lighter**; option (b) is simpler to write.

#### 5. Algorithm — Must Know

```text
3Sum with sort + two pointers:
sort nums
for i from 0 to n - 3:
    if i > 0 and nums[i] == nums[i-1]: continue        // skip repeated first value
    l = i + 1; r = n - 1
    while l < r:
        sum = nums[i] + nums[l] + nums[r]
        if sum < 0: l++
        else if sum > 0: r--
        else:
            record (nums[i], nums[l], nums[r]); l++; r--
            skip equal values on both sides
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Remove duplicates from a SORTED array in place (two pointers, no set)
fun removeDuplicates(nums: IntArray): Int {
    if (nums.isEmpty()) return 0
    var write = 1
    for (read in 1 until nums.size) {
        if (nums[read] != nums[read - 1]) {
            nums[write] = nums[read]
            write++
        }
    }
    return write                     // new length
}

// 3Sum — sort + two pointers, no set needed for the answers
fun threeSum(nums: IntArray): List<List<Int>> {
    nums.sort()
    val result = mutableListOf<List<Int>>()
    for (i in 0 until nums.size - 2) {
        if (i > 0 && nums[i] == nums[i - 1]) continue
        var l = i + 1
        var r = nums.size - 1
        while (l < r) {
            val sum = nums[i] + nums[l] + nums[r]
            when {
                sum < 0 -> l++
                sum > 0 -> r--
                else -> {
                    result.add(listOf(nums[i], nums[l], nums[r]))
                    l++
                    r--
                    while (l < r && nums[l] == nums[l - 1]) l++
                    while (l < r && nums[r] == nums[r + 1]) r--
                }
            }
        }
    }
    return result
}

// Same idea with a set of triples (shorter, but uses more memory)
fun threeSumWithSet(nums: IntArray): List<List<Int>> {
    nums.sort()
    val found = LinkedHashSet<List<Int>>()
    for (i in 0 until nums.size - 2) {
        var l = i + 1
        var r = nums.size - 1
        while (l < r) {
            val sum = nums[i] + nums[l] + nums[r]
            when {
                sum < 0 -> l++
                sum > 0 -> r--
                else -> { found.add(listOf(nums[i], nums[l], nums[r])); l++; r-- }
            }
        }
    }
    return found.toList()
}
```

Checks: `threeSum([-1, 0, 1, 2, -1, -4])` → `[[-1, -1, 2], [-1, 0, 1]]`.

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Pair sum with a set | `O(n)` | `O(n)` |
| Pair sum, sorted, two pointers | `O(n)` | `O(1)` |
| 3Sum with sort + two pointers | `O(n²)` | `O(1)` extra (plus the answer) |
| 3Sum with a set of triples | `O(n²)` | `O(answer size)` |
| Sorting first | `O(n log n)` | — |

#### 8. Common Combined Patterns — Must Know

1. **Remove Duplicates from Sorted Array** (LeetCode 26) — read/write pointers.
2. **3Sum** (LeetCode 15), **4Sum** (LeetCode 18) — sort, two pointers, skip duplicates.
3. **Intersection of sorted arrays** — two pointers instead of a set.
4. **Two Sum on unsorted data** — set / map.
5. **Two Sum II, sorted** (LeetCode 167) — two pointers.
6. **Squares, merges, partitions** — two pointers on sorted data.

#### 9. Edge Cases / Common Mistakes

1. Using two pointers on **unsorted** data without sorting first.
2. Sorting when the original positions (indices) are needed. Sorting loses them.
3. Not skipping duplicates, so repeated triples appear.
4. Skipping duplicates in the wrong place (for example, skipping `nums[i]` before using it).
5. `IntArray` triples in a set. Use `List<Int>` so equality works.
6. Fewer than 3 elements. The loop `0 until size - 2` is empty, which is correct.
7. Overflow of `nums[i] + nums[l] + nums[r]` with extreme values.

#### 10. When to Use / When Not to Use

**Use the set when:**

1. Input is unsorted and you must keep original positions or order.
2. You process a stream.

**Use two pointers when:**

1. Input is sorted (or sorting is allowed), and you need `O(1)` extra space.

#### 11. Related Topics

1. Two Sum / Complement Lookup with HashSet
2. Intersection / Common Elements
3. Two Pointers (`03-leetcode-patterns`, topic 4)
4. Sorting (`02-algorithm/01-sorting`)

#### 12. Interview Must Remember

1. **Unsorted → set (`O(n)` memory). Sorted → two pointers (`O(1)` memory).**
2. 3Sum: sort, then skip equal neighbours to avoid repeated triples.
3. Sorting destroys original indices.
4. Say both approaches and when each one wins.
