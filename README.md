# Emotional-AI-Chatbot

This project demonstrates a simple Emotional AI Chatbot built with React on the frontend and Flask with Langchain on the backend. This application is an AI-powered chatbot that allows users to interact via a web interface. It consists of a Flask backend serving AI responses and a React frontend for user interaction. The system processes user messages, communicates with the AI model, and returns responses in real time.

Frontend (React Application):

User Interface:

Parameter Sliders: Provides sliders for users to adjust the values of emotional parameters (valence, arousal, etc.).
Message Input: Allows users to enter their messages.
Chat History: Displays the conversation between the user and the bot.
Functionality:

Parameter Updates: Sends parameter changes to the backend using the /set_parameters API endpoint.
Message Sending: Sends user messages to the backend using the /chat API endpoint.
Receives and Displays Responses: Receives bot responses from the backend and displays them in the chat history.
Overall Functioning:

Initialization: The backend starts, initializing the parameters dictionary and the ConversationBufferMemory.
Parameter Adjustment: The user adjusts the emotional parameters using the sliders on the frontend. These changes are sent to the backend via the /set_parameters endpoint.
User Interaction: The user enters a message and clicks "Send."
Backend Processing:
The backend receives the message via the /chat endpoint.
It calculates emotion levels (anger, sadness) based on the current parameters.
It generates a response based on the calculated emotions and stores the conversation history in memory.
The backend sends the generated response to the frontend.
Frontend Display: The frontend receives the bot's response and displays it in the chat history.
Loop: The process repeats for subsequent user messages.

Flask app 
Handles API Requests: The backend is built using the Flask framework, which allows it to create and handle API endpoints.
Stores Parameters: It maintains a dictionary (parameters) to store the current values of emotional parameters (valence, arousal, etc.) received from the frontend.
Updates Parameters: The /set_parameters endpoint receives parameter updates from the frontend via POST requests, updates the parameters dictionary, and sends a success response.
Generates Responses: The /chat endpoint receives user messages via POST requests.
It uses a simple emotion-based logic to determine the initial bot response.
This logic calculates "anger" and "sadness" levels based on the current parameter values.
If "anger" is high, the bot responds with a frustration-related message.
If "sadness" is high, the bot offers support.
Otherwise, it provides a generic continuation response.
Manages Conversation Memory:
It utilizes LangChain's ConversationBufferMemory to store the conversation history between the user and the bot.
This allows the bot to potentially maintain context in future interactions (though the current implementation is basic).


Key Components:

Flask: The web framework for building the backend.
CORS: Enables Cross-Origin Resource Sharing, allowing the frontend (React) to make requests to the backend.
LangChain: Provides tools for building conversational AI applications, including memory management.
