# src/combat.py
import random
from .utils import print_slow

def combat(player, enemy):
    """Handle turn-based combat"""
    print_slow(f"\n⚠️  COMBAT: {enemy.name} detected!", 0.05)
    
    while enemy.health > 0 and player.health > 0:
        print(f"\nYour Health: {player.health}/{player.max_health} | Enemy: {enemy.health}")
        print("1. Shoot")
        print("2. Hack (-15 energy)")
        print("3. Use Item")
        print("4. Run")
        
        choice = input("\n> ").strip()

        if choice == "1":
            dmg = random.randint(22, 38)
            enemy.health -= dmg
            print_slow(f"Pistol hits for {dmg} damage!")
            
        elif choice == "2":
            if player.energy >= 15:
                player.energy -= 15
                dmg = random.randint(32, 52)
                enemy.health -= dmg
                print_slow(f"Neural hack successful! {dmg} damage.")
            else:
                print_slow("Not enough energy!")
                continue
                
        elif choice == "3":
            print("Inventory:", player.inventory)
            item = input("Use which? ").strip()
            if "Medpatch" in item and item in player.inventory:
                player.heal(45)
                player.inventory.remove(item)
                print_slow("Medpatch used (+45 health)")
            continue
            
        elif choice == "4":
            if random.random() > 0.45:
                print_slow("You escaped into the neon!")
                return True
            else:
                print_slow("Couldn't escape!")
        else:
            continue

        # Enemy attacks
        if enemy.health > 0:
            dmg = random.randint(12, enemy.damage + 8)
            player.health -= dmg
            print_slow(f"{enemy.name} hits you for {dmg} damage!")

    if player.health <= 0:
        print_slow("\n💀 You flatlined...")
        return False
    else:
        print_slow(f"\n{enemy.name} eliminated!")
        player.credits += enemy.reward
        print_slow(f"+¥{enemy.reward} received.")
        return True
