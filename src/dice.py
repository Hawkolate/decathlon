import random

class Die:

    def __init__(self, sides: int) -> None:
        """Initializes a die."""
        self.sides = sides
        self.frozen = False
        self.num = self.roll()

    def roll(self):
        """Rolls the die."""
        if self.frozen:
            return self.num
        else:
            self.num = random.randrange(1, self.sides + 1)
            return self.num
    
    def freeze(self):
        self.frozen = True
    
    def unfreeze(self):
        self.frozen = False

class Dice:
    
    def __init__(self, die_amount: int, sides: int):
        """Creates a list of dice which can be manipulated."""
        self.die_amount = die_amount
        self.sides = sides
        self.frozen_dice = []
        self.dice = [] 
        for i in range(die_amount + 1):
            current_die = Die(self.sides)
            self.dice.append(current_die)
    
    def format_dice(self):
        """Displays the dice in an aesthestic way.
        +---+-F-+
        | 6 |[5]|
        +---+---+
        """
        top_header = "+"
        horizontal_side = "---+"
        values = ""
        # We know the amount of dice, if a die is frozen, 
        # change the header and format its value.
        for i, j in enumerate(self.rolls):
            # Header logic
            if self.dice[i].frozen == True:
                top_header += "-F-+"
                values += f"|[{j}]"
            else:
                top_header += horizontal_side
                values += f"| {j} "

        bottom_header = "+" + (horizontal_side * (self.die_amount + 1))
        print(top_header + "\n" + values + "|" + "\n" + bottom_header)
        
    def roll(self):
        """Rolls all dice."""
        self.rolls = []
        for die in self.dice:
            die.roll()
            self.rolls.append(die.num)
        self.format_dice()
        return self.rolls
    
    def reset(self):
        """Unfreezes and rolls the dice for a new round."""
        for die in self.dice:
            die.unfreeze()
        self.frozen_dice
        return self.roll()
    
    def frozen_index(self, index: int, freeze: bool):
        """Freezes or unfreezes a given die based on its index and boolean value."""
        if freeze:
            self.dice[index].freeze()
            self.frozen_dice.append(index)
        else:
            self.dice[index].unfreeze()
            self.frozen_dice.remove(index)
    
    def get_frozen_dice_values(self):
        values = []
    
    def find_index_from_value(self, value):
        """From the value of a die, find an index."""
        for index, die in self.rolls:
            if die == value:
                return index
    
    def freeze_dice(self):
        to_freeze = input(f"Enter a die to freeze 1-{self.die_amount + 1}:\t")
        if to_freeze == "q" or to_freeze == "quit":
            return
        else:
            self.frozen_index(int(to_freeze) - 1, True)


if __name__ == '__main__':
    my_dice = Dice(5, 6)
    my_dice.frozen_index(4, True)
    my_dice.frozen_index(2, True)
    for i in range(12):
        my_dice.roll()
    print(my_dice.frozen_dice)
    my_dice.reset()