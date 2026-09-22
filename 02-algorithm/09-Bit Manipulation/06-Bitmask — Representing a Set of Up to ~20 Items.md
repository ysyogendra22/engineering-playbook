# Bitmask — Representing a Set of Up to ~20 Items

#### 1. Definition — Must Know

A **bitmask** uses the individual bits of an integer to represent membership in a set: bit `i` is 1 if item `i` is "in", and 0 if it's "out". A 32-bit integer can represent a subset of up to 32 items this way — in practice, this is mainly used for sets of up to about 20 items, since `2^20` (roughly a million) is already the practical limit for exploring every possible subset.

#### 2. Why It Is Used — Must Know

1. It turns "is item i selected?" into an O(1) bit check, and "try every possible subset" into a simple loop from `0` to `2^n - 1`.
2. It's the state representation behind bitmask DP (`05-Dynamic Programming/12`) and small Travelling-Salesman-style problems (`06-Backtracking & Branch and Bound/08`).

#### 3. How It Works — Must Know

```text
Items: [apple, banana, cherry]     (3 items, indices 0, 1, 2)

mask = 0b101   means: item 0 (apple) IS included,
                       item 1 (banana) is NOT included,
                       item 2 (cherry) IS included
     → represents the subset {apple, cherry}

All possible subsets of 3 items = all masks from 0b000 to 0b111 (0 to 7),
i.e. all integers from 0 to 2³ - 1.

mask = 0b000 → {}                    mask = 0b100 → {cherry}
mask = 0b001 → {apple}               mask = 0b101 → {apple, cherry}
mask = 0b010 → {banana}              mask = 0b110 → {banana, cherry}
mask = 0b011 → {apple, banana}       mask = 0b111 → {apple, banana, cherry}
```

#### 4. Algorithm — Must Know

```text
Check if item i is in the mask:      (mask shr i) and 1 == 1     (topic 2)
Add item i to the mask:              mask or (1 shl i)            (topic 2)
Remove item i from the mask:         mask and (1 shl i).inv()     (topic 2)
Try every possible subset:           for mask in 0 until (1 shl n)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun subsetFromMask(items: List<String>, mask: Int): List<String> {
    val result = mutableListOf<String>()
    for (i in items.indices) {
        if ((mask shr i) and 1 == 1) {
            result.add(items[i])
        }
    }
    return result
}

fun allSubsets(items: List<String>): List<List<String>> {
    val n = items.size
    val result = mutableListOf<List<String>>()
    for (mask in 0 until (1 shl n)) {
        result.add(subsetFromMask(items, mask))
    }
    return result
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Checking/setting/clearing one item | O(1) |
| Trying every subset of n items | O(2ⁿ) masks, O(n) work per mask to read it → O(n × 2ⁿ) total |

This exponential cost is exactly why bitmask techniques are limited to small `n` — usually up to about 20.

#### 7. Common Mistakes — Must Know

1. Trying to use a bitmask for more than about 20-25 items — `2^30` and beyond becomes far too slow to enumerate, and even storage of `dp[mask]` arrays becomes impractical.
2. Off-by-one between "item index" and "bit position" — item 0 maps to bit 0, item 1 to bit 1, and so on; keep this mapping consistent.
3. Using a bitmask when a plain `Set` or `BooleanArray` would be just as clear and the input size doesn't actually need the speed — bitmasks are an optimisation, not the default choice for every "track a subset" problem.

#### 8. Related Topics

1. `2` Check, Set, Clear, and Toggle a Bit — the operations bitmasks are built from
2. `7` Iterating All Subsets of a Bitmask — the next layer up
3. `12` Interval DP & Bitmask DP — Names Only (in `05-Dynamic Programming`) — where bitmasks become part of a DP state

#### 9. Interview Must Remember

1. Bitmask = **an integer where bit `i` means "is item `i` in the set?"**
2. Looping `mask` from `0` to `2^n - 1` tries every possible subset — a common template for small-n brute force.
3. This only stays fast for **small n** (roughly ≤ 20) — always mention that limit.
