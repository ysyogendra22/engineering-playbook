# Evaluate Postfix / Reverse Polish Notation

#### 1. Definition — Must Know

1. **Postfix notation** (Reverse Polish Notation, RPN) writes the operator **after** its two operands: `3 4 +` means `3 + 4`.
2. It needs **no brackets** and no priority rules. The order of the tokens already says what to do first.
3. Evaluate it with a **stack of numbers**: push numbers; on an operator, pop two numbers, apply the operator, push the result.
4. It is *Evaluate Reverse Polish Notation* (LeetCode 150). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is the simplest stack-based evaluator and a common easy/medium question.
2. Compilers and calculators convert normal (infix) expressions to postfix and evaluate them this way.
3. It teaches the **operand order** rule, which is a very common bug.

#### 3. How It Works — Must Know

`tokens = ["2", "1", "+", "3", "*"]` means `(2 + 1) * 3`.

```text
2   push                         stack [2]
1   push                         stack [2, 1]
+   pop b=1, pop a=2, push 2+1   stack [3]
3   push                         stack [3, 3]
*   pop b=3, pop a=3, push 3*3   stack [9]

answer = 9
```

Order matters for `-` and `/`: the **first popped is the right operand**.

```text
tokens: "5", "3", "-"     →   b = pop() = 3,  a = pop() = 5,  result = a - b = 2     (not 3 - 5)
```

Division in the problem truncates toward zero: `["4","13","5","/","+"]` is `4 + (13 / 5) = 6`.

#### 4. Core Concepts — Must Know

1. **Numbers → push. Operators → pop two, compute, push.**
2. **Right operand first:** `b = pop()`, then `a = pop()`, result is `a op b`.
3. **At the end, the stack has exactly one number** (for a valid expression). That is the answer.
4. **Negative numbers are tokens too** (`"-3"`). Distinguish a number from the operator `"-"` by its length or by checking whether it is exactly one of `+ - * /`.
5. **Division:** Kotlin `/` on `Int` truncates toward zero, which is what the problem asks.
6. **No priority rules are needed.** The tokens' order already includes them.
7. **Overflow:** if results can be large, use `Long`.

#### 5. Algorithm — Must Know

```text
stack = empty
for each token:
    if token is an operator:
        b = stack.pop();  a = stack.pop()
        stack.push(a op b)
    else:
        stack.push(token as number)
return stack.pop()
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun evalRPN(tokens: Array<String>): Int {
    val stack = ArrayDeque<Int>()
    for (token in tokens) {
        when (token) {
            "+", "-", "*", "/" -> {
                val b = stack.removeLast()               // right operand first
                val a = stack.removeLast()
                stack.addLast(
                    when (token) {
                        "+" -> a + b
                        "-" -> a - b
                        "*" -> a * b
                        else -> a / b                    // truncates toward zero
                    }
                )
            }
            else -> stack.addLast(token.toInt())          // handles "-3" too
        }
    }
    return stack.last()
}

// Same idea with Long and a map of operators
fun evalRPNLong(tokens: List<String>): Long {
    val ops: Map<String, (Long, Long) -> Long> = mapOf(
        "+" to { a: Long, b: Long -> a + b },
        "-" to { a: Long, b: Long -> a - b },
        "*" to { a: Long, b: Long -> a * b },
        "/" to { a: Long, b: Long -> a / b },
    )
    val stack = ArrayDeque<Long>()
    for (t in tokens) {
        val op = ops[t]
        if (op != null) {
            val b = stack.removeLast()
            val a = stack.removeLast()
            stack.addLast(op(a, b))
        } else {
            stack.addLast(t.toLong())
        }
    }
    return stack.last()
}
```

Checks: `evalRPN(["2","1","+","3","*"])` → `9`. `evalRPN(["4","13","5","/","+"])` → `6`. `evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])` → `22`.

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---:|
| Time | `O(n)` — each token is handled once |
| Space | `O(n)` for the stack (at most about `n/2` numbers at once) |

#### 8. Common Postfix Patterns — Must Know

1. **Evaluate Reverse Polish Notation** (LeetCode 150).
2. **Infix → postfix conversion** (shunting-yard) — next note.
3. **Basic Calculator I/II/III** (LeetCode 224, 227, 772) — evaluate infix with a stack directly.
4. **Expression trees** — postfix evaluation matches a post-order walk of the tree.
5. **Prefix evaluation** — scan right to left; the operand order flips (first popped is the **left** operand).
6. **Build an expression tree from postfix** (LeetCode 1628).
7. **Android example:** a formula engine in a spreadsheet-like feature.

#### 9. Edge Cases / Common Mistakes

1. **Wrong operand order** for `-` and `/` (`b - a` instead of `a - b`).
2. Treating `"-3"` as the operator `-`. Compare the whole token with `"-"`.
3. Division rounding: use truncation toward zero (Kotlin `Int` division), not floor.
4. Division by zero (the problem usually guarantees it does not happen).
5. Popping with fewer than two numbers on the stack (invalid input). Decide whether to throw.
6. Overflow in `Int` for big expressions.
7. Using `stack.removeLast()` for the answer and leaving the stack in an unknown state; use `last()` if you only read it.
8. Assuming the stack ends with one number without checking when input may be invalid.

#### 10. When to Use / When Not to Use

**Use when:**

1. The expression is already in postfix form.
2. You convert infix to postfix first and then evaluate.

**Avoid when:**

1. The expression has brackets and is in infix form and you only need a result. A direct two-stack evaluation or recursive descent parser may be simpler.

#### 11. Related Topics

1. Infix / Prefix / Postfix — Basic Concept
2. Expression / String Processing with Stack
3. Stack Operations & Complexity
4. Expression Parsing (study separately)

#### 12. Interview Must Remember

1. **Number → push. Operator → `b = pop()`, `a = pop()`, push `a op b`.**
2. Right operand is popped first.
3. Division truncates toward zero; negative numbers are valid tokens.
4. `O(n)` time and space.
