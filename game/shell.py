#!/usr/bin/env python3
# pylint: disable=missing-module-docstring

import cmd
from game import Game


class Shell(cmd.Cmd):
    """Shell class"""

    prompt = '(game): '
    intro = "Enter help or ? to get the words that can be used.\n"
    computer_control = bool

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = Game()

    def do_start(self, player_num):
        """Game starting"""
        try:
            self.game.still_going = True
            if player_num == "1":
                self.game.set_computer_controler(True)
                self.computer_control = self.game.create_player(1)
            elif player_num == "2":
                self.game.set_computer_controler(False)
                self.computer_control = self.game.create_player(2)
            else:
                print("Wrong choice! Enter 'start 1' or 'start 2'.\n")    
        except AttributeError:
            print("do start error")

    def do_roll(self, _):
        """Roll the dice"""
        try:
            if self.game.get_game_status():
                self.game.roll()
            else:
                print("Game is End.\nYou can enter 'start 1' or 'start 2' to start a new game")
        except ValueError:
            print("You need to start the game first.")

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
                print("Game is End. You can 'start' a new game")
        except AttributeError:
            print("No game and no turns to hold!!")

    def do_cheat(self, _):
        """Return the upcoming value of the dice."""
        print("The next dice value is {n},"
        "you know what to do, don't yah! =)\n".format(n = self.game.cheat()))

    def do_help(self, *args):
        """Print orders' format"""
        # cmd.Cmd.do_help(self, *args) 
        print("\nstart _: Enter 'start' + 'space' + '1' or '2' to start a new game.")
        print("name _: 'name' + 'the wnated name' to change the current player name.")
        print("roll: Roll the dice.")
        print("pass: To hold the turn and switch to the next player.")
        print("cheat: Return the value of the upcoming dice.")
        print("level: Change the computer level.")
        print("q, exit, EOF: Exit the game.\n")

    def default(self, line):
        self.stdout.write('\nOBS! Unknown command: %s.\nEnter help to get info\n' % (line,))

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        return True

    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
