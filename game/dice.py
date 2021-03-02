
#  pylint: disable=missing-module-docstring

import random


class Dice():
    """Dice Class."""

    lowest = 1
    highest = 6

    def __init__(self):
        """Generate the number rolled on the dice."""
        self.rolled_dice = random.randint(self.lowest, self.highest)

    def roll_dice(self):
        """Roll the dice."""
        self.rolled_dice = random.randint(self.lowest, self.highest)

    def get_dice(self):
        """Return the rolled dice value."""
        return self.rolled_dice
