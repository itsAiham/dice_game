coverage:
	coverage run -m unittest discover test "test_*.py"
	coverage report -m



clean:
	rm -rf app/.coverage *.pyc

	rm -rf test/.coverage *.pyc
	rm -rf test/__pycache__
