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
        if (die_amount > 9 or die_amount < 1) or (sides > 9 or sides < 1):
            # Limiting values to avoid formatting complexities.
            raise ValueError("Die amount and the number of sides must in a range of 1-9.")
        self.die_amount = die_amount
        self.sides = sides
        self.frozen_dice = []
        self.dice = []
        self.reroll = True
        for i in range(die_amount + 1):
            current_die = Die(self.sides)
            self.dice.append(current_die)


    def roll(self, hidden=False):
        """Rolls all dice."""
        if self.reroll == True:
            self.rolls = []
            for die in self.dice:
                die.roll()
                self.rolls.append(die.num)
            if hidden == False:
                self.format_dice()
        else:
            self.format_dice() 
            self.reroll = True
    

    def reset(self):
        """Unfreezes and rolls the dice for a new round."""
        for die in self.dice:
            die.unfreeze()
        self.frozen_dice
        return self.roll(hidden=True)


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


    def frozen_index(self, index: int, freeze: bool):
        """Freezes or unfreezes a given die based on its index and boolean value."""
        try:
            if freeze:
                self.dice[index].freeze()
                self.frozen_dice.append(index)
            else:
                self.dice[index].unfreeze()
                self.frozen_dice.remove(index)
        except IndexError:
            # Need to prevent die reroll after this point.
            self.reroll = False
            print("Please enter a valid index.")
            

    
    def sum_frozen_dice_values(self):
        """Sums the values of all frozen dice."""
        values = []
        # Sort of inefficient, but it gets the job done.
        for die in self.dice:
            if die.frozen == True:
                values.append(die.num)
        return sum(values)

    
    def freeze_die_position(self):
        """Take index as input, catch any errors and unwanted behaviour."""
        try:
            to_freeze = input(f"Enter a die position to freeze 0-{self.die_amount} or `stop` to end the round:\t")
            if to_freeze == "stop":
                return True
            else:
                # Prevent player from abusing the roll of a frozen index to roll other dice.
                to_freeze = int(to_freeze)
                if self.dice[to_freeze].frozen == True:
                    raise ValueError
                else:
                    self.frozen_index(to_freeze, True)
                return False
        except (ValueError, IndexError):
            self.reroll = False
            print("Please enter a valid position.")
            return False
        
    def satisfied_value(self):
        """Roll dice until stopping conditions."""
        self.roll()
        to_roll = input("Would you like to continue rolling (yes/No)?\t").lower()
        no_words = ["no", "n"]
        if to_roll in no_words:
            stop = True
        else:
            stop = False


if __name__ == '__main__':
    my_dice = Dice(5, 6)
    my_dice.frozen_index(4, True)
    my_dice.frozen_index(2, True)
    for i in range(12):
        my_dice.roll()
    print(my_dice.frozen_dice)
    my_dice.reset()