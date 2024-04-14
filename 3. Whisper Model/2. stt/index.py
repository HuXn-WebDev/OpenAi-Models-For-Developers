from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

audio_file = open("./recording.m4a", "rb")

transcription = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file, response_format="text"
)

print(transcription)
