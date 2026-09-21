# AI Landscape & ML Basics

Roadmap topic 1 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** AI is a big field. Machine learning is one way to build it: instead of writing rules, you show a program many examples and it learns the pattern. LLMs are one kind of machine learning model. Know how these words fit together, because interviews start here.

---

#### 1. AI, ML, Deep Learning, Generative AI, LLM — 🟢 Must Know

*Each word is a smaller circle inside the one before it.*

```text
AI  (any software that seems intelligent)
 └─ Machine learning  (learns patterns from data)
     └─ Deep learning  (ML with many-layer neural networks)
         └─ Generative AI  (creates new text, images, audio, code)
             └─ LLM  (generative AI for text: predicts the next token)
```

1. **AI** — software that does tasks that normally need human intelligence.
2. **Machine learning (ML)** — the program learns from data instead of following hand-written rules.
3. **Deep learning** — ML that uses neural networks with many layers. Good at images, voice, and language.
4. **Generative AI** — creates new content instead of only labelling existing content.
5. **LLM (large language model)** — a model trained on huge amounts of text. ChatGPT-style assistants are built on LLMs.

**Example:** a spam filter is ML (it learns from labelled emails). Face Unlock is deep learning. An assistant that writes an email is generative AI, powered by an LLM.

---

#### 2. Training vs Inference — 🟢 Must Know

*Training is learning. Inference is using what was learned.*

| | Training | Inference |
|---|---|---|
| What happens | The model learns from data | The trained model answers a request |
| Cost | Very high, done rarely | Small per request, but paid on every call |
| Who does it | Model providers, big labs | You, every time your app calls a model |

1. As an app developer you almost always do **inference**: you call a model that someone else trained.
2. Every API call to an LLM is inference. That is what you pay for.
3. A trained model is fixed. It does not learn from your calls unless someone trains it again.

**Mobile view:** training is like building and shipping the app. Inference is like the app running on a user's phone.

---

#### 3. Three Ways Machines Learn — 🟢 Must Know

*The difference is what kind of feedback the model gets.*

| Type | Feedback | Example |
|---|---|---|
| **Supervised** | Examples with the right answer (labels) | Email marked "spam" or "not spam" |
| **Unsupervised** | No answers. The model finds groups or patterns | Grouping customers with similar behaviour |
| **Reinforcement** | A reward or penalty for actions | A game-playing agent, or tuning a chat model to give better answers |

1. Most business ML is supervised.
2. LLMs are first trained by predicting the next token in text. This needs no human labels.
3. After that, reinforcement-style training (from human feedback) shapes how helpful and safe they are (topic `03`).

---

#### 4. Overfitting and Data Splits — 🟢 Must Know

*A model that memorizes its practice questions will fail the real exam.*

1. **Overfitting** — the model does very well on its training data but badly on new data. It memorized instead of learning the pattern.
2. To detect it, split the data:

```text
Training set    → the model learns from this
Validation set  → you tune settings with this
Test set        → you check the final result, once
```

3. Never test on data the model has already seen. The score would look better than reality.
4. This same idea returns in evaluation for LLM apps (topic `15`): test on examples the prompt was not built around.

---

#### 5. Accuracy, Precision, Recall — 🟡 Good to Know

*Accuracy can look great while the model is useless.*

Example: fraud is 1 in 100 transactions. A model that always says "not fraud" is **99% accurate** and catches **zero** fraud.

1. **Precision** — of the items the model flagged, how many were really positive. (Few false alarms.)
2. **Recall** — of all the real positives, how many the model found. (Few misses.)
3. Choose by cost of the mistake: for fraud, missing a case is worse (favour recall). For an auto-ban system, a false alarm is worse (favour precision).

---

#### 6. Classic ML Tasks — 🟡 Good to Know

*Many "AI features" are one of these four jobs. Not everything needs an LLM.*

| Task | Question it answers | Example |
|---|---|---|
| Classification | Which category? | Spam or not spam |
| Regression | What number? | Estimated delivery time |
| Clustering | Which items are similar? | Group similar photos |
| Recommendation | What should the user see next? | "You may also like" |

A small classic model is often cheaper, faster, and easier to test than an LLM for these tasks.

---

#### 7. Neural Networks in One Minute — 🟡 Good to Know

*Layers of simple math units. The numbers between them are learned.*

1. A neural network is layers of small units. Each unit takes numbers in and passes numbers out.
2. The numbers that control it are **parameters** (also called **weights**). Training adjusts them to reduce mistakes.
3. "Deep" means many layers.
4. You do not need the math for interviews. Know: layers, weights, and "learning means adjusting weights to reduce error".

---

#### 8. Bias and Fairness — 🟡 Good to Know

*A model learns whatever its data contains, including unfair patterns.*

1. **Bias** — the model treats groups differently because the training data was unbalanced or reflected past unfairness.
2. Sources: unbalanced data, missing groups, biased labels, and your own choices about what to measure.
3. Reduce it: check results per group, use more representative data, and keep a human in the loop for high-impact decisions (loans, hiring).

---

#### 9. Common Interview Questions

1. **What is the difference between AI, ML, and deep learning?**
   AI is the broad goal. ML learns from data. Deep learning is ML with many-layer neural networks.
2. **Training vs inference?**
   Training teaches the model and is costly. Inference uses the trained model and happens on every request.
3. **What is overfitting and how do you spot it?**
   The model memorizes training data and fails on new data. You see high training score, low test score.
4. **Why can accuracy be misleading?**
   With rare events, always predicting "no" scores high. Use precision and recall.
5. **Supervised vs unsupervised learning?**
   Supervised uses labelled examples. Unsupervised finds structure without labels.
6. **Is an LLM machine learning?**
   Yes. It is a deep learning model trained to predict the next token.
7. **When would you not use an LLM?**
   When a simple rule, a database query, or a small classic model does the job faster, cheaper, and more predictably.

---

#### 10. Common Mistakes

1. Treating "AI" and "LLM" as the same thing.
2. Using an LLM for a job that a rule or a small model handles better.
3. Testing on the data used to build or tune the system.
4. Judging a model by accuracy alone.
5. Thinking a deployed model keeps learning from user requests by itself.
6. Ignoring bias until users complain.

---

#### 11. Related Topics

1. `02` How LLMs Work
2. `03` Training, Fine-Tuning & Model Choice
3. `15` Evaluation & Quality
4. `21` AI Interview Answer Points (when AI is needed at all)

---

#### 12. Interview Must Remember

1. **AI ⊃ ML ⊃ deep learning ⊃ generative AI ⊃ LLM.**
2. **Training** is costly and rare. **Inference** is every request.
3. **Overfitting** = memorized training data. Always test on unseen data.
4. **Accuracy misleads** on rare events. Know precision and recall.
5. Not every problem needs an LLM.
