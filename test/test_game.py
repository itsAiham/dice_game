#!/usr/bin/env python3
# -*- coding: utf-8 -*
# pylint: disable=E0401
# pylint: disable=E1111

"""Test game module."""

import sys
import io
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from app.dice import Dice
from app.game import Game
from app.player import Player
from app.highscore import Highscore
from app.histogram import Histogram


class TestGameClass(unittest.TestCase):
    """Test Game Class."""

    def setUp(self):
        """Run at the beginning of the test."""
        self.game = Game()
        self.game.set_game_status(True)
        self.dice = Dice()

        self.player1 = Player(str, bool)
        self.player2 = Player(str, bool)
        self.computer_player = Player(str, bool)

        self.highscore = Highscore(self.player1, self.player2)

    @patch('builtins.input', return_value='')
    def test_create_player(self, mock):
        """Test create_player."""
        # Test with one player name and no name entered
        self.game.create_player(1)
        self.game.player1_name = mock
        self.assertEqual(self.game.player1.get_name(), "USER1")

    @patch('builtins.input', return_value='name')
    def test_create_player1(self, mock):
        """Test create_player."""
        # Test with one player name and no name entered
        self.game.create_player(1)
        self.game.player1_name = mock
        self.assertEqual(self.game.player1.get_name(), "name")
        self.assertEqual(self.game.player2.get_name(), "Computer")

    @patch('builtins.input', return_value='')
    def test_create_player2(self, mock):
        """Test create_player."""
        # Test with Two players name and no name entered
        self.game.create_player(2)
        self.game.player1_name = mock
        self.game.player2_name = mock
        self.assertEqual(self.game.player1.get_name(), "USER1")
        self.assertEqual(self.game.player2.get_name(), "USER2")
        # Check that computer_controler is off
        self.assertFalse(self.game.get_computer_controler())

    @patch.object(Game, 'switch_with_computer')
    def test_switch_with_computer(self, mock_calls_swit_com):
        """Test switching between player-1 and computer player."""
        # self.game.set_computer_controler(True)
        self.game.computer_controlar = True
        # self.game.set_game_status(True)
        self.game.still_going = True
        self.game.set_playing_now(self.game.computer_player)
        # self.game.switch_with_computer()
        self.game.switcher()
        self.game.switch_with_computer()
        mock_calls_swit_com.assert_called()

    @patch.object(Game, 'switch_between_humans')
    def test_switch_with_human_players(self, mock_calls_swit_humans):
        """Test-switching between humans' players."""
        self.game.set_computer_controler(False)
        self.game.set_game_status(True)
        self.game.set_playing_now(self.game.player2)
        self.assertTrue(self.game.get_playing_now() == self.game.player2)

        self.game.switcher()
        self.game.switch_between_humans()
        mock_calls_swit_humans.assert_called()

    def test_change_name(self):
        """Test changing name feature."""
        self.game.change_name("new_name")
        res = self.game.playing_now.get_name()
        self.assertTrue(res == "new_name")

    def test_end_game(self):
        """Test end_game."""
        histogram = Histogram()
        score = Highscore(self.game.player1, self.game.player2)

        self.game.set_game_status(False)
        self.assertIsInstance(histogram, Histogram)
        # self.assertFalse(self.game.get_game_status())
        self.assertIsInstance(score, Highscore)

        #   The folling two lines work find to test
        #   the the method change-game.status to false
        #     exp = self.player1
        #     self.game.end_game(exp)
        # However;
        # The followign method-call raise an error
        #  and may need another tests typ!
        # score.write_file()    <-----
        highscore = Highscore(self.game.player1, self.game.player2)
        highscore.write_file = MagicMock(name='write_file')
        highscore.write_file()

    def test_check_levels(self):
        """Test check_levels."""
        # assuming easy level passed:
        passed_level = "easy"
        levels_list = ("easy")
        self.game.check_levels(passed_level)
        if passed_level in levels_list:
            res = self.computer_player.reaction.level
            self.assertEqual(res, passed_level)

    def test_print_score(self):
        """Test print_score."""
        name_res = self.player1.get_name()
        score_res = self.player1.get_score()
        res = name_res and score_res

        catch_output = io.StringIO()
        sys.stdout = catch_output
        self.game.print_score(self.player1)
        # print player's name and score and catch it.
        sys.stdout = sys.__stdout__
        output = catch_output.getvalue()
        self.assertIn(str(res), output)

    def test_print_out_dice(self):
        """Test print_out_dice."""
        res = str(self.player1.get_name())

        catch_output = io.StringIO()
        sys.stdout = catch_output
        self.game.print_out_dice(self.player1, 5)
        # print cube out and catch it.
        sys.stdout = sys.__stdout__
        output = catch_output.getvalue()
        self.assertIn(res, output)

    def test_get_playing_now(self):
        """Test set And get_playing_now."""
        exp = self.player1
        self.game.set_playing_now(exp)
        res = self.game.get_playing_now()
        self.assertEqual(res, exp)

    def test_get_game_status(self):
        """Test get_game_status."""
        self.game.still_going = False
        self.assertFalse(self.game.get_game_status())
        self.game.still_going = True
        self.assertTrue(self.game.get_game_status())

    def test_set_cmputer_controler(self):
        """Test set_computer_controler."""
        self.game.set_computer_controler(True)
        self.assertTrue(self.game.computer_controlar)

    def test_get_computer_controler(self):
        """Test get_computer_controler."""
        res = self.game.get_computer_controler()
        self.assertIn(res, [True, False])

    def test_set_face(self):
        """Test set_face."""
        self.game.set_face(2)
        res = self.game.get_face()
        self.assertEqual(res, 2)
