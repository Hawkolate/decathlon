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
# Prevent player from abusing the roll of a frozen index to roll other dies.
# Can't easliy import core package outside for testing.
# Refactoring of the @play_time decorator.