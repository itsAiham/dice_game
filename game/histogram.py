#!/usr/bin/env python3
# pylint: disable=missing-module-docstring


class Histogram():
    """Histogram Class."""

    user1_list = []
    user2_list = []

    min = 1
    max = 6

    def __init__(self, player1):
        self.player1 = player1

    def add_histogram(self, player, rolled_dice):
        """
        Add to the player's list the equivalent asterisk
        append to the score thay get.
        """

        if player == self.player1:
            self.user1_list.append(rolled_dice)
        else:
            self.user2_list.append(rolled_dice)

    def print_histogram(self, player1, player2):
        """Print Histogram"""

        print("\n{} got the following score within thes game : ".format(player1))
        for ast in self.user1_list:
            print(ast * " * ")

        print("\n{} got the following score within thes game : ".format(player2))
        for ast in self.user2_list:
            print(ast * " * ")