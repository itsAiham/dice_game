"""."""

# pylint: disable=missing-module-docstring


class Highscore():
    """Highscore Class."""

    def __init__(self, player1, player2):
        """."""
        self.player1 = player1
        self.player2 = player2

    def write_file(self):
        """Write highscores in file."""
        with open('score.txt', 'a') as score_file:
            score_file.write("player name: " + self.player1.get_name()
                             .capitalize() +
                             " (score) -> " + str(self.player1.get_score())
                             + '\n')
            score_file.write("player name: " + self.player2.get_name()
                             .capitalize() +
                             " (score) -> " + str(self.player2.get_score()) +
                             '\n')

    def read_file(self):
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
        except IOError:
            print("File problem!")
        except FileNotFoundError:
            print("No file")
        except FileExistsError:
            print("existense error")
