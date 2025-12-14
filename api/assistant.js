// This function will be called from AssistantChat.jsx
export const askAssistant = async (query) => {
  try {
    const response = await fetch("http://localhost:3000/api/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: query }),
    });

    const data = await response.json();
    return data.message; // this will be displayed in frontend
  } catch (err) {
    console.error("API error:", err);
    return "Backend not responding.";
  }
};
