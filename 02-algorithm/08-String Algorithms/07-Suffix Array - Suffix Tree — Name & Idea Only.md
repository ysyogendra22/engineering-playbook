# Suffix Array / Suffix Tree — Name & Idea Only

#### 1. Definition — Must Know

1. A **suffix** of a string is everything from some starting position to the end (`"banana"` has suffixes `"banana"`, `"anana"`, `"nana"`, `"ana"`, `"na"`, `"a"`).
2. A **suffix array** is a sorted list of all of a string's suffixes (stored as starting indices, for efficiency). A **suffix tree** stores the same information as a compressed trie of all suffixes.
3. Both let you answer many substring questions on a large, fixed text very quickly, after a one-time build cost.

#### 2. Why It Is Used — Must Know

These are advanced tools for when the same large text needs to be searched **many times** with different patterns — a search engine indexing a document, or genome analysis. Full construction is well outside interview-implementation scope; knowing the name and what problem it solves is the goal.

#### 3. How It Works — Must Know

```text
String: "banana"

All suffixes:            Sorted (the suffix array, as indices):
0: banana                5: a
1: anana                 3: ana
2: nana                  1: anana
3: ana                   0: banana
4: na                    4: na
5: a                     2: nana

Suffix array = [5, 3, 1, 0, 4, 2]   (starting indices, in sorted suffix order)
```

Once built, a suffix array lets you **binary search** for any pattern inside the text in O(m log n) time — much faster than repeating a full O(n) search for every new pattern.

#### 4. Algorithm — Must Know

*(Name and idea only — construction algorithms are not expected to be reproduced from memory.)*

```text
Once you have a suffix array, searching for pattern P:
  binary search over the sorted suffixes, comparing P against each
  candidate suffix's prefix — similar to normal binary search, but
  comparing "does P come before/after this suffix?"
```

#### 5. Kotlin Implementation — Must Know

*(Not expected — this is an awareness-level topic, not an implementation one.)*

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Building a suffix array (naive) | O(n² log n) — sort n suffixes, each comparison up to O(n) |
| Building a suffix array (efficient methods) | O(n log n) |
| Searching once built | O(m log n) per pattern |

Compare with running naive search fresh each time: O(n · m) per pattern search — the suffix array wins decisively when the **same text** is searched **many times**.

#### 7. Common Mistakes — Must Know

1. Reaching for a suffix array/tree for a **one-off** search — the build cost isn't worth it unless the text is searched repeatedly.
2. Trying to build one from scratch in an interview — this is squarely an "I know the name and when I'd use it" topic, not an implement-live one.
3. Confusing "suffix" with "prefix" or "substring" — a suffix specifically starts somewhere and runs to the **end** of the string.

#### 8. Related Topics

1. `4` KMP, `5` Rabin-Karp, `6` Z-Algorithm — faster tools for a single search, without the upfront build cost
2. `DS Trie` — a related structure for storing many strings by shared prefix, rather than all suffixes of one string

#### 9. Interview Must Remember

1. Suffix array/tree = **precompute all suffixes of a large text once, to answer many future substring queries fast.**
2. Worth it only when the **same text** is queried **repeatedly** — not for a single search.
3. Name-and-idea level knowledge is the expectation here — say what it's for, and move on.
