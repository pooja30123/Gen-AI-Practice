# 🧠 Gen AI CampusX – Lecture-wise Practice & Code

This repository contains my structured lecture-wise learning and coding practice based on the **CampusX Gen AI series**.

---

## 📚 Lecture-wise Folders

| Lecture | Folder Name             | Topic Covered                    |
|---------|--------------------------|---------------------------------|
| 3       | `3_Langchain Model`      | Loading and using LLM models    |
| 4       | `4_Prompts`              | Prompt engineering              |
| 5       | `5_Structured Output`    | Output parsing with TypedDict   |
| 6       | `6_Output Parser`        | Output parser types             |
| 7       | `7_chains`               | Simple chains in LangChain      |
| 8       | `8_Runnables`            | Runnable logic and chaining     |
| 9       | `9_Runnables`            | Advanced Runnables & composition |

---

## 🔧 Local Environment Setup

> This project uses a local virtual environment called `genai_env`.

### ▶️ How to Set Up

```bash
# Step 1: Create env (only once)
python -m venv genai_env

# Step 2: Activate it
# On Windows:
genai_env\Scripts\activate

# On macOS/Linux:
source genai_env/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

```
## 🤖 Using Multiple Local LLMs via LM Studio

I’m running local LLMs using LM Studio, connected via LangChain’s ChatOpenAI wrapper with OpenAI-compatible API.

## ✅ Supported Models & Functions

```
| Function           | Model Name                             | Description                       |
| ------------------ | -------------------------------------- | --------------------------------- |
| `Tiny_llm()`       | `tinyllama-1.1b-chat-v1.0`             | Small & fast local model          |
| `Mistral_llm()`    | `thebloke/mistral-7b-instruct-v0.1`    | General-purpose 7B model          |
| `Thebloke_llm()`   | `thebloke/mistral-7b-instruct-v0.1`    | Alias of above                    |
| `nomicEmbedding()` | `text-embedding-nomic-embed-text-v1.5` | Embedding model for vector DB use |

```
## 🧪 Sample Usage

```
from load_model import Mistral_llm

llm = Mistral_llm()
response = llm.invoke("What is LangChain?")
print(response)

```