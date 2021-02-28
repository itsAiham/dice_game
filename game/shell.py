#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd
from game import Game


class Shell(cmd.Cmd):
    """Shell class"""

    prompt = '(game): '
    intro = "Enter help or ? to get the words that can be used.\n"

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = Game()

    def do_start(self, _):
        """Game starting"""
        print("A new")
        del self.game
        self.__init__()

    def do_roll(self, _):
        """Roll the dice"""
        if self.game.get_game_status():
            self.game.roll()
        else:
            print("Game is End. You can 'start' a new game")

    def do_name(self, new_name):
        """Change player name."""
        self.game.change_name(new_name)

    def do_level(self, level):
        """Change the game's level."""
        try:
            self.game.check_levels(level)
        except ValueError as level_error:
            print(level_error)

    def do_pass(self, _):
        """hold turn"""
        if self.game.get_game_status():
            self.game.computer_turn()
        else:
            print("Game is End. You can 'start' a new game")

    def do_cheat(self, _):
        """Return the upcoming value of the dice."""
        print("The next dice value is {},\
             you know what to do, don't yah! =)".format(self.game.cheat()))

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye - see ya soon again")
        return True

    def do_quit(self, arg):
        # pylint: disable=no-self-use
        """Leave the game."""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)