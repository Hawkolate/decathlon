"""
Assigned Games:     Long Jump + Discus + 110 Metre Hurdles (if time)
"""

from dice import Dice
from games import LongJump

def main() -> None:
    
    game = LongJump("Long Jump", 1, Dice(5, 6), "Loooooooong jump...")
    game.play()

if __name__ == '__main__':
    main()