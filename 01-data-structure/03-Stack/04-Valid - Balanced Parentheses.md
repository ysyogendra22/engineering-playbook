# Valid / Balanced Parentheses

#### 1. Definition — Must Know

1. A string of brackets is **valid** if every opening bracket is closed by the **same type** of bracket and in the **correct order**.
2. Valid: `"()[]{}"`, `"{[]}"`. Invalid: `"(]"`, `"([)]"`, `"(("`.
3. The method: **push opening brackets; on a closing bracket, the top of the stack must be its match.**
4. This is *Valid Parentheses* (LeetCode 20). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is the most famous stack problem and a standard first question.
2. The same idea checks HTML/XML tags, code blocks, math expressions, and JSON.
3. The nested "last opened, first closed" shape is exactly LIFO.

#### 3. How It Works — Must Know

`s = "{[()]}"`

```text
{   push           stack: {
[   push           stack: { [
(   push           stack: { [ (
)   top is ( → match → pop       stack: { [
]   top is [ → match → pop       stack: {
}   top is { → match → pop       stack: (empty)

End: stack is empty → valid
```

`s = "([)]"`

```text
(   push           stack: (
[   push           stack: ( [
)   top is [ , but ) needs ( → mismatch → INVALID
```

Invalid in three ways:

```text
closing bracket with an empty stack   "())"      → nothing to match
wrong type on top                     "(]"
leftover openings at the end          "(("       → stack not empty
```

#### 4. Core Concepts — Must Know

1. **Push openers. Match closers against the top.**
2. **Map closer → opener** (`')' to '('`) so you can compare in one line.
3. **Three checks:** stack not empty when a closer arrives, top matches, stack empty at the end.
4. **Quick exit:** an odd length can never be valid.
5. **Only one bracket type?** No stack is needed. A counter is enough (`open++` for `(`, `open--` for `)`, never below 0, and 0 at the end).
6. **Other characters** (letters, digits) are ignored in "balanced expression" versions.
7. **Stack of indices** helps when the answer needs positions (Longest Valid Parentheses).

#### 5. Algorithm — Must Know

```text
for each character c:
    if c is an opener: push c
    else if c is a closer:
        if stack is empty or stack.pop() != matching opener of c: return false
return stack is empty
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Valid Parentheses
fun isValid(s: String): Boolean {
    if (s.length % 2 != 0) return false
    val match = mapOf(')' to '(', ']' to '[', '}' to '{')
    val stack = ArrayDeque<Char>()
    for (c in s) {
        if (c in match) {                                   // a closing bracket
            if (stack.isEmpty() || stack.removeLast() != match[c]) return false
        } else {
            stack.addLast(c)                                // an opening bracket
        }
    }
    return stack.isEmpty()
}

// Only one bracket type: a counter is enough
fun isValidSingleType(s: String): Boolean {
    var open = 0
    for (c in s) {
        if (c == '(') open++
        else if (c == ')') {
            if (open == 0) return false
            open--
        }
    }
    return open == 0
}

// Minimum Add to Make Parentheses Valid (LeetCode 921) — counters, no stack needed
fun minAddToMakeValid(s: String): Int {
    var open = 0          // unmatched '('
    var add = 0           // ')' that had no '(' before it
    for (c in s) {
        if (c == '(') open++
        else if (open > 0) open--
        else add++
    }
    return open + add
}

// Longest Valid Parentheses (LeetCode 32) — stack of indices
fun longestValidParentheses(s: String): Int {
    val stack = ArrayDeque<Int>()
    stack.addLast(-1)                                       // base index before the string
    var best = 0
    for (i in s.indices) {
        if (s[i] == '(') {
            stack.addLast(i)
        } else {
            stack.removeLast()
            if (stack.isEmpty()) stack.addLast(i)           // new base
            else best = maxOf(best, i - stack.last())
        }
    }
    return best
}
```

Checks: `isValid("()[]{}")` → `true`. `isValid("([)]")` → `false`. `minAddToMakeValid("())")` → `1`. `longestValidParentheses(")()())")` → `4`.

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Stack | `O(n)` | `O(n)` |
| Counter (one bracket type) | `O(n)` | `O(1)` |
| Longest Valid Parentheses (stack of indices) | `O(n)` | `O(n)` |

#### 8. Common Parentheses Patterns — Must Know

1. **Valid Parentheses** (LeetCode 20).
2. **Minimum Add to Make Parentheses Valid** (LeetCode 921).
3. **Minimum Remove to Make Valid Parentheses** (LeetCode 1249) — stack of indices to remove.
4. **Longest Valid Parentheses** (LeetCode 32).
5. **Generate Parentheses** (LeetCode 22) — backtracking.
6. **Valid Parenthesis String with `*`** (LeetCode 678) — range counter.
7. **Score of Parentheses** (LeetCode 856), **Remove Outermost Parentheses** (LeetCode 1021).
8. **Android example:** validating a custom markup or a templating string.

#### 9. Edge Cases / Common Mistakes

1. Popping from an empty stack when a closer comes first (`"))"`).
2. Forgetting the final `stack.isEmpty()` check (`"(("`).
3. Comparing the wrong way round: the **closer** maps to its **opener**.
4. An empty string is valid.
5. Odd length: invalid at once.
6. Using one counter for several bracket types (`"([)]"` would pass wrongly).
7. Treating other characters as brackets.
8. In Longest Valid Parentheses: forgetting the base index `-1`.

#### 10. When to Use / When Not to Use

**Use a stack when:**

1. There are several bracket types or the nesting order matters.

**Use a counter when:**

1. There is only one bracket type. It is simpler and `O(1)` space.

#### 11. Related Topics

1. Stack Fundamentals — LIFO
2. Expression / String Processing with Stack
3. Decode String
4. Backtracking — Generate Parentheses (`02-algorithm/06-Backtracking & Branch and Bound`)

#### 12. Interview Must Remember

1. **Push openers. A closer must match the top. The stack must be empty at the end.**
2. Three failures: closer on an empty stack, wrong top, leftovers.
3. One bracket type → a counter is enough.
4. Longest Valid Parentheses → stack of indices with a base of `-1`.
