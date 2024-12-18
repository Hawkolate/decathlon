"""
Assigned Games:     Long Jump + Discus + 110 Metre Hurdles (if time)
"""

from dice import Dice
from long_jump import LongJump

def main() -> None:
    
    current_game = LongJump("Long Jump", 3, Dice(5, 6), "Loooooooong jump...")
    current_game.welcome_message()
    current_game.play()

if __name__ == '__main__':
    main()