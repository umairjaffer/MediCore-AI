# 🏥 MediCore AI — Medical Chatbot (Streamlit + Groq + Llama 3)

## 📌 Overview

MediCore AI is a strict AI-powered medical assistant built using Groq LLM (Llama 3), LangChain, and Streamlit. It is designed to answer only health-related questions and politely redirect all unrelated topics back to medical discussions.

---

## 🚀 Features

- 🏥 Medical-only AI assistant (strict domain control)
- 💬 Human-like conversational responses
- 🧠 Memory-enabled chat (session-based)
- ⏳ Loading spinner during response generation
- 🤖 AI identity: MediCore AI 🏥
- 🔄 Reset chat option
- ⚡ Fast inference using Groq API (Llama 3)

---

## 🧠 AI Behavior Rules

- Only responds to medical / health / disease-related queries  
- Politely redirects unrelated questions back to health topics  
- Friendly, human-like tone (doctor assistant style)  
- Always stays safe and educational  

Example:  
User: What is your favorite movie?  
AI: I’m here to help with health-related concerns 😊 If you're feeling unwell, I can assist you.

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🎨  
- LangChain 🧠  
- Groq API ⚡  
- Llama 3 Model 🤖  
- python-dotenv 🔐  

---

## 📁 Project Structure

```
MediCore-AI/
├── app.py
├── requirements.txt
├── .env
└── README.md
```

## 🔑 Environment Variables

Create a `.env` file:

GROQ_API_KEY=your_groq_api_key_here

---

## ⚙️ Installation & Setup

1. Clone repo  
git clone https://github.com/your-username/medi-core-ai.git  
cd medi-core-ai  

2. Create virtual environment  
python -m venv venv  
venv\Scripts\activate (Windows)  
source venv/bin/activate (Mac/Linux)  

3. Install dependencies  
pip install -r requirements.txt  

4. Run app  
streamlit run app.py  

---

## 🌐 Deployment (Hugging Face Spaces)

Go to https://huggingface.co/spaces  
Create new Space  
Select Streamlit SDK  
Upload files  
Add GROQ_API_KEY in Secrets  

---

## ⚠️ Disclaimer

MediCore AI is not a real doctor. It is for educational purposes only and should not replace professional medical advice.

---

## 👨‍💻 Developer

Built with ❤️ using Groq + LangChain + Streamlit

---

## 🚀 Future Improvements

- Voice-enabled AI doctor  
- Symptom diagnosis system  
- Hospital recommendation engine  
- Long-term memory system