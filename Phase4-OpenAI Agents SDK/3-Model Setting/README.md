## 🔹 Model Setting – Definition

**English (simple):** Model setting means how we control the AI model’s behavior, creativity, randomness, and output quality
**Urdu (roman):** Model setting ka matlab hai AI model ke behavior aur creativity ko control karna — jaise output kitna random ho, kitna creative ho, ya kitna focused ho


## 🔹 Tool Choice

1. **Auto**

   * **English:** Model automatically decides whether to use a tool or not.
   * **Urdu:** Model khud decide karega tool call karna hai ya nahi.

2. **Required**

   * **English:** Model is forced to call a tool, it must use one.
   * **Urdu:** Model ko tool call karna hi hoga (forcefully).


## 🔹 Temperature (0.1 vs 0.9)

* **English:** Temperature controls creativity/randomness of responses.

* **Urdu:** Temperature decide karta hai ke jawab kitna random/creative hoga.

* **0.1 →** Very focused, less random, almost same type ka jawab (deterministic).

* **0.9 →** Highly creative, more random, har baar thoda different jawab.

* **Range:** Usually `0` se `1` tak hota hai (kabhi kabhi `2` tak bhi hota hai).


## 🔹 Top-K

* **English:** Top-K means model picks from the **K most likely words** only.
* **Urdu:** Top-K ka matlab hai model sirf sabse zyada possible **K words** mein se select karega.

👉 Example: Agar **Top-K = 50**, to model har step pe sirf top 50 likely words me se choose karega.


## 🔹 Top-P (Nucleus Sampling)

* **English:** Top-P means model picks from the smallest set of words whose probabilities add up to P.
* **Urdu:** Top-P ka matlab hai model sirf un words me se choose karega jinki total probability P (jaise 0.9) tak banti ho.

👉 Example: **Top-P = 0.9** → Model unhi words me se choose karega jinki cumulative probability 90% tak hoti hai.



✅ **Summary in short:**

* **Temperature** → Randomness level (0 = strict, 1 = creative).
* **Top-K** → Kitne likely words ka pool consider karna hai.
* **Top-P** → Probability threshold se pool decide hota hai.
* **Tool Choice (auto/required)** → Model tools auto decide kare ya forcefully use kare.

