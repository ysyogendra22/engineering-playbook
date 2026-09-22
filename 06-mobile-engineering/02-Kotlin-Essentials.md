# Kotlin Essentials

Roadmap topic 2 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** Kotlin is the language every other topic in this folder is written in. Its null-safety, data classes, and functional collection operators aren't decoration — they're what make the rest of Android development (state modelling, coroutines, Compose) work the way it does.

---

#### 1. Null Safety — 🟢 Must Know

*The type system tells you, at compile time, whether a value can be missing.*

1. A type like `String` can never hold `null`. `String?` can. The compiler forces you to handle the difference.
2. `?.` — call a method only if the value isn't null (a "safe call"). `?:` — provide a default if it is (the "Elvis operator"). `!!` — force-unwrap, and crash if it's actually null.

```kotlin
val name: String? = user?.profile?.name   // safe calls, chained
val display = name ?: "Unknown"           // Elvis operator: fallback if null
val forced = name!!                       // avoid — crashes on null, no safety net
```

3. **Avoid `!!`** in real code — it throws away the whole point of null safety. Prefer `?.`, `?:`, or a proper null check.

---

#### 2. `val` vs `var`, Immutability — 🟢 Must Know

1. `val` — assigned once, cannot be reassigned (like `final` in Java). `var` — can be reassigned.
2. **Default to `val`.** Immutable data is easier to reason about, especially once coroutines and Compose recomposition are involved (topics `3`, `5`) — a value that can't change can't cause a race condition.

---

#### 3. Modelling State: Data Classes, Sealed Types, Enums — 🟢 Must Know

*This is the single most important Kotlin skill for Android — modelling UI state cleanly (topic `6`).*

1. **Data class** — auto-generates `equals`, `hashCode`, `toString`, and `copy()`. Used for plain data (a UI state, a network model).
2. **Sealed class / sealed interface** — a closed, exhaustive set of subtypes. The compiler forces you to handle every case in a `when`.
3. **Enum** — a fixed set of named constants.

```kotlin
sealed interface UiState {
    object Loading : UiState
    data class Content(val items: List<Note>) : UiState
    data class Error(val message: String) : UiState
}

fun render(state: UiState) = when (state) {           // compiler checks all cases are covered
    is UiState.Loading -> showSpinner()
    is UiState.Content -> showList(state.items)
    is UiState.Error -> showError(state.message)
}
```

---

#### 4. Functions: Defaults, Named Args, Extensions — 🟢 Must Know

1. **Default arguments** — a parameter can have a default value, so callers only pass what differs.
2. **Named arguments** — pass arguments by name, in any order, which makes call sites at a glance readable.
3. **Extension functions** — add a function to an existing type without modifying or subclassing it.

```kotlin
fun greet(name: String, formal: Boolean = false) = if (formal) "Good day, $name" else "Hi, $name"
greet(name = "Asha", formal = true)              // named argument

fun String.isValidEmail(): Boolean = this.contains("@")   // extension function
"a@b.com".isValidEmail()
```

---

#### 5. Lambdas and Higher-Order Functions — 🟢 Must Know

1. A **lambda** is a function you can pass around as a value.
2. A **higher-order function** takes a function as a parameter, or returns one — this is how `map`, `filter`, click listeners, and Compose's `onClick` all work.

```kotlin
val onClick: () -> Unit = { println("tapped") }
button.setOnClickListener { onClick() }
```

---

#### 6. Collections and Sequences — 🟢 Must Know

1. Kotlin's collection operators (`map`, `filter`, `groupBy`, `fold`, `sortedBy`) let you transform data without hand-written loops — read `03-leetcode-patterns`'s "Kotlin for Coding Interviews" topic for the interview-specific list.
2. **Sequences** (`asSequence()`) evaluate lazily, one element at a time through the whole chain — better than a `List` chain for large data or many chained operations, since a `List` chain builds a full intermediate list at every step.

```kotlin
val activeNames = users.filter { it.isActive }.map { it.name }   // two full lists built
val lazyNames = users.asSequence().filter { it.isActive }.map { it.name }.toList()  // one pass
```

---

#### 7. Scope Functions — 🟢 Must Know

*Five small functions that run a block of code "in the context of" an object.*

