import express from "express";
const router = express.Router();

// Simulated agent logic with CI/CD pipeline
function runAssistant(question) {
  question = question.toLowerCase();

  // Simulate Deploy
  if (question.includes("deploy")) {
    return `
Deployment Simulation Started...
[Step 1] Pulling latest code...
[Step 2] Installing dependencies...
[Step 3] Running tests... ✅
[Step 4] Building Docker image...
[Step 5] Deploying container...
Deployment Completed Successfully!
`;
  }

  // Simulate Logs
  if (question.includes("logs")) {
    return `
CI/CD Pipeline Logs:
- [10:00] Code pulled from GitHub
- [10:01] Tests executed
- [10:02] Build created
- [10:03] Deployment completed
`;
  }

  // Simulate Scaling
  if (question.includes("scale")) {
    return `
Scaling Pods Simulation:
- Current replicas: 2
- Requested replicas: 5
- Scaling up...
- Scaling completed!
`;
  }

  // Generic reply
  return "AI Assistant Response: " + question;
}

// API endpoint
router.post("/ask", (req, res) => {
  const { message } = req.body;
  console.log("Received:", message);

  const reply = runAssistant(message || "");
  console.log("Reply:", reply);

  res.json({ message: reply });
});

export default router;
