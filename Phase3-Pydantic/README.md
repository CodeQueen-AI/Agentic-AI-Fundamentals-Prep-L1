## 🔹 What is Pydantic?

Pydantic is a **Python library** used for **data validation and data modeling**.
It lets you define Python classes with type hints (like `name: str`, `age: int`) and automatically:

* Checks if the provided data matches the type
* Converts (parses) data into correct types when possible
* Gives clear errors if data is invalid


## 🔹 Relation with Python

* In normal Python, **type hints** (like `x: int`) are **not enforced** — they are just suggestions for developers
* Pydantic makes these type hints **strict** → it actually validates and enforces them
* Pydantic builds on Python’s **dataclasses**, **typing module**, and modern features to provide strict data models
* In short: **Python gives hints, Pydantic enforces them.** 

## 🔹 Uses of Pydantic

1. **Data Validation:** Ensures incoming data (like from API or JSON) is in correct format
2. **Parsing Data:** Converts strings to numbers, dates, etc. automatically
3. **Error Handling:** Provides detailed error messages for invalid data
4. **APIs:** Used heavily in **FastAPI** to define request/response schemas
5. **Configuration:** Useful for managing app settings and environment variables
6. **AI & Agents:** Defines structured output for LLMs (Large Language Models)

# 📦 Installation

1. **Create a Virtual Environment**

```bash
python -m venv venv
```

2. **Activate the Environment**

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

3. **Install Pydantic**

```bash
pip install pydantic
```

(Recommended latest version:)

```bash
pip install "pydantic>=2.0"
```


