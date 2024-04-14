# pip install python-dotenv
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a language translator"},
        {"role": "user", "content": "Translate English To Chines: Animal"},
    ],
    max_tokens=100,
    stop="5",
    n=10,
)

message = response.choices[0].message.content
print(message)
# print(response)
