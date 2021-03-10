#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=E0401

"""Test player module."""

import unittest
import random
from player import Player
from game import Game
from dice import Dice


class TestPlayer(unittest.TestCase):
    """Test Histogram Class."""

    def setUp(self):
        """Creating instances at the beginning of tests cases"""
        self.game = Game()
        self.player = Player(str, bool)
        self.score_list = []
        self.dice = Dice()

        self.fake_die = random.randint(1, 6)

    def test__chane_score(self):
        """Test change_score method."""

        self.player.change_score(1)
        self.assertTrue(self.player.get_score() == 0)
        # Assuming the die face == 6
        self.player.change_score(6)
        self.assertTrue(self.player.get_score() == 0)

        # Assuming the die face == 2
        self.player.change_score(2)
        self.assertTrue(self.player.get_score() + 2)

    def test_set_name(self):
        """Test set/change player name."""
        name = "new_name"
        self.player.set_name(name)
        self.assertTrue(self.player.get_name() == name)

    def test_get_score_list(self):
        """Test Player Class."""
        #  test that name returned in both classes are equals.
        check_name_within_game = self.game.player1.get_score()
        check_name_within_player = self.player.get_score()
        self.assertEqual(check_name_within_player, check_name_within_game)
        self.assertEqual(self.player.score_list, self.player.score_list)

        return_score_list = self.player.get_score_list()
        self.assertEqual(return_score_list, self.score_list)

    def test_set_score_list(self):
        """Test set_score_list."""
        # Assuming that the play got die face = 3:
        self.player.set_score_list(3)
        self.player.score_list.append(3)
        list_long = len(self.player.get_score_list())
        print(list_long)
        self.assertEqual(self.player.score_list[list_long - 1], 3)
