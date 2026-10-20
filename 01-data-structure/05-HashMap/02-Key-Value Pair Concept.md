# Key-Value Pair Concept

#### 1. What Is It?

A **key-value pair** (also called an **entry**) links one **key** to one **value**.

- The **key** is what you search with. It must be unique in the map.
- The **value** is the data stored under that key. Values can repeat.

```text
Key (unique)     Value (can repeat)
"Asha"       →   30
"Ben"        →   25
"Chitra"     →   30          ← two keys may have the same value
"Asha"       →   31          ← same key again: the old value 30 is replaced
```

In Kotlin, `"Ben" to 25` makes a `Pair`, and `mapOf("Ben" to 25)` makes a map from pairs.

**The most important skill in HashMap problems is choosing the key and the value.** Ask two questions:

1. What do I **search with**? → that is the **key**.
2. What do I **need back**? → that is the **value**.

#### 2. How It Works

| Problem | Key | Value |
|---|---|---|
| Count letters | the letter | the count |
| Two Sum | the number | its index |
| Group Anagrams | sorted letters | list of words |
| Subarray sum | prefix sum | how many times it appeared |
| Cache | the request | the saved result |
| Copy a linked list | old node | new node |

Three shapes of values appear again and again:

| Value is... | Meaning | Example |
|---|---|---|
| a number | count or index | frequency map, Two Sum |
| a list | a group | Group Anagrams |
| an object | extra data | `id → User` |

#### 3. Kotlin Code

```kotlin
val scores = hashMapOf("Asha" to 90, "Ben" to 75)

// Read every pair
for ((name, score) in scores) println("$name has $score")

// Three views of a map
println(scores.keys)        // the keys, as a Set
println(scores.values)      // the values (repeats allowed)
println(scores.entries)     // the pairs

// Value is a list: key → many items
val tags = HashMap<String, MutableList<String>>()
tags.getOrPut("kotlin") { mutableListOf() }.add("android")
tags.getOrPut("kotlin") { mutableListOf() }.add("coroutines")
println(tags)               // {kotlin=[android, coroutines]}

// Build a map from a list
data class User(val id: Int, val name: String)
val users = listOf(User(1, "Asha"), User(2, "Ben"))
val byId = users.associateBy { it.id }              // id → User
val nameById = users.associate { it.id to it.name } // id → name
```

`associateBy` and `associate` keep only the **last** item when two items have the same key. Use `groupBy` to keep all of them.

#### 4. Complexity

| Action | Time |
|---|---|
| Find, add, update or remove one pair | `O(1)` on average |
| Visit all pairs | `O(n)` |
| Find a key from a value (reverse lookup) | `O(n)` |

For a fast reverse lookup, keep a second map the other way round.

#### 5. Common Mistakes

1. **Choosing the wrong key**, so you cannot find the thing you need quickly.
2. **Overwriting a value by accident** when two items share a key.
3. **Searching by value.** That is `O(n)`. Keep a second map.
4. **Using a mutable object as a key** and changing it.
5. **Using `associateBy` when you need all items.** It keeps only the last.
6. **Joining fields into a `String` key without a separator.** `"1" + "23"` and `"12" + "3"` are both `"123"`. Use `"1,23"`.

#### 6. Say This in the Interview

1. "My key is the number, and my value is its index."
2. "I need to look up by X, so X is the key."
3. "The value is a list, because several items can share a key."

#### 7. Quick Check

1. For "count how many times each word appears", what are the key and the value?
2. For "group words that are anagrams", what is the value?

<details>
<summary>Answers</summary>

1. Key: the word. Value: the count (a number).
2. A list of words.

</details>

#### 8. Related LeetCode Questions

| # | Question | Key → value |
|---|---|---|
| 1 | Two Sum (Easy) | number → index |
| 242 | Valid Anagram (Easy) | letter → count |
| 49 | Group Anagrams (Medium) | sorted letters → list of words |
| 981 | Time Based Key-Value Store (Medium) | key → list of (time, value) |
| 138 | Copy List with Random Pointer (Medium) | old node → new node |
