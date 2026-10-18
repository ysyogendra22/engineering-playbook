# Wildcard Search

#### 1. Definition — Must Know

1. **Wildcard search** matches a pattern that contains a special character standing for "any one letter", usually `.`.
2. Example: `.ad` matches `bad`, `dad`, and `mad`.
3. A Trie handles this by trying **every child** at a wildcard position, using DFS.

#### 2. Why It Is Used — Must Know

1. A `HashSet` cannot search with a wildcard without checking every word.
2. A Trie prunes: as soon as a path cannot match, that branch is dropped.
3. It is the classic problem *Design Add and Search Words Data Structure* (LeetCode 211).

#### 3. How It Works — Must Know

Trie holds `bad`, `dad`, `mad`:

```text
root
├── b → a → d*
├── d → a → d*
└── m → a → d*
```

```text
search("bad") → normal walk                                   → true
search("pad") → p has no child                                → false
search(".ad") → at '.', try b, d, m. Each leads to a → d*     → true
search("b..") → b ✓, then '.' tries a, then '.' tries d       → true
search("...") → every branch matches three letters            → true
search("..")  → ends at nodes that are not end of word        → false
```

#### 4. Core Concepts — Must Know

1. A normal character follows **one** child, or fails.
2. A `.` follows **all** children, and succeeds if **any** branch succeeds.
3. At the end of the pattern, the current node must be an **end of word**.
4. The pattern index tells you the depth, so no extra path tracking is needed.

#### 5. Algorithm — Must Know

```text
search(pattern):
    return dfs(root, pattern, 0)

dfs(node, pattern, index):
    if index == pattern.length: return node.isEndOfWord

    ch = pattern[index]
    if ch is '.':
        for each child of node:
            if dfs(child, pattern, index + 1): return true
        return false
    else:
        child = node.children[ch]
        if child is null: return false
        return dfs(child, pattern, index + 1)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class WordDictionary {

    private val root = TrieNode()

    fun addWord(word: String) {
        var node = root
        for (ch in word) {
            node = node.children.getOrPut(ch) { TrieNode() }
        }
        node.isEndOfWord = true
    }

    fun search(pattern: String): Boolean = dfs(root, pattern, 0)

    private fun dfs(node: TrieNode, pattern: String, index: Int): Boolean {
        if (index == pattern.length) return node.isEndOfWord

        val ch = pattern[index]
        if (ch == '.') {
            return node.children.values.any { dfs(it, pattern, index + 1) }
        }
        val next = node.children[ch] ?: return false
        return dfs(next, pattern, index + 1)
    }
}
```

#### 7. Time & Space Complexity — Must Know

| Case | Time |
|---|---:|
| Pattern with no wildcards | `O(L)` |
| Pattern with wildcards | bounded by the number of nodes in the Trie (each node is visited at most once) |
| Space (recursion) | `O(L)` |

Each node has one parent, and the pattern position equals the node depth, so a node is never visited twice during one search.

More wildcards mean more branches to try, so the cost grows toward the whole Trie.

#### 8. Common Wildcard Patterns — Must Know

1. `.` for any single letter (LeetCode 211).
2. Count of dots matters: few dots stay close to `O(L)`.
3. For `*` (any number of letters), the idea needs more branching and is not covered here.
4. Mobile example: searching a word list with unknown letters (crossword or word-game helpers).

#### 9. Edge Cases / Common Mistakes

1. At the end of the pattern, returning `true` without checking `isEndOfWord`.
2. Treating `.` as a normal character, so it never matches.
3. Returning on the first failed branch instead of trying the other children.
4. A `.` matching *zero* letters. It must match exactly one.
5. Pattern longer or shorter than any stored word. The end check handles it.

#### 10. When to Use / When Not to Use

**Use when:**

1. Patterns have a few wildcards and the words are in a Trie.
2. You need exact length matching with unknown letters.

**Avoid when:**

1. Patterns are mostly wildcards over a huge Trie (close to scanning everything).
2. You need full regular expressions. Use a regex engine.

#### 11. Related Topics

1. Search Word
2. Trie + DFS
3. Word Dictionary / Prefix Matching
4. DFS and Recursion (`02-algorithm/03-Recursion & Divide and Conquer`)

#### 12. Interview Must Remember

1. A normal character follows one child. A **`.` tries all children**.
2. At the end of the pattern, check **`isEndOfWord`**.
3. Cost is bounded by the number of nodes, and is close to `O(L)` with few wildcards.
4. This is DFS inside a Trie, not a loop.
