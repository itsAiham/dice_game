
import sys
import io
import json
import os
import unittest
from unittest import mock

from unittest.mock import patch, Mock
from unittest.mock import MagicMock
from dice_game.dice import Dice
from dice_game.game import Game
# from player import Player
from dice_game.player import Player
from dice_game.highscore import Highscore
from dice_game.histogram import Histogram

# import sys, os
# sys.path.append('C:\\Users\\46737\\Desktop\\Methods_for_Sustainable_Programming\\Exam_2\\game_file')



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
        # Check that computer.controler is on
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
        # Check that computer.controler is off
        self.assertFalse(self.game.get_computer_controler())


        
        # self.assertEqual(self.player1.get_name(), fake_player_1)


        # print("name create", name_res)
        # empty_user_input = ""
        # with patch('builtins.input', side_effect=empty_user_input):
        #     self.game.create_player(1)
        
        # name_res = self.player1.get_name()
        # self.assertTrue(name_res == 'USER1')




        # Testing that in case no computer controler,
        #    then the second player gonna change his name.
        
        # if not self.game.computer_controlar:
        #     exp_input2 = 'name2'
        #     self.game.player2.set_name(exp_input2)
        #     result2 = self.game.player2.get_name()
        #     self.assertTrue(exp_input2 == result2)

        # # Otherwise, the second player's name = Computer
        # elif self.game.computer_controler:
        #     result2 = self.game.player2.get_name()
        #     self.assertTrue(result2 == 'Computer')

        # Another way of testing
        # exp_input = 'name'
        # if exp_input == "":
        #     self.assertTrue(self.game.player1.get_name() == "USER1")
        # self.game.player1.set_name(exp_input)
        # result = self.game.player1.get_name()
        # self.assertTrue(exp_input == result)

        # num = 2
        # self.game.create_player(num)
        # exp_name_when_ply_2 = 'name'
        # if exp_name_when_ply_2 == "":
        #     exp_name_when_ply_2 = "USER2"
        #     self.game.player2.set_name(exp_name_when_ply_2)
        #     self.assertTrue(self.game.player2.get_name() == "USER2")
        
        # # self.game.player2.set_name(exp_input_2)
        # # self.assertTrue(self.game.player2.get_name() == exp_input_2)

        # self.game.create_player(1)
        # self.assertTrue(self.game.player2.get_name() == "Computer")

    def test_switcher(self):
        """Test Switcher."""
        before_switching = self.game.get_playing_now()
        self.game.switcher()
        after_switching = self.game.get_playing_now()
        self.assertNotEqual(before_switching, after_switching)

        if (self.game.get_computer_controler() and
            self.get_playing_now() == self.computer_player):
            hold_player = self.game.get_playing_now()
            self.set_playing_now(self.player1)
            assert (hold_player != self.player1)

    def test_roll(self):
        """Test roll."""
        res = self.game.roll()
        if self.game.get_face() in (1, 6):
            self.assertFalse(res)
        # else:
        #     self.assertTrue(res)

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


    # NOT SURE ABOUT THIS ONE YET!!
    def test_parameters(self):
        parameter_list = [('player_amount', 'int'),  #creat_player
                          ('player', 'Player'),
                          ('name', 'name'),  ## change_name
                          ('player', 'str'),  # end_game
                          ('bool', 'bool')]  ##  set_computer_control
        for para in parameter_list:
            yield self.game.create_player, para[0], para[1]  #creat_player
            yield self.game.console, para[2], para[3]
            yield self.game.change_name, para[4], para[5]   # change_name
            yield self.game.end_game, para[6], para[7]  # end_game
            yield self.game.set_computer_controlar, para[8], para[9] # set_computer_control

    def test_computer_turn(self):
        """Test computer_turn."""
        # Testing prints message:
        self.game.computer_turn()
        # Most output from method inculds :
        printing_res = ' Computer decide '

        catch_output = io.StringIO()
        sys.stdout = catch_output
        self.game.computer_turn()

        # print player's name and score and catch it.
        sys.stdout = sys.__stdout__
        output = catch_output.getvalue()
        self.assertIn(str(printing_res), output)

    def test_cheat(self):
        """Test cheat method."""
        cheat_method = self.game.cheat()
        self.assertEqual(cheat_method, self.game.dice.get_dice())

    def test_highscore(self):
        """Test highscore."""
        mock = Mock(spec=Highscore)
        self.assertIsInstance(mock, Highscore)
        with patch('dice_game.highscore.Highscore') as fake_obj:
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

        # self.assertIsNotNone(self.game.playing_now.get_name())

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
        #   and may need another tests typ!        
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

        # Could not test the following!
        elif passed_level not in levels_list:
            self.assertRaises(ValueError)

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

    # def test_highscore(self):
    #     res = self.game.score.read_file()

    #     catch_output = io.StringIO()
    #     sys.stdout = catch_output
    #     self.game.print_out_dice(self.player1, 5)
    #     # print file out and catch it.
    #     sys.stdout = sys.__stdout__
    #     output = catch_output.getvalue()
    #     self.assertIn(res, output)


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
        self.game.set_face(2)
        res = self.game.get_face()
        self.assertEqual(res, 2)


if __name__ == '__main__':
    unittest.main()