| Function | `this` or `it`? | Returns |
|---|---|---|
| `let` | `it` | the lambda's result |
| `apply` | `this` | the object itself |
| `also` | `it` | the object itself |
| `run` | `this` | the lambda's result |
| `with` | `this` | the lambda's result |

```kotlin
val user = User().apply {          // configure an object, then return it
    name = "Asha"
    age = 30
}
val length = name?.let { it.length } ?: 0   // run only if non-null
```

---

#### 8. Generics and Variance — 🟡 Good to Know

1. Generics let a class or function work with any type, checked at compile time (`List<String>`, `Repository<Note>`).
2. `out` (covariance) and `in` (contravariance) describe whether a generic type can safely be substituted with a subtype or supertype — mostly relevant when designing your own generic APIs.

---

#### 9. `object`, Companion Object, Singletons — 🟡 Good to Know

1. `object` declares a class with exactly one instance (a singleton), created lazily and thread-safely by Kotlin.
2. `companion object` — members tied to the class itself, not an instance (similar to `static` in Java).

---

#### 10. Delegation — 🟡 Good to Know

1. `by lazy { }` — computes a value only the first time it's accessed, then caches it.
2. **Property delegates** (`by`) and **class delegation** let you reuse getter/setter or interface implementation logic without repeating it.

```kotlin
val expensiveValue: String by lazy { computeExpensiveValue() }   // computed once, on first access
```

---

#### 11. `inline` and Value Classes — 🟡 Good to Know

1. `inline` functions are copied into the call site at compile time, avoiding the overhead of creating a lambda object — mainly relevant for higher-order functions.
2. **Value classes** (`@JvmInline value class`) wrap a single value (like a typed ID) with zero runtime overhead — type safety without allocation cost.

---

#### 12. Kotlin vs Java Interop — 🟡 Good to Know

1. Kotlin compiles to the same bytecode as Java and can call Java code directly, and vice versa.
2. Common friction points: Java has no null safety (so Kotlin treats unannotated Java types as "platform types", requiring care), and checked exceptions don't exist in Kotlin.

---

#### 13. Idiomatic Kotlin — 🟡 Good to Know

1. Prefer expressions over statements where it reads better (`val x = if (...) a else b`).
2. Prefer immutable collections (`List`) over mutable ones (`MutableList`) in public APIs, exposing mutability only where truly needed.

---

#### 14. Common Interview Questions

1. **What does null safety actually prevent?**
   `NullPointerException`s caught at compile time instead of runtime, by making nullability part of the type (`String` vs `String?`).
2. **When would you use a sealed class instead of an enum?**
   When each case needs to carry different data (an enum's cases can't each hold different fields; a sealed class's subtypes can).
3. **What's the difference between `let`, `apply`, and `also`?**
   `let` and `apply`/`also` differ in what they return (`let`/`run` return the lambda result; `apply`/`also` return the object) and whether the object is `this` or `it` inside the lambda.
4. **Why avoid `!!`?**
   It throws away compile-time null safety and crashes at runtime instead — defeats the purpose of nullable types.
5. **What's the difference between `map` on a `List` vs a `Sequence`?**
   `List` operators are eager and build an intermediate list at each step. `Sequence` operators are lazy and process one element through the whole chain at a time — better for large data or long chains.

---

#### 15. Common Mistakes

1. Overusing `!!` instead of handling nullability properly.
2. Using `var` and mutable state by default instead of `val` and immutability.
3. Modelling UI state with loose booleans and nullable fields instead of a sealed type.
4. Chaining many collection operators on a large `List` instead of using a `Sequence`.
5. Ignoring named arguments, leading to unreadable call sites with many positional booleans.

---

#### 16. Related Topics

1. `3` Coroutines & Flow — builds directly on lambdas and suspend functions
2. `5` UI with Jetpack Compose — state modelling uses sealed classes and data classes heavily
3. `6` App Architecture — sealed UI state is the backbone of MVVM/MVI here
4. `03-leetcode-patterns/3` Kotlin for Coding Interviews — the interview-coding-specific Kotlin toolkit

---

#### 17. Interview Must Remember

1. **Null safety is a compile-time type system feature** — `String` vs `String?`, avoid `!!`.
2. **Sealed classes model a closed set of states**, and the compiler enforces handling every case.
3. **Default to `val` and immutability** — it avoids a whole class of bugs once coroutines and Compose are involved.
4. Know the **five scope functions** and when each fits.
