# Iterating All Subsets of a Bitmask

#### 1. Definition — Must Know

Beyond iterating every subset of `n` items (topic 6), there's a related, less obvious technique: iterating every **sub-mask** of one specific mask — every subset of the items that mask represents, not of the whole universe of items.

#### 2. Why It Is Used — Must Know

This shows up in more advanced bitmask DP, where a transition needs to try "every way to split this particular subset into two smaller pieces" — the classic interval DP idea (`05-Dynamic Programming/12`), applied to sets instead of ranges.

#### 3. How It Works — Must Know

```text
mask = 0b101   (represents the subset {item 0, item 2})

All sub-masks of 0b101 (every subset of {item 0, item 2}):
  0b101  → {item 0, item 2}
  0b100  → {item 2}
  0b001  → {item 0}
  0b000  → {}

The trick to generate them, without checking every possible mask from 0
to mask (which would be wasteful): start at `mask` itself, and repeatedly
do `submask = (submask - 1) and mask` — this always jumps directly to the
next smaller sub-mask, skipping anything that isn't actually a subset.
```

#### 4. Algorithm — Must Know

```text
submask = mask
while true:
    process(submask)
    if submask == 0: break
    submask = (submask - 1) and mask
```

The `(submask - 1) and mask` step is the one piece of "magic" here: subtracting 1 borrows through the lowest set bits (same idea as in Brian Kernighan's trick, topic 4), and ANDing with `mask` clamps the result back down to only bits that `mask` actually has.

#### 5. Kotlin Implementation — Must Know

```kotlin
fun allSubmasks(mask: Int): List<Int> {
    val result = mutableListOf<Int>()
    var submask = mask
    while (true) {
        result.add(submask)
        if (submask == 0) break
        submask = (submask - 1) and mask
    }
    return result
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Iterating all sub-masks of ONE mask with `k` set bits | O(2ᵏ) — exactly the number of subsets of those k items, no wasted work |
| Iterating all sub-masks of ALL masks (a common DP pattern) | O(3ⁿ) total, across all masks — a known, sometimes-asked result, not obvious at a glance |

#### 7. Common Mistakes — Must Know

1. Iterating from `0` to `mask` and checking `(candidate and mask) == candidate` for each — this works, but is far slower (checks many non-sub-masks) than the `(submask - 1) and mask` trick.
2. Forgetting the `submask == 0` termination check — without it, `(0 - 1) and mask` would produce `mask` again, looping forever.
3. Treating this as the same thing as "iterate all subsets of n items" (topic 6) — that iterates subsets of the **whole universe**; this iterates subsets of **one specific mask**.

#### 8. Related Topics

1. `6` Bitmask — Representing a Set of Up to ~20 Items — the simpler, whole-universe version
2. `4` Counting Set Bits — bitCount and Brian Kernighan's Trick — the related `n and (n-1)` idea
3. `12` Interval DP & Bitmask DP — Names Only (in `05-Dynamic Programming`) — where this technique gets used in a DP transition

#### 9. Interview Must Remember

1. To walk every sub-mask of `mask`: start at `mask`, repeat `submask = (submask - 1) and mask`, stop after processing `0`.
2. This is a more advanced, less commonly needed trick than the basic bitmask operations (topics 1–6) — know it exists, reach for it only when the problem specifically needs "all subsets of this particular subset".
3. Don't confuse it with iterating all subsets of the full item universe (topic 6) — different scope, different loop.
