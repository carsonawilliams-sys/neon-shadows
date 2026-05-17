import random
import time
import sys

class Player:
    def __init__(self, name="Ghost"):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.energy = 85
        self.max_energy = 85
        self.credits = 650
        self.reputation = 12
        self.inventory = ["Basic Pistol", "Quickheal Medpatch", "Street Cred Chip"]
        self.cyberware = ["Neural Jack"]
        self.location = "The Sprawl"
        self.level = 1

    def show_stats(self):
        print("\n" + "═"*65)
        print(f"   RUNNER: {self.name.upper()}     LEVEL: {self.level}")
        print(f"   Health: {self.health}/{self.max_health}    Energy: {self.energy}/{self.max_energy}")
        print(f"   Credits: ¥{self.credits:,}     Reputation: {self.reputation}/100")
        print(f"   Location: {self.location}")
        print("═"*65)

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def restore_energy(self, amount):
        self.energy = min(self.max_energy, self.energy + amount)


class Enemy:
    def __init__(self, name, health, damage, reward):
        self.name = name
        self.health = health
        self.damage = damage
        self.reward = reward


locations = {
    "The Sprawl": ["Neon Bazaar", "Underground Bar", "Black Market Alley", "Abandoned Arcade"],
    "Neon Bazaar": ["The Sprawl", "Corp Security Checkpoint"],
    "Underground Bar": ["The Sprawl", "Fixer's Booth"],
    "Black Market Alley": ["The Sprawl"],
    "Fixer's Booth": ["Underground Bar"],
    "Corp Security Checkpoint": ["Neon Bazaar"],
    "Abandoned Arcade": ["The Sprawl"]
}

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def combat(player, enemy):
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
                print_slow("You escaped!")
                return True
            else:
                print_slow("Couldn't escape!")
        else:
            continue

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


def explore(player):
    current = player.location
    print(f"\n📍 Current Location: {current}")
    print("Available destinations:")
    for loc in locations.get(current, []):
        print(f"  → {loc}")

    dest = input("\nWhere do you want to go? (or 'explore'): ").strip()

    if dest in locations.get(current, []):
        player.location = dest
        print_slow(f"\nMoving to {dest}...")
        time.sleep(1.2)

        roll = random.random()
        if roll < 0.3:
            # Combat
            enemies = [
                Enemy("Street Thug", 50, 18, 160),
                Enemy("Corporate Security", 65, 24, 240),
                Enemy("Augmented Gangster", 85, 30, 350)
            ]
            combat(player, random.choice(enemies))
        elif roll < 0.5 and player.location == "Fixer's Booth":
            print_slow("\nFixer has a job for you...")
            if input("Accept? (y/n): ").lower() == 'y':
                player.credits += 2200
                player.reputation += 8
                print_slow("Job completed successfully!")

    elif dest.lower() in ["explore", ""]:
        print_slow("Scanning the area...")
        if random.random() > 0.55:
            loot = random.choice(["Quickheal Medpatch", "¥400 Credchip", "Energy Drink"])
            if "Credchip" in loot:
                player.credits += 400
            else:
                player.inventory.append(loot)
            print_slow(f"Found: {loot}")
        else:
            print_slow("Nothing useful here.")


def main():
    print("\n" + "═"*70)
    print_slow("       NEON SHADOWS: CHROME & BLOOD")
    print_slow("            Cyberpunk Text RPG")
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
                print_slow("\nBlack Market Dealer: What do you need?")
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
            player.restore_energy(999)
            print_slow("Autodoc restored your systems.")
        elif choice == "4":
            print("\nInventory:", player.inventory)
            print("Cyberware:", player.cyberware)
        elif choice == "5":
            print_slow(f"\n{player.name} disconnects... Stay frosty.")
            break
        else:
            print_slow("Invalid choice.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nConnection terminated.")
