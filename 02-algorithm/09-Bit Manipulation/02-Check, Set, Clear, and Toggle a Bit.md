# Check, Set, Clear, and Toggle a Bit

#### 1. Definition — Must Know

Four small, extremely common operations on a single bit at position `i` of a number, all built from the basics in topic 1:

1. **Check** — is bit `i` a 1 or a 0?
2. **Set** — force bit `i` to 1.
3. **Clear** — force bit `i` to 0.
4. **Toggle** — flip bit `i` (1 becomes 0, 0 becomes 1).

#### 2. Why It Is Used — Must Know

These four operations are the actual "verbs" used whenever a number is treated as a set of flags — permissions, feature flags, visited-state tracking, or a bitmask representing a subset (`06-Bitmask`).

#### 3. How It Works — Must Know

```text
n = 0b1010   (bit 1 and bit 3 are set, counting from bit 0 on the right)

Check bit 1:   (n shr 1) and 1  →  (0b0101) and 1  →  1     (bit 1 IS set)
Set bit 0:     n or (1 shl 0)   →  0b1010 or 0b0001 → 0b1011
Clear bit 1:   n and (1 shl 1).inv()  →  0b1010 and ...11111101 → 0b1000
Toggle bit 3:  n xor (1 shl 3)  →  0b1010 xor 0b1000 → 0b0010
```

The pattern in every case: build a "mask" with a 1 in exactly the position you care about (`1 shl i`), then combine it with the number using the right operation.

#### 4. Algorithm — Must Know

```text
check(n, i)  = (n shr i) and 1
set(n, i)    = n or (1 shl i)
clear(n, i)  = n and (1 shl i).inv()
toggle(n, i) = n xor (1 shl i)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun checkBit(n: Int, i: Int): Boolean = (n shr i) and 1 == 1
fun setBit(n: Int, i: Int): Int = n or (1 shl i)
fun clearBit(n: Int, i: Int): Int = n and (1 shl i).inv()
fun toggleBit(n: Int, i: Int): Int = n xor (1 shl i)
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Each operation | O(1) |

#### 7. Common Mistakes — Must Know

1. Forgetting to build the mask first (`1 shl i`) and accidentally operating on the wrong bit or the whole number.
2. Using `or` when you meant `and` (or the reverse) — set uses `or`, clear uses `and` with an inverted mask; mixing them up silently does the wrong thing.
3. Off-by-one on bit position — bit 0 is the **rightmost** (least significant) bit, not the leftmost.

#### 8. Related Topics

1. `1` AND, OR, XOR, NOT, Left Shift, Right Shift — the operations these build on
2. `6` Bitmask — Representing a Set of Up to ~20 Items — where these four operations get used together
3. `7` Iterating All Subsets of a Bitmask

#### 9. Interview Must Remember

1. **Check** = shift and AND with 1. **Set** = OR with the mask. **Clear** = AND with the inverted mask. **Toggle** = XOR with the mask.
2. All four are O(1) — this is why bit tricks are attractive whenever a small, fixed-size set of flags is involved.
3. Bit 0 is the rightmost bit — always double-check which end you're counting from.
