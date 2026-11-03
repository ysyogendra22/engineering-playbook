# Backtracking

> Try a choice, explore, then undo it and try the next. It is DFS over a decision tree.

#### 1. What Is It?

**Backtracking** builds a solution step by step. At each step you choose one option, recurse, and then **undo** the choice. It enumerates all valid answers and **prunes** branches that cannot work.

**Signals**

- "**All** subsets / combinations / permutations"
- "Generate all valid ..." (parentheses, IP addresses)
- "Place things under rules" (N-Queens, Sudoku, word search)
- Small `n` (about 20 or less) and the answer is a **list of solutions**

**Template: choose, explore, un-choose**

```text
fun backtrack(path, choices):
    if path is a complete answer: save a COPY of path; return
    for each choice in choices:
        if choice is invalid: continue        // prune
        path.add(choice)                      // choose
        backtrack(path, remaining choices)    // explore
        path.removeLast()                     // un-choose
```

#### 2. How It Works

Draw the decision tree before coding. Subsets of `[1, 2, 3]` (each node is the current `path`):

```text
[]
├─ [1]
│  ├─ [1,2]
│  │  └─ [1,2,3]
│  └─ [1,3]
├─ [2]
│  └─ [2,3]
└─ [3]
```

**Which pattern?**

| Problem | What changes in the template |
|---|---|
| Subsets | save at **every** node; loop from a `start` index; recurse with `i + 1` |
| Combinations / Combination Sum | save when the target is hit; `start` index; recurse with `i` if reuse is allowed |
| Permutations | loop over **all** items; a `used` array stops reuse; save when `path.size == n` |
| Duplicates in the input | sort first; skip `nums[i] == nums[i−1]` when `i > start` |
| Grid (word search) | mark the cell, recurse in 4 directions, unmark |
| Constraint (N-Queens) | keep sets for columns and diagonals; place a queen only if safe |

**Pruning** makes it fast: stop when the running sum exceeds the target, when the path can't be completed, or when a rule is already broken.

**Duplicates rule:** `i > start && nums[i] == nums[i-1]` skips an equal value at the **same level** but still allows it deeper (so `[1,2,2]` is kept).

#### 3. Brute Force vs Optimized

Backtracking *is* the structured brute force. The optimization is **pruning**, and **memoization** when sub-problems repeat (then it becomes DP, note 18).

| Problem | Naive | Better |
|---|---|---|
| Combination Sum | generate all combinations, filter | stop when `remaining < 0` |
| Permutations with dups | build all, put in a set | sort + skip equal siblings |
| N-Queens | try all `nⁿ` placements and check | place row by row, check conflicts as you go |
| Word Break (all splits) | list every split | memoize on the start index |

```kotlin
// Naive subsets: use a bitmask 0 until 2^n (fine for n <= 20)
fun subsetsBitmask(nums: IntArray): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    for (mask in 0 until (1 shl nums.size)) {
        result.add(nums.indices.filter { ((mask shr it) and 1) == 1 }.map { nums[it] })
    }
    return result
}
```

#### 4. Kotlin Code

