## 🔹 Handoff (singular)

**Definition:**
Handoff ka matlab hai **ek agent apna kaam doosre agent ko de deta hai**, jab us agent ko lage k doosra agent us task ke liye zyada suitable hai.

**Example:**
Agar ek **general chatbot** ko koi **finance related sawal** aata hai, toh wo us sawal ko **finance agent** ko handoff kar dega

## 🔹 Handoffs (plural)

**Definition:**
Handoffs ka matlab hai **multiple agents ke beech switching system**, jisme har agent apni **specialty ke mutabiq** kaam karta hai.

**Example:**

* Customer Support agent → Order Agent ko handoff karega
* Order Agent → Refund Agent ko handoff karega

Yani ek se dusre tak chain banti hai

## 🔹 Triage Agent

**Definition:**
Triage Agent ek **decision maker** hota hai jo user ka input analyze karke decide karta hai k konsa specialized agent kaam karega.

**Example:**
Agar user ne pucha:

* "2 + 2 = ?" → Triage Agent → Math Tutor ko bhej dega
* "When was Pakistan founded?" → Triage Agent → History Tutor ko bhej dega


## 🔹 Flow Example (Diagram in Text)

```text
# [User Input]
#      ↓
# [Triage Agent] → Decides topic (e.g., "math", "history", etc.)
#      ↓
# [History Tutor / Math Tutor] → Executes based on triage decision
#      ↓
# Final Output (sent to user)
```



### ✅ Summary:

* **Handoff:** Ek agent kaam doosre ko de deta hai.
* **Handoffs:** Multiple agents ke beech switching.
* **Triage Agent:** Decide karta hai k user ka input kis agent ko bhejna hai.
