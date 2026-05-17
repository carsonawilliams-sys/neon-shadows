# src/utils.py
import time
import sys

def print_slow(text, delay=0.03):
    """Typewriter effect for immersive cyberpunk feel"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def clear_screen():
    """Clear the terminal screen"""
    print("\033[H\033[J", end="")
