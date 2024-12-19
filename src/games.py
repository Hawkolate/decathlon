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
            print(f"{msg[:-2]}.")
        else:
            print(msg)
        print(self.description)


    def play(self):
        """Method intended to be over written by subclasses."""
        print(f"Currently playing, {self.name}")

class LongJump(Game):
    
    def __init__(self, name, rounds: int, dice: Dice, description: str):
        super().__init__(name, rounds, dice, description)

    
    def round(self, round) -> int:
        print(f"Round {round} of {self.name}")
        # Need to get frozen die values.
        while sum() <= 9:
            self.dice.roll()
            self.dice.freeze_dice()

    
    def play(self):
        """Contains logic for the Long Jump game."""
        # Might move some of this to parent class.
        self.welcome_message()
        scores = []
        for round in range(1, self.rounds + 1):
            score = self.round(round)
            scores.append(score)
