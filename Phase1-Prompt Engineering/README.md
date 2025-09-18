# 🧠 PROMPT ENGINEERING MASTER GUIDE 

> *"Prompt Engineering sirf AI ko instructions dena nahi ye ek **magic wand** hai jisse aap AI ka dimagh guide karte ho aur woh har baar **perfect answer** de!



## 📌 Section 1: Introduction to Prompt Engineering

**Definition:**
Prompt Engineering ek technique hai jismein aap AI ko **smartly guide karte ho instructions ke through** taake woh aapke expected output ke mutabiq answer de

**Usage:**

* AI ko **specific tasks** ke liye customize karna
* ChatGPT, LLMs ya kisi bhi AI model se **better aur controlled output** lena
* AI ko complex reasoning ya multiple steps ka task solve karne ke liye **step-by-step guide** karna


## 📌 Section 2: Core Concepts in Prompt Engineering

### 1️⃣ Temperature

**Definition:**
Temperature ek parameter hai jo AI ke **randomness** ko control karta hai

**Details:**

* Low value (0.0 – 0.3): AI zyada deterministic aur **predictable** hota hai
* Medium (0.4 – 0.7): AI balanced creativity aur predictability deta hai
* High (0.8 – 1.0): AI **creative aur unpredictable** responses deta hai

**Default Value:** Usually `1.0`
**Range:** `0.0 to 2.0`



### 2️⃣ Top-K Sampling

**Definition:**
Top-K ek technique hai jisme AI sirf **top K probable words** me se choose karta hai

**Details:**

* K chhota ho → AI deterministic aur safe output deta hai
* K bada ho → AI zyada creative aur diverse output deta hai

**Default Value:** Varies by model (e.g., 50)
**Range:** 1 se infinity


### 3️⃣ Top-P (Nucleus Sampling)

**Definition:**
Top-P probability ka **cumulative threshold** hai AI sirf top P probability words me se select karta hai

**Details:**

* P low → safe aur predictable output
* P high → creative aur diverse output

**Default Value:** 0.9
**Range:** 0.0 – 1.0


### 4️⃣ Safe System Messages for Sensitive Data

**Definition:**
System messages jo **AI ko guide karte hain** ke woh sensitive data ko **handle ya reveal na kare**.

**Usage:**

* AI ko instructions dena ke koi **personal info, passwords, ya confidential data na share kare**.
* Example: `"You must not share personal user information under any circumstances."`


### 5️⃣ Chain-of-Thought (CoT) Prompting

**Definition:**
Chain-of-Thought prompting ek technique hai jisme **AI se reasoning step by step karwaya jata hai** before final answer

**Usage:**

* Complex reasoning tasks solve karne ke liye
* Example Prompt: `"Think step by step and then answer"`


### 6️⃣ Tree-of-Thought (ToT) Prompting

**Definition:**
Tree-of-Thought prompting **multiple reasoning paths** explore karne ke liye hai, aur best solution select karta hai

**Usage:**

* AI ko parallel ideas ya options generate karne ke liye guide karna
* Best for complex problems jahan multiple strategies possible hain
* Example: AI ko bola jata hai: `"Explore 3 possible reasoning paths, evaluate each, then choose the best outcome"`


## 📌 Section 3: Best Practices

* **Explicit Instructions:** Hamesha clear aur direct prompts use karein.
* **Set Parameters:** Temperature, Top-K, Top-P adjust karein based on **task complexity**.
* **Sensitive Data Protection:** System messages zarur add karein.
* **Step-by-Step Reasoning:** Chain-of-Thought ya Tree-of-Thought use karein for complex tasks.



## 📌 Section 4: Quick Reference Table

| Concept             | Definition                       | Default | Range   | Best Use Case                     |
| ------------------- | -------------------------------- | ------- | ------- | --------------------------------- |
| Temperature         | AI randomness control            | 1.0     | 0.0–2.0 | Creative vs predictable responses |
| Top-K               | Top K probable words selection   | 50      | 1–∞     | Controlled randomness             |
| Top-P               | Cumulative probability threshold | 0.9     | 0.0–1.0 | Balanced diversity                |
| Safe System Message | Protect sensitive info           | -       | -       | Secure prompts                    |
| Chain-of-Thought    | Step-by-step reasoning           | -       | -       | Complex reasoning                 |
| Tree-of-Thought     | Explore multiple reasoning paths | -       | -       | Complex problem solving           |

