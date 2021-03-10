


venv:
	@printf "Welcomce in make File!"

coverage:
	coverage run -m unittest discover . "test_*.py"
	coverage report -m

html:
	coverage html

pylint:
	pylint main.py
	pylint game.py
	pylint dice.py
	pylint histogram.py
	pylint highscore.py
	pylint player.py
	pylint shell.py
	pylint test_dice.py
	pylint test_game.py
	pylint test_highscore.py
	pylint test_histogram.py
	pylint test_intelligence.py
	pylint test_player.py


flake8:
	flake8

test: flake8 pylint

