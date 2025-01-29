from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.memory import ConversationBufferMemory
import os
import requests
from dotenv import load_dotenv

# Load environment variables from the parent directory
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=dotenv_path)

# Access API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API Key not found. Make sure it's set in the .env file.")

app = Flask(__name__)
CORS(app)

# Initialize LangChain memory
memory = ConversationBufferMemory()

# Store dynamic parameters
parameters = {
    "valence": 4,
    "arousal": 4,
    "selection_threshold": 4,
    "resolution_level": 4,
    "goal_directedness": 4,
    "securing_rate": 4
}

@app.route('/set_parameters', methods=['POST'])
def set_parameters():
    """Update emotional parameters dynamically."""
    data = request.json
    parameters.update(data)
    return jsonify({"status": "Parameters updated", "parameters": parameters})

@app.route('/chat', methods=['POST'])
def chat():
    """Handle user chat and generate a response using the Gemini API."""
    user_message = request.json.get('message', '')

    # Compute emotional response
    anger = max(1, min(5, parameters["valence"] + parameters["arousal"] - parameters["goal_directedness"]))
    sadness = max(1, min(5, 7 - parameters["valence"] + parameters["selection_threshold"]))

    # Make a request to Gemini API
    url = "https://generativelanguage.googleapis.com/v1beta2/models/gemini-pro:generateText"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": user_message,
        "key": GEMINI_API_KEY
    }

    response = requests.post(url, json=data, headers=headers)
    gemini_response = response.json()

    # Extract generated response
    ai_response = gemini_response.get("candidates", [{}])[0].get("output", "I'm here to assist you.")

    # Store conversation history
    memory.chat_memory.add_user_message(user_message)
    memory.chat_memory.add_ai_message(ai_response)

    return jsonify({
        "response": ai_response,
        "anger": anger,
        "sadness": sadness,
        "conversation": memory.chat_memory.messages
    })

if __name__ == '__main__':
    app.run(debug=True)
