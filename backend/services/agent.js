export async function runAssistant(question) {
  question = question.toLowerCase();

  if (question.includes("deploy")) {
    return "Deployment simulation started...";
  }

  if (question.includes("logs")) {
    return "Fetching latest CI/CD logs...";
  }

  if (question.includes("scale")) {
    return "Scaling pods...";
  }

  return "AI Assistant Response: " + question;
}
