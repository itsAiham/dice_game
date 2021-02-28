#!/usr/bin/env python3



"""
Create the decision for the next computer move
"""

import random


class Intelligence():
    """Intelligence Class."""

    orders = [True, False, True]

    def __init__(self, level):
        self.level = level

    def act_easy(self):
        """Return decision as an easy level."""

        print("act easy")
        return random.choice(self.orders)

    def act_normal(self, player):
        """Control decision when level is Normal."""

        print("acting normal")
        if player.get_score() < 10:
            print("Low score")
            return True
        return self.act_easy()

    def act_hard(self, value):
        """Method control dicison when level is hard.
        Notice that the computer has ability to cheat."""

        print("ACTIIGN HARD")
        cheat_decison = random.choice(self.orders)
        if cheat_decison and value not in (1, 6):
            print("Computer is also a CHEATER!!")
            return True
        return self.act_easy()

    def get_inti_decision(self, player, dice_value):
        """Currying append to level."""
        if self.level == "normal":
            return self.act_normal(player)

        if self.level == "hard":
            return self.act_hard(dice_value)

        return self.act_easy()