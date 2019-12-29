# <img src=".pics/lexx_headshot_clear.png" width="100px"/> Lexxeous's Python Hangman: <img src=".pics/hangman.png" width="100px"/>

### Summary
This program is a simple game that is compatible with `Python3`. The game supports play for 1 and 2 or more players. A text file (`words.txt`) is provided by default as a makeshift database for words and phrases that a user may need to guess. <br><br>

If the user provides a text file as the second argument for this program, by default, the game will assume that there will only be 1 player, choose a word or phrase at random from the file, and have the user try to guess the word or phrase. If the user does not provide a text file as the second argument for this program, by default, the game will assume that there will be 2 or more players participating, prompt 1 player to input a secret word or phrase, then prompt the rest of the players to guess. The guessers must guess the correct word or phrase within 6 guesses to win.

### Instructions
The `Makefile` contains two commands that are useful for default play. By running `make run1`, the game will automatically import the default text file (`words.txt`) and continue the game for 1 player. The input file can be changed by manually running the command with a differnt filename or by simply changing the filename provided in the `Makefile`. By running `make run2`, the game will automatically start the game without importing any text file and continue the game for 2 or more players.

### Disclaimers
The words and phrases provided in `words.txt` are all alpha based (no special characters or numbers), separated by spaces (if there is more than one word per line), and each line is ended with a newline character (`\n`).

### Features
When playing with 2 or more players, the secret input phrase is hidden after it is submitted, so that other game participants cannot cheat. The game also keeps a log of the previous guesses for the current game so that guessers are not punished for guessing the same letter twice.