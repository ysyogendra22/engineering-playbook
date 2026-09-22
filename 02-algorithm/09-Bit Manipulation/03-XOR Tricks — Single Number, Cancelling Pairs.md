# XOR Tricks — Single Number, Cancelling Pairs

#### 1. Definition — Must Know

XOR has a special property that makes it useful far beyond a basic bitwise operation: **`x XOR x = 0`** (anything XORed with itself cancels to zero), and **`x XOR 0 = x`** (XOR with zero does nothing). Combined, this means **pairs of equal numbers cancel out** when XORed together, leaving only whatever doesn't have a pair.

#### 2. Why It Is Used — Must Know

This single property solves a small, well-known family of problems in O(n) time and O(1) space — no hash set or extra memory needed, which is exactly what makes it a favourite "clever trick" interview question.

#### 3. How It Works — Must Know

**Single Number**: every number in an array appears twice, except one — find it.

```text
[4, 1, 2, 1, 2]

XOR all of them together:
4 xor 1 xor 2 xor 1 xor 2
= 4 xor (1 xor 1) xor (2 xor 2)      ← XOR is commutative/associative, so pairs group together
= 4 xor 0 xor 0
= 4

Answer: 4  — every paired number cancelled to 0, leaving only the unpaired one.
```

**Swapping two numbers without a temp variable** (a related classic trick):

```text
a = a xor b
b = a xor b   // = (original a xor b) xor b = original a
a = a xor b   // = (original a xor b) xor (original a) = original b
```

#### 4. Algorithm — Must Know

```text
function findSingleNumber(nums):
    result = 0
    for num in nums:
        result = result xor num
    return result
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun singleNumber(nums: IntArray): Int {
    var result = 0
    for (num in nums) {
        result = result xor num
    }
    return result
}
```

#### 6. Complexity — Must Know

| | Time | Space |
|---|---|---|
| XOR trick | O(n) | O(1) |
| Alternative: HashMap counting | O(n) | O(n) |

Same time complexity as the hash map approach, but **no extra memory** — this is the whole reason the trick is worth knowing.

#### 7. Common Mistakes — Must Know

1. Trying to apply this trick when a number could appear **three or more times**, or when there could be **two** unpaired numbers — the plain XOR trick only works for the exact "everything paired except one" shape (variants exist for these harder cases, but they're a different technique).
2. Forgetting that XOR is both **commutative** (order doesn't matter) and **associative** (grouping doesn't matter) — this is *why* the pairs can cancel regardless of where they appear in the array.
3. Overcomplicating a problem that's really just "find the odd one out" with sorting or a hash set, when XOR solves it more simply.

#### 8. Related Topics

1. `1` AND, OR, XOR, NOT, Left Shift, Right Shift — the base operation
2. `20` More Patterns to Know (in `03-leetcode-patterns`) — where Single Number is listed as a classic problem
3. `9` Bit Manipulation (this folder's own index) — other tricks in the same family

#### 9. Interview Must Remember

1. **`x XOR x = 0`, `x XOR 0 = x`** — the whole trick in two facts.
2. Recognise the shape: **"everything appears twice/in pairs except one thing"** is the signal for this trick.
3. O(n) time, O(1) space — a strong answer specifically because it beats the "obvious" hash-map solution on space.
