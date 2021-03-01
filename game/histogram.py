#!/usr/bin/env python3
# pylint: disable=missing-module-docstring


class Histogram():
    """Histogram Class."""

    def add_histogram(self, player, rolled_dice):
        """
        Add to the player's list the equivalent asterisk
        append to the score thay get.
        """
        player.score_list.append(rolled_dice)

    def print_histogram(self, player1, player2):
        """Print Histogram"""

        print("\n{} got the following score within thes game : \n".format(player1.get_name()))
        self.print_asterisk(player1.score_list)

        print("\n{} got the following score within thes game : \n".format(player2.get_name()))
        self.print_asterisk(player1.score_list)

    def print_asterisk(self, player_list):
        """Print the equavelent asterisks in the list."""
        list(map(lambda x : print(x * " * "), player_list))
