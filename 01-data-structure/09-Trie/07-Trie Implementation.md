# Trie Implementation

#### 1. Definition — Must Know

1. This is the complete, interview-ready Trie class: `insert`, `search`, and `startsWith`.
2. It is the classic problem *Implement Trie (Prefix Tree)* (LeetCode 208). If a number and a title ever disagree, trust the title.
3. Everything else in this folder builds on this class.

#### 2. Why It Is Used — Must Know

1. It is asked directly in interviews, and it is the starting point for harder Trie questions.
2. You can write it in a few minutes once the three operations are clear.

#### 3. How It Works — Must Know

Run these calls in order:

```text
insert("apple")      → a → p → p → l → e*
search("apple")      → true
search("app")        → false   (path exists, but "app" is not an end of word)
startsWith("app")    → true
insert("app")        → marks the second p as an end of word
search("app")        → true
```

```text
root
└── a
    └── p
        └── p*        ← "app" (added last)
            └── l
                └── e*    ← "apple"
```

#### 4. Core Concepts — Must Know

1. One `root` node, created once.
2. `insert` creates missing nodes and marks the end.
3. `search` and `startsWith` share one helper, `findNode`.
4. The difference between them is a single check: `isEndOfWord`.

#### 5. Algorithm — Must Know

```text
class Trie:
    root = new node

    insert(word):      walk, create missing nodes, mark last as end
    findNode(text):    walk; return last node, or null if a character is missing
    search(word):      findNode(word) exists AND is end of word
    startsWith(prefix):findNode(prefix) exists
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class TrieNode {
    val children = HashMap<Char, TrieNode>()
    var isEndOfWord = false
}

class Trie {

    private val root = TrieNode()

    fun insert(word: String) {
        var node = root
        for (ch in word) {
            node = node.children.getOrPut(ch) { TrieNode() }
        }
        node.isEndOfWord = true
    }

    fun search(word: String): Boolean {
        return findNode(word)?.isEndOfWord == true
    }

    fun startsWith(prefix: String): Boolean {
        return findNode(prefix) != null
    }

    private fun findNode(text: String): TrieNode? {
        var node = root
        for (ch in text) {
            node = node.children[ch] ?: return null
        }
        return node
    }
}
```

Array version, if the input is only lowercase `a`–`z`:

```kotlin
class ArrayTrieNode {
    val children = arrayOfNulls<ArrayTrieNode>(26)
    var isEndOfWord = false
}
// child lookup: node.children[ch - 'a']
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time | Extra space |
|---|---:|---:|
| `insert` | `O(L)` | `O(L)` worst case |
| `search` | `O(L)` | `O(1)` |
| `startsWith` | `O(P)` | `O(1)` |
| Whole Trie | | `O(total characters)` |

#### 8. Common Implementation Patterns — Must Know

1. Add a `delete` method (see "Delete Word from Trie").
2. Add counts to each node (see "Counting Words / Prefixes").
3. Add `wordsWithPrefix` using DFS (see "Trie + DFS").
4. Add `.` wildcard support (see "Wildcard Search").

#### 9. Edge Cases / Common Mistakes

1. `search` returning `true` for a prefix that is not a stored word.
2. Not marking `isEndOfWord` in `insert`.
3. Duplicating the walking code in `search` and `startsWith` instead of sharing `findNode`.
4. Using `Array(26)` and then receiving an uppercase letter or digit.
5. Making `root` public so outside code can change the structure.

#### 10. When to Use / When Not to Use

**Use when:**

1. The problem asks for prefix operations on a set of words.

**Avoid when:**

1. The problem needs exact lookup only. Use a `HashSet`.

#### 11. Related Topics

1. Insert Word, Search Word, Prefix Search
2. TrieNode Structure
3. Word Dictionary / Prefix Matching
4. Delete Word from Trie

#### 12. Interview Must Remember

1. Three methods: `insert`, `search`, `startsWith`.
2. `search` checks **`isEndOfWord`**. `startsWith` does not.
3. Share one `findNode` helper.
4. Say the complexity out loud: `O(L)` per operation.
