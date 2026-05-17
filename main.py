import random
import time
import sys
import json
from datetime import datetime

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
        print("\n" + "═"*60)
        print(f"   RUNNER: {self.name.upper()}   |   LEVEL {self.level}")
        print(f"   Health: {self.health}/{self.max_health}   Energy: {self.energy}/{self.max_energy}")
        print(f"   Credits: ¥{self.credits:,}   Reputation: {self.reputation}/100")
        print(f"   Location: {self.location}")
        print("═"*60)

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


# ====================== GAME DATA ======================
locations = {
    "The Sprawl": ["Neon Bazaar", "Underground Bar", "Black Market Alley", "Abandoned Arcade", "Data Hub"],
    "Neon Bazaar": ["The Sprawl", "Corp Security Checkpoint"],
    "Underground Bar": ["The Sprawl", "Fixer's Booth"],
    "Black Market Alley": ["The Sprawl"],
    "Fixer's Booth": ["Underground Bar"],
    "Corp Security Checkpoint": ["Neon Bazaar"],
    "Abandoned Arcade": ["The Sprawl"],
    "Data Hub": ["The Sprawl"]
}

def print_slow(text, delay=0.028):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def combat(player, enemy):
    print_slow(f"\n⚠️  HOSTILE DETECTED — {enemy.name}!", 0.05)
    
    while enemy.health > 0 and player.health > 0:
        print(f"\n   Your Health: {player.health}/{player.max_health} | Enemy: {enemy.health}")
        print("1. Shoot Pistol")
        print("2. Neural Hack (15 energy)")
        print("3. Use Item")
        print("4. Run")
        
        choice = input("\n> ").strip()

        if choice == "1":
            dmg = random.randint(20, 37)
            enemy.health -= dmg
            print_slow(f"→ Pistol shots hit for {dmg} damage.")
            
        elif choice == "2":
            if player.energy >= 15:
                player.energy -= 15
                dmg = random.randint(30, 50)
                enemy.health -= dmg
                print_slow(f"→ Neural hack breached! {dmg} damage.")
            else:
                print_slow("Not enough energy!")
                continue
                
        elif choice == "3":
            print("Inventory:", player.inventory)
            item = input("Use which item? ").strip()
            if item in player.inventory and "Med" in item:
                player.heal(45)
                player.inventory.remove(item)
                print_slow("Medpatch applied. +45 health.")
            continue
            
        elif choice == "4":
            if random.random() > 0.4:
                print_slow("You vanished into the neon rain.")
                return True
            else:
                print_slow("Escape failed!")
        else:
            continue

        if enemy.health > 0:
            dmg = random.randint(enemy.damage-8, enemy.damage+10)
            player.health -= dmg
            print_slow(f"{enemy.name} hits you for {dmg} damage!")

    if player.health <= 0:
        print_slow("\n💀 YOU FLATLINED...")
        return False
    else:
        print_slow(f"\n✅ {enemy.name} eliminated.")
        player.credits += enemy.reward
        print_slow(f"¥{enemy.reward} transferred to your account.")
        return True


def explore(player):
    current = player.location
    print(f"\n📍 You are in: {current}")
    print("Connected nodes:")
    for loc in locations.get(current, []):
        print(f"   → {loc}")

    dest = input("\nWhere to? (or type 'explore' here): ").strip()

    if dest in locations.get(current, []):
        player.location = dest
        print_slow(f"\nTraveling to {dest} through the sprawl...")
        time.sleep(1)

        roll = random.random()
        if roll < 0.25:
            print_slow("Street vendor offers goods...")
            if player.credits >= 90 and random.random() > 0.5:
                player.credits -= 90
                player.inventory.append("Quickheal Medpatch")
                print_slow("Purchased Quickheal Medpatch.")
        elif roll < 0.48:
            enemies = [
                Enemy("Street Thug", 55, 20, 180),
                Enemy("Corporate Drone", 70, 25, 250),
                Enemy("Augmented Enforcer", 90, 32, 380)
            ]
            combat(player, random.choice(enemies))
        elif player.location == "Fixer's Booth":
            print_slow("\n🔵 Fixer whispers: 'Got a job for you...'")
            if input("Accept the run? (y/n): ").lower() == 'y':
                print_slow("Job complete. Data extracted.")
                player.credits += 2500
                player.reputation += 10
                print_slow("Payment received. Reputation increased.")

    elif dest.lower() in ["explore", "search", ""]:
        print_slow("You scan the shadows...")
        if random.random() > 0.6:
            loot = random.choice(["Quickheal Medpatch", "Energy Boost", "¥450 Credchip"])
            if "Credchip" in loot:
                player.credits += 450
            else:
                player.inventory.append(loot)
            print_slow(f"Found: {loot}")
        else:
            print_slow("Nothing but rain and broken neon.")


def main():
    print("\n" + "═"*70)
    print_slow("          NEON SHADOWS: CHROME & BLOOD")
    print_slow("                 v0.2 - DEPLOYED")
    print("═"*70)

    name = input("\nEnter your street name: ").strip() or "Ghost"
    player = Player(name)

    print_slow(f"\nWelcome to the Sprawl, {name}...\n")

    while player.health > 0:
        player.show_stats()
        
        print("\nWhat do you do?")
        print("1. Explore / Travel")
        print("2. Black Market")
        print("3. Rest in Autodoc")
        print("4. Inventory")
        print("5. Quit")
        
        choice = input("\n> ").strip()

        if choice == "1":
            explore(player)
        elif choice == "2":
            if player.location == "Black Market Alley":
                print_slow("\nBlack Market Dealer: 'Best chrome in the sprawl.'")
                if player.credits >= 520 and input("Buy Cyberarm (+25 HP) for ¥520? (y/n): ").lower() == 'y':
                    player.credits -= 520
                    player.max_health += 25
                    player.heal(25)
                    player.cyberware.append("Cyberarm")
                    print_slow("Cyberarm installed successfully.")
            else:
                print_slow("No black market here.")
        elif choice == "3":
            player.heal(40)
            player.restore_energy(999)
            print_slow("You jack into an autodoc pod... Systems restored.")
        elif choice == "4":
            print("\nInventory:", player.inventory)
            print("Cyberware:", player.cyberware)
        elif choice == "5":
            print_slow(f"\n{player.name} jacks out. Stay frosty, runner.")
            break
        else:
            print_slow("Signal lost. Try again.")

    print_slow("\nGame Over.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nConnection terminated.")
