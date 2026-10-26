# Remove Adjacent Duplicates

#### 1. What Is It?

Remove neighbouring equal characters again and again, until none are left.

Two versions:

| Version | Rule | Example |
|---|---|---|
| **I** (LeetCode 1047) | remove pairs of equal neighbours | `"abbaca"` → `"ca"` |
| **II** (LeetCode 1209) | remove groups of `k` equal neighbours | `"deeedbbcccbdaa"`, `k=3` → `"aa"` |

The tricky part: removing a pair can make **new neighbours** touch. In `"abba"`, removing `bb` leaves `"aa"`, which must also go.

A stack handles this in **one pass**. The top of the stack is always the last character you kept.

#### 2. How It Works

**Version I.** For each character: if it equals the top, **pop** (the pair disappears). Otherwise **push**.

```text
s = "abbaca"

a   stack empty → push          stack: a
b   top is a, different → push  stack: a b
b   top is b, same → pop        stack: a
a   top is a, same → pop        stack:
c   stack empty → push          stack: c
a   top is c, different → push  stack: c a

result: "ca"
```

**Version II.** Store `(character, count)` pairs. If the new character equals the top character, add 1 to its count. When the count reaches `k`, remove the whole pair.

```text
s = "deeedbbcccbdaa", k = 3

d(1)  e(1) e(2) e(3) → count is 3 → remove the e's         stack: d(1)
d     → top is d → d(2)                                    stack: d(2)
b(1) b(2)  c(1) c(2) c(3) → remove the c's                 stack: d(2) b(2)
b     → b(3) → remove the b's                              stack: d(2)
d     → d(3) → remove the d's                              stack:
a(1) a(2)                                                  stack: a(2)

result: "aa"
```

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea | keep deleting `"aa"`, `"bb"`... until nothing changes | one pass with a stack |
| Time | `O(n²)` | `O(n)` |
| Space | `O(n)` | `O(n)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
fun removeDuplicatesBrute(s: String): String {
    var t = s
    var changed = true
    while (changed) {
        changed = false
        for (c in 'a'..'z') {
            val r = t.replace("$c$c", "")
            if (r != t) { t = r; changed = true }
        }
    }
    return t
}
```

A removal can create a new pair. The stack handles this in one pass because the top is always the last kept character.

#### 4. Kotlin Code

```kotlin
// Version I: remove pairs
fun removeDuplicates(s: String): String {
    val sb = StringBuilder()                                   // a StringBuilder works as a stack
    for (c in s) {
        if (sb.isNotEmpty() && sb.last() == c) sb.deleteCharAt(sb.length - 1)   // pop
        else sb.append(c)                                                         // push
    }
    return sb.toString()
}

// Version II: remove groups of k
fun removeDuplicatesK(s: String, k: Int): String {
    val stack = ArrayDeque<Pair<Char, Int>>()                  // (character, count)
    for (c in s) {
        if (stack.isNotEmpty() && stack.last().first == c) {
            val (ch, count) = stack.removeLast()
            if (count + 1 < k) stack.addLast(ch to count + 1)  // if it reaches k, the group is gone
        } else {
            stack.addLast(c to 1)
        }
    }
    return stack.joinToString("") { (ch, count) -> ch.toString().repeat(count) }
}
```

Checks: `removeDuplicates("abbaca")` → `"ca"`. `removeDuplicates("azxxzy")` → `"ay"`. `removeDuplicatesK("deeedbbcccbdaa", 3)` → `"aa"`. `removeDuplicatesK("pbbcggttciiippooaais", 2)` → `"ps"`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Version I and II | `O(n)` | `O(n)` |

Each character is pushed at most once and popped at most once.

#### 6. Common Mistakes

1. **Using `replace` in a loop** until nothing changes. It works but is `O(n²)`.
2. **Reading the top of an empty stack.** Check `isNotEmpty()`.
3. **Version I with three equal letters.** `"aaa"` becomes `"a"`, not `""`. Pairs only.
4. **Version II:** forgetting to remove the pair when the count reaches `k`.
5. **Building the result in the wrong order.** The bottom of the stack is the first character.

#### 7. Say This in the Interview

1. "Removing a pair can create a new pair, so I use a stack. The top is the last kept character."
2. "If the new character equals the top, I pop. Otherwise I push."
3. "For groups of `k` I keep a count with each character and remove the group when the count hits `k`."
4. "One pass: `O(n)` time and `O(n)` space."

#### 8. Quick Check

1. What does `"abccba"` give in Version I?
2. What does `"aaa"` give in Version II with `k = 2`?

<details>
<summary>Answers</summary>

1. `""`. Remove `cc`, then `bb`, then `aa`.
2. `"a"`. The first two `a` are removed as a pair. The third `a` stays.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1047 | [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) (Easy) | version I |
| 1209 | [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) (Medium) | version II |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) (Easy) | `#` pops |
| 1544 | [Make The String Great](https://leetcode.com/problems/make-the-string-great/) (Easy) | remove neighbours that are the same letter in different cases |
| 735 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) (Medium) | chain reactions |
