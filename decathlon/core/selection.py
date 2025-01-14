from .games import Game, LongJump, Discus, Hurdles

def select_game() -> Game:
    """Game Selection Interface."""
    names = ["Long Jump", "Discus", "110 Metre Hurdles",]
    games = [LongJump(), Discus(), Hurdles()]
    print("\nSelect a game from the list below.")
    for index, name in enumerate(names):
        print(f"{index}-[ {name} ]")
    selection = input(f"Enter a game 0-{len(names) - 1} or q to quit:\t")
    print() # Blank Line
    if selection == 'q' or selection == 'quit':
        return
    try:
        return games[int(selection)]
    except (IndexError, ValueError):
        print("No Game Selected.")
        print("Exiting...")
    