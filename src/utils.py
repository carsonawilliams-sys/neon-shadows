# src/utils.py
import time
import sys

def print_slow(text, delay=0.03):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Clear terminal screen"""
    print("\033[H\033[J", end="")
