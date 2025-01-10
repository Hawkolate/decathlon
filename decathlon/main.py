"""
Assigned Games:     Long Jump + Discus + 110 Metre Hurdles (if time)
"""

from core import select_game

def main() -> None:
    print("Welcome to Decathlon!")
    try:
        while True:
            game = select_game()
            if game == None:
                break
            else:
                game.play()
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == '__main__':
    main()

"""Current Issues."""
# Index select_game() from 1 instead of 0.
# Clean up dice freezing logic.
# Add check to see if all dice are frozen.
# Can't easliy import core package outside for testing.
# Refactoring of the @play_time decorator.