# Context in OpenAI Agents

## 🔹 Context – Definition
**Context** ek information hoti hai jiske behalf par LLM decide karta hai ke user ko kya response dena hai.  
(Yani, LLM ka jawab context par depend karta hai.)

---

## 🔹 Types of Context

1. **LLM Context**  
   - Jo information **LLM ke paas hoti hai** (instructions, prompts, tools).  
   - Ye directly model ko provide ki jati hai.  

2. **Local Context**  
   - Jo **secret ya private information** hoti hai (API keys, configs, sensitive data).  
   - Ye model ko directly share nahi hoti.  

---

## 🔹 4 Ways to Pass Context to LLM

1. **Instructions** → Agent ko batana ke kaise behave karna hai.  
2. **Prompt** → User ka actual input / sawal.  
3. **Function Tools** → Agent ke kaam ke liye defined tools (e.g., calculator, search).  
4. **Hosted Tools** → External tools jo LLM ke sath integrate hote hain.  

---

## 🔹 Context Wrappers

- **Run Context Wrapper**  
  - **Definition:** Ye ek wrapper hota hai jo run ke dauran context ko manage karta hai.  
  - **Kaam:** Agent ke execution ke waqt extra data (jaise metadata, tracing info) ko handle karta hai.  

---

## 🔹 Related Concepts

- **Dataclass**  
  - **Definition:** Python ka feature jo classes ko as data containers use karne ke liye hota hai.  
  - **Kaam:** Less boilerplate code (automatic `__init__`, `__repr__` etc.).  

- **Asyncio**  
  - **Definition:** Python ka async framework.  
  - **Kaam:** Ek hi time me multiple tasks run karne ke liye (concurrency).  

- **@ (Decorator)**  
  - **Definition:** Python me ek special syntax jo functions/classes ke behavior ko modify karta hai.  
  - **Kaam:** Extra features add karna bina original code badle.  
  - **Example:** `@dataclass`, `@staticmethod`, `@tool`.  

---

## 🔹 LLM Context Variants

- **LLMContext Tool** → Jab context ek tool ke zariye diya jata hai.  
- **LLMContext Instructions** → Jab context directly instructions ki form me diya jata hai.  

---

## ✅ Summary

- **Context** → LLM ke liye decision making info.  
- **Local Context** → Secret/private info (not shared).  
- **LLM Context** → Model ke pass wali info (instructions, prompts, tools).  
- **4 Ways to Pass Context** → Instructions, Prompt, Function Tools, Hosted Tools.  
- **Run Context Wrapper** → Context ko execution ke time handle karta hai.  
- **Dataclass** → Easy data classes.  
- **Asyncio** → Async programming for concurrency.  
- **@** → Decorators for modifying behavior.  
