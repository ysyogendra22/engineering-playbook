# Deduplication of Complex States

#### 1. Definition — Must Know

1. **Deduplication of complex states** means detecting that two states are **the same**, even when they are big (a board, a list, a shape) or can be written in different ways.
2. The method: turn each state into a **canonical key** (one standard form), and store that key in a HashSet.
3. If two states give the same key, they are duplicates.

#### 2. Why It Is Used — Must Know

1. Search and generation problems produce the same result by different paths. Without dedup, work and answers repeat.
2. It appears in: unique combinations, unique shapes, repeated board positions, memoization.
3. The hard part is the key design: too loose merges different states, too strict misses duplicates.

#### 3. How It Works — Must Know

Example: *Number of Distinct Islands* (LeetCode 694, premium). Two islands are the same if one is a translation of the other.

```text
Island 1:  X X        Island 2:      X X       They have the same shape.
           X                         X         Absolute positions differ, the shape does not.
```

**Canonical key idea:** record the DFS path (directions taken, with a mark when backtracking) starting from the island's first cell. Position disappears; only the shape remains.

```text
Both islands → "S R D B B"-style string  → same key → counted once
```

Other examples of canonical keys:

```text
{3, 1, 2} and {2, 3, 1} (same triple)   → sort first:           [1, 2, 3]
Board (2×2) [[1,2],[3,0]]               → string:               "1,2|3,0"
Anagram "eat" and "tea"                 → sorted letters:       "aet"
Position + keys collected               → packed into a Long:   (row, col, mask)
```

#### 4. Core Concepts — Must Know

1. **Canonical form** = a single, agreed way to write equal states.
2. **Choose what to ignore:** order (sort), position (use relative moves), case (lowercase), rotations (take the smallest rotation).
3. **Choose a key type:**

| Key type | Best for | Cost |
|---|---|---|
| `String` | boards, shapes, signatures | simple, but slower and bigger |
| `List<Int>` / data class | small sorted groups | clear and safe |
| `Long` / `Int` (bit packing) | many small fields | fastest, smallest |
| `BitSet` / bitmask | subsets of up to 32/64 items | very fast |

4. **Immutable keys.** Never store a mutable array. Convert it to a `String` or `List` first.
5. **Hash cost:** a long key costs `O(length)` to build and hash. Keep it short when states are many.
6. **Sorting + skipping** (as in Subsets II) avoids creating duplicates at all, which is lighter than a set.

#### 5. Algorithm — Must Know

```text
seen = empty set
for each generated state:
    key = canonical(state)
    if seen.add(key):
        keep the state / continue searching from it
    // else: duplicate → skip
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// 1. Unique groups where order does not matter: sort, then store as List
fun uniqueTriples(triples: List<IntArray>): List<List<Int>> {
    val seen = LinkedHashSet<List<Int>>()
    for (t in triples) seen.add(t.sorted())            // [3,1,2] and [2,3,1] → [1,2,3]
    return seen.toList()
}

// 2. Board to a string key
fun boardKey(board: Array<IntArray>): String =
    board.joinToString("|") { row -> row.joinToString(",") }

// 3. Pack small numbers into a Long (row, col, keysMask)
fun packState(row: Int, col: Int, mask: Int): Long =
    (row.toLong() shl 40) or (col.toLong() shl 20) or mask.toLong()
//   row, col < 2^20 and mask < 2^20 are assumed here

// 4. Anagram signature
fun anagramKey(word: String): String = String(word.toCharArray().also { it.sort() })

// 5. Number of Distinct Islands — key = DFS path signature
fun numDistinctIslands(grid: Array<IntArray>): Int {
    val rows = grid.size
    val cols = grid[0].size
    val shapes = HashSet<String>()

    fun dfs(r: Int, c: Int, dir: Char, path: StringBuilder) {
        if (r !in 0 until rows || c !in 0 until cols || grid[r][c] != 1) return
        grid[r][c] = 0                                  // mark visited (changes the input)
        path.append(dir)
        dfs(r + 1, c, 'D', path)
        dfs(r - 1, c, 'U', path)
        dfs(r, c + 1, 'R', path)
        dfs(r, c - 1, 'L', path)
        path.append('B')                                // backtrack marker keeps shapes unique
    }

    for (r in 0 until rows) {
        for (c in 0 until cols) {
            if (grid[r][c] == 1) {
                val path = StringBuilder()
                dfs(r, c, 'S', path)
                shapes.add(path.toString())
            }
        }
    }
    return shapes.size
}

// 6. Dedupe a list of objects by a key
data class Contact(val email: String, val name: String)
val contacts = listOf(Contact("A@x.com", "Asha"), Contact("a@x.com", "Asha K"))
val unique = contacts.distinctBy { it.email.lowercase() }     // case-insensitive email key
```

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---|
| Building a key of length `L` | `O(L)` (or `O(L log L)` if you sort) |
| `add` to the set | `O(L)` to hash and compare |
| Total for `n` states | `O(n × L)` |
| Space | `O(n × L)` |

Bit-packed `Long` keys have `L = 1` in practice, so they are the cheapest.

#### 8. Common Deduplication Patterns — Must Know

1. **Unique combinations / subsets** — sort the input, then skip equal neighbours (LeetCode 90 *Subsets II*, 40 *Combination Sum II*), or store sorted lists in a set.
2. **Distinct shapes** — relative path signature (*Number of Distinct Islands*).
3. **Anagram groups** — sorted letters or a 26-count tuple as a key (LeetCode 49).
4. **Board states** — string key for puzzles (LeetCode 773).
5. **Memoization keys** — `(index, remaining, mask)` as a `Long` or data class.
6. **Visited with extra state** — `(row, col, direction, steps left)`.
7. **App data** — `distinctBy { it.id }` or a normalized email / url key.
8. **Symmetry** — rotations and reflections reduced to the smallest form.

#### 9. Edge Cases / Common Mistakes

1. A key that is **too coarse**. For example, ignoring the keys collected in a maze merges different states.
2. A key that is **too fine**. Equal states look different, so duplicates remain.
3. Keys without separators: `"1" + "23"` and `"12" + "3"` both give `"123"`. Use `,` and `|`.
4. Shapes without the backtrack marker. Different shapes can then give the same path string.
5. Using `IntArray` as a key.
6. Packing fields into a `Long` without checking the ranges. Fields can overlap.
7. Changing the input (the grid) while you need it later.
8. Case, spaces, Unicode forms in text keys.
9. Forgetting to sort before using a list as an unordered key.

#### 10. When to Use / When Not to Use

**Use when:**

1. The same state can be reached or generated in many ways.
2. Equality is not simply "same object".

**Avoid when:**

1. You can avoid duplicates by construction (sort + skip), which is lighter.
2. The key would be larger than the state itself and states are huge. Consider hashing to a `Long` (with a small risk of collision) only when the problem allows it.

#### 11. Related Topics

1. HashSet with Custom Objects
2. HashSet in Graph / State-Space Problems
3. Common HashSet Edge Cases
4. Backtracking (`02-algorithm/06-Backtracking & Branch and Bound`)
5. Dynamic Programming memoization (`02-algorithm/05-Dynamic Programming`)

#### 12. Interview Must Remember

1. **Design a canonical key, then use a set.**
2. Decide what to ignore (order, position, case) and what to keep (everything that changes the future).
3. Immutable keys only: `String`, `List`, `data class`, or a packed `Long`.
4. Sorting plus skipping equal neighbours can avoid the set entirely.
