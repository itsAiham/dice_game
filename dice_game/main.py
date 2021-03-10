#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=E0401

"""

Welcome In Pig Dice!
The game is easy. Try to roll the dice and not gitting
values 1 and 6, or you lose your score and turn.
Try to win over me, since my default level is easy.
If you succeed then change the level, but not the hard one! or I will bit yours
I expect from you to change your name
to let me know who I play with!!

Otherwise, I call you USER you Loser!

"""
import shell


if __name__ == '__main__':
    print(__doc__)
    shell.Shell().cmdloop()
