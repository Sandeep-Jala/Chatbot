from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()
MODEL = 'gpt-4.1-mini'
system_message = "You are a helpful assistant"

def chat(message, history):
    history = [{"role":h["role"],"content":h["content"]} for h in history]
    messages = [{"role":"system","content":system_message}]+history+[{"role":"user","content":message}]
    stream = openai.chat.completions.create(model=MODEL, messages = messages, stream = True)
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response
