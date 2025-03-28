# 🧠 Agentic AI Demo (Python + OpenAI)

This is a beginner-friendly project that shows how to build a basic **agentic AI** system using Python and OpenAI's API.

## 🚀 What It Does
The AI agent:
- Accepts a goal (e.g., "Find the square root of 144 and write to a file")
- Thinks step-by-step
- Chooses actions
- Uses tools (like math and file writing)
- Stores a short memory of past steps

## 📁 Project Structure
```
main.py       # Run the agent
agent.py      # Core agent logic
tools.py      # Tools available to the agent
memory.py     # Simple memory storage
.env          # API key file (not included in repo)
```

## 🧪 How to Run

1. Clone this repo
2. Install dependencies:
   ```
   pip install openai python-dotenv
   ```
3. Create a `.env` file:
   ```
   cp .env.example .env
   ```
   Add your OpenAI API key in `.env`.

4. Run the agent:
   ```
   python main.py
   ```

## 🧰 Tools Used by Agent
- `CalculateSquareRoot`: Calculates square root of a number
- `WriteToFile`: Writes text to `output.txt`

## 🧠 How It Works
The agent sends a prompt to GPT, including:
- Its goal
- The available tools
- A memory of recent steps

GPT replies with a "thought", selects an "action", and provides input. The agent then executes that tool and repeats until the goal is done.

## ✨ Ideas for Extension
- Add more tools (e.g., Google search, APIs)
- Use persistent memory (e.g., vector DB)
- Add error recovery and retry logic

## 📄 License
MIT
