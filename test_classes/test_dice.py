#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import random
#import sys
#sys.path.append('dice_game')
from dice_game.dice import Dice


class TestDiceClass(unittest.TestCase):
    """Dice class Test"""

    def setUp(self):
        """Runs first."""
        self.faces = [1, 2, 3, 4, 5, 6]

    def test_init_(self):
        """Test the created instance"""
        dice = Dice()
        self.assertIsInstance(dice, Dice)

    def test_roll_dice(self):
        """Test that the rolled value is in the list above"""
        dice = Dice()
        exp = random.randint(dice.lowest, dice.highest)
        res = dice.lowest <= exp <= dice.highest
        self.assertIn(exp, self.faces)
        self.assertTrue(res)

        # another test
        dice.roll_dice()
        self.assertIn(dice.rolled_dice, self.faces)

    def test_get_dice(self):
        """Testing the returned value from rolling a die"""
        dice = Dice()
        exp = dice.get_dice()
        self.assertIn(exp, self.faces)