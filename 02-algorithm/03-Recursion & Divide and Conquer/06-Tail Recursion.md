# Tail Recursion

#### 1. Definition — Must Know

1. A recursive call is a **tail call** when it is the very last action in the function — nothing happens after it returns.
2. **Tail recursion** is a recursive function where every recursive call is a tail call.

#### 2. Why It Is Used — Must Know

1. A tail-recursive function can, in principle, be turned into a plain loop by the compiler, using O(1) stack space instead of O(n).
2. It matters for functions that could recurse very deep — a tail-recursive version avoids a stack overflow that a normal recursive version would hit.

#### 3. How It Works — Must Know

Not tail recursive — there is work left to do *after* the recursive call returns:

```kotlin
fun factorial(n: Int): Int {
    if (n <= 1) return 1
    return n * factorial(n - 1)   // multiplication happens AFTER the call returns
}
```

Tail recursive — the recursive call is the last thing that happens, with no pending work:

```kotlin
fun factorialTail(n: Int, accumulator: Int = 1): Int {
    if (n <= 1) return accumulator
    return factorialTail(n - 1, n * accumulator)  // nothing left to do after this call
}
```

The trick is carrying the running result forward as a parameter (the **accumulator**), instead of computing it on the way back up.

#### 4. Algorithm — Must Know

```text
Not tail recursive:  return combine(n, f(n - 1))     ← work after the call
Tail recursive:      return f(n - 1, updatedState)   ← nothing after the call
```

#### 5. Kotlin Implementation — Must Know

Kotlin has a `tailrec` keyword. The compiler checks that the function really is tail recursive, and if so, rewrites it into a loop for you:

```kotlin
tailrec fun factorialTail(n: Int, accumulator: Int = 1): Int {
    if (n <= 1) return accumulator
    return factorialTail(n - 1, n * accumulator)
}
```

If the function is not actually tail recursive, the compiler gives a warning that `tailrec` had no effect.

#### 6. Complexity — Must Know

| Version | Space |
|---|---|
| Plain recursive `factorial` | O(n) — one stack frame per call |
| `tailrec` `factorialTail` | O(1) — compiled into a loop, no growing stack |

Time stays O(n) either way. Only the space changes.

#### 7. Common Mistakes — Must Know

1. Assuming Kotlin optimises *all* recursion automatically — it only does so for functions marked `tailrec` that genuinely qualify.
2. Adding `tailrec` to a function that isn't actually tail recursive (for example, `n * factorial(n - 1)`) and not noticing the compiler's warning that it did nothing.
3. Forgetting that a function with two recursive calls (like naive Fibonacci) can never be simple tail recursion, since one call's result still needs combining with the other.

#### 8. Related Topics

1. `1` Base Case & Recursive Case — the accumulator still needs a correct base case
2. `2` The Call Stack & Space Complexity — what tail recursion avoids growing
3. `7` Recursion to Iteration — the general technique when `tailrec` doesn't apply

#### 9. Interview Must Remember

1. Tail call = the recursive call is the **last** thing the function does, with no leftover work.
2. Kotlin's `tailrec` turns a true tail-recursive function into a loop — O(1) space instead of O(n).
3. The usual trick to make a function tail recursive is passing the running result as an **accumulator** parameter.
