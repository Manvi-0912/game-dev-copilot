import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def playtester_agent(game_spec, game_code):
    print(f"\n🐛 Playtester Agent reviewing: '{game_spec['title']}'")
    print("-" * 40)
    
    prompt = f"""
    You are a Playtester Agent. Review this game code and find issues.
    
    Game Spec:
    {json.dumps(game_spec, indent=2)}
    
    Game Code:
    {game_code}
    
    Provide a review in JSON format with these fields:
    - overall_score: score out of 10
    - bugs_found: list of potential bugs
    - missing_features: list of features from spec not implemented
    - suggestions: list of 3 improvements
    - verdict: "ship it" or "needs work"
    
    Respond with ONLY the JSON, no extra text.
    """
    
    response = model.generate_content(prompt)
    
    review_text = response.text.strip()
    review_text = review_text.replace("```json", "").replace("```", "").strip()
    
    review = json.loads(review_text)
    
    print("✅ Playtester Review Complete!")
    print(f"\n🎯 Score: {review['overall_score']}/10")
    print(f"🔴 Bugs Found: {len(review['bugs_found'])}")
    for bug in review['bugs_found']:
        print(f"   - {bug}")
    print(f"\n💡 Suggestions:")
    for s in review['suggestions']:
        print(f"   - {s}")
    print(f"\n⚖️  Verdict: {review['verdict'].upper()}")
    
    return review

# Test it
if __name__ == "__main__":
    # Load the generated game code
    with open("generated_game.py", "r") as f:
        game_code = f.read()
    
    test_spec = {
        "title": "Galactic Fury",
        "genre": "Space Shooter",
        "description": "Pilot a starfighter against alien invaders.",
        "player_goal": "Defeat the enemy mothership.",
        "mechanics": ["Arcade Combat", "Weapon System", "Wave Encounters"],
        "difficulty": "medium"
    }
    
    review = playtester_agent(test_spec, game_code)