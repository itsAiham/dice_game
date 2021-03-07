
import os
import unittest
from unittest.mock import patch, Mock
from unittest import mock
import sys
import io
from unittest.mock import MagicMock
import json
from dice import Dice
from game import Game
# from player import Player
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
    
        # mock = Mock()

    # def test__init__(self):
    #     """Test Constrctor."""
    #     # game = Game()
    #     self.assertFalse(self.game.get_computer_controler())

    #     # dice = Dice()
    #     self.assertIsInstance(self.dice, Dice)

    #     playing_now = Game()       # Test playing_now is created in Game Class
    #     self.assertIsInstance(self.game, Game)
    #     self.assertIsInstance(playing_now, Game)

    #     player1 = Player(str, bool)  # Test that players are created
    #     player2 = Player(str, bool)

    #     self.assertIsInstance(player1, Player)
    #     self.assertIsInstance(player2, Player)
    #     self.assertIsInstance(self.computer_player, Player)

    #     self.assertIsInstance(playing_now, Game)

    #     highscore = Highscore(player1, player2)
    #     self.assertIsInstance(highscore, Highscore)

    #     histogram = Histogram()
    #     self.assertIsInstance(histogram, Histogram)

        
        # if self.game.computer_controlar:  

    # @patch('yourmodule.get_input', return_value=' ')
    def test_create_player(self):

        # Testing that in case no computer controler,
        #    then the second player gonna change his name.
        if not self.game.computer_controlar:
            exp_input2 = 'name2'
            self.game.player2.set_name(exp_input2)
            result2 = self.game.player2.get_name()
            self.assertTrue(exp_input2 == result2)

        # Otherwise, the second player's name = Computer
        elif self.game.computer_controler:
            result2 = self.game.player2.get_name()
            self.assertTrue(result2 == 'Computer')

        # Another way of testing
        exp_input = 'name'
        if exp_input == "":
            self.assertTrue(self.game.player1.get_name() == "USER1")
        self.game.player1.set_name(exp_input)
        result = self.game.player1.get_name()
        self.assertTrue(exp_input == result)

        num = 2
        self.game.create_player(num)
        exp_name_when_ply_2 = 'name'
        if exp_name_when_ply_2 == "":
            exp_name_when_ply_2 = "USER2"
            self.game.player2.set_name(exp_name_when_ply_2)
            self.assertTrue(self.game.player2.get_name() == "USER2")
        
        # self.game.player2.set_name(exp_input_2)
        # self.assertTrue(self.game.player2.get_name() == exp_input_2)

        self.game.create_player(1)
        self.assertTrue(self.game.player2.get_name() == "Computer")



    # def test_switcher(self):
    #     """Test Switcher."""
        # assert (self.game.get_computer_controler and
        #         (self.game.playing_now == self.game.player1))
        #          self.game.get_playing_now() 
        # # Test switcher append to the players' name
        # if (self.game.get_computer_controler() and
        #         self.game.playing_now == self.game.player1):
        #     print("playing now", self.game.playing_now.get_name())

        #     assert self.game.computer_turn()
        #     self.assertEqual(self.game.get_playing_now().get_name(),
        #                      self.game.computer_player.get_name())

        # if (self.game.get_computer_controler() and
        #         (self.game.get_playing_now.get_name() ==
        #          self.game.computer_player.get_name())):

        #     self.assertEqual(self.game.get_playing_now().get_name(),
        #                      self.game.player1.get_name())

        # if (not self.game.get_computer_controler() and
        #         self.game.get_playing_now == self.game.player1):

        #     self.assertEqual(self.game.get_playing_now().get_name(),
        #                      self.game.player2.get_name())

        # self.assertEqual(self.game.get_playing_now().get_name(),
        #                  self.game.player1.get_name())

    def test_roll(self):
        """Test roll."""
        res = self.game.roll()
        if self.game.get_face() in (1, 6):
            self.assertFalse(res)
        else:
            self.assertTrue(res)

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

    # def test_console(self):
    #     """Test Console."""
    #     mock = Mock(spec=Dice, return_value=6)
    #     self.game.con

        # if self.game.forbidden_face in (1, 6):
        #     self.assertTrue(mock.get_playing_now() == 0)

        if self.game.playing_now.get_score() >= self.game.win_pig:
            print("score", self.game.playing_now.get_score() )
            self.assertFalse(self.game.get_game_status())

    def test_computer_turn(self):
        """Test computer_turn."""
        # Testing prints message:
        pint_res = " Computer " 

        catch_output = io.StringIO()
        sys.stdout = catch_output
        self.game.computer_turn()
        # print player's name and score and catch it.
        sys.stdout = sys.__stdout__
        output = catch_output.getvalue()
        self.assertIn(pint_res, output)

    def test_cheat(self):
        """Test cheat method."""
        cheat_method = self.game.cheat()
        self.assertEqual(cheat_method, self.game.dice.get_dice())

    ## LINE 165
    def test_highscore(self):
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
        # mock = Mock()
        histogram = Histogram()
        score = Highscore(self.game.player1, self.game.player2)

        # self.assertIsInstance(self.game.player.get_name(), str)
        self.assertIsNotNone(self.game.playing_now.get_name())

        self.game.set_game_status(False)
        self.assertIsInstance(histogram, Histogram)
        # self.assertFalse(self.game.get_game_status())
        self.assertIsInstance(score, Highscore)
        # moch.write_file().assert_called()

        # score.write_file()
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


    # def test_end_game(self):
    #     """Test end_game."""
    #     exp = self.player1
    #     self.game.end_game(exp)
    #     self.assertFalse(self.game.get_game_status)

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


if __name__ == '__main__':
    unittest.main()
