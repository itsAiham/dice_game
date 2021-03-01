#!/usr/bin/env python3,
# pylint: disable=missing-module-docstring




from player import Player
from dice import Dice
from histogram import Histogram
from intelligence import Intelligence


class Game():

    """Game Class."""

    win_pig = 10
    still_going = True
    # playing_now = object

    def __init__(self):
        print("Game Starts!\n")

        self.computer_controlar = bool
        self.dice = Dice()


    def create_player(self, player_amount):
        player1_name = input("Enter the first player's name >> ")
        self.player1 = Player(player1_name,  bool)
        self.playing_now = self.player1  #  Hold player object temporarily
        self.histogram = Histogram(self.player1)

        if player_amount == 2:
            print("Created another player")
            player2_name = input("Enter the second player's name >> ")
            self.player2 = Player(player2_name,  bool)
            # print(self.get_computer_controler())
            # return self.get_computer_controler()

        else:
            print("Created computer player")
            print(self.get_computer_controler())
            self.computer_player = Player("Computer",  bool)
            self.computer_player.set_level("easy")
            self.player2 = self.computer_player

    def switcher(self):
        """Switch turns between players."""
        if self.get_computer_controler():
            print("found computer controler")
            return self.computer_turn()

        if self.playing_now == self.player1 and not self.get_computer_controler():
            self.playing_now = self.player2
            print(">>>>> Start {} turn <<<<<\n". format(self.playing_now.get_name()))

        else:
            self.playing_now = self.player1
            print(">>>>> Start {} turn <<<<<\n".format(self.player1.get_name()))

    def roll(self):
        """Roll the dice."""
        force_stop = self.console(self.playing_now)

        if not force_stop and self.get_game_status():
            self.switcher()

    def console(self, player):
        """Synchronize between players's scores and rolled dice """
        self.print_out_dice(player, self.dice.get_dice())
        player.change_score(self.dice.get_dice())
        self.histogram.add_histogram(player, self.dice.get_dice())
        self.print_score(player)

        if self.dice.get_dice() in (1, 6):
            self.dice.roll_dice()
            return False

        if self.playing_now.get_score() >= self.win_pig:
            self.end_game(self.playing_now)
            self.histogram.print_histogram(self.player1.get_name(),
                                           self.player2.get_name())
        self.dice.roll_dice()
        return True

    def computer_turn(self):
        """Take orders from Intelligence class to control the decison"""
        print(">>>>> Start Computer turn <<<<<\n")

        while True:
            reaction = self.computer_player.reaction.get_inti_decision(
                       self.computer_player,
                       self.cheat())

            if not self.get_game_status():
                break

            if not reaction:
                print(self.still_going, "statusu")
                print(">>>>>  Computer decide to HOLD <<<<<")
                break

            force_stop = self.console(self.computer_player)
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

    def print_out_dice(self, player, number):
        """Print out the dice"""
        print("{} got:". format(self.playing_now.get_name()))
        print("  _______")
        print(r"|\_______\ ")
        print( "| |      |")
        print( "| |   {}  |".format(number))
        print(r" \|______|")

    def end_game(self, player):
        """Print the winner. """
        self.still_going = False
        print("WOW! Congra {} you won the game!". format(player.get_name()))

    def get_game_status(self):
        """Check the game status"""
        return self.still_going

    def set_computer_controler(self, bool):
        self.computer_controlar = bool

    def get_computer_controler(self):
        return self.computer_controlar