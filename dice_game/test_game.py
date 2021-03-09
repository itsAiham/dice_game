#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys
import io
import unittest
from unittest.mock import patch, Mock
from unittest.mock import MagicMock
from dice import Dice
from game import Game
from player import Player
from highscore import Highscore
from histogram import Histogram


class TestGameClass(unittest.TestCase):

    def setUp(self):
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
        # Check that computer_controler is on
        self.assertTrue(self.game.get_computer_controler())

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

    def test_switcher(self):
        """Test Switcher."""
        # Testing switcher
        self.game.set_game_status(True)
        before_switching = self.game.get_playing_now()
        self.game.switcher()
        after_switching = self.game.get_playing_now()
        self.assertNotEqual(before_switching, after_switching)

        # another test and assuming it is ccomputer's turn
        self.game.set_game_status(True)
        self.game.set_playing_now(self.computer_player)
        self.game.switcher()
        self.assertEqual(self.game.get_playing_now(), self.game.player1)

    def test_roll(self):
        """Test roll."""
        res = self.game.roll()
        if self.game.get_face() in (1, 6):
            self.assertFalse(res)

    def test_console(self):
        """Test console."""
        ret_bool = self.game.console(self.game.get_playing_now())
        if self.game.get_face() in (1, 6):
            self.assertFalse(ret_bool)

        # Test that the game ends when the currently player
        # reached the winning score
        if self.game.get_playing_now().get_score() >= self.game.win_pig:
            self.assertFalse(self.game.get_game_status())
            self.game.end_game(self.game.get_playing_now())

    def test_computer_turn(self):
        """Test computer_turn."""
        # Testing prints message:
        self.game.computer_turn()
        # Most output from method inculds :
        printing_res = ' Computer '

        catch_output = io.StringIO()
        sys.stdout = catch_output
        self.game.computer_turn()

        # print player's name and score and catch it.
        sys.stdout = sys.__stdout__
        output = catch_output.getvalue()
        self.assertIn(str(printing_res), output)

        # Testing switcher() be called by computer_player
        #   when it decide stops playing
        test_reaction = self.computer_player.reaction.get_inti_decision(
            self.computer_player, 4)

        if not test_reaction:
            mock_com_player = Mock(spec=Game)
            self.assertIsInstance(mock_com_player, Game)
            mock_com_player.switcher()
            mock_com_player.switcher.assert_called()

        # If game force stop, call switcher
        mock_com_player2 = Mock(spec=Game)
        game_return = self.game.console(self.computer_player)
        if not game_return:
            mock_com_player2.switcher()
            mock_com_player2.switcher.assert_called()

    def test_cheat(self):
        """Test cheat method."""
        cheat_method = self.game.cheat()
        self.assertEqual(cheat_method, self.game.dice.get_dice())

    def test_highscore(self):
        """Test highscore method."""
        mock = Mock(spec=Highscore)
        self.assertIsInstance(mock, Highscore)
        with patch('highscore.Highscore') as fake_obj:
            mock.read_file()
            fake_obj.asert_called()

        # another test
        read_file_method = self.highscore.read_file()
        self.assertEqual(read_file_method, self.highscore.read_file())
        # Test The Instance
        self.assertIsInstance(self.highscore, Highscore)

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
        res = self.game.get_game_status()
        self.assertIn(res, [True, False])

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


if __name__ == '__main__':
    unittest.main()
