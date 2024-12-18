from dice import Dice
from game import Game

class LongJump(Game):
    
    def __init__(self, name: str, rounds: int, dice: Dice, description: str):
        super().__init__(name, rounds, dice, description)
    
    def play(self):
        pass