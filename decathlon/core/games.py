from core.dice import Dice
import time as ti

def play_time(func):
    """Experimenting with decorators to track play time."""
    def wrapper(self, *args, **kwargs):
        t1 = ti.time()
        result = func(self, *args, **kwargs)
        t2 = ti.time()
        t_total = t2 - t1
        msg = f"You've played {self.name} for "
        # Could clean this up with a dictionary.
        # Might store this data in a file to track it.
        if t_total >= 3600:
           t_total /= 3600
           unit = "h"
        elif t_total >= 60:
            t_total /= 60
            unit = "m"
        else:
            unit = "s"

        print(f"You've played {self.name} for {t_total:.1f}{unit}.")
        return result
    return wrapper


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
        self.dice.reset()
        print(f"Round {round} of {self.name}")
        stop = False
        # Detect invalid sum or a stop flag.
        while (self.dice.sum_frozen_dice_values() <= 9) and (stop == False):
            self.dice.roll()
            stop = self.dice.freeze_die_position()
        self.dice.format_dice()
        return self.dice.sum_frozen_dice_values()

    @play_time
    def play(self):
        """Contains logic for the Long Jump game."""
        # Might move some of this to parent class.
        self.welcome_message()
        scores = []
        for round in range(1, self.rounds + 1):
            score = self.round(round)
            scores.append(score)
        print(scores)