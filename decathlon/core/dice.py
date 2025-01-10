import random

class Die:

    def __init__(self, sides: int) -> None:
        """Initializes a die."""
        self.sides = sides
        self.frozen = False
        self.num = self.roll()


    def roll(self) -> int:
        """Rolls the die."""
        if self.frozen:
            return self.num
        else:
            self.num = random.randrange(1, self.sides + 1)
            return self.num


    def freeze(self) -> bool:
        self.frozen = True
    

    def unfreeze(self) -> bool:
        self.frozen = False


class Dice:
    
    def __init__(self, die_amount: int, sides: int) -> None:
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


    def roll(self, hidden=False) -> None:
        """Rolls all dice."""
        if self.reroll == True:
            self.rolls = []
            for die in self.dice:
                die.roll()
                self.rolls.append(die.num)
            # This allows for a roll not to be displayed.
            if hidden == False:
                self.format_dice()
        else:
            self.format_dice() 
            self.reroll = True
    

    def reset(self) -> None:
        """Unfreezes and rolls the dice for a new round."""
        for die in self.dice:
            die.unfreeze()
        self.frozen_dice = []
        self.roll(hidden=True)


    def format_dice(self) -> None:
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


    def frozen_index(self, index: int, freeze: bool) -> None:
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
    
    def all_frozen(self) -> bool:
        """Checks to see if all the dice are frozen."""
        if len(self.frozen_dice) == len(self.dice):
            return True
        else:
            return False
            

    def sum_dice_values(self) -> int:
        """Sums the values of all dice."""
        return sum(self.rolls)

    
    def sum_frozen_dice_values(self) -> int:
        """Sums the values of all frozen dice."""
        # self.frozen_dice contains indices, not values.
        values = []
        # Sort of inefficient, but it gets the job done.
        for die in self.dice:
            if die.frozen == True:
                values.append(die.num)
        return sum(values)


    def check_for_even(self) -> bool:
        """Short algorithm that returns True if it finds an even number."""
        for i, roll in enumerate(self.rolls):
            # Find the first even value to 
            if roll % 2 == 0 and self.dice[i].frozen == False:
                return True
        return False
    
    
    def freeze_die_position(self, only_even=False) -> bool:
        """Take index as input, catch any errors and unwanted behaviour."""
        # Some sketchy code with a lot of error handling.
        try:
            to_freeze = input(f"Enter a die position to freeze 0-{self.die_amount} or `stop` to end the round:\t")
            if to_freeze == "stop":
                return True
            else:
                to_freeze = int(to_freeze)
                # Account for specific freezing requirements.
                if only_even == True:
                    if self.dice[to_freeze].num % 2 != 0:
                        print("Only dice with even values may be frozen.")
                        raise ValueError
                # Prevent player from abusing the roll of a frozen index to roll other dice.
                if self.dice[to_freeze].frozen == True:
                    raise ValueError
                else:
                    self.frozen_index(to_freeze, True)
                return False
        except (ValueError, IndexError):
            self.reroll = False
            print("Please enter a valid position.")
            return False
        

    def satisfied_value(self) -> bool:
        """Roll dice until stopping conditions."""
        to_roll = input("Would you like to continue rolling (yes/No)?\t").lower()
        no_words = ["no", "n"]
        if to_roll in no_words:
            stop = True
        else:
            self.roll()
            stop = False
        return stop


if __name__ == '__main__':
    my_dice = Dice(5, 6)
    my_dice.frozen_index(4, True)
    my_dice.frozen_index(2, True)
    for i in range(12):
        my_dice.roll()
    print(my_dice.frozen_dice)
    my_dice.reset()