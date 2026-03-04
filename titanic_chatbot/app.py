import streamlit as st
import requests

st.title("🚢 Titanic Dataset Chatbot")

question = st.text_input("Ask your question about Titanic dataset:")

if st.button("Ask"):
    if question:
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )

        if response.status_code == 200:
            answer = response.json()["answer"]
            st.success(answer)
        else:
            st.error("Backend error!")