from .dice import Dice
from .games import Game, LongJump
# Discus

def select_game() -> Game:
    """Game Selection Interface."""
    names = ["Long Jump", "Discus", "110 Metre Hurdles",]
    games = [
        LongJump(),
        Game("Discus", 1, Dice(5, 6), "we be throwin errors here?"),
        Game("110 Metre Hurdles", 2, Dice(5, 6), "Don't fall down?"),
    ]
    print("\nSelect a game from the list below.")
    for index, name in enumerate(names):
        print(f"{index}-[ {name} ]")
    selection = input("Enter a game or q to quit:\t")
    print()
    if selection == 'q' or selection == 'quit':
        return
    try:
        return games[int(selection)]
    except (IndexError, ValueError):
        print("No Game Selected.")
        print("Exiting...")
    