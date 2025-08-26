Gemini API Chatbot

A Python-based chatbot that connects to Gemini AI via API key. This allows you to interact with Gemini models without hosting the model locally. Perfect for integrating AI chat features in your apps or experiments.

Features

Chat with Gemini models using your API key.

Interactive, streaming responses.

Easy integration into Python scripts or Flask web apps.

Supports multiple Gemini models (e.g., gemini:2b, gemini:5b).
```bash
Requirements

Python 3.10+

Virtual environment (recommended)

Dependencies in requirements.txt

Installation

Clone the repository:

git clone https://github.com/<YOUR_USERNAME>/gemini-chatbot.git
cd gemini-chatbot


Create a virtual environment:

python -m venv env


Activate the environment:

Windows (PowerShell):

.\env\Scripts\Activate.ps1


Windows (Git Bash/CMD):

source env/Scripts/activate


Linux/Mac:

source env/bin/activate


Install dependencies:

pip install -r requirements.txt

Configuration

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here
MODEL=gemini:2b


Never share your API key publicly. Add .env to .gitignore.

The Python code reads the key from .env using python-dotenv:

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("MODEL", "gemini:2b")

Usage
Python Script Example
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("MODEL", "gemini:2b")

def chat_gemini(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"https://api.gemini.ai/v1/generate"
    payload = {"model": MODEL, "prompt": prompt}
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("response", "")

reply = chat_gemini("Explain machine learning in simple words.")
print("Bot:", reply)

Flask Web App Example
python main.py


Visit http://localhost:5000
 to chat via web interface.

Security Tips

Keep .env private.

Add .env to .gitignore.

Do not hardcode your API key in the code.

Rotate your API key regularly if needed.

Project Structure
gemini-chatbot/
│
├─ main.py             # Flask backend
├─ chat.html           # Frontend template
├─ requirements.txt
├─ .gitignore
├─ env/                # Virtual environment (ignored)
└─ .env                # Contains API key (ignored)
'''
License

MIT License