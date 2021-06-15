#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=E0401
# pylint: disable=C0116

"""Test intelligence module."""

import unittest
from unittest.mock import patch
from app.intelligence import Intelligence
from app.player import Player
from app.game import Game
from app.dice import Dice


class TestIntelligenceClass(unittest.TestCase):
    """Test Histogram Class."""

    def setUp(self):
        """Run at the beginning of the test."""
        self.game = Game()
        self.dice = Dice()
        self.intelligence = Intelligence("easy")
        self.game.player = Player("intell_class", True)

    def test_act_easy(self):
        """Test act_easy."""
        exp = self.intelligence.act_easy()
        self.assertIn(exp, self.intelligence.orders)

    @patch.object(Intelligence, 'act_easy')
    def test_act_normal(self, mock_calls_act_easy):
        """
        Tests act-normal returns True/False.

        When computer-player score is less than 10, another test
        to assert it calls act-easy if the score higher that 10.
        """
        self.game.computer_player.score = 9
        self.game.computer_player.reaction.act_normal(
            self.game.computer_player
        )
        self.assertTrue(self.game.computer_player.reaction)

        # Tests it calls act-easy when computer score higher than 10
        self.game.computer_player.score = 20
        self.game.computer_player.reaction.act_normal(
            self.game.computer_player
        )
        self.game.computer_player.reaction.act_easy()
        mock_calls_act_easy.assert_called()

    def test_act_hard(self):
        """
        act-hard method where it returns true when computer dicide to cheat.

        The method returns True when dice-face between 2-5.
        """
        self.game.computer_player.reaction.orders = (True, True)
        self.game.dice.rolled_dice = 4
        exp_true = self.game.computer_player.reaction.act_hard(4)
        self.assertTrue(exp_true)

        self.game.dice.rolled_dice = 6
        exp_false = self.game.computer_player.reaction.act_hard(6)
        self.assertFalse(exp_false)

    @patch.object(Intelligence, 'act_easy')
    def test_act_hard_calls_easy(self, mock_calls_act_easy):
        """Tests act-hard calls easy when cheat_decison = False."""
        self.game.computer_player.reaction.orders = (False, False)
        self.game.computer_player.reaction.act_hard(3)
        self.game.computer_player.reaction.act_easy()
        mock_calls_act_easy.assert_called()

    @patch.object(Intelligence, 'act_normal')
    def test_get_inti_decision_normal(self, mock_calls_act_normal):
        """Tests get_inti_decision method calls act-normal."""
        self.game.check_levels("normal")
        self.game.computer_player.reaction.get_inti_decision(
            self.game.computer_player,
            5
        )
        self.game.computer_player.reaction.act_easy()
        mock_calls_act_normal.assert_called()

    @patch.object(Intelligence, 'act_hard')
    def test_get_inti_decision_hard(self, mock_calls_act_hard):
        """Tests get_inti_decision method calls act-hard."""
        self.game.check_levels("hard")
        self.game.computer_player.reaction.get_inti_decision(
            self.game.computer_player,
            2
        )
        self.game.computer_player.reaction.act_hard()
        mock_calls_act_hard.assert_called()

    def test_cheat_decision(self):
        """Test cheat-decision."""
        res = self.intelligence.cheat_decison()
        self.assertIn(res, self.intelligence.orders)
