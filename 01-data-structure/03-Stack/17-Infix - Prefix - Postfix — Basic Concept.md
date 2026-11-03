# Infix / Prefix / Postfix — Basic Concept

> Keep this at a basic level. Interviews rarely go deeper than this note.

#### 1. What Is It?

Three ways to write the same maths expression. The only difference is **where the operator goes**.

| Name | Operator position | Example for "a plus b" | Needs brackets? |
|---|---|---|---|
| **Infix** | between | `a + b` | yes, and priority rules |
| **Prefix** | before | `+ a b` | no |
| **Postfix** | after | `a b +` | no |

```text
Infix            Prefix          Postfix
a + b * c        + a * b c       a b c * +
(a + b) * c      * + a b c       a b + c *
```

Computers like postfix. A stack evaluates it in one pass (see the RPN note). So calculators often **convert infix → postfix first**.

#### 2. How It Works

All three come from the same expression tree. Only the order of reading changes.

```text
      +
     / \
    a   *            prefix  = root, left, right  →  + a * b c
       / \           postfix = left, right, root  →  a b c * +
      b   c          infix   = left, root, right  →  a + b * c   (with brackets when needed)
```

**Infix → postfix with a stack** (the "shunting-yard" idea). Rules:

1. A letter or number → send it to the output.
2. `(` → push it.
3. `)` → pop operators to the output until you meet `(`. Discard the `(`.
4. An operator → first pop operators of **higher or equal priority** from the stack to the output. Then push the new one.
5. At the end → pop everything to the output.

Priority: `^` (highest) → `*` `/` → `+` `-` (lowest).

```text
a + b * c

a   output: a
+   push +                  stack: +
b   output: a b
*   * is higher than +, so push        stack: + *
c   output: a b c
end pop all                 output: a b c * +
```

#### 3. Brute Force vs Optimized

| Approach | Idea | Time |
|---|---|---|
| Parse the infix text recursively for every parenthesis and precedence level | split on the lowest-precedence operator, recurse on both sides | `O(n²)` worst case |
| Convert to postfix with the **shunting-yard** algorithm, then evaluate with a stack | one pass with an operator stack, one pass to evaluate | `O(n)` |
| Evaluate infix directly with two stacks (numbers and operators) | pop and apply while the top operator has higher or equal precedence | `O(n)` |

The idea to remember: **postfix needs no parentheses and no precedence rules**. Once the expression is in postfix form, a single stack evaluates it. The hard part (precedence) is handled once, in the conversion.

```text
infix:    2 + 3 * 4        postfix:  2 3 4 * +        value 14
infix:  (2 + 3) * 4        postfix:  2 3 + 4 *        value 20
```

#### 4. Kotlin Code

```kotlin
// Infix → postfix. Operands are single letters or digits.
fun toPostfix(expression: String): String {
    val priority = mapOf('+' to 1, '-' to 1, '*' to 2, '/' to 2, '^' to 3)
    val output = StringBuilder()
    val ops = ArrayDeque<Char>()

    for (c in expression) {
        when {
            c.isLetterOrDigit() -> output.append(c)
            c == '(' -> ops.addLast(c)
            c == ')' -> {
                while (ops.isNotEmpty() && ops.last() != '(') output.append(ops.removeLast())
                if (ops.isNotEmpty()) ops.removeLast()                 // throw away the '('
            }
            c in priority -> {
                while (ops.isNotEmpty() && ops.last() != '(' &&
                    (priority.getValue(ops.last()) > priority.getValue(c) ||
                        (priority.getValue(ops.last()) == priority.getValue(c) && c != '^'))
                ) {
                    output.append(ops.removeLast())
                }
                ops.addLast(c)
            }
        }
    }
    while (ops.isNotEmpty()) output.append(ops.removeLast())
    return output.toString()
}

// Evaluate a postfix string of single digits, e.g. "23*5+" = 2*3+5 = 11
fun evalPostfixDigits(postfix: String): Int {
    val stack = ArrayDeque<Int>()
    for (c in postfix) {
        if (c.isDigit()) {
            stack.addLast(c - '0')
        } else {
            val b = stack.removeLast()
            val a = stack.removeLast()
            stack.addLast(
                when (c) {
                    '+' -> a + b
                    '-' -> a - b
                    '*' -> a * b
                    '/' -> a / b
                    else -> throw IllegalArgumentException("Unknown operator $c")
                }
            )
        }
    }
    return stack.last()
}
```

Checks: `toPostfix("a+b*c")` → `"abc*+"`. `toPostfix("(a+b)*c")` → `"ab+c*"`. `toPostfix("a-b-c")` → `"ab-c-"`. `evalPostfixDigits("23*5+")` → `11`.

Prefix is evaluated the same way, but you scan from the **right** and the first number you pop is the **left** operand.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Infix → postfix | `O(n)` | `O(n)` |
| Evaluate postfix | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Wrong order for equal priority.** `a - b - c` means `(a - b) - c`, so pop an equal operator before pushing. The exception is `^`, which goes right to left.
2. **Not discarding `(`** after `)`.
3. **Treating `(` as a normal operator** when comparing priority. Stop at `(`.
4. **Leaving operators in the stack** at the end.
5. **Evaluating prefix with the wrong operand order.**
6. Multi-digit numbers and negative numbers need extra handling (this version uses single characters).

#### 7. Say This in the Interview

1. "Postfix needs no brackets, so a stack can evaluate it in one pass."
2. "To convert infix to postfix, operands go straight to the output. Operators wait on a stack until a lower-priority operator arrives."
3. "Time `O(n)`, space `O(n)`."

#### 8. Quick Check

1. Write `a * (b + c)` in postfix.
2. Which reading order of the expression tree gives postfix?

<details>
<summary>Answers</summary>

1. `a b c + *`.
2. Left, right, root (post-order).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (Medium) | evaluate postfix |
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) (Medium) | evaluate infix directly |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) (Hard) | brackets |
| 1628 | [Design an Expression Tree With Evaluate Function](https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/) (Medium) | postfix to tree |
