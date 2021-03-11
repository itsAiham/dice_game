#!/usr/bin/env make


into:
	@echo "Welcome!"
	#test
	@echo "coverage"
	@echo "html"
	# Code cleaner
	@echo "flake8"
	@echo "coverage"
	@echo "pylint"
	@echo "test"
	#Doc
	@echo "pdoc"
	#uml
	@echo "uml"
	@echo "game"

run:
	$(PYTHON) main.py


coverage:
	coverage run -m unittest discover . "test_*.py"
	coverage report -m

html:
	coverage html

flake8:
	flake8
	
pylint:
	pylint *.py

test: flake8 pylint



pdoc:
	rm -rf doc/pdoc
	pdoc --html -o doc/pdoc .

uml:
	pyreverse *.py
	pyreverse -o png -p pyreverse *.py

game:
	pyreverse game.py
	pyreverse -o png -p pyreverse game.py




# irst 
# Cd dice_game
# python3 -m venv .venv
# . .venv/bin/activate
# pip3 install mesa(just pip for you)
# pip3 install conda(pip for you)
# pip3 install graphviz(if it doesn't work)
# brew install graphviz 
# Then cd dice_game
#  pyreverse -o png -p Pyreverse /Users/Aiham/dice_game/dice_game
# And that's it my friend
# write me the command on how to make requirements