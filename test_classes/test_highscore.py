# https://stackoverflow.com/questions/18762293/how-to-test-that-a-function-is-called-within-a-function-with-nosetests


import unittest
from dice_game.player import Player
from dice_game.game import Game
from dice_game.highscore import Highscore


class TestHigscore(unittest.TestCase):
    """Test Higscore Class."""

    def setUp(self):
        self.game = Game()
        self.player1 = Player("name1", 5)
        self.player2 = Player("name2", 10)



    
    # def test__init__(self):

    #     self.highscore = Highscore(self.game.player1, self.game.player2)

    # def test_write_file(self):
    # #     self.assertEqual(self.player1.get_name(), self.game.score.name1)


    #     self.game = Game()
    #     with self.assertRaises(FileNotFoundError):
    #         self.game.highscore1()

