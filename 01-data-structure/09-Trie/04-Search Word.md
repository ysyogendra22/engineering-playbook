# Search Word

#### 1. Definition — Must Know

1. **Search** checks whether an exact word is stored in the Trie.
2. Walk down the characters. If a character has no matching child, the word is **not** there.
3. If you reach the last character, the word exists only if that node is marked as an **end of word**.

#### 2. Why It Is Used — Must Know

1. It is the dictionary lookup: "is this a valid word?"
2. It takes `O(L)` regardless of how many words are stored.
3. It teaches the key idea of a Trie: **a path existing is not enough**.

#### 3. How It Works — Must Know

Trie holds `car` and `cat`:

```text
root
└── c
    └── a
        ├── r*
        └── t*
```

```text
search("car") → c ✓ → a ✓ → r ✓ → r is end of word   → true
search("ca")  → c ✓ → a ✓ → a is NOT end of word      → false  (only a prefix)
search("cow") → c ✓ → o ✗                             → false
search("cart")→ c ✓ → a ✓ → r ✓ → t ✗                 → false
```

#### 4. Core Concepts — Must Know

1. **Walk the path** one character at a time.
2. **Missing child** → return `false` immediately.
3. **End of path** → return `isEndOfWord`, not `true`.
4. A helper `findNode(text)` that returns the final node (or `null`) is reused by search and by prefix check.

#### 5. Algorithm — Must Know

```text
node = root

for each character ch in word:
    if node has no child for ch:
        return false
    node = child for ch

return node.isEndOfWord
```

#### 6. Kotlin Implementation — Must Know

```kotlin
private fun findNode(text: String): TrieNode? {
    var node = root
    for (ch in text) {
        node = node.children[ch] ?: return null
    }
    return node
}

fun search(word: String): Boolean {
    return findNode(word)?.isEndOfWord == true
}
```

#### 7. Time & Space Complexity — Must Know

| Case | Time |
|---|---:|
| Best (first character missing) | `O(1)` |
| Worst | `O(L)` |
| Space | `O(1)` |

Why `O(L)`?

```text
At most one step per character of the searched word.
```

#### 8. Common Search Patterns — Must Know

1. Exact dictionary lookup.
2. Check whether a candidate word is valid before using it.
3. The base for wildcard search (see "Wildcard Search").
4. The base for prefix matching and autocomplete.

#### 9. Edge Cases / Common Mistakes

1. Returning `true` when the path exists but the last node is not an end of word (the `ca` case above).
2. Not handling the empty string. It is found only if the root itself was marked as a word.
3. Using `!!` on a missing child and crashing instead of returning `false`.
4. Case mismatch: searching `Car` when `car` was inserted.
5. Searching a word longer than any stored word. The walk fails at the first missing character.

#### 10. When to Use / When Not to Use

**Use when:**

1. You also need prefix queries on the same data.

**Avoid when:**

1. You only ever check exact words. A `HashSet` does the same job with less code and memory.

#### 11. Related Topics

1. Insert Word
2. Prefix Search / `startsWith`
3. Word Dictionary / Prefix Matching
4. Wildcard Search

#### 12. Interview Must Remember

1. Walk the path. Missing child → `false`.
2. At the end, return **`isEndOfWord`**, not `true`.
3. Search is `O(L)`.
4. `search("ca")` is `false` when only `car` is stored. This is the classic trap.
