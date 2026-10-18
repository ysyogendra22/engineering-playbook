# TrieNode Structure

#### 1. Definition — Must Know

1. A **TrieNode** is the building block of a Trie.
2. Every node stores two things:
   - its **children** (the next characters that can follow), and
   - an **end-of-word flag**.
3. The character itself is usually **not stored in the node**. It is the key used to reach the node from its parent.

#### 2. Why It Is Used — Must Know

1. The node design decides the memory use and the speed of every Trie operation.
2. Two designs are common: a **map** of children, or a fixed **array** of children.
3. Extra fields (counts, a stored word) turn a plain Trie into a counting or autocomplete Trie.

#### 3. How It Works — Must Know

A node for the prefix `ca` in a Trie holding `cat` and `car`:

```text
Node "ca"
├── isEndOfWord = false
└── children
    ├── 't' → Node "cat"
    └── 'r' → Node "car"
```

The edge label (`'t'`, `'r'`) is the key in the `children` map.

#### 4. Core Concepts — Must Know

1. **`children`** — maps a character to the next node.
2. **`isEndOfWord`** — `true` if a stored word ends at this node.
3. **No parent pointer** is needed for basic operations. Walking down is enough.
4. **Optional fields:**
   - `passCount` / `endCount` — for counting words and prefixes
   - `word` — store the full word at its end node for easy retrieval

#### 5. Two Common Designs — Must Know

| | `HashMap<Char, TrieNode>` | `Array<TrieNode?>(26)` |
|---|---|---|
| Lookup of a child | Hash lookup | Direct index: `c - 'a'` |
| Memory per node | Only the children that exist | Always 26 slots |
| Character set | Any character | Fixed (for example `a`–`z`) |
| Best for | Mixed or large alphabets, sparse Tries | Lowercase letters, dense Tries, speed |

#### 6. Kotlin Implementation — Must Know

Map version (flexible, used in these notes):

```kotlin
class TrieNode {
    val children = HashMap<Char, TrieNode>()
    var isEndOfWord = false
}
```

Array version (lowercase `a`–`z` only):

```kotlin
class ArrayTrieNode {
    val children = arrayOfNulls<ArrayTrieNode>(26)
    var isEndOfWord = false
}

// reach or create a child
val index = ch - 'a'
val next = node.children[index] ?: ArrayTrieNode().also { node.children[index] = it }
```

#### 7. Time & Space Complexity — Must Know

| Design | Child lookup | Space per node |
|---|---:|---:|
| `HashMap` | `O(1)` average | grows with the children that exist |
| `Array(26)` | `O(1)` | `O(26)` always |

Total nodes in a Trie are at most **the total number of stored characters + 1** (the root). Sharing prefixes makes it smaller.

#### 8. Common Node Variations — Must Know

1. Plain node: `children` + `isEndOfWord`.
2. Counting node: add `passCount` and `endCount` (see "Counting Words / Prefixes").
3. Word-storing node: add `var word: String? = null` and set it at the end node. Useful for returning matches without rebuilding the string.
4. Binary node: only two children, for `0` and `1` (see "Bitwise Trie").

#### 9. Edge Cases / Common Mistakes

1. `Array(26)` with an uppercase letter, a digit, or a space. The index goes out of range.
2. Allocating all 26 slots for a Trie that holds only a few words. Memory is wasted.
3. Storing the character in the node *and* using it as the map key. It is redundant.
4. Forgetting that `HashMap` iteration order is not alphabetical. Sort the keys when order matters.

#### 10. When to Use / When Not to Use

**Use `HashMap` children when:**

1. The alphabet is large or unknown (Unicode, mixed case, digits).
2. The Trie is sparse.

**Use `Array(26)` children when:**

1. Input is guaranteed lowercase `a`–`z`.
2. You want the fastest, simplest child access.

#### 11. Related Topics

1. Trie Fundamentals
2. Insert Word
3. Counting Words / Prefixes
4. Bitwise Trie / Binary Trie

#### 12. Interview Must Remember

1. A node = **children + end-of-word flag**.
2. **Map** children are flexible. **Array(26)** children are fast but fixed to one alphabet.
3. Number of nodes ≤ total characters stored + 1.
4. Say which design you chose and **why** (alphabet size and sparsity).
