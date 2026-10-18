# Common Trie Edge Cases

#### 1. Definition — Must Know

1. These are the inputs and situations that most often break a Trie solution.
2. Most bugs come from confusing a **prefix** with a **word**, or from the way the Trie is built, not from the walking logic itself.
3. Check this list before you submit any Trie code.

#### 2. Why It Is Used — Must Know

1. A Trie works on the happy path very easily, so interviewers use edge cases to see whether you think carefully.
2. Fixing these cases early saves debugging time.

#### 3. How It Works — Must Know

Trie holds only `do` and `dog`:

```text
root
└── d
    └── o*        ← "do" is a word
        └── g*    ← "dog" is a word
```

```text
search("do")     → true      (a word that is also a prefix of another word)
search("d")      → false     (only a prefix)
search("dogs")   → false     (path breaks after g)
startsWith("d")  → true
```

#### 4. Core Concepts — Must Know

1. A node can be an end of word **and** have children.
2. A path can exist without being a word.
3. The root represents the empty prefix and normally holds no word.
4. Everything depends on the same rule: **`isEndOfWord` decides a word, the path decides a prefix.**

#### 5. Edge Case Checklist — Must Know

| Case | What should happen |
|---|---|
| Empty Trie | `search` → `false`; `startsWith("x")` → `false` |
| Empty string `""` | `startsWith("")` → `true`; `search("")` is `true` only if `""` was inserted |
| Single character word | Works like any other word: one node with the end flag |
| Prefix of another word (`app` and `apple`) | Both must be searchable. The end flag must exist on the earlier node |
| Word longer than anything stored | `search` and `startsWith` return `false` when the path breaks |
| Duplicate insert | No change. Safe to repeat (but counts increase in a counting Trie) |
| Upper vs lower case | `Car` and `car` are different paths unless you normalise first |
| Non-lowercase character with `Array(26)` | Index out of range. Validate or use a `HashMap` |
| Spaces and punctuation | Treated as normal characters in a `HashMap` Trie |
| Unicode / emoji | Kotlin `Char` is a UTF-16 unit. Some symbols take two units |
| Delete a word that is a prefix of another | Unmark the end flag, but **do not remove** nodes that other words use |
| Delete a word that is missing | Do nothing and do not break the structure |

#### 6. Kotlin Implementation — Must Know

Defensive handling for the common cases:

```kotlin
fun insert(word: String) {
    if (word.isEmpty()) return                       // decide: ignore the empty string
    var node = root
    for (ch in word) {
        node = node.children.getOrPut(ch) { TrieNode() }
    }
    node.isEndOfWord = true
}

fun search(word: String): Boolean = findNode(word)?.isEndOfWord == true

// Normalise before inserting or searching when case should not matter
fun normalise(text: String) = text.lowercase()
```

#### 7. Time & Space Complexity — Must Know

Edge cases do not change the complexity. Every operation is still `O(L)`.

Normalising a string (for example `lowercase()`) adds one more `O(L)` pass, which is fine.

#### 8. Common Edge-Case Patterns — Must Know

1. **Prefix vs word:** test `search("app")` after inserting only `apple`.
2. **Word that is a prefix:** test `search("app")` after inserting both `app` and `apple`.
3. **Empty input:** test the empty Trie and the empty string.
4. **Case sensitivity:** state your assumption out loud.
5. **Alphabet assumption:** state it (`a`–`z` only, or any character).

#### 9. Edge Cases / Common Mistakes

1. Treating `search("ca")` as `true` because the path exists.
2. Marking the end flag on the wrong node.
3. Removing shared nodes during delete, which breaks other words.
4. Assuming lowercase letters and crashing on other input.
5. Not stating assumptions (alphabet, case, empty string) before coding.

#### 10. When to Use / When Not to Use

**Use this checklist:**

1. Before you write the solution, to state your assumptions.
2. After you write it, to dry-run two or three cases by hand.

**Skip nothing:** edge-case thinking applies to every Trie problem.

#### 11. Related Topics

1. Search Word
2. Prefix Search / `startsWith`
3. Delete Word from Trie
4. TrieNode Structure

#### 12. Interview Must Remember

1. **Path = prefix. End flag = word.**
2. A word can also be a prefix of a longer word.
3. State your assumptions: alphabet, case, and empty string.
4. Test `app` / `apple` and the empty Trie on every solution.
