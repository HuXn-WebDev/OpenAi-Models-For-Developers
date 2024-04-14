from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

response = client.images.generate(
    model="dall-e-2",
    prompt="Cat using a computer",
    size="1024x1024",
    # size="256x256",
    n=1,
)

image_url = response.data[0].url
print(image_url)
# print(response)
