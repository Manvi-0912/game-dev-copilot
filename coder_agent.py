import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def coder_agent(game_spec):
    print(f"\n💻 Coder Agent is building: '{game_spec['title']}'")
    print("-" * 40)
    
    prompt = f"""
    You are a Coder Agent. Based on this game spec, write a simple but complete 
    Python text-based game that runs in the terminal.
    
    Game Spec:
    {json.dumps(game_spec, indent=2)}
    
    Requirements:
    - Use only Python standard library (no external packages)
    - Make it playable in the terminal
    - Include the core mechanics from the spec
    - Keep it under 80 lines
    - Add comments explaining the code
    
    Respond with ONLY the Python code, no extra text.
    """
    
    response = model.generate_content(prompt)
    
    code = response.text.strip()
    code = code.replace("```python", "").replace("```", "").strip()
    
    # Save the game code to a file
    with open("generated_game.py", "w") as f:
        f.write(code)
    
    print("✅ Game Code Written!")
    print(f"📄 Saved to: generated_game.py")
    print("\n--- PREVIEW (first 10 lines) ---")
    lines = code.split("\n")[:10]
    for line in lines:
        print(line)
    
    return code

# Test it with the space shooter spec
if __name__ == "__main__":
    test_spec = {
        "title": "Galactic Fury",
        "genre": "Space Shooter",
        "description": "Pilot a starfighter against alien invaders.",
        "player_goal": "Defeat the enemy mothership.",
        "mechanics": ["Arcade Combat", "Weapon System", "Wave Encounters"],
        "difficulty": "medium"
    }
    code = coder_agent(test_spec)