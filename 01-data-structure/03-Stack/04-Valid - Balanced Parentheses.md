# Valid / Balanced Parentheses

> This is the most asked stack question. Make sure you can write it from memory.

#### 1. What Is It?

You get a string with brackets: `( ) [ ] { }`. It is **valid** when:

1. every opening bracket is closed by the **same type** of bracket, and
2. the brackets close in the **correct order**.

| Valid | Invalid | Why invalid |
|---|---|---|
| `()[]{}` | `(]` | wrong type |
| `{[()]}` | `([)]` | wrong order |
| `""` (empty) | `((` | never closed |
| | `())` | closing bracket with nothing to match |

**Idea:** push every opening bracket. When a closing bracket comes, the **top** of the stack must be its match. The newest open bracket must close first. That is exactly LIFO.

#### 2. How It Works

`s = "{[()]}"`

```text
{   push                          stack: {
[   push                          stack: { [
(   push                          stack: { [ (
)   top is "(" → match, pop       stack: { [
]   top is "[" → match, pop       stack: {
}   top is "{" → match, pop       stack: (empty)

end: stack is empty → valid
```

`s = "([)]"`

```text
(   push                          stack: (
[   push                          stack: ( [
)   top is "[", but ")" needs "(" → mismatch → invalid
```

Three ways to fail:

1. A closing bracket arrives and the stack is **empty**.
2. The top is the **wrong** type.
3. The loop ends and the stack is **not empty**.

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea | keep deleting `()`, `[]`, `{}` until nothing changes | one stack, match on the fly |
| Time | `O(n²)` | `O(n)` |
| Space | `O(n)` (new strings) | `O(n)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
fun isValidBrute(s: String): Boolean {
    var t = s
    while (true) {
        val r = t.replace("()", "").replace("[]", "").replace("{}", "")
        if (r == t) break                  // nothing was removed
        t = r
    }
    return t.isEmpty()                      // valid only if everything was removed
}
```

The stack version does each match once instead of scanning the string again and again.

#### 4. Kotlin Code

```kotlin
fun isValid(s: String): Boolean {
    val match = mapOf(')' to '(', ']' to '[', '}' to '{')   // closing → opening
    val stack = ArrayDeque<Char>()

    for (c in s) {
        if (c in match) {                                    // c is a closing bracket
            if (stack.isEmpty() || stack.removeLast() != match[c]) return false
        } else {
            stack.addLast(c)                                 // c is an opening bracket
        }
    }
    return stack.isEmpty()                                   // leftovers mean invalid
}
```

**Only one type of bracket `( )`?** You do not need a stack. A counter is enough:

```kotlin
fun minAddToMakeValid(s: String): Int {      // LeetCode 921
    var open = 0      // "(" still waiting for a ")"
    var extra = 0     // ")" that had no "("
    for (c in s) {
        if (c == '(') open++
        else if (open > 0) open--
        else extra++
    }
    return open + extra
}
```

**Remove the fewest brackets to make the string valid (LeetCode 1249).** Store the **index** of each `(` in the stack.

```kotlin
fun minRemoveToMakeValid(s: String): String {
    val remove = HashSet<Int>()
    val stack = ArrayDeque<Int>()                 // indexes of "("
    for ((i, c) in s.withIndex()) {
        if (c == '(') stack.addLast(i)
        else if (c == ')') {
            if (stack.isEmpty()) remove.add(i) else stack.removeLast()
        }
    }
    remove.addAll(stack)                          // "(" that never closed
    val sb = StringBuilder()
    for ((i, c) in s.withIndex()) if (i !in remove) sb.append(c)
    return sb.toString()
}
// "lee(t(c)o)de)" → "lee(t(c)o)de"
```

**Longest valid substring (LeetCode 32).** Push indexes. Keep `-1` at the bottom as a starting point.

```kotlin
fun longestValidParentheses(s: String): Int {
    val stack = ArrayDeque<Int>()
    stack.addLast(-1)
    var best = 0
    for (i in s.indices) {
        if (s[i] == '(') {
            stack.addLast(i)
        } else {
            stack.removeLast()
            if (stack.isEmpty()) stack.addLast(i)            // new starting point
            else best = maxOf(best, i - stack.last())
        }
    }
    return best
}
```

#### 5. Complexity

| Solution | Time | Space |
|---|---|---|
| Stack (`isValid`) | `O(n)` | `O(n)` |
| Counter (one bracket type) | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Popping an empty stack** (input starts with `)`). Check `stack.isEmpty()` first.
2. **Forgetting the final `stack.isEmpty()`** check. `"(("` would pass.
3. **Mapping the wrong way.** The map goes from the **closing** bracket to its **opening** bracket.
4. **Using one counter for several bracket types.** `"([)]"` would wrongly pass.
5. **Longest Valid Parentheses:** forgetting the `-1` at the bottom.

#### 7. Say This in the Interview

1. "I push opening brackets and match each closing bracket against the top."
2. "It fails if the stack is empty on a closing bracket, if the types differ, or if the stack is not empty at the end."
3. "Time `O(n)`, space `O(n)`. With one bracket type a counter gives `O(1)` space."
4. "An odd length can never be valid, so I can return false immediately."

#### 8. Quick Check

1. Is `"(()"` valid? Why?
2. Is `"{[}]"` valid? Why?

<details>
<summary>Answers</summary>

1. No. After the loop the stack still holds one `(`.
2. No. When `}` arrives, the top is `[`, which does not match.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) | this note |
| 921 | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) (Medium) | counter |
| 1249 | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) (Medium) | stack of indexes |
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) (Hard) | stack of indexes with `-1` |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium) | backtracking, not a stack |
| 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) (Medium) | counter with a range for `*` |
