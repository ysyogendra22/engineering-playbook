# Grouping Pattern

#### 1. What Is It?

The **grouping pattern** puts items that share something under the **same key**.

The map is `key → list of items`. The key is a value you work out from each item: its length, first letter, sorted letters, date, category.

It organises data in **one pass** (`O(n)`) instead of filtering again and again. In an Android app: group chat messages by date, contacts by first letter, products by category.

#### 2. How It Works

Group words by length: `["hi", "yo", "hello", "world", "ok"]`

```text
key = word.length

"hi"     → key 2    {2: [hi]}
"yo"     → key 2    {2: [hi, yo]}
"hello"  → key 5    {2: [hi, yo], 5: [hello]}
"world"  → key 5    {2: [hi, yo], 5: [hello, world]}
"ok"     → key 2    {2: [hi, yo, ok], 5: [hello, world]}
```

The important step: **if the key is new, create an empty list first**, then add the item. `getOrPut` does both in one call.

Kotlin tools:

| Tool | Result |
|---|---|
| `groupBy { key }` | `Map<K, List<T>>` — all items for each key |
| `associateBy { key }` | `Map<K, T>` — one item per key (the **last** one wins) |
| `groupingBy { key }.eachCount()` | `Map<K, Int>` — only the counts |
| `partition { condition }` | two lists: matching and not matching |

#### 3. Kotlin Code

```kotlin
// Manual grouping by length
fun groupByLength(words: List<String>): Map<Int, List<String>> {
    val groups = HashMap<Int, MutableList<String>>()
    for (w in words) {
        groups.getOrPut(w.length) { mutableListOf() }.add(w)
    }
    return groups
}

// Built in
val byLength = listOf("hi", "yo", "hello", "world", "ok").groupBy { it.length }
// {2=[hi, yo, ok], 5=[hello, world]}

// Group objects (Android style: messages by date)
data class Message(val date: String, val text: String)
val messages = listOf(Message("Mon", "Hi"), Message("Tue", "Yo"), Message("Mon", "Bye"))
val byDate = messages.groupBy { it.date }                      // {Mon=[...2 messages], Tue=[...1]}
val textsByDate = messages.groupBy({ it.date }, { it.text })   // {Mon=[Hi, Bye], Tue=[Yo]}

// Group indexes by value
fun groupIndexesByValue(nums: IntArray): Map<Int, List<Int>> {
    val groups = HashMap<Int, MutableList<Int>>()
    for ((i, n) in nums.withIndex()) groups.getOrPut(n) { mutableListOf() }.add(i)
    return groups
}

// The largest group
val biggestKey = byLength.maxByOrNull { it.value.size }?.key
```

The most famous grouping question is **Group Anagrams** (note 20).

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Group `n` items with an `O(1)` key | `O(n)` | `O(n)` |
| Key made from a string of length `k` | `O(n · k)` or more | `O(n · k)` |

The cost of computing the key is what changes. A simple key is `O(1)`.

#### 5. Common Mistakes

1. **`getOrDefault(key, mutableListOf()).add(x)`.** The new list is never stored, so `x` is lost. Use `getOrPut`.
2. **`associateBy` when you need all items.** It keeps only the last.
3. **A key that is too coarse** (different things grouped together) **or too fine** (equal things split).
4. **An `IntArray` as a key.** Use a `List` or a `String`.
5. **Expecting sorted groups from a `HashMap`.** Sort the keys yourself, or use `groupBy` (which keeps first-seen order).
6. **`groupBy` returns read-only lists.** Call `toMutableList()` if you need to edit them.

#### 6. Say This in the Interview

1. "I group with `key → list`. The key is ... for each item."
2. "I use `getOrPut` so the list is created the first time a key appears."
3. "One pass: `O(n)` plus the cost of building each key."

#### 7. Quick Check

1. What does `listOf(1, 2, 3, 4).groupBy { it % 2 }` give?
2. Why is `getOrDefault(key, mutableListOf())` a bug for grouping?

<details>
<summary>Answers</summary>

1. `{1=[1, 3], 0=[2, 4]}`.
2. The default list is never stored in the map, so the items you add to it are lost.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 49 | Group Anagrams (Medium) | key = sorted letters (note 20) |
| 1282 | Group the People Given the Group Size They Belong To (Medium) | key = group size |
| 249 | Group Shifted Strings (Medium, premium) | key = pattern of differences |
| 451 | Sort Characters By Frequency (Medium) | group letters by count |
| 981 | Time Based Key-Value Store (Medium) | key → list of (time, value) |
