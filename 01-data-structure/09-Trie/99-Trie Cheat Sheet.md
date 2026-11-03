# Trie Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–15.

#### 1. Key Takeaways

1. A trie stores words **character by character**. Words with the same beginning **share a path**.
2. `insert`, `search` and `startsWith` are all **`O(L)`** (the word length), independent of how many words are stored.
3. **`search` needs `isEnd`. `startsWith` does not.** This is the most common bug.
4. Children: **array of 26** for lowercase (fast), **`HashMap<Char, Node>`** for any alphabet (compact).
5. Tries shine for **prefix** questions. For exact lookup alone, a `HashSet` is enough.
6. **Trie + DFS** searches many words at once in a grid (Word Search II). The trie prunes dead paths.
7. Memory is the cost: up to one node per character, 26 slots each.

#### 2. Complexity Table

| Operation | Time | Notes |
|---|---|---|
| `insert(word)` | `O(L)` | creates up to `L` nodes |
| `search(word)` | `O(L)` | needs `isEnd` |
| `startsWith(prefix)` | `O(L)` | path must exist |
| `delete(word)` | `O(L)` | unmark, then prune unused nodes |
| Count words with prefix | `O(L)` | `pass` counter on nodes |
| List words with a prefix (K) | `O(L + K · len)` | DFS `a..z` for sorted output |
| Wildcard `.` search | up to `O(26^dots · L)` | DFS; bounded by the trie size |
| Maximum XOR (binary trie) | `O(32 · n)` | 2 children per node |
| Build for `n` words | `O(n · L)` time, `O(n · L)` nodes | |

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Note |
|---|---|---|
| "implement a trie", "prefix tree" | insert / search / startsWith | 07 |
| "starts with", "any word with this prefix" | walk the prefix, return `node != null` | 05 |
| "longest common prefix" | walk while exactly one child and not a word end | 05 |
| "replace with the shortest root" | stop at the first `isEnd` | 08 |
| "every prefix must also be a word" | descend only through word ends | 08 |
| "sum / count of values with a prefix" | running totals or counters on nodes | 08, 14 |
| "find all words in a grid" | trie + DFS + backtracking, store the word at the end node | 09 |
| "autocomplete", "top 3 suggestions" | walk the prefix, DFS `a..z` with a limit | 12 |
| "`.` matches any letter" | DFS, try all children at `.` | 13 |
| "exactly one letter different" | DFS with a `changed` flag | 13 |
| "remove a word" | unmark, prune unused nodes | 11 |
| "count words equal to / starting with" | `pass` and `end` counters | 14 |
| "maximum XOR of two numbers" | binary trie, take the opposite bit | 15 |

#### 4. Templates to Memorise

**Node and trie**

```kotlin
class TrieNode {
    val next = arrayOfNulls<TrieNode>(26)
    var isEnd = false
}

class Trie {
    private val root = TrieNode()

    fun insert(word: String) {
        var node = root
        for (c in word) {
            if (node.next[c - 'a'] == null) node.next[c - 'a'] = TrieNode()
            node = node.next[c - 'a']!!
        }
        node.isEnd = true
    }

    private fun find(s: String): TrieNode? {
        var node = root
        for (c in s) node = node.next[c - 'a'] ?: return null
        return node
    }

    fun search(word: String) = find(word)?.isEnd == true
    fun startsWith(prefix: String) = find(prefix) != null
}
```

**Any alphabet**

```kotlin
class Node { val next = HashMap<Char, Node>(); var isEnd = false }
// child: node.next.getOrPut(c) { Node() }       lookup: node.next[c] ?: return false
```

**Autocomplete DFS (alphabetical)**

```kotlin
fun dfs(cur: TrieNode) {
    if (result.size == limit) return
    if (cur.isEnd) result.add(path.toString())
    for (i in 0 until 26) {
        val child = cur.next[i] ?: continue
        path.append('a' + i); dfs(child); path.deleteCharAt(path.length - 1)
    }
}
```

**Wildcard search**

```kotlin
fun dfs(node: TrieNode, w: String, i: Int): Boolean {
    if (i == w.length) return node.isEnd
    if (w[i] == '.') return node.next.any { it != null && dfs(it, w, i + 1) }
    val child = node.next[w[i] - 'a'] ?: return false
    return dfs(child, w, i + 1)
}
```

**Trie + grid DFS (Word Search II)**

