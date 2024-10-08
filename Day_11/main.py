############## Capstone Project: Blackjack game ###################

from art import logo
import random
import os


def clear():
  os.system('cls')

#random_card generator.
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#calculate_score() takes a List of cards as input and returns the score.
def calculate_score(card_list):
  # Early win checks. 0 represents Blackjack.
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0
  #Early win checks. 
  if 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)

#Win metrics
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "It's a draw🙃"
  elif computer_score == 0:
    return "Opponent has blackjack. You Lose 😭"
  elif user_score == 0:
    return "Blackjack, You win.😎"
  elif user_score > 21:
    return "You went over. You Lose 😥"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  
  print(logo)
  
  #Game logic: first, Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  #The score is rechecked with every new card drawn and the checks need to be repeated until the game ends.
  while not is_game_over:
    #Call calculate_score(). Game logic: If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your card: {user_cards}, current_score {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
  
    if user_score == 0 or computer_score == 0 or  user_score > 21:
      is_game_over = True
    else:
      # Game logic: If the game has not ended, ask the user if they want to draw another card. If yes, use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      wants_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if wants_card == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  #User's turn is over, it's time to let the computer play. Game logic: The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  #Show the results of the user and computer, and identify the winner.
  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
 
#Ask the user if they want to restart the game. If they answer yes, the console clears and a new game of blackjack is started. 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()