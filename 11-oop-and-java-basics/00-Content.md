# OOP & Java Basics: Learning & Interview Roadmap

The object-oriented ideas and the Java details that every design discussion and coding interview uses: the four pillars, abstract class vs interface, `equals`/`hashCode`, `==` vs `equals`, pass-by-value, immutability, exceptions, and generics. Learn this folder **before** SOLID and design patterns (`ARCH 24`, `ARCH 25`).

- **Numbering:** own, 1–13, plus 99 (cheat sheet). Room is left after 13 for later topics (see "Planned Later" at the end).
- **Every note has the same layout:** what it is and how to spot it in an interview, how it works (with a diagram), naive vs better design, templates and examples in Java and Kotlin with checked outputs, numbers and rules of thumb, common mistakes and edge cases, what to say in the interview, a quick check, and practice (interview questions, exercises, and LeetCode design problems, Easy → Medium). Java examples are compiled and run on JDK 21; Kotlin examples are marked "not compiled" unless they were run.
- **References:** `11` = this folder · `ARCH 4`/`ARCH 24`/`ARCH 25` = topic N in `09-architecture` · `DS 1` = `01-data-structure` · Kotlin language detail in `06-mobile-engineering/02-Kotlin-Essentials`
- **Start with:** topic 1 if OOP is new. If you already know the pillars, jump to topics 6 to 9 (the Java details interviewers love).
- **Marks:** 🟢 must have · 🟡 good to have · (New) for a mobile engineer, or still changing

---

## Index

| #   | Topic                                          | Stage                         | Mark |
| --- | ---------------------------------------------- | ----------------------------- | ---- |
| 1   | Classes and Objects                            | 1. The Four Pillars           | 🟢   |
| 2   | Encapsulation and Access Modifiers            | 1. The Four Pillars           | 🟢   |
| 3   | Inheritance and Polymorphism                   | 1. The Four Pillars           | 🟢   |
| 4   | Abstraction: Abstract Class vs Interface      | 1. The Four Pillars           | 🟢   |
| 5   | Composition vs Inheritance                     | 1. The Four Pillars           | 🟢   |
| 6   | `equals`, `hashCode` and `toString`            | 2. Java Details Interviewers Ask | 🟢 |
| 7   | `==` vs `equals`, String Pool, Integer Cache   | 2. Java Details Interviewers Ask | 🟢 |
| 8   | Pass-by-Value and References                   | 2. Java Details Interviewers Ask | 🟢 |
| 9   | Immutability and Value Objects                 | 2. Java Details Interviewers Ask | 🟢 |
| 10  | `static`, `final`, Nested Classes and Enums    | 2. Java Details Interviewers Ask | 🟢 |
| 11  | Exceptions and Resource Handling               | 2. Java Details Interviewers Ask | 🟢 |
| 12  | Generics                                       | 2. Java Details Interviewers Ask | 🟡 |
| 13  | Java vs Kotlin Cheat Table (New)               | 3. Java and Kotlin            | 🟡   |
| 99  | OOP & Java Cheat Sheet                         | Revision                      | 🟢   |

**Short on time:** 3, 4, 5, 6, 7, 8, 9, 11, then the cheat sheet (99). 🟢 items only.

**How the folders connect:**

| Folder | What it adds | Read it |
|---|---|---|
| **11 OOP & Java Basics** (this folder) | the language-level ideas: classes, inheritance, `equals`, immutability | first |
| `09-architecture` topic 24 | SOLID: five habits for classes that are easy to change | after topics 1 to 5 |
| `09-architecture` topic 25 | design patterns and class-design (LLD) interview steps | after SOLID |

**Languages used:** Java is the language interviewers and most OOP books use, so every example is shown in Java first. Kotlin is shown next to it, because you write Android code in Kotlin. Where they differ, topic 13 has the full table.

**Glossary:** the terms to learn first are listed at the end, each with a priority mark and the topic that explains it.

---

# What to Follow for Every Topic

*The same seven steps work for any topic here. Keep your notes short and write the code yourself.*

