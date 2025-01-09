"""
Assigned Games:     Long Jump + Discus + 110 Metre Hurdles (if time)
"""

from core import select_game

def main() -> None:
    print("Welcome to Decathlon!")
    while True:
        game = select_game()
        if game == None:
            break
        else:
            game.play()
            


if __name__ == '__main__':
    main()

"""Current Issues."""
# Work on actual game logic.
# Index select_game() from 1 instead of 0.
# Clean up dice freezing logic.
# Add check to see if all dice are frozen.
# Can't easliy import core package outside for testing.
# Refactoring of the @play_time decorator.