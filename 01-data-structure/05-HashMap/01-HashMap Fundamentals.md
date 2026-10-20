# HashMap Fundamentals

> Start here. HashMap is the most used data structure in coding interviews. Read this note slowly once.

#### 1. What Is a HashMap?

A **HashMap** stores **key → value** pairs, and finds a value by its key **very fast**.

Think of a phone book: you look up a **name** (the key) and get a **number** (the value). You do not read every page.

Rules:

- Each **key is unique**. Adding a value under an existing key **replaces** the old value.
- Values can repeat.
- A HashMap has **no index** and **no guaranteed order**.

#### 2. Words You Must Know

| Word | Meaning |
|---|---|
| **Key** | what you search with |
| **Value** | the data stored for that key |
| **Put** | add or replace a pair |
| **Get** | find the value for a key |
| **Hash code** | a number made from the key. It decides where the pair is stored. |
| **Bucket** | a slot in the table where pairs are stored |
| **`O(1)`** | the work stays the same however big the map is (fast) |

#### 3. How It Works

```text
key → hashCode() → bucket number → look inside that bucket, compare keys with equals()

put("apple", 3):  hash → bucket 5 → empty → store ("apple" → 3)
put("pear", 7):   hash → bucket 9 → empty → store ("pear" → 7)
get("apple"):     hash → bucket 5 → key matches → return 3
put("apple", 9):  hash → bucket 5 → key matches → replace 3 with 9
```

The hash code jumps straight to the right bucket, so you never scan all the pairs. That is why `get` and `put` are `O(1)` on average.

Java's `HashMap` starts with 16 buckets and doubles them when it is 75% full.

#### 4. Kotlin Code

```kotlin
val map = HashMap<String, Int>()          // empty map: String keys, Int values

map["apple"] = 3                           // put
map["apple"] = 9                           // same key: the value is replaced
println(map["apple"])                      // 9
println(map["kiwi"])                       // null: the key is missing
println(map.getOrDefault("kiwi", 0))       // 0: a default for a missing key
println("apple" in map)                    // true: does the key exist?
map.remove("apple")
println(map.size)                          // 0

val ages = hashMapOf("Asha" to 30, "Ben" to 25)
for ((name, age) in ages) println("$name is $age")     // the order is not guaranteed
```

The most common use, **counting**:

```kotlin
val counts = HashMap<Char, Int>()
for (c in "banana") counts[c] = (counts[c] ?: 0) + 1
println(counts)                            // {a=3, b=1, n=2}
```

`map[key]` gives `Int?` (nullable), so `counts[c]++` does not compile. Write `(counts[c] ?: 0) + 1`.

#### 5. Which Map to Use

| Type | Order | Speed | Use when |
|---|---|---|---|
| `HashMap` / `hashMapOf()` | none | `O(1)` | most interview problems |
| `LinkedHashMap` / `mutableMapOf()` | insertion order | `O(1)` | you need the original order |
| `TreeMap` / `sortedMapOf()` | sorted by key | `O(log n)` | you need sorted keys, floor/ceiling |
| `mapOf()` | insertion order | `O(1)` | read-only |

Note: `mutableMapOf()` gives a `LinkedHashMap`, not a plain `HashMap`.

#### 6. How to Spot a HashMap Problem

| If the question says... | Think... |
|---|---|
| "how many times", "most frequent" | count with a map |
| "find two numbers that add to...", "have I seen this?" | store what you saw |
| "group by...", "anagrams" | `key → list` |
| "subarray with sum k" | prefix sum + map |
| "longest substring with..." | window + count map |
| "cache", "least recently used" | map + linked list |
| the brute force has two nested loops | try to replace one loop with a map lookup |

#### 7. Complexity

| Action | Average time |
|---|---|
| `put`, `get`, `remove`, `containsKey` | `O(1)` |
| `containsValue` | `O(n)` |
| Memory for `n` pairs | `O(n)` |

Say "`O(1)` on average". In the very worst case (many keys in one bucket) it is slower, but modern Java handles that well.

#### 8. Common Mistakes

1. **Forgetting that `map[key]` can be `null`.** Use `?: 0`, `getOrDefault` or `getOrPut`.
2. **Writing `map[key]++`.** It does not compile. Use `map[key] = (map[key] ?: 0) + 1`.
3. **Expecting insertion order** from a `HashMap`. Use `LinkedHashMap` for that.
4. **Using an array as a key.** Arrays compare by reference, so lookups fail. Use a `List`, `String` or `data class`.
5. **Changing a key** after putting it in the map.

#### 9. Say This in the Interview

1. "Brute force is `O(n²)`. With a HashMap I can look up in `O(1)`, so I get `O(n)` time and `O(n)` space."
2. "My key is ... and my value is ..." (always say this out loud).
3. "I handle the missing key with a default."

#### 10. Quick Check

1. What does `map["x"]` return if `"x"` is not in the map?
2. What happens if you `put` the same key twice?

<details>
<summary>Answers</summary>

1. `null`.
2. The old value is replaced by the new one. The map still has one pair for that key.

</details>

#### 11. Related LeetCode Questions (Often Asked)

Solve them in this order. Search by title if a number looks wrong.

**Start here — Easy**

| # | Question | Main idea | Note |
|---|---|---|---|
| 1 | Two Sum | `value → index` | 08 |
| 217 | Contains Duplicate | seen before? | 18 |
| 242 | Valid Anagram | count letters | 06, 19 |
| 387 | First Unique Character in a String | count, then scan | 22 |
| 383 | Ransom Note | count letters | 06 |
| 169 | Majority Element | count | 06 |

**Most often asked — Medium**

| # | Question | Main idea | Note |
|---|---|---|---|
| 49 | Group Anagrams | `sorted letters → words` | 20 |
| 347 | Top K Frequent Elements | count, then heap | 06 |
| 560 | Subarray Sum Equals K | prefix sum + map | 11 |
| 3 | Longest Substring Without Repeating Characters | window + last index | 13 |
| 438 | Find All Anagrams in a String | window of counts | 19 |
| 146 | LRU Cache | map + doubly linked list | 25 |
| 454 | 4Sum II | map of pair sums | 08 |
| 523 | Continuous Subarray Sum | remainders in a map | 12 |
| 525 | Contiguous Array | balance in a map | 12 |
| 138 | Copy List with Random Pointer | old node → new node | 23 |

**Hard — these separate strong candidates**

| # | Question | Main idea | Note |
|---|---|---|---|
| 76 | Minimum Window Substring | window + count maps | 13 |
| 992 | Subarrays with K Different Integers | `atMost(k) - atMost(k-1)` | 13 |
| 460 | LFU Cache | map of frequency lists | 25 |

**If you have little time, do these 8 first:** 1, 242, 49, 347, 560, 3, 146, 76.
