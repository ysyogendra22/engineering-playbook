# Device Capabilities & Permissions

Roadmap topic 19 · Stage 7: Mobile in the System

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** every device capability the app touches — location, camera, contacts — comes with a permission the user must grant, and a real cost (battery, privacy) even after they do. Asking well and using sparingly are both part of the actual skill.

---

#### 1. Runtime Permission Flow — 🟢 Must Know

1. **Ask in context** — request a permission right when the feature that needs it is used, not upfront at launch (topic `1`).
2. **Explain why** — show the user what the permission is for before (or as part of) the system prompt, so the request makes sense.
3. **Handle denial** — the feature should degrade gracefully, not crash or block the whole app.
4. **"Don't ask again"** — after repeated denials, the OS may stop showing the prompt at all; detect this and guide the user to the app's settings screen instead of silently failing.

```kotlin
when {
    hasPermission(Manifest.permission.CAMERA) -> openCamera()
    shouldShowRationale(Manifest.permission.CAMERA) -> showExplanationThenRequest()
    else -> requestPermission(Manifest.permission.CAMERA)   // or route to Settings if permanently denied
}
```

---

#### 2. Location — 🟢 Must Know

1. **Precision** — coarse (approximate area) vs fine (exact) location; request only the precision the feature actually needs.
2. **Foreground vs background** — background location access is a much heavier ask (both in permission friction and store review scrutiny) than foreground-only.
3. **Battery cost** — continuous high-precision location tracking is one of the biggest battery drains an app can cause; use the lowest update frequency and precision that still satisfies the feature.

---

#### 3. Camera and Media — 🟢 Must Know

1. **Capture** — using the camera directly within the app.
2. **Picker APIs** — letting the user pick an existing photo/video, which on recent Android versions can avoid needing broad media permissions at all.
3. **Large images** — downsample before processing or uploading (topics `8`, `11`) — never hold a full-resolution camera image in memory longer than necessary.

---

#### 4. Connectivity and Network Changes — 🟢 Must Know

Detect connectivity type (Wi-Fi, cellular, metered vs unmetered) and react to changes — pause a large download on a lost connection, resume when reconnected, and prefer unmetered connections for non-urgent large transfers (topic `8`).

---

#### 5. Biometrics and Device Credentials — 🟡 Good to Know

Fingerprint/face unlock, or falling back to the device PIN/pattern, for re-authentication gates (topic `13`) — not a replacement for backend authentication, an additional local gate.

---

#### 6. Files and Scoped Storage — 🟡 Good to Know

Recent Android versions restrict broad filesystem access in favour of **scoped storage** — an app generally accesses its own files freely, and other files (photos, downloads) through mediated APIs rather than raw filesystem paths.

---

#### 7. Contacts, Calendar, Sensitive Data — 🟡 Good to Know

Treat access to contacts, calendar, health, and similar categories as especially sensitive — request only if core to the feature, and be ready to justify it in store review (topic `15`).

---

#### 8. Bluetooth, NFC, Sensors — 🟡 Good to Know

Names and purpose: Bluetooth for nearby device communication, NFC for tap-to-interact, and various sensors (accelerometer, gyroscope) for motion/orientation — each with its own permission and battery considerations.

---

#### 9. Privacy Dashboards and Auto-Reset — 🟡 Good to Know

Recent Android versions show users a dashboard of which apps used which permissions and when, and can **auto-reset** permissions for apps the user hasn't opened in a while — design for permissions potentially being silently revoked over time.

---

#### 10. Data-Safety Declarations — 🟡 Good to Know

Both app stores require declaring what data the app collects and how it's used, shown to users before install — keep this genuinely accurate; a mismatch between the declaration and actual behaviour is a policy violation, not just an inconvenience.

---

#### 11. Common Interview Questions

1. **How should an app request a sensitive permission like location?**
   In context, right when the feature needs it, with a clear explanation beforehand — not at launch, and with graceful handling if the user denies it.
2. **What's the difference between foreground and background location access?**
   Foreground-only location works while the app is in use; background access continues even when the app isn't visible — a much heavier privacy ask, with more permission friction and store scrutiny.
3. **How do you handle a permanently denied ("don't ask again") permission?**
   Detect that the system prompt won't appear again, and guide the user to the app's settings screen instead of silently failing or repeatedly requesting.
4. **Why prefer a photo picker over broad media/storage permissions?**
   It lets the user select a specific file without granting the app ongoing access to their entire media library — less permission friction, better privacy.
5. **What should the app do if a permission is revoked automatically (auto-reset) while installed?**
   Detect the missing permission at the point of use and re-request or degrade gracefully — the same handling as an initial denial.

---

#### 12. Common Mistakes

1. Requesting permissions upfront at launch instead of in context.
2. No graceful fallback when a permission is denied.
3. Requesting background location when foreground-only would suffice.
4. Holding full-resolution camera images in memory longer than needed.
5. An inaccurate data-safety declaration that doesn't match the app's real behaviour.

---

#### 13. Related Topics

1. `1` Mobile Platform Basics — the runtime permission model introduced there
2. `13` Security — minimal permissions as a security principle too
3. `18` Mobile System Design — location and camera features as part of a larger design
4. `08-artificial-intelligence/16` Safety, Security & Privacy — the same "collect the minimum" principle applied to AI features

---

#### 14. Interview Must Remember

1. **Ask in context, explain why, handle denial gracefully.**
2. **Foreground location, not background**, unless truly required — and always the coarsest precision that works.
3. **Prefer picker APIs** over broad, standing storage/media permissions.
4. Permissions can be **silently auto-reset** — design to detect and recover from that.
