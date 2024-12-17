import random

class Die:

    def __init__(self, sides: int) -> None:
        """Initializes a die."""
        self.sides = sides
        self.num: int
        self.frozen: bool

    def roll(self):
        """Rolls the dice."""
        self.num = random.randrange(1, self.sides + 1)
        print(self.num)
    
    def freeze(self):
        self.frozen = True
    
    def unfreeze(self):
        self.frozen = False

if __name__ == '__main__':
    my_die = Die(6)
    my_die.roll()
    for i in range(12):
        my_die.roll()