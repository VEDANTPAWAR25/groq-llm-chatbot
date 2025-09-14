import os
import json
import streamlit as st
import requests

# configure API key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
GROQ_API_KEY = config_data["GROQ_API_KEY"]

# configure streamlit page
st.set_page_config(
    page_title="Groq-Chat",
    page_icon="💬",
    layout="centered",
)

# initialize chat session
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# page title
st.title("🤖 Groq LLaMA-3 ChatBot")

# let user pick model from sidebar
st.sidebar.header("⚙️ Settings")
model_choice = st.sidebar.selectbox(
    "Choose model",
    [
        "llama-3.1-8b-instant",     #  fast, cheaper
        "llama-3.3-70b-versatile",  #  larger, more accurate
        "mixtral-8x7b-32768"        #  mixture of experts, good for reasoning
    ],
    index=0
)

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
user_prompt = st.chat_input("Ask anything...")

if user_prompt:
    # add user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send request to Groq API
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model_choice,  # chosen from sidebar
        "messages": [
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.chat_history
        ]
    }

    response = requests.post(url, headers=headers, json=payload).json()

    #safely extract assistant response
    if "choices" in response:
        assistant_response = response["choices"][0]["message"]["content"]
    elif "error" in response:
        assistant_response = f"⚠️ API Error: {response['error'].get('message', 'Unknown error')}"
    else:
        assistant_response = f"⚠️ Unexpected response: {response}"

    # add assistant message
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
