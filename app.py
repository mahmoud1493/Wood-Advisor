import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

st.title("🪵 Wood Advisor")
woods = st.text_area("List some wood types:", "oak, pine, walnut, MDF")

if st.button("Which is best for furniture?"):
    with st.spinner("Thinking..."):
        response = model.invoke(f"Which of these is best for furniture: {woods}?")
    st.write(response.text)