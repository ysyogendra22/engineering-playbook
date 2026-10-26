# Expression / String Processing with Stack

#### 1. What Is It?

Many string questions are solved by reading the characters one by one and using a stack to **remember what is still pending** or **what you kept so far**.

Four classic jobs:

| Job | Stack holds | Question |
|---|---|---|
| Calculator with `+ - * /` | numbers | Basic Calculator II |
| Calculator with brackets | results and signs | Basic Calculator |
| Make the smallest number | kept digits | Remove K Digits |
| Undo characters | kept characters | Backspace String Compare |

#### 2. How It Works

**Basic Calculator II** (`+ - * /`, no brackets): `"3+2*2"`.

Idea: `*` and `/` must be done **first**. `+` and `-` can wait. So:

- `+` → push the number. `-` → push the negative number.
- `*` or `/` → pop the last number, combine it with the new number, push the result.
- At the end, **add up** everything in the stack.

```text
"3+2*2"

3        number 3 is read, operator before it was "+"  → push 3        stack [3]
2        operator before it was "+"                     → push 2        stack [3, 2]
2        operator before it was "*"                     → pop 2, push 2*2 = 4   stack [3, 4]

sum of the stack = 3 + 4 = 7
```

**Remove K Digits**: remove `k` digits to make the smallest number. When a new digit is **smaller** than the top, the top digit should go (while you still may remove).

```text
num = "1432219", k = 3
1 → push                          1
4 → push                          14
3 → 4 > 3: remove 4 (k=2), push   13
2 → 3 > 2: remove 3 (k=1), push   12
2 → push                          122
1 → 2 > 1: remove 2 (k=0), push   121
9 → push                          1219        → answer "1219"
```

**Backspace String Compare**: `#` means "delete the previous character". Build each string with a stack. `#` pops.

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea (Remove K Digits) | remove one digit at a time, `k` times | one pass with an increasing stack |
| Time | `O(n · k)` | `O(n)` |
| Space | `O(n)` | `O(n)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
fun removeKdigitsBrute(num: String, k: Int): String {
    var s = num
    repeat(k) {
        if (s.isEmpty()) return "0"
        var idx = 0
        while (idx < s.length - 1 && s[idx] <= s[idx + 1]) idx++       // the first digit bigger than the next one
        s = s.removeRange(idx, idx + 1)
    }
    val result = s.trimStart('0')
    return if (result.isEmpty()) "0" else result
}
```

The stack removes the same digits, but each digit is pushed and popped only once.

#### 4. Kotlin Code

```kotlin
// Basic Calculator II: non-negative integers, + - * /, spaces allowed
fun calculate(s: String): Int {
    val stack = ArrayDeque<Int>()
    var num = 0
    var op = '+'                                              // the operator BEFORE the current number
    for (i in s.indices) {
        val c = s[i]
        if (c.isDigit()) num = num * 10 + (c - '0')           // build multi-digit numbers
        if ((!c.isDigit() && c != ' ') || i == s.length - 1) {
            when (op) {
                '+' -> stack.addLast(num)
                '-' -> stack.addLast(-num)
                '*' -> stack.addLast(stack.removeLast() * num)
                '/' -> stack.addLast(stack.removeLast() / num)   // truncates toward zero
            }
            op = c
            num = 0
        }
    }
    return stack.sum()
}

// Basic Calculator: + - ( ) with brackets
fun calculateWithBrackets(s: String): Int {
    val stack = ArrayDeque<Int>()
    var result = 0
    var num = 0
    var sign = 1
    for (c in s) {
        when {
            c.isDigit() -> num = num * 10 + (c - '0')
            c == '+' || c == '-' -> {
                result += sign * num
                num = 0
                sign = if (c == '+') 1 else -1
            }
            c == '(' -> {                                      // save the outside, start fresh inside
                stack.addLast(result)
                stack.addLast(sign)
                result = 0
                sign = 1
            }
            c == ')' -> {
                result += sign * num
                num = 0
                result *= stack.removeLast()                   // the sign before "("
                result += stack.removeLast()                   // the result before "("
            }
        }
    }
    return result + sign * num
}

// Remove K Digits
fun removeKdigits(num: String, k: Int): String {
    var remaining = k
    val sb = StringBuilder()                                  // used as a stack of digits
    for (c in num) {
        while (remaining > 0 && sb.isNotEmpty() && sb.last() > c) {
            sb.deleteCharAt(sb.length - 1)
            remaining--
        }
        sb.append(c)
    }
    while (remaining > 0 && sb.isNotEmpty()) {                // still need to remove: drop from the end
        sb.deleteCharAt(sb.length - 1)
        remaining--
    }
    val result = sb.toString().trimStart('0')                 // remove leading zeros
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
```

Checks: `calculate("3+2*2")` → `7`. `calculate(" 3/2 ")` → `1`. `calculateWithBrackets("1-(2+3)")` → `-4`. `calculateWithBrackets("(1+(4+5+2)-3)+(6+8)")` → `23`. `removeKdigits("1432219", 3)` → `"1219"`. `removeKdigits("10200", 1)` → `"200"`. `removeKdigits("10", 2)` → `"0"`. `backspaceCompare("ab#c", "ad#c")` → `true`.

#### 5. Complexity

| Problem | Time | Space |
|---|---|---|
| Basic Calculator II | `O(n)` | `O(n)` |
| Basic Calculator (brackets) | `O(n)` | `O(n)` |
| Remove K Digits | `O(n)` | `O(n)` |
| Backspace String Compare | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Forgetting the last number.** No operator follows it, so process it when `i` is the last index.
2. **Multi-digit numbers.** Use `num = num * 10 + digit`, not `num = digit`.
3. **Spaces treated as operators.** Skip them.
4. **Changing `op` too early.** Use the previous operator first, then store the new one.
5. **Remove K Digits:** leading zeros (`"10200"` → `"200"`), an empty result (return `"0"`), and `k` bigger than the number of pops done (drop from the end).
6. **Backspace on an empty stack.** Check `isNotEmpty()`.
7. **Brackets:** the sign before `(` is popped first, then the old result.

#### 7. Say This in the Interview

1. "`*` and `/` bind tighter, so I apply them immediately to the last number. I push `+` and `-` terms and add everything at the end."
2. "For brackets I save the current result and sign on `(`, and restore them on `)`."
3. "For Remove K Digits I keep an increasing stack: a smaller digit pops bigger digits before it."
4. "Everything is one pass: `O(n)` time."

#### 8. Quick Check

1. What does `"2*3+4"` give in Calculator II? Show the stack.
2. What does `removeKdigits("112", 1)` give?

<details>
<summary>Answers</summary>

1. Push `2`; then `*` with `3` → pop `2`, push `6`; then `+` with `4` → push `4`. Stack `[6, 4]`, sum `10`.
2. `"11"`. No digit is bigger than the one after it, so nothing is popped inside the loop. The last digit is removed at the end.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) (Medium) | numbers stack, `*` `/` first |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) (Hard) | save and restore at brackets |
| 402 | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) (Medium) | increasing stack |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) (Easy) | `#` pops |
| 316 | [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) (Medium) | increasing stack with extra rules |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (Medium) | next note group |
