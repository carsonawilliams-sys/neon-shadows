import sys
from src.game import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nConnection terminated. Stay frosty.")
