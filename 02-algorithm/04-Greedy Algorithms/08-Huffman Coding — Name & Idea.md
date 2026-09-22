# Huffman Coding — Name & Idea

#### 1. Definition — Must Know

1. **Huffman coding** is a greedy algorithm that builds the smallest possible encoding for a set of characters, based on how often each one appears.
2. Characters that appear more often get shorter codes; characters that appear rarely get longer codes.

#### 2. Why It Is Used — Must Know

1. It's a real compression technique (used in formats like ZIP and JPEG), and a good example of greedy applied to building a tree, not just scanning a list.
2. Interviews usually only expect you to know the **idea** and be able to describe the process — not implement it from memory.

#### 3. How It Works — Must Know

```text
Characters and frequencies: a:5  b:9  c:12  d:13  e:16  f:45

Repeatedly take the two least frequent nodes and merge them into a new node
(whose frequency is their sum), until only one node (the root) remains.

Step 1: merge a(5) + b(9)  → new node(14)
Step 2: merge c(12) + d(13) → new node(25)
Step 3: merge node(14) + e(16) → new node(30)
Step 4: merge node(25) + node(30) → new node(55)
Step 5: merge node(55) + f(45) → root(100)

Reading the path from the root to each character (left = 0, right = 1)
gives that character's code. Frequent characters end up near the root
(short codes); rare ones end up deep (long codes).
```

#### 4. Algorithm — Must Know

```text
put every character in a min-heap, keyed by frequency
while more than one node remains in the heap:
    take the two smallest nodes out
    merge them into a new node (frequency = sum of the two)
    put the new node back in the heap
the last remaining node is the root of the Huffman tree
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// The shape of it, using a min-heap — full tree-building and code assignment
// is usually beyond what's expected to reproduce from memory.
data class Node(val freq: Int, val char: Char? = null, val left: Node? = null, val right: Node? = null)

fun buildHuffmanTree(frequencies: Map<Char, Int>): Node {
    val heap = java.util.PriorityQueue<Node>(compareBy { it.freq })
    frequencies.forEach { (c, f) -> heap.add(Node(f, c)) }
    while (heap.size > 1) {
        val a = heap.poll()
        val b = heap.poll()
        heap.add(Node(a.freq + b.freq, left = a, right = b))
    }
    return heap.poll()
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Building the tree | O(n log n), n = number of distinct characters |

#### 7. Common Mistakes — Must Know

1. Expecting to write the full tree-building **and** code-assignment logic from memory in an interview — this is usually "know the idea", not "implement it cold" (see the mark on this topic).
2. Forgetting the min-heap detail — always merging the two *least* frequent nodes is what makes the result optimal.
3. Confusing this with a fixed-length encoding — the whole point of Huffman coding is **variable-length** codes.

#### 8. Related Topics

1. `DS Heap` — the min-heap this algorithm is built on
2. `1` The Greedy Choice Property — why "always merge the two smallest" works here
3. `7` Greedy Graph Algorithms — Dijkstra, Kruskal, Prim — another greedy algorithm that also uses a min-heap

#### 9. Interview Must Remember

1. Huffman coding = **repeatedly merge the two least frequent nodes** using a min-heap, until one tree remains.
2. Frequent characters end up with **short codes**; rare characters end up with **long codes**.
3. This is a name-and-idea topic — know what it does and why, not necessarily the full implementation.
