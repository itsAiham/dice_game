

import unittest
from unittest.mock import patch, Mock
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
        game = Game()
        game.set_game_status(True)

    def test__init__(self):
        """Test Constrctor."""
        game = Game()
        self.assertFalse(game.get_computer_controler())

        dice = Dice()
        self.assertIsInstance(dice, Dice)

        playing_now = Game()       # Test playing_now is created in Game Class
        self.assertIsInstance(game, Game)
        self.assertIsInstance(playing_now, Game)

        player1 = Player(str, bool)     # Test that players are created
        player2 = Player(str, bool)
        computer_player = Player(str, bool)
        self.assertIsInstance(player1, Player)
        self.assertIsInstance(player2, Player)
        self.assertIsInstance(computer_player, Player)

        self.assertIsInstance(playing_now, Game)

        highscore = Highscore(player1, player2)
        self.assertIsInstance(highscore, Highscore)

        histogram = Histogram()
        self.assertIsInstance(histogram, Histogram)

    # def test_create_player(self):
    #     game = Game()

    #     player1 = Player(str, bool)
    #     player2 = Player(str, bool)
        # computer_player = Player(str, bool)

        # self.assertTrue(player1.set_name(str))
        # self.assertTrue(player2.set_name(str))

        # check_player = 1 <= player_amount >= 2
        # self.assertTrue(check_player)

        # self.assertTrue(player2.set_name(str))
        # self.assertTrue(game.get_computer_controler())

    # @patch("dice_game.Game", returned_name="name")
    # def test_input_name(self, input):
    #     game = Game()
    #     self.assertEqual(game.create_player(), "You entered name.")

    # @patch("dice_game.Game", returned_name="NO name!")
    # def test_NOT_input_name(self, input):
    #     game = Game()
    #     self.assertEqual(game.create_player(), "You did not enter a namw!")

    def test_switcher(self):
        game = Game()

        if (game.get_computer_controler() and
                game.get_playing_now == game.player1):

            self.assertEqual(game.get_playing_now().get_name(),
                             game.computer_player.get_name())

        # if (game.get_computer_controler() and
        #         game.get_playing_now.get_name() ==
        #         game.computer_player.get_name()):

        #     self.assertEqual(game.get_playing_now().get_name(),
        #                      game.player1.get_name())

        # if (not game.get_computer_controler() and
        #         game.get_playing_now == game.player1):

        #     self.assertEqual(game.get_playing_now().get_name(),
        #                      game.player2.get_name())

        # self.assertEqual(game.get_playing_now().get_name(),
        #                  game.player1.get_name())






        #     return game.computer_turn()
        #     return game.set_playing_now(game.player2)
        # return game.set_playing_now(game.player1)



    def test_roll(self):
        json = Mock()
        game = Game()
        dice = Dice()
        # true_return = game.console(game.get_playing_now())
        # self.assertTrue(true_return)

        # false_return = game.console(game.get_playing_now())
        # self.assertFalse(false_return)

        returned_bool = dice.get_dice() == 1 or dice.get_dice()  == 6
        # return_true = dice.get_dice() in (1, 2, 3, 4)
        # self.assertTrue(game.console(game.get_playing_now()), return_true)

        # mock = Mock(side_effect=KeyError(1, 6))
        # self.assertFalse(game.console(game.get_playing_now()), mock)

        # mock1 = Mock(side_effect=(1,6))
        # self.assert_(game.console(game.get_playing_now()), mock1)

        # mock_false = Mock(return_value=False)
        # self.assertFalse(game.console(game.get_playing_now()), mock_false)
        # if returned_bool and game.get_game_status():
        #     game.switcher()
        # self.assertFalse(returned_bool)
        # false_trurn = (1, 6)
        # exp = dice.get_dice() 
        self.assertFalse(game.console(game.get_playing_now()), (1,6))
        self.assertTrue(game.console(game.get_playing_now()), (2,3,4,5))
        # self.assertTrue(game.console(game.playing_now(), ))
        # self.assertTrue(exp)

        # if not exp:
        #     json.method_calls(game.switch())



        
if __name__ == '__main__':
    unittest.game()
