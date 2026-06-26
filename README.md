# LangChain Practice API

A modular FastAPI project demonstrating core LangChain Expression Language (LCEL) concepts through five independent tasks.

---

## Features

- FastAPI
- LangChain LCEL
- Google Gemini / OpenRouter LLM
- Pydantic Validation
- Modular Project Structure
- Environment Variables using pydantic-settings

---

## Project Structure

```text
app/
│
├── core/
│   ├── llm.py
│   ├── settings.py
│
├── health/
│
├── task1/
├── task2/
├── task3/
├── task4/
├── task5/
│
└── main.py
```

---

## Installation

Clone the repository

```bash
git clone <repo-url>
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=your_api_key
OPENROUTER_API_KEY=your_api_key
```

---

## Run the API

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health

GET

```
/health
```

Returns

```json
{
    "status":"ok"
}
```

---

## Task 1

POST

```
/transform
```

Uses RunnableBranch to:

- Summarize
- Translate
- Tone Shift

---

## Task 2

POST

```
/parse-resume
```

Extracts

- Name
- Skills
- Years of Experience
- Last Role

using structured output.

---

## Task 3

POST

```
/ask
```

Uses

- Query Classification
- RunnableBranch

to answer

- Coding
- Math
- General questions

---

## Task 4

POST

```
/generate-content
```

Uses RunnableParallel to generate

- Summary
- Tweet
- LinkedIn Post

simultaneously.

---

## Task 5

POST

```
/safe-json
```

Uses RunnableLambda to automatically repair malformed JSON before returning a validated response.

---

# Concepts Demonstrated

- Prompt Templates
- LCEL
- RunnableBranch
- RunnableParallel
- RunnableLambda
- Structured Output
- Output Parsers
- FastAPI
- Pydantic
- Modular Architecture

---

# Technologies

- Python 3.13
- FastAPI
- LangChain
- Pydantic
- Google Gemini / OpenRouter
- Uvicorn

---

# Author

Vansh Gautam