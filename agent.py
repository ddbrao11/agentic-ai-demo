import openai
import os
from tools import tools
from memory import Memory
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Agent:
    def __init__(self):
        self.memory = Memory()
        self.available_tools = tools

    def think(self, goal, history):
        prompt = f"""You are an intelligent AI agent. Your goal is: {goal}
You can use the following tools: {', '.join(self.available_tools.keys())}
Conversation history: {history}

Decide what to do next. Reply in format: Thought:..., Action:..., ToolInput:...
"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']

    def run(self, goal):
        print(f"Agent goal: {goal}")
        while True:
            history = self.memory.get()
            decision = self.think(goal, history)
            print("\n" + decision)

            self.memory.add(decision)

            if "Action:" not in decision:
                print("No action found. Exiting.")
                break

            try:
                action_line = [line for line in decision.splitlines() if line.startswith("Action:")][0]
                tool_line = [line for line in decision.splitlines() if line.startswith("ToolInput:")][0]
                tool = action_line.replace("Action:", "").strip()
                tool_input = tool_line.replace("ToolInput:", "").strip()

                if tool in self.available_tools:
                    result = self.available_tools[tool](tool_input)
                    print(f"Tool Result: {result}")
                    self.memory.add(f"Tool Result: {result}")
                else:
                    print("Invalid tool. Exiting.")
                    break
            except Exception as e:
                print(f"Error parsing or executing action: {e}")
                break
