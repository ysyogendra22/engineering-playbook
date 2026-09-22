# KMP (Knuth-Morris-Pratt) — the Failure Function, O(n + m)

#### 1. Definition — Must Know

**KMP** finds all occurrences of a pattern inside a text in **O(n + m)** time, by pre-computing a **failure function** (also called the "partial match table" or "LPS array" — longest proper prefix that is also a suffix) for the pattern, so that on a mismatch, it never re-checks characters it has already matched.

#### 2. Why It Is Used — Must Know

1. It fixes naive search's (topic 1) worst case — no more O(n · m) blow-up on repetitive patterns like `"AAAAB"`.
2. It's a name worth recognising and being able to describe, even if reproducing the failure-function construction exactly from memory is a stretch goal, not a baseline expectation.

#### 3. How It Works — Must Know

The failure function for pattern `"ABABC"`:

```text
Pattern:  A  B  A  B  C
Index:    0  1  2  3  4
LPS:      0  0  1  2  0

LPS[i] = the length of the longest proper prefix of pattern[0..i] that is
         also a suffix of pattern[0..i].

At i=2 ("ABA"): prefix "A" equals suffix "A" → LPS[2] = 1
At i=3 ("ABAB"): prefix "AB" equals suffix "AB" → LPS[3] = 2
```

When matching against the text and a mismatch happens partway through, KMP uses the LPS array to know **how far it can safely skip ahead** without re-comparing characters it has already confirmed match — because the LPS array already tells it what part of the pattern would match again.

```text
Text:    "ABABABC"
Pattern: "ABABC"

Match A,B,A,B... then mismatch comparing C vs A (text has A, not C, at that spot)
Naive search would restart the whole pattern from the next position (index 1).
KMP uses LPS[3] = 2 to know "AB" is already confirmed matching — skip
straight to comparing from there, instead of re-checking A and B again.
```

#### 4. Algorithm — Must Know

```text
Build the LPS array for the pattern:
  lps[0] = 0
  length = 0   # length of the current matching prefix
  i = 1
  while i < pattern.length:
      if pattern[i] == pattern[length]:
          length++
          lps[i] = length
          i++
      elif length > 0:
          length = lps[length - 1]     # fall back, don't advance i
      else:
          lps[i] = 0
          i++

Search using the LPS array:
  i = 0 (text index), j = 0 (pattern index)
  while i < text.length:
      if text[i] == pattern[j]: i++; j++
      if j == pattern.length: record match at (i - j); j = lps[j - 1]
      elif i < text.length and text[i] != pattern[j]:
          if j > 0: j = lps[j - 1]     # use the failure function, don't restart from 0
          else: i++
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun buildLPS(pattern: String): IntArray {
    val lps = IntArray(pattern.length)
    var length = 0
    var i = 1
    while (i < pattern.length) {
        if (pattern[i] == pattern[length]) {
            length++; lps[i] = length; i++
        } else if (length > 0) {
            length = lps[length - 1]
        } else {
            lps[i] = 0; i++
        }
    }
    return lps
}
// Full search loop follows the LPS array as shown in section 4 —
// knowing the LPS array's purpose and construction is the key part to know.
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Building the LPS array | O(m) |
| Searching | O(n) |
| Total | O(n + m) — always, no bad worst case like naive search |

#### 7. Common Mistakes — Must Know

1. Confusing the LPS array's purpose — it's about the **pattern matching itself** (prefix = suffix), not about matching against the text.
2. On a mismatch, restarting `j` at 0 instead of `lps[j - 1]` — this loses the whole benefit of KMP and degrades back toward naive search behaviour.
3. Spending too long trying to derive the LPS construction from scratch in an interview — describing what it does and why is usually enough; full derivation is a stretch, not a baseline expectation (see the mark on this topic).

#### 8. Related Topics

1. `1` Naive Substring Search — O(n·m) — the problem KMP fixes
2. `5` Rabin-Karp — Rolling Hash — an alternative fast approach
3. `6` Z-Algorithm — Longest Common Prefix with Itself — a related technique with a similar goal

#### 9. Interview Must Remember

1. KMP = **precompute a failure function (LPS array) so mismatches never re-check already-matched characters.**
2. O(n + m) — always, no bad worst case, unlike naive search's O(n · m).
3. It's fine to describe the idea and what the LPS array represents without reproducing the exact construction code from memory.
