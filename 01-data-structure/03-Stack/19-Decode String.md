# Decode String

#### 1. What Is It?

A string uses the rule `k[text]`, which means "write `text` exactly `k` times". Brackets can be **nested**. Decode it.

```text
"3[a]2[bc]"    → "aaabcbc"
"3[a2[c]]"     → "accaccacc"
"2[abc]3[cd]ef" → "abcabccdcdcdef"
```

This is *Decode String* (LeetCode 394). The nested part is the key: you must finish the **inner** group before the **outer** one. That is last-opened, first-closed, so it is a stack.

#### 2. How It Works

Keep these things:

- `current`: the text of the group you are inside right now,
- `k`: the number you just read,
- a stack of **counts** and a stack of **earlier texts**.

Rules:

| You read | Do this |
|---|---|
| a digit | `k = k * 10 + digit` (numbers can have many digits) |
| `[` | save `k` and `current` on the stacks. Start a new empty `current`, set `k = 0`. |
| `]` | take the saved count and earlier text. New `current` = earlier text + `current` repeated count times. |
| a letter | add it to `current` |

`s = "3[a2[c]]"`

```text
'3'   k = 3
'['   save count 3 and text ""      current = "", k = 0
'a'   current = "a"
'2'   k = 2
'['   save count 2 and text "a"    current = "", k = 0
'c'   current = "c"
']'   count 2, earlier text "a"    current = "a" + "c" × 2 = "acc"
']'   count 3, earlier text ""     current = "" + "acc" × 3 = "accaccacc"

result: "accaccacc"
```

#### 3. Kotlin Code

```kotlin
fun decodeString(s: String): String {
    val counts = ArrayDeque<Int>()
    val earlier = ArrayDeque<StringBuilder>()
    var current = StringBuilder()
    var k = 0

    for (c in s) {
        when {
            c.isDigit() -> k = k * 10 + (c - '0')
            c == '[' -> {
                counts.addLast(k)
                earlier.addLast(current)
                current = StringBuilder()
                k = 0
            }
            c == ']' -> {
                val times = counts.removeLast()
                val outer = earlier.removeLast()
                repeat(times) { outer.append(current) }
                current = outer
            }
            else -> current.append(c)
        }
    }
    return current.toString()
}
```

Checks: `decodeString("3[a]2[bc]")` → `"aaabcbc"`. `decodeString("3[a2[c]]")` → `"accaccacc"`. `decodeString("2[abc]3[cd]ef")` → `"abcabccdcdcdef"`. `decodeString("10[a]")` → `"aaaaaaaaaa"`.

**Recursive version** (shorter to read, and often accepted):

```kotlin
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
                    i++                                    // skip '['
                    val inner = parse()
                    repeat(k) { sb.append(inner) }
                    k = 0
                }
                c == ']' -> { i++; return sb.toString() }  // this group is finished
                else -> { sb.append(c); i++ }
            }
        }
        return sb.toString()
    }
    return parse()
}
```

#### 4. Complexity

Let `L` be the length of the **decoded** result.

| | Time | Space |
|---|---|---|
| Stack version | `O(L)` | `O(L)` |

The output can be much longer than the input, for example `"100[100[a]]"` gives 10,000 characters.

#### 5. Common Mistakes

1. **Reading only one digit.** `"12[a]"` is 12 repeats. Use `k = k * 10 + digit`.
2. **Not resetting `k = 0`** after `[`. The old number leaks into the next group.
3. **Not starting a new `current`** after `[`. Outer and inner text get mixed.
4. **Letters after a `]`** (like `ef` in `"2[abc]3[cd]ef"`). They must be added to the outer text. The code does this because `current = outer` after `]`.
5. **Pushing `k` as a character** instead of an `Int`.

#### 6. Say This in the Interview

1. "Brackets are nested, so I use a stack. On `[` I save the count and the text so far. On `]` I restore them and repeat the inner text."
2. "Digits build `k`, so multi-digit counts work."
3. "Time and space are `O(L)`, where `L` is the length of the decoded string."

#### 7. Quick Check

1. Decode `"2[a2[b]]"`.
2. What happens to `k` after you read `[`?

<details>
<summary>Answers</summary>

1. Inner `2[b]` = `bb`. Then `a` + `bb` = `abb`. Repeated twice: `"abbabb"`.
2. It is saved on the stack and then reset to `0`, ready for the next number.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 394 | Decode String (Medium) | this note |
| 726 | Number of Atoms (Hard) | the same idea with a stack of maps |
| 224 | Basic Calculator (Hard) | save and restore at brackets |
| 1190 | Reverse Substrings Between Each Pair of Parentheses (Medium) | stack of partial strings |
| 385 | Mini Parser (Medium) | nested lists |
