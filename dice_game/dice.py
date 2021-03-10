#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Present Die object used in the game."""

import random
# import os
# cwd = os.getcwd()
# import sys


class Dice():
    """Dice Class."""

    def __init__(self):
        """Generate the number rolled on the dice."""
        self.lowest = 1
        self.highest = 6
        self.rolled_dice = random.randint(self.lowest, self.highest)

    def roll_dice(self):
        """Roll the dice and initialize random value."""
        self.rolled_dice = random.randint(self.lowest, self.highest)

    def get_dice(self):
        """Return the rolled dice face."""
        return self.rolled_dice
