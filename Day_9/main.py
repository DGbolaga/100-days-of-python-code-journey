############# Topic: Dictionaries and Nesting ##############
# Day 9 project: Blind Auction

import os

def clear():
    os.system('cls')

from art import logo
print(logo)

print("Welcome to the auction program")
bid = {}
is_last_bidder = False

def find_the_highest_bidder(record):
    highest_price = 0
    winner = ""
    highest_bidder_amount = ""
    #bid = {"Victor": 234, "favour": 225,}
    for bidder in record:
        highest_bidder_amount = record[bidder]
        if highest_bidder_amount > highest_price:
            highest_price = highest_bidder_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of {highest_price}")
        


while is_last_bidder == False:
    name = input("What is your name? \n" )
    price = int(input("What's your bid? \n$"))
    bid[name] = price
    are_you_last_bidder = input("Are you the last bidder? Type 'yes' or 'no' \n")
    if are_you_last_bidder == "yes":
        is_last_bidder = True
        find_the_highest_bidder(bid)
    else:
        clear()
