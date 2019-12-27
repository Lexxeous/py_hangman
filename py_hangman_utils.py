#!/usr/local/bin/python3
# coding: utf-8

#--------------------------------------------- Import Necessary Libraries --------------------------------------------#



#-------------------------------------------------- Global Variables -------------------------------------------------#



#---------------------------------------------- Utilities Implementation ---------------------------------------------#

def draw_hang_loser():
  print(" _________    ")
  print("|         |   ")
  print("|         0   ")
  print("|        /|\  ")
  print("|        / \  ")
  print("|             ")
  print("|             ")


def draw_hang_head_body_legs_la():
  print(" _________    ")
  print("|         |   ")
  print("|         0   ")
  print("|         |\  ")
  print("|        / \  ")
  print("|             ")
  print("|             ")


def draw_hang_head_body_legs():
  print(" _________    ")
  print("|         |   ")
  print("|         0   ")
  print("|         |   ")
  print("|        / \  ")
  print("|             ")
  print("|             ")


def draw_hang_head_body_ll():
  print(" _________    ")
  print("|         |   ")
  print("|         0   ")
  print("|         |   ")
  print("|          \  ")
  print("|             ")
  print("|             ")


def draw_hang_head_body():
  print(" _________    ")
  print("|         |   ")
  print("|         0   ")
  print("|         |   ")
  print("|             ")
  print("|             ")
  print("|             ")


def draw_hang_head():
  print(" _________    ")
  print("|         |   ")
  print("|         0   ")
  print("|             ")
  print("|             ")
  print("|             ")
  print("|             ")


def draw_hang_scaffold():
  print(" _________    ")
  print("|         |   ")
  print("|             ")
  print("|             ")
  print("|             ")
  print("|             ")
  print("|             ")


def draw_hangman(state):
  if state == 0:
      draw_hang_scaffold()
  elif state == 1:
      draw_hang_head()
  elif state == 2:
      draw_hang_head_body()
  elif state == 3:
      draw_hang_head_body_ll()
  elif state == 4:
      draw_hang_head_body_legs()
  elif state == 5:
     draw_hang_head_body_legs_la()
  elif state == 6:
      draw_hang_loser()
        
        
def blanks_gone(s):
  if(s.find('_') == -1):
    return True
  else:
    return False


def replace_all(orig, working, ch):
  done = False
  count = 0
  while not done:
    idx = orig.find(ch) # returns the index of the first occurence of <ch> in <orig>
    if idx != -1: # if found
      count = count + 1 # increment the amount of <ch> that was found
      orig = orig[:idx] + "_" + orig[idx+1:] # replace that index with a '_' in the original string
      working = working[:idx] + ch + working[idx+1:] # replace that index with <ch> in the working string
    else: # if not found
      done = True
  return count != 0, orig, working # returns the number of <ch> found in <orig>, the modified original string, and the modified working string

#---------------------------------------------------------------------------------------------------------------------#
