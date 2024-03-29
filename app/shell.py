#!/usr/bin/env python3
# -*- coding: utf-8 -*
# pylint: disable=E0401
# pylint: disable=E1111

"""
Takes input from user/s.

Control the game through parse the input
and call the equivalent method to operate the work.
"""

import cmd
from app.game import Game


class Shell(cmd.Cmd):
    """Shell class."""

    prompt = '(game): '
    intro = "Enter help or ? to get the words that can be used.\n"
    # computer_control = bool

    def __init__(self):
        """Init game object."""
        super().__init__()
        try:
            self.game = Game()
        except AttributeError:
            print("Something went wrong! Start a new game.")

    def do_start(self, player_num):
        """Game starting."""
        try:
            self.__init__()
            self.game.set_game_status(True)
            if player_num == "1":
                self.game.set_computer_controler(True)
                self.computer_control = self.game.create_player(1)
            elif player_num == "2":
                self.game.set_computer_controler(False)
                self.computer_control = self.game.create_player(2)
            else:
                print("Wrong choice! Enter 'start 1' or 'start 2'.\n")
        except AttributeError:
            print("An Error occured! Try again!")

    def do_roll(self, _):
        """Roll the dice."""
        try:
            if self.game.get_game_status():
                self.game.roll()
            else:
                print("\nYou need to enter 'start 1' or 'start 2'"
                      "to start a new game")
        except AttributeError:
            print("Game Over!")
        except ValueError:
            self.__delattr__("game")
            self.__init__()
            print(ValueError)

    def do_name(self, new_name):
        """Change player name."""
        self.game.change_name(new_name)

    def do_level(self, level):
        """Change the game's level."""
        try:
            self.game.check_levels(level)
        except ValueError as level_error:
            print(level_error)
        except AttributeError:
            print("You are playing against a human," +
                  "ask him to change the level not me!!!\n")

    def do_pass(self, _):
        """Hold turn."""
        try:
            if self.game.get_game_status():
                self.game.switcher()
            else:
                print("Game is End. You must 'start' a new game")
        except AttributeError:
            print("No game and no turns to hold!!")

    def do_cheat(self, _):
        """Return the upcoming value of the dice."""
        print("The next dice value is {n}, "
              "you know what to do, don't yah! =)\n"
              .format(n=self.game.cheat()))

    def do_score(self, _):
        """Read from highscore file."""
        try:
            self.game.highscore()
        except AttributeError:
            print("Sorry! You need to start a game first.")

    def do_help(self, _):
        """Print orders' format."""
        print("\nstart n : Enter 'start' + 'space' + '1' or '2' to"
              "start or restart a new game.")
        print("name      : 'name' + 'your name' to"
              " change the current player name.")
        print("roll      : Roll the dice.")
        print("score     : Print out highscores.")
        print("pass      : To hold the turn and switch to the next player.")
        print("cheat     : Return the value of the upcoming dice.")
        print("level     : Change the computer level.")
        print("end       : Ends currently game without exiting the terminal.")
        print("q, exit   : Exit the game.\n")

    def default(self, line):
        """Print out message when invalid input."""
        self.stdout.write('\nOBS! Unknown command:  %s.\n'
                          "Enter help or ? to get info\n\n"
                          '' % (line,))

    def do_end(self, _):
        """End currnet game."""
        try:
            del self.game
        except AttributeError:
            print("\nGame is ended.\n")

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Exit CMD-terminal the game."""
        return True

    def do_q(self, arg):
        """Exit CMD-terminal the game."""
        return self.do_exit(arg)
