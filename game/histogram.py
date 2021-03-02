"""."""
# !/usr/bin/env python3
# pylint: disable=missing-module-docstring


class Histogram():
    """Histogram Class."""

    def print_histogram(self, player1, player2):
        """Print Histogram."""
        print("\n{} got the following score within thes game : \n"
              .format(player1.get_name()))
        self.print_asterisk(player1.get_score_list())

        print("\n{} got the following score within thes game : \n"
              .format(player2.get_name()))
        self.print_asterisk(player2.get_score_list())

    def print_asterisk(self, player_list):
        """Print the equavelent asterisks in the list."""
        list(map(lambda x: print(x * " * "), player_list))
