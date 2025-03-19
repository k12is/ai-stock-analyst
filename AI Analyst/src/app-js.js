import React, { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  // Replace with your actual API endpoint for the AI service
  const API_URL = process.env.REACT_APP_API_URL || "https://your-backend-api.com/chat";

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!question.trim()) return;
    
    setLoading(true);
    setResponse("");
    
    try {
      const result = await axios.post(API_URL, {
        question: question
      });
      
      setResponse(result.data.response || result.data.answer || result.data.message);
    } catch (error) {
      console.error("Error fetching response:", error);
      setResponse("Sorry, there was an error processing your request. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header>
        <img src="/logo.png" alt="Quantflow AI" className="logo" />
        <h1>Quantflow AI</h1>
      </header>
      
      <div className="chat-container">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask me about market analysis..."
            disabled={loading}
          />
          <button type="submit" disabled={loading || !question.trim()}>
            {loading ? "Thinking..." : "Ask"}
          </button>
        </form>
        
        {response && (
          <div className="response-box">
            <p>{response}</p>
          </div>
        )}
        
        <p className="disclaimer">
          Quantflow AI provides analysis for informational purposes only. Not financial advice.
        </p>
      </div>
    </div>
  );
}

export default App;