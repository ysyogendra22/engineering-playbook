# Evaluate Postfix / Reverse Polish Notation

#### 1. What Is It?

Normal maths writes the operator **between** the numbers: `3 + 4`. This is called **infix**.

**Postfix** (also called **Reverse Polish Notation**, RPN) writes the operator **after** the numbers: `3 4 +`.

```text
Infix:    (2 + 1) * 3
Postfix:  2 1 + 3 *
```

Postfix needs **no brackets** and no priority rules (`*` before `+`). The order of the tokens already says what to do first.

You evaluate it with a **stack of numbers**:

- number → push it,
- operator → pop two numbers, calculate, push the result.

This is *Evaluate Reverse Polish Notation* (LeetCode 150).

#### 2. How It Works

`tokens = ["2", "1", "+", "3", "*"]`

```text
"2"   push 2                                  stack [2]
"1"   push 1                                  stack [2, 1]
"+"   pop 1 (right), pop 2 (left), push 2+1   stack [3]
"3"   push 3                                  stack [3, 3]
"*"   pop 3 (right), pop 3 (left), push 3*3   stack [9]

answer = 9
```

**Order matters** for `-` and `/`. The **first number you pop is the RIGHT number**.

```text
tokens: "5", "3", "-"
pop → 3 (right), pop → 5 (left), calculate 5 - 3 = 2      (not 3 - 5)
```

Division truncates toward zero: `13 / 5 = 2`, and `-7 / 2 = -3`. Kotlin `Int` division does exactly this.

#### 3. Kotlin Code

```kotlin
fun evalRPN(tokens: Array<String>): Int {
    val stack = ArrayDeque<Int>()
    for (token in tokens) {
        when (token) {
            "+", "-", "*", "/" -> {
                val b = stack.removeLast()               // right number first
                val a = stack.removeLast()               // then the left number
                stack.addLast(
                    when (token) {
                        "+" -> a + b
                        "-" -> a - b
                        "*" -> a * b
                        else -> a / b                    // truncates toward zero
                    }
                )
            }
            else -> stack.addLast(token.toInt())          // also works for "-3"
        }
    }
    return stack.last()
}
```

Checks: `["2","1","+","3","*"]` → `9`. `["4","13","5","/","+"]` → `6`. `["10","6","9","3","+","-11","*","/","*","17","+","5","+"]` → `22`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Stack | `O(n)` | `O(n)` |

Each token is handled once.

#### 5. Common Mistakes

1. **Wrong operand order.** `b - a` instead of `a - b`. The first pop is the right number.
2. **Mistaking `"-3"` for the operator `-`.** Compare the **whole token** with `"-"`. `"-3"` is a number.
3. **Floor division.** The question wants truncation toward zero. Kotlin `/` on `Int` does this. Do not use `Math.floorDiv`.
4. **Overflow.** Use `Long` if the numbers can be large.
5. **Stack has fewer than two numbers** when an operator arrives. Only happens with invalid input.

#### 6. Say This in the Interview

1. "Postfix needs no brackets. I scan left to right with a stack."
2. "A number is pushed. For an operator I pop the right operand, then the left operand, and push the result."
3. "Time `O(n)`, space `O(n)`. Division truncates toward zero."

#### 7. Quick Check

1. Evaluate `["6", "2", "/", "3", "-"]`.
2. Why is `["-3"]` a number and not an operator?

<details>
<summary>Answers</summary>

1. `6 / 2 = 3`, then `3 - 3 = 0`. The answer is `0`.
2. The token is `"-3"`, which is not exactly `"-"`. Only a token that equals `+`, `-`, `*` or `/` is an operator.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (Medium) | this note |
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) (Medium) | evaluate infix with a stack |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) (Hard) | brackets |
| 772 | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) (Hard, premium) | brackets and `* /` |
| 1628 | [Design an Expression Tree With Evaluate Function](https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/) (Medium) | build a tree from postfix |
