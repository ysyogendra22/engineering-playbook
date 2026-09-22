# Security

Roadmap topic 13 · Stage 4: Quality

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) beyond the basics, or still changing

**In simple words:** an app ships to every user's device, decompilable and inspectable — treat anything inside it as eventually exposed. The real security boundary is the backend (`BE 6`); the app's job is to store secrets carefully, validate anything from outside, and not make an attacker's job easy.

---

#### 1. Never Ship Secrets in the App — 🟢 Must Know

API keys, passwords, and backend credentials inside the app can be extracted by decompiling the APK/IPA — this echoes `BE 1`'s rule directly. Secrets belong on the backend; the app authenticates as a *user*, never as a privileged service.

---

#### 2. Secure Token Storage — 🟢 Must Know

1. **Android Keystore** — hardware-backed (where available) secure storage for cryptographic keys, used to protect stored tokens.
2. Store auth tokens in **encrypted storage** built on the Keystore, never in plain `SharedPreferences` or a plain file.
3. Check the **current recommended API** before implementing this — Android's encrypted-storage guidance has changed across versions; verify against current documentation rather than an old tutorial.

---

#### 3. TLS Everywhere — 🟢 Must Know

1. All network traffic should use **HTTPS**, and **cleartext (plain HTTP) traffic is blocked by default** on recent Android versions unless explicitly allowed for a specific domain (rare, and usually only for local development).
2. Never weaken this default for convenience in a release build.

---

#### 4. Validate Everything from Outside — 🟢 Must Know

*Deep links, intents, WebView content, and backend responses are all untrusted input — the same "never trust the client" principle (`BE 1`), applied in reverse: the app must not trust what reaches it either.*

1. **Deep links** — validate parameters before acting on them (topic `4`); don't let a link parameter directly control something sensitive.
2. **Intents** from other apps — check the sender/data before acting, especially for **exported** components (topic `4`).
3. **WebView content** — treat loaded pages as untrusted; restrict JavaScript bridges carefully (item 11).

---

#### 5. Minimal Permissions and Data Collection — 🟢 Must Know

Request only the permissions actually needed (topic `19`), and collect only the data actually used — both reduce the app's attack surface and its exposure if a device is compromised.

---

#### 6. Logs and Screenshots — 🟢 Must Know

1. **Never log** passwords, tokens, or personal data — logs can be read by other tools, uploaded to crash reporters, or left on a device.
2. **`FLAG_SECURE`** on a window blocks screenshots and app-switcher previews — use it for genuinely sensitive screens (a payment form, a seed phrase).

---

#### 7. Certificate Pinning — 🟡 Good to Know

1. The app trusts only a specific, known certificate for your server, instead of any certificate a trusted CA has signed — defends against certain interception attacks.
2. **Operational risk**: if you rotate your certificate without updating pinned apps first, those app versions lose all connectivity — plan certificate rotation carefully around this (`SD 30`).

---

#### 8. Code Obfuscation with R8 — 🟡 Good to Know

R8 renames classes/methods and strips unused code, making reverse-engineering harder — a speed bump for attackers, not a real barrier; never rely on it as your only protection for sensitive logic.

---

#### 9. App Integrity — 🟡 Good to Know

**Play Integrity API** (Android) and **App Attest** (iOS) let the backend verify a request is coming from a genuine, unmodified app on a genuine device — useful against automated abuse and tampered clients.

---

#### 10. Biometric Authentication — 🟡 Good to Know

Fingerprint/face unlock APIs let the app gate access to a feature behind the device's own biometric check — useful for re-authentication, not as a replacement for backend-side auth.

---

#### 11. WebView Risks — 🟡 Good to Know

A `WebView` loading untrusted content is a real attack surface — disable JavaScript unless needed, restrict any JavaScript-to-native bridge tightly, and never load arbitrary, unvalidated URLs into a `WebView` with a bridge enabled.

---

#### 12. Root/Jailbreak Detection — 🟡 Good to Know

Can raise the bar, but a determined attacker on their own device can usually bypass detection — treat it as one layer, not a guarantee, and never let it be the only defence for something critical.

---

#### 13. OWASP MASVS and MASTG — 🟡 Good to Know

Standard mobile security checklists and testing guides — useful as a structured review framework when auditing an app's security posture.

---

#### 14. iOS Equivalents — 🟡 Good to Know

**Keychain** for secure storage, **App Transport Security** for enforcing HTTPS — the iOS counterparts to Android Keystore and default cleartext blocking. See topic `16`.

---

#### 15. Common Interview Questions

1. **Why is it unsafe to put an API key in the app?**
   The app can be decompiled, exposing anything embedded in it. Secrets belong on the backend; the app should authenticate as a user, not carry service-level credentials.
2. **How do you securely store an auth token on the device?**
   Encrypted storage backed by the Android Keystore (or Keychain on iOS) — never plain `SharedPreferences` or an unencrypted file.
3. **What's the risk of certificate pinning?**
   If the server's certificate is rotated without first updating pinned app versions, those versions lose connectivity entirely — coordinate rotation carefully.
4. **Why treat deep links and intents as untrusted input?**
   They can come from other apps or arbitrary URLs, not just your own backend — validate their data the same way you'd validate any external input.
5. **Is R8 obfuscation a real security measure?**
   It raises the effort needed to reverse-engineer the app, but it's not a strong barrier — don't rely on it to protect anything genuinely sensitive.

---

#### 16. Common Mistakes

1. Embedding API keys or credentials directly in the app.
2. Storing tokens in plain `SharedPreferences`.
3. Logging tokens or personal data, even temporarily, during debugging.
4. Trusting deep link or intent data without validation.
5. Rotating a pinned certificate without a rollout plan for existing app versions.

---

#### 17. Related Topics

1. `4` App Components & Lifecycle — exported components and deep links as attack surfaces
2. `8` Networking — TLS and where tokens are attached to requests
3. `19` Device Capabilities & Permissions — minimal permissions in practice
4. `BE 6` Backend Security Essentials — the shared "never trust the client" principle
5. `ARCH 11` Security Architecture — the broader architectural view
6. `16` iOS & Swift Essentials — Keychain and App Transport Security

---

#### 18. Interview Must Remember

1. **No secrets in the app** — ever. The backend is the real trust boundary.
2. **Encrypted, Keystore-backed storage** for tokens.
3. **HTTPS by default**, cleartext blocked.
4. **Deep links, intents, and WebView content are untrusted input** — validate them.
5. **Never log** tokens or personal data.
