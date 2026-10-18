# Bitwise Trie / Binary Trie

#### 1. Definition — Must Know

1. A **bitwise trie** (binary trie) stores **numbers**, one **bit** per level.
2. Every node has at most **two children**: bit `0` and bit `1`.
3. A number is inserted from its **most significant bit** down to the least significant bit, so every number of the same bit-length has a path of the same length.

#### 2. Why It Is Used — Must Know

1. It lets you search by the *bit pattern* of numbers, not by value comparison.
2. Its best-known use is the **maximum XOR** problem: for a number, find the stored number that gives the largest XOR. The Trie answers it by choosing, at every bit, the opposite bit when it exists.
3. Each operation costs the number of bits (for example 31), which is a constant. That is why it is faster than comparing against every stored number.

#### 3. How It Works — Must Know

Store `5` (`101`) and `3` (`011`). Three bits are shown to keep the picture small. Real code uses 31 bits for non-negative `Int` values.

```text
root
├── 0 → 1 → 1*     ← 011 = 3
└── 1 → 0 → 1*     ← 101 = 5
```

Reading a number's bits from the top and following the matching child gives its path.

Idea behind maximum XOR for `x = 5` (`101`): at each level, prefer the child with the **opposite** bit, because `1 XOR 0 = 1` makes the result larger.

```text
x = 101
level 1: x has 1 → prefer 0 → exists (3 starts with 0)   → this bit of the XOR is 1
level 2: x has 0 → prefer 1 → exists (3 has 1)           → this bit of the XOR is 1
level 3: x has 1 → prefer 0 → 3 has 1, so take 1         → this bit of the XOR is 0
Best partner = 011 = 3, XOR = 110 = 6
```

#### 4. Core Concepts — Must Know

1. **Two children only:** index `0` and index `1`.
2. **Fixed depth:** every number uses the same number of bits (for example bits 30 down to 0).
3. **Bit extraction:** `(num shr bit) and 1`.
4. **Greedy choice for XOR:** take the opposite bit when possible, otherwise the same bit.
5. **Negative numbers:** they use bit 31 as the sign. Either handle that bit as well or restrict the input to non-negative values.

#### 5. Algorithm — Must Know

```text
insert(num):
    node = root
    for bit from 30 down to 0:
        b = (num >> bit) & 1
        if node has no child b: create it
        node = child b

contains(num):
    node = root
    for bit from 30 down to 0:
        b = (num >> bit) & 1
        if node has no child b: return false
        node = child b
    return true
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class BinaryTrieNode {
    val children = arrayOfNulls<BinaryTrieNode>(2)
}

class BinaryTrie {

    private val root = BinaryTrieNode()

    fun insert(num: Int) {
        var node = root
        for (bit in 30 downTo 0) {
            val b = (num shr bit) and 1
            val next = node.children[b] ?: BinaryTrieNode().also { node.children[b] = it }
            node = next
        }
    }

    fun contains(num: Int): Boolean {
        var node = root
        for (bit in 30 downTo 0) {
            val b = (num shr bit) and 1
            node = node.children[b] ?: return false
        }
        return true
    }
}
```

The bit operations used here are explained in `02-algorithm/09-Bit Manipulation`.

#### 7. Time & Space Complexity — Must Know

`B` = number of bits (31 for non-negative `Int`).

| Operation | Time |
|---|---:|
| `insert` | `O(B)` |
| `contains` | `O(B)` |
| Maximum XOR for one number | `O(B)` |
| Space | `O(N · B)` nodes in the worst case |

Because `B` is a constant, each operation is effectively `O(1)`. Building the Trie for `N` numbers is `O(N · B)`.

#### 8. Common Binary Trie Patterns — Must Know

1. **Maximum XOR of Two Numbers in an Array** (LeetCode 421) — insert every number, then query each number for its best XOR partner.
2. Maximum XOR with a query value.
3. Find a number that matches the most leading bits of a given number.
4. Count numbers that share a bit-prefix (add counts to the nodes, as in "Counting Words / Prefixes").

#### 9. Edge Cases / Common Mistakes

1. Using too few bits, so large numbers collide or get cut off.
2. Handling bits from the **least** significant end. The Trie needs the **most** significant bit first.
3. Negative numbers and the sign bit.
4. Querying an empty Trie, where there is no child to follow.
5. Forgetting that a child may be missing when you prefer the opposite bit. Fall back to the same bit.
6. `node` captured inside `also` while it is being reassigned. Compute `next` first, as above.

#### 10. When to Use / When Not to Use

**Use when:**

1. The problem is about XOR, bit prefixes, or "closest by bits".
2. You must query many numbers against a changing set.

**Avoid when:**

1. A simple loop over all pairs is fast enough for the given size.
2. A `HashSet` of prefixes solves the task more simply (this alternative exists for maximum XOR).

#### 11. Related Topics

1. TrieNode Structure
2. Counting Words / Prefixes
3. Bit Manipulation (`02-algorithm/09-Bit Manipulation`): shifts, masks, and XOR
4. Greedy choice (`02-algorithm/04-Greedy Algorithms`)

#### 12. Interview Must Remember

1. Binary trie: **two children, one bit per level, most significant bit first.**
2. Maximum XOR = at each level, take the **opposite bit** if it exists.
3. Each operation is `O(B)`, which is a constant for `Int`.
4. State how you handle negative numbers and how many bits you use.
