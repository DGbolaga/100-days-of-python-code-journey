########### Topic: Scope ####################
# Day 12 project: Number Guessing Game.

import random
import os
from art import logo

def clear():
  os.system('cls')


def game():
  """introduces the guessing game and contains the logic to run it."""
  
  #create a function that returns a random card from 1 to 100
  def random_number():
    """returns are random integer from 1 to 100, both inclusive."""
    num = random.randint(1, 100)
    return num
  
  print(logo)
  print("Welcome to Guessing the Number!")
  print(" I'm thinking of a number between 1 and 100")
  
  computer_guess = random_number()
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  #difficulty level.
  if difficulty == 'easy':
    attempts = 10
  else:
    attempts = 5
  
  new_attempts = attempts
  while True: 
    
    print(f"You have {new_attempts} attempts remaining to guess the number.")
    
    #ask the user to make a guess.
    user_guess = int(input("Make a guess: "))
  
    #Conditions for win and lose.
    if user_guess > computer_guess:
      print(" Too high.")
      new_attempts -= 1
      #check if the user has used up the 5 attempts.
      if new_attempts == 0:
        print("You have run out of attempt. You lose.")
        break
      print(" Guess again")
      
    elif user_guess < computer_guess:
      print(" Too low.")
      new_attempts -= 1
      if new_attempts == 0:
        print("You have run out of attempt. You lose.")
        break
      print(" Guess again")
      
    else:
      print(f"You got it! The answer was {computer_guess}")
      break

#this allows the game to restart if user wants to play again.
def play_again():
  """runs the number guessing game from start to finish ones, then restarts if user wants to play again."""
  while True:
    game()
    if input("Do you want to play again? Type 'y' or 'n' ") == 'n':
      print("Goodbye.")
      break
    #else keep playing till the user types n, but first clear the screen.
    else:
      clear()


play_again()