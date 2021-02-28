#!/usr/bin/env python3
# pylint: disable=missing-module-docstring


class Histogram():
    """Histogram Class."""

    user_list = []
    computer_list = []

    min = 1
    max = 6

    def add_histogram(self, player, rolled_dice):
        """
        Add to the player's list the equivalent asterisk
        append to the score thay get.
        """

        if player.get_name() != "Computer":
            self.user_list.append(rolled_dice)
        else:
            self.computer_list.append(rolled_dice)

    def print_histogram(self, name):
        """Print Histogram"""

        print("{} got the following score within thes game : ".format(name))
        for ast in self.user_list:
            print(ast * " * ")

        print("Computer got the following score within the game  : ")
        for ast in self.computer_list:
            print(ast * " * ")