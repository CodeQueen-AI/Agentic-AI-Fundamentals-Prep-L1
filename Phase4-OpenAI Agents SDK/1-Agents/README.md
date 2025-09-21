# Agents
* **Agent** → Ek LLM ka instance jisme name, instructions aur tools set kiye jate hain
* **Runner** → Agent ko chalata hai aur uska result return karta hai
* **AsyncOpenAI** → OpenAI ka async client jo non-blocking calls karta hai
* **OpenAIChatCompletionsModel** → Chat Completions API shape ke liye wrapper
* **enable\_verbose\_stdout\_logging** → Console/terminal par detailed logs show karta hai


## 🔑 Main Key Points

1. **TypeError: Agent.**init**() missing 1 required positional argument: 'name'**
   → Matlab **Agent class mein `name` dena zaroori hai**

2. **OpenAI Agents SDK by default model `gpt-4.1` use karta hai**

3. **OpenAI Agents SDK "Responses API" use karta hai**

4. **`OPENAI_API_KEY is not set, skipping trace export`**
   → Matlab API key environment variable mein set karni hogi

5. **`enable_verbose_stdout_logging()`**
   → Matlab terminal par poora workflow aur debug logs dikhayega


