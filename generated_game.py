import random # Needed for random choices like dragon types and enemy stats

# Player's current dragon, initialized after hatching
player_dragon = None

def game_intro():
    # Welcomes player, simulates egg discovery and hatching
    print("Welcome to Dragon Tamer!")
    print("You've found a mysterious egg...")
    input("Press Enter to hatch it!") # Nurturing/waiting stage
    
    name = input("Name your dragon: ")
    d_type = random.choice(['Fire', 'Water', 'Grass']) # Random elemental type
    # Initialize player's dragon with base stats
    global player_dragon
    player_dragon = {'name': name, 'type': d_type, 'power': 10, 'hp': 50}
    print(f"It's {player_dragon['name']}, a {player_dragon['type']} dragon!") # Unique dragon born

def train():
    # Dragon training: increases power and HP (simplified growth path)
    print(f"\nTraining {player_dragon['name']}...")
    player_dragon['power'] += 2
    player_dragon['hp'] += 5 # HP also increases with training
    print(f"{player_dragon['name']} stats up! P:{player_dragon['power']} HP:{player_dragon['hp']}")
    if player_dragon['power'] > 20: print("Your dragon feels stronger, perhaps it's evolving!") # Basic evolution hint

def battle():
    # Turn-based combat against a wild dragon
    e_type = random.choice(['Fire', 'Water', 'Grass']) # Random enemy type
    enemy = {'name': f'Wild {e_type}', 'type': e_type, 'power': random.randint(8,15), 'hp': random.randint(30,60)}
    print(f"\nA {enemy['name']} ({enemy['type']}, P:{enemy['power']}, HP:{enemy['hp']}) appeared!")

    # Battle loop: continues until one dragon's HP reaches 0 or below
    while player_dragon['hp'] > 0 and enemy['hp'] > 0:
        dmg_p = player_dragon['power'] # Player's base damage
        # Apply elemental advantage/weakness
        if (player_dragon['type'] == 'Fire' and e_type == 'Grass') or \
           (player_dragon['type'] == 'Water' and e_type == 'Fire') or \
           (player_dragon['type'] == 'Grass' and e_type == 'Water'): dmg_p += 5
        enemy['hp'] -= dmg_p # Player attacks
        print(f"{player_dragon['name']} hits {enemy['name']} for {dmg_p} dmg! Enemy HP: {max(0,enemy['hp'])}")
        if enemy['hp'] <= 0: break # Check if enemy fainted

        player_dragon['hp'] -= enemy['power'] # Enemy attacks
        print(f"{enemy['name']} hits {player_dragon['name']} for {enemy['power']} dmg! Your HP: {max(0,player_dragon['hp'])}")
    
    # Battle outcome and rewards/penalties
    if player_dragon['hp'] <= 0:
        print(f"\n{player_dragon['name']} fainted! You lost the battle. Game Over.")
        exit() # Player goal not achieved if dragon faints
    else:
        print(f"\n{player_dragon['name']} won! Power +1.") # Training/evolution mechanic
        player_dragon['power'] += 1
        # Restore player dragon's HP, scaling with new power level
        player_dragon['hp'] = 50 + (player_dragon['power'] - 10) * 2

def main_game_loop():
    # Main game loop for player interaction
    game_intro() # Start the adventure!

    while True: # Game continues until player exits or loses
        # Display current dragon stats
        print(f"\n--- {player_dragon['name']} ({player_dragon['type']}) P:{player_dragon['power']} HP:{player_dragon['hp']} ---")
        print("1. Train | 2. Battle | 3. Exit") # Menu options
        choice = input("Action: ").strip()

        if choice == '1': train() # Dragon Training & Evolution
        elif choice == '2': battle() # Turn-based Dragon Combat
        elif choice == '3': print("Thanks for playing Dragon Tamer!"); break # Exit game
        else: print("Invalid choice. Try again.")

# Ensures main_game_loop runs when script is executed
if __name__ == "__main__":
    main_game_loop()