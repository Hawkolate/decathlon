import unittest
from dice import Die
from dice import Dice


class TestDie(unittest.TestCase):
    """Testing the die class."""

    def test_roll(self):
        die = Die(6)
        assert die.roll() in range(1, 7)
    
    def test_freezing(self):
        die = Die(6)
        die.freeze()
        assert die.frozen == True
        die.unfreeze()
        assert die.frozen == False


if __name__ == '__main__':
    unittest.main()