"""."""
# !/usr/bin/env python3
# pylint: disable=missing-module-docstring


import random


class Intelligence():
    """Intelligence Class."""

    orders = [True, False, True]

    def __init__(self, level):
        """."""
        self.level = level

    def act_easy(self):
        """Return decision as an easy level."""
        return random.choice(self.orders)

    def act_normal(self, player):
        """Control decision when level is Normal."""
        if player.get_score() < 10:
            print("Computer: Hmmmmm, my score is low anyway!!")
            return True
        return self.act_easy()

    def act_hard(self, value):
        """."""
        """Notice that the computer has ability to cheat."""
        print("value ", value)
        if self.cheat_decison() and value not in (1, 6):
            print("Computer: I think my score gonna be higher now!")
            return True

        elif self.cheat_decison():
            print("bst bst -->  Computer CHEATS!!")
            return False

        print("Computer: I'm NOT a cheater like you!!")
        return self.act_easy()

    def get_inti_decision(self, player, dice_value):
        """Currying ap  pend to level."""
        if self.level == "normal":
            return self.act_normal(player)

        if self.level == "hard":
            return self.act_hard(dice_value)
        return self.act_easy()

    def cheat_decison(self):
        """."""
        return random.choice(self.orders)
