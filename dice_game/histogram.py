# !/usr/bin/env python3
# pylint: disable=E0401

"""
Histogram Class: Recive players lists and organize printable
style considers of asterisks, each printed row equavle
the face that player got it his turn.
"""


class Histogram():
    """Histogram Class."""

    def print_histogram(self, player1, player2):
        """Print Histogram and sending players lists to
        another method to organize asterisks style."""
        print("\n{} got the following score within thes game : \n"
              .format(player1.get_name()))
        self.print_asterisk(player1.get_score_list())

        print("\n{} got the following score within thes game : \n"
              .format(player2.get_name()))
        self.print_asterisk(player2.get_score_list())

    @staticmethod
    def print_asterisk(player_list):
        """Print the equavelent asterisks in player list."""
        list(map(lambda x: print(x * " * "), player_list))
