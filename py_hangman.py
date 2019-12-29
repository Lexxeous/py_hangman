#!/usr/local/bin/python3
# coding: utf-8

"""
Title: py_hangman.py
Author(s): Jonathan A. Gibson
Description:
  1.
Goals:
  1. Remove the printing of the word array and the phrase.
  2. Store previous guesses so that the player is not punished twice for guessing the same wrong character twice, and print thier guesses with the scaffold.
  3. Give an option between picking between a random list of words from a file, or just inputting a word manually (like if there were gunna be 2 or more players).
  4. Allow for the guessable phrase to be more than one word separated by spaces (do not allow special characters or numbers, only alpha).
  5. Make the text file an optional input.
  6. If no input file is given, default to the manual input. Otherwise, default to the randomized pick from the list.
Notes:
  > Need to specify the use of the second (optional text file) parameter for myself and for the user.
"""

#--------------------------------------------- Import Necessary Libraries --------------------------------------------#

import sys
import math
import random
import py_hangman_utils as phu

#--------------------------------------------- Import Necessary Libraries --------------------------------------------#

def main():
  winner = False
  state = 0
  losing_state = 6
  places = ""
  guesses = list()

  print("\nProgram Name:", sys.argv[0])
  print("Number of command line arguments:", len(sys.argv))
  print("The command line argument(s) are:", str(sys.argv))

  print("\nWelcome to the game of HANGMAN!!!")

  # This will initialize a 2 or more player game
  if(len(sys.argv) == 1):
    print("Player 1, please provide a word or phrase for Player 2 to guess.")
    print("The word or phrase must not contain special characters or numbers but can be separated with spaces.\n")
    phrase = input("Word or phrase to guess: ").upper()
    l = len(phrase)
    sys.stdout.write("\033[F" + '*'*(math.floor(l/2)) + "HANGMAN WORD OR PHRASE HAS BEEN SUBMITTED" + '*'*(math.floor(l/2)) + '\n')

  # This will initialize a 1 player game
  if(len(sys.argv) == 2):
    # Put all the words from the text file into a single array
    word_arr = [line.rstrip('\n') for line in open(sys.argv[1])]

    # Generate random index and get the word from that index in lowercase
    random_idx = random.randint(0, len(word_arr) - 1)
    phrase = word_arr[random_idx].upper()
    print(phrase)

  # Create a string of the same lenth of <phrase> out of just '_' for the <working> string
  for i in range(0, len(phrase)):
    if(phrase[i].isalpha()): places += '_'
    else: places += ' '

  while(winner == False and state != losing_state):
    phu.draw_hangman(state) # draw the current state of the game after every guess
    print("Current progress:", places) # print the player's current progress

    # Print the list of previous guesses
    print("Previous Guesses: ", end="")
    if(len(guesses) > 0):
      for j in range(0, len(guesses)):
        print(guesses[j], end="")
        if j == len(guesses): break
        print(',', end=" ")
    
    cur_char = input("\nGuess a character: ").upper() # get a character guess as input from the user

    # Validate user input
    if(cur_char.isalpha() == False or len(cur_char) != 1): # if not a valid character
      print("\"" + cur_char + "\"", "is not a valid alphabet character. Try again.")
      continue
    else: # a valid character
      if(cur_char in guesses): # if have guessed already
        print("You have already guessed \"" + cur_char + "\". Try again.")
        continue
      else:
        guesses.append(cur_char)

    # Collect potential progression tuple
    success_bool, phrase, places = phu.replace_all(phrase, places, cur_char)

    # If no characters were found that matched the guess
    if(success_bool == False):
      state += 1 # if this gets incremented to 6, this will force the program out of the loop

    # If all the underscores in <places> have been replaced with correct guesses
    if(phu.blanks_gone(places)):
      winner = True # this will force the program out of the while loop


  # Outside the main "while" loop
  phu.draw_hangman(state)

  if(winner == True):
    print("The phrase was \"" + places + "\".")
    print("CONGRATS! YOU WIN!")
  else:
    print("Sorry, You Lose...")
    

main() # call the main function

    
#---------------------------------------------------------------------------------------------------------------------#
