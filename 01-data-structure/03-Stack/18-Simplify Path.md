# Simplify Path

#### 1. What Is It?

You get an **absolute file path** (it starts with `/`). Return its **simplest form**.

Rules:

| Part | Meaning | What to do |
|---|---|---|
| `.` | the current folder | ignore it |
| `..` | go up one folder | remove the last folder (if there is one) |
| `//` (empty part) | a repeated slash | ignore it |
| anything else | a folder name | keep it |

The result must start with `/`, must not end with `/` (except the root itself), and must not contain `.` or `..`.

```text
"/home//foo/"        → "/home/foo"
"/a/./b/../../c/"    → "/c"
"/../"               → "/"        (you cannot go above the root)
"/..."               → "/..."     ("..." is a normal folder name)
```

This is *Simplify Path* (LeetCode 71). The folders you are currently inside form a **stack**: going into a folder is a push, and `..` is a pop.

#### 2. How It Works

`path = "/a/./b/../../c/"`

Split by `/`: `["", "a", ".", "b", "..", "..", "c", ""]`

```text
""   skip (empty)                 stack: []
"a"  push                         stack: [a]
"."  skip                         stack: [a]
"b"  push                         stack: [a, b]
".." pop                          stack: [a]
".." pop                          stack: []
"c"  push                         stack: [c]
""   skip                         stack: [c]

result: "/" + "c" = "/c"
```

#### 3. Kotlin Code

```kotlin
fun simplifyPath(path: String): String {
    val stack = ArrayDeque<String>()
    for (part in path.split("/")) {
        when (part) {
            "", "." -> { }                               // ignore
            ".." -> stack.removeLastOrNull()             // go up; nothing happens at the root
            else -> stack.addLast(part)                  // a folder name
        }
    }
    return "/" + stack.joinToString("/")                 // empty stack gives "/"
}
```

Checks: `simplifyPath("/home/")` → `"/home"`. `simplifyPath("/../")` → `"/"`. `simplifyPath("/home//foo/")` → `"/home/foo"`. `simplifyPath("/a/./b/../../c/")` → `"/c"`. `simplifyPath("/.../a/../b/c/../d/./")` → `"/.../b/d"`.

Same idea in Android: the **back stack** of screens. Opening a screen is a push, pressing back is a pop.

```kotlin
class Navigator {
    private val backStack = ArrayDeque<String>()
    fun open(screen: String) { backStack.addLast(screen) }
    fun back(): String? = backStack.removeLastOrNull()
    fun current(): String? = backStack.lastOrNull()
}
```

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Split + one pass | `O(n)` | `O(n)` |

#### 5. Common Mistakes

1. **Forgetting to skip empty parts.** `split("/")` returns `""` for a leading slash and for `//`.
2. **Popping an empty stack on `..`.** Use `removeLastOrNull()`.
3. **Returning `""` for the root.** It must be `"/"`.
4. **Treating `"..."` as `..`.** It is a normal folder name.
5. **A trailing `/`** in the result.

#### 6. Say This in the Interview

1. "Folders I am inside form a stack. A name is a push, `..` is a pop, `.` and empty parts are skipped."
2. "`..` at the root does nothing."
3. "Time `O(n)`, space `O(n)`."

#### 7. Quick Check

1. What does `"/a/../.."` give?
2. What does `"/a/b/c/../.."` give?

<details>
<summary>Answers</summary>

1. `"/"`. The first `..` removes `a`. The second `..` is at the root and does nothing.
2. `"/a"`. The two `..` remove `c` and `b`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) (Medium) | this note |
| 1598 | [Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/) (Easy) | only the depth counter is needed |
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/) (Medium) | back and forward stacks |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) (Easy) | pop to undo |
