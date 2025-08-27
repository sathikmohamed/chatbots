Local Chatbot

A Python-based chatbot that runs locally using models like LLaMA, Mistral, or Gemma. This project allows you to interact with AI models without relying on external APIs, keeping your data private and enabling faster experimentation.

Features

Run a chatbot locally on your machine.

Supports multiple models (LLaMA, Mistral, Gemma, etc.).

Interactive streaming responses with "typing" effect.

Can integrate RAG (Retrieval-Augmented Generation) and document-based chat.

Simple Flask frontend for chat interface.

Easy to extend with PDF/document ingestion.
```bash
Requirements

Python 3.10+

Virtual environment (recommended)

Dependencies in requirements.txt

Installation

Clone the repository:

git clone https://github.com/<YOUR_USERNAME>/chatbots.git
cd chatbots


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

Running the Local Chatbot
1. Start Ollama (or your local model server)

Make sure your local model server is running:

ollama serve


or any other local model.

2. Run the Flask app
python main.py


Visit http://localhost:xxxx
 in your browser.
```
Usage

Type messages in the chat input and hit Send.

The bot streams responses in real-time, showing a typing effect.

Supports multiple modes: plain chat, RAG, PDF/document Q&A.
````bash
Configuration

Add your environment variables to a .env file:

OLLAMA_URL=xxxxxxxxxx #local url
MODEL=xxxxxxxxxxxxxx #model name


Update the Flask app to read from .env using python-dotenv.

Project Structure
chatbots/
│
├─ main.py              # Flask backend
├─ chat.html            # Frontend template
├─ requirements.txt
├─ .gitignore
├─ env/                 # Virtual environment (ignored in Git)
└─ docs/                # Optional PDFs for RAG
```
Tips

Use .gitignore to keep sensitive files (.env, virtual env, large models) out of GitHub.

Use stream=True in the API for real-time chatbot responses.

Keep local models updated for best performance.

License

MIT License