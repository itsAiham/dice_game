#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, Mock
from intelligence import Intelligence
from player import Player
from game import Game
from dice import Dice


class TestIntelligenceClass(unittest.TestCase):
    """Test Histogram Class."""

    def setUp(self):
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
        with patch('intelligence.Intelligence') as fake_obj:
            mock.act_easy()
            fake_obj.asert_called()

    def test_act_hard(self):
        exp = self.intelligence.act_hard(self.dice.get_dice())
        if self.intelligence.cheat_decison() and 1 < self.dice.get_dice() > 6:
            self.assertTrue(exp)

        self.assertIn(exp, self.intelligence.orders)

    def test_get_init_decision(self):
        """Teset get_initelligence_dicision."""
        if self.intelligence.level == 'normal':
            self.assertEqual(self.game.player.reaction.level, "normal")
            self.intelligence.act_normal(self.player)

        if self.intelligence.level == 'hard':
            self.assertEqual(self.game.player.reaction.level, "hard")
            self.intelligence.act_hard(self.dice.get_dice())

        self.assertEqual(self.game.player.reaction.level, "easy")

    def test_cheat_decision(self):
        res = self.intelligence.cheat_decison()
        self.assertIn(res, self.intelligence.orders)

        # elif self.intelligence.cheat_decison():
        #     computer_saying = "bst -->  Computer CHEATS!!"
        #     catch_output = io.StringIO()
        #     sys.stdout = catch_output
        #     exp11 = self.intelligence.act_hard(6)
        #     sys.stdout = sys.__stdout__
        #     output = catch_output.getvalue()
        #     self.assertIn(output, computer_saying)
        #     self.assertFalse(exp11)

        # self.assertIn("I'm NOT a cheater", exp11)
