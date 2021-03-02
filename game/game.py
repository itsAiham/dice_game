#!/usr/bin/env python3,
# pylint: disable=missing-module-docstring
# pylint: disable=R0902
# pylint: disable=W0622
# pylint: disable=W0201


from player import Player
from dice import Dice
from histogram import Histogram
from highscore import Highscore


class Game():
    """Game Class."""

    win_pig = 10
    still_going = False

    def __init__(self):
        print("Game Starts!\n")
        self.computer_controlar = False
        self.dice = Dice()

        self.player1 = Player("USER1",  bool)
        self.set_playing_now(self.player1)
        self.player2 = Player(("USER2"),  bool)
        # Basically, player2 may be computer in case user decided.
        # However, computer_player object has been added to make the
        # code easier to read. Since computer controlled by another class.
        self.computer_player = Player("Computer",  bool)
        self.computer_player.set_level("easy")

        self.score = Highscore(self.player1, self.player2)
        self.histogram = Histogram()

    def create_player(self, player_amount):
        """Get info from shell.py, fit equavelent players with names"""
        player1_name = input("Enter the first player's name >> ")
        self.player1.set_name(player1_name)
        #  Hold player object temporarily above

        if player_amount == 2:
            print("Created another player")
            player2_name = input("Enter the second player's name >> ")
            self.player2.set_name(player2_name)

        else:
            print("Created computer player")
            print(self.set_computer_controler(True))
            self.player2 = self.computer_player

    def switcher(self):
        """Switch turns between players."""
        if (self.get_computer_controler() and
           self.get_playing_now() == self.player1):
            self.set_playing_now(self.computer_player)
            return self.computer_turn()

        if (self.get_computer_controler() and
           self.get_playing_now() == self.computer_player):
            self.set_playing_now(self.player1)

        if self.get_playing_now() == self.player1 and not (
           self.get_computer_controler()):

            print(">>>>> Start {} turn <<<<<\n".format(
                self.player2.get_name()))
            return self.set_playing_now(self.player2)

        print(">>>>> Start {} turn <<<<<\n".format(self.player1.get_name()))
        return self.set_playing_now(self.player1)

    def roll(self):
        """Roll the dice."""
        force_stop = self.console(self.get_playing_now())

        if not force_stop and self.get_game_status():
            self.switcher()

    def console(self, player):
        """Synchronize between players's scores and rolled dice """
        self.print_out_dice(player, self.dice.get_dice())
        player.change_score(self.dice.get_dice())
        player.set_score_list(self.dice.get_dice())
        self.print_score(player)

        if self.dice.get_dice() in (1, 6):
            self.dice.roll_dice()
            return False

        if self.get_playing_now().get_score() >= self.win_pig:
            self.end_game(self.playing_now)
            self.set_game_status(False)

        self.dice.roll_dice()
        return True

    def computer_turn(self):
        """Take orders from Intelligence class to control the decison"""
        print(">>>>> Start Computer turn <<<<<\n")

        while self.get_game_status():
            reaction = self.computer_player.reaction.get_inti_decision(
                       self.computer_player,
                       self.cheat())

            if not reaction:
                print(self.still_going, "statusu")
                print("\t\t\t\t>>>>>  Computer decide to HOLD <<<<<")
                self.switcher()
                break

            print("\t\t\t\t>>>>>  Computer decide to ROLL <<<<<")
            self.playing_now = self.computer_player
            force_stop = self.console(self.computer_player)
            print(force_stop)
            if not force_stop:
                print("\t\t\t\t>>>>>  Computer lose its turn <<<<<")
                self.switcher()
                break

    def cheat(self):
        """Return the rolled dice"""
        return self.dice.get_dice()

    def check_levels(self, level):
        """Check if the entered level is valid"""
        levels = ("easy", "normal", "hard")
        if level in levels:
            self.computer_player.set_level(level)
            print("My level now is", level)

        else:
            raise ValueError("This kind of level is not available!!")

    def change_name(self, name):
        """Change player name."""
        self.playing_now.set_name(name)

    @staticmethod
    def print_score(player):
        """Print out player score and name."""
        print("{} score is {}". format(player.get_name(),
                                       player.get_score()))

    @staticmethod
    def print_out_dice(player, number):
        """Print out the dice"""
        print("{} got:". format(player.get_name()))
        print(" ______")
        print(r"|\______\ ")
        print("||      |")
        print("||   {}  |".format(number))
        print(r"\|______|"+"\n")

    def highscore(self):
        """Read and print out from highscore file."""
        self.score.read_file()

    def end_game(self, player):
        """Print the winner. """
        self.set_game_status(False)
        print("WOW! Congra {} you won the game!". format(player.get_name()))
        self.histogram.print_histogram(self.player1,
                                       self.player2)
        self.score.write_file()

    def set_game_status(self, bool):
        """Check the game status"""
        self.still_going = bool

    def get_game_status(self):
        """Check the game status"""
        return self.still_going

    def set_playing_now(self, player):
        """Change object holder to help exchanging players"""
        self.playing_now = player

    def get_playing_now(self):
        """Return currently player."""
        return self.playing_now

    def set_computer_controler(self, bool):
        """Setter for a boolen variable.
        Help to switching turns."""
        self.computer_controlar = bool

    def get_computer_controler(self):
        """Getter for a boolen variable.
        Help to switching turns."""
        return self.computer_controlar
