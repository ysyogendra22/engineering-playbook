# Expression / String Processing with Stack

#### 1. Definition — Must Know

1. Many string problems are solved by walking through the characters and using a stack to **remember what is still open or pending**.
2. Typical jobs: **evaluate** an expression, **undo** characters (backspace), **remove** characters to get the smallest number, **reverse** parts of a string.
3. The stack holds partial results, operators, or the characters kept so far.

#### 2. Why It Is Used — Must Know

1. Expressions have priority rules (`*` before `+`) and nesting (brackets). A stack handles both.
2. "Delete the last kept character" is exactly a `pop`.
3. These problems appear very often as medium-level interview questions.

#### 3. How It Works — Must Know

**Basic Calculator II** (LeetCode 227): evaluate `"3+2*2"` with `+ - * /` and no brackets.

Idea: keep a stack of numbers to add up at the end.
`+` and `-` push the number (negated for `-`). `*` and `/` pop the last number, combine it with the new number, and push the result. So multiplication and division are done immediately, and addition is delayed.

```text
"3+2*2"

read 3, operator '+' pending ...
see '+':  previous operator was '+' → push 3             stack [3]
read 2
see '*':  previous operator was '+' → push 2             stack [3, 2]
read 2 (end of string): previous operator was '*' → pop 2, push 2*2=4    stack [3, 4]

sum of stack = 3 + 4 = 7
```

**Remove K Digits** (LeetCode 402): remove `k` digits to make the smallest number. Use an increasing stack: when a new digit is **smaller** than the top, the top digit should go (while `k > 0`).

```text
num = "1432219", k = 3
1 → push                   1
4 → push                   14
3 → 4 > 3, remove 4 (k=2), push 3     13
2 → 3 > 2, remove 3 (k=1), push 2     12
2 → push                   122
1 → 2 > 1, remove 2 (k=0), push 1     121
9 → push                   1219
result "1219"
```

**Backspace String Compare** (LeetCode 844): `#` means "delete the previous character". Build each string with a stack; a `#` pops.

#### 4. Core Concepts — Must Know

1. **Choose what the stack holds:** numbers (calculator), characters (backspace, remove digits), partial strings (decode), indexes (positions).
2. **Delay low-priority work.** Push `+`/`-` results, and combine `*`/`/` at once.
3. **Pop to undo.** A backspace or a "smaller digit arrives" pops the last kept item.
4. **Use `StringBuilder` as the stack of characters.** `append`, `deleteCharAt(length - 1)`, and `last()` do the job without extra objects.
5. **Handle the last token.** Many parsers forget the final number because no operator follows it.
6. **Brackets in calculators:** push the current result and sign on `(`, restore on `)` (Basic Calculator, LeetCode 224).
7. **Spaces and multi-digit numbers** need extra handling (`num = num * 10 + digit`).

| Task | Stack holds | Pop when |
|---|---|---|
| Calculator II | numbers | `*` or `/` arrives |
| Calculator with brackets | numbers and signs | `)` arrives |
| Remove K Digits | digits (increasing) | new digit is smaller and `k > 0` |
| Backspace Compare | characters | `#` arrives |
| Reverse Words / Substrings | characters | reversing at `)` |

#### 5. Algorithm — Must Know

