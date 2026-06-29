# Agentic AI Projects

This project demonstrates a basic **Agentic AI system** using Python and OpenAI.
It follows the **ReAct pattern**: **Reasoning + Acting**.

The agent can reason about a user question, decide which tool/function to use, execute that function, observe the result, and then provide the final answer.

---

## Project Overview

This is a beginner-friendly implementation of an AI agent with:

* OpenAI LLM integration
* Tool/function calling using Python
* ReAct-style loop
* Separate packages for agent logic, query execution, and tools
* Environment variable support using `.env`

---

## Agent Pattern Used

This project uses the **ReAct pattern**:

```text
Thought → Action → PAUSE → Observation → Answer
```

<img width="1672" height="941" alt="RaG_Workflow_ReACT_Pattern" src="https://github.com/user-attachments/assets/306f2dfe-e7ff-4209-9c3a-b473df77093b" />


### Meaning

* **Thought**: The LLM decides what it needs to do.
* **Action**: The LLM selects a tool/function.
* **PAUSE**: The LLM waits while Python executes the function.
* **Observation**: The tool/function result is sent back to the LLM.
* **Answer**: The LLM gives the final response.

---

## Project Structure

```text
Agentic AI - Projects/
├── main.py
├── .env
├── .gitignore
├── agent/
│   ├── __init__.py
│   └── agent.py
├── query/
│   ├── __init__.py
│   └── query.py
├── tools/
│   ├── __init__.py
│   └── actions.py
└── README.md
```

---

## Files Explanation

### `main.py`

Entry point of the application.
It creates a `QueryRunner` object and asks questions to the agent.

### `agent/agent.py`

Contains the `Agent` class.
This class manages conversation history and calls the OpenAI model.

### `query/query.py`

Contains the `QueryRunner` class.
This file controls the agent loop:

```text
Question → LLM response → Action detection → Tool execution → Observation → Final answer
```

### `tools/actions.py`

Contains available Python functions/tools.

Current tools:

* `calculate`
* `average_dog_weight`

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/uditsharma14/Agentic_ai_Projects.git
cd Agentic_ai_Projects
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

---

### 4. Create `.env` file

Create a `.env` file in the project root:

```bash
touch .env
```

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Do not commit `.env` to GitHub.

---

## Run the Project

```bash
python3 main.py
```

Or if imports are not detected:

```bash
PYTHONPATH=. python3 main.py
```

---

## Example Questions

### Dog weight question

```python
runner.query("How much does a Bulldog weigh?")
```

Expected flow:

```text
Thought: I should look up the dog's weight using average_dog_weight.
Action: average_dog_weight: Bulldog
PAUSE

Observation: A Bulldog weighs around 51 lbs

Answer: A Bulldog weighs around 51 lbs.
```

---

### Calculation question

```python
runner.query("What is 4 * 7 / 3?")
```

Expected flow:

```text
Thought: I need to calculate this expression.
Action: calculate: 4 * 7 / 3
PAUSE

Observation: 9.333333333333334

Answer: 4 * 7 / 3 is 9.33.
```

---

## Example Code

### `main.py`

```python
from query.query import QueryRunner

runner = QueryRunner()

runner.query("How much does a Bulldog weigh?")

print("\n--- Second Question ---\n")

runner.query("What is 4 * 7 / 3?")
```

---

## Environment Variables

This project uses `.env` for API key management.

Example:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Make sure `.env` is added to `.gitignore`.

---

## Recommended `.gitignore`

```gitignore
# Virtual environment
venv/
.venv/

# Environment variables
.env

# Python cache
__pycache__/
*.py[cod]

# macOS
.DS_Store

# VS Code
.vscode/

# Logs
*.log
```

---

## Why This Project Is Useful

This project helps understand the foundation of agentic AI:

* How an LLM can decide which tool to use
* How Python can execute that tool
* How the tool result is sent back to the LLM
* How the LLM produces a final answer after observing the result

This is the basic concept behind more advanced frameworks like:

* LangChain
* CrewAI
* AutoGen
* OpenAI tool calling
* LangGraph

---

## Future Enhancements

Possible improvements:

* Add more tools like weather, search, database lookup, or file reader
* Replace manual action parsing with OpenAI function calling
* Add logging
* Add unit tests
* Add FastAPI endpoint
* Add Streamlit UI
* Add memory support
* Add multi-agent workflow

---

## Tech Stack

* Python
* OpenAI API
* python-dotenv
* ReAct Agent Pattern

---

## Author

Udit Sharma

---

## Disclaimer

This is a learning project created to understand basic Agentic AI concepts.
Do not expose your OpenAI API key or commit `.env` files to GitHub.
