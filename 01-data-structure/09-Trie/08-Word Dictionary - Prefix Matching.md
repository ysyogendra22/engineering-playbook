# Word Dictionary / Prefix Matching

#### 1. Definition — Must Know

1. A **word dictionary** is a Trie used as a set of valid words.
2. **Prefix matching** uses that dictionary to answer questions about the *beginnings* of other strings: "which dictionary word is a prefix of this word?" or "what do all these words have in common at the start?"
3. This is the step between the basic operations and full autocomplete.

#### 2. Why It Is Used — Must Know

1. One walk through the Trie can check many prefixes of a string at once, because they are all on the same path.
2. It replaces repeated `startsWith` calls or repeated string comparisons with a single pass.
3. Typical tasks: replacing words with their shortest root, finding the longest common prefix, and validating input against a list.

#### 3. How It Works — Must Know

Dictionary: `cat`, `bat`, `rat`. Sentence word: `cattle`.

```text
Walk "cattle" through the Trie:
c ✓ → a ✓ → t ✓ and t is an end of word → the shortest root is "cat"
```

Stop at the **first end-of-word node** to get the shortest matching root.

Longest common prefix of `flower`, `flow`, `flight`:

```text
root → f → l → (two children: o and i)   ← branching: stop here
Common prefix: "fl"
```

#### 4. Core Concepts — Must Know

1. **Shortest matching prefix** — stop at the first node with `isEndOfWord = true`.
2. **Longest matching prefix** — keep going and remember the last end-of-word seen.
3. **Longest common prefix of all words** — walk while the node has exactly one child and is not an end of word.
4. One pass is `O(L)` for a word of length `L`.

#### 5. Algorithm — Must Know

```text
shortestRoot(word):
    node = root
    for each character ch in word:
        if node has no child for ch: return null
        node = child for ch
        append ch to the prefix so far
        if node.isEndOfWord: return the prefix so far
    return null
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Methods inside the Trie class from "Trie Implementation"

fun shortestRoot(word: String): String? {
    var node = root
    val prefix = StringBuilder()
    for (ch in word) {
        node = node.children[ch] ?: return null
        prefix.append(ch)
        if (node.isEndOfWord) return prefix.toString()
    }
    return null
}

// Replace each word in a sentence with its shortest root, if it has one
fun replaceWords(sentence: String): String =
    sentence.split(" ").joinToString(" ") { shortestRoot(it) ?: it }

// Longest common prefix of every word stored in the Trie
fun longestCommonPrefix(): String {
    val prefix = StringBuilder()
    var node = root
    while (node.children.size == 1 && !node.isEndOfWord) {
        val (ch, next) = node.children.entries.first()
        prefix.append(ch)
        node = next
    }
    return prefix.toString()
}
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time | Space |
|---|---:|---:|
| Build the dictionary | `O(total characters)` | `O(total characters)` |
| `shortestRoot` for one word | `O(L)` | `O(L)` for the prefix string |
| `replaceWords` | `O(total characters of the sentence)` | `O(sentence length)` |
| `longestCommonPrefix` | `O(length of the answer)` | `O(length of the answer)` |

#### 8. Common Prefix-Matching Patterns — Must Know

1. **Replace Words** (LeetCode 648) — replace each word by its shortest dictionary root.
2. **Longest Common Prefix** (LeetCode 14) — usually solved by comparing characters, but a Trie shows the same idea.
3. Check that an input string starts with any dictionary word.
4. Find the longest dictionary word that is a prefix of the input (remember the last end-of-word on the walk).

#### 9. Edge Cases / Common Mistakes

1. Not stopping at the **first** end of word when the task asks for the *shortest* root.
2. Returning a partial prefix that is not a dictionary word (the end-of-word check is what makes it valid).
3. Longest common prefix: forgetting that a stored word can end before the branch (`flow` inside `flower`). The `!node.isEndOfWord` check handles this.
4. An empty dictionary or an empty input word.
5. Words in the sentence separated by more than one space when using `split(" ")`.

#### 10. When to Use / When Not to Use

**Use when:**

1. One dictionary is checked against many strings.
2. You need the shortest or longest matching prefix.

**Avoid when:**

1. The dictionary is tiny. A simple loop with `startsWith` on a list is clearer.
2. You only compare a few strings once.

#### 11. Related Topics

1. Search Word
2. Prefix Search / `startsWith`
3. Autocomplete / Prefix Suggestions
4. String (`01-data-structure/01-Array`, `02-algorithm/08-String Algorithms`)

#### 12. Interview Must Remember

1. Stop at the **first end-of-word** for the shortest root. Remember the **last** one for the longest.
2. One walk down the Trie checks all prefixes of a string.
3. Longest common prefix = walk while there is exactly one child and no word ends.
4. Cost is `O(L)` per word.
