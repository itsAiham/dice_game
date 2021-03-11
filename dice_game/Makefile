#!/usr/bin/env make


intro:
	@echo "Welcome!"
	@echo "The following are the commands you can enter after 'make'"
	@echo " "
	@echo "unittest :"
	@echo "		coverage"
	@echo "		html"
	@echo "clean code :"
	@echo "		flake8"
	@echo "		pylint"
	@echo "		test"
	@echo "Documentation :"
	@echo "		pdoc"
	@echo "UML :"
	@echo "		uml"
	@echo "		game"


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
	rm -rf scr="classes.png"
	pdoc --html -o "packages.png" .

uml:
	pyreverse *.py
	pyreverse -o png -p pyreverse *.py

game:
	pyreverse game.py
	pyreverse -o png -p pyreverse game.py
