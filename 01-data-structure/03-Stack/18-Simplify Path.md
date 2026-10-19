# Simplify Path

#### 1. Definition — Must Know

1. Given an absolute Unix-style file path, return its **simplified canonical form**.
2. Rules:
   - `.` means "the current folder" → ignore it.
   - `..` means "go up one folder" → remove the last folder (if any).
   - Multiple slashes (`//`) count as one slash.
   - The result starts with `/`, has no trailing `/`, and has no `.` or `..`.
3. It is *Simplify Path* (LeetCode 71). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. "Go back one level" is a pop. The folders you are inside are a stack.
2. It is a short, clean stack question.
3. In apps: file managers, deep links and URL path normalisation, navigation back stacks.

#### 3. How It Works — Must Know

`path = "/a/./b/../../c/"`

Split by `/` into parts: `["", "a", ".", "b", "..", "..", "c", ""]`.

```text
""   skip (empty part)                  stack: []
a    push                               stack: [a]
.    skip                               stack: [a]
b    push                               stack: [a, b]
..   pop                                stack: [a]
..   pop                                stack: []
c    push                               stack: [c]
""   skip                               stack: [c]

result: "/" + "c" = "/c"
```

More cases:

```text
"/home//foo/"     → "/home/foo"
"/../"            → "/"           (.. at the root does nothing)
"/a/b/c/../.."    → "/a"
"/..."            → "/..."        ("..." is a normal folder name)
```

#### 4. Core Concepts — Must Know

1. **Split on `/`** and process each part.
2. **Skip** `""` (from `//` or leading/trailing slash) and `"."`.
3. **`..` pops** the stack if it is not empty. At the root, it does nothing.
4. **Anything else is a folder name → push.**
5. **Join** the stack with `/` and add a leading `/`. An empty stack gives `"/"`.
6. **`...` or `.hidden` are valid names**, not special.
7. **Why a stack:** the last folder entered is the first one removed by `..`.

#### 5. Algorithm — Must Know

```text
stack = empty
for part in path.split("/"):
    "" or "."  → skip
    ".."       → pop if the stack is not empty
    otherwise  → push part
return "/" + stack joined by "/"
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun simplifyPath(path: String): String {
    val stack = ArrayDeque<String>()
    for (part in path.split("/")) {
        when (part) {
            "", "." -> { /* skip */ }
            ".." -> stack.removeLastOrNull()               // does nothing at the root
            else -> stack.addLast(part)
        }
    }
    return "/" + stack.joinToString("/")
}

// Android style: navigate a back stack of screens
class Navigator {
    private val backStack = ArrayDeque<String>()

    fun open(screen: String) { backStack.addLast(screen) }
    fun back(): String? = backStack.removeLastOrNull()
    fun current(): String? = backStack.lastOrNull()
}
```

Checks: `simplifyPath("/home/")` → `"/home"`. `simplifyPath("/../")` → `"/"`. `simplifyPath("/home//foo/")` → `"/home/foo"`. `simplifyPath("/a/./b/../../c/")` → `"/c"`. `simplifyPath("/.../a/../b/c/../d/./")` → `"/.../b/d"`.

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---:|
| Time | `O(n)` — split and one pass over the parts |
| Space | `O(n)` — the parts and the stack |

#### 8. Common Path / Navigation Patterns — Must Know

1. **Simplify Path** (LeetCode 71).
2. **Crawler Log Folder** (LeetCode 1598) — just a counter of the depth.
3. **Browser History** (LeetCode 1472) — back and forward with two stacks or one array.
4. **Design File System** (LeetCode 1166) — a trie or a map.
5. **Resolve relative URLs** (`../images/a.png` against a base).
6. **Undo/back navigation** — each screen is pushed; back pops.
7. **Android:** `NavController` back stack, `FragmentManager` back stack.

#### 9. Edge Cases / Common Mistakes

1. Forgetting to skip empty parts from `//` and the leading `/` (the split gives `""`).
2. Popping from an empty stack on `..` at the root (use `removeLastOrNull()`).
3. Returning `""` for the root instead of `"/"`.
4. Leaving a trailing `/`.
5. Treating `"..."` as `..`.
6. Splitting with `trim('/')` first and then forgetting that empty parts still appear between double slashes.
7. Relative paths: this version assumes an **absolute** path starting with `/`.
8. Joining without the leading `/`.

#### 10. When to Use / When Not to Use

**Use when:**

1. You normalise a path-like string where `..` undoes the last step.

**Avoid when:**

1. Symbolic links or the real file system matter. Use the OS or `File.canonicalPath` / `Path.normalize()`.

#### 11. Related Topics

1. Stack Operations & Complexity
2. Expression / String Processing with Stack
3. Remove Adjacent Duplicates
4. Trie (`01-data-structure/09-Trie`)

#### 12. Interview Must Remember

1. **Split by `/`; skip `""` and `.`; `..` pops; names push; join with `/` and a leading `/`.**
2. `..` at the root does nothing.
3. Empty stack → `"/"`.
4. `O(n)` time and space.
