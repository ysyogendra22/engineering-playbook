# Decode String

#### 1. Definition — Must Know

1. Decode a string with the rule `k[encoded]`, meaning "repeat `encoded` exactly `k` times". Brackets can be **nested**.
2. Example: `"3[a2[c]]"` → `"accaccacc"`.
3. It is *Decode String* (LeetCode 394). If a number and a title ever disagree, trust the title.
4. The method: a stack remembers the **repeat count** and the **text built so far** each time a `[` opens.

#### 2. Why It Is Used — Must Know

1. It is a standard medium question about nested structure.
2. It shows how to "save the outside state when going inside, restore it when coming out".
3. The same idea parses nested JSON-like or markup text.

#### 3. How It Works — Must Know

`s = "3[a2[c]]"`

Keep: `current` (text of the current level), `k` (the number being read), a stack of counts, and a stack of previous texts.

```text
'3'   k = 3
'['   push count 3 and the current text "" ; reset current = "", k = 0
'a'   current = "a"
'2'   k = 2
'['   push count 2 and the current text "a" ; reset current = "", k = 0
'c'   current = "c"
']'   pop count 2, pop previous text "a" → current = "a" + "c" × 2 = "acc"
']'   pop count 3, pop previous text ""  → current = "" + "acc" × 3 = "accaccacc"

result: "accaccacc"
```

Idea in one line: **on `[` save the state; on `]` pop it and glue the repeated text onto the saved text.**

#### 4. Core Concepts — Must Know

1. **Read digits into `k`** (numbers can have several digits: `"12[a]"`).
2. **On `[`:** push `k` (the repeat count) and the current text; start a fresh current text.
3. **On `]`:** pop the count and the previous text; new current = previous + current × count.
4. **On a letter:** append it to the current text.
5. **Two stacks (or one stack of pairs):** one for counts, one for previous texts.
6. **`StringBuilder`** keeps appends cheap.
7. **Recursive alternative:** parse with a function that returns when it sees `]`.
8. **The answer is the final current text** after the loop.

| Character | Action |
|---|---|
| digit | `k = k * 10 + digit` |
| `[` | push `k` and `current`; reset both |
| `]` | pop count and previous; `current = previous + current × count` |
| letter | append to `current` |

#### 5. Algorithm — Must Know

```text
current = ""; k = 0; counts = []; texts = []
for each character c:
    digit  → k = k * 10 + c
    '['    → counts.push(k); texts.push(current); current = ""; k = 0
    ']'    → times = counts.pop(); previous = texts.pop(); current = previous + current × times
    letter → current += c
return current
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun decodeString(s: String): String {
    val counts = ArrayDeque<Int>()
    val previous = ArrayDeque<StringBuilder>()
    var current = StringBuilder()
    var k = 0

    for (c in s) {
        when {
            c.isDigit() -> k = k * 10 + (c - '0')
            c == '[' -> {
                counts.addLast(k)
                previous.addLast(current)
                current = StringBuilder()
                k = 0
            }
            c == ']' -> {
                val times = counts.removeLast()
                val outer = previous.removeLast()
                repeat(times) { outer.append(current) }
                current = outer
            }
            else -> current.append(c)
        }
    }
    return current.toString()
}

// Recursive version (clear, but uses the call stack)
fun decodeStringRecursive(s: String): String {
    var i = 0
    fun parse(): String {
        val sb = StringBuilder()
        var k = 0
        while (i < s.length) {
            val c = s[i]
            when {
                c.isDigit() -> { k = k * 10 + (c - '0'); i++ }
                c == '[' -> {
                    i++                                   // skip '['
                    val inner = parse()
                    repeat(k) { sb.append(inner) }
                    k = 0
                }
                c == ']' -> { i++; return sb.toString() }  // skip ']' and finish this level
                else -> { sb.append(c); i++ }
            }
        }
        return sb.toString()
    }
    return parse()
}
```

Checks: `decodeString("3[a]2[bc]")` → `"aaabcbc"`. `decodeString("3[a2[c]]")` → `"accaccacc"`. `decodeString("2[abc]3[cd]ef")` → `"abcabccdcdcdef"`. `decodeString("10[a]")` → `"aaaaaaaaaa"`.

#### 7. Time & Space Complexity — Must Know

Let `L` be the length of the decoded output.

| Part | Cost |
|---|---:|
| Time | `O(L)` — every output character is written once (plus `O(n)` for input) |
| Space | `O(L)` for the result; the stacks hold at most the nesting depth |

The output can be much longer than the input (`"100[100[a]]"` is 10,000 characters).

#### 8. Common Nested-Structure Patterns — Must Know

1. **Decode String** (LeetCode 394).
2. **Number of Atoms** (LeetCode 726) — formulas like `K4(ON(SO3)2)2`; a stack of maps.
3. **Basic Calculator** with brackets (LeetCode 224).
4. **Reverse Substrings Between Each Pair of Parentheses** (LeetCode 1190).
5. **Mini Parser** (LeetCode 385) — nested lists.
6. **Brace Expansion** (LeetCode 1087).
7. **Android example:** parsing a small markup or template language with nested tags.

#### 9. Edge Cases / Common Mistakes

1. Treating a number as a single digit (`"12[a]"` is 12 repeats).
2. Not resetting `k = 0` after `[` (the old number leaks into the next group).
3. Not creating a **new** `current` after `[` (mixing the outer and inner text).
4. On `]`: appending the inner text to the wrong builder, or using the same object for `outer` and `current`.
5. Letters after a closing bracket (`"2[a]bc"`): they must be appended to the outer text.
6. Empty brackets (`"3[]"`) → empty string.
7. Very large repeat counts create huge outputs. The problem limits them.
8. Pushing `k` as a character instead of an `Int`.

#### 10. When to Use / When Not to Use

**Use the stack when:**

1. Nested groups must be expanded or combined, and you want to avoid recursion.

**Use recursion when:**

1. Depth is small and the grammar is clear. It is shorter to read.

#### 11. Related Topics

1. Valid / Balanced Parentheses
2. Expression / String Processing with Stack
3. Stack-Based DFS (stack instead of recursion)
4. Recursion (`02-algorithm/03-Recursion & Divide and Conquer`)

#### 12. Interview Must Remember

1. **On `[`: push count and current text. On `]`: pop and repeat.**
2. Digits build `k` (multi-digit). Reset `k` and `current` after `[`.
3. Two stacks (counts and texts), or recursion.
4. `O(output length)` time and space.
