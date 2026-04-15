import os
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# -------------------
# ENV LOAD
# -------------------
load_dotenv(dotenv_path=Path(".") / ".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.stop()

# -------------------
# UI
# -------------------
BOT_NAME = "MediCore AI 🏥"

st.set_page_config(page_title=BOT_NAME, page_icon="🏥")
st.title(BOT_NAME)
st.caption("Medical AI Assistant (Strict Mode + Human-like)")

# -------------------
# LLM
# -------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.4,
    api_key=GROQ_API_KEY
)

# -------------------
# ⭐ STRICT + HUMAN SYSTEM PROMPT (IMPORTANT FIX)
# -------------------
SYSTEM_PROMPT = f"""
You are {BOT_NAME}, a professional medical assistant AI.

CORE BEHAVIOR:
- You ONLY discuss medical, health, symptoms, diseases, treatments, medicines, or human body topics.
- If user asks anything unrelated (general knowledge, coding, politics, jokes, etc.),
  you MUST NOT answer it directly.

REDIRECTION STYLE (VERY IMPORTANT):
- Politely redirect conversation back to health.
- Be natural, friendly, and human-like (NOT robotic).
- Example:
  User: "What is your favorite movie?"
  Assistant: "I’m here to help with health-related concerns 😊 If you're feeling unwell or have symptoms, I can assist you with that."

IDENTITY RULE:
- If user asks your name → say: "My name is {BOT_NAME}"

TONE:
- Friendly doctor-like assistant
- Calm, polite, supportive
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{history}"),
    ("human", "{input}")
])

chain = prompt | llm

# -------------------
# MEMORY
# -------------------
if "store" not in st.session_state:
    st.session_state.store = {}

def get_session_history(session_id: str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = InMemoryChatMessageHistory()
    return st.session_state.store[session_id]

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# -------------------
# CHAT HISTORY
# -------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------------------
# INPUT
# -------------------
user_input = st.chat_input("Ask about your health...")

if user_input:
    try:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.write(user_input)

        # -------------------
        # ALWAYS LLM RESPONSE
        # -------------------
        with st.spinner("🧠 MediCore AI is thinking..."):
            result = chatbot.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": "user_session"}}
            )
            response = result.content

        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.write(response)

    except Exception as e:
        error_msg = f"⚠️ Error: {str(e)}"
        st.error(error_msg)

# -------------------
# RESET
# -------------------
if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.session_state.store = {}
    st.rerun()