#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=E0401

"""Test dice file."""

import unittest
import random
from app.dice import Dice


class TestDiceClass(unittest.TestCase):
    """Dice class Test."""

    def setUp(self):
        """Run at the beginning of the test."""
        self.faces = (1, 2, 3, 4, 5, 6)

    def test_init(self):
        """Test the created instance."""
        dice = Dice()
        self.assertIsInstance(dice, Dice)

    def test_roll_dice(self):
        """Test that the rolled value is in the list above."""
        dice = Dice()
        exp = random.randint(dice.lowest, dice.highest)
        res = dice.lowest <= exp <= dice.highest
        self.assertIn(exp, self.faces)
        self.assertTrue(res)

        # another assertion
        dice.roll_dice()
        self.assertIn(dice.rolled_dice, self.faces)

    def test_get_dice(self):
        """Tests the returned value after rolling a die."""
        dice = Dice()
        exp = dice.get_dice()
        self.assertIn(exp, self.faces)