```kotlin
// Subsets (LeetCode 78)
fun subsets(nums: IntArray): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    val path = mutableListOf<Int>()
    fun backtrack(start: Int) {
        result.add(path.toList())                          // copy the path
        for (i in start until nums.size) {
            path.add(nums[i])
            backtrack(i + 1)
            path.removeAt(path.size - 1)
        }
    }
    backtrack(0)
    return result
}

// Subsets II, with duplicates (LeetCode 90)
fun subsetsWithDup(nums: IntArray): List<List<Int>> {
    nums.sort()
    val result = mutableListOf<List<Int>>()
    val path = mutableListOf<Int>()
    fun backtrack(start: Int) {
        result.add(path.toList())
        for (i in start until nums.size) {
            if (i > start && nums[i] == nums[i - 1]) continue     // skip equal sibling
            path.add(nums[i])
            backtrack(i + 1)
            path.removeAt(path.size - 1)
        }
    }
    backtrack(0)
    return result
}

// Permutations (LeetCode 46)
fun permute(nums: IntArray): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    val path = mutableListOf<Int>()
    val used = BooleanArray(nums.size)
    fun backtrack() {
        if (path.size == nums.size) { result.add(path.toList()); return }
        for (i in nums.indices) {
            if (used[i]) continue
            used[i] = true
            path.add(nums[i])
            backtrack()
            path.removeAt(path.size - 1)
            used[i] = false
        }
    }
    backtrack()
    return result
}

// Combination Sum (LeetCode 39): numbers can be reused
fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    val path = mutableListOf<Int>()
    fun backtrack(start: Int, remaining: Int) {
        if (remaining == 0) { result.add(path.toList()); return }
        for (i in start until candidates.size) {
            if (candidates[i] > remaining) continue                  // prune
            path.add(candidates[i])
            backtrack(i, remaining - candidates[i])                  // i, not i + 1: reuse allowed
            path.removeAt(path.size - 1)
        }
    }
    backtrack(0, target)
    return result
}

// Letter Combinations of a Phone Number (LeetCode 17)
fun letterCombinations(digits: String): List<String> {
    if (digits.isEmpty()) return emptyList()
    val letters = arrayOf("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
    val result = mutableListOf<String>()
    val sb = StringBuilder()
    fun backtrack(index: Int) {
        if (index == digits.length) { result.add(sb.toString()); return }
        for (c in letters[digits[index] - '0']) {
            sb.append(c)
            backtrack(index + 1)
            sb.deleteCharAt(sb.length - 1)
        }
    }
    backtrack(0)
    return result
}

// Generate Parentheses (LeetCode 22)
fun generateParenthesis(n: Int): List<String> {
    val result = mutableListOf<String>()
    val sb = StringBuilder()
    fun backtrack(open: Int, close: Int) {
        if (sb.length == 2 * n) { result.add(sb.toString()); return }
        if (open < n) {
            sb.append('('); backtrack(open + 1, close); sb.deleteCharAt(sb.length - 1)
        }
        if (close < open) {                                          // never close more than opened
            sb.append(')'); backtrack(open, close + 1); sb.deleteCharAt(sb.length - 1)
        }
    }
    backtrack(0, 0)
    return result
}

// Word Search (LeetCode 79)
fun exist(board: Array<CharArray>, word: String): Boolean {
    val rows = board.size
    val cols = board[0].size
    fun dfs(r: Int, c: Int, index: Int): Boolean {
        if (index == word.length) return true
        if (r !in 0 until rows || c !in 0 until cols || board[r][c] != word[index]) return false
        val saved = board[r][c]
        board[r][c] = '#'                                            // mark as used
        val found = dfs(r + 1, c, index + 1) || dfs(r - 1, c, index + 1) ||
                    dfs(r, c + 1, index + 1) || dfs(r, c - 1, index + 1)
        board[r][c] = saved                                          // un-choose
        return found
    }
    for (r in 0 until rows) for (c in 0 until cols) if (dfs(r, c, 0)) return true
    return false
}

// Palindrome Partitioning (LeetCode 131)
fun partition(s: String): List<List<String>> {
    val result = mutableListOf<List<String>>()
    val path = mutableListOf<String>()
    fun isPalindrome(l: Int, r: Int): Boolean {
        var i = l
        var j = r
        while (i < j) { if (s[i++] != s[j--]) return false }
        return true
    }
    fun backtrack(start: Int) {
        if (start == s.length) { result.add(path.toList()); return }
        for (end in start until s.length) {
            if (!isPalindrome(start, end)) continue
            path.add(s.substring(start, end + 1))
            backtrack(end + 1)
            path.removeAt(path.size - 1)
        }
    }
    backtrack(0)
    return result
}

// N-Queens II (LeetCode 52): count the solutions
fun totalNQueens(n: Int): Int {
    val cols = BooleanArray(n)
    val diag1 = BooleanArray(2 * n)            // row - col + n
    val diag2 = BooleanArray(2 * n)            // row + col
    var count = 0
    fun place(row: Int) {
        if (row == n) { count++; return }
        for (c in 0 until n) {
            if (cols[c] || diag1[row - c + n] || diag2[row + c]) continue
            cols[c] = true; diag1[row - c + n] = true; diag2[row + c] = true
            place(row + 1)
            cols[c] = false; diag1[row - c + n] = false; diag2[row + c] = false
        }
    }
    place(0)
    return count
}
```