| Step | Question to answer | Output |
|---|---|---|
| 1. Name it | What is it, in one sentence a beginner understands? | Your own one-line definition |
| 2. See it | Where does it appear in real code (an Android class, a collection, an SDK)? | One real example from your own app |
| 3. Break it | What goes wrong if I ignore the rule? | A small failing example (for instance a `HashSet` that cannot find an object) |
| 4. Fix it | What is the better design? | The corrected code, written by you, in Java and Kotlin |
| 5. Say it | Can I explain it in 30 seconds, out loud? | The "Say This in the Interview" lines, in your own words |
| 6. Check it | Can I answer the quick-check questions without looking? | All answers right, or note which to revisit |
| 7. Practise it | Can I use it in a design problem? | The LeetCode design problems and exercises at the end of the note |

**Priority order when time is short:** steps 3, 4, and 5. Most interview answers are "here is the trap, here is the fix, here is why".

---

# Stage 1: The Four Pillars

*The vocabulary every design discussion uses. Learn these in order: each builds on the one before.*

## 1. Classes and Objects

- 🟢 Class (blueprint) vs object (one instance on the heap)
- 🟢 Fields, methods, constructors; `this`
- 🟢 Instance vs `static` members (preview; full detail in topic 10)
- 🟢 Stack vs heap: where variables and objects live
- 🟡 Initialization order: fields, initializer blocks, constructor
- 🟡 Constructor overloading; Kotlin primary constructor and `init`

## 2. Encapsulation and Access Modifiers

- 🟢 Private state, with methods that enforce the rules (the `Account` example)
- 🟢 Access modifiers: `public`, `protected`, package-private, `private`; Kotlin `internal`
- 🟢 Getters and setters: when to have them, and when to skip them
- 🟢 Do not expose an internal mutable list
- 🟡 Kotlin properties: `val`, `var`, `private set`
- 🟡 Encapsulation and testing

## 3. Inheritance and Polymorphism

- 🟢 Is-a relationship; `extends`; `super`
- 🟢 Overriding (runtime) vs overloading (compile time), with the `Dog`/`Animal` trap
- 🟢 Polymorphism: one call, different behaviour; removing `if (type)` chains
- 🟢 `final` (Java) and `open` (Kotlin): control what can be overridden
- 🟢 The constructor trap: calling an overridable method from a constructor
- 🟡 `instanceof` / `is` and smart casts; when a cast is a design smell
- 🟡 Method hiding and `super` calls in a chain

## 4. Abstraction: Abstract Class vs Interface

- 🟢 Abstract class: shared state and code, one parent
- 🟢 Interface: a contract, many allowed, `default` methods
- 🟢 Comparison table and the rule of thumb: start with an interface
- 🟢 Default-method conflicts and how to resolve them
- 🟡 Kotlin `fun interface`, interface properties, sealed interfaces
- 🟡 Marker interfaces and functional interfaces

## 5. Composition vs Inheritance

- 🟢 Has-a vs is-a; why "prefer composition" is a common interview line
- 🟢 The fragile base class problem
- 🟢 Refactor: from a deep inheritance tree to small parts you can swap
- 🟡 Delegation with Kotlin `by`
- 🟡 Strategy as composition (a preview of `ARCH 25`)

---

# Stage 2: Java Details Interviewers Ask

*Short, sharp topics. Each is a favourite "gotcha" question, so learn the trap and the fix.*

## 6. `equals`, `hashCode` and `toString`

- 🟢 The contract: equal objects must have equal hash codes
- 🟢 Why `HashMap` and `HashSet` find the bucket first, then compare
- 🟢 Demo: an object with `equals` but no `hashCode`, lost in a `HashSet`
- 🟢 The four `equals` rules: reflexive, symmetric, transitive, consistent
- 🟢 `record` (Java) and `data class` (Kotlin): generated `equals`, `hashCode`, `toString`
- 🟡 `equals` and inheritance: the symmetry problem
- 🟡 `Objects.hash`, `Objects.equals`, and `hashCode` with mutable fields

## 7. `==` vs `equals`, String Pool, Integer Cache

