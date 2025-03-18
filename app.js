import React from "react";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        {/* Logo */}
        <img src="/quantflow-AI.png" alt="Quantflow AI Logo" className="logo" />
        <h1>Quantflow AI</h1>
        <p className="developed-by">Developed by 24K Research</p>
      </header>

      {/* Your chat UI */}
      <div className="chat-container">
        <input type="text" placeholder="Enter Stock Ticker (e.g., AAPL)" />
        <button>Analyze</button>
      </div>
    </div>
  );
}

export default App;
