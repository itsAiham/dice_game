#!/usr/bin/env python3
# -*- coding: utf-8 -*
# pylint: disable=E0401
# pylint: disable=W0201
# pylint: disable=C0411

"""Test highscore module."""


import unittest
from app.player import Player
from app.game import Game
from app.highscore import Highscore
from unittest.mock import Mock


class TestHigscore(unittest.TestCase):
    """Test Higscore Class."""

    def setUp(self):
        """Run at the beginning of the test."""
        self.game = Game()
        self.mock_player1 = Mock(spec=Player, name="player1",
                                 score=42, decision=False)
        self.mock_player2 = Mock(spec=Player, name="Computer",
                                 score=65, decision=True)

        self.assertIsInstance(self.mock_player1, Player)
        self.assertIsInstance(self.mock_player2, Player)
        self.score = Highscore(self.mock_player1, self.mock_player2)

    def test_write_file(self):
        """Test write_file."""
        self.player1 = Player("score1", False)
        self.game.set_playing_now(self.game.player1)
        self.player1.change_score(5)
        self.score.write_file()

        self.player2_name = Player("score2", False)
        self.game.set_playing_now(self.game.player2)
        self.player1.change_score(4)

    def test_get_path(self):
        """Test get_path."""
        exp = self.score.get_path()
        self.assertTrue(exp, 'score.txt')
