from google import genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from difflib import SequenceMatcher

# Load environment variables
load_dotenv()

# Flask app
app = Flask(__name__)

# Configure Gemini Client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Model Name
MODEL_NAME = "gemini-2.5-flash"

# Store conversation history
conversation_history = []

# Voice Assistant Function
def voice_assistance(user_input):
    global conversation_history

    prompt = f"""
    You are an AI voice assistant.

    User Question:
    {user_input}

    Provide a concise, direct, and informative response.
    """

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        response_text = response.text

    except Exception as e:
        response_text = f"Error: {str(e)}"

    # Store limited history
    conversation_history.append({
        "user": user_input,
        "ai": response_text
    })

    # Keep only last 5 chats
    conversation_history = conversation_history[-5:]

    return response_text

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Process Voice Route
@app.route('/process_voice', methods=['POST'])
def process_voice():

    data = request.get_json()

    user_input = data.get("user_input")

    response = voice_assistance(user_input)

    return jsonify({
        "response": response,
        "history": conversation_history
    })

# Run App
if __name__ == "__main__":
    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 7860))
        app.run(host="0.0.0.0", port=port)