# Accessibility, Localization & Adaptive UI

Roadmap topic 14 · Stage 4: Quality

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** the app runs on a huge range of devices, screen sizes, languages, and abilities. A layout that only works for one exact screen size, in one language, for someone with perfect vision, is a layout that breaks for a large share of real users.

---

#### 1. Accessibility Basics — 🟢 Must Know

1. **Content descriptions** — text a screen reader announces for an image or icon that has no visible label of its own; without one, that element is invisible to a screen reader user.
2. **Touch target size** — interactive elements need a minimum tappable size (roughly 48dp), even if the visible icon is smaller.
3. **Contrast** — text needs enough contrast against its background to be readable, including for users with low vision.
4. **Focus order** — for screen readers and external input (keyboard, switch access), elements should be reachable in a sensible, predictable order.

```kotlin
Icon(
    imageVector = Icons.Default.Delete,
    contentDescription = "Delete note",   // read aloud by TalkBack
    modifier = Modifier.clickable { onDelete() }
)
```

---

#### 2. Screen Readers — 🟢 Must Know

**TalkBack** (Android) reads the screen aloud based on the accessibility tree — actually turning it on and navigating your own app with it is the fastest way to find real accessibility gaps, far more effective than reading a checklist alone.

---

#### 3. Font Scaling and Display Size — 🟢 Must Know

Users can increase system font size or display size significantly — layouts built with fixed pixel heights or `Text` that gets clipped will break. Use flexible layouts (`wrap_content`-style sizing, scalable units) so text can grow without being cut off.

---

#### 4. Strings in Resources — 🟢 Must Know

1. All user-facing text belongs in **string resources**, not hardcoded in code — this is what makes translation possible at all.
2. **Plurals** — different languages have different pluralisation rules (not just "1 item" vs "N items"); use the platform's plural-resource support instead of manual `if` checks.
3. **Never concatenate translated strings** — word order differs by language; use a format string with placeholders instead (`"You have %d notes"`, not `"You have " + count + " notes"`).

---

#### 5. Dark Theme — 🟢 Must Know

Support both light and dark themes (via `MaterialTheme`, topic `5`) — many users set dark mode as their default, at the OS level, for battery and comfort reasons, and expect apps to respect it.

---

#### 6. Right-to-Left Languages — 🟡 Good to Know

Arabic, Hebrew, and other RTL languages mirror the entire layout direction — use direction-aware layout properties (start/end, not left/right) so the UI mirrors correctly instead of looking broken.

---

#### 7. Adaptive Layouts — 🟡 Good to Know

**Window size classes** (compact, medium, expanded) let a layout adapt meaningfully across phones, tablets, and foldables, rather than just stretching a phone layout onto a larger screen.

---

#### 8. Edge-to-Edge Display — 🟡 Good to Know

Modern Android encourages drawing behind the system bars (status bar, navigation bar) for a more immersive look — handled correctly with **insets**, so content isn't hidden behind those bars.

---

#### 9. Design Systems — 🟡 Good to Know

Shared **tokens** (colours, spacing, typography) and reusable components (often built on Material) keep the app visually consistent and make theming (including dark mode and adaptive layouts) manageable from one place.

---

#### 10. Accessibility in Compose — 🟡 Good to Know

Compose exposes **semantics** (`Modifier.semantics`, `contentDescription`, `role`) that describe a composable's meaning to accessibility services — the Compose-specific mechanism behind item 1's general principles.

---

#### 11. Reduced Motion and User Settings — 🟡 Good to Know

Respect OS-level accessibility settings like reduced motion — an animation-heavy UI can be genuinely uncomfortable or disorienting for some users; check the setting and scale back animations accordingly.

---

#### 12. Common Interview Questions

1. **How do you make an icon-only button accessible?**
   Give it a `contentDescription` describing its action, and ensure its tappable area meets the minimum touch target size.
2. **Why shouldn't you concatenate strings for translation?**
   Word order and grammar differ across languages — concatenation breaks translated sentences. Use format strings with placeholders instead.
3. **How do you support very large font sizes without breaking layouts?**
   Use flexible, wrap-content-style layouts and scalable text units instead of fixed pixel heights that would clip growing text.
4. **What's a window size class, and why does it matter?**
   A classification (compact/medium/expanded) of the available screen space, used to adapt layouts meaningfully across phones, tablets, and foldables, rather than just stretching one fixed layout.
5. **How would you actually test your app's accessibility?**
   Turn on TalkBack and navigate the app using only it — this surfaces real gaps (missing content descriptions, poor focus order) far more effectively than a static checklist review.

---

#### 13. Common Mistakes

1. Icons and images with no `contentDescription`.
2. Hardcoded strings instead of string resources, or concatenated translated strings.
3. Fixed-size layouts that clip text at larger font/display sizes.
4. Never actually testing with a screen reader turned on.
5. One fixed phone layout stretched onto tablets and foldables instead of adapting.

---

#### 14. Related Topics

1. `5` UI with Jetpack Compose — semantics and theming mechanics
2. `MOB 16` iOS & Swift Essentials — the iOS accessibility and localization equivalents
3. `18` Mobile System Design — adaptive UI as part of a larger design

---

#### 15. Interview Must Remember

1. **Content descriptions, touch target size, contrast, focus order** — the accessibility basics.
2. **Test with a real screen reader** (TalkBack), not just a checklist.
3. **String resources, plurals, and format strings** — never hardcode or concatenate translated text.
4. **Support dark theme and large font/display sizes** by default, not as an afterthought.
5. **Window size classes** for adapting across phones, tablets, and foldables.
