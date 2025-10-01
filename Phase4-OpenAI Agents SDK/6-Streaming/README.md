## 🔹 Streaming 

**Definition (English):** Streaming means the model sends its response **piece by piece (chunks)** instead of sending the full answer at once.
**Urdu (roman):** Streaming ka matlab hai ke model apna jawab **thoda-thoda karke bhejta hai**, pura ek saath nahi.

**Kaam:**

* Early output mil jata hai (user ko wait nahi karna padta)
* Real-time typing effect ya fast UI build karne ke liye best hota hai


## 🔹 `openai.types.responses`

* Ye OpenAI Agents SDK ka type system hai jo responses ko **structured format** me represent karta hai
* Isme alag-alag event aur data classes hoti hain (jaise `ResponseTextDeltaEvent`)



## 🔹 `ResponseTextDeltaEvent`

**English:** This event represents a **small chunk of text** streamed by the model
**Urdu (roman):** Ye event ek **chhota hissa (delta)** hota hai model ke jawab ka jo stream ke dauran aata hai

👉 Example: Agar model ka jawab hai `"Hello Code Queen!"`, to stream me pehle `"Hello"`, phir `" Code"`, phir `" Queen!"` alag-alag events aayenge


## 🔹 Run Methods

1. **`Runner.run_sync()`**

   * **English:** Runs the agent synchronously (waits until the full response is ready).
   * **Urdu (roman):** Agent ko sync chalata hai aur poora jawab ek saath milta hai.

2. **`Runner.run()`**

   * **English:** Runs asynchronously (good with asyncio).
   * **Urdu (roman):** Async run hota hai, yani dusre kaam ke sath parallel chal sakta hai.

3. **`Runner.run_streamed()`**

   * **English:** Runs agent with streaming, so you receive **events** (like partial text, tool calls, etc.).
   * **Urdu (roman):** Agent ko stream mode me chalata hai jahan jawab tukron (chunks) me aata hai.


## 🔹 `instance`

* Instance ka matlab hota hai **object jo class se bana ho**.
* Example: `agent = Agent(name="Helper")` → yahan `agent` ek instance hai `Agent` class ka.



## 🔹 `"raw_response_event"`

* Ye ek **low-level event** hota hai jo pure response ka raw data deta hai stream ke dauran.
* Helpful agar tum debugging ya custom handling karna chah rahi ho.


## 🔹 `event.data.delta`

* **English:** This is the actual **piece of new text** coming from the model during streaming.
* **Urdu (roman):** Streaming ke dauran model jo naya text bhejta hai woh `event.data.delta` me milta hai.

👉 Example:

* First event → `"Hello"`
* Second event → `" Code"`
* Third event → `" Queen!"`



✅ **Summary (easy):**

* **Streaming** → Answer chunk by chunk.
* **ResponseTextDeltaEvent** → Ek chunk of text.
* **run\_sync** → Full answer ek saath.
* **run** → Async run.
* **run\_streamed** → Answer stream me tukron me.
* **instance** → Class ka object.
* **raw\_response\_event** → Full raw stream data.
* **event.data.delta** → Har chunk ka actual text.


