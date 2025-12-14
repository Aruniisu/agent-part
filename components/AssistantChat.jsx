import { useState } from "react";
import { askAssistant } from "../api/assistant";

export default function AssistantChat() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    // Show user message
    setMessages((prev) => [...prev, { sender: "You", text: input }]);

    // Call backend via fetch
    const reply = await askAssistant(input);

    // Show assistant message
    setMessages((prev) => [...prev, { sender: "Assistant", text: reply }]);

    setInput("");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Smart DevOps Assistant</h2>

      <div style={{
        border: "1px solid #ccc",
        padding: "10px",
        height: "250px",
        overflowY: "scroll",
        marginBottom: "10px"
      }}>
        {messages.map((msg, i) => (
          <p key={i}><b>{msg.sender}:</b> {msg.text}</p>
        ))}
      </div>

      <input
        style={{ width: "70%" }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
