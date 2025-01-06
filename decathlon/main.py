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
# Some unwanted cases allow the dice to be rerolled.
# Can't easliy import core package outside for testing.
# Refactoring of the @play_time decorator.
# Work on actual game logic.