```text
Calculator II:
stack = []; num = 0; op = '+'
for each character c (and at the end of the string):
    if c is a digit: num = num * 10 + c
    if c is an operator (or the last character):
        '+' → push num;  '-' → push -num;  '*' → push(pop() * num);  '/' → push(pop() / num)
        op = c;  num = 0
answer = sum of the stack
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Basic Calculator II — non-negative integers, + - * /, spaces allowed
fun calculate(s: String): Int {
    val stack = ArrayDeque<Int>()
    var num = 0
    var op = '+'
    for (i in s.indices) {
        val c = s[i]
        if (c.isDigit()) num = num * 10 + (c - '0')
        if ((!c.isDigit() && c != ' ') || i == s.length - 1) {
            when (op) {
                '+' -> stack.addLast(num)
                '-' -> stack.addLast(-num)
                '*' -> stack.addLast(stack.removeLast() * num)
                '/' -> stack.addLast(stack.removeLast() / num)     // truncates toward zero
            }
            op = c
            num = 0
        }
    }
    return stack.sum()
}

// Remove K Digits — smallest possible number
fun removeKdigits(num: String, k: Int): String {
    var remaining = k
    val sb = StringBuilder()                                 // used as a stack
    for (c in num) {
        while (remaining > 0 && sb.isNotEmpty() && sb.last() > c) {
            sb.deleteCharAt(sb.length - 1)
            remaining--
        }
        sb.append(c)
    }
    while (remaining > 0 && sb.isNotEmpty()) {               // still need to remove: drop from the end
        sb.deleteCharAt(sb.length - 1)
        remaining--
    }
    val result = sb.toString().trimStart('0')
    return if (result.isEmpty()) "0" else result
}

// Backspace String Compare
fun backspaceCompare(s: String, t: String): Boolean {
    fun build(text: String): String {
        val sb = StringBuilder()
        for (c in text) {
            if (c == '#') { if (sb.isNotEmpty()) sb.deleteCharAt(sb.length - 1) }
            else sb.append(c)
        }
        return sb.toString()
    }
    return build(s) == build(t)
}

// Reverse the words of a sentence with a stack
fun reverseWords(s: String): String {
    val stack = ArrayDeque<String>()
    for (word in s.trim().split(Regex("\\s+"))) stack.addLast(word)
    val parts = mutableListOf<String>()
    while (stack.isNotEmpty()) parts.add(stack.removeLast())
    return parts.joinToString(" ")
}
```

Checks: `calculate("3+2*2")` → `7`. `calculate(" 3/2 ")` → `1`. `calculate(" 3+5 / 2 ")` → `5`. `removeKdigits("1432219", 3)` → `"1219"`. `removeKdigits("10200", 1)` → `"200"`. `removeKdigits("10", 2)` → `"0"`. `backspaceCompare("ab#c", "ad#c")` → `true`.

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| Basic Calculator II | `O(n)` | `O(n)` (can be `O(1)` with a running last term) |
| Remove K Digits | `O(n)` | `O(n)` |
| Backspace Compare | `O(n)` | `O(n)` (two-pointer from the end gives `O(1)`) |
| Reverse words | `O(n)` | `O(n)` |

#### 8. Common Expression / String Patterns — Must Know

1. **Basic Calculator II** (LeetCode 227), **Basic Calculator** (LeetCode 224) with brackets.
2. **Remove K Digits** (LeetCode 402).
3. **Backspace String Compare** (LeetCode 844).
4. **Evaluate Reverse Polish Notation** (LeetCode 150) — next notes.
5. **Reverse Substrings Between Each Pair of Parentheses** (LeetCode 1190).
6. **Remove Duplicate Letters / Smallest Subsequence** (LeetCode 316, 1081).
7. **Decode String** and **Simplify Path** — next notes.
8. **Android example:** parsing a formula typed into a calculator widget.

#### 9. Edge Cases / Common Mistakes

1. Forgetting to process the **last number** (no operator follows it).
2. Treating spaces as operators.
3. Multi-digit numbers: `num = num * 10 + digit`, not `num = digit`.
4. Division and negative numbers: Kotlin `/` truncates toward zero, which matches most problem statements.
5. Updating `op = c` before using the previous operator.
6. Remove K Digits: leading zeros (`"10200"` → `"200"`), result becoming empty (return `"0"`), `k` larger than needed.
7. Backspace on an empty stack. Check `isNotEmpty()`.
8. Overflow in the calculator. Use `Long` if the problem says numbers can be large.

#### 10. When to Use / When Not to Use

**Use when:**

1. The result depends on the most recent kept item, or on operator priority.

**Avoid when:**

1. A single pass with a few variables is enough (single bracket type counter, running last term for the calculator).

#### 11. Related Topics

1. Valid / Balanced Parentheses
2. Evaluate Postfix / Reverse Polish Notation
3. Decode String
4. Expression Parsing (study separately)

#### 12. Interview Must Remember

1. **Stack of numbers: push `+`/`-` terms, combine `*`/`/` immediately, sum at the end.**
2. **Pop to undo:** backspace, smaller digit arrives, mismatch.
3. Handle the last token and multi-digit numbers.
4. `StringBuilder` works as a character stack.
