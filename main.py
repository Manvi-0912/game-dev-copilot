import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import time

# Import all 3 agents
from designer_agent import designer_agent
from coder_agent import coder_agent
from playtester_agent import playtester_agent

print("=" * 50)
print("🎮 GAME DEV CO-PILOT")
print("Powered by 3 AI Agents")
print("=" * 50)

# Get game idea from user
game_idea = input("\nEnter your game idea: ")

print("\n🚀 Starting Multi-Agent Pipeline...")
print("=" * 50)

# AGENT 1: Designer creates the spec
spec = designer_agent(game_idea)

print("\n⏭️  Passing spec to Coder Agent...")
time.sleep(30)

# AGENT 2: Coder writes the game
code = coder_agent(spec)

print("\n⏭️  Passing code to Playtester Agent...")
time.sleep(30)

# AGENT 3: Playtester reviews the code
review = playtester_agent(spec, code)

print("\n" + "=" * 50)
print("✅ PIPELINE COMPLETE!")
print(f"🎮 Game: {spec['title']}")
print(f"📄 Code saved to: generated_game.py")
print(f"🎯 Quality Score: {review['overall_score']}/10")
print(f"⚖️  Verdict: {review['verdict'].upper()}")
print("=" * 50)
print("\nRun 'python generated_game.py' to play your game!")