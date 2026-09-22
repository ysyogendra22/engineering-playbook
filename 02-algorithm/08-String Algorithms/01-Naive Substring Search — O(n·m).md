# Naive Substring Search — O(n·m)

#### 1. Definition — Must Know

**Naive substring search** checks every possible starting position in the text, and at each one, compares the pattern character by character, to find all places the pattern occurs.

#### 2. Why It Is Used — Must Know

1. It's simple, correct, and fast enough for most interview-sized inputs — the fancier algorithms (KMP, Rabin-Karp) only matter when the text or pattern is genuinely large, or the search happens repeatedly.
2. Knowing this baseline is what lets you say, honestly, "the simple approach is O(n·m); here's when I'd reach for something faster" — which is a stronger answer than jumping straight to KMP from memory.

#### 3. How It Works — Must Know

```text
Text:    "ABABDABACDABABCABAB"
Pattern: "ABABCABAB"

Try starting at index 0: "ABABD..." vs "ABABC..." → mismatch at position 4
Try starting at index 1: "BABDA..." vs "ABABC..." → mismatch at position 0
... continue trying every starting position ...
Try starting at index 10: "ABABCABAB" matches fully → found at index 10
```

At each starting position, comparison stops as soon as a mismatch is found — no need to check the rest of the pattern.

#### 4. Algorithm — Must Know

```text
for start in 0 to (n - m):          # every possible starting position
    matched = true
    for i in 0 to m - 1:             # compare the pattern, character by character
        if text[start + i] != pattern[i]:
            matched = false
            break
    if matched:
        record `start` as a match
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun naiveSearch(text: String, pattern: String): List<Int> {
    val matches = mutableListOf<Int>()
    val n = text.length
    val m = pattern.length
    for (start in 0..(n - m)) {
        var matched = true
        for (i in 0 until m) {
            if (text[start + i] != pattern[i]) {
                matched = false
                break
            }
        }
        if (matched) matches.add(start)
    }
    return matches
}
```

#### 6. Complexity — Must Know

| Case | Time |
|---|---|
| Best case | O(n) — mismatches found immediately at most positions |
| Worst case | O(n · m) — for example, text `"AAAAAAAAAB"`, pattern `"AAAAB"`, where each starting position almost fully matches before failing |
| Space | O(1) |

#### 7. Common Mistakes — Must Know

1. Getting the loop bound wrong (`n - m`, not `n`) — the pattern can't start at a position where it wouldn't fit in the remaining text.
2. Not breaking out of the inner comparison loop immediately on a mismatch — wastes time re-checking characters that already failed.
3. Reaching for KMP or Rabin-Karp (topics 4, 5) by default, when the naive approach is fine for the given input size — always check the constraints first (`03-leetcode-patterns/2`).

#### 8. Related Topics

1. `4` KMP (Knuth-Morris-Pratt) — the failure-function fix for the worst case above
2. `5` Rabin-Karp — Rolling Hash — the hash-based alternative
3. `2` Two Pointers, Sliding Window & Frequency Maps on Strings — related string techniques for other kinds of problems

#### 9. Interview Must Remember

1. Naive search is **O(n · m)** worst case, O(n) in most practical cases — know both numbers.
2. It's a perfectly fine default answer — only reach for KMP or Rabin-Karp when the input size or repeated-search pattern actually demands it.
3. Break early on a mismatch — it's a small but real optimisation, always include it.