- 🟢 `==` compares references, `equals` compares content (Java); Kotlin `==` vs `===`
- 🟢 String literals and the string pool; `new String("a")`; `intern()`
- 🟢 Integer cache: -128 to 127, and why `1000 == 1000` can be `false`
- 🟢 Never compare strings or boxed numbers with `==`
- 🟡 `float`/`double` comparison and `NaN`
- 🟡 Autoboxing, unboxing, and `NullPointerException` traps

## 8. Pass-by-Value and References

- 🟢 Java is always pass-by-value; for objects the value is a reference
- 🟢 Demo: a method can change an object's contents but cannot re-point the caller's variable
- 🟢 Stack vs heap diagram of a method call
- 🟢 Why a primitive passed in is never changed
- 🟡 Kotlin: parameters are `val`, so you cannot reassign them
- 🟡 Defensive copies at the boundary (link to topic 9)

## 9. Immutability and Value Objects

- 🟢 What immutable means and why it is useful (sharing, map keys, thread safety)
- 🟢 The recipe: `final` class, `private final` fields, no setters, defensive copies
- 🟢 Why `String` is immutable
- 🟢 `copy()` in Kotlin `data class`; `List.copyOf` in Java
- 🟢 Never use a mutable object as a `HashMap` key
- 🟡 Value objects (`Money`, `Email`): wrap a primitive to give it rules
- 🟡 Kotlin `val` vs read-only `List` vs truly immutable

## 10. `static`, `final`, Nested Classes and Enums

- 🟢 `static` members and why global mutable state is risky
- 🟢 `final` (Java) vs `val` (Kotlin) vs `const`
- 🟢 Kotlin: `companion object` and top-level functions instead of `static`
- 🟢 Enums with fields and methods; replacing "magic strings"
- 🟡 Nested vs inner classes; Kotlin nested by default, `inner` to capture the outer class
- 🟡 Anonymous classes and lambdas

## 11. Exceptions and Resource Handling

- 🟢 Checked vs unchecked exceptions; `Error` vs `Exception`
- 🟢 try-with-resources (Java) and `use {}` (Kotlin): resources close in reverse order
- 🟢 `try`/`catch`/`finally`: what runs, and in what order
- 🟢 What not to do: catching `Exception` and ignoring it
- 🟢 Custom exceptions and when to use them
- 🟡 Kotlin has no checked exceptions; `Result` and `runCatching`
- 🟡 Exceptions in constructors; `finally` that returns

## 12. Generics

- 🟡 Type safety at compile time: `List<String>`
- 🟡 Type erasure: what is lost at runtime
- 🟡 Bounded types: `<T extends Comparable<T>>`
- 🟡 Wildcards: `? extends`, `? super` (PECS)
- 🟡 Kotlin `in` / `out` variance
- 🟡 Why you cannot create `new T()` or `new T[]`

---

# Stage 3: Java and Kotlin

*One page that puts the two languages side by side. Use it for the "I know Kotlin, but this is a Java interview" moment.*

## 13. Java vs Kotlin Cheat Table (New)

- 🟡 Inheritance: open by default (Java) vs `final` by default (Kotlin)
- 🟡 `@Override` vs required `override`
- 🟡 `static` vs `companion object`
- 🟡 Singleton: enum/holder vs `object`
- 🟡 `record` vs `data class`
- 🟡 `==` and `===`
- 🟡 Checked exceptions: Java yes, Kotlin no
- 🟡 Null safety: annotations vs the type system (`String?`)
- 🟡 Common Java idioms and their Kotlin one-liners

---

# Glossary: Terms to Learn First

Plain meanings, with a priority. The last column is the topic that explains the term.

