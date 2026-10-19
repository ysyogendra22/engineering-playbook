# Infix / Prefix / Postfix — Basic Concept

#### 1. Definition — Must Know

1. **Infix** — the operator is **between** its operands: `a + b`. This is normal maths, and it needs brackets and priority rules.
2. **Prefix** (Polish notation) — the operator comes **before** its operands: `+ a b`.
3. **Postfix** (Reverse Polish Notation) — the operator comes **after** its operands: `a b +`.
4. Prefix and postfix need **no brackets** and no priority rules. Computers prefer them.

#### 2. Why It Is Used — Must Know

1. It explains how calculators and compilers evaluate expressions.
2. Converting infix to postfix is a classic stack algorithm (**shunting-yard**).
3. It connects stacks to expression trees and parsing. Keep it at the basic level for interviews.

#### 3. How It Works — Must Know

```text
Infix           Prefix          Postfix
a + b           + a b           a b +
a + b * c       + a * b c       a b c * +
(a + b) * c     * + a b c       a b + c *
a - b - c       - - a b c       a b - c -
```

All three describe the same expression tree:

```text
      +
     / \
    a   *            infix:   a + b * c   (needs priority: * before +)
       / \           prefix:  + a * b c   (root, left, right)
      b   c          postfix: a b c * +   (left, right, root)
```

- **Prefix** = pre-order walk of the tree.
- **Postfix** = post-order walk of the tree.
- **Infix** = in-order walk (plus brackets).

**Infix → postfix with a stack (shunting-yard).** Operands go straight to the output. Operators wait on a stack until an operator of lower priority arrives.

```text
a + b * c

a   operand        output: a
+   push           stack: +
b   operand        output: a b
*   priority higher than + on top → push      stack: + *
c   operand        output: a b c
end: pop all       output: a b c * +
```

#### 4. Core Concepts — Must Know

1. **Operator priority:** `^` (highest, right-associative) > `* /` > `+ -` (lowest). Brackets override priority.
2. **Associativity:** `a - b - c` means `(a - b) - c` (left to right). `a ^ b ^ c` means `a ^ (b ^ c)` (right to left).
3. **Shunting-yard rules:**
   - operand → output,
   - `(` → push,
   - `)` → pop operators to the output until `(`, then discard `(`,
   - operator → pop operators from the stack while the stack top has **higher priority**, or **equal priority and the new operator is left-associative**; then push the new operator,
   - at the end → pop everything to the output.
4. **Evaluate postfix** with a number stack (see the RPN note).
5. **Evaluate prefix** by scanning right to left; the first popped is the **left** operand.
6. **Convert prefix ↔ postfix** by reading the expression tree or by using a stack of strings.

| Notation | Brackets needed? | Priority rules needed? | Easy for a stack? |
|---|---|---|---|
| Infix | yes | yes | needs conversion |
| Prefix | no | no | yes (right to left) |
| Postfix | no | no | yes (left to right) |

#### 5. Algorithm — Must Know

```text
toPostfix(expression):
    output = ""; operators = empty stack
    for each token:
        operand        → append to output
        '('            → push
        ')'            → pop to output until '(' , discard '('
        operator o1    → while stack top o2 is not '(' and (priority(o2) > priority(o1)
                                or (priority(o2) == priority(o1) and o1 is left-associative)):
                             pop o2 to output
                         push o1
    pop everything left on the stack to output
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Infix → postfix for single-character operands (letters or digits)
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
                if (ops.isNotEmpty()) ops.removeLast()          // discard '('
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

// Evaluate prefix: scan from the right; the first popped is the LEFT operand
fun evalPrefixDigits(prefix: String): Int {
    val stack = ArrayDeque<Int>()
    for (c in prefix.reversed()) {
        if (c.isDigit()) {
            stack.addLast(c - '0')
        } else {
            val a = stack.removeLast()          // left operand
            val b = stack.removeLast()          // right operand
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

Checks: `toPostfix("a+b*c")` → `"abc*+"`. `toPostfix("(a+b)*c")` → `"ab+c*"`. `toPostfix("a-b-c")` → `"ab-c-"`. `toPostfix("a^b^c")` → `"abc^^"`. `evalPostfixDigits("23*5+")` → `11`. `evalPrefixDigits("+*235")` → `11`.

#### 7. Time & Space Complexity — Must Know

| Task | Time | Space |
|---|---:|---:|
| Infix → postfix | `O(n)` | `O(n)` |
| Evaluate postfix / prefix | `O(n)` | `O(n)` |

Each token is pushed and popped at most once.

#### 8. Common Notation Patterns — Must Know

1. **Evaluate postfix** (LeetCode 150).
2. **Infix → postfix** (shunting-yard), usually as a stepping stone to a calculator.
3. **Basic Calculator** problems (LeetCode 224, 227, 772).
4. **Prefix ↔ postfix conversions** (string stacks).
5. **Expression tree** construction from postfix (LeetCode 1628).
6. **Check if an expression has redundant brackets** (stack).
7. **Android example:** a formula parser for a unit converter or a finance calculator.

#### 9. Edge Cases / Common Mistakes

1. Wrong associativity: `a - b - c` must pop equal-priority operators; `a ^ b ^ c` must not.
2. Forgetting to discard `(` after `)`.
3. Treating `(` as a normal operator when comparing priorities. Stop at `(`.
4. Leaving operators on the stack at the end.
5. Wrong operand order when evaluating prefix (left operand is popped first there).
6. Multi-digit numbers and spaces in real input (the examples above use single characters).
7. Unary minus (`-3`) is not handled by this basic version.
8. Mismatched brackets (invalid input).

#### 10. When to Use / When Not to Use

**Use when:**

1. You explain how expression evaluation works.
2. You build a calculator that must respect priority and brackets.

**Skip the full conversion when:**

1. A direct approach (two stacks, or the Basic Calculator II method) answers the question. Advanced expression conversion is low priority.

#### 11. Related Topics

1. Evaluate Postfix / Reverse Polish Notation
2. Expression / String Processing with Stack
3. Tree traversals (`01-data-structure/07-Tree`)
4. Expression Parsing (study separately)

#### 12. Interview Must Remember

1. **Infix: `a + b`. Prefix: `+ a b`. Postfix: `a b +`.**
2. Postfix and prefix need no brackets; postfix = post-order of the expression tree.
3. Shunting-yard: operands to output, operators wait on a stack by priority, `)` pops to `(`.
4. Left-associative operators pop equal priority; `^` does not.
