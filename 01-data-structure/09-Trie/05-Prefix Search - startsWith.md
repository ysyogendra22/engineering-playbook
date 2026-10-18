# Prefix Search / `startsWith`

#### 1. Definition — Must Know

1. **Prefix search** (`startsWith`) checks whether **any stored word begins with** a given prefix.
2. Walk the prefix through the Trie. If every character has a matching child, the answer is `true`.
3. Unlike `search`, it does **not** care whether the last node is an end of word.

#### 2. Why It Is Used — Must Know

1. This is the operation a Trie exists for. A `HashSet` cannot answer it without scanning every word.
2. It is the first step of autocomplete, search suggestions, and prefix counting.
3. It costs `O(P)`, where `P` is the prefix length.

#### 3. How It Works — Must Know

Trie holds `car`, `cat`, `dog`:

```text
root
├── c
│   └── a
│       ├── r*
│       └── t*
└── d
    └── o
        └── g*
```

```text
startsWith("ca")  → c ✓ → a ✓                 → true
startsWith("car") → c ✓ → a ✓ → r ✓           → true
startsWith("do")  → d ✓ → o ✓                 → true  (even though "do" is not a word)
startsWith("cow") → c ✓ → o ✗                 → false
startsWith("")    → no characters to check    → true  (every word starts with "")
```

#### 4. Core Concepts — Must Know

1. Same walk as `search`.
2. **Reaching the end of the prefix is enough.** No end-of-word check.
3. Both operations share the helper `findNode(text)`.

| | `search(word)` | `startsWith(prefix)` |
|---|---|---|
| Missing child | `false` | `false` |
| Path complete | `isEndOfWord` | `true` |
| `"ca"` with only `car` stored | `false` | `true` |

#### 5. Algorithm — Must Know

```text
node = root

for each character ch in prefix:
    if node has no child for ch:
        return false
    node = child for ch

return true
```

#### 6. Kotlin Implementation — Must Know

Reuses `findNode` from "Search Word":

```kotlin
fun startsWith(prefix: String): Boolean {
    return findNode(prefix) != null
}
```

#### 7. Time & Space Complexity — Must Know

| Case | Time |
|---|---:|
| Best | `O(1)` |
| Worst | `O(P)` |
| Space | `O(1)` |

Why `O(P)`?

```text
One step per prefix character. The number of stored words does not matter.
```

Compare with a `HashSet<String>`: checking a prefix means testing every word, `O(N · P)`.

#### 8. Common Prefix Patterns — Must Know

1. "Is there any word that starts with …?"
2. Reject a path early in a search (prune when no word can continue).
3. Count how many words share a prefix (see "Counting Words / Prefixes").
4. Collect all words with a prefix (see "Trie + DFS" and "Autocomplete").

#### 9. Edge Cases / Common Mistakes

1. Checking `isEndOfWord` in `startsWith`. That turns it into `search`.
2. Treating the empty prefix as `false`. With the `findNode` helper it returns the root, so `startsWith("")` is `true`, even for an empty Trie. Decide whether your problem wants that, and handle it explicitly if not.
3. Case mismatch between inserted words and the prefix.
4. Forgetting that the prefix can be a full word too (`startsWith("car")` is `true` when `car` is stored).

#### 10. When to Use / When Not to Use

**Use when:**

1. Questions are about beginnings of words.
2. You want to stop a search early when no stored word can match.

**Avoid when:**

1. Questions are about the middle or end of words. A Trie is organised by prefix only.

#### 11. Related Topics

1. Search Word
2. Trie + DFS
3. Autocomplete / Prefix Suggestions
4. Counting Words / Prefixes

#### 12. Interview Must Remember

1. `startsWith` = walk the prefix. **No** end-of-word check.
2. `O(P)`, independent of the number of words.
3. `search("ca")` is `false` but `startsWith("ca")` is `true` when only `car` is stored.
4. Share one `findNode` helper between both.
