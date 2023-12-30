import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_KEY")

openai.api_key = openai_key

model = "gpt-3.5-turbo-1106"

message = [
    {
        "role": "system",
        "content": "안녕 너는 누구니?"
    }
]

tokens = 100

response = openai.chat.completions.create(
    model=model,
    messages=message,
    max_tokens=tokens
)

answer = response.choices[0].message.content

print(answer)