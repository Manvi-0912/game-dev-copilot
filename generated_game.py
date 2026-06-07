import random # For random chances in combat and evasion

# Game state variables: Player health (hp), damage (dmg), upgrade points (upgrades)
hp, dmg, upgrades = 100, 20, 0 
# Current wave (wave) and total waves (max_waves), including the final boss
wave, max_waves = 1, 5 

# Game introduction
print("GALACTIC ASSAULT\nPilot your ship, protect the galaxy!\n")

# Main game loop: Continues as long as the player is alive and there are waves left
while hp > 0 and wave <= max_waves:
    print(f"\n--- WAVE {wave} ---")
    # Enemy health (eh) and damage (ed) scale per wave; final boss (max_waves) has fixed higher stats
    eh = 250 if wave == max_waves else 50 + (wave * 10) 
    ed = 40 if wave == max_waves else 15 + (wave * 5) 
    print(f"Enemy Health: {eh} | Your Health: {hp} | Upgrades: {upgrades}")

    # Combat loop for the current wave: continues until enemy or player is defeated
    while eh > 0 and hp > 0:
        action = input("Action (attack/evade/upgrade): ").lower()

        if action == "attack": # Player chooses to attack
            print(f"You fire, dealing {dmg} damage!")
            eh -= dmg # Decrease enemy health
            if eh > 0: # If enemy is still alive, they counter-attack
                if random.random() < 0.7: # 70% chance for enemy to hit player
                    hp -= ed; print(f"Enemy hits! You take {ed} damage. HP: {max(0, hp)}")
                else:
                    print("Enemy attack missed!")
        elif action == "evade": # Player chooses to evade
            if random.random() < 0.6: # 60% chance to completely evade
                print("You skillfully dodge all incoming fire!")
            else: # Partial evade, player takes half damage
                hp -= ed // 2; print(f"Partial evade! Took {ed // 2} damage. HP: {max(0, hp)}")
            # Note: For simplicity, choosing "evade" means the enemy doesn't counter-attack this turn.
        elif action == "upgrade": # Player chooses to upgrade
            if upgrades > 0: # Check if upgrade points are available
                choice = input("Upgrade (health/damage): ").lower()
                if choice == "health": hp += 25; upgrades -= 1; print("Shields reinforced! +25 HP.")
                elif choice == "damage": dmg += 10; upgrades -= 1; print("Weapon enhanced! +10 Damage.")
                else: print("Invalid upgrade choice.")
            else: print("No upgrade points available.")
        else: print("Invalid action.")

    if hp <= 0: break # Break main loop if player lost during combat
    
    # If enemy defeated, progress to next wave
    print(f"Wave {wave} defeated! You scavenge resources.")
    upgrades += 1 # Gain an upgrade point
    # Small health regeneration after a wave, capped based on player's overall progress
    hp = min(100 + (wave * 5), hp + 20) 
    wave += 1 # Advance to the next wave

# Game end messages: Displays win or lose condition
print("\n--- GAME OVER ---") if hp <= 0 else print("\n--- VICTORY! ---")
print("Your ship destroyed!") if hp <= 0 else print("Galaxy saved from invasion!")