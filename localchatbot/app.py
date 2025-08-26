from flask import Flask, request, render_template, Response
import requests
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)


load_dotenv()

# Get Ollama URL and model from .env
OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL = os.getenv("MODEL")

@app.route("/", methods=["GET"])
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    def generate():
        with requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": user_message},
            stream=True,
        ) as r:
            for line in r.iter_lines():
                if line:
                    try:
                        obj = json.loads(line.decode("utf-8"))
                        chunk = obj.get("response", "")
                        if chunk:
                            yield chunk
                    except Exception as e:
                        print("Error:", e)

    return Response(generate(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
