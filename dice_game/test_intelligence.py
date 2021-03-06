#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# import sys
# import io
import unittest
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
        # need to be checked !
        # if self.game.player.get_score() < 10:
        #     self.assertEqual(self.game.player.reaction.get_inti_decision(
        #                      self.game.player.get_score(),
        #                      self.dice.get_dice()), True)
        # self.intelligence.act_easy()
        #  same result!! line 27 return act_easy()
        self.assertIn(self.game.player.reaction.get_inti_decision(
                self.game.player.get_score(),
                self.dice.get_dice()), self.intelligence.orders)

    def test_act_hard(self):
        self.intelligence.act_hard(4)
        if self.intelligence.cheat_decison() and 1 < self.dice.get_dice() > 6:
            self.assertEqual(self.game.player.reaction.get_inti_decision(
                             self.game.player.get_score(),
                             self.dice.get_dice()), True)

        elif self.intelligence.cheat_decison():
            self.assertIn(self.game.player.reaction.get_inti_decision(
                             self.game.player.get_score(),
                             self.dice.get_dice()), self.intelligence.orders)

    def test_get_init_decision(self):
        self.intelligence.get_inti_decision(self.game.player, self.dice.get_dice())
        if self.intelligence.level == 'normal':
            self.assertEqual(self.game.player.reaction.level, "normal")
            # self.intelligence.act_normal(self.player)

        if self.intelligence.level == 'hard':
            self.assertEqual(self.game.player.reaction.level, "hard")
            # self.intelligence.act_hard(self.dice.get_dice())

        self.assertEqual(self.game.player.reaction.level, "easy")
        # self.intelligence.act_easy()

    def test_cheat_decision(self):
        res = self.intelligence.cheat_decison()
        self.assertIn(res, self.intelligence.orders)
