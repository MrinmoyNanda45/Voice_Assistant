AI Voice Assistant using Google Gemini API 🎙️🤖

An AI-powered Voice Assistant chatbot built using Flask and Google Gemini API that supports:

🎤 Real-time Speech Recognition
🤖 Conversational AI Responses
🔊 Text-to-Speech Output
🌐 Web-based Interactive Interface

The assistant listens to the user’s voice, sends the query to the Gemini LLM, generates intelligent responses, and speaks the response back to the user.

🚀 Features
Voice-based interaction using browser microphone
Real-time speech-to-text conversion
AI-generated responses using Google Gemini API
Text-to-speech response playback
Conversation history tracking
Clean and responsive frontend UI
Flask backend integration
Secure API key management using .env
Deployable on Hugging Face Spaces

🛠️ Tech Stack
Frontend
HTML5
CSS3
JavaScript
Web Speech API
Backend
Flask
AI Model
Google Gemini API (gemini-1.5-flash)
Deployment
Hugging Face Spaces (Docker)
GitHub

📂 Project Structure
Voice_Assistant/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
├── .env
│
├── templates/
│   └── index.html

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone [github.com/yourusername/Voice_Assistant](https://github.com/MrinmoyNanda45/Voice_Assistant)

cd Voice_Assistant
2️⃣ Create Virtual Environment
Windows
python -m venv .venv

Activate environment:

.\.venv\Scripts\Activate.ps1

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Setup Gemini API Key
Create .env File

Inside project root create:

.env

Add:

GOOGLE_API_KEY=your_gemini_api_key

▶️ Run the Application
python app.py

Application will run on:

http://localhost:5000

🎤 How It Works
User clicks Speak Now
Browser captures voice input
Speech converts to text using Web Speech API
Query sent to Flask backend
Gemini API generates AI response
Response displayed on UI
Text-to-Speech reads response aloud

🌐 Deployment
Hugging Face Spaces

This project supports deployment using:

Docker
Hugging Face Spaces
Required Files
Dockerfile
requirements.txt
Environment Variables

Add this secret in Hugging Face:

Key	Value
GOOGLE_API_KEY	Your Gemini API Key

🐳 Docker Support
Build Docker Image
docker build -t voice-assistant .
Run Docker Container
docker run -p 7860:7860 voice-assistant

📦 Requirements
flask
google-genai
python-dotenv
gunicorn

🔒 Security Note
Never expose your API key publicly
Never upload .env to GitHub
.env is included inside .gitignore
📸 Future Improvements
Chat memory with database
Multi-language support
Voice customization
Wake-word activation
Streaming AI responses
Advanced UI/UX
Authentication system

🤝 Contributing

Contributions are welcome.

Feel free to:

Fork the repository
Create feature branches
Submit pull requests

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Mrinmoy Nanda
