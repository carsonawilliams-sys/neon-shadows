# src/enemy.py
import random

class Enemy:
    def __init__(self, name, health, damage, reward):
        self.name = name
        self.health = health
        self.damage = damage
        self.reward = reward
