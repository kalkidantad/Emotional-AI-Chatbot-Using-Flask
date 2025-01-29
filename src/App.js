import React, { useState } from "react";
import axios from "axios";

const App = () => {
    const [message, setMessage] = useState("");
    const [chatLog, setChatLog] = useState([]);
    const [parameters, setParameters] = useState({
        valence: 4,
        arousal: 4,
        selection_threshold: 4,
        resolution_level: 4,
        goal_directedness: 4,
        securing_rate: 4,
    });

    const handleParameterChange = (e) => {
        setParameters({
            ...parameters,
            [e.target.name]: parseInt(e.target.value),
        });
    };

    const updateParameters = async () => {
        await axios.post("http://127.0.0.1:5000/set_parameters", parameters);
    };

    const sendMessage = async () => {
        const res = await axios.post("http://127.0.0.1:5000/chat", { message });
        setChatLog([...chatLog, { user: message, bot: res.data.response }]);
        setMessage("");
    };

    return (
        <div className="app">
            <h1>Emotional AI Chatbot</h1>
            <div>
                <h2>Adjust Parameters</h2>
                {Object.keys(parameters).map((key) => (
                    <div key={key}>
                        <label>{key.replace("_", " ")}: </label>
                        <input
                            type="range"
                            min="1"
                            max="7"
                            name={key}
                            value={parameters[key]}
                            onChange={handleParameterChange}
                        />
                        <span>{parameters[key]}</span>
                    </div>
                ))}
                <button onClick={updateParameters}>Update Parameters</button>
            </div>
            <div>
                <h2>Chat</h2>
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                />
                <button onClick={sendMessage}>Send</button>
                <div>
                    {chatLog.map((log, index) => (
                        <div key={index}>
                            <p><strong>You:</strong> {log.user}</p>
                            <p><strong>Bot:</strong> {log.bot}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default App;
