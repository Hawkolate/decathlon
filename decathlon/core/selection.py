from .dice import Dice
from .games import Game, LongJump
# Discus

def select_game() -> Game:
    """Game Selection Interface."""
    games = {
        # These should be refactored and made the defaults.
         "Long Jump": LongJump("Long Jump", 3, Dice(5, 6), "Loooooooong jump..."),
         "Discus": Game("Discus", 1, Dice(5, 6), "we be throwin errors here?"),
         "110 Metre Hurdles": Game("110 Metre Hurdles", 2, Dice(5, 6), "Don't fall down?")
    }
    print("\nSelect a game from the list below.")
    # Change this to a numerical list selction over case-sensitive names.
    for name in games.keys():
        print(f"|[ {name} ]|")
    selection = input("Enter a game or q to quit:\t")
    print()
    if selection in games.keys():
        return games[selection]
    elif selection == 'q' or selection == 'quit':
        return
    else:
        print("No Game Selected.")
    