Checks: `subsets([1,2,3])` → `[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]`. `subsetsWithDup([1,2,2])` → `[[],[1],[1,2],[1,2,2],[2],[2,2]]`. `permute([1,2,3])` → `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`. `combinationSum([2,3,6,7], 7)` → `[[2,2,3],[7]]`. `letterCombinations("23")` → `["ad","ae","af","bd","be","bf","cd","ce","cf"]`. `generateParenthesis(3)` → `["((()))","(()())","(())()","()(())","()()()"]`. `exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")` → `true`; `"SEE"` → `true`; `"ABCB"` → `false`. `partition("aab")` → `[["a","a","b"],["aa","b"]]`. `totalNQueens(4)` → `2`; `totalNQueens(1)` → `1`; `totalNQueens(8)` → `92`.

#### 5. Complexity

| Problem | Time | Space (stack + path) |
|---|---|---|
| Subsets | `O(n · 2ⁿ)` | `O(n)` |
| Permutations | `O(n · n!)` | `O(n)` |
| Combination Sum | up to `O(2^target)` (pruned) | `O(target / min)` |
| Generate Parentheses | `O(4ⁿ / √n)` (Catalan) | `O(n)` |
| Word Search | `O(m·n·3^L)` | `O(L)` |
| N-Queens | about `O(n!)` | `O(n)` |

The `n` factor comes from copying each answer into the result.

#### 6. Common Mistakes

1. **Saving `path` itself** instead of a copy. Every saved answer ends up empty or equal. Use `path.toList()`.
2. **Forgetting to undo** (`removeAt`, `used[i] = false`, restore the cell).
3. **Combinations:** looping from `0` each time instead of from `start`, which creates duplicate sets.
4. **Duplicates:** skipping with `i > 0` instead of `i > start`, or forgetting to sort.
5. **Combination Sum:** recursing with `i + 1` when reuse is allowed (or `i` when it is not).
6. **Not pruning**, so the search is much slower than needed.
7. **Word Search:** checking bounds after reading the cell, or not restoring the cell.
8. **Using `removeLast()`** on a `MutableList`. Newer JDKs changed this method; use `removeAt(size − 1)`.

#### 7. Say This in the Interview

1. "This asks for all solutions, so I'll use backtracking. At each step I choose, recurse, and undo."
2. "I'll draw the decision tree first: at each node I decide which numbers can still be picked."
3. "I prune when the remaining sum goes negative, so I don't explore branches that can't work."
4. "The output itself has `2ⁿ` entries, so exponential time is expected."

#### 8. Quick Check

1. How many subsets does an array of 4 distinct numbers have?
2. Why use `i > start` and not `i > 0` to skip duplicates?

<details>
<summary>Answers</summary>

1. `2⁴ = 16`.
2. `i > 0` would also skip a duplicate that is the *first* pick at a deeper level, and lose answers like `[1,2,2]`. `i > start` only skips equal values among siblings.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 78 | [Subsets](https://leetcode.com/problems/subsets/) (Medium) | save at every node |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) (Medium) | `used` array |
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (Medium) | one choice per digit |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) | reuse, prune |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium) | open/close counts |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) (Medium) | grid, mark and unmark |
| 90 | [Subsets II](https://leetcode.com/problems/subsets-ii/) (Medium) | sort, skip siblings |
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) (Medium) | cut points |
| 51 | [N-Queens](https://leetcode.com/problems/n-queens/) (Hard) | column + diagonal sets |
