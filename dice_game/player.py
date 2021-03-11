#!/usr/bin/env python3
# -*- coding: utf-8 -*
# pylint: disable=E0401

"""Player Class to control player objects create in game."""

from intelligence import Intelligence


class Player():
    """Player Class."""

    reaction = Intelligence(None)

    def __init__(self, name, decision):
        """Accept player's name and create score."""
        self.name = name
        self.score = 0
        self.score_list = []
        self.decision = decision

    def change_score(self, score):
        """Change player score according to dice dance."""
        if score not in (1, 6):
            self.score += score
        else:
            print("OBS!!\n")
            self.score *= 0

    def set_name(self, name):
        """Change plyer name."""
        self.name = name

    def set_level(self, level):
        """Set computer's level."""
        self.reaction.level = level

    def get_name(self):
        """Return player name."""
        return self.name

    def get_score(self):
        """Return player score."""
        return self.score

    def set_score_list(self, num):
        """Set score list."""
        self.score_list.append(num)

    def get_score_list(self):
        """Return score list."""
        return self.score_list
