#!/usr/bin/env python3
# -*- coding: utf-8 -*


"""

This controls the intelligence and logic of the whole game

"""

from intelligence import Intelligence


class Player():
    """Player Class."""

    reaction = Intelligence(None)

    def __init__(self, name, decision):
        """Initialisation."""
        self.name = name
        self.score = 0
        self.score_list = []
        self.decision = decision

    def change_score(self, score):
        """Change player score."""
        if score not in (1, 6):
            self.score += score
        else:
            print("OBS!!\n")
            self.score *= 0

    def set_name(self, name):
        """Change plyer name."""
        self.name = name

    def set_level(self, level):
        """Set game's level."""
        self.reaction.level = level

    def get_name(self):
        """Return player name."""
        return self.name

    def get_score(self):
        """Return player score."""
        return self.score

    def set_score_list(self, num):
        """. Initialisation."""
        self.score_list.append(num)

    def get_score_list(self):
        """. Initialisation."""
        return self.score_list
