# Trie Fundamentals

#### 1. Definition — Must Know

1. A **Trie** (said "try", also called a **prefix tree**) is a tree that stores strings **one character per node**.
2. The path from the root down to a node spells a **prefix**.
3. A node marked as an **end of word** means that prefix is also a complete stored word.
4. Words that start the same way **share the same nodes**.

#### 2. Why It Is Used — Must Know

1. Answers "does any stored word start with this prefix?" in `O(L)`, where `L` is the length of the prefix. The number of stored words does not matter.
2. A `HashSet` checks a whole word quickly, but it cannot answer a prefix question without looking at every word.
3. It is the standard structure behind autocomplete, dictionaries, and spell checkers.

#### 3. How It Works — Must Know

Store `cat`, `car`, `do`, `dog`:

```text
root
├── c
│   └── a
│       ├── t*     ← "cat"
│       └── r*     ← "car"
└── d
    └── o*         ← "do"
        └── g*     ← "dog"
```

`*` marks an end of word.

1. `c → a` is stored **once**, even though `cat` and `car` both use it.
2. `do` is a word **and** a prefix of `dog`, so the node for `o` is both an end of word and has a child.

#### 4. Core Concepts — Must Know

1. **Root** — an empty node. It stands for the empty prefix and holds no character.
2. **Node** — represents one character, reached from its parent.
3. **Children** — the possible next characters after this prefix.
4. **End-of-word marker** — a flag that says "a stored word stops here".
5. **Shared prefix** — common beginnings are stored once, which saves space and makes prefix queries natural.

#### 5. Algorithm — Must Know

The three basic ideas (each has its own topic):

```text
Insert:     walk down the characters, create missing nodes, mark the last node as end of word
Search:     walk down; if a character is missing → false; otherwise return last.isEndOfWord
startsWith: walk down; if a character is missing → false; otherwise true
```

#### 6. Kotlin Implementation — Must Know

The building block (the full class is in topic 7):

```kotlin
class TrieNode {
    val children = HashMap<Char, TrieNode>()
    var isEndOfWord = false
}
```

#### 7. Time & Space Complexity — Must Know

`N` = number of words, `L` = length of the word or prefix being handled.

| Operation | Time |
|---|---:|
| Insert a word | `O(L)` |
| Search a word | `O(L)` |
| Prefix check | `O(L)` |
| Space (worst case) | `O(total characters stored)` |

Why `O(L)`?

```text
Every step moves one level deeper, and the walk stops after L characters.
The number of stored words N never appears in the cost.
```

#### 8. Common Trie Patterns — Must Know

1. Prefix existence (`startsWith`).
2. Word dictionary and prefix matching.
3. Autocomplete and prefix suggestions.
4. Wildcard search.
5. Counting words that share a prefix.
6. Binary trie for numbers.

Study these patterns in the next topics.

#### 9. Edge Cases / Common Mistakes

1. Returning `true` from `search` just because the path exists. The last node must be marked as an end of word.
2. Forgetting that a word can be a prefix of another word (`do` and `dog`).
3. Forgetting the empty string.
4. Treating the root as if it holds a character.
5. Using a Trie when a `HashSet` would be enough.

#### 10. When to Use / When Not to Use

**Use when:**

1. You answer many prefix queries.
2. Many words share beginnings.
3. You need all words with a prefix, in alphabetical order.

**Avoid when:**

1. You only need exact word lookup. A `HashSet` is simpler and lighter.
2. There are few words.
3. Words are long and share almost nothing. A Trie then uses far more memory than a set.

#### 11. Related Topics

1. TrieNode Structure
2. Insert Word, Search Word, Prefix Search
3. Tree basics (`01-data-structure/07-Tree`)
4. HashMap / HashSet (`01-data-structure/05-HashMap`, `06-HashSet`)

#### 12. Interview Must Remember

1. A Trie stores **one character per node**, and shared prefixes share nodes.
2. Insert, search, and prefix check are all `O(L)`, independent of the number of words.
3. **End-of-word marker** is what separates a word from a mere prefix.
4. Use a Trie for **prefix** questions. Use a `HashSet` for exact lookup.
