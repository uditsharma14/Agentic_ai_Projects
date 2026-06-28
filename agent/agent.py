from openai import OpenAI
from dotenv import load_dotenv
import os
import re

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Please add it to your .env file.")

if api_key == "your_api_key_here":
    raise ValueError("Replace placeholder API key with real OpenAI API key.")

client = OpenAI(api_key=api_key)


class Agent:
    def __init__(self, system=""):
        self.system = system
        self.messages = []

        if self.system:
            self.messages.append({
                "role": "system",
                "content": system
            })

    def __call__(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

        result = self.execute()

        self.messages.append({
            "role": "assistant",
            "content": result
        })

        return result

    def execute(self):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            messages=self.messages
        )

        return completion.choices[0].message.content