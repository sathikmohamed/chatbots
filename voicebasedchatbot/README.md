Voice/Text Chat Application
A Flask-based web application that supports both text and voice chat using the Vosk speech recognition library and integrates with the Ollama API for natural language responses. This project allows users to send text messages or record voice messages, which are transcribed and responded to by an AI model.

Author: mohamed sathik
License: [Specify License, e.g., MIT, if applicable]

Features

Real-time text chat.
Voice message recording and transcription using Vosk.
Integration with Ollama API for AI-powered responses.
Dark/light theme toggle.
Visual waveform for voice recording and bot typing animation.

Prerequisites

Python 3.8 or higher.
FFmpeg installed and accessible (e.g., D:\ffmpeg\bin\ffmpeg.exe as configured).
Vosk speech recognition model downloaded and placed in the model directory.
Ollama server running at the specified OLLAMA_URL (default: http://localhost:xxxxx/api/chat).

Installation
1. Clone the Repository
git clone <repository-url>
cd voice-text-chat

2. Install Dependencies
Create a virtual environment and install the required packages:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Set Up Environment Variables
Create a .env file in the project root and add the following:
OLLAMA_URL=http://localhost:xxxxx/api/chat
MODEL=gemma:2b

Load the variables using python-dotenv.
4. Download Vosk Model

Download a Vosk model (e.g., vosk-model-small-en-us-0.15) from Vosk Models.
Extract it and place the folder in the project directory as model.

5. Install FFmpeg

Download and install FFmpeg from FFmpeg Official Site.
Update the FFMPEG_PATH in the code to point to the executable (e.g., D:\ffmpeg\bin\ffmpeg.exe).

6. Start the Ollama Server

Ensure the Ollama server is running at the specified OLLAMA_URL. Follow Ollama's official documentation to set it up.

Usage

Run the application:python app.py


Open a web browser and navigate to http://localhost:xxxx.
Use the interface to:
Type and send text messages.
Record and send voice messages.
Toggle between light and dark themes.



Project Structure

app.py: Main Flask application file.
requirements.txt: List of Python dependencies.
templates/index.html: HTML template for the chat interface (not included here but assumed).
model/: Directory for the Vosk model files.

Configuration

VOSK_MODEL_PATH: Set to model in the code; ensure the model folder is present.
FFMPEG_PATH: Adjust the path in app.py to match your FFmpeg installation.
OLLAMA_URL: Configurable via .env for the Ollama API endpoint.
MODEL_NAME: Configurable via .env for the Ollama model (default: gemma:2b).

Troubleshooting

Vosk Model Not Found: Verify the model directory contains the Vosk model files.
FFmpeg Error: Ensure FFmpeg is installed and the path is correct.
Ollama Connection Error: Check that the Ollama server is running and the URL is accessible.

Contributing
Feel free to submit issues or pull requests. Please follow the existing code style and include tests where applicable.
License
[Specify your license here, e.g., MIT License - include the full text if needed.]
Acknowledgments

Vosk for speech recognition.
Ollama for AI model integration.
Flask and related libraries for the web framework.
