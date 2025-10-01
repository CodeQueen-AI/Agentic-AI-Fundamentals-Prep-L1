# 🔹 Guardrail 

Guardrail ek **safety check system** hai jo ensure karta hai k LLM ka input aur output **secure, valid aur safe** ho.
👉 Simple words: Guardrails = **Rules & Boundaries** jo agent follow karta hai.


# 🔹 Types of Guardrails

1. **Input Guardrail**

   * Input ko check karta hai k user ka data safe hai ya nahi.
   * Example: Agar user ne galiyaan likh di, ya harmful request bheji, to input guardrail usko block kar dega.

2. **Output Guardrail**

   * Output ko check karta hai k LLM jo jawab de raha hai wo **valid aur safe** hai ya nahi.
   * Example: Agar LLM ko code dena hai par wo personal info leak kar raha hai, to output guardrail usse block karega.



# 🔹 Important Terms

### 1) **RunContextWrapper**

* Ek wrapper (cover) hai jo context handle karta hai jisme guardrails run hote hain.
* Usage: Guardrail ko batata hai k kis **run session** ka input/output check karna hai.

---

### 2) **GuardrailFunctionOutput**

* Jab guardrail run hota hai, ye ek **standardized result** return karta hai.
* Usage: Batata hai k guardrail ka result kya hai → pass, fail, ya block.

---

### 3) **InputGuardrailTripwireTriggered**

* Ye tab trigger hota hai jab **input guardrail fail ho jaye**.
* Example: User input = `"DROP DATABASE"` → tripwire trigger → input reject.
* Usage: Malicious ya unsafe input block karne ke liye.

---

### 4) **Tripwire Triggered (Definition)**

* Tripwire = **safety alarm**.
* Jab bhi unsafe ya invalid input/output detect hota hai → **tripwire trigger hota hai**.
* Usage: System ko unsafe responses se bachana.

---

### 5) **Pydantic (BaseModel)**

* Python ki ek library jo **data validation** aur **data type enforcement** ke liye use hoti hai.
* `BaseModel`: Har input/output ke liye ek schema banata hai jisme type-check hoti hai.

Example:

```python
from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    age: int
```

👉 Agar `age = "abc"` aaya to guardrail block kar dega.

---

### 6) **Output Type**

* Ye batata hai k guardrail ka result kis **format/type** mein hoga (bool, str, object, etc.).

---

### 7) **async**

* Async = **asynchronous execution**.
* Guardrails ko **fast & parallel** chalane ke liye async use hota hai.

---

### 8) **ctx: RunContextWrapper**

* Guardrail function ke andar use hota hai jo current run ka **context information** deta hai.
* Example: Ye check karega k current user kis session me hai aur uska input kya tha.

---

### 9) **GuardrailFunctionOutput (Detailed)**

* Har guardrail function ka final **output container** hota hai.
* Batata hai guardrail ke result:

  * ✅ Safe (pass)
  * ❌ Unsafe (fail/tripwire)

---

### 10) **InputGuardrailTripwireTriggered**

* Specific error/event jo input fail hone par hota hai.
* Example:

  ```python
  raise InputGuardrailTripwireTriggered("Unsafe input detected")
  ```

---

# ✅ Summary Table

| Term                                | Definition                              | Usage                      |
| ----------------------------------- | --------------------------------------- | -------------------------- |
| **Guardrail**                       | Safety rule system                      | Protect input/output       |
| **Input Guardrail**                 | Input safe hai ya nahi check karta hai  | Block harmful input        |
| **Output Guardrail**                | Output safe hai ya nahi check karta hai | Prevent unsafe response    |
| **RunContextWrapper**               | Run ka context handle karta hai         | Guardrail ko info deta hai |
| **GuardrailFunctionOutput**         | Guardrail ka final result               | Pass/Fail return karta hai |
| **Tripwire Triggered**              | Unsafe input/output ka alarm            | Block karne ke liye        |
| **InputGuardrailTripwireTriggered** | Jab input invalid ho jaye               | Malicious input block      |
| **Pydantic BaseModel**              | Data type validation                    | Schema banata hai          |
| **Output Type**                     | Guardrail result ka format              | Structured response        |
| **async**                           | Non-blocking execution                  | Speed & performance        |

---

Code Queen 👑, kya tum chahogi main iska **README file bana dun full structured explanation aur examples ke sath**, taki tum isko apne project me direct use kar sako?


