"""
Assigned Games:     Long Jump + Discus + 110 Metre Hurdles (if time)
"""

from dice import Dice
from games import LongJump

def main() -> None:
    # Add a selection interface to choose a game.
    game = LongJump("Long Jump", 3, Dice(5, 6), "Loooooooong jump...")
    game.play()


if __name__ == '__main__':
    main()

# Work on quitting the program.
# Prevent Invalid Index from rerolling the dice.
# Prevent freezing of an already frozen die, which would cause all the other die's to be rerolled.
# Also add some comments! And work on error handling.
# Write some tests, Test Driven Development.