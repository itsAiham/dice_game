
import os
import unittest
from unittest.mock import patch, Mock
from unittest import mock

from unittest.mock import MagicMock
import json
from dice import Dice
from game import Game
# from player import Player
from player import Player
from highscore import Highscore
from histogram import Histogram



        # json = Mock()
        # computer_controlar = Game()
        # set_computer_controlar()


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


    def test_create_player(self):
        exp_input = 'name'
        self.game.player1.set_name(exp_input)

        result = self.game.player1.get_name()
        self.assertTrue(exp_input == result)

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

    # def test_switcher(self):
    #     """Test Switcher."""
        # assert (self.game.get_computer_controler and
        #         (self.game.playing_now == self.game.player1))
        #          self.game.get_playing_now() 












        # Test switcher append to the players' name
        # if (self.game.get_computer_controler() and
        #         self.game.playing_now == self.game.player1):
        #     print("playing now", self.game.playing_now.get_name())

        #     assert self.game.computer_turn()
            # self.assertEqual(self.game.get_playing_now().get_name(),
            #                  self.game.computer_player.get_name())

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


    @mock.patch("game.Game.console")
    def test_roll(self, mock_in_console):
        """Test roll."""
        # just checking if the method return bool
        # need another test for method calling

        # mock = Mock(spec=self.game)
        # Asserting that console return boolean
        # returned_bool_from_consol_meth = [True, False]
        # self.assertIn(self.game.console(
        #               self.game.get_playing_now()),
        #               returned_bool_from_consol_meth)


        # false_dice = 1
        # ## another tests:
        # mock = Mock(spec=Game)
        # # player = self.game.get_playing_now()

        # # self.game.console.return_value = False
        # # assert not self.game.console(self.player1) 

        # if not self.game.console(self.game.player1):
        #     with patch('game.Game') as fake_obj:
        #         mock.switcher()
        #         fake_obj.asert_called()

        # if mock.console().forbidden_face in (1, 6):
        #     self.assertTrue(self.game.get_playing_now() == 0)
        #     self.assertFalse(mock.console())

        # mock_console = mock.Mock(name='mock_in_console', return_value=True)
        mock_in_console.return_value = False
        print("dice", self.game.dice.get_dice())
        print(mock_in_console)
        values = (1, 6)
        self.assertIn(self.game.get_face(), values )

        # mock_console.assert_called()
        # if not self.game.console(mock):
        #     assert mock.switcher()
            # mock.assert_called_with(self.game.switcher())
    
        # mock = Mock(soec=Game, get_face=6 ,  return_value=False )
        # self.game.console(mock)

        # if self.game.forbidden_face not in (1, 6):
        #     print("face", self.game.get_face())
        #     self.assertTrue(self.game.console(mock))
        
        # else :
        #     self.assertFalse(self.game.console(mock))



        

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

    def test_console(self):
        """Test Console."""
        mock = Mock(spec=Game)

        # if self.game.forbidden_face in (1, 6):
        #     self.assertTrue(mock.get_playing_now() == 0)

        if self.game.playing_now.get_score() >= self.game.win_pig:
            print("score",self.game.playing_now.get_score() )
            self.assertFalse(self.game.get_game_status())

    # def test_computer_turn(self):
        



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
        mock = Mock()
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

    def test_get_game_status(self):
        self.game.get_game_status()


    def test_set_computer_controler(self):
        mock = Mock()
        self.game.set_computer_controler(mock)



if __name__ == '__main__':
    unittest.main()
