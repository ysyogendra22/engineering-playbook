# Rabin-Karp — Rolling Hash, O(n + m) Average

#### 1. Definition — Must Know

**Rabin-Karp** finds pattern matches by comparing **hash values** instead of comparing characters directly: hash the pattern once, then slide a window across the text, updating its hash in O(1) per step (a **rolling hash**), and only doing a full character comparison when the hashes match.

#### 2. Why It Is Used — Must Know

1. It's naturally suited to searching for **multiple patterns at once** — hash all patterns once, then check the text's rolling hash against the whole set.
2. The "rolling hash" idea itself (updating a hash in O(1) as a window slides, rather than recomputing it from scratch) reappears in other sliding-window problems too, not just string search.

#### 3. How It Works — Must Know

```text
Treat each character as a digit in a large base (e.g. base 256), and
compute the hash as a "number" in that base, modulo a large prime
(to keep the numbers manageable).

Text:    "ABCABCD"     Pattern: "ABC"   (window size 3)

hash("ABC") = A*base² + B*base¹ + C*base⁰    (mod some large prime)

Rolling from window "ABC" to the next window "BCA":
newHash = (oldHash - A*base²) * base + newChar     (mod prime)
        = subtract the character leaving the window, shift, add the
          character entering the window — O(1), no need to rehash
          all 3 characters from scratch.

If newHash == hash(pattern):
    do a full character-by-character check to confirm (hashes CAN collide)
```

#### 4. Algorithm — Must Know

```text
patternHash = hash(pattern)
windowHash = hash(text[0 until m])
for start in 0..(n - m):
    if windowHash == patternHash:
        if text[start until start+m] == pattern:   # confirm — avoid false positives
            record match at `start`
    if start < n - m:
        windowHash = roll the hash forward by one character   # O(1)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun rabinKarp(text: String, pattern: String): List<Int> {
    val n = text.length; val m = pattern.length
    if (m > n) return emptyList()
    val base = 256L; val mod = 1_000_000_007L
    var patternHash = 0L; var windowHash = 0L; var highestPower = 1L
    for (i in 0 until m - 1) highestPower = (highestPower * base) % mod

    for (i in 0 until m) {
        patternHash = (patternHash * base + pattern[i].code) % mod
        windowHash = (windowHash * base + text[i].code) % mod
    }

    val matches = mutableListOf<Int>()
    for (start in 0..(n - m)) {
        if (windowHash == patternHash && text.substring(start, start + m) == pattern) {
            matches.add(start)   // confirmed, not just a hash collision
        }
        if (start < n - m) {
            windowHash = ((windowHash - text[start].code * highestPower % mod + mod) % mod
                    * base + text[start + m].code) % mod
        }
    }
    return matches
}
```

#### 6. Complexity — Must Know

| | Time | Notes |
|---|---|---|
| Average case | O(n + m) | Hash comparisons are O(1); the rolling update is O(1) |
| Worst case | O(n · m) | Only if there are many hash collisions requiring full re-checks — rare with a good hash function and large prime modulus |
| Space | O(1) beyond the input | Just a few running hash values |

#### 7. Common Mistakes — Must Know

1. **Skipping the full-string confirmation check** after a hash match — hashes can collide (two different strings hashing to the same value), so a hash match alone is not proof of a real match.
2. Using a modulus that's too small, causing frequent collisions and degrading toward the worst case.
3. Getting the rolling-hash update formula wrong (forgetting to remove the old leading character's contribution before adding the new trailing one).

#### 8. Related Topics

1. `1` Naive Substring Search — O(n·m) — the baseline this improves on
2. `4` KMP (Knuth-Morris-Pratt) — the other O(n+m)-average approach, without hashing
3. `06-Embeddings & Vector Search` (in `08-artificial-intelligence`) — a very different, unrelated use of "hashing for comparison", worth not confusing with this

#### 9. Interview Must Remember

1. Rabin-Karp = **rolling hash, compare hashes first, confirm with a real character check only when hashes match.**
2. Always confirm a hash match with an actual string comparison — never trust the hash alone.
3. Good for searching for **many patterns at once** against the same text — a distinct advantage over KMP.
