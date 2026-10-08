# 🪵 Wood Advisor

An AI web app that recommends the best wood for furniture, built with **LangChain**, **Google Gemini** and **Streamlit**.

**🔗 Live demo:** [wood-advisor](https://wood-advisor-mi7773.streamlit.app/)

Part of my work through the [GenAI Engineer Bootcamp](https://www.udemy.com/course/ai-developer-bootcamp/) (Section 1). I extended the course's Python script into a deployed web app.

## What I learned

- Connecting Python to an LLM with LangChain's `init_chat_model`
- Extracting model responses reliably with `response.text`
- Building and deploying a UI with Streamlit

## Run locally

```bash
pip install -r requirements.txt
cp .env.example .env   # then add your GOOGLE_API_KEY
streamlit run app.py
```
