#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=E0401
# pylint: disable=C0116

"""Test intelligence module."""

import unittest
from unittest.mock import patch, Mock
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

    def test_act_normal(self):
        """Test act_normal."""
        self.intelligence.act_normal(self.game.player)

        if self.game.player.get_score() < self.game.win_pig:
            self.assertTrue(self.game.player.reaction)

        mock = Mock(spec=Intelligence)
        self.assertIsInstance(mock, Intelligence)
        with patch('app.intelligence.Intelligence') as fake_obj:
            mock.act_easy()
            fake_obj.asert_called()

    # def test_act_hard(self):
    #     """Test act-hard method."""
    #     exp = self.intelligence.act_hard(self.dice.get_dice())
    #     if (self.intelligence.cheat_decison() and
    #     1 < self.dice.get_dice() > 6):
    #         self.assertTrue(exp)

    #     self.assertIn(exp, self.intelligence.orders)

    # def test_get_init_decision(self):
    #     """Teset get_initelligence_dicision."""
    #     if self.intelligence.level == 'normal':
    #         self.assertEqual(self.game.player.reaction.level, "normal")
    #         self.intelligence.act_normal(self.game.player)

    #     if self.intelligence.level == 'hard':
    #         self.assertEqual(self.game.player.reaction.level, "hard")
    #         self.intelligence.act_hard(self.dice.get_dice())

    #     self.assertEqual(self.game.player.reaction.level, "easy")

    def test_cheat_decision(self):
        """Test cheat-decision."""
        res = self.intelligence.cheat_decison()
        self.assertIn(res, self.intelligence.orders)
