# Trie + DFS

#### 1. Definition — Must Know

1. **Trie + DFS** means finding the Trie node for a prefix, then using **depth-first search** to visit everything below it.
2. It answers "give me every word that starts with this prefix", and "how many words are under this node?"
3. Plain search and `startsWith` only walk one path. DFS explores **all** paths below a node.

#### 2. Why It Is Used — Must Know

1. A Trie keeps all words with the same prefix in one subtree, so they are easy to collect.
2. It is the basis of autocomplete, listing suggestions, and any "all matches" question.
3. It also shows why a Trie is a Tree: the same DFS ideas apply (`01-data-structure/07-Tree`).

#### 3. How It Works — Must Know

Trie holds `car`, `card`, `care`, `cat`. Collect all words with prefix `car`:

```text
root → c → a → r*        ← walk the prefix "car" to this node
                ├── d*
                └── e*

Start DFS at the node for "car", with path = "car":
  r is an end of word  → add "car"
  go to d              → path "card", end of word → add "card"
  go to e              → path "care", end of word → add "care"

Result: ["car", "card", "care"]      ("cat" is under a different branch and is never visited)
```

#### 4. Core Concepts — Must Know

1. **Step 1:** walk the prefix with `findNode`. If it is missing, the answer is empty.
2. **Step 2:** DFS from that node, building the current word in a `StringBuilder`.
3. **Add a word** whenever the current node is an end of word.
4. **Undo the last character** after returning from a child, so the path stays correct.
5. The recursion depth is at most the length of the longest word.

#### 5. Algorithm — Must Know

```text
wordsWithPrefix(prefix):
    start = findNode(prefix)
    if start is null: return empty list
    collect(start, prefix, results)

collect(node, path, results):
    if node.isEndOfWord: results.add(path)
    for each (ch, child) in node.children:
        append ch to path
        collect(child, path, results)
        remove the last character from path
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Methods inside the Trie class from "Trie Implementation"

fun wordsWithPrefix(prefix: String): List<String> {
    val start = findNode(prefix) ?: return emptyList()
    val results = mutableListOf<String>()
    collect(start, StringBuilder(prefix), results)
    return results
}

private fun collect(node: TrieNode, path: StringBuilder, results: MutableList<String>) {
    if (node.isEndOfWord) results.add(path.toString())
    for (ch in node.children.keys.sorted()) {        // sorted → alphabetical order
        path.append(ch)
        collect(node.children.getValue(ch), path, results)
        path.deleteCharAt(path.length - 1)           // undo
    }
}

// Count how many words are stored below (and at) a node
private fun countWords(node: TrieNode): Int =
    (if (node.isEndOfWord) 1 else 0) + node.children.values.sumOf { countWords(it) }
```

`HashMap` does not keep order. Sorting the keys gives alphabetical results.

#### 7. Time & Space Complexity — Must Know

`S` = number of nodes in the subtree under the prefix.

| Step | Time |
|---|---:|
| Walk the prefix | `O(P)` |
| DFS over the subtree | `O(S)` |
| Total | `O(P + S)`, plus the cost of building the result strings |
| Space (recursion + path) | `O(longest word)` |

Sorting keys at every node adds a small factor of `A log A`, where `A` is the alphabet size.

#### 8. Common Trie + DFS Patterns — Must Know

1. List all words with a prefix.
2. Count words below a node.
3. Find the longest word in the Trie.
4. Visit all words in alphabetical order (DFS with sorted children, starting at the root).
5. Stop after `k` results (see "Autocomplete / Prefix Suggestions").

#### 9. Edge Cases / Common Mistakes

1. Forgetting to **undo** the appended character, which corrupts every later word.
2. Skipping the check for a missing prefix and crashing on `null`.
3. Forgetting that the prefix itself may be a stored word (`car` above).
4. Relying on `HashMap` order when the result must be alphabetical.
5. Very deep Tries causing deep recursion. Words are rarely long enough to be a problem, but an iterative stack avoids it.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need **all** matches for a prefix, not just a yes/no.
2. You need counts or the longest word.

**Avoid when:**

1. You only need to know whether a prefix exists. `startsWith` is enough.
2. The prefix is very short and the subtree is huge. Cap the results (see "Autocomplete").

#### 11. Related Topics

1. Prefix Search / `startsWith`
2. Autocomplete / Prefix Suggestions
3. Counting Words / Prefixes
4. DFS (`01-data-structure/07-Tree`, `10-Graph`) and Recursion (`02-algorithm/03-Recursion & Divide and Conquer`)

#### 12. Interview Must Remember

1. Two steps: **walk the prefix, then DFS the subtree**.
2. Add a word when `isEndOfWord` is true, and **undo** the character after each child.
3. Cost is `O(P + S)`.
4. Sort the children if the output must be alphabetical.
