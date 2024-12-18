from dice import Dice

class Game:
    """Intended to be used a base for dice based games."""

    def __init__(self, name: str, rounds: int, dice: Dice, description: str):
        self.name = name
        self.rounds = rounds
        self.dice = dice
        self.description = description
    
    def welcome_message(self):
        msg = f"You are now playing {self.name}, it has {self.rounds} rounds."
        if self.rounds == 1:
            print(msg[:-2])
        else:
            print(msg)


    def play(self):
        """Method intended to be over written by subclasses."""
        print(f"Currently playing, {self.name}")

