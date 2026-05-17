# src/player.py
import random

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

    def restore_energy(self, amount=999):
        self.energy = min(self.max_energy, self.energy + amount)
