import os
from groq import Groq

class GroqLLM:
    def __init__(self, model="llama3-70b-8192"):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = model

    def run(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content
