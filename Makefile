
# Change this to be your variant of the python command

# PYTHON = python3
PYTHON = python
#PYTHON = py



venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"



install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


clean:
	rm -rf app/.coverage *.pyc
	rm -rf app/__pycache__
	rm -rf test/.coverage *.pyc
	rm -rf test/__pycache__
	rm -rf .coverage
	rm -rf classes.dot



clean-doc:
	rm -rf doc

clean-all: clean clean-doc
	rm -rf .venv
	rm -rf htmlcov/


# Code unit-tests and linter
unittest:
	 $(PYTHON) -m unittest discover test "*_test.py"


coverage:
	coverage run -m unittest discover test/ "test_*.py"
	coverage report -m

coverage-html:
	coverage html

pylint:
	cd app/ && pylint *.py
	cd test/ && pylint *.py

flake8:
	flake8

lint: flake8 pylint

test: lint coverage


# docs
pydoc:
	install -d doc/pydoc
	$(PYTHON) -m pydoc -w "$(PWD)"
	mv *.html doc/pydoc

pdoc:
	rm -rf doc/pdoc
	pdoc --html -o doc/pdoc .

doc: pdoc pyreverse #pydoc sphinx

pyreverse:
	install -d doc/pyreverse
	pyreverse *.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot
	ls -l doc/pyreverse



# Complexity measurement
radon-cc:
	radon cc . -a

radon-mi:
	radon mi .

radon-raw:
	radon raw .

radon-hal:
	radon hal .

bandit: bandit-app bandit-test

bandit-app:
	bandit -r app/

bandit-test:
	bandit -r test/
