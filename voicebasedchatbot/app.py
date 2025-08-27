import os
import tempfile
import subprocess
import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from vosk import Model, KaldiRecognizer
import json

app = Flask(__name__)
CORS(app)

# -----------------------------
# Vosk setup
# -----------------------------
VOSK_MODEL_PATH = "model"  # Your Vosk model path
if not os.path.exists(VOSK_MODEL_PATH):
    raise FileNotFoundError(f"Vosk model not found at {VOSK_MODEL_PATH}")
vosk_model = Model(VOSK_MODEL_PATH)

# -----------------------------
# FFmpeg path
# -----------------------------
FFMPEG_PATH = r"D:\ffmpeg\bin\ffmpeg.exe"  # Adjust your path

# -----------------------------
# Ollama setup
# -----------------------------
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL_NAME = os.environ.get("MODEL", "gemma:2b")

# -----------------------------
# Helpers
# -----------------------------
def convert_webm_to_wav(webm_file, wav_file):
    """Convert WebM/Opus to 16kHz mono WAV"""
    command = [
        FFMPEG_PATH, "-y", "-i", str(webm_file),
        "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", str(wav_file)
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("FFmpeg error:", result.stderr)
        raise Exception("FFmpeg failed to convert audio.")

def transcribe_audio(wav_file):
    """Transcribe WAV audio with Vosk"""
    rec = KaldiRecognizer(vosk_model, 16000)
    rec.SetWords(True)
    text_parts = []
    with open(wav_file, "rb") as f:
        while True:
            data = f.read(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                part = json.loads(rec.Result()).get("text", "")
                if part:
                    text_parts.append(part)
        final_part = json.loads(rec.FinalResult()).get("text", "")
        if final_part:
            text_parts.append(final_part)
    return " ".join(text_parts).strip()

def get_ollama_reply(user_text):
    """Send text to Ollama and get reply safely (handles multiple JSON objects)"""
    if not user_text.strip():
        return "I couldn't hear anything."
    try:
        payload = {"model": MODEL_NAME, "messages": [{"role": "user", "content": user_text}]}
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        replies = []
        for line in response.text.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                if "results" in data and len(data["results"]) > 0:
                    replies.append(data["results"][0].get("content", ""))
                elif "message" in data and "content" in data["message"]:
                    replies.append(data["message"]["content"])
            except json.JSONDecodeError:
                continue
        return "\n".join(replies) if replies else "No reply from model."
    except Exception as e:
        print("Error calling Ollama:", e)
        return f"Error calling model: {e}"

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Text input
        if "text" in request.form:
            user_text = request.form["text"].strip()
            if not user_text:
                return jsonify({"error": "Empty text input"}), 400
            reply = get_ollama_reply(user_text)
            return jsonify({"user_text": user_text, "bot_reply": reply})

        # Voice input
        if "audio_data" not in request.files:
            return jsonify({"error": "No audio file uploaded"}), 400

        audio_file = request.files["audio_data"]

        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp_webm:
            audio_file.save(tmp_webm.name)
            tmp_webm_path = tmp_webm.name

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
            tmp_wav_path = tmp_wav.name

        try:
            convert_webm_to_wav(tmp_webm_path, tmp_wav_path)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        transcript = transcribe_audio(tmp_wav_path)
        if not transcript:
            return jsonify({"error": "Could not transcribe audio"}), 500

        reply = get_ollama_reply(transcript)
        return jsonify({"user_text": transcript, "bot_reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        try: os.remove(tmp_webm_path)
        except: pass
        try: os.remove(tmp_wav_path)
        except: pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
