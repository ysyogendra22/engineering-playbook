# Base Case & Recursive Case

#### 1. Definition — Must Know

1. Every recursive function has two parts: a **base case** that stops the recursion, and a **recursive case** that calls the function again on a smaller input.
2. Without a base case, the function keeps calling itself forever and crashes with a stack overflow.

#### 2. Why It Is Used — Must Know

1. It lets you describe a solution in terms of a smaller version of the same problem, instead of writing out every step by hand.
2. Many problems are naturally recursive: trees, nested folders, "do this, then do the rest".

#### 3. How It Works — Must Know

Example: factorial of 5.

```text
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0)   ← base case, factorial(0) = 1
= 120
```

1. `factorial(0) = 1` is the base case — it needs no further calls.
2. `factorial(n) = n * factorial(n - 1)` is the recursive case — it calls itself on a smaller input, `n - 1`.

#### 4. Algorithm — Must Know

```text
function f(n):
    if n meets the base case:
        return the base answer directly
    return combine(n, f(smaller n))
```

1. Always check the base case first, before doing any recursive work.
2. Always call the function on an input that is strictly smaller, so it eventually reaches the base case.

#### 5. Kotlin Implementation — Must Know

```kotlin
fun factorial(n: Int): Int {
    if (n <= 1) return 1          // base case
    return n * factorial(n - 1)   // recursive case
}
```

#### 6. Complexity — Must Know

| Case | Time | Space |
|---|---|---|
| `factorial(n)` | O(n) | O(n) — one stack frame per call |

The time is one unit of work per call. The space is the depth of the call stack (topic 2).

#### 7. Common Mistakes — Must Know

1. Forgetting the base case, so the function never stops.
2. A base case that is never reached (for example, shrinking by 2 but checking only for an odd base case).
3. Calling the function again on the same input instead of a smaller one.
4. Writing the base case after code that already assumes a smaller input exists.

#### 8. Related Topics

1. `2` The Call Stack & Space Complexity — what the base case protects you from
2. `3` Divide and Conquer — recursion with more than one recursive call
3. `8` Memoization — the Bridge to Dynamic Programming

#### 9. Interview Must Remember

1. **Two parts, always:** a base case that stops it, and a recursive case that shrinks the problem.
2. State the base case **before** you write the recursive case.
3. Check: does every recursive call move strictly closer to the base case?
