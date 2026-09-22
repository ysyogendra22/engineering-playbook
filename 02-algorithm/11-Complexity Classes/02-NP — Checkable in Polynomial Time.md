# NP — Checkable in Polynomial Time

#### 1. Definition — Must Know

**NP** is the set of problems where, if someone **hands you a proposed answer**, you can **check** whether it's correct in polynomial time — even if *finding* that answer in the first place might take much longer.

#### 2. Why It Is Used — Must Know

This is the key distinction that trips people up: NP is not "hard problems" — it's "problems whose *solutions* are easy to verify", regardless of how hard they are to *solve*. Every problem in P is automatically in NP too (if you can solve it fast, you can obviously also check a proposed answer fast, by just solving it yourself).

#### 3. How It Works — Must Know

```text
Sudoku:
  SOLVING a Sudoku puzzle from scratch can take real search effort
  (backtracking, `06-Backtracking & Branch and Bound/07`).
  But CHECKING a proposed filled-in solution is fast and easy:
  just verify every row, column, and 3x3 box has digits 1-9 with no
  repeats — a simple O(n²) scan. → Sudoku is in NP.

Travelling Salesman (decision version — "is there a route under length X?"):
  FINDING the optimal route is very hard (no known fast algorithm).
  But CHECKING a proposed route: just add up its total distance and
  compare to X — fast. → TSP (this version) is in NP.

Sorting:
  Both solving (sort it) AND checking (is it sorted?) are fast.
  → Sorting is in P, and therefore also in NP (P is a subset of NP).
```

#### 4. Algorithm — Must Know

```text
To check "is my problem in NP?":
  If I'm handed a PROPOSED solution, can I verify it's correct
  in polynomial time?

  Yes → the problem is in NP (regardless of how hard finding
        that solution actually is)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// The "checker" for Sudoku — fast, even though SOLVING Sudoku is slow.
// This is exactly what makes Sudoku a problem "in NP".
fun isValidSudokuSolution(board: Array<IntArray>): Boolean {
    fun isValidGroup(values: List<Int>) = values.sorted() == (1..9).toList()
    for (row in board) if (!isValidGroup(row.toList())) return false
    for (col in 0..8) if (!isValidGroup((0..8).map { board[it][col] })) return false
    for (boxRow in 0..2) for (boxCol in 0..2) {
        val box = (0..2).flatMap { r -> (0..2).map { c -> board[boxRow*3+r][boxCol*3+c] } }
        if (!isValidGroup(box)) return false
    }
    return true
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Checking a proposed Sudoku solution | O(n²) — fast |
| Solving a Sudoku puzzle from scratch | Exponential in the worst case — slow |

The gap between these two numbers is exactly the interesting question NP is built around.

#### 7. Common Mistakes — Must Know

1. Thinking "NP" stands for "not polynomial" — it doesn't; it stands for "Nondeterministic Polynomial", and it's about verification, not about being slow to solve.
2. Assuming all NP problems are hard to solve — P is a **subset** of NP, so every "easy" problem is technically in NP too.
3. Confusing NP with NP-Complete (topic 3) — NP-Complete is a much smaller, specific set of the *hardest* problems within NP.

#### 8. Related Topics

1. `1` P — Solvable in Polynomial Time — the subset of NP that's also easy to *solve*
2. `3` NP-Complete — the Hardest Problems in NP — the hardest problems within NP
3. `7` P vs NP Is an Open Problem — whether P and NP are actually the same set is unknown

#### 9. Interview Must Remember

1. **NP = "easy to check a proposed answer", not "easy to solve".**
2. Every problem in P is automatically in NP too — P is a subset of NP.
3. The gap between "hard to solve" and "easy to check" is exactly what makes NP an interesting category.
