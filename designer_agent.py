import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def designer_agent(game_idea):
    print(f"\n🎨 Designer Agent is working on: '{game_idea}'")
    print("-" * 40)
    
    prompt = f"""
    You are a Game Designer Agent. A user wants to build this game: "{game_idea}"
    
    Create a detailed game spec in JSON format with these fields:
    - title: name of the game
    - genre: type of game
    - description: 2 sentence description
    - player_goal: what the player must do to win
    - mechanics: list of 3 core game mechanics
    - difficulty: easy/medium/hard
    
    Respond with ONLY the JSON, no extra text.
    """
    
    response = model.generate_content(prompt)
    
    # Parse and display the spec
    spec_text = response.text.strip()
    spec_text = spec_text.replace("```json", "").replace("```", "").strip()
    
    spec = json.loads(spec_text)
    
    print("✅ Game Spec Created!")
    print(json.dumps(spec, indent=2))
    
    return spec

# Test it!
if __name__ == "__main__":
    game_idea = input("Enter your game idea: ")
    spec = designer_agent(game_idea)