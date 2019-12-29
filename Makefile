words ?= words.txt

run1:
	python3 py_hangman.py $(words) # default for 1 player

run2:
	python3 py_hangman.py # default for 2 or more players