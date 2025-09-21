
# OpenAI Agents Setup

## Installations

Install OpenAI Agents SDK:
```bash
uv pip install openai-agents
````

Install Rich 

```bash
uv add rich
```

## ⚒️ Tools & Overrides

* **Tool Calling** → Jab agent ko koi extra task perform karwana ho (jaise calculator ya search) to woh tool call karta hai
* **Function Tool** → Ek function ko tool banate hain jo agent ke liye action perform karta hai

  * Example: `get_weather(city)` → agent ko weather details mil jati hain
* **Override** → Tool ke attributes (name/description) ko customize karna

  * **Name Override** → Tool ka naam apni marzi se set karna
  * **Description Override** → Tool ka explanation custom likhna


## 🔑 Important Points

1. **Function Tool use to perform an agent action**
   → Agent ke liye practical task perform hota hai

2. **Overrides help in clarity**
   → Name aur Description override se tools ka samajhna easy ho jata hai

3. **Multiple Tools**
   → Ek agent ke sath ek se zyada tools attach kiye ja sakte hain

4. **Real-world Tasks**
   → Tools agent ko text ke alawa real kaam karne ki ability dete hain (e.g., fetch data, calculations)


