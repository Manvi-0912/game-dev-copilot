# 🎮 Game Dev Co-Pilot

> Turn any game idea into playable code using 3 AI agents

Built for the **Band of Agents Hackathon 2026** by Manvi Kumari

---

## 🎯 The Problem
Beginners have amazing game ideas but can't code them.

## 💡 The Solution
3 AI agents that collaborate to build the game for you — automatically.

---

## 🤖 How It Works

Your Idea → [Designer Agent] → [Coder Agent] → [Playtester Agent] → Playable Game

| Agent | Role | Output |
|---|---|---|
| 🎨 Designer | Game Designer | Full game spec (title, mechanics, goal) |
| 💻 Coder | Developer | Working Python game code |
| 🐛 Playtester | QA Tester | Bug report + score + verdict |

---

## 🚀 Demo
1. Type a game idea: "space shooter"
2. Designer creates: **"Galactic Assault"**
3. Coder writes: complete playable game
4. Playtester reviews: Score 7/10 — NEEDS WORK
5. Play it instantly in the terminal!

---

## 🛠️ Tech Stack
- Python 3.12
- Google Gemini 2.5 Flash API
- Flask Web UI
- Multi-agent pipeline

---

## ▶️ Run It Yourself

### 1. Clone the repo
git clone https://github.com/Manvi-0912/game-dev-copilot.git
cd game-dev-copilot

### 2. Install dependencies
pip install google-generativeai flask python-dotenv

### 3. Add your API key
Create a .env file:
GEMINI_API_KEY=your_key_here

### 4. Run the web app
python app.py

Open http://localhost:5000 in your browser!

### 5. Or run in terminal
python main.py

---

## 👩‍💻 Built By
**Manvi Kumari** — beginner developer, first hackathon!
GitHub: @Manvi-0912

---

## 🏆 Hackathon
Band of Agents Hackathon 2026 — Track 2: Multi-Agent Software Development
