import logging
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

logging.getLogger("google_genai").setLevel(logging.ERROR)
load_dotenv()

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

with open("wood.txt") as file:
    wood = file.read()

response = model.invoke(f"Which of these is best for furniture: {wood}?")
print(response.text)