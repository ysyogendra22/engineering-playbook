# Counting Words / Prefixes

#### 1. Definition — Must Know

1. A **counting Trie** stores numbers in its nodes, so you can answer counts without visiting a whole subtree.
2. Two counts are used:
   - `passCount` — how many inserted words pass through this node (their prefix includes it)
   - `endCount` — how many inserted words end exactly at this node
3. This answers "how many words equal X?" and "how many words start with X?" in `O(L)`.

#### 2. Why It Is Used — Must Know

1. Without counts, "how many words start with this prefix?" needs a DFS over the whole subtree.
2. With counts it is a single walk, then one read.
3. It also supports duplicates, because `endCount` can be greater than 1.

#### 3. How It Works — Must Know

Insert `car`, `car`, `cat`:

```text
root
└── c   (pass 3)
    └── a   (pass 3)
        ├── r   (pass 2, end 2)     ← "car" twice
        └── t   (pass 1, end 1)     ← "cat" once
```

```text
countWordsEqualTo("car")        → end count at r             = 2
countWordsStartingWith("ca")    → pass count at a            = 3
countWordsStartingWith("cat")   → pass count at t            = 1
countWordsStartingWith("dog")   → path missing               = 0
```

#### 4. Core Concepts — Must Know

1. On insert, **increase `passCount` on every node visited** (not the root). At the last node, also increase `endCount`.
2. On erase, do the opposite along the same path.
3. `passCount` of a node = number of words whose prefix includes that node.
4. A node with `passCount = 0` is unused and can be removed.

#### 5. Algorithm — Must Know

```text
insert(word):
    node = root
    for each character ch in word:
        node = child for ch (create if missing)
        node.passCount += 1
    node.endCount += 1

countWordsEqualTo(word):     node = findNode(word); return node?.endCount ?: 0
countWordsStartingWith(p):   node = findNode(p);    return node?.passCount ?: 0

erase(word):                 (word is assumed to exist)
    walk the path, decreasing passCount on each node
    decrease endCount on the last node
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class CountingNode {
    val children = HashMap<Char, CountingNode>()
    var passCount = 0
    var endCount = 0
}

class CountingTrie {

    private val root = CountingNode()

    fun insert(word: String) {
        var node = root
        for (ch in word) {
            node = node.children.getOrPut(ch) { CountingNode() }
            node.passCount++
        }
        node.endCount++
    }

    fun countWordsEqualTo(word: String): Int = findNode(word)?.endCount ?: 0

    fun countWordsStartingWith(prefix: String): Int = findNode(prefix)?.passCount ?: 0

    fun erase(word: String) {
        if (countWordsEqualTo(word) == 0) return        // not stored
        var node = root
        for (ch in word) {
            val next = node.children.getValue(ch)
            next.passCount--
            if (next.passCount == 0) {                   // nothing uses it any more
                node.children.remove(ch)
                return
            }
            node = next
        }
        node.endCount--
    }

    private fun findNode(text: String): CountingNode? {
        var node = root
        for (ch in text) {
            node = node.children[ch] ?: return null
        }
        return node
    }
}
```

When `passCount` falls to 0, the rest of that branch belongs to this word only, so removing the child drops it all at once.

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `insert` | `O(L)` |
| `countWordsEqualTo` | `O(L)` |
| `countWordsStartingWith` | `O(P)` |
| `erase` | `O(L)` |
| Extra space | two integers per node |

#### 8. Common Counting Patterns — Must Know

1. **Implement Trie II (Prefix Tree)** (LeetCode 1804, premium) — exactly this class.
2. Count how many strings share a prefix with a query.
3. Score a word by how many other words share its prefixes.
4. Frequency for ranking autocomplete suggestions (see "Autocomplete / Prefix Suggestions").

#### 9. Edge Cases / Common Mistakes

1. Increasing `passCount` on the root, or forgetting to increase it on the last node.
2. Updating only `endCount` and then answering prefix counts wrongly.
3. Erasing a word that is not stored, driving counts negative.
4. Removing a node while other words still use it. Remove only when `passCount` reaches 0.
5. Using a `Boolean` end flag when duplicates must be counted.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need counts for prefixes or exact words, often.
2. Duplicates are allowed.

**Avoid when:**

1. Only existence matters. A plain Trie is lighter.
2. You can afford a DFS because counts are rare.

#### 11. Related Topics

1. Insert Word
2. Delete Word from Trie
3. Prefix Search / `startsWith`
4. Autocomplete / Prefix Suggestions

#### 12. Interview Must Remember

1. **`passCount`** = words passing through. **`endCount`** = words ending here.
2. Prefix count = `passCount` of the prefix node. Exact count = `endCount`.
3. Erase reverses insert along the same path.
4. Counts turn a subtree walk into an `O(P)` lookup.
