# Autocomplete / Prefix Suggestions

#### 1. Definition — Must Know

1. **Autocomplete** suggests complete words while the user is still typing a prefix.
2. With a Trie: walk to the prefix node, then collect words below it, but only a **limited number** (`k`) and usually in a useful order.
3. It builds directly on "Trie + DFS", adding a limit and an order.

#### 2. Why It Is Used — Must Know

1. It is the best-known use of a Trie: search boxes, keyboards, address fields, command palettes.
2. It must answer fast, on every keystroke.
3. It is a common interview question, and a good place to show mobile awareness.

#### 3. How It Works — Must Know

Words stored: `car`, `card`, `care`, `cat`, `cart`. User types `ca`, limit `3`:

```text
1. Walk "ca" to its node.
2. DFS in alphabetical order, adding words:
   car  → card → care     (stop: 3 suggestions found)
3. Return ["car", "card", "care"]
```

Each new keystroke can continue from the node already reached, instead of walking the whole prefix again.

#### 4. Core Concepts — Must Know

1. **Prefix node** — where the suggestions start.
2. **Limit `k`** — stop collecting after `k` words. It keeps the response small and fast.
3. **Order** — alphabetical (sort children) or by popularity (store a frequency at each end node).
4. **Early exit** — once `k` results exist, stop the DFS.

#### 5. Algorithm — Must Know

```text
suggestions(prefix, k):
    start = findNode(prefix)
    if start is null: return empty list
    DFS from start in alphabetical order,
    adding each end-of-word until k results exist, then stop
```

By popularity: collect candidates, sort by frequency (highest first), take `k`.

#### 6. Kotlin Implementation — Must Know

Alphabetical, with early exit:

```kotlin
// Methods inside the Trie class from "Trie Implementation"

fun suggestions(prefix: String, limit: Int): List<String> {
    val start = findNode(prefix) ?: return emptyList()
    val results = mutableListOf<String>()
    collectLimited(start, StringBuilder(prefix), limit, results)
    return results
}

private fun collectLimited(
    node: TrieNode,
    path: StringBuilder,
    limit: Int,
    results: MutableList<String>
) {
    if (results.size >= limit) return
    if (node.isEndOfWord) results.add(path.toString())
    for (ch in node.children.keys.sorted()) {
        if (results.size >= limit) return
        path.append(ch)
        collectLimited(node.children.getValue(ch), path, limit, results)
        path.deleteCharAt(path.length - 1)
    }
}
```

By popularity: add `var frequency = 0` to `TrieNode`, do `node.frequency++` on the end node in `insert`, then:

```kotlin
// candidates = list of Pair(word, frequency) gathered with the DFS above (without the limit)
val top = candidates
    .sortedWith(compareByDescending<Pair<String, Int>> { it.second }.thenBy { it.first })
    .take(limit)
    .map { it.first }
```

#### 7. Time & Space Complexity — Must Know

| Step | Time |
|---|---:|
| Walk the prefix | `O(P)` |
| Alphabetical, early exit | about `O(P + k · L)` |
| By popularity (collect all, then sort) | `O(P + S + C log C)`, where `C` = candidates under the prefix |
| Space | `O(L + k)` |

For very large Tries, ranking by popularity is usually precomputed (each node stores its own top-`k` list), trading memory for speed.

#### 8. Common Autocomplete Patterns — Must Know

1. **Search Suggestions System** (LeetCode 1268) — up to 3 suggestions after each typed character.
2. **Design Search Autocomplete System** (LeetCode 642, premium) — suggestions ranked by how often sentences were typed.
3. On a phone, debounce typing before querying (`06-mobile-engineering/3`, `debounce`) so a lookup does not run on every key press.
4. A small local dictionary can live in an on-device Trie. A very large one lives on the server.

#### 9. Edge Cases / Common Mistakes

1. No limit on results, returning thousands of words for a one-letter prefix.
2. Not stopping the DFS once `k` results are found.
3. Relying on `HashMap` order. Sort the keys, or the suggestions change between runs.
4. Rebuilding the Trie on every keystroke instead of keeping it.
5. Case differences: normalise the prefix and the stored words the same way.
6. Ignoring that the typed prefix may itself be a word and should be suggested.

#### 10. When to Use / When Not to Use

**Use when:**

1. Suggestions are driven by a typed prefix.
2. The dictionary is reasonably static, or updated in controlled ways.

**Avoid when:**

1. Matching should be fuzzy (typos). A Trie matches exact prefixes only.
2. Matching is on the middle of words. Use a search engine or an inverted index.
3. The data is huge and ranking is complex. See "Production Autocomplete Design" in the low-priority list.

#### 11. Related Topics

1. Prefix Search / `startsWith`
2. Trie + DFS
3. Counting Words / Prefixes
4. Debounce and `Flow` (`06-mobile-engineering/3`)
5. Top K Elements (`03-leetcode-patterns`)

#### 12. Interview Must Remember

1. **Walk the prefix, then collect up to `k` words.** Stop early.
2. Order by alphabet (sort children) or by popularity (store frequency).
3. Keep the Trie and continue from the last node as the user types.
4. Mobile: debounce the query and keep small dictionaries on the device.
