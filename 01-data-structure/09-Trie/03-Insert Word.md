# Insert Word

#### 1. Definition — Must Know

1. **Insert** adds a word to the Trie.
2. Walk down from the root, one character at a time. **Create** any node that does not exist yet.
3. After the last character, mark that node as an **end of word**.

#### 2. Why It Is Used — Must Know

1. It is the only way words get into the Trie.
2. It reuses nodes that already exist, so words with the same beginning cost almost nothing extra.
3. Every other operation (search, prefix check, autocomplete) depends on insert having built the right path.

#### 3. How It Works — Must Know

Insert `car`, then `cat`, into an empty Trie:

```text
Insert "car":
root → create c → create a → create r*        (3 new nodes)

Insert "cat":
root → c exists → a exists → create t*        (1 new node)

root
└── c
    └── a
        ├── r*
        └── t*
```

`cat` only created one new node, because `c → a` already existed.

#### 4. Core Concepts — Must Know

1. Start at the **root**.
2. For each character: if the child exists, move to it. If not, **create it**, then move.
3. At the end, set `isEndOfWord = true`.
4. Inserting a word that already exists changes nothing important. It is safe to repeat.

#### 5. Algorithm — Must Know

```text
node = root

for each character ch in word:
    if node has no child for ch:
        create a new node for ch
    node = child for ch

node.isEndOfWord = true
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun insert(word: String) {
    var node = root
    for (ch in word) {
        node = node.children.getOrPut(ch) { TrieNode() }
    }
    node.isEndOfWord = true
}
```

`getOrPut` returns the existing child, or creates and stores a new one.

#### 7. Time & Space Complexity — Must Know

| Case | Time |
|---|---:|
| Insert (any case) | `O(L)` |
| Extra space | `O(L)` worst case |

Why `O(L)`?

```text
One step per character. A fully new word creates up to L nodes.
A word made only of existing prefixes creates none.
```

#### 8. Common Insert Patterns — Must Know

1. Build a Trie from a list of words.
2. Insert a word while counting (see "Counting Words / Prefixes").
3. Insert and store the full word at the end node for easy retrieval.
4. Insert numbers as bits (see "Bitwise Trie").

#### 9. Edge Cases / Common Mistakes

1. Forgetting `isEndOfWord = true`. The word is then only a prefix and `search` fails.
2. Setting the end flag on the **root** by mistake.
3. Inserting the empty string. It marks the root itself as a word. Decide whether to allow it.
4. Overwriting an existing child with a new empty node, which erases the words below it. Always check first (`getOrPut` does this).
5. Mixing upper and lower case. `Car` and `car` become different paths.

#### 10. When to Use / When Not to Use

**Use when:**

1. You build the Trie once and then run many prefix queries.
2. Many words share beginnings.

**Avoid when:**

1. You only need a few exact lookups. A `HashSet` is cheaper to build.

#### 11. Related Topics

1. TrieNode Structure
2. Search Word
3. Prefix Search / `startsWith`
4. Counting Words / Prefixes

#### 12. Interview Must Remember

1. Walk the characters, **create missing nodes**, then **mark the last node as end of word**.
2. Insert is `O(L)`.
3. Never replace an existing child. Reuse it.
4. Forgetting the end flag is the most common bug.