**The four pillars**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Class | A blueprint that describes fields and methods | 1 |
| 🟢 | Object | One instance of a class, living on the heap | 1 |
| 🟢 | Encapsulation | Keep data private and change it only through methods that protect the rules | 2 |
| 🟢 | Access modifier | A keyword (`public`, `private`, ...) that says who can see a member | 2 |
| 🟢 | Inheritance | A subclass reuses and specialises a parent class (is-a) | 3 |
| 🟢 | Polymorphism | One call runs different code depending on the real object type | 3 |
| 🟢 | Overriding | A subclass replaces a parent method with the same signature; chosen at runtime | 3 |
| 🟢 | Overloading | Same method name, different parameters; chosen at compile time | 3 |
| 🟢 | Abstraction | Show what something does, hide how | 4 |
| 🟢 | Abstract class | A class with shared state and code that cannot be created directly | 4 |
| 🟢 | Interface | A contract that a class can implement; a class may implement many | 4 |
| 🟢 | Composition | Build behaviour from smaller parts a class holds (has-a) | 5 |
| 🟡 | Delegation | Pass a job to a helper object; Kotlin `by` does it for you | 5 |

**Java details**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | `equals` | Says whether two objects have the same content | 6 |
| 🟢 | `hashCode` | A number used to pick a bucket in hash-based collections; equal objects must match | 6 |
| 🟢 | `record` / `data class` | A short class that generates `equals`, `hashCode`, `toString` | 6 |
| 🟢 | Reference equality | Same object in memory (`==` in Java, `===` in Kotlin) | 7 |
| 🟢 | String pool | A shared store of string literals, so equal literals are the same object | 7 |
| 🟢 | Integer cache | Boxed `Integer` values from -128 to 127 are shared | 7 |
| 🟢 | Pass-by-value | A method receives a copy of the argument; for objects, a copy of the reference | 8 |
| 🟢 | Immutable | An object that never changes after creation | 9 |
| 🟢 | Defensive copy | Copy a mutable input or output so outside code cannot change your state | 9 |
| 🟢 | `static` | A member that belongs to the class, not to one object | 10 |
| 🟢 | Checked exception | One the compiler forces you to catch or declare (Java only) | 11 |
| 🟢 | try-with-resources / `use` | Closes a resource automatically, even on failure | 11 |
| 🟡 | Generics | Classes and methods that work with a type chosen by the caller | 12 |
| 🟡 | Type erasure | Generic type arguments are removed at runtime | 12 |
| 🟡 | Wildcard | `?` in a generic type: an unknown type with an upper or lower bound | 12 |

---

# Planned Later

*Not numbered yet, so you can add them without renumbering. Each would be its own note with the same layout.*

- **Java 8+ features:** lambdas, streams, `Optional`, method references
- **Collections internals:** `HashMap` buckets and resizing, `ArrayList` vs `LinkedList`, fail-fast iterators (mostly links to `01-data-structure`)
- **Concurrency basics:** threads, `synchronized`, `volatile`, executors
- **JVM memory and garbage collection:** heap, stack, reachability, memory leaks
- **Kotlin-only topics:** null safety, sealed classes, extension functions, scope functions
- **Class-design practice:** parking lot, library, vending machine (shared with `ARCH 25`)

## Skip for Now

- Reflection, annotation processing and bytecode details
- Old Java features nobody uses in new code (raw types, `Vector`, `Hashtable`, `finalize`)
- Serialization internals (`Serializable`, `transient`)
- Multiple inheritance puzzles beyond the interface default-method case

## How to Proceed

1. Read topics 1 to 5 as a set: they are the four pillars and the "prefer composition" rule. Write a small `Shape`, `Account` and `Animal` example yourself in both languages.
2. Learn topics 6 to 9 next. They are the most frequent Java "gotcha" questions, so run each demo and watch it fail before you read the fix.
3. Learn topics 10 and 11 as a checklist: `static`/`final` rules, and how resources are closed.
4. Read topic 12 (generics) after you are comfortable with 1 to 11. It is good to know, rarely the whole question.
5. Read topic 13 once, then keep it open when you switch between Java and Kotlin.
6. Then continue with SOLID and design patterns (`ARCH 24`, `ARCH 25`) and do the LeetCode design problems at the end of each note.
7. For each topic: what it is, what goes wrong without it, the fix, one line to say out loud.
8. The night before an interview, read `99-OOP-and-Java-Cheat-Sheet`, then the `Say This in the Interview` part of the topics you are least sure of.
