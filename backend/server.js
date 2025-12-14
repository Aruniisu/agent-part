import express from "express";
import cors from "cors";
import assistantRoutes from "./routes/assistant.js";

const app = express();
app.use(cors());
app.use(express.json());

// All API routes
app.use("/api", assistantRoutes);

app.get("/", (req, res) => {
  res.send("Backend is running!");
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Backend running on http://localhost:${PORT}`);
});
