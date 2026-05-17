# src/world.py
locations = {
    "The Sprawl": ["Neon Bazaar", "Underground Bar", "Black Market Alley", "Abandoned Arcade"],
    "Neon Bazaar": ["The Sprawl", "Corp Security Checkpoint"],
    "Underground Bar": ["The Sprawl", "Fixer's Booth"],
    "Black Market Alley": ["The Sprawl"],
    "Fixer's Booth": ["Underground Bar"],
    "Corp Security Checkpoint": ["Neon Bazaar"],
    "Abandoned Arcade": ["The Sprawl"]
}

def get_locations():
    return locations
