################ Topic: Randomisation and Python List ###################
# Day 4 project: Rock, Paper Scissors Game.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random 

print("Welcome to the Rock, Paper, Scissors game! \n What do you choose?\n Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid choice. Try again. Please choose 0, 1, or 2.")
    


if user_choice == 0 or user_choice == 1 or user_choice == 2:
    print("Computer chose:")
    possible_computer_choice = [rock, paper, scissors]
    the_random_index = random.randint(0, len(possible_computer_choice)-1)
    computer_choice = possible_computer_choice[the_random_index]

    if computer_choice == rock:
        print(rock)
    elif computer_choice == paper:
        print(paper)
    else:
        print(scissors)
    
    if user_choice == 0 and computer_choice == rock:
        print("It's a draw.")
    elif user_choice == 0 and computer_choice == paper:
        print("You lose.")
    elif user_choice == 0 and computer_choice == scissors:
        print("You win.")
    elif user_choice == 1 and computer_choice == rock:
        print("You win.")
    elif user_choice == 1 and computer_choice == paper:
        print("It's a draw")
    elif user_choice == 1 and computer_choice == scissors:
        print("You lose.")
    elif user_choice == 2 and computer_choice == rock:
        print("You lose.")
    elif user_choice == 2 and computer_choice == paper:
        print("You win.")
    else:
        print("Its a draw.")

    

