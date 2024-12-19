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
        return self.roll()
    
    def freeze_index(self, index: int, freeze: bool):
        """Freezes or unfreezes a given die based on its index."""
        if freeze:
            self.dice[index].freeze()
        else:
            self.dice[index].unfreeze()
        # Keeps track of frozen dice.
        self.frozen_dice.append(index)

if __name__ == '__main__':
    my_dice = Dice(5, 6)
    for i in range(12):
        print(my_dice.roll())
    data = my_dice.reset()
    print(data)
    
