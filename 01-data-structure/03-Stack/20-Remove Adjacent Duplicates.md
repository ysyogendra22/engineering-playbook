# Remove Adjacent Duplicates

#### 1. Definition — Must Know

1. Repeatedly remove **adjacent equal characters** until none are left.
2. *Remove All Adjacent Duplicates In String* (LeetCode 1047): remove pairs. `"abbaca"` → `"ca"`.
3. *Remove All Adjacent Duplicates in String II* (LeetCode 1209): remove groups of `k` equal characters.
4. A stack does it in **one pass**: if the new character matches the top, pop; otherwise push.

#### 2. Why It Is Used — Must Know

1. Removing a pair can make **new neighbours** meet (`"abba"`: remove `bb`, then `aa`). A stack handles this automatically.
2. It is the standard example of "undo the last kept character".
3. It is a short, common easy/medium question.

#### 3. How It Works — Must Know

`s = "abbaca"`

```text
a   stack empty → push                 stack: a
b   top a != b → push                  stack: a b
b   top b == b → pop                   stack: a
a   top a == a → pop                   stack:
c   stack empty → push                 stack: c
a   top c != a → push                  stack: c a

result: "ca"
```

Version II with `k = 3`, `s = "deeedbbcccbdaa"`: the stack stores `(character, count)`. When a count reaches `k`, the whole group is popped.

```text
d(1)  e(1)  e(2)  e(3) → remove the three e's    stack: d(1)
d     → top is d(1) → d(2)                        stack: d(2)
b(1) b(2)  c(1) c(2) c(3) → remove the c's        stack: d(2) b(2)
b     → b(3) → remove the b's                     stack: d(2)
d     → d(3) → remove the d's                     stack:
a(1)  a(2)                                        stack: a(2)

result: "aa"
```

#### 4. Core Concepts — Must Know

1. **Stack of kept characters.** The top is the last kept character.
2. **Match the top → pop** (version I). **Different → push.**
3. **Version II:** keep `(char, count)` pairs. If the top char matches, increase its count; remove the pair when the count reaches `k`.
4. **New neighbours** appear after a pop. The stack makes this free, because the new top is the character before.
5. **`StringBuilder` as a stack** is the shortest form for version I.
6. **Final string** = the stack contents from bottom to top.
7. **Order of removals does not matter** for the final result in these problems.

#### 5. Algorithm — Must Know

```text
Version I:
for each character c:
    if stack is not empty and stack.top == c: stack.pop()
    else: stack.push(c)
return stack as a string

Version II (k):
for each character c:
    if stack is not empty and stack.top.char == c:
        stack.top.count++
        if stack.top.count == k: stack.pop()
    else: stack.push((c, 1))
return each (char, count) expanded
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Version I — remove pairs
fun removeDuplicates(s: String): String {
    val sb = StringBuilder()                                   // acts as the stack
    for (c in s) {
        if (sb.isNotEmpty() && sb.last() == c) sb.deleteCharAt(sb.length - 1)
        else sb.append(c)
    }
    return sb.toString()
}

// Version II — remove groups of k
fun removeDuplicatesK(s: String, k: Int): String {
    val stack = ArrayDeque<Pair<Char, Int>>()                  // (character, count)
    for (c in s) {
        if (stack.isNotEmpty() && stack.last().first == c) {
            val (ch, count) = stack.removeLast()
            if (count + 1 < k) stack.addLast(ch to count + 1)  // otherwise the group of k disappears
        } else {
            stack.addLast(c to 1)
        }
    }
    return stack.joinToString("") { (ch, count) -> ch.toString().repeat(count) }
}

// Remove duplicates in a list of numbers the same way
fun removeAdjacentEqual(nums: List<Int>): List<Int> {
    val stack = ArrayDeque<Int>()
    for (n in nums) {
        if (stack.isNotEmpty() && stack.last() == n) stack.removeLast() else stack.addLast(n)
    }
    return stack.toList()
}
```

Checks: `removeDuplicates("abbaca")` → `"ca"`. `removeDuplicates("azxxzy")` → `"ay"`. `removeDuplicatesK("deeedbbcccbdaa", 3)` → `"aa"`. `removeDuplicatesK("pbbcggttciiippooaais", 2)` → `"ps"`.

#### 7. Time & Space Complexity — Must Know

| Version | Time | Space |
|---|---:|---:|
| I (pairs) | `O(n)` | `O(n)` |
| II (groups of `k`) | `O(n)` | `O(n)` |

Each character is pushed at most once and popped at most once.

#### 8. Common Adjacent-Removal Patterns — Must Know

1. **Remove All Adjacent Duplicates In String** (LeetCode 1047).
2. **Remove All Adjacent Duplicates in String II** (LeetCode 1209).
3. **Backspace String Compare** (LeetCode 844) — `#` pops.
4. **Make The String Great** (LeetCode 1544) — remove adjacent letters that are the same letter in different cases.
5. **Remove Outermost Parentheses** (LeetCode 1021), **Valid Parentheses** — pair removal.
6. **Asteroid Collision** (LeetCode 735) — collisions as removals.
7. **Reducing a sequence of events** (e.g. cancel a "like" followed by "unlike") in app logs.

#### 9. Edge Cases / Common Mistakes

1. Doing repeated passes with `replace` until nothing changes. It is `O(n²)`.
2. Not checking `isNotEmpty()` before reading the top.
3. Version II: pushing `(c, 1)` when the top matches, or forgetting to check `count == k`.
4. Version II: `k = 1` removes everything.
5. Pairs only: `"aaa"` → `"a"` (the third `a` stays), not `""`.
6. Case-sensitive vs case-insensitive matching (LeetCode 1544).
7. Empty input.
8. Building the final string in the wrong order (the stack's bottom is the first character).

#### 10. When to Use / When Not to Use

**Use when:**

1. Removals can chain (new neighbours become adjacent).

**Avoid when:**

1. You only remove duplicates globally (any position). Use a set.
2. You only compare neighbours without removing. A simple loop is enough.

#### 11. Related Topics

1. Valid / Balanced Parentheses
2. Expression / String Processing with Stack
3. Asteroid Collision
4. HashSet (global duplicate removal) (`01-data-structure/06-HashSet`)

#### 12. Interview Must Remember

1. **If the new character equals the top, pop. Otherwise push.**
2. For groups of `k`, store `(char, count)` and pop when the count reaches `k`.
3. One pass, `O(n)`.
4. Chain reactions are handled by the stack automatically.
