#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=E0401
# pylint: disable=E0401

"""
Welcome In Pig Dice!.

The game is easy. Try to roll the dice and not gitting
values 1 and 6, or you lose your score and turn.
The winner who reach 50 points first.

To start the game,

    Enter 'start 1' to play against the computer
          'start 2' to play with two players.

If you choose to play against the computer, you are able to change the
level when ever you want.

I expect to change your name by entering 'name (Your Name)'

Prese help or ? to get more about commands
"""
import shell


if __name__ == '__main__':
    print(__doc__)
    shell.Shell().cmdloop()
