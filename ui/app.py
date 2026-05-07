import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/run"

st.title("🤖 AgentFlow AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        res = requests.post(API_URL, params={"query": prompt})
        data = res.json()

        answer = data.get("answer", "No response")

    except Exception as e:
        answer = f"Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)