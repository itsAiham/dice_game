#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from player import Player
from dice import Dice
from histogram import Histogram


class Game():

    """Game Class."""

    win_pig = 10
    still_going = True

    def __init__(self):
        print("Game Starts!\n")

        self.human_player = Player("USER",  bool)
        self.computer_player = Player("Computer",  bool)
        self.histogram = Histogram()
        self.computer_player.set_level("easy")
        self.dice = Dice()

    def roll(self):
        """Roll the dice."""
        force_stop = self.console(self.human_player)

        if not force_stop and self.get_game_status:
            self.computer_turn()

    def console(self, player):
        """Synchronize between players's scores and rolled dice """

        self.print_out_dice(player.get_name(), self.dice.get_dice())
        player.change_score(self.dice.get_dice())
        self.histogram.add_histogram(player, self.dice.get_dice())

        self.print_score(player)

        if self.dice.get_dice() in (1, 6):
            self.dice.roll_dice()
            return False

        if player.get_score() >= self.win_pig:
            self.histogram.print_histogram(self.human_player.get_name())
            self.end_game(player)
            # return False
            # self.end_game(player)

        self.dice.roll_dice()
        return True

    def computer_turn(self):
        """Take orders from Intelligence class to control the decison"""
        print("Start of computer method")

        while True:
            reaction = self.computer_player.reaction.get_inti_decision(
                       self.computer_player,
                       self.cheat())

            if not self.get_game_status():
                break

            if not reaction:
                print(self.still_going, "statusu")
                print(">>>>>  Computer decide to hold <<<<<")
                break

            force_stop = self.console(self.computer_player)
            # print("computer dicide to ", reaction)

            if not force_stop:
                break

    def cheat(self):
        """Return the rolled dice"""

        return self.dice.get_dice()

    def check_levels(self, level):
        """Check if the entered level is valid"""

        levels = ("easy", "normal", "hard")
        if level in levels:
            self.computer_player.set_level(level)
        else:
            raise ValueError("This kind of level is not available!!")

    def change_name(self, name):
        """Change player name."""
        self.human_player.set_name(name)

    @staticmethod
    def print_score(player):
        """Print out player score and name."""
        print("{} score is {}". format(player.get_name(),
                                       player.get_score()))

    @staticmethod
    def print_out_dice(name, number):
        """Print out the dice"""
        print("{} got:". format(name))
        print("  ______")
        print(r" |\______\ ")
        print(" ||      |")
        print(" ||   {}  |".format(number))
        print(r" \|______|")

    def end_game(self, player):
        """Print the winner. """
        self.still_going = False
        print("WOW! Congra {} you won the game!". format(player.get_name()))

    def get_game_status(self):
        """Check the game status"""
        return self.still_going