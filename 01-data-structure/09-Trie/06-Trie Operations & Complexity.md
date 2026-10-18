# Trie Operations & Complexity

#### 1. Definition — Must Know

1. This topic collects the cost of every Trie operation in one place and compares a Trie with the other ways of storing words.
2. Notation used here:
   - `N` — number of stored words
   - `L` — length of the word being inserted or searched
   - `P` — length of the prefix being searched
   - `S` — total size of the part of the Trie you visit (for example, everything under a prefix)

#### 2. Why It Is Used — Must Know

1. Interviewers often ask "why a Trie and not a `HashSet`?" The answer is a complexity comparison.
2. Knowing the cost of each operation tells you when a Trie wins and when it does not.

#### 3. How It Works — Must Know

Every Trie operation is a walk down from the root. The cost is the number of characters on the walk, not the number of words stored.

```text
Stored words: 1,000,000
search("cat") still visits at most 3 nodes
```

#### 4. Core Concepts — Must Know

1. **Cost depends on word length**, not on the number of words.
2. **Space depends on the total characters stored**, reduced by shared prefixes.
3. **Nodes ≤ total characters + 1**, and often much fewer when words share beginnings.
4. Each node costs memory. A `HashMap` per node can make a Trie larger in practice than the plain character count suggests.

#### 5. Algorithm — Must Know

Nothing new to implement here. The operations are covered in their own topics:

```text
insert, search, startsWith  →  walk the characters
delete                      →  walk, unmark, then prune empty nodes
words with a prefix         →  walk the prefix, then DFS the subtree
```

#### 6. Kotlin Implementation — Must Know

Not needed for a complexity topic. See "Trie Implementation" for the full class.

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| Insert a word | `O(L)` |
| Search a word | `O(L)` |
| Prefix check (`startsWith`) | `O(P)` |
| Delete a word | `O(L)` |
| Collect all words under a prefix | `O(P + S)` |
| Count words with a prefix (with counts stored) | `O(P)` |
| Build a Trie from `N` words | `O(total characters)` |

| Space | Cost |
|---|---:|
| Worst case (no shared prefixes) | `O(total characters)` |
| `Array(26)` children | `26 slots` per node |
| `HashMap` children | only the children that exist, plus map overhead |

#### 8. Trie vs Other Structures — Must Know

| Structure | Exact search | Prefix check | List words with a prefix |
|---|---:|---:|---|
| Trie | `O(L)` | `O(P)` | `O(P + S)` |
| `HashSet<String>` | `O(L)` average | `O(N · P)` (check every word) | scan every word |
| Sorted list + binary search | `O(L log N)` | `O(P log N)` | find the start, then scan forward |

Use the table to explain the choice: a Trie wins when **prefix questions are common**. A `HashSet` wins when only exact lookup is needed.

#### 9. Edge Cases / Common Mistakes

1. Saying a Trie is `O(1)`. It is `O(L)`.
2. Forgetting that the space can be large when words share nothing.
3. Ignoring the memory overhead of a `HashMap` per node.
4. Claiming a Trie is faster than a `HashSet` for exact lookup. Both are about `O(L)`, and the set is lighter.

#### 10. When to Use / When Not to Use

**Use when:**

1. Prefix queries are frequent.
2. You need ordered or grouped results by prefix.

**Avoid when:**

1. Only exact lookup is needed.
2. Memory is tight and words are long with little overlap.

#### 11. Related Topics

1. Trie Fundamentals
2. TrieNode Structure
3. Trie Implementation
4. HashMap / HashSet (`01-data-structure/05-HashMap`, `06-HashSet`)

#### 12. Interview Must Remember

1. Insert, search, and prefix check are `O(L)` or `O(P)`. The number of words does not appear.
2. Space is `O(total characters)` in the worst case.
3. A Trie beats a `HashSet` for **prefix** queries, not for exact lookup.
4. Mention the memory overhead per node when asked for downsides.
