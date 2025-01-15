from .dice import Dice
import time as ti


def play_time(func):
    """Experimenting with decorators to track play time."""
    def wrapper(self, *args, **kwargs):
        t1 = ti.time()
        result = func(self, *args, **kwargs)
        t2 = ti.time()
        t_total = t2 - t1
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

    def __init__(self, name: str, rounds: int, dice: Dice, description: str) -> None:
        self.name = name
        self.rounds = rounds
        self.dice = dice
        self.description = description
        self.scores = []
    

    def score(self) -> None:
        """Outputs scores in round order."""
        print(f"Thanks for playing.")
        for index, score in enumerate(self.scores):
            print(f"Round {index + 1}:\t{score}")


    def welcome_message(self) -> None:
        msg = f"You are now playing {self.name}, it has {self.rounds} rounds."
        if self.rounds == 1:
            print(f"{msg[:-2]}.")
        else:
            print(msg)
        print(self.description)


    def play(self) -> None:
        """Method intended to be over written by subclasses."""
        print(f"Currently playing, {self.name}")


class LongJump(Game):
    
    def __init__(self, name="Long Jump", 
        rounds=3, dice=Dice(5, 6), 
        description="Freeze at least one die per turn, total frozen must be less than 9."
        ) -> None:
        super().__init__(name, rounds, dice, description)

    
    def round(self, round) -> int:
        self.dice.reset()
        print(f"Round {round} of {self.name}")
        stop, all_frozen = (False, False)
        # Detect invalid sum or a stop flag.
        while (self.dice.sum_frozen_dice_values() < 9) and (stop == False) and (all_frozen == False):
            self.dice.roll()
            stop = self.dice.freeze_die_values()
            all_frozen == self.dice.all_frozen()
        self.dice.format_dice()
        return self.dice.sum_frozen_dice_values()


    @play_time
    def play(self) -> None:
        """Contains logic for the Long Jump game."""
        self.welcome_message()
        # Round Logic
        for round in range(1, self.rounds + 1):
            score = self.round(round)
            # Catching invalid scores over nine.
            if score >= 9 or score <= 0:
                self.scores.append(0)
            else:
                self.scores.append(score)
        self.score()
       

class Discus(Game):

    def __init__(self, name="Discus", 
        rounds=3, dice=Dice(5, 6), 
        description="Freeze at least one die per turn, you may not freeze odd dice.\
        \nIf no even dice remain, the round becomes invalid.",
        ) -> None:
        super().__init__(name, rounds, dice, description)
    
    
    def round(self, round) -> int:
        self.dice.reset()
        print(f"Round {round} of {self.name}")
        valid, stop, all_frozen = (True, False, False)
        # Valid becomes False if there are no even unfrozen values left.
        # The loop stops if the player enters stop.
        # If all dice are frozen, end the loop.
        while (valid == True) and (stop == False) and (all_frozen == False):
            self.dice.roll()
            # Checking at the start makes the game better for the player.
            valid = self.dice.check_for_even() # Needs to happen at start to catch changes after rolling.
            stop = self.dice.freeze_die_values(only_even=True)
            all_frozen = self.dice.all_frozen()
        self.dice.format_dice()
        if valid == False:
            return 0
        else:
            return self.dice.sum_frozen_dice_values()


    @play_time
    def play(self) -> None:
        """Contains logic for Discus Game."""
        self.welcome_message()
        # Round Logic
        for round in range(1, self.rounds + 1):
            score = self.round(round)
            self.scores.append(score)
        self.score()
         

class Hurdles(Game):

    def __init__(self, name="110 Metre Hurdles", 
        rounds=1, dice=Dice(5, 6), 
        description="Roll until you are satisfied with the dice total.\nUp to five rerolls are allowed."
        ) -> None:
        super().__init__(name, rounds, dice, description)
 

    def sum_score(self) -> None:
        score = self.dice.sum_dice_values()
        print(f"Total Score:\t{score}")


    @play_time
    def play(self) -> None:
        """Contains logic for Hurdles Game."""
        # Throw all five dice up to six times.
        self.dice.reset()
        self.welcome_message()
        self.dice.roll()
        stop = False
        roll_limit = 5
        count = 0
        while (count < roll_limit) and (stop == False):
            rolls_left = roll_limit - count
            if rolls_left == 1:
                end = "roll remaining."
            else:
                end = "rolls remaining."
            print(f"You have {roll_limit - count} {end}") 
            self.sum_score()
            stop = self.dice.satisfied_value()
            count += 1
        self.sum_score()