```kotlin
fun dfs(r: Int, c: Int, parent: TrieNode) {
    if (r !in 0 until rows || c !in 0 until cols) return
    val ch = board[r][c]; if (ch == '#') return
    val node = parent.next[ch - 'a'] ?: return          // prune
    node.word?.let { result.add(it); node.word = null }  // no duplicates
    board[r][c] = '#'
    dfs(r + 1, c, node); dfs(r - 1, c, node); dfs(r, c + 1, node); dfs(r, c - 1, node)
    board[r][c] = ch                                     // restore
}
```

**Counters**

```kotlin
// insert: node = child; node.pass++ ...  at the end: node.end++
fun countWordsStartingWith(p: String) = find(p)?.pass ?: 0
fun countWordsEqualTo(w: String) = find(w)?.end ?: 0
```

**Delete with pruning**

```kotlin
fun remove(node: TrieNode, depth: Int): Boolean {        // true = parent may drop this node
    if (depth == word.length) { node.isEnd = false; return !node.hasChildren() }
    val i = word[depth] - 'a'
    if (remove(node.next[i]!!, depth + 1)) node.next[i] = null
    return !node.isEnd && !node.hasChildren()
}
```

**Binary trie (max XOR)**

```kotlin
for (b in 30 downTo 0) {
    val bit = (x shr b) and 1; val want = 1 - bit
    if (node.next[want] != null) { cur = cur or (1 shl b); node = node.next[want]!! } else node = node.next[bit]!!
}
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Trie |
|---|---|---|
| Any word starting with `p`? | scan all words `O(n · L)` | walk `O(L)` |
| Count words with a prefix | scan `O(n · L)` | `pass` counter `O(L)` |
| Longest common prefix | compare all words | walk while one child |
| Words in a grid | Word Search I per word `O(W · m · n · 4^L)` | one trie + one DFS |
| Autocomplete | filter + sort per prefix | walk + limited DFS |
| Maximum XOR | all pairs `O(n²)` | binary trie `O(32 · n)` |
| Prefix scores | for each prefix scan all `O(n² · L²)` | `pass` counters `O(total chars)` |
| Wildcard search | compare with every word `O(n · L)` | DFS with pruning |

#### 6. Common Mistakes and Edge Cases

1. **`search` without `isEnd`** (returning true for a prefix).
2. **Overwriting an existing child** (`node.next[i] = TrieNode()` without a null check).
3. **Not setting `isEnd`** on the last node.
4. **Input outside `a..z`** crashing the array index (use a map).
5. **Eager creation** `Array(26) { TrieNode() }` (infinite recursion).
6. **Empty string:** decide what `search("")` and `startsWith("")` return, and say it.
7. **Delete:** removing nodes that other words need, or not unmarking a prefix word.
8. **Grid DFS:** not restoring the cell, duplicates in results, indexing with `'#'`.
9. **Wildcard:** treating `.` as a letter.
10. **Max XOR:** inserting from the lowest bit, or wrong bit count.
11. **Memory:** mention array nodes use 26 slots each.

#### 7. What to Say Out Loud

1. "A trie shares prefixes, so insert, search and prefix queries are all `O(L)`, independent of how many words are stored."
2. "`search` must check `isEnd`. A prefix is not a word."
3. "I'll use an array of 26 for lowercase letters. For other characters I'd use a hash map."
4. "For many words in a grid I'll build one trie and DFS once, pruning when the trie has no child for the letter."
5. "The cost is memory: one node per character, 26 slots each."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | walk while one child |
| Medium | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | the base |
| Medium | [Replace Words](https://leetcode.com/problems/replace-words/) | first `isEnd` |
| Medium | [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) | descend through word ends |
| Medium | [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | totals on nodes |
| Medium | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | wildcard DFS |
| Medium | [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/) | one change |
| Medium | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | autocomplete |
| Medium | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | binary trie |
| Medium | [Implement Trie II (Prefix Tree)](https://leetcode.com/problems/implement-trie-ii-prefix-tree/) | counters (premium) |
| Hard | [Word Search II](https://leetcode.com/problems/word-search-ii/) | trie + DFS |
| Hard | [Sum of Prefix Scores of Strings](https://leetcode.com/problems/sum-of-prefix-scores-of-strings/) | `pass` sums |
| Hard | [Concatenated Words](https://leetcode.com/problems/concatenated-words/) | trie + DFS on splits |
