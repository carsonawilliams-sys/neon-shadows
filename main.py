# main.py
import random
from src.player import Player
from src.enemy import Enemy
from src.combat import combat
from src.world import get_locations
from src.utils import print_slow

def explore(player):
    """Handle exploration and travel"""
    current = player.location
    locations = get_locations()
    
    print(f"\n📍 Current Location: {current}")
    print("Available destinations:")
    for loc in locations.get(current, []):
        print(f"  → {loc}")

    dest = input("\nWhere do you want to go? (or 'explore'): ").strip()

    if dest in locations.get(current, []):
        player.location = dest
        print_slow(f"\nMoving to {dest} through the sprawl...")
        time.sleep(1.2)

        roll = random.random()
        if roll < 0.3:
            # Random combat
            enemies = [
                Enemy("Street Thug", 50, 18, 160),
                Enemy("Corporate Security", 65, 24, 240),
                Enemy("Augmented Gangster", 85, 30, 350)
            ]
            combat(player, random.choice(enemies))
            
        elif roll < 0.5 and player.location == "Fixer's Booth":
            print_slow("\n🔵 A Fixer approaches with a job...")
            if input("Accept the job? (y/n): ").lower() == 'y':
                player.credits += 2200
                player.reputation += 8
                print_slow("Job completed. Payment received.")

    elif dest.lower() in ["explore", ""]:
        print_slow("Scanning the shadows...")
        if random.random() > 0.55:
            loot = random.choice(["Quickheal Medpatch", "¥400 Credchip", "Energy Drink"])
            if "Credchip" in loot:
                player.credits += 400
            else:
                player.inventory.append(loot)
            print_slow(f"Found: {loot}")
        else:
            print_slow("Only rain and flickering holograms...")


def main():
    print("\n" + "═"*70)
    print_slow("       NEON SHADOWS: CHROME & BLOOD")
    print_slow("            Cyberpunk Runner RPG  v0.3")
    print("═"*70)

    name = input("\nEnter your street name, runner: ").strip() or "Ghost"
    player = Player(name)

    print_slow(f"\nJacking in as {name}...\n")

    while player.health > 0:
        player.show_stats()
        
        print("\nActions:")
        print("1. Explore / Travel")
        print("2. Black Market")
        print("3. Rest (Autodoc)")
        print("4. Inventory")
        print("5. Quit")
        
        choice = input("\n> ").strip()

        if choice == "1":
            explore(player)
        elif choice == "2":
            if player.location == "Black Market Alley":
                print_slow("\nBlack Market Dealer: What do you need, runner?")
                if player.credits >= 550:
                    if input("Buy Cyberarm (+25 Max Health) for ¥550? (y/n): ").lower() == 'y':
                        player.credits -= 550
                        player.max_health += 25
                        player.heal(25)
                        player.cyberware.append("Cyberarm")
                        print_slow("Cyberarm installed!")
            else:
                print_slow("Black Market not available here.")
        elif choice == "3":
            player.heal(40)
            player.restore_energy()
            print_slow("Autodoc pod restored your systems.")
        elif choice == "4":
            print("\nInventory:", player.inventory)
            print("Cyberware:", player.cyberware)
        elif choice == "5":
            print_slow(f"\n{player.name} disconnects... Stay frosty, runner.")
            break
        else:
            print_slow("Invalid choice.")

    print_slow("\nGame Over.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nConnection terminated.")
