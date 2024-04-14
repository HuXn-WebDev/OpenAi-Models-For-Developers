from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

response = client.audio.speech.create(
    model="tts-1", voice="alloy", input="Hello world! This is a streaming test."
)

with open("output.mp3", "wb") as f:
    for chunk in response.stream_to_file("output.mp3"):
        f.write(chunk)
