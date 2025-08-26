import os
import google.generativeai as genai
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ No API key found! Please set GOOGLE_API_KEY in .env")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# FastAPI app
app = FastAPI(title="Gemini Chatbot API", version="1.0")

# Serve static frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root → return index.html
@app.get("/")
def read_index():
    return FileResponse("static/index.html")

# Request body
class ChatRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = model.generate_content(request.message)
        return {"user": request.message, "bot": response.text}
    except Exception as e:
        return {"error": str(e)}
