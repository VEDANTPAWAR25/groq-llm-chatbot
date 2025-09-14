# GroqChat 🤖

A **Streamlit-based chatbot** powered by **Groq’s LLaMA-3 and Mixtral models**.  
Chat with an AI assistant in real-time, with chat history maintained in session state.  

---

## 🚀 Features

- Interactive **Streamlit UI** for chatting with AI  
- Maintains **chat history** using `st.session_state`  
- Supports **Groq API** (OpenAI-compatible format)  
- Easily switch between models like:
  - `llama3-8b-8192` (fast & lightweight)  
  - `llama3-70b-8192` (large & smart)  
  - `mixtral-8x7b-32768` (Mixture of Experts, long context)  
- Configurable API key using `config.json`  

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/GroqChat.git
cd GroqChat
