# Z-Algorithm — Longest Common Prefix with Itself

#### 1. Definition — Must Know

The **Z-algorithm** builds an array `Z`, where `Z[i]` is the length of the longest substring starting at position `i` that matches a prefix of the string itself. It runs in O(n), and is another way (alongside KMP) to solve pattern matching and related string problems in linear time.

#### 2. Why It Is Used — Must Know

It's a clean, general-purpose tool: once you have the Z-array, you can answer several different string questions from it (substring search, finding repeated patterns, checking string periods) — it's worth recognising as a named alternative to KMP, even if you reach for KMP first in practice.

#### 3. How It Works — Must Know

```text
String: "aabxaabxcaabxaabxay"
Index:   0123456789...

Z[0] is undefined/ignored by convention (comparing the whole string to itself is trivial)
Z[1] = 1   ("a" matches the prefix "a", but "ab..." doesn't match "aa...")
Z[4] = 4   ("aabx" starting at index 4 matches the prefix "aabx" exactly)
Z[9] = 4   ("aabx" starting at index 9 also matches the prefix "aabx")

To search for pattern P inside text T:
  build Z-array for the combined string:  P + "#" + T   (# is a separator
  that doesn't appear in either string)
  wherever Z[i] == length(P), a match of P starts at that position in T
```

#### 4. Algorithm — Must Know

```text
Z[0] = 0 (by convention, unused)
left = 0, right = 0    # the rightmost window known to match a prefix so far
for i in 1 to n-1:
    if i < right:
        Z[i] = min(right - i, Z[i - left])   # reuse previously computed info
    while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
        Z[i]++
    if i + Z[i] > right:
        left = i; right = i + Z[i]
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun zArray(s: String): IntArray {
    val n = s.length
    val z = IntArray(n)
    var left = 0; var right = 0
    for (i in 1 until n) {
        if (i < right) {
            z[i] = minOf(right - i, z[i - left])
        }
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++
        }
        if (i + z[i] > right) {
            left = i; right = i + z[i]
        }
    }
    return z
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Time | O(n) |
| Space | O(n) — the Z-array itself |

#### 7. Common Mistakes — Must Know

1. Forgetting the separator character (`#`) when combining pattern and text for a search — without it, the Z-array can be thrown off if the pattern and text share overlapping content across the boundary.
2. Using a separator character that could actually appear in the input — it must be guaranteed not to occur in either string.
3. Trying to memorise this over KMP without a reason — for most interviews, KMP (topic 4) is the more commonly expected name; the Z-algorithm is a good "I also know an alternative" answer, not usually the first-choice tool.

#### 8. Related Topics

1. `4` KMP (Knuth-Morris-Pratt) — the more commonly expected alternative for the same class of problems
2. `1` Naive Substring Search — O(n·m) — the baseline both of these improve on

#### 9. Interview Must Remember

1. Z-array: `Z[i]` = length of the longest prefix of the string that also starts at position `i`.
2. Combine pattern + separator + text to turn it into a search tool, checking for `Z[i] == pattern length`.
3. O(n) time and space — a solid alternative to KMP, worth naming even if KMP is your default answer.
