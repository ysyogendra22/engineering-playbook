# Delete Word from Trie

#### 1. Definition — Must Know

1. **Delete** removes a word from the Trie.
2. The word must stop being found by `search`.
3. Other words must keep working. Nodes that other words still use must **not** be removed.

#### 2. Why It Is Used — Must Know

1. Real dictionaries change: words are removed, expired, or corrected.
2. It is a common follow-up question, because the careful part is *how much to remove*.
3. It tests whether you understand shared prefixes.

#### 3. How It Works — Must Know

Trie holds `car`, `cat`, `do`, `dog`, `fan`:

```text
root
├── c
│   └── a
│       ├── r*
│       └── t*
├── d
│   └── o*
│       └── g*
└── f
    └── a
        └── n*
```

Four cases:

```text
delete("fan")  → unique chain f → a → n. Remove all three nodes.
delete("car")  → shares "ca" with "cat". Remove only the node r. Keep c and a.
delete("do")   → "do" is a prefix of "dog". Only unmark the end flag. Keep every node.
delete("cow")  → not in the Trie. Do nothing.
```

#### 4. Core Concepts — Must Know

1. **Unmark** the end-of-word flag on the last node. That alone makes `search` return `false`.
2. **Prune** (remove) nodes upward only while a node:
   - is not an end of word, **and**
   - has no children left.
3. **Stop pruning** at the first node that another word still needs.
4. Two valid strategies:
   - **Lazy delete** — only unmark. Simple, but unused nodes stay in memory.
   - **Full delete** — unmark and prune. Frees memory, needs recursion or a stack.

#### 5. Algorithm — Must Know

```text
delete(word):
    if word is not in the Trie: return
    deleteHelper(root, word, 0)

deleteHelper(node, word, index):    // returns true if the caller should remove this node
    if index == word.length:
        node.isEndOfWord = false
        return node has no children

    child = node.children[word[index]]
    if deleteHelper(child, word, index + 1):
        remove that child from node.children

    return (not node.isEndOfWord) and node has no children
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Methods inside the Trie class from "Trie Implementation"

// Lazy delete: simple, keeps the nodes
fun deleteLazy(word: String) {
    findNode(word)?.isEndOfWord = false
}

// Full delete: unmark, then prune nodes nobody needs
fun delete(word: String) {
    if (!search(word)) return                  // not stored: nothing to do
    deleteHelper(root, word, 0)
}

// Returns true when the caller should remove this node from its parent
private fun deleteHelper(node: TrieNode, word: String, index: Int): Boolean {
    if (index == word.length) {
        node.isEndOfWord = false
        return node.children.isEmpty()
    }
    val ch = word[index]
    val child = node.children[ch] ?: return false
    if (deleteHelper(child, word, index + 1)) {
        node.children.remove(ch)
    }
    return !node.isEndOfWord && node.children.isEmpty()
}
```

The return value of the very first call (for the root) is ignored. The root is never removed.

Trace `delete("car")` with `cat` present:

```text
r: isEndOfWord = false, no children          → return true  (remove r)
a: removes r, still has child t              → return false (stop pruning)
c, root: nothing more to remove
```

#### 7. Time & Space Complexity — Must Know

| Strategy | Time | Extra space |
|---|---:|---:|
| Lazy delete | `O(L)` | `O(1)` |
| Full delete | `O(L)` | `O(L)` recursion |

#### 8. Common Delete Patterns — Must Know

1. Remove a word from a live dictionary.
2. Remove a user's history or a banned word.
3. With counts: decrement along the path instead of removing (see "Counting Words / Prefixes").

#### 9. Edge Cases / Common Mistakes

1. Removing nodes that another word uses (deleting `car` also deletes `cat`).
2. Removing the whole chain when the deleted word is a prefix of a longer word (`do` and `dog`).
3. Crashing when the word is not in the Trie. Check with `search` first.
4. Removing the root.
5. Forgetting to unmark `isEndOfWord`, so the word still appears after "deleting".

#### 10. When to Use / When Not to Use

**Use full delete when:**

1. The Trie is large, and words are removed often.

**Use lazy delete when:**

1. Deletes are rare, or you want the simplest correct code.
2. The Trie is rebuilt regularly anyway.

#### 11. Related Topics

1. Insert Word
2. Search Word
3. Common Trie Edge Cases
4. Counting Words / Prefixes
5. Recursion (`02-algorithm/03-Recursion & Divide and Conquer`)

#### 12. Interview Must Remember

1. Always **unmark** the end flag first.
2. **Prune only nodes that are not a word and have no children.**
3. A word that is a prefix of another word is only unmarked, never pruned.
4. Lazy delete is acceptable. Say it, then offer the full version.
