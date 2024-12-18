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
        self.dice = [] 
        for i in range(die_amount + 1):
            current_die = Die(self.sides)
            if i == 2:
                current_die.freeze()
            self.dice.append(current_die)
        
    def roll(self):
        """Rolls all dice."""
        self.rolls = []
        for die in self.dice:
            die.roll()
            self.rolls.append(die.num)
        return self.rolls
    
    def reset(self):
        """Unfreezes and rolls the dice for a new round."""
        for die in self.dice:
            die.unfreeze()
        return self.roll()

if __name__ == '__main__':
    my_dice = Dice(5, 6)
    for i in range(12):
        print(my_dice.roll())
    data = my_dice.reset()
    print(data)
    
