# pylint: disable=missing-module-docstring


class Highscore():
    """Highscore Class."""

    def __init__(self, player1, player2):
        """."""
        self.player1 = player1
        self.player2 = player2

    def write_file(self):
        """Write highscores in file."""
        try:
            # The following variables to pass Flake8
            name1 = self.player1.get_name().capitalize()
            score1 = str(self.player1.get_score())
            name2 = self.player2.get_name().capitalize()
            score2 = str(self.player2.get_score())

            with open('score.txt', 'a') as score_file:
                score_file.write("player name: " + name1 +
                                 " (score) -> " + score1 + '\n')
                score_file.write("player name: " + name2 +
                                 " (score) -> " + score2 + '\n')
        except FileNotFoundError:
            print("System can not add player game to the score list!!")
        except IOError:
            print("File problem!")

    @staticmethod
    def read_file():
        """Read highscore file."""
        try:
            print("\n>>>>>   Score lise :\n")
            with open('score.txt', 'r') as score_file:
                read_lines = score_file.readline().strip('\n')
                while read_lines != '':
                    print(read_lines)
                    print("PLAYED AGAINST : ")
                    second_line = score_file.readline().strip('\n')
                    print(second_line)
                    print("\t____________\n")
                    read_lines = score_file.readline().strip('\n')
                print()
        except FileNotFoundError:
            print("System could not find the highscore file!